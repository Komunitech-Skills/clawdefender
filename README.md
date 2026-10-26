# clawdefender

> **Product classification:** Plugin · Activation: Passive + Manual · Model discovery: Explicit only

## Activation model

The OpenClaw plugin passively scans the prompt before an agent run and fails closed on scanner errors. The CLI remains available for explicit scans. Installing only the skill does not activate the plugin.

Preflight untrusted text, JSON and URLs with heuristic checks. Strict sanitization withholds content
when scanning fails or detects a threat.

## Use and expected result

Before consuming external content, or when validating a URL before a fetch. Use workspace-security
for workspace posture.

Example request: **“Scan this synthetic input in strict mode and report whether it can be
returned.”**

Expected behavior: Clean text content is returned with a trailing output newline (an existing
newline is retained too). Flagged input or malformed/scanner-unavailable input is withheld with
nonzero status.

The installer places this package in the explicit workspace. Current OpenClaw discovers its
`SKILL.md` directly and leaves `AGENTS.md` owner-controlled. The chat example is natural language, not a promise of a registered slash command.

## Quick start

From a reviewed checkout, run:

```bash
bash examples/quickstart.sh
```

The real local helper runs on synthetic data and checks the documented result. This is not an
assessment of production data or model answer quality. Success ends with `Quickstart passed:
clawdefender`.

## Install and operate

This is a private repository. Authenticate with an account or GitHub App that has read access, and
never place a token in a clone URL, prompt or log. Check out the reviewed full commit before running
repository code:

```bash
git clone https://github.com/rin-proxy/clawdefender.git
cd clawdefender
REF=FULL_40_CHARACTER_COMMIT
git checkout --detach "$REF"
```

```bash
WS=/absolute/agent/workspace
bash scripts/install.sh --workspace "$WS"
bash scripts/status.sh --workspace "$WS"
printf '{"text":"ordinary fixture"}\n' | bash scripts/sanitize.sh --strict
bash scripts/clawdefender.sh --check-url https://example.com
```

The commands above install the explicit CLI skill. To enable passive preflight, register the reviewed
checkout as an OpenClaw plugin and restart only the selected Gateway:

```bash
openclaw plugins install "$PWD" --force --accept-capabilities
openclaw config set plugins.entries.clawdefender.hooks.allowConversationAccess true
openclaw plugins inspect clawdefender
```

The plugin uses `before_agent_run`, scans the assembled prompt locally, and withholds it when the
scanner detects a threat, fails, times out, or exceeds `maxChars`. `blockedMessage` controls the
replacement message. The conversation-access setting is required because this hook must inspect the
assembled prompt; restart the selected Gateway after changing it. Keep the defaults unless the
selected agent has a reviewed reason to change them. A scanner pass is heuristic evidence, not a
security boundary.

For a reviewed pinned update or recovery:

```bash
bash scripts/update.sh --workspace "$WS" --repo https://github.com/rin-proxy/clawdefender.git --ref "$REF"
bash scripts/rollback.sh --workspace "$WS"
bash scripts/uninstall.sh --workspace "$WS"
```

## Operation and safety

Input: stdin for sanitizer or an explicit URL for preflight. Sanitizer exits 0 clean, 1 detected, 2
malformed/unavailable. URL policy covers allowed scheme/address forms; the transport still must
enforce redirects and peer checks.

`bash scripts/sanitize.sh --strict`; `bash scripts/clawdefender.sh --check-prompt`; `python3
scripts/url_policy.py URL`. The old `--install` action is deliberately unavailable.

Text inspection is local. URL preflight can resolve DNS but does not fetch a page. No runtime
sandbox or comprehensive prompt-injection prevention is established by a pass. Keep credentials out
of example commands and reports. Use synthetic data for verification; preserve owner data during
code maintenance.

Release evidence covers OpenClaw 2026.9.6. Bash, Python 3.11+, Git for lifecycle; standard Unix
utilities. Revalidate changed SDK/native contracts before using another OpenClaw version.

Recovery hint: Strict mode returned nothing → inspect exit/stderr before using content. URL rejected
→ check scheme, userinfo and private addresses. Do not bypass checks by executing an unreviewed
installer.

## Verification and evidence

```bash
bash test.sh
node tests/runtime.mjs
python3 scripts/check-docs.py
```

**Runtime evidence incomplete.** Strict success on the recorded synthetic battery was 11/12 before
and 12/12 after. Some attempted runs lack valid runtime evidence. They remain in the denominator;
the superiority claim is incomplete.

See [the full benchmark](BENCHMARK.md) for the exact comparison and limits. Installation alone does
not guarantee a better answer on every task.

### Current-version comparison status

The separate v3 three-repetition campaign was cancelled by the owner on 2026-10-26. The scoped
historical benchmark remains published with its original runtime and source pins. This release does
not claim statistically certified superiority on the current OpenClaw version; readiness is based on
deterministic tests, functional quickstart and lifecycle checks, and the explicitly scoped recorded
evidence.

Detailed documentation: [skill instructions](SKILL.md) · [acceptance and recovery](VERIFICATION.md)
· [tested compatibility](COMPATIBILITY.md) · [release notes](RELEASE-NOTES.md) ·
[changelog](CHANGELOG.md) · [commercial license](LICENSE-COMMERCIAL.md).
