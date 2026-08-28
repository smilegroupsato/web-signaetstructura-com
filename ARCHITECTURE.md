# SIGNA ET STRUCTURA — Site Architecture v0.1

ページ作成日時：2026-08-28 23:32 JST
最終更新日時：2026-08-28 23:32 JST

status: design-draft
brand: SIGNA ET STRUCTURA
publisher: Smile Company LLC
production_domain: signaetstructura.com
source_research_repository: smilegroupsato/sc-crypto-ops

## 1. Purpose

SIGNA ET STRUCTURA is the public publication surface for research approved through the SC Markets Research publication lane.

Editorial direction:

**Financial Times × academic journal × modern data publication**

Editorial principle:

**Signal → Structure → Evidence**

The public repository must contain only material safe for public release. Internal research, unpublished evidence, portfolio decisions, approvals, secrets, and non-public review records remain outside this repository.

## 2. Source-of-truth boundary

```text
smilegroupsato/sc-crypto-ops (private)
  Research / Evidence / Public Draft
  Publish Gate / Compliance Gate / Approval
          ↓ approved publication artifact
smilegroupsato/web-signaetstructura-com
  public edition / public figures / site source
          ↓ candidate build
          ↓ human publish approval
          ↓ production deploy
signaetstructura.com
```

GitHub presence in this repository does not itself mean production publication approval.

## 3. Language model

Japanese and English are first-class public languages.

```text
/
  → language-aware landing / redirect policy
/ja/
/en/
```

Recommended content routes:

```text
/ja/research/
/ja/market-watch/
/ja/case-studies/
/ja/methods/
/ja/about/

/en/research/
/en/market-watch/
/en/case-studies/
/en/methods/
/en/about/
```

Japanese approved research is the initial canonical editorial source unless a publication is originally authored in English. Translation is a derivative edition, not a second research truth.

Language editions must preserve:

- publication_id
- canonical source reference
- numerical values
- dates / times / as_of
- evidence meaning
- risk / methodology notes
- disclosures
- correction status

Translation differences that materially change meaning require re-review.

## 4. Repository target structure

```text
/
  README.md
  ARCHITECTURE.md
  AGENTS.md
  content/
    ja/
    en/
  data/
    public/
  figures/
    data/
    specs/
    output/
  publishing/
    templates/
    schemas/
    releases/
    requests/
  site/
  scripts/
  .github/workflows/
```

Principles:

- `content/` = public language editions, not internal research drafts.
- `data/public/` = publish-approved datasets only.
- `figures/` = publish-approved figure sources and derivatives.
- `publishing/` = publication contracts, candidate receipts, explicit promotion requests.
- `site/` = production-ready generated output.
- `site/` should become reproducible from public source materials.

## 5. Content contract

Each public article should minimally include:

```yaml
publication_id: scmr-YYYYMMDD-NNN
language: ja
title: "..."
slug: "..."
content_type: "Historical Case Study"
published_by: "Smile Company LLC"
created_at: "YYYY-MM-DD HH:MM JST"
updated_at: "YYYY-MM-DD HH:MM JST"
as_of: "YYYY-MM-DD HH:MM JST"
source_canonical_sha: "..."
source_publication_path: "publication/sc-markets-research/drafts/..."
translation_of: null
status: publication-candidate
risk_level: medium
correction_status: none
```

English derivative example:

```yaml
language: en
translation_of: ja
translation_review_status: reviewed
```

## 6. Visual / figure contract

The public site follows the internal SC Markets Research contracts:

- `publication/sc-markets-research/FIGURE_DATA_PUBLICATION_CONTRACT_v0.1.md`
- `publication/sc-markets-research/FIGURE_DESIGN_SYSTEM_v0.1.md`

Public figure model:

```text
approved CSV / JSON
+ figure spec
+ public design tokens
      ↓
deterministic builder
      ↓
SVG primary
PNG derivative
      ↓
site candidate
```

Data Figure, Analytical Diagram, Editorial Visual, and External Figure must remain distinguishable in provenance.

## 7. Design system direction

Visual identity:

- restrained editorial typography
- generous whitespace
- strong serif masthead / headline layer
- neutral sans-serif for metadata, axes and utility UI
- warm paper-like background may be considered
- fine rules and grid discipline
- data-first presentation
- minimal decorative crypto aesthetics
- no neon trading-dashboard visual language

The site should read like a research publication, not a trading signal service.

Final typefaces and exact design tokens are deferred until licensing and implementation are confirmed.

## 8. Navigation model

Initial top-level navigation:

- Research
- Market Watch
- Case Studies
- Methods
- About
- 日本語 / English

Potential later sections:

- Theme Watch
- SNS Trends
- Data
- Corrections

Do not create empty top-level sections solely for future possibilities.

## 9. SEO / bilingual requirements

Each page should support:

- canonical URL
- `hreflang="ja"`
- `hreflang="en"`
- language-specific title and description
- Open Graph metadata
- structured publication dates
- visible `as_of`
- correction / update state

Language switching should connect equivalent publication IDs rather than guess equivalent routes from slugs.

## 10. Publication pipeline

Target flow:

```text
approved source from sc-crypto-ops
      ↓
import / promotion request
      ↓
public content validation
      ↓
JA edition build
      ↓
EN translation artifact + translation QA
      ↓
figure / data validation
      ↓
site candidate
      ↓
HTML / link / metadata validation
      ↓
desktop + mobile visual QA
      ↓
candidate SHA fixed
      ↓
human final publish approval
      ↓
explicit production promotion
      ↓
Lolipop deploy
      ↓
public URL verification
      ↓
receipt returned to sc-crypto-ops
```

No draft commit should automatically deploy merely because it entered the repository.

## 11. Lolipop production deployment

Existing `web-genai-ron-jp` uses GitHub Actions with FTPS and repository secrets:

- `FTP_SERVER`
- `FTP_USERNAME`
- `FTP_PASSWORD`
- `SERVER_DIR`

SIGNA ET STRUCTURA may reuse this deployment pattern because the production account is also on Lolipop, but v0.1 should strengthen the release boundary.

Recommended approach:

```text
feature/content branch
→ validation PR
→ main
→ prepare production candidate
→ human approval / explicit workflow_dispatch
→ FTPS upload of exact `site/` candidate
→ public verification
```

Production deploy should not be triggered by every push to `main` in the initial phase.

Secrets remain in GitHub Actions secrets and must never be committed.

`SERVER_DIR` must point only to the document root assigned to `signaetstructura.com`, avoiding any overlap with existing Lolipop sites.

## 12. Release receipt

Each production release should record at minimum:

```yaml
release_id: ses-YYYYMMDD-NNN
publication_ids:
  - scmr-YYYYMMDD-NNN
source_repo: smilegroupsato/web-signaetstructura-com
source_sha: "..."
candidate_sha256: "..."
published_at: "YYYY-MM-DD HH:MM JST"
production_domain: signaetstructura.com
routes:
  - /ja/...
  - /en/...
verified: true
```

The SC Markets Research internal publication receipt should link to this public release evidence.

## 13. Correction / withdrawal

Public corrections preserve provenance.

```text
published version A
→ correction request
→ updated content B
→ validation / Gate where required
→ production promotion B
→ visible correction note
→ release receipt links A and B
```

For withdrawal, preserve an internal receipt even if public content is removed. Where appropriate, retain a public withdrawal notice rather than silently erasing history.

## 14. Security boundary

Never place in this public repository:

- API keys / passwords / private keys / seed phrases
- unpublished portfolio holdings when not explicitly disclosed
- internal investment decisions
- raw confidential evidence
- private reviewer comments
- unapproved drafts from research chats
- internal-only receipts containing sensitive material
- non-public personal information

CI should include secret scanning and public-boundary validation before production release.

## 15. MVP implementation order

1. Repository operating contract / public-boundary README
2. bilingual content schema and templates
3. base static site / design tokens / masthead
4. one JA/EN fixture publication
5. figure/data fixture integration
6. candidate builder + validation
7. desktop/mobile visual QA
8. SHA-fixed release receipt
9. explicit Lolipop FTPS deploy workflow
10. production domain verification

The first real content fixture should preferably use an SC Markets Research article already carrying reproducible figures, such as the Tomb Fork historical case study.

## 16. Current decisions

Fixed:

- Brand: `SIGNA ET STRUCTURA`
- Domain: `signaetstructura.com`
- Publisher: `Smile Company LLC`
- Languages: Japanese + English
- Editorial direction: Financial Times × academic journal × modern data publication
- Editorial principle: Signal → Structure → Evidence
- Hosting: existing Lolipop account
- Public site repository: `smilegroupsato/web-signaetstructura-com`
- Internal research / gate repository: `smilegroupsato/sc-crypto-ops`

Not yet fixed:

- final typography
- exact palette
- static site implementation technology
- production document-root path on Lolipop
- translation tooling
- exact candidate builder implementation

## 更新履歴

- 2026-08-28 23:32 JST：v0.1作成。ブランド、日英二言語、private/public境界、figure/data、candidate-first publication、Lolipop FTPS deployment、release receiptの初期Architectureを定義。
