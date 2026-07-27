# Checkpoint — stage 30 (`30_radiation_compensation`)

- **Stage / gate:** 30 complete; all acceptance gates satisfied.
- **Model/effort:** Fable 5 / xhigh (requested = reported; no auxiliary
  models used; downgrade count this cycle: 0).
- **Timestamp:** 2026-07-27 03:35 (local).

## Completed outputs

1. `outputs\03_RADIATION_COMPENSATION_ARCHITECTURE.md` — 8-option
   comparison (A–G + added layered option H), MVD ("anchored hybrid",
   A+C+zero-field epochs) and higher-accuracy ("triangulated self-test
   hybrid", +B+E, +D at top tier) recommendations, full Hall/coil/
   reference parameterization, block-level interfaces, embedded-winding
   deep analysis (gain-product-only identifiability, offset structural
   blindness, frequency plan, heating ceiling, triangle-closure test,
   winding's own reference problem), 4-mode compensation logic,
   uncertainty budgets, in-situ vs ex-situ mechanism table, 4 budget
   tiers (T0–T3) with stop/go gates G0–G5, HSX-paper decoupling
   statement (§9.4, per conflict C6).
2. `outputs\03_SIMULATION_AND_VALIDATION_PLAN.md` — full state-space
   truth-model spec, parameter schema with species-vector and
   placeholder-basis enforcement, 12 scenarios (S1–S12) with
   pre-registered stage-20 expected behaviors, 14 fault injections,
   8 metrics incl. non-identifiability honesty test T-NI, test suite
   bound to `tools\observability_rank_tests.py` regression, 7-rung
   experimental ladder with standards, sample sizes (rung 5: ≥5+≥3 per
   material, R003 9-sample precedent), repeatability, acceptance
   thresholds and stop rules, module interface spec, evidence-class
   boundary table.
3. `outputs\03_RADIATION_RISK_REGISTER.csv` — 24 rows (RR-01…RR-24),
   exact 15-column stage header, parse-verified, unique IDs, all
   evidence_ids resolve.

## Validation

`tools\validate_30_outputs.py`: **13/13 PASS** (existence/nontriviality;
exact CSV header; 24 rows; unique risk_ids; all evidence_ids resolve;
enum/gate vocab; 54+10 bracketed source IDs and 24+11 claim IDs in the
two MDs all resolve against `01_SOURCE_LEDGER.csv` /
`01_EVIDENCE_MAP.csv`; zero invented IDs).

## Reusable tools kept

- `tools\build_03_risk_register.py` (deterministic CSV source).
- `tools\validate_30_outputs.py` (revalidation for stages 70/80).

## Files safe to reuse

All stage 00/10A–10D/20 outputs unchanged; stage-30 outputs final.

## Unresolved questions (carried forward, not blockers)

- GaN Hall-plate neutron drift magnitudes remain Unknown (C14) — every
  cadence/threshold is provisional until validation rung 5.
- Witness-channel basis rests on single source R071 (C18).
- No dose-to-RIEMF or dose-to-effective-area curves exist (C19).

## Next action

Run/resume the parent one-command launcher into
`40_applications_collaboration` (Sonnet 5 / xhigh per MODEL_POLICY.md
"Applications/collaboration scoring" row).
