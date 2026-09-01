#!/usr/bin/env python3
import argparse, html, json
from collections import Counter
from datetime import datetime
from pathlib import Path
from xml.sax.saxutils import escape

ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'site'
BASE='https://signaetstructura.com'

def load(path): return json.loads((ROOT/path).read_text(encoding='utf-8'))
def h(v): return html.escape(str(v), quote=True)
def published(items, lang):
    return sorted([x for x in items if x['language']==lang and x['status']=='published'], key=lambda x:(x['published_at'],x['homepage']['priority']), reverse=True)
def rel_url(x): return f"research/{x['slug']}/"
def figure_map(figs): return {x['figure_id']:x for x in figs}

def validate(pubs, figs):
    errors=[]; seen=set(); slugs=set(); ids={x['publication_id'] for x in pubs}
    fmap=figure_map(figs)
    for x in pubs:
        key=(x['publication_id'],x['language'])
        if key in seen: errors.append(f'duplicate edition: {key}')
        seen.add(key)
        sk=(x['language'],x['slug'])
        if sk in slugs: errors.append(f'slug collision: {sk}')
        slugs.add(sk)
        if x['language'] not in ('ja','en'): errors.append(f"bad language: {x['language']}")
        try: datetime.fromisoformat(x['published_at'])
        except Exception: errors.append(f"bad published_at: {key}")
        if not (ROOT/x['article_path']).exists(): errors.append(f"missing article: {x['article_path']}")
        if x.get('hero_figure') and x['hero_figure'] not in fmap: errors.append(f"missing hero figure: {x['hero_figure']}")
        for rid in x.get('related_publications',[]):
            if rid not in ids: errors.append(f"broken related publication: {rid}")
    for f in figs:
        if f['publication_id'] not in ids: errors.append(f"figure publication missing: {f['figure_id']}")
        if not (ROOT/f['svg_path']).exists(): errors.append(f"missing figure file: {f['svg_path']}")
    if errors: raise SystemExit('\n'.join(errors))

def validate_series(series_defs):
    errors=[]; seen=set()
    for s in series_defs:
        sid=s.get('series_id')
        if not sid: errors.append('series_id missing'); continue
        if sid in seen: errors.append(f'duplicate series_id: {sid}')
        seen.add(sid)
        if s.get('section')!='market-watch': errors.append(f'unsupported series section: {sid}')
        for key in ('title_ja','title_en','dek_ja','dek_en','method_ja','method_en'):
            if not s.get(key): errors.append(f'missing {key}: {sid}')
    if errors: raise SystemExit('\n'.join(errors))

def theme_label(k,lang):
    labels={'market-structure':('市場構造','Market Structure'),'stablecoins':('ステーブルコイン','Stablecoins'),'defi':('DeFi','DeFi'),'liquidity':('流動性','Liquidity'),'sns':('SNS・注目','SNS / Attention'),'historical-markets':('過去市場','Historical Markets')}
    return labels.get(k,(k,k))[0 if lang=='ja' else 1]

def top_themes(items):
    c=Counter(t for x in items for t in x.get('themes',[])); return [k for k,_ in c.most_common(6)]

def home(lang,items,fmap,preview):
    ja=lang=='ja'; lead=next((x for x in items if x['homepage'].get('lead_candidate')),items[0]); latest=[x for x in items if x is not lead][:4]
    themes=top_themes(items)
    fig=fmap.get(lead.get('hero_figure')); figsrc=''
    if fig: figsrc='../'+fig['svg_path'].removeprefix('site/')
    noindex='<meta name="robots" content="noindex,nofollow">' if preview else ''
    title='SIGNA ET STRUCTURA | 市場リサーチとデータ' if ja else 'SIGNA ET STRUCTURA | Market Research & Data'
    desc='市場の兆候から構造を読む。Smile Company LLCによる市場リサーチとデータ。' if ja else 'Market research and data on signals, structures and evidence, published by Smile Company LLC.'
    top=('市場の兆候から、構造を読む。','兆候 → 構造 → 根拠','発行：Smile Company LLC') if ja else ('Read the structure behind the signals.','Signal → Structure → Evidence','Published by Smile Company LLC')
    strap='市場リサーチとデータ' if ja else 'Market Research & Data'
    nav=['トップ','リサーチ','市場観測','テーマ','過去事例','データ','方法論'] if ja else ['Home','Research','Market Watch','Themes','Case Studies','Data','Methodology']
    intro='SIGNA ET STRUCTURAは、観測可能な市場の兆候を、構造と根拠から読み解くリサーチ媒体です。' if ja else 'SIGNA ET STRUCTURA reads observable market signals through structure and evidence.'
    latest_title='新着' if ja else 'Latest'; themes_title='いま追っているテーマ' if ja else 'Themes We Track'; data_title='データと図表' if ja else 'Data & Figures'
    lead_label='注目のリサーチ' if ja else 'Lead Research'; all_label='すべてのリサーチ' if ja else 'All Research'
    latest_html=''.join(f'<article><div class="eyebrow">{h(x["content_type_label"])}</div><h3><a href="{rel_url(x)}">{h(x["title"])}</a></h3><p>{h(x["summary"])}</p></article>' for x in latest)
    themes_html=''.join(f'<div class="theme-card"><strong>{h(theme_label(t,lang))}</strong><p>{sum(t in x.get("themes",[]) for x in items)} publication(s)</p></div>' for t in themes)
    figs=[f for f in fmap.values() if any(x['publication_id']==f['publication_id'] for x in items)][:4]
    figure_html=''.join(f'<article class="card"><div class="eyebrow">{("図表" if ja else "Figure")}</div><h3>{h(f["title_ja" if ja else "title_en"])}</h3><p>{h(f["as_of"])}</p></article>' for f in figs)
    stylesheet='''<style>.edition-line{font-family:var(--sans);font-size:.75rem;color:var(--ink-soft);padding:.65rem 0;border-bottom:1px solid var(--rule)}.news-lead{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(280px,.65fr);gap:2.5rem;padding:2.2rem 0;border-bottom:1px solid var(--ink)}.news-lead h1{font-size:clamp(2.35rem,4.5vw,4.6rem);line-height:1.02;letter-spacing:-.025em;margin:.45rem 0 1rem}.lead-visual img{width:100%;display:block}.lead-visual{border-top:4px solid var(--ink);padding-top:.7rem}.latest-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:2rem}.latest-list article{padding:1rem 0;border-bottom:1px solid var(--rule)}.latest-list h3{font-size:1.35rem;line-height:1.2;margin:.25rem 0}.theme-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}.theme-card{border-top:3px solid var(--ink);padding:.75rem 0}.compact-block{padding:1.6rem 0;border-top:1px solid var(--ink)}.utility-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:2rem}@media(max-width:800px){.news-lead,.latest-grid{grid-template-columns:1fr}.theme-grid{grid-template-columns:1fr 1fr}.utility-grid{grid-template-columns:1fr}}@media(max-width:560px){.news-lead h1{font-size:2.45rem}.theme-grid{grid-template-columns:1fr}}</style>'''
    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">{noindex}<title>{h(title)}</title><meta name="description" content="{h(desc)}"><link rel="canonical" href="{BASE}/{lang}/"><link rel="alternate" hreflang="ja" href="{BASE}/ja/"><link rel="alternate" hreflang="en" href="{BASE}/en/"><link rel="alternate" type="application/rss+xml" href="{BASE}/{lang}/feed.xml"><link rel="stylesheet" href="../assets/site.css">{stylesheet}</head><body><div class="topline"><div class="wrap topline-inner"><span>{h(top[0])}</span><span>{h(top[1])}</span><span>{h(top[2])}</span></div></div><header class="masthead masthead-centered"><div class="wrap masthead-grid"><div class="mast-language"><a href="../ja/">日本語</a> / <a href="../en/">English</a></div><div><div class="brand">SIGNA ET STRUCTURA</div><div class="strap">{h(strap)}</div></div><div class="mast-search"><a href="research/">{h(all_label)}</a></div></div></header><nav class="wrap nav nav-wide"><a href="./">{h(nav[0])}</a><a href="research/">{h(nav[1])}</a><a href="market-watch/">{h(nav[2])}</a><span>{h(nav[3])}</span><span>{h(nav[4])}</span><span>{h(nav[5])}</span><span class="nav-spacer"></span><a href="methods/">{h(nav[6])}</a></nav><main><div class="wrap edition-line">{h(intro)}</div><section class="wrap news-lead"><article><div class="eyebrow">{h(lead_label)} · {h(lead['content_type_label'])}</div><h1><a href="{rel_url(lead)}">{h(lead['title'])}</a></h1><p class="standfirst">{h(lead['summary'])}</p><div class="article-meta"><span>{'調査時点' if ja else 'Research as of'} {h(lead['as_of'])}</span></div></article><aside class="lead-visual">{f'<img src="{figsrc}" alt="{h(fig["title_ja" if ja else "title_en"])}">' if fig else ''}</aside></section><section class="wrap section latest-grid"><div><div class="section-head"><h2>{h(latest_title)}</h2><a href="research/">{h(all_label)} →</a></div><div class="latest-list">{latest_html}</div></div><aside><div class="section-head"><h2>{h(themes_title)}</h2></div><div class="theme-grid">{themes_html}</div></aside></section>{f'<section class="wrap compact-block"><div class="section-head"><h2>{h(data_title)}</h2></div><div class="grid">{figure_html}</div></section>' if figs else ''}<section class="wrap compact-block utility-grid"><div><h2>{'方法論' if ja else 'Methodology'}</h2><p><a href="methods/">{'調査方法を読む' if ja else 'Read our methodology'} →</a></p></div><div><h2>{'この媒体について' if ja else 'About'}</h2><p><a href="about/">{'詳しく見る' if ja else 'About this publication'} →</a></p></div><div><h2>{'編集' if ja else 'Editorial'}</h2><p><a href="editorial-policy/">{'編集方針' if ja else 'Editorial Policy'} →</a><br><a href="corrections/">{'訂正について' if ja else 'Corrections'} →</a></p></div></section></main><footer class="site-footer"><div class="wrap"><p class="meta">SIGNA ET STRUCTURA · {h(strap)} · Smile Company LLC</p></div></footer></body></html>'''

def research_index(lang,items,preview):
    ja=lang=='ja'; noindex='<meta name="robots" content="noindex,nofollow">' if preview else ''
    cards=''.join(f'<article class="card"><span class="eyebrow">{h(x["content_type_label"])} · {h(x["published_at"][:10])}</span><h3><a href="{h(x["slug"])}/">{h(x["title"])}</a></h3><p>{h(x["summary"])}</p></article>' for x in items)
    title='リサーチ' if ja else 'Research'; top='トップ' if ja else 'Home'; methods='方法論' if ja else 'Methodology'
    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">{noindex}<title>{title} | SIGNA ET STRUCTURA</title><link rel="canonical" href="{BASE}/{lang}/research/"><link rel="alternate" hreflang="ja" href="{BASE}/ja/research/"><link rel="alternate" hreflang="en" href="{BASE}/en/research/"><link rel="alternate" type="application/rss+xml" href="{BASE}/{lang}/feed.xml"><link rel="stylesheet" href="../../assets/site.css"></head><body><header class="masthead"><div class="wrap"><div class="brand"><a href="../">SIGNA ET STRUCTURA</a></div><div class="strap">{title}</div></div></header><nav class="wrap nav"><a href="../">{top}</a><a href="./">{title}</a><a href="../methods/">{methods}</a><span class="nav-spacer"></span><a href="../../{'en' if ja else 'ja'}/research/">{'English' if ja else '日本語'}</a></nav><main class="wrap section"><div class="section-head"><h1>{title}</h1><span class="meta">{len(items)} publications</span></div><div class="grid">{cards}</div></main></body></html>'''

def market_watch_index(lang,items,series_defs,preview):
    ja=lang=='ja'; noindex='<meta name="robots" content="noindex,nofollow">' if preview else ''
    title='市場観測' if ja else 'Market Watch'
    intro='意味のある変化だけを記録する継続観測。変化がない日は更新しません。' if ja else 'Continuing watches that publish only when a material change is observed. No material change means no post.'
    cards=[]
    for sd in series_defs:
        if sd.get('section')!='market-watch': continue
        sid=sd['series_id']; count=sum(x.get('series')==sid for x in items)
        st=sd['title_ja' if ja else 'title_en']; dek=sd['dek_ja' if ja else 'dek_en']
        unit='件' if ja else 'entries'
        cards.append(f'<article class="card"><div class="eyebrow">SERIES · {count} {unit}</div><h3><a href="../series/{h(sid)}/">{h(st)}</a></h3><p>{h(dek)}</p></article>')
    cards_html=''.join(cards) or f'<p>{h("現在公開中の観測シリーズはありません。" if ja else "No watch series are currently published.")}</p>'
    home_label='トップ' if ja else 'Home'; research_label='リサーチ' if ja else 'Research'
    other_lang='en' if ja else 'ja'; other_label='English' if ja else '日本語'
    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">{noindex}<title>{h(title)} | SIGNA ET STRUCTURA</title><meta name="description" content="{h(intro)}"><link rel="canonical" href="{BASE}/{lang}/market-watch/"><link rel="alternate" hreflang="ja" href="{BASE}/ja/market-watch/"><link rel="alternate" hreflang="en" href="{BASE}/en/market-watch/"><link rel="stylesheet" href="../../assets/site.css"></head><body><header class="masthead"><div class="wrap"><div class="brand"><a href="../">SIGNA ET STRUCTURA</a></div><div class="strap">{h(title)}</div></div></header><nav class="wrap nav"><a href="../">{h(home_label)}</a><a href="../research/">{h(research_label)}</a><a href="./">{h(title)}</a><span class="nav-spacer"></span><a href="../../{other_lang}/market-watch/">{h(other_label)}</a></nav><main class="wrap section"><div class="section-head"><div><div class="eyebrow">MARKET WATCH</div><h1>{h(title)}</h1><p class="dek">{h(intro)}</p></div></div><div class="grid">{cards_html}</div></main></body></html>'''

def series_landing(lang,items,sd,preview):
    ja=lang=='ja'; noindex='<meta name="robots" content="noindex,nofollow">' if preview else ''
    sid=sd['series_id']; title=sd['title_ja' if ja else 'title_en']; dek=sd['dek_ja' if ja else 'dek_en']; method=sd['method_ja' if ja else 'method_en']
    entries=[x for x in items if x.get('series')==sid]
    if entries:
        cards=''.join(f'<article class="card"><div class="eyebrow">{h(x["content_type_label"])} · {h(x["published_at"][:10])}</div><h3><a href="../../research/{h(x["slug"])}/">{h(x["title"])}</a></h3><p>{h(x["summary"])}</p></article>' for x in entries)
    else:
        watch_title='観測継続中' if ja else 'Watch active'
        watch_text='意味のある変化が確認できた時だけ、ここに新しい観測記事を追加します。' if ja else 'A new entry will appear here only when a material change is confirmed.'
        cards=f'<article class="card"><div class="eyebrow">WATCHING</div><h3>{h(watch_title)}</h3><p>{h(watch_text)}</p></article>'
    home_label='トップ' if ja else 'Home'; watch_label='市場観測' if ja else 'Market Watch'
    section_title='観測対象' if ja else 'What we watch'; entries_title='更新' if ja else 'Entries'
    rule_label='更新原則' if ja else 'Update rule'; rule='変化がある時だけ掲載' if ja else 'Publish only material change'
    other_lang='en' if ja else 'ja'; other_label='English' if ja else '日本語'
    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">{noindex}<title>{h(title)} | SIGNA ET STRUCTURA</title><meta name="description" content="{h(dek)}"><link rel="canonical" href="{BASE}/{lang}/series/{h(sid)}/"><link rel="alternate" hreflang="ja" href="{BASE}/ja/series/{h(sid)}/"><link rel="alternate" hreflang="en" href="{BASE}/en/series/{h(sid)}/"><link rel="stylesheet" href="../../../assets/site.css"></head><body><header class="masthead"><div class="wrap"><div class="brand"><a href="../../">SIGNA ET STRUCTURA</a></div><div class="strap">MARKET WATCH</div></div></header><nav class="wrap nav"><a href="../../">{h(home_label)}</a><a href="../../market-watch/">{h(watch_label)}</a><span class="nav-spacer"></span><a href="../../../{other_lang}/series/{h(sid)}/">{h(other_label)}</a></nav><main><article class="article"><header class="article-head"><div class="eyebrow">MARKET WATCH · SERIES</div><h1>{h(title)}</h1><p class="dek">{h(dek)}</p></header><section class="article-grid"><div class="article-body"><h2>{h(section_title)}</h2><p>{h(method)}</p><h2>{h(entries_title)}</h2><div class="grid">{cards}</div></div><aside class="article-rail"><div class="rail-box"><div class="meta">{h(rule_label)}</div><strong>{h(rule)}</strong></div></aside></section></article></main></body></html>'''

def rss(lang,items):
    ja=lang=='ja'; title='SIGNA ET STRUCTURA リサーチ' if ja else 'SIGNA ET STRUCTURA Research'
    entries=''.join(f'<item><title>{escape(x["title"])}</title><link>{escape(x["url"])}</link><guid>{escape(x["url"])}</guid><description>{escape(x["summary"])}</description><pubDate>{datetime.fromisoformat(x["published_at"]).strftime("%a, %d %b %Y %H:%M:%S %z")}</pubDate></item>' for x in items)
    return f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>{escape(title)}</title><link>{BASE}/{lang}/</link><description>{escape(title)}</description>{entries}</channel></rss>'

def sitemap(pubs,series_defs):
    byid={}
    for x in pubs:
        if x['status']=='published': byid.setdefault(x['publication_id'],{})[x['language']]=x
    urls=[f'<url><loc>{BASE}/</loc></url>']
    for path in ('ja/','en/','ja/research/','en/research/','ja/market-watch/','en/market-watch/','ja/methods/','en/methods/','ja/about/','en/about/','ja/editorial-policy/','en/editorial-policy/','ja/corrections/','en/corrections/'):
        urls.append(f'<url><loc>{BASE}/{path}</loc></url>')
    for sd in series_defs:
        sid=sd['series_id']
        for lang in ('ja','en'):
            urls.append(f'<url><loc>{BASE}/{lang}/series/{escape(sid)}/</loc></url>')
    for editions in byid.values():
        for x in editions.values():
            alts=''.join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{escape(e["url"])}"/>' for l,e in editions.items())
            urls.append(f'<url><loc>{escape(x["url"])}</loc>{alts}</url>')
    return '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'+''.join(urls)+'</urlset>'

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--preview',action='store_true'); args=ap.parse_args()
    pubs=load('publishing/publications.json')['publications']; figs=load('publishing/figures.json')['figures']; series_defs=load('publishing/series.json')['series']; validate(pubs,figs); validate_series(series_defs); fmap=figure_map(figs)
    for lang in ('ja','en'):
        items=published(pubs,lang)
        if not items: raise SystemExit(f'no published {lang} items')
        (SITE/lang/'market-watch').mkdir(parents=True,exist_ok=True)
        (SITE/lang/'series').mkdir(parents=True,exist_ok=True)
        (SITE/lang/'index.html').write_text(home(lang,items,fmap,args.preview),encoding='utf-8')
        (SITE/lang/'research'/'index.html').write_text(research_index(lang,items,args.preview),encoding='utf-8')
        (SITE/lang/'market-watch'/'index.html').write_text(market_watch_index(lang,items,series_defs,args.preview),encoding='utf-8')
        for sd in series_defs:
            out=SITE/lang/'series'/sd['series_id']; out.mkdir(parents=True,exist_ok=True)
            (out/'index.html').write_text(series_landing(lang,items,sd,args.preview),encoding='utf-8')
        (SITE/lang/'feed.xml').write_text(rss(lang,items),encoding='utf-8')
    (SITE/'sitemap.xml').write_text(sitemap(pubs,series_defs),encoding='utf-8')
    allitems=sorted([x for x in pubs if x['status']=='published'],key=lambda x:x['published_at'],reverse=True)
    (SITE/'feed.xml').write_text(rss('en',allitems),encoding='utf-8')
    print(f'Built {len(pubs)} editions, {len(figs)} figures and {len(series_defs)} series; preview={args.preview}')
if __name__=='__main__': main()
