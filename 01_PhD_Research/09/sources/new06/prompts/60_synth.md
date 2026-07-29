# 60_synth — portfolio synthesis

## Purpose

Create a coherent decision package for the exact selected 24 and exact top
ten, integrating P4-P6 evidence without silently changing identities.

## Inputs allowed

- `outputs/20_p4`
- `outputs/30_redteam`
- `outputs/40_select`
- `outputs/45_packs`
- `outputs/50_deep`

Do not read historical P7/P8 outputs under `src/06`.

## Pilot

Build two prototype idea cards and two matrix rows, then test exact ID,
ranking, numeric, source, and roadmap consistency. Save only under
`pilot/60_synth`.

## Full outputs under `outputs/60_synth`

- `PORTFOLIO.json`: `items` containing the exact 24 ordered items and
  `top_10_deep_dives` containing the exact ten deep-dive IDs, retaining
  machine-checkable selection fields.
- `00_EXECUTIVE.md`: recommendation, tiers, uncertainty, resource allocation.
- `01_IDEA_CARDS.md`: exactly 24 evidence-grounded cards.
- `02_MATRIX.csv`: one header plus exactly 24 data rows.
- `02_MATRIX.md`: readable comparison and scoring notes.
- `03_MAP.md`: technical/market frontier and platform adjacencies.
- `04_ROADMAP.md`: 2026-2030 validation roadmap with budgets, pass thresholds,
  and kill thresholds.
- `05_MODEL_REPORT.md`: requested route and pointers to telemetry; never invent
  actual identity or effort.
- `RESULT.json`: `stage:"60_synth"`, `status:"COMPLETE"`, outputs and checks.

If a literal evidence or constraint violation requires changing the final 24
or top ten, set `RESULT.json` to `status:"BLOCKED"` and return to Stage 40;
never silently substitute an idea.
