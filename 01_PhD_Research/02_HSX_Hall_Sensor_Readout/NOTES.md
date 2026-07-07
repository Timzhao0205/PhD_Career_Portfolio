# Research notes — HSX Hall sensor readout

Append new entries at the top (newest first). One dated section per entry.
Claude Code reads this file every session (see CLAUDE.md) so it always has
the current status without you re-explaining it.

---

## 2026-07-06 — folder restructure
- Project now lives inside the reorganized `01_PhD_Research/` tree with a
  root-level CLAUDE.md, shared `.claude/` automation (`/log`, `/specs`,
  `/deep`, `rsi-editor` agent), and budget defaults (opusplan + medium).
- Firmware moved to `firmware/pico2/` — module unchanged, plus new
  `main.py` (boots into the interactive menu) and `README.md` with the
  full Pico-pin ↔ J3 ↔ test-point wiring table.
- Added `docs/SPECS.md`: one-page quick reference (phase table, pin maps,
  gains, expected numbers, cal targets). Check it before re-deriving.
- New sibling project `03_HSX_Vector_Probe_RSI2026/` created for the 2–3
  axis cube probe, second HSX campaign, and the RSI paper plan.
- No functional changes to firmware or analysis code; only the firmware
  path reference in the bring-up plan doc was updated.

## 2026-07-06
- Verified `circuit/hsx_2026_v1.net` (KiCad) against
  `circuit/hall_sensor_measurement_system_v1.net` (LTspice) pin-by-pin:
  bias mux, sense mux, chopper cross-wiring, AD8429 pinout, bias-return
  resistors, and output network all match. Three integration items open,
  not design errors: EN pulldown, no J3 ground pin, external current
  source needed.
- Built `firmware/pico2_hsx_phase_clock.py` — PIO-based a0/a1/a2 + sync
  generator with atomic single-edge updates, plus EN sequencing and a
  static-hold mode for the manual 8-state survey.
- Built `analysis/hsx_demod_scope_csv.py` — demodulates a 2-channel scope
  capture (v_meas + sync only) by reconstructing the phase index from the
  sync pulse and the known phase rate f. Validated against a synthetic
  waveform before use.
- Confirmed as-built R9 = R10 = 100 Ω (current-sense resistors).
- Next: Week-1 Day 1 cold checks + DMM value audit, then current-limited
  first power. Full plan in `docs/hsx_readout_bringup_and_calibration_plan.md`.
