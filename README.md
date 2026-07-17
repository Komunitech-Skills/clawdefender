# 🛡️ clawdefender

> 🔒 **Diaudit & aman** — lolos skill-gate 100/100 · berjalan **lokal-saja**: tanpa panggilan jaringan, tanpa `eval`/kode ter-obfuscate. Semua kode terbuka & bisa kamu verifikasi sendiri. _(Audit keamanan: 2026-07-17)_

Security scanner and input sanitizer for AI agents. Detects prompt injection, command injection, SSRF, credential exfiltration, and path traversal attacks. Use when (1) installing new skills from ClawHub, (2) processing external input like emails, calendar events, Trello cards, or API responses, (3) validating URLs before fetching, (4) running security audits on your workspace. Protects agents from malicious content in untrusted data sources.

**Version:** 1.0.2 · **Triggers:** security scan, prompt injection, input sanitizer, skill audit, validate URL, check for malware

## Usage
Full guide and procedure: see **SKILL.md**. Bundled scripts (if any) live in **scripts/**; deep reference material in **references/** (loaded on demand).

## Install
    openclaw skills install git:rin-proxy/clawdefender

Or copy this folder into your OpenClaw workspace/skills/ directory.

---
*README for the clawdefender skill. The authoritative contract is SKILL.md.*
