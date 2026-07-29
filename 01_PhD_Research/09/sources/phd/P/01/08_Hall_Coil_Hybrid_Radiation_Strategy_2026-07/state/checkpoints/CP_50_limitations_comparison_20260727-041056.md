# Checkpoint — stage 50 (`50_limitations_comparison`) complete

- **Stage / gate:** 50 — Fable limitations, alternatives, and falsification.
  All acceptance gates satisfied; validated 33/33 by
  `tools\validate_50_outputs.py`.
- **Model/effort:** Fable 5, xhigh (stage-assigned; outputs and final main
  response produced by Fable 5; no auxiliary models used this stage).

## Completed outputs and counts

1. `outputs\05_LIMITATIONS_AND_FAILURE_MODES.md` — 18 failure modes
   (FM-01…FM-18; gate ≥15), each with cause/symptom/detectability/
   consequence/mitigation/residual-risk/test; explicit coverage map onto
   all 15 stage-required areas; §3 potential separated into 6 value
   classes, each conditional on a measurable advantage + identifiable
   calibration; §3.6 narrowest-defensible-contribution verdict after the
   2007 ([H006]/[H007]) / 2022 ([H003], [H004]) / 2025 ([H001], [H002])
   direct prior art — broad hybrid idea plainly stated as NOT novel;
   §4 seven counterexamples where a simpler sensor wins.
2. `outputs\05_TECHNOLOGY_COMPARISON.csv` — 15 rows (gate ≥10), exact
   20-column stage header, built by
   `tools\build_05_technology_comparison.py`; all required technology
   classes present (hybrid; GaN/InSb/metal/graphene Hall; B-dot/Mirnov;
   Rogowski/CT+DCCT; fluxgate; TMR; AMR; planar Hall; FOCS; NMR; SQUID;
   NV); `unknown`/`not_applicable` used instead of fake precision;
   5 rows explicitly marked COUNTEREXAMPLE (simpler sensor wins); all
   evidence_ids resolve against ledger + evidence map.
3. `outputs\05_FALSIFICATION_TESTS.md` — 12 tests FT-01…FT-12 ordered
   cheapest→most expensive (desk → simulation → bench → machine-piggyback
   → irradiation), each with hypothesis/setup/reference/metric/threshold/
   confounders/decision/evidence; FT-01…FT-10 are radiation-free, each
   with a stop/descope decision (gate: project can stop before expensive
   radiation work); FT-11/FT-12 remain collaborator-led behind G0–G3 per
   stage-30 §9.4.

## Analyses completed

- Failure analysis grounded line-by-line in stage-20 identifiability
  results (Theorem 1, CASE A–J), stage-30 architecture/risk register
  (RR-01…RR-24 cross-referenced), and stage-10D evidence (claims cited by
  ID throughout; zero invented IDs, validator-enforced).
- Technology comparison consumes 10C alternative-technology evidence
  (P058–P073 cluster) plus the radiation lane; species discipline
  maintained (TMR/AMR gamma-only explicitly not extrapolated to neutron).

## Unresolved questions / honest limitations

- All absence claims (C03, C06, C14, C21, C32, C36 gaps) remain bounded
  by the mission's documented search scope.
- Single-source dependencies persist: [R071] (metallic-Hall null),
  [H059] (coil-calibrates-Hall precedent).
- Cost categories are order-of-magnitude labels; no vendor pricing in
  evidence.
- GaN Hall-plate radiation drift magnitudes remain Unknown (C14); FT-03
  therefore sweeps drift rates instead of assuming one.

## Files safe to reuse

- All three `05_*` outputs; `tools\build_05_technology_comparison.py`;
  `tools\validate_50_outputs.py` (33 checks). No sibling/prior-stage file
  modified.

## Next action

Run/resume the parent launcher into `60_research_program` (consumes the
C36/§3.6 narrowest-contribution verdict, the FT ladder ordering, and the
stage-40 gate sequence; model/effort per `MODEL_POLICY.md`).
