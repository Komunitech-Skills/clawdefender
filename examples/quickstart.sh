#!/usr/bin/env bash
# Synthetic onboarding example; run from a reviewed checkout.
set -euo pipefail
umask 077
REPO="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
DEMO_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/rin-readme-clawdefender.XXXXXX")"
WS="$DEMO_ROOT/workspace"
mkdir -p "$WS"
export OPENCLAW_WORKSPACE="$WS"
printf 'Example artifacts: %s\n' "$DEMO_ROOT"
bash "$REPO/scripts/install.sh" --workspace "$WS"
bash "$REPO/scripts/status.sh" --workspace "$WS"
printf '%s\n' 'A plain synthetic greeting.' > "$DEMO_ROOT/input.txt"
bash "$REPO/scripts/sanitize.sh" --strict < "$DEMO_ROOT/input.txt" > "$DEMO_ROOT/clean.txt"
python3 - "$DEMO_ROOT/input.txt" "$DEMO_ROOT/clean.txt" <<'PY'
from pathlib import Path
import sys
assert Path(sys.argv[2]).read_bytes()==Path(sys.argv[1]).read_bytes()+b'\n'
PY
if python3 "$REPO/scripts/url_policy.py" 'http://127.0.0.1/'; then
  echo 'Unexpected acceptance of loopback URL' >&2; exit 1
fi
cat "$DEMO_ROOT/clean.txt"
printf 'Quickstart passed: %s (synthetic; see README for scope).\n' "clawdefender"
