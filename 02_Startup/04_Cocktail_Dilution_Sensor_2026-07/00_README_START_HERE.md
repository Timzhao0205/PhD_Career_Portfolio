# 04 — Cocktail Dilution Sensor (product development, started 2026-07)

Real-time dilution / ABV instrument for stirred drinks: capacitive
permittivity sensing + thermistor + IMU, robust burst estimator.
Consumer/prosumer bar-tool concept ("smart barspoon" family). This is
a personal-time product-dev project, deliberately separable from PhD
work (see CLAUDE.md hard rule 3).

## Build order
- Phase 0 — benchtop dipstick (FDC2214EVM + IDE coupons + NTC): derisk
  drift + chaos rejection. Plan: 40_EXPERIMENTS/PLAN_P0_dipstick.md
- Phase 1 — clip-on inner-wall probe (XIAO nRF52840 Sense, sealed)
- Phase 2 — instrumented barspoon (flex PCB on shaft, potted handle)
- Stretch — through-glass coaster puck (glass vessels only)

## Working here with Claude Code
Launch `claude` from THIS folder. Read CLAUDE.md first — it is
binding. Session shorthand: `/log`, `/specs`, `/deep`, `/metrics`.
Activity-recording hooks are ON (98_CLAUDE_METRICS/).

## Folder map
01_PRODUCT (brief/requirements/feasibility/risk) · 05_STATE (state,
progress, assumptions, decisions) · 10_SENSING_DESIGN (strategy,
SPECS, estimator) · 20_HARDWARE (BOM, electrodes, readout) ·
30_FIRMWARE · 40_EXPERIMENTS (protocols + data) · 50_ANALYSIS
(python) · 60_RND_STRATEGY (R&D plan + 5.6 sol prompt pack) ·
90_REFERENCES · 98_CLAUDE_METRICS (Claude Code activity logs +
analyzer).
