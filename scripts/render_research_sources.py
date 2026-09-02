#!/usr/bin/env python3
import html, json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'site'
BASE='https://signaetstructura.com'

def h(v): return html.escape(str(v), quote=True)
def load(p): return json.loads((ROOT/p).read_text(encoding='utf-8'))

def inline(s):
    s=h(s)
    s=re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s=re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    s=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2">\1</a>', s)
    return s

def table_html(rows):
    if len(rows)<2: return '<p>'+inline(' | '.join(rows[0]))+'</p>' if rows else ''
    head=rows[0]
    body=rows[2:] if all(re.fullmatch(r'\s*:?-+:?\s*',x) for x in rows[1]) else rows[1:]
    th=''.join(f'<th>{inline(x.strip())}</th>' for x in head)
    trs=''.join('<tr>'+''.join(f'<td>{inline(x.strip())}</td>' for x in r)+'</tr>' for r in body)
    return f'<div class="table-wrap"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'

def render_figure(fid, fmap, lang):
    f=fmap.get(fid)
    if not f: return f'<p class="meta">Figure {h(fid)}</p>'
    title=f.get('title_ja' if lang=='ja' else 'title_en') or f.get('title_ja') or f.get('title_en') or fid
    path='../../../'+f['svg_path'].removeprefix('site/')
    asof=f.get('as_of','')
    return f'<figure class="research-figure"><img src="{h(path)}" alt="{h(title)}"><figcaption><strong>{h(title)}</strong>{f" · {h(asof)}" if asof else ""}</figcaption></figure>'

def markdown_to_html(text, entry, fmap):
    lang=entry['language']; lines=text.splitlines(); out=[]; para=[]; ul=[]; code=[]; in_code=False; table=[]
    inserts=entry.get('inline_figures',{})
    seen_h1=False
    def flush_para():
        nonlocal para
        if para:
            out.append('<p>'+inline(' '.join(x.strip() for x in para))+'</p>'); para=[]
    def flush_ul():
        nonlocal ul
        if ul:
            out.append('<ul>'+''.join(f'<li>{inline(x)}</li>' for x in ul)+'</ul>'); ul=[]
    def flush_table():
        nonlocal table
        if table:
            out.append(table_html(table)); table=[]
    def flush_all(): flush_para(); flush_ul(); flush_table()
    for raw in lines:
        line=raw.rstrip()
        if line.strip().startswith('```'):
            flush_all()
            if in_code:
                out.append('<pre><code>'+h('\n'.join(code))+'</code></pre>'); code=[]; in_code=False
            else: in_code=True
            continue
        if in_code:
            code.append(line); continue
        m=re.match(r'^(#{1,4})\s+(.+)$',line)
        if m:
            flush_all(); level=len(m.group(1)); title=m.group(2).strip()
            if level==1 and not seen_h1:
                seen_h1=True; continue
            level=max(2,level)
            out.append(f'<h{level}>{inline(title)}</h{level}>')
            for key,fids in inserts.items():
                if title.startswith(key):
                    for fid in fids: out.append(render_figure(fid,fmap,lang))
            continue
        fm=re.match(r'^Figure(?:s)?\s*:\s*`([^`]+)`\s*$',line,re.I)
        if fm:
            flush_all(); out.append(render_figure(fm.group(1),fmap,lang)); continue
        fm2=re.match(r'^Figure\s+(\d+).*$' ,line,re.I)
        if fm2 and entry.get('figure_number_map',{}).get(fm2.group(1)):
            flush_all(); out.append(render_figure(entry['figure_number_map'][fm2.group(1)],fmap,lang)); continue
        if line.startswith('- '):
            flush_para(); flush_table(); ul.append(line[2:].strip()); continue
        if line.startswith('|') and line.endswith('|'):
            flush_para(); flush_ul(); table.append([x for x in line.strip('|').split('|')]); continue
        if not line.strip():
            flush_all(); continue
        if line.startswith('> '):
            flush_all(); out.append('<blockquote>'+inline(line[2:].strip())+'</blockquote>'); continue
        para.append(line)
    flush_all()
    return '\n'.join(out)

def article(entry, pubs, fmap, preview=False):
    lang=entry['language']; ja=lang=='ja'; slug=entry['slug']; source=(ROOT/entry['source_markdown']).read_text(encoding='utf-8')
    body=markdown_to_html(source,entry,fmap)
    paired=next((x for x in pubs if x['publication_id']==entry['publication_id'] and x['language']!=lang and x['status']=='published'),None)
    alt=''
    if paired:
        alt=f'<link rel="alternate" hreflang="{h(paired["language"])}" href="{h(paired["url"])}">'
    noindex='<meta name="robots" content="noindex,nofollow">' if preview else ''
    labels={
      'home':'トップ' if ja else 'Home','research':'リサーチ' if ja else 'Research','methods':'方法論' if ja else 'Methodology',
      'asof':'調査時点' if ja else 'Research as of','published':'公開' if ja else 'Published',
      'figures':'図表' if ja else 'Figures'
    }
    fig_gallery=''
    gallery=entry.get('figure_gallery',[])
    if gallery:
        fig_gallery='<section class="figure-gallery"><h2>'+labels['figures']+'</h2>'+''.join(render_figure(fid,fmap,lang) for fid in gallery)+'</section>'
    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">{noindex}<title>{h(entry['title'])} | SIGNA ET STRUCTURA</title><meta name="description" content="{h(entry['summary'])}"><link rel="canonical" href="{h(entry['url'])}"><link rel="alternate" hreflang="{lang}" href="{h(entry['url'])}">{alt}<link rel="stylesheet" href="../../../assets/site.css"><style>.article-body{{max-width:790px}}.article-body h2{{margin-top:2.6rem}}.article-body h3{{margin-top:2rem}}.article-body p{{font-size:1.04rem;line-height:1.9}}.article-body ul{{line-height:1.8}}.article-body pre{{overflow:auto;padding:1rem;border:1px solid var(--rule);background:var(--paper-soft,#f6f4ef)}}.table-wrap{{overflow-x:auto;margin:1.5rem 0}}table{{border-collapse:collapse;width:100%;font-family:var(--sans)}}th,td{{padding:.65rem;border-bottom:1px solid var(--rule);text-align:left;vertical-align:top}}.research-figure{{margin:2.4rem 0;padding-top:1rem;border-top:1px solid var(--ink)}}.research-figure img{{width:100%;height:auto;display:block}}.research-figure figcaption{{font-family:var(--sans);font-size:.78rem;line-height:1.5;color:var(--ink-soft);margin-top:.65rem}}blockquote{{margin:1.5rem 0;padding:.2rem 0 .2rem 1.2rem;border-left:3px solid var(--ink);font-size:1.05rem}}</style></head><body><header class="masthead"><div class="wrap"><a class="brand" href="../../../{lang}/">SIGNA ET STRUCTURA</a><div class="strap">{h(entry['content_type_label'])}</div></div></header><nav class="wrap nav"><a href="../">{labels['research']}</a><a href="../../../{lang}/methods/">{labels['methods']}</a><span class="nav-spacer"></span><a href="../../../{lang}/">{labels['home']}</a>{f'<a href="../../../{paired["language"]}/research/{paired["slug"]}/">{"English" if ja else "日本語"}</a>' if paired else ''}</nav><main><article class="article"><header class="article-head"><div class="eyebrow">{h(entry['content_type_label'])}</div><h1>{h(entry['title'])}</h1><p class="dek">{h(entry['summary'])}</p><div class="article-meta"><span>{labels['asof']} {h(entry['as_of'])}</span><span>{labels['published']} {h(entry['published_at'][:10])}</span></div></header><section class="article-grid"><div class="article-body">{body}{fig_gallery}</div></section></article></main><footer class="site-footer"><div class="wrap"><p class="meta">SIGNA ET STRUCTURA · Smile Company LLC</p></div></footer></body></html>'''

def main():
    import argparse
    ap=argparse.ArgumentParser(); ap.add_argument('--preview',action='store_true'); args=ap.parse_args()
    pubsdoc=load('publishing/publications.json'); pubs=pubsdoc['publications']; figs=load('publishing/figures.json')['figures']; fmap={x['figure_id']:x for x in figs}
    count=0
    for e in pubs:
        if e.get('status')!='published' or not e.get('source_markdown'): continue
        src=ROOT/e['source_markdown']
        if not src.exists(): raise SystemExit(f'missing research source: {src}')
        out=ROOT/e['article_path']; out.parent.mkdir(parents=True,exist_ok=True)
        out.write_text(article(e,pubs,fmap,args.preview),encoding='utf-8'); count+=1
    print(f'Rendered {count} approved research editions; preview={args.preview}')
if __name__=='__main__': main()
