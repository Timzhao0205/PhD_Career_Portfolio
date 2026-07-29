# RUN_META — A10_blind pilot attempt-1

PILOT SAMPLE — NOT FINAL

- Stage: `A10_blind`
- Mode: `PILOT`
- Attempt: `1`
- Target directory: `pilot/A10_blind/attempt-1/`
- Named agent: `pap06-fable-xhigh`
- Requested model: `Fable 5`
- Requested effort: `xhigh`
- Observed model: `Fable 5` (model ID `claude-fable-5`) — explicitly declared
  in the runtime environment/system prompt. Note: this is a harness-declared
  identity, an explicit runtime exposure per MODEL_POLICY, not an independent
  measurement of provider-side execution.
- Observed effort: `NOT_EXPOSED` (the runtime does not expose an effort
  setting; not guessed).
- Start time: `NOT_EXPOSED` (no clock available to the worker; environment
  date is 2026-07-28).
- End time: `NOT_EXPOSED` (same limitation).

## Files read (all read-only, all allowed)

1. `state/CURRENT_TASK.md` — task card.
2. `workflow/stages/A10_blind.md` — stage specification.
3. `SOURCE_POLICY.md`, `LIT_POLICY.md`, `MODEL_POLICY.md`, `MODEL_PLAN.md` —
   root policies.
4. `evidence/blind/MANIFEST.json` — full file.
5. `evidence/blind/POOL_1.json` — leading window (lines 1-200) covering
   entries 1-2 (`P3R2-A-01`, `P3R2-A-02`) in full.
6. `evidence/blind/POOL_2.json` — leading windows (lines 1-280) covering
   entries 1-2 (`P3R2-B-21`, `P3R2-B-22`) in full.
7. `evidence/blind/POOL_3.json` — leading windows (lines 1-280) covering
   entries 1-2 (`P3R2-D-19`, `P3R2-D-20`) in full.

Read windows incidentally included the start of each shard's third entry;
those candidates were not evaluated or used. No file under `sources/`,
`archive/`, `outputs/`, `verification/`, or any other pilot directory was
read. No prior or new ranking of any kind was read.

## Web activity

NONE. WebSearch and WebFetch were not used (prohibited in this blind stage and
not invoked).

## Files written (all inside the target directory)

- `pilot/A10_blind/attempt-1/SELECTION.json`
- `pilot/A10_blind/attempt-1/TOP10.json`
- `pilot/A10_blind/attempt-1/METHOD.md`
- `pilot/A10_blind/attempt-1/RUN_META.md` (this file)
- `pilot/A10_blind/attempt-1/SELF_CHECK.md`

Nothing outside the target directory was created or modified.

## Limitations

- Blind stage: all candidate market/technical claims are unverified
  candidate-internal evidence; lane source IDs cited by candidates were not
  opened. See METHOD.md limitations.
- Shard SHA-256 hashes were not recomputed (no code execution under the
  native contract); manifest row counts (42 per shard, 126 total, 126 unique
  IDs) are taken from `MANIFEST.json` as stated, not independently recounted
  in the pilot.
- No clock access: wall-clock start/end times could not be recorded and were
  not fabricated.
- Effort setting is not observable at runtime; requested-vs-observed effort
  evidence is therefore intent-only, per MODEL_POLICY.
- No retries, provider safeguards, account limits, or organization
  restrictions were encountered during this run.
