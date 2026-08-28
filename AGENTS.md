# SIGNA ET STRUCTURA — Repository Operating Contract

ページ作成日時：2026-08-28 23:32 JST
最終更新日時：2026-08-28 23:32 JST

status: active

## 1. Purpose

This repository is the public website and publication infrastructure for SIGNA ET STRUCTURA, published by Smile Company LLC.

Internal market research and publication approval remain canonical in `smilegroupsato/sc-crypto-ops`.

## 2. Public boundary

Only publish-approved material may be promoted into this repository as public content.

Never commit:

- internal research drafts
- confidential evidence
- private reviewer comments
- portfolio decisions or undisclosed holdings
- API secrets / passwords / private keys / seed phrases
- internal-only publication receipts
- personal or confidential information

Repository presence does not equal production publish approval.

## 3. Source hierarchy

For public site implementation:

1. `ARCHITECTURE.md`
2. public content / metadata contract
3. public figure / data artifacts
4. `site/` generated output

For research meaning, evidence, compliance and approval, `smilegroupsato/sc-crypto-ops` remains authoritative.

## 4. Languages

Japanese and English are first-class public editions.

Translation must preserve publication ID, numerical values, dates, `as_of`, evidence meaning, disclosures and correction state.

Material semantic changes require review rather than silent translation edits.

## 5. Git / release

- Use feature branches for implementation and content changes.
- Validate before merging.
- Do not treat merge to `main` as automatic production permission.
- Production deploy requires an explicit release action and human approval.
- Preserve release provenance and candidate SHA.
- Do not modify unrelated files in a publication change.

## 6. Deployment

Production target is `signaetstructura.com` on the existing Lolipop account.

Deploy only to the dedicated document root for this domain.

Credentials must be stored only as GitHub Actions secrets or an equivalent secret store.

## 7. Visual system

Editorial direction:

**Financial Times × academic journal × modern data publication**

Editorial principle:

**Signal → Structure → Evidence**

Data figures must remain reproducible and distinguish measured data from editorial imagery.

## 8. Completion checklist

Before a production release:

1. public-boundary validation passes
2. language metadata is valid
3. links / canonical / hreflang are valid
4. figures and source notes are present
5. desktop/mobile preview is reviewed
6. approved candidate SHA matches release candidate
7. production target is correct
8. release receipt is generated
9. public URL is verified after deploy

## 更新履歴

- 2026-08-28 23:32 JST：初版。public boundary、日英、release、secret、production deploy ruleを定義。
