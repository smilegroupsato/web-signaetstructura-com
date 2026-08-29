# SIGNA ET STRUCTURA Launch Checklist v0.1

ページ作成日時：2026-08-29 14:48 JST  
最終更新日時：2026-08-29 14:48 JST

## Current candidate

- candidate source SHA: `1b2cc4431e8a08b3e579a299e1e01e7de4873998`
- candidate artifact digest: `sha256:9c6670961669b4c5b2215bbcb522a6a46fef2dcf1abce7c4c099be814d66abe3`
- production deploy: not executed

## Infrastructure

- [x] `signaetstructura.com` acquired
- [x] Lolipop public folder selected: `signaetstructura.com`
- [x] GitHub Repository Secrets configured: FTP server / username / password
- [x] GitHub `production` Environment created
- [x] production Environment restricted to `main`
- [x] preview CI passed
- [x] first production candidate generated
- [ ] repository visibility changed to Public
- [ ] DNS / Lolipop domain mapping verified by successful HTTP(S) response

## Site launch content

- [x] bilingual home scaffold
- [x] Research Index scaffold
- [x] Tomb Fork Series scaffold
- [x] Methods / About / Editorial Policy / Corrections
- [x] favicon / default OGP / article OGP template
- [ ] remove or clearly quarantine all draft-only article placeholders from public launch surface
- [ ] decide whether launch is publication shell only or includes first research article
- [ ] if first article is included: Publish Gate pass
- [ ] if first article is included: Compliance Gate pass
- [ ] if first article is included: approved canonical SHA and public derivative correspondence recorded

## Search / discoverability

Current state: `site/robots.txt` intentionally contains `Disallow: /`.

Do not remove the no-index gate until:

- public launch surface is approved
- domain mapping works
- canonical URLs resolve correctly
- placeholder/draft pages are not unintentionally indexable
- sitemap policy is decided

## Final QA

- [ ] desktop visual QA
- [ ] mobile visual QA
- [ ] JA/EN language switch QA
- [ ] local and external link QA
- [ ] OGP / title / description QA
- [ ] canonical / hreflang QA
- [ ] no secrets / internal-only research / private evidence
- [ ] production candidate regenerated from final approved main SHA
- [ ] candidate digest recorded
- [ ] explicit human deploy approval

## Launch recommendation

Prefer a two-step launch:

1. publish the approved publication shell with no unapproved research article exposed as published content
2. promote the first research article only after its independent Publish + Compliance Gate cycle completes

This keeps infrastructure launch separate from investment-research publication approval.

## 更新履歴

- 2026-08-29 14:48 JST：初版。初回candidate、infrastructure、content、search、final QAのlaunch gateを固定。
