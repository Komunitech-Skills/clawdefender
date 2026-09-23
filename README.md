# clawdefender

Preflight untrusted text, JSON and URLs with heuristic checks. Strict sanitization withholds content when scanning fails or detects a threat.

Navigation: [When to use it](#when-to-use-it) · [See the expected result](#see-the-expected-result) · [Quick start on synthetic data](#quick-start-on-synthetic-data) · [Using it from OpenClaw](#using-it-from-openclaw) · [Input, output and completion](#input-output-and-completion) · [Commands and configuration](#commands-and-configuration) · [Data and effects](#data-and-effects) · [Get the private repository](#get-the-private-repository) · [Compatibility](#compatibility) · [Install and verify](#install-and-verify) · [Update, rollback and remove](#update-rollback-and-remove) · [Validation](#validation) · [Shared installer source](#shared-installer-source) · [Troubleshooting](#troubleshooting) · [Related products and further reading](#related-products-and-further-reading) · [Measured before/after behavior](#measured-beforeafter-behavior)

## When to use it

Before consuming external content, or when validating a URL before a fetch. Use security-analysis for workspace posture.

## See the expected result

Example request: **“Scan this synthetic input in strict mode and report whether it can be returned.”**

Expected behavior: Clean text content is returned with a trailing output newline (an existing newline is retained too). Flagged input or malformed/scanner-unavailable input is withheld with nonzero status. This is an illustrative acceptance scenario, not a captured production conversation.

## Quick start on synthetic data

After obtaining a reviewed checkout using [private access](#get-the-private-repository), run:

```bash
bash examples/quickstart.sh
```

The script creates a private temporary workspace, prints its artifact directory and checks the result. Read [the example](examples/quickstart.sh) before running it. It keeps the synthetic artifacts for inspection; remove only the printed example directory when finished. It does not target your existing workspace or enable production services.

**What this example proves:** The real local helper runs on synthetic data and checks the documented result. This is not an assessment of production data or model answer quality.

Success ends with `Quickstart passed: clawdefender`; an unexpected result exits nonzero. Some examples deliberately provoke a failure and verify it is rejected. Run installation and the relevant functional probe below for your own selected instance.

## Using it from OpenClaw

The installer places this package under `skills/clawdefender` in the explicit workspace and adds its managed instruction pointer. Ask the agent in that workspace to read the matching SKILL.md and follow it. The chat example is natural language, not a promise of a registered slash command.

## Input, output and completion

Input: stdin for sanitizer or an explicit URL for preflight. Sanitizer exits 0 clean, 1 detected, 2 malformed/unavailable. URL policy covers allowed scheme/address forms; the transport still must enforce redirects and peer checks.

Typical workflow: select the intended input/workspace → inspect prerequisites → run the matching operation → inspect its real result and artifact → report success, missing evidence or failure. Clean text content is returned with a trailing output newline (an existing newline is retained too). Flagged input or malformed/scanner-unavailable input is withheld with nonzero status.

## Commands and configuration

`bash scripts/sanitize.sh --strict`; `bash scripts/clawdefender.sh --check-prompt`; `python3 scripts/url_policy.py URL`. The old `--install` action is deliberately unavailable.

## Data and effects

Text inspection is local. URL preflight can resolve DNS but does not fetch a page. No runtime sandbox or comprehensive prompt-injection prevention is established by a pass. Keep credentials out of example commands and reports. Use synthetic data for verification; preserve owner data during code maintenance.

## Get the private repository

Use an account or GitHub App with **read access** to this repository. Configure authentication on the machine running OpenClaw; a successful login on another machine does not transfer access. For an existing GitHub CLI login:

```bash
gh auth status
gh auth setup-git
gh repo clone rin-proxy/clawdefender
cd clawdefender
git fetch origin main
# Set REF to the reviewed full commit from the release manifest or PR.
REF=FULL_40_CHARACTER_COMMIT
git checkout --detach "$REF"
```

The placeholder must be replaced before execution. Do not paste tokens into clone URLs, agent prompts, config examples or logs. HTTPS updates below use the configured Git credential helper. A 404 on a private repo can mean missing access: check the account and repository permission first. Run installer commands from this checkout; `WS` always selects the target agent workspace explicitly.

## Compatibility

Release evidence covers OpenClaw 2026.9.3. Bash, Python 3.11+, Git for lifecycle; standard Unix utilities. Revalidate changed SDK/native contracts before using another OpenClaw version.

## Install and verify

Select an existing workspace explicitly; do not point a test at production. Review and check out the intended full commit before running its installer.

```bash
WS=/absolute/agent/workspace
bash scripts/install.sh --workspace "$WS"
bash scripts/status.sh --workspace "$WS"
printf '{"text":"ordinary fixture"}\n' | bash scripts/sanitize.sh --strict
bash scripts/clawdefender.sh --check-url https://example.com
```

## Update, rollback and remove

```bash
bash scripts/update.sh --workspace "$WS" --repo https://github.com/rin-proxy/clawdefender.git --ref "$REF"
bash scripts/rollback.sh --workspace "$WS"
bash scripts/uninstall.sh --workspace "$WS"
```

Install/reinstall is idempotent. Updates refuse unreviewed code drift; `--force` is an explicit override after review. Rollback refuses conflicting owner edits to `AGENTS.md`. Uninstall archives owned code outside discovery and preserves owner memory/configuration. `--keep-code` only removes the instruction pointer, so the skill remains discoverable. Installation status always separates code presence from runtime verification.

## Validation

```bash
bash test.sh
```

This entrypoint runs provider-free tests in temporary workspaces with a clean HOME and no inherited service credentials. Exit 0 means the listed tests passed; optional native tests print SKIPPED when dependencies are absent. It does not prove live model quality, delivery, or production readiness. See [VERIFICATION.md](VERIFICATION.md) for functional acceptance criteria, expected results and failure handling. CI runs this same entrypoint on Python 3.11 and Node 24. Recheck real SDK/native/model integration separately when changing those components.

## Shared installer source

Lifecycle code is generated from the reviewed skill-forge core; `vendor.json` records
source commits and file hashes. Run `python3 scripts/vendor.py check` to detect drift.
Keep this manifest with the package. Installation and pinned updates remain standalone;
no mutable upstream branch is fetched at runtime.

A suite-owned component can move to standalone ownership using
`bash scripts/install.sh --workspace /absolute/workspace --adopt-suite` after reviewing
the change. The transfer requires the suite's recorded code to be unchanged. Suite
rollback/uninstall will then preserve that standalone component. To return to suite
ownership, uninstall the standalone package (data remains preserved), then explicitly
install the selected suite component. Ordinary update/rollback commands remain available.

## Troubleshooting

Strict mode returned nothing → inspect exit/stderr before using content. URL rejected → check scheme, userinfo and private addresses. Do not bypass checks by executing an unreviewed installer.

Private clone returns 404 → check the authenticated account and repository read permission on this machine → repeat checkout. Installation rejected → inspect the reported workspace/ownership/drift conflict → resolve that exact cause and rerun status. A successful install receipt alone is not functional evidence; repeat the acceptance probe after recovery.

## Related products and further reading

[security-analysis](https://github.com/rin-proxy/security-analysis) · [code-reviewer](https://github.com/rin-proxy/code-reviewer). The [runbook catalog](https://github.com/rin-proxy/rin-runbook/blob/main/CATALOG.md) identifies active sources and presets. skill-curator is archived; new skill-management installs use skill-forge.

[Skill instructions](SKILL.md) · [Acceptance and recovery](VERIFICATION.md) · [Changelog](CHANGELOG.md) · [Commercial license](LICENSE-COMMERCIAL.md). Follow the repository's actual license/metadata and owner-granted access; this guide introduces no new license or redistribution grant. Detailed agent procedures stay in their existing reference files so discovery instructions remain concise.

## Release and maintenance checks

See [release notes](RELEASE-NOTES.md) and [tested compatibility](COMPATIBILITY.md).
Run `python3 scripts/check-docs.py` to validate local documentation links and declared interfaces;
CI also runs the synthetic quickstart. Private GitHub access is required to download releases.

## Measured before/after behavior

**Runtime evidence incomplete.** Strict success on the recorded synthetic battery was
11/12 before and 12/12 after. Some attempted runs lack valid runtime evidence. They remain in the denominator; the superiority claim is incomplete.

Failed strict trials across both arms: 1. Same-evaluator review classifies 0 as representation/fixture ambiguity, 1 as incomplete runtime, and 0 as substantive task failures. These interpretations do not replace original scores.

See [the full comparison, scope, source pin and reproducible evidence](BENCHMARK.md).
Installation alone does not guarantee a better answer on every task.
