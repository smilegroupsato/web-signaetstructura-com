# Production publish requests

This directory is the explicit production-deploy trigger for ChatGPT/GitHub-operated publication.

Normal pushes or merges to `main` do not deploy production through this lane. Deployment occurs only when `publication/publish-requests/active.json` is changed on `main` and the request passes the workflow checks.

Required fields:

- `request_id`: unique publication request ID
- `target_sha`: exact approved `main` commit whose `site/` tree will be deployed
- `confirm`: must be exactly `DEPLOY`
- `approved_at_jst`: human approval timestamp in JST
- `approved_by`: approving human/operator
- `note`: optional audit note

The workflow verifies that `target_sha` is an ancestor of current `main`, checks the production bundle, records a deployment manifest, and deploys exactly the requested SHA to the `production` environment by FTPS.

The request file is an execution instruction, not a content canonical source. Article canonical sources remain in the research repository and approved Web artifacts remain in the site history.
