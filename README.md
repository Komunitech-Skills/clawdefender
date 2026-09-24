# clawdefender

Preflight untrusted text, JSON and URLs with heuristic checks. Strict sanitization withholds content
when scanning fails or detects a threat.

## Use and expected result

Before consuming external content, or when validating a URL before a fetch. Use security-analysis
for workspace posture.

Example request: **“Scan this synthetic input in strict mode and report whether it can be
returned.”**

Expected behavior: Clean text content is returned with a trailing output newline (an existing
newline is retained too). Flagged input or malformed/scanner-unavailable input is withheld with
nonzero status.

The installer places this package under `skills/clawdefender` in the explicit workspace and adds its
managed instruction pointer. Ask the agent in that workspace to read the matching SKILL.md and
follow it. The chat example is natural language, not a promise of a registered slash command.

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

Release evidence covers OpenClaw 2026.9.3. Bash, Python 3.11+, Git for lifecycle; standard Unix
utilities. Revalidate changed SDK/native contracts before using another OpenClaw version.

Recovery hint: Strict mode returned nothing → inspect exit/stderr before using content. URL rejected
→ check scheme, userinfo and private addresses. Do not bypass checks by executing an unreviewed
installer.

## Verification and evidence

```bash
bash test.sh
python3 scripts/check-docs.py
```

**Runtime evidence incomplete.** Strict success on the recorded synthetic battery was 11/12 before
and 12/12 after. Some attempted runs lack valid runtime evidence. They remain in the denominator;
the superiority claim is incomplete.

See [the full benchmark](BENCHMARK.md) for the exact comparison and limits. Installation alone does
not guarantee a better answer on every task.

Detailed documentation: [skill instructions](SKILL.md) · [acceptance and recovery](VERIFICATION.md)
· [tested compatibility](COMPATIBILITY.md) · [release notes](RELEASE-NOTES.md) ·
[changelog](CHANGELOG.md) · [commercial license](LICENSE-COMMERCIAL.md).
