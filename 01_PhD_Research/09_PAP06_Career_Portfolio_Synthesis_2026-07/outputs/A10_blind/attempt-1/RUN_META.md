# RUN_META — A10_blind FULL attempt-1

- Stage: `A10_blind`
- Mode: `FULL`
- Attempt: `1`
- Named agent (worker): `pap06-fable-xhigh`
- Requested model: `Fable 5`
- Requested effort: `xhigh`
- Observed model: the runtime system prompt identifies the model as
  "Fable 5" (model ID `claude-fable-5`). This is a runtime self-identification,
  not an independent provider-side telemetry record.
- Observed effort: `NOT_EXPOSED` (the runtime does not expose an effort
  level; never guessed)
- Start time: `NOT_EXPOSED` (runtime does not expose wall-clock timestamps to
  the worker; the environment date context is 2026-07-28)
- End time: `NOT_EXPOSED`

## Files read (with read windows)

1. `state/CURRENT_TASK.md` — full (37 lines)
2. `workflow/stages/A10_blind.md` — full (37 lines)
3. `SOURCE_POLICY.md` — full
4. `LIT_POLICY.md` — full
5. `MODEL_POLICY.md` — full
6. `MODEL_PLAN.md` — full
7. `evidence/blind/MANIFEST.json` — full (35 lines)
8. `evidence/blind/POOL_1.json` — full, windowed reads: lines 1–400, 400–900,
   900–1400, 1400–1900, 1900–2400, 2400–2558 (EOF). 42 records
   (P3R2-A-01..A-22, P3R2-B-01..B-20).
9. `evidence/blind/POOL_2.json` — full, windowed reads: lines 1–500, 500–1000,
   1000–1520, 1520–2040, 2040–2559, 2559–2681 (EOF). 42 records
   (P3R2-B-21, P3R2-B-22, P3R2-C-01..C-22, P3R2-D-01..D-18).
10. `evidence/blind/POOL_3.json` — full, windowed reads: lines 1–500, 500–1020,
    1020–1538, 1538–2058, 2058–2524 (EOF). 42 records
    (P3R2-D-19, P3R2-D-20, P3R2-E-01..E-14, P3R2-F-01..F-23,
    P3R2-G-01..G-03).

Not read (per blind restrictions): `sources/`, `archive/`, `verification/`,
any prior ranking, any other stage output, and the pilot directory's
`SELECTION`/`TOP10`/`METHOD` content (no file under `pilot/` was opened).

## Files written

All inside `outputs/A10_blind/attempt-1/` only:

1. `SELECTION.json` — 24 unique ranked objects with nine-component scores,
   uncertainty, principal risk, falsifier each
2. `TOP10.json` — 10 unique IDs, all contained in the 24, with rank and reason
3. `METHOD.md` — rubric, tie handling, 126/126 coverage proof, limitations,
   independence statements
4. `RUN_META.md` — this file
5. `SELF_CHECK.md` — acceptance checklist

## Web activity

`NONE`. No WebSearch and no WebFetch calls were made in this stage (blind
restriction honored).

## Limitations

- Judgments rely exclusively on candidate-record content; no external
  verification was permitted or performed. Source IDs (e.g., L02-043) are
  quoted from the records, not independently checked.
- Effort level and timestamps are not exposed by the runtime; recorded as
  `NOT_EXPOSED` per MODEL_POLICY (a requested configuration proves intent,
  not provider-side execution).
- Duplicate-cluster consolidation (many records are explicit merges of
  earlier seeds) required judgment about which variant represents each
  concept; every such call is disclosed in METHOD.md's disposition table.
- No provider safeguards, account limits, organization restrictions, or
  missing-evidence blockers were encountered; the run completed normally.
