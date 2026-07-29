# Decision log — append-only; reversals get a new entry

- D-001 (2026-07-07) SENSING PRIMARY = capacitive IDE + NTC + IMU.
  Rejected for v1: ultrasonic (non-monotonic vs ABV), RI (sugar
  confound moot for v1 but optics cost), tuning-fork density
  (fouling/miniaturization). RI is the designated backup modality.
- D-002 (2026-07-07) ESTIMATOR = burst sampling + mode-of-histogram +
  IMU strike blanking + thermodynamic melt model as fusion/sanity
  channel. Mean/median rejected (one-sided outlier bias).
- D-003 (2026-07-07) SCOPE v1 = spirits+ice binary only. Sugared
  cocktails require a second modality; parked until P0/P1 gates pass.
- D-004 (2026-07-07) BUILD ORDER = dipstick -> clip-on probe -> spoon.
  Through-glass puck is stretch (glass vessels only; pitch/parasitics
  penalty).
- D-005 (2026-07-07) GROUND TRUTH = gravimetric standards + strain-
  and-weigh ice mass balance. Hydrometer/refractometer are checks,
  not truth.
- D-006 (2026-07-07) CLAUDE CODE TELEMETRY ON: hooks log session/
  model/effort/tool/duration to 98_CLAUDE_METRICS; prompt content
  never stored.
