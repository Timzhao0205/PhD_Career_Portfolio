# DELIVERABLES_SPEC & acceptance checklist

Final tree (the run isn't done until every box is checkable):

```
HSX_Readout_Review_PromptPack/
├── 05_STATE/
│   ├── MASTER_STATE.json        [ ] mission=="COMPLETE"; ST1–ST6 + synthesis "complete"
│   ├── PROGRESS_LOG.md          [ ] one dated line per subtask
│   └── ASSUMPTIONS.md           [ ] every gap-filling assumption logged
├── 10_COMPONENTS/
│   ├── COMPONENT_REVIEW.md      [ ] keep/change per part, datasheet-cited, ambient/≤20 kHz lens
│   └── bom_verdict.csv          [ ] machine-readable keep/change table
├── 20_CONNECTIONS/
│   └── CONNECTION_CHECK.md      [ ] net-by-net pass/flag; J1 Amphenol pinout verified vs sensor map
├── 30_3AXIS_ARCH/
│   └── ARCHITECTURE_TRADE.md    [ ] 3-option weighted matrix + rec + runner-up + flip condition
├── 40_PI_FANOUT/
│   └── PI_FANOUT.md             [ ] quantified 3× load; buffer/no-buffer verdict + threshold
├── 50_FLANGE/
│   └── FLANGE_SELECTION.md      [ ] ≥12-cond option(s) ≥ 9D-275 ratings; every part cited
├── 60_WIRING_SHORTS/
│   └── WIRING_PLAN.md           [ ] pinout table + short-circuit FMEA + pre-power test procedure
├── 70_PACKAGING/
│   └── PACKAGING_REVIEW.md      [ ] LCC02046 verified; die→pad→DSUB map; comment on wire-bond strategy
├── 80_3D_PACKAGING/
│   ├── PACKAGING_3D_DESIGN.md   [ ] 3–4 glue-free concepts + critique of user's idea + matrix + rec
│   └── <concept>/               [ ] per concept: .scad/.py + iso/top/front/section PNG + STEP/STL
└── 90_SYNTHESIS/
    ├── RECOMMENDATIONS.md       [ ] master answer table (6 Qs) + 3-axis build order
    ├── DECISION_GATES.md        [ ] 2–3 sign-off items with the options laid out
    └── RED_TEAM.md              [ ] surviving objections + settling evidence
```

## Acceptance rules
- Every quantitative claim has an inline citation (datasheet or vendor URL) OR is marked
  `UNVERIFIED` / `ENGINEERING JUDGMENT`.
- Every recommendation is keep/change, names the alternative part when "change," and has a
  failure-mode-if-wrong line.
- No conclusion depends on the 2026-07-08 measured amplitudes (open anomaly).
- The locked constraints (ambient readout, ≤20 kHz, sensor-only-in-vessel) are respected —
  no high-T or wideband recommendations about the readout electronics.
- The single-axis Aug-2026 build is not blocked by anything recommended.
- Each deliverable is self-contained enough to read alone.

## Style
Direct, math-forward, units on every number, dates where relevant. Tables over prose. No
filler, no restating the question back at length. Bottom-line-up-front in each file.
