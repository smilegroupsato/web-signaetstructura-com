# Publishing

SIGNA ET STRUCTURAのpublic publication layer。

ページ作成日時：2026-08-28 23:32 JST
最終更新日時：2026-08-28 23:32 JST

## Boundary

内部Research / Evidence / Gate / Approvalの正本は `smilegroupsato/sc-crypto-ops`。

このrepositoryへ入れるのは、外部公開可能と判断されたpublic edition、public data、figure、site source、release evidenceのみ。

## Target flow

```text
sc-crypto-ops approved publication
→ public edition import
→ JA / EN validation
→ figure/data validation
→ candidate build
→ visual QA
→ candidate SHA fixation
→ human approval
→ explicit deploy
→ production verification
→ release receipt
```

## Directories

- `templates/` — public article templates
- `schemas/` — machine validation contracts
- `requests/` — future prepare/promote requests
- `releases/` — public release receipts

GitHub commitやmain mergeだけでproduction公開を許可しない。
