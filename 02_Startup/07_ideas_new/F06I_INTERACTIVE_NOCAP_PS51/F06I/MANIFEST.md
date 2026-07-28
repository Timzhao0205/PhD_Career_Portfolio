# Package map

## Start and validation

- `START.ps1` — one-command start/resume launcher.
- `CHECK.ps1` — PS5.1, syntax, route, hash, count, override, and path checks.
- `PILOT.ps1` — offline fixtures for all eight pilots/stages and all hooks.
- `VALIDATE.ps1` — per-pilot, per-stage, and full-release validator.
- `CHECKPOINT.ps1` — validated stage/pilot telemetry and SHA-256 checkpoint.
- `COMPLETE.ps1` — final completion gate and `RUN_COMPLETE` writer.

## Claude Code project

- `CLAUDE.md` and `SESSION_POLICY.md` — main autonomous instructions.
- `.claude/settings.json` — full permissions, xhigh, hooks, and status line.
- `.claude/agents` — bounded Sonnet/high auxiliary agents.
- `.claude/hooks` — session/model, performance, failure, and stop logging.

## Research specification

- `RUNBOOK.md`
- `ROUTE.json`
- `MODEL_POLICY.md`
- `SOURCE_POLICY.md`
- `prompts\10_refresh.md` through `prompts\70_audit.md`

## Imported resources

- `src\06` — immutable 419-file completed Folder 06 corpus.
- `SOURCE_SHA256.json` — per-file frozen-corpus hashes.
- `INPUT_PROVENANCE.md` — archive and completed-work provenance.

## Runtime data

- `pilot` — per-stage pilots and offline hook self-tests.
- `outputs` — full-stage work and canonical release.
- `state` — session, checkpoints, model events, pauses, completion.
- `logs` — model/effort/performance and lifecycle JSONL.
- `quarantine` — rejected model-attempt evidence.

## Build fixtures

- `tests\fixtures` — deterministic accepted examples for every validator.
- `tests\BUILD_FIXTURES.py` — reproducible fixture builder; not required at
  runtime.
- `PACKAGE_SHA256.json` — immutable active-package hashes.

