# Phase 0 — benchtop dipstick plan

Goal: derisk the two lowest-confidence items (electrode drift, chaos
rejection) for ≤$400 before any packaging spend. Pass/fail gates map
to MASTER_STATE.json.

Fixture: IDE coupon + NTC on an acrylic rod, clamped on the ring
stand; FDC2214EVM on the bench (<10 cm leads); GUI → CSV.

## P0-E0 — Sanity, drift, parasitics  [gate: P0_drift_pass]
1. Log each coupon in air → DI water → IPA; confirm monotone, gross
   discrimination, and record noise floor per pitch (sets the
   estimator histogram bin width).
2. 30 min continuous in DI water at constant temp; drift target:
   ≤ FDC noise-equivalent, hard fail if > 0.5 % ABV-equivalent.
   Compare parylene-C vs 422B silicone vs bare-ENIG control coupon.
3. Parasitics: touch glass, ground yourself, wave hand at 5 cm — with
   and without guard grounded. Guard must reduce hand sensitivity by
   ≥10×.
Pass: drift + parasitics within budget on ≥1 pitch → freeze pitch.

## P0-E1 — Static calibration surface  [gate: P0_static_cal_pass]
1. Gravimetric standards: 0/10/20/30/40/50/60 % ABV from 190-proof +
   DI on the 0.01 g balance (record masses; density-convert to % v/v).
   Fresh standards each session — evaporation shifts 40 % overnight.
2. For each standard: seal sample around probe (small jar), log C + T
   continuously while cooling 25 °C → −5 °C in the salt-ice bath.
   One run per standard = full temperature trace for free.
3. Fit ε(T, ABV) with `50_ANALYSIS/calibration_fit.py` (≤3×3 poly);
   invert to ABV(ε, T). Also extract NTC lag τ by step test
   (room → ice bath plunge).
Pass: residual ≤1.0 % ABV over the grid; T-comp residual ≤0.5 % ABV.

## P0-E2 — Dynamic dilution, hard ground truth  [gate: P0_dynamic_tracking_pass]
1. 60 mL whisky (known ABV) at recorded temp + ~150 g weighed ice;
   stir realistically; log at max rate for 60–90 s.
2. End: strain, WEIGH surviving ice → melted mass → exact dilution →
   exact final ABV by mass balance.
3. Compare: sensor live estimate vs melt-model estimate vs mass-
   balance truth. Repeat across 3 whiskies (A-002) + 1 pure-ethanol
   control.
Pass: converged sensor ABV within ±1.5 % of mass-balance truth on
≥4/5 runs; melt-model divergence flag behaves sensibly.

## P0-E3 — Chaos testing  [gate: P0_chaos_pass]
1. Deliberate ice strikes on the probe at ~1–2 Hz; record IMU + C
   together → build the strike-blanking classifier (thresholds to
   30_FIRMWARE scope).
2. Soda-water splash for bubble loading; measure occlusion fraction
   and bubble residence time on the electrode (verifies A-001).
3. Probe half-immersed; wet hand on glass; vigorous vs gentle stir.
Pass: mode estimator recovers baseline within 2 s in every abuse
case with ≤40 % sample corruption (R-05); update FEASIBILITY.md.

## Safety block (applies to all runs)
190-proof is flammable: no open flames/hot plates near standards,
ventilate, small volumes, spill plan. Benchtop hardware is NOT
food-safe: every sample is labeled and dumped. Nitrile gloves when
handling coatings/epoxy.

## Data discipline
Every run gets a `40_EXPERIMENTS/TEMPLATE_run_log.md` copy named
`RUN_YYYYMMDD_<n>_<slug>.md`; raw CSVs → `data/` (gitignored if
large) with the run log carrying filenames, conditions, and the
one-paragraph verdict. Numbers promoted to SPECS.md only from run
logs.
