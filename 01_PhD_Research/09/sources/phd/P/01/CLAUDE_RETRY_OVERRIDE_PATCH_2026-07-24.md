# Claude retry override patch — 2026-07-24

> Historical note: the active workflow was later reset to stage 00. This file
> documents the older retry feature; current policy and state are defined by
> `FABLE_PRIMARY_POLICY_PATCH_2026-07-24.md`.

## User authorization

The user reported that Claude usage remains and requested another PowerShell
run after `10a_literature_gan` reached `CHATGPT_HANDOFF_REQUIRED`.

## Preserved state

- `state\markers\00_inventory.done.json` remains authoritative.
- Both prior `10a_literature_gan` attempts, raw streams, model reports,
  generated prompts, checkpoints, operation/model/session logs, and rejected
  outputs remain present.
- The current handoff is not reset during packaging.
- On the first run with the new switch, the existing handoff is copied to
  `state\handoff_history` before any live-attempt state is written.

## New behavior

`-RetryClaudeAfterHandoff` is accepted and forwarded by all three PowerShell
launch layers. The override:

- requires explicit invocation;
- starts a fresh Claude session rather than resuming the rejected session;
- continues the earliest incomplete stage from durable files;
- numbers the next attempt after the prior global attempt;
- records retry cycle, cycle attempt, model, effort, downgrade count, flags,
  stream, prompt, checkpoint, archive, and next action;
- retains the one-retry-then-handoff model-integrity policy in every newly
  authorized cycle.

Normal runs without the switch remain fail-safe: a saved handoff is preserved
and Claude is not restarted.

## Command

```powershell
powershell -ExecutionPolicy Bypass -File .\RUN_EVERYTHING.ps1 -RetryClaudeAfterHandoff
```

## Validation scope

The rebuild verifies PowerShell syntax, JSON, CSV logs, immutable input
checksums, preserved marker hashes, absence of alternate-provider/MCP runtime
paths, switch forwarding, retry-cycle transitions, unique prompt/log paths,
archive integrity, and extracted-package byte identity. No paid live Claude
research call is made during packaging.
