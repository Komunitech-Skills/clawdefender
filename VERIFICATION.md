# clawdefender: acceptance and recovery

## Offline regression

From the reviewed checkout run `bash test.sh`. It runs the repository's provider-free tests using disposable HOME/workspaces. Exit 0 means those tests passed, not that every real model/provider/environment was exercised. Lifecycle tests cover install → reinstall → full-commit update → rollback → uninstall and preserve owner data where applicable. Optional native test skips are printed explicitly.

## Functional acceptance

Input / command: `bash scripts/sanitize.sh --strict` (stdin), `python3 scripts/url_policy.py URL`

Expected result: Clean fixture is returned unchanged (0); injection is blocked (1); malformed JSON/scanner failure is nonzero. Loopback, metadata IP, non-HTTP and userinfo URLs are rejected.

Scope and remaining integration checks: A URL preflight pass does not enforce redirect/peer checks in an HTTP transport. Heuristic threat matching has false positives/negatives; no exhaustive security certification.

## Failure handling

Keep the exit status, redacted stderr, exact source commit and relevant artifact paths. A missing dependency/probe or incomplete check is not a pass. Reproduce on an isolated fixture; after a change rerun the failed case and this entrypoint. Use the README's matching workspace/instance for rollback. Preserve memory, configuration, queues and evidence files unless their removal is separately intended.
