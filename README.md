# SIGNA ET STRUCTURA

最終更新日時：2026-09-01 23:55 JST

Public website and publication infrastructure for **SIGNA ET STRUCTURA**, a bilingual market-research and data publication by **Smile Company LLC**.

Production: `signaetstructura.com`

## Current state

The site is live and the publication layer is no longer a bootstrap shell.

Current implementation:

- Japanese / English public editions
- registry-driven Publication Builder
- generated JA / EN homepages
- generated Research indexes
- generated Market Watch / series landing support
- generated sitemap / hreflang
- JA / EN / all-publication RSS feeds
- public Figure registry
- exact-SHA production candidate / deploy flow
- explicit production publish request for ordinary Research
- FTPS deployment to the Lolipop production document root

The public-site repository is:

`smilegroupsato/web-signaetstructura-com`

The internal research / evidence / publication-review source remains:

`smilegroupsato/sc-crypto-ops`

## Core public registries

```text
publishing/publications.json   public article / edition registry
publishing/figures.json        public figure registry
publishing/series.json         recurring public series registry
```

`site/` is generated output / public static assets. It is not the metadata source of truth for indexes and navigation.

The current builder is:

```text
scripts/build_publication_site.py
```

It generates or refreshes homepage projections, Research indexes, Market Watch / series landings, feeds and sitemap from the registries.

## Publication model

Long-form Research:

```text
sc-crypto-ops Research / Evidence
→ public draft
→ Research / compliance review
→ public edition + figure package
→ public registry
→ Builder
→ Preview
→ exact SHA
→ explicit publish request
→ production
```

Recurring short-form Market Watch is being separated into a controlled automatic lane:

```text
scheduled patrol
→ public-safe observation package
→ pre-approved series profile
→ automatic publication validation
→ public registry / short brief
→ Builder
→ production projection
```

The automatic lane is for factual, short, time-sensitive observations such as notable DeFi changes, abnormal market flow, X/SNS trends and Meme-market observations. It must not silently convert internal Candidate / Portfolio / BUY decisions into public posts.

See `publishing/AUTO_PUBLICATION.md`.

## Market Watch

Market Watch is a generated public section rather than a hand-maintained article directory.

The current registered series is:

- `base-tokenized-stock-yield-watch` — continuing observation of material structural changes in tokenized-stock yield markets on Base.

A series may exist before it has published entries. Empty series do not require manually maintained HTML pages.

## Design / editorial direction

**Financial Times × academic journal × modern data publication**

Editorial principle:

**Signal → Structure → Evidence**

The public surface should remain a research publication, not a trading-signal dashboard.

## Key documents

- `ARCHITECTURE.md` — current system architecture
- `INFORMATION_ARCHITECTURE_v0.2.md` — scalable information architecture
- `DESIGN_SYSTEM.md` — public design rules
- `AGENTS.md` — repository operating contract
- `PRODUCTION_PUBLISHING.md` — production publication lane
- `publishing/AUTO_PUBLICATION.md` — recurring short-form automatic-publication contract

## Security boundary

Never place secrets, private keys, seed phrases, internal portfolio decisions, non-public holdings, confidential evidence, private reviewer comments or raw internal research in this public repository.

## 更新履歴

- 2026-09-01 23:55 JST：bootstrap表記を廃止し、Registry-driven Builder、Market Watch、RSS、exact-SHA deploy、短報自動公開レーンの現行構成へ同期。
