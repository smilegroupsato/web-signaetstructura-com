# SIGNA ET STRUCTURA Production Publishing v0.1

ページ作成日時：2026-08-29 12:24 JST  
最終更新日時：2026-08-29 12:24 JST

## 1. Goal

GitHub上の承認済みpublic artifactを、明示的なhuman approval後にLolipop productionへ公開する。

mainへのmerge、preview artifact生成、production candidate生成は、production公開を意味しない。

## 2. Flow

```text
feature branch
  -> PR validation
  -> main
  -> production candidate artifact
  -> candidate SHA / manifest固定
  -> human publish approval
  -> explicit deploy workflow
  -> Lolipop production
  -> live verification
  -> publication receipt
```

## 3. Production candidate

candidateは`site/`の完全snapshotであり、少なくとも以下を持つ。

- source commit SHA
- candidate artifact digest
- generated_at
- file manifest
- robots policy
- target host identifier

candidate生成時点ではFTP/FTPS接続を行わない。

## 4. Human approval boundary

初期運用ではproduction deployはGitHub Actions `workflow_dispatch`のみとし、次を入力・確認する。

- approved source SHA
- candidate digest
- target environment: production
- operator acknowledgment

GitHub Environment `production` のrequired reviewerを利用できる場合は設定する。

## 5. Secrets

Lolipopの接続情報はGitHub Actions Secrets / Environment Secretsにのみ保存する。

想定名：

- `LOLIPOP_FTPS_HOST`
- `LOLIPOP_FTPS_USERNAME`
- `LOLIPOP_FTPS_PASSWORD`
- `LOLIPOP_REMOTE_DIR`

repo、Markdown、issue、workflow logへ実値を書かない。

## 6. Deploy behavior

- candidate SHAと指定SHAが一致しない場合は停止
- validationを再実施
- `site/`のみをdeploy
- production rootを明示的に固定
- dangerous delete / mirrorはMVPでは使わない
- upload完了後に主要URLをHTTP GETで確認

## 7. Receipt

成功時に少なくとも以下をartifactまたはrecordsへ残す。

```yaml
site: signaetstructura.com
source_sha: <sha>
candidate_digest: <sha256>
deployed_at: <JST timestamp>
target: production
verification:
  root: pass
  ja: pass
  en: pass
operator: <github actor>
```

個別Research記事のpublication receiptは、SC Markets Research側のpublication_id / approved SHAと対応させる。

## 8. Rollback

初期段階のrollbackは、過去の承認済みcandidateを指定して再deployする。

production filesystem上で直接編集しない。

## 9. Current safety state

この文書作成時点ではproduction deploy workflowは**未有効**。

Lolipop secrets / target remote directoryが確認され、明示的な承認を得るまで、外部書き込みを行うworkflowを追加しない。

## 更新履歴

- 2026-08-29 12:24 JST：v0.1作成。candidate固定、human approval、secret境界、receipt、rollbackを定義。
