# Assumptions ledger
Log every assumption made without verification; retire with evidence.

- A-001 (2026-07-07): Bubble-induced capacitance outliers are one-sided
  (eps -> 1) and short-lived (<100 ms residence on electrode under
  stirring shear). VERIFY in P0-E3.
- A-002: Whisky congeners shift calibration by <0.5 % ABV vs pure
  ethanol-water (99.9 % binary). VERIFY across 3 whiskies in P0-E2.
- A-003: Glass-bead NTC thermal tau < 1 s in stirred liquid, adequate
  for 20 degC/min transients with lag modeling. VERIFY in P0-E1.
- A-004: FDC2214 effective resolution suffices for 0.5 % ABV steps at
  150-300 um pitch coupons with <10 cm leads. VERIFY in P0-E0.
- A-005: `python` resolves on the Windows host PATH (hooks depend on
  it). If not, change hook commands to the py launcher (`py -3 ...`).
