# Package manifest

## Runtime

- `..\RUN_EVERYTHING.ps1` — single command
- `..\RUN_PHD_RESEARCH.ps1` — root dispatcher/parser check
- `..\RETRY_CLAUDE_AFTER_HANDOFF.md` — explicit retry command and guarantees
- `..\CLAUDE_RETRY_OVERRIDE_PATCH_2026-07-24.md` — patch and validation record
- `..\FABLE_PRIMARY_POLICY_PATCH_2026-07-24.md` — Fable final-result
  enforcement, temporary/auxiliary-model allowance, and full restart record
- `..\PACKAGE_TEST_REPORT_2026-07-24.md` — concrete source/state/test results
- `RUN_PHD_RESEARCH.ps1` — Claude-only stage runner/state machine
- `INVOKE_CLAUDE_CHILD.ps1` — live stream and per-event durable logger
- `TEST_CLAUDE_MODELS.ps1` — Sonnet 5/Fable 5 probes
- `VALIDATE_PACKAGE.ps1` — Windows PowerShell 5.1 package validator

There is no active alternate-agent client, MCP server configuration, or
automatic provider fallback.

## Durable transition

- `..\AGENTS.md`
- `AGENTS.md`
- `..\CHATGPT_WINDOWS_CONTINUE.md`
- `..\CHATGPT_WINDOWS_START_PROMPT.md`
- `state\CHATGPT_HANDOFF_STATE.json`
- `state\CHATGPT_HANDOFF.md`
- `state\OPERATION_LOG.csv`
- `state\CLAUDE_EVENT_LOG.jsonl`
- `state\MODEL_EFFORT_LOG.csv`
- `state\SESSION_INDEX.csv`
- `state\attempts`, `state\markers`, `state\sessions`,
  `state\checkpoints`, `state\generated_prompts`, `state\handoff_history`

## Evidence and outputs

- immutable originals under `inputs`
- stage instructions under `prompts`
- literature evidence under `evidence`
- mission deliverables under `outputs`
- raw run transcripts and rejected-attempt quarantine under `logs`
- pre-restart audit-only mission artifacts under `_history\r0`

`INPUT_CHECKSUMS.sha256` protects the supplied originals.
