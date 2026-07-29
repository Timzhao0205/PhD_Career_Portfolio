# Model report — requested route and telemetry pointers

This report records what was requested and where the observed evidence
lives. Per MODEL_POLICY.md, prompt text is never model evidence; actual
identity and effort are established only by hooks and status telemetry.
This document therefore asserts no identity from its own text.

## Requested route (ROUTE.json)

- Route: `F06_INTERACTIVE_NOCAP_PS51_V1`, execution surface
  `claude_code_interactive`.
- Main session request: model `fable` (required observed family
  "Fable 5"), effort `xhigh`, permission mode `bypassPermissions`,
  session persistence on; no monetary stop, turn limit, or time limit.
- Every stage's `main_final_model` is `fable` at `xhigh` with a
  required pilot; auxiliary agents (`source-retriever`,
  `mechanical-auditor`) are Sonnet/high, retrieval- and
  mechanical-checks-only, and never produce accepted judgments.

## Where the observed evidence lives

- `logs/status.jsonl` — status-line telemetry snapshots: model_id,
  exposed effort, token totals, context use, duration, cost telemetry,
  Claude Code version. The newest line at any moment is the current
  identity evidence.
- `logs/status.last` — the deduplication signature of the most recent
  snapshot (model_id|effort|cost|duration|tokens).
- `state/ACTIVE_SESSION.json` — the newest SessionStart record
  (source, session_id, model observed at start when exposed).
- `state/stages/<stage>.json` — each full-stage checkpoint records the
  model/effort observed at validation time plus SHA-256 hashes of every
  output file; `pilot/<stage>/PILOT_COMPLETE.json` records the same for
  pilots. CHECKPOINT.ps1 refuses to create a checkpoint unless the
  newest telemetry shows the required family and effort (or honestly
  NOT_EXPOSED with requested xhigh).
- `logs/events.jsonl` — hook events: session starts/stops, subagent
  boundaries, compaction, tool failures, and adjudication records.

## Integrity events affecting this run (recorded, not summarized away)

- `state/FABLE_EVENTS.json` holds one model-integrity event
  (2026-07-28T06:33:59Z): during a context-compaction step the harness
  observed `claude-opus-5`. The event history is preserved unreset
  under the `first_retry_second_pause` policy.
- Adjudication: `quarantine/model_event_20260728/ADJUDICATION.json`
  records the user's explicit classification of that event as an
  auxiliary compaction-model use only — no interactive turn, tool
  call, or file write executed under the non-Fable model; no stage
  checkpoint carries non-Fable telemetry; the transient retry flag was
  cleared after telemetry re-verified the required family at xhigh.
  The one file open during the event window (D01.md draft) was fully
  re-verified by the main session before acceptance into INDEX.json.
- `quarantine/package_repair_20260728/REPAIR.json` records the
  hook-script repairs (strict-mode-safe SessionStart/Stop handlers,
  event-log lock retries) and the settings.json rewrite by the host,
  with pre-repair manifest snapshot and old/new hashes.

## Verification pointers for an auditor

1. For each of the eight stage markers under `state/stages/` and six
   pilot markers, confirm `model_observed` matches the required family
   and `effort_observed` is `xhigh` (or `not_exposed` with
   `effort_requested` = `xhigh`).
2. Re-run `CHECKPOINT.ps1 -Stage <name> -Verify` per stage: it
   revalidates outputs and rechecks every recorded hash.
3. Cross-check `logs/status.jsonl` timestamps against stage
   `validated_at_utc` values for continuity.
4. Read the two quarantine records above; confirm
   `state/MODEL_PAUSE.json` does not exist and
   `state/FABLE_EVENTS.json` still shows count 1.

Nothing in this report claims an identity; it points to where identity
is recorded.
