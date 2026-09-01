# SIGNA ET STRUCTURA — Information Architecture v0.2

ページ作成日時：2026-09-01 14:24 JST  
最終更新日時：2026-09-01 14:24 JST

status: design-proposal

## 1. 目的

記事・データ・図表が数十〜数百件へ増えても、SIGNA ET STRUCTURAを「最新記事の置き場」ではなく、市場を継続的に読むpublicationとして維持する。

トップページは媒体説明を主役にせず、**その時点で読む価値の高いResearch / Market Watch / Dataを編集して見せる一面**とする。

## 2. 原則

- 1つのpublicationを複数カテゴリへコピーしない。
- `publication_id` を単位にmetadataから各indexへ投影する。
- 時系列だけでなく、content type / theme / series / entity / dateから辿れるようにする。
- 空カテゴリを先回りして大量に公開しない。公開物が一定数できた時点で入口を有効化する。
- 日本語版と英語版は同じinformation architectureを持つ。
- 公開用UIへ内部Gate名、SHA、内部statusを露出しない。
- Data / Figureは記事の付属物だけでなく、独立して再利用・参照できるpublic objectとして扱えるようにする。

## 3. Public taxonomy

### Content types

- 市場観測 / Market Watch — 現在進行形の市場変化。比較的短く、更新頻度が高い。
- テーマ分析 / Theme Analysis — 一つの構造・テーマをEvidenceで掘る中長文。
- 過去事例研究 / Historical Case Study — 過去市場を再構築する保存価値の高い研究。
- プロトコル分析 / Protocol Analysis — protocol / product / mechanismの構造と実態を検証。
- SNS動向 / SNS Trends — 公開SNS上の観測・signal研究。
- 方法論 / Methodology — Replay、Evidence、metric definition等。
- データ / Data — publish-approved dataset / figure / chart / data note。

Content typeは相互排他的な主分類を原則とする。Theme / tagは横断分類として別に持つ。

### Themes / tags

初期候補：

- DeFi
- Market Structure
- Stablecoins
- Liquidity
- SNS / Attention
- Meme / Speculation
- Tokenized Assets
- CEX / Exchange
- Historical Markets

Themeは記事数が増えたものからpublic landingを作る。

## 4. Route model

```text
/ja/
├─ research/              全公開物の総合index
├─ market-watch/          市場観測が蓄積したら有効化
├─ themes/                theme landingが必要になったら有効化
│   └─ <theme>/
├─ case-studies/          Historical Case Studyが複数本になったら有効化
├─ data/                  public data / figuresが蓄積したら有効化
├─ methods/
├─ about/
├─ editorial-policy/
└─ corrections/

/en/ は同型。
```

記事URLは既存 `/ja/research/<slug>/` を維持し、分類変更でURLを変えない。カテゴリページはarticleへのprojectionとする。

## 5. Top page v0.2

トップは次の順で構成する。

1. Masthead / language / compact navigation
2. Lead Research — 編集上もっとも重要な1本。Figureを伴える。
3. Latest — 新着3〜5本
4. Market Watch — 公開物がある場合のみ
5. Themes — 現在追跡中の主要theme 3〜6件
6. Case Studies — 保存価値の高い研究
7. Data & Figures — public data objectがある場合のみ
8. Methods / About — compact utility block
9. disclosure notice / footer

現在の大きな媒体説明Heroと「公開基準」3カードは縮小・撤去する。媒体説明はAbout、公開方針は編集方針へ委譲する。

## 6. Lead Research selection

Leadは単純な最新順に固定しない。

metadata例：

```yaml
homepage:
  eligible: true
  priority: 80
  lead_candidate: true
```

Publication Ownerが公開時にlead候補を指定できる。自動builderは`lead_candidate`と公開日時を使って一面を構築する。

## 7. Public content registry

将来のbuilder正本として、public repoにmachine-readable registryを置く。

```yaml
publication_id: scmr-20260831-001
language: ja
edition: japanese
slug: robinhood-chain-capital-parking
title: ...
content_type: theme_analysis
themes: [market-structure, stablecoins, defi]
series: null
published_at: ...
updated_at: ...
as_of: ...
summary: ...
hero_figure: scmr-20260831-001-fig01
related_publications: [scmr-20260831-002]
status: published
homepage:
  eligible: true
  priority: 80
```

内部Gate / reviewer / private evidenceはここへ入れない。

## 8. Builder target

手編集対象を減らす。

```text
public content registry
+ approved public article edition
+ approved figure/data package
        ↓
Publication Builder
        ├─ article HTML
        ├─ /research/ index
        ├─ homepage sections
        ├─ content-type indexes
        ├─ theme pages
        ├─ data index
        ├─ related research
        ├─ sitemap.xml
        ├─ RSS / Atom
        └─ optional JSON feed
```

記事公開のたびにトップ、index、sitemapを人手で別々に編集しない。

## 9. Search / filtering growth path

### Stage 1 — 〜20 publications

- Research index
- content type labels
- theme links
- chronological archive

### Stage 2 — 20〜100

- client-side filter or generated filtered indexes
- content type / theme / year
- series landing
- related publications

### Stage 3 — 100+

- full-text search index
- entity / protocol / chain indexes
- dataset catalog
- machine-readable API/feedを検討

最初から重い検索基盤を入れない。

## 10. Data / Figure model

Figureはpublicationに従属しつつ、public objectとして以下を持つ。

```yaml
figure_id: scmr-20260831-001-fig01
publication_id: scmr-20260831-001
title: ...
kind: data_figure
as_of: ...
source_summary: ...
method_summary: ...
svg_path: ...
data_path: ...
spec_path: ...
```

Dataページでは、記事から独立してFigureを探せるようにする。ただし元記事、source、limitationsへの導線を必須とする。

## 11. Bilingual model

同じ`publication_id`にJA / EN editionを紐づける。

- 日本語版を単純に英訳しただけの別正本にはしない。
- 数値・Evidence・Figure・留保の意味は一致させる。
- language switchはpublication_idで対応するeditionへ移動する。
- 片方しか存在しない場合は無理にリンクを生成しない。

## 12. RSS / feeds

記事数増加前にRSS/Atom生成をbuilderへ入れる。

最低限：

- all research
- Japanese
- English

将来必要ならMarket Watch等のtype別feedを追加する。

## 13. MVP implementation plan

### IA-01 Public registry
既存4 edition（2 publication × JA/EN）をregistry化する。

### IA-02 Homepage v0.2
現在の2本をfixtureとして、Lead + Latest + Themes + Case Studies/Data placeholder behaviorを実装する。空sectionは表示しない。

### IA-03 Generated Research Index
registryからJA/EN indexを生成するbuilderを作る。

### IA-04 Generated sitemap / hreflang
publication_idペアから生成する。

### IA-05 RSS / Atom
registryから生成する。

### IA-06 Data/Figure registry
現行4 Figureをfixtureとして登録する。

### IA-07 Validation
重複publication_id、slug collision、missing edition path、missing figure、invalid dates、broken related IDsをCIでfailさせる。

## 14. Human approval boundary

Builderが生成物を更新しても、それ自体はpublish approvalではない。

```text
approved public source
→ builder
→ preview artifact
→ visual / link QA
→ exact main SHA
→ explicit publish request
→ production deploy
```

既存の明示publish-request laneを維持する。

## 15. 今回のwireframe判断

トップページv0.2では、現在の「市場の兆候から、構造を読む。」という大きな説明Heroを縮小し、Robinhood / Twofold等の**実際のResearchをファーストビューへ引き上げる**。

媒体の思想はmasthead下の短い1文とAboutへ残す。

## 更新履歴

- 2026-09-01 14:24 JST：v0.2作成。大量publication、data/figure、taxonomy、registry-driven builder、homepage一面化、段階的search、RSSを定義。
