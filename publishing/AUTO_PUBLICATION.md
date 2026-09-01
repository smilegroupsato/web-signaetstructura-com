# Automatic Market Watch Publication

ページ作成日時：2026-09-01 23:55 JST  
最終更新日時：2026-09-01 23:55 JST

status: design-approved / implementation-pending

## Purpose

定時巡回やDiscovery scriptが検出した公開市場の重要変化を、SIGNA ET STRUCTURAの短報として低遅延で掲載するための専用レーン。

対象は長文Researchではなく、**事実中心の短い継続観測**とする。

## Intended flow

```text
sc-crypto-ops scheduled patrol
→ evidence snapshot
→ public short-brief package
→ auto-series profile lookup
→ fail-closed validation
→ web-signaetstructura-com intake
→ public article / registry entry
→ Publication Builder
→ Market Watch / Series / RSS
→ production deploy
→ machine receipt
```

## Human approval model

個々の短報を毎回人間承認する方式では、速報性が失われる。

代わりに、**series単位で人間が事前承認**する。

事前承認時に固定するもの：

- series ID
- 監視対象
- 許可するdata source / evidence type
- publication cadence / event trigger
- freshness window
- 最大文字数
- allowed claim types
- prohibited claim types
- disclosure template
- language policy
- auto-deploy permission

seriesの意味や対象を変更する場合は再承認する。

## Suitable content

- DeFi TVL / liquidity / volume / utilizationの大きな変化
- protocol launch / deployment / material parameter change
- stablecoin supply / lending-market compositionの変化
- public on-chain abnormal flow
- X / SNSでの投稿数・unique author・CA mention等の明確な加速
- Meme市場のattention / liquidity / volume変化
- public listing / pair creation / new DEX observation
- 既存Watch仮説に対する重要な反証データ

## Not suitable for automatic publication

以下は自動公開禁止：

- BUY / SELL / short / long指示
- Entry / Size / Exit判断
- Portfolio固有評価
- Real / Paper Intent
- 未公開保有状況
- private API credential / raw secret
- 未検証rumorを事実として記述するもの
- private group / DM / non-public source内容
- 個人情報
- 将来価格の断定
- 市場を煽る目的の文言
- 自らのpositionのExit liquidity形成につながるpromotion
- conflict / sponsorshipが未確認の対象

## Short-brief package v0.1

Source-side generatorからWeb側へ渡すpackage例：

```json
{
  "schema_version": "signa-auto-brief-v0.1",
  "publication_id": "mw-20260901-2355-base-yield",
  "series_id": "base-tokenized-stock-yield-watch",
  "observed_at": "2026-09-01T23:55:00+09:00",
  "as_of": "2026-09-01T23:55:00+09:00",
  "language": "ja",
  "title": "...",
  "summary": "...",
  "what_changed": "...",
  "evidence": [
    {
      "source_name": "...",
      "source_url": "https://...",
      "observed_at": "2026-09-01T23:55:00+09:00",
      "fact": "..."
    }
  ],
  "limitations": "...",
  "disclosure": "本稿は公開市場の観測記録であり、売買推奨ではありません。",
  "auto_publish_profile": "base-tokenized-stock-yield-watch-v0.1"
}
```

## Validation

Web-side intakeは最低限以下をfail-closedで確認する。

- schema version
- publication ID uniqueness
- approved series ID
- approved auto-publish profile
- observed_at / as_of validity
- freshness
- evidence count >= 1
- public source URL presence where applicable
- required limitation / disclosure
- maximum text lengths
- no secret-like strings
- no internal-only field names
- no BUY / SELL / Entry / Size / Exit / Intent style directive
- no missing source article / figure reference when referenced
- no duplicate observation hash

AI生成文の「自然さ」だけで通さない。Evidenceと構造化fieldを先に検証する。

## Suggested public article form

短報は長文Researchと見た目を分ける。

```text
Market Watch
[time] [series]
Title

What changed
2〜5文

Evidence
・source / timestamp / metric
・source / timestamp / metric

Why it matters
1〜3文。仮説は仮説と明記。

Limitations
短い留保
```

1本の短報を無理に長文化しない。

## Series registry

Public recurring seriesは `publishing/series.json` に置く。

現行：

- `base-tokenized-stock-yield-watch`

今後候補：

- DeFi Opportunity Watch
- Abnormal Flow Watch
- X / SNS Trend Watch
- Meme Attention Watch
- New DEX / New Pair Watch

実際のseries名は内部patrol laneと1:1でなくてよい。複数の内部detectorを1つの読者向けSeriesへ集約してよい。

## Deployment model

通常Researchのhuman-approved exact-SHA laneとは分離するが、以下は共通化する。

- same public registry model
- same Publication Builder
- same link / secret validation
- same FTPS target
- same release provenance

Auto laneだけ別HTML builderを作らない。

Production auto-deployを有効にする前に、shadow package → Preview → non-production artifactで少なくとも複数件を通し、誤投稿条件を確認する。

## Cross-repository connection

`sc-crypto-ops` からpublic repoへ直接write credentialを広く配布しない。

推奨：

```text
sc-crypto-ops workflow
→ narrowly scoped repository_dispatch / GitHub App event
→ web repo intake workflow
```

必要なtokenはGitHub Actions secretにのみ保存する。

Source patrol script自身へWeb repoの長期PATを埋め込まない。

## Receipt

Auto publicationごとにmachine receiptを残す。

最低限：

```yaml
publication_id: ...
series_id: ...
source_observation_id: ...
source_sha: ...
web_sha: ...
validation_profile: ...
published_at: ...
production_url: ...
deploy_result: success
```

## Rollback / correction

誤りを発見した場合は静かに上書きしない。

- data source correction
- generator bug
- stale evidence
- wording error

を区別し、必要ならvisible correction noteとmachine receiptを残す。

重大な誤投稿時にはseries auto-deployを停止できるkill switchを用意する。

## Implementation order

1. auto-series profile schema
2. short-brief JSON validator
3. HTML short-brief renderer / Builder integration
4. shadow fixtures
5. Web-side intake workflow
6. source-side repository_dispatch producer
7. Preview-only live patrol test
8. series単位のhuman activation
9. unattended production deploy
10. receipt / kill switch確認

## 更新履歴

- 2026-09-01 23:55 JST：v0.1作成。定時巡回からMarket Watch短報をseries事前承認＋fail-closed validationで自動公開する境界を定義。
