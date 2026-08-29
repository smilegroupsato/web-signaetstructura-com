# SIGNA ET STRUCTURA URL Taxonomy v0.1

ページ作成日時：2026-08-29 09:02 JST  
最終更新日時：2026-08-29 09:02 JST

## Principles

- JA / ENを同じinformation architectureで管理する。
- content typeとseriesをURLに混在させない。
- article slugは原則英数字・kebab-case。
- canonical URLは公開後に変更しない。
- 訂正・更新では同じURLを維持し、version / receipt / change historyで追跡する。

## Root

- `/` — language entry / x-default
- `/ja/`
- `/en/`

## Research

- `/ja/research/`
- `/en/research/`
- `/ja/research/{slug}/`
- `/en/research/{slug}/`

## Content-type indexes

- `/ja/case-studies/`
- `/en/case-studies/`
- `/ja/market-watch/`
- `/en/market-watch/`
- `/ja/sns-trends/`
- `/en/sns-trends/`
- `/ja/methods/`
- `/en/methods/`

## Series / Collections

- `/ja/series/{series-slug}/`
- `/en/series/{series-slug}/`

Series is a curated grouping and does not replace the article canonical URL.

Examples:
- `/ja/series/tomb-fork-boom/`
- `/en/series/tomb-fork-boom/`
- `/ja/series/historical-replay/`

## Data

- `/ja/data/`
- `/en/data/`
- `/data/figures/{publication-id}/{figure-id}.svg`
- `/data/figures/{publication-id}/{figure-id}.png`
- `/data/datasets/{publication-id}/{dataset-name}.csv`

Public datasets / figures are language-neutral where practical.

## Standards / company

- `/ja/about/`, `/en/about/`
- `/ja/methods/`, `/en/methods/`
- `/ja/corrections/`, `/en/corrections/`
- future: `/ja/editorial-policy/`, `/en/editorial-policy/`

## Search / Index

MVPではserver-side searchを前提にしない。

- `/ja/index/`
- `/en/index/`

ここへcontent type / series / topic / dateの静的indexを生成する。
将来client-side full-text searchを導入してもcanonical content pathは変更しない。

## hreflang

JA / EN pairが存在する場合：
- `hreflang=ja`
- `hreflang=en`
- rootには`x-default`

英訳未作成の記事では存在しないEN URLを生成しない。

## 更新履歴

- 2026-08-29 09:02 JST：v0.1作成。
