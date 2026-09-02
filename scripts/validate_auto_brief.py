#!/usr/bin/env python3
import argparse,json,re
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[1]; PROFILES=ROOT/'publishing/auto-series-profiles.json'; SERIES=ROOT/'publishing/series.json'
SECRET_PATTERNS=[re.compile(r'BEGIN (?:RSA|OPENSSH|EC) PRIVATE KEY',re.I),re.compile(r'\b(?:api[_-]?key|private[_-]?key|seed phrase|bearer token)\b\s*[:=]',re.I)]
INTERNAL_FIELD_NAMES={'portfolio','portfolio_id','intent','intent_id','real_intent','paper_intent','entry','entry_price','position_size','size','take_profit','stop_loss','exit','execution_mode','approval_record','private_evidence','internal_rating','real_money_rating'}
DIRECTIVE_PATTERNS=[re.compile(r'\bBUY\b',re.I),re.compile(r'\bSELL\b',re.I),re.compile(r'買(?:い|う|え)',re.I),re.compile(r'売(?:り|る|れ)',re.I),re.compile(r'エントリー',re.I),re.compile(r'利確',re.I),re.compile(r'損切',re.I),re.compile(r'実弾評価',re.I),re.compile(r'現段階では追いかけない',re.I)]
SLUG_RX=re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
def load(p): return json.loads(p.read_text(encoding='utf-8'))
def parse_iso(v,f):
    try: dt=datetime.fromisoformat(v)
    except Exception as e: raise ValueError(f'invalid {f}: {v}') from e
    if dt.tzinfo is None: raise ValueError(f'{f} must include timezone offset')
    return dt
def validate_url(v):
    u=urlparse(v); return u.scheme in ('http','https') and bool(u.netloc)
def walk_keys(o):
    if isinstance(o,dict):
        for k,v in o.items(): yield k; yield from walk_keys(v)
    elif isinstance(o,list):
        for v in o: yield from walk_keys(v)
def all_text(o):
    out=[]
    if isinstance(o,dict):
        for v in o.values(): out.extend(all_text(v))
    elif isinstance(o,list):
        for v in o: out.extend(all_text(v))
    elif isinstance(o,str): out.append(o)
    return out
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('brief'); ap.add_argument('--now'); args=ap.parse_args(); brief=load(Path(args.brief)); pd=load(PROFILES); sd=load(SERIES); errors=[]
    req=['schema_version','publication_id','series_id','observed_at','as_of','language','slug','title','summary','what_changed','why_it_matters','evidence','limitations','disclosure','auto_publish_profile','claim_type','source_observation_id']
    for k in req:
        if k not in brief or brief[k] in (None,'',[]): errors.append(f'missing required field: {k}')
    if brief.get('schema_version')!='signa-auto-brief-v0.1': errors.append('unsupported schema_version')
    if brief.get('slug') and not SLUG_RX.match(brief['slug']): errors.append('slug must be lowercase kebab-case')
    profiles={x['profile_id']:x for x in pd.get('profiles',[])}; p=profiles.get(brief.get('auto_publish_profile'))
    if not p: errors.append('auto_publish_profile is not approved')
    else:
        if not p.get('enabled'): errors.append('auto_publish_profile is disabled')
        if p.get('series_id')!=brief.get('series_id'): errors.append('series_id does not match profile')
        if brief.get('language') not in p.get('languages',[]): errors.append('language is not allowed by profile')
        if brief.get('claim_type') not in p.get('allowed_claim_types',[]): errors.append('claim_type is not allowed by profile')
        for field,lim in [('title','max_title_chars'),('summary','max_summary_chars'),('what_changed','max_what_changed_chars'),('why_it_matters','max_why_it_matters_chars'),('limitations','max_limitations_chars')]:
            n=p.get(lim)
            if n and isinstance(brief.get(field),str) and len(brief[field])>n: errors.append(f'{field} exceeds {lim}')
        if p.get('require_disclosure') and not brief.get('disclosure'): errors.append('disclosure required')
        templates=p.get('public_disclosure_templates')
        expected=templates.get(brief.get('language')) if isinstance(templates,dict) else p.get('public_disclosure_template')
        if expected and brief.get('disclosure')!=expected: errors.append('disclosure does not match approved template')
        for term in p.get('prohibited_terms_case_insensitive',[]):
            for text in all_text(brief):
                if term.casefold() in text.casefold(): errors.append(f'prohibited term: {term}')
    if brief.get('series_id') not in {x['series_id'] for x in sd.get('series',[])}: errors.append('series_id is not registered')
    try:
        observed=parse_iso(brief.get('observed_at',''),'observed_at'); asof=parse_iso(brief.get('as_of',''),'as_of'); now=parse_iso(args.now,'now') if args.now else datetime.now(timezone.utc)
        if asof>now or observed>now: errors.append('future timestamps are not allowed')
        if p:
            age=(now-observed.astimezone(timezone.utc)).total_seconds()/60
            if age<0 or age>p.get('max_age_minutes',0): errors.append('brief exceeds profile freshness window')
    except ValueError as e: errors.append(str(e))
    evidence=brief.get('evidence',[]) if isinstance(brief.get('evidence'),list) else []
    if p and len(evidence)<p.get('min_evidence_items',1): errors.append('not enough evidence items')
    for i,item in enumerate(evidence):
        for k in ('source_name','observed_at','fact'):
            if not item.get(k): errors.append(f'evidence[{i}] missing {k}')
        if p and p.get('require_source_url') and (not item.get('source_url') or not validate_url(item.get('source_url',''))): errors.append(f'evidence[{i}] requires valid public source_url')
        try: parse_iso(item.get('observed_at',''),f'evidence[{i}].observed_at')
        except ValueError as e: errors.append(str(e))
    bad=sorted(set(walk_keys(brief))&INTERNAL_FIELD_NAMES)
    if bad: errors.append('internal-only fields present: '+', '.join(bad))
    for text in all_text(brief):
        for rx in SECRET_PATTERNS:
            if rx.search(text): errors.append('secret-like content detected')
        for rx in DIRECTIVE_PATTERNS:
            if rx.search(text): errors.append('trading directive-like language detected')
    if pd.get('global_kill_switch'): errors.append('global auto-publication kill switch is active')
    if errors:
        print('AUTO BRIEF REJECTED'); [print(f'- {e}') for e in sorted(set(errors))]; raise SystemExit(1)
    print('AUTO BRIEF VALID'); print(json.dumps({'publication_id':brief['publication_id'],'series_id':brief['series_id'],'profile_id':brief['auto_publish_profile'],'production_auto_publish':bool(p.get('production_auto_publish'))},ensure_ascii=False))
if __name__=='__main__': main()
