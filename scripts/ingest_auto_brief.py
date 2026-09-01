#!/usr/bin/env python3
import argparse, html, json, subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PUBS=ROOT/'publishing/publications.json'
SERIES=ROOT/'publishing/series.json'
SITE=ROOT/'site'
RECEIPTS=ROOT/'publication/auto-receipts'
BASE='https://signaetstructura.com'
JST=timezone(timedelta(hours=9))

def load(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def h(s): return html.escape(str(s),quote=True)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('brief')
    ap.add_argument('--source-repo',required=True)
    ap.add_argument('--source-sha',required=True)
    ap.add_argument('--source-path',required=True)
    ap.add_argument('--shadow',action='store_true')
    ap.add_argument('--now',help='override validation clock for deterministic tests only')
    args=ap.parse_args()

    validate_cmd=['python3',str(ROOT/'scripts/validate_auto_brief.py'),args.brief]
    if args.now: validate_cmd += ['--now',args.now]
    subprocess.run(validate_cmd,check=True)
    brief=load(args.brief)
    pubsdoc=load(PUBS); pubs=pubsdoc['publications']
    if any(x['publication_id']==brief['publication_id'] and x['language']==brief['language'] for x in pubs): raise SystemExit('duplicate publication_id/language')
    if any(x.get('source_observation_id')==brief['source_observation_id'] for x in pubs): raise SystemExit('duplicate source_observation_id')

    series_map={x['series_id']:x for x in load(SERIES)['series']}
    sd=series_map[brief['series_id']]
    lang=brief['language']; ja=lang=='ja'; slug=brief['slug']
    out=SITE/lang/'research'/slug
    if out.exists(): raise SystemExit('article path already exists')
    out.mkdir(parents=True,exist_ok=True)

    evidence=''.join(f'<li><a href="{h(e["source_url"])}">{h(e["source_name"])}</a> — {h(e["fact"])} <span class="meta">{h(e["observed_at"])}</span></li>' for e in brief['evidence'])
    title=brief['title']; series_title=sd['title_ja' if ja else 'title_en']
    labels={'watch':'市場観測' if ja else 'Market Watch','changed':'何が変わったか' if ja else 'What changed','why':'なぜ重要か' if ja else 'Why it matters','evidence':'根拠' if ja else 'Evidence','limits':'留保' if ja else 'Limitations','disclosure':'開示' if ja else 'Disclosure','home':'トップ' if ja else 'Home','research':'リサーチ' if ja else 'Research'}
    noindex='<meta name="robots" content="noindex,nofollow">' if args.shadow else ''
    body=f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">{noindex}<title>{h(title)} | SIGNA ET STRUCTURA</title><meta name="description" content="{h(brief['summary'])}"><link rel="canonical" href="{BASE}/{lang}/research/{h(slug)}/"><link rel="stylesheet" href="../../../assets/site.css"></head><body><header class="masthead"><div class="wrap"><a class="brand" href="../../../{lang}/">SIGNA ET STRUCTURA</a><div class="strap">{h(labels['watch'])}</div></div></header><nav class="wrap nav"><a href="../">{h(labels['research'])}</a><a href="../../../{lang}/market-watch/">{h(labels['watch'])}</a><span class="nav-spacer"></span><a href="../../../{lang}/">{h(labels['home'])}</a></nav><main><article class="article"><header class="article-head"><div class="eyebrow">{h(labels['watch'])} · {h(series_title)}</div><h1>{h(title)}</h1><p class="dek">{h(brief['summary'])}</p><div class="article-meta"><span>{h(brief['observed_at'])}</span><span>{h(brief['series_id'])}</span></div></header><section class="article-grid"><div class="article-body"><h2>{h(labels['changed'])}</h2><p>{h(brief['what_changed'])}</p><h2>{h(labels['why'])}</h2><p>{h(brief['why_it_matters'])}</p><h2>{h(labels['evidence'])}</h2><ul>{evidence}</ul><h2>{h(labels['limits'])}</h2><p>{h(brief['limitations'])}</p><h2>{h(labels['disclosure'])}</h2><p>{h(brief['disclosure'])}</p></div></section></article></main></body></html>'''
    (out/'index.html').write_text(body,encoding='utf-8')

    published_at=brief['observed_at']
    entry={'publication_id':brief['publication_id'],'language':lang,'edition':'automatic-market-watch','slug':slug,'title':title,'summary':brief['summary'],'content_type':'market_watch','content_type_label':labels['watch'],'themes':[],'series':brief['series_id'],'published_at':published_at,'updated_at':published_at,'as_of':brief['as_of'],'status':'published','article_path':f'site/{lang}/research/{slug}/index.html','url':f'{BASE}/{lang}/research/{slug}/','hero_figure':None,'related_publications':[],'homepage':{'eligible':True,'priority':20,'lead_candidate':False},'source_observation_id':brief['source_observation_id'],'auto_publish_profile':brief['auto_publish_profile']}
    pubs.append(entry); pubsdoc['updated_at_jst']=datetime.now(JST).strftime('%Y-%m-%d %H:%M JST')
    PUBS.write_text(json.dumps(pubsdoc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

    RECEIPTS.mkdir(parents=True,exist_ok=True)
    receipt={'schema_version':'signa-auto-publication-receipt-v0.1','publication_id':brief['publication_id'],'series_id':brief['series_id'],'source_observation_id':brief['source_observation_id'],'source_repo':args.source_repo,'source_sha':args.source_sha,'source_path':args.source_path,'validation_profile':brief['auto_publish_profile'],'shadow':bool(args.shadow),'production_url':entry['url'] if not args.shadow else None}
    (RECEIPTS/f"{brief['publication_id']}.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'publication_id':brief['publication_id'],'article_path':entry['article_path'],'shadow':args.shadow},ensure_ascii=False))

if __name__=='__main__': main()
