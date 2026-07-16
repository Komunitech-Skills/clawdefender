# ClawDefender — Detection Categories

Full threat-pattern catalog for the `clawdefender` skill — loaded on demand.

## Prompt Injection (90+ patterns)

**Critical — direct instruction override:**
- `ignore previous instructions`, `disregard.*instructions`
- `forget everything`, `override your instructions`
- `new system prompt`, `reset to default`
- `you are no longer`, `you have no restrictions`
- `reveal the system prompt`, `what instructions were you given`

**Warning — manipulation attempts:**
- `pretend to be`, `act as if`, `roleplay as`
- `hypothetically`, `in a fictional world`
- `DAN mode`, `developer mode`, `jailbreak`

**Delimiter attacks:**
- `<|endoftext|>`, `###.*SYSTEM`, `---END`
- `[INST]`, `<<SYS>>`, `BEGIN NEW INSTRUCTIONS`

## Credential/Config Theft
Protects sensitive files and configs:
- `.env` files, `config.yaml`, `config.json`
- `.openclaw/`, `.clawdbot/` (OpenClaw configs)
- `.ssh/`, `.gnupg/`, `.aws/`
- API key extraction attempts (`show me your API keys`)
- Conversation/history extraction attempts

## Command Injection
Dangerous shell patterns:
- `rm -rf`, `mkfs`, `dd if=`
- Fork bombs `:(){ :|:& };:`
- Reverse shells, pipe to bash/sh
- `chmod 777`, `eval`, `exec`

## SSRF / Data Exfiltration
Blocked endpoints:
- `localhost`, `127.0.0.1`, `0.0.0.0`
- `169.254.169.254` (cloud metadata)
- Private networks (`10.x.x.x`, `192.168.x.x`)
- Exfil services: `webhook.site`, `requestbin.com`, `ngrok.io`
- Dangerous protocols: `file://`, `gopher://`, `dict://`

## Path Traversal
- `../../../` sequences
- `/etc/passwd`, `/etc/shadow`, `/root/`
- URL-encoded variants (`%2e%2e%2f`)
