# Changelog — clawdefender

## 1.0.4 (2026-07-17)
- docs: document --install as scan-first/safe-default (removes an installed path only if the skill fails the scan; a clean skill is never touched).

## 1.0.3 (2026-06-18)
- **Fix:** sanitize.sh now correctly flags injection (was failing on a non-executable clawdefender.sh → ran via bash).
- **Fix:** finding delimiter pipe→tab so commands/patterns containing | no longer corrupt scoring (--check-command integer error gone).

# Changelog — clawdefender

## 1.0.2 (2026-06-15)
- Packaging pass: README added, frontmatter standardized (license / lastUpdated), structure/PDA hygiene.
- Baseline entry — track future changes here going forward. The authoritative contract is SKILL.md.
