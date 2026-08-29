# Production Deploy Setup

ページ作成日時：2026-08-29 12:32 JST  
最終更新日時：2026-08-29 12:32 JST

## 1. Lolipop

Domain public folder:

`signaetstructura.com`

Production workflow uploads `./site/` to:

`signaetstructura.com/`

via FTPS port 21.

## 2. GitHub Repository Secrets

Repository:

`smilegroupsato/web-signaetstructura-com`

GitHub UI:

`Settings → Secrets and variables → Actions → Repository secrets`

Create:

- `FTP_SERVER`
- `FTP_USERNAME`
- `FTP_PASSWORD`

Do not commit these values into the repository.

`SERVER_DIR` is not required for this repository because `signaetstructura.com/` is intentionally fixed in the guarded workflow. If future infrastructure requires changing the directory dynamically, move it to an Environment variable or secret after review.

## 3. Production Environment

GitHub UI:

`Settings → Environments → New environment → production`

Recommended protection:

- add required reviewer if GitHub plan/settings permit
- prevent self-bypass where available
- deployment branches: main only

The workflow also requires two explicit inputs:

- `approved_sha`: approved commit SHA from main
- `confirm_production`: exact text `DEPLOY`

These application-level gates are additional to GitHub Environment protection.

## 4. Workflow

Production workflow:

`.github/workflows/deploy-production.yml`

It is `workflow_dispatch` only. A push to main does not deploy.

Flow:

1. enter approved main SHA
2. type `DEPLOY`
3. verify SHA exists in main history
4. validate production bundle
5. create file hash manifest
6. pass GitHub `production` Environment approval if configured
7. upload `site/` by FTPS
8. retain deployment manifest artifact

## 5. Current launch gate

Do not run production deploy until all of the following are true:

- repository scaffold PR merged to main
- domain DNS / Lolipop domain mapping confirmed
- FTP secrets configured
- `production` Environment configured
- robots policy deliberately changed from scaffold no-index state
- launch content passed Publish Gate and Compliance Gate
- final approved SHA recorded

## 更新履歴

- 2026-08-29 12:32 JST：初版。signaetstructura.com公開フォルダ、GitHub Secrets、production Environment、手動deploy手順を固定。
