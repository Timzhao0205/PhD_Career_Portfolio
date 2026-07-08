# Research notes — HSX Hall sensor readout

Append new entries at the top (newest first). One dated section per entry.
Claude Code reads this file every session (see CLAUDE.md) so it always has
the current status without you re-explaining it.

---

## 2026-07-08 — first dynamic spinning run on the emulator (20 kHz, 20 mA)
Full session write-up: `journal/2026-07-08_spinning_emulator_20mA.md`.
- Config: 20 mA bias, 20 kHz spin, emulator = 4×680 Ω ring + 2.2 kΩ across
  p1–p2; R_G = 60.4 Ω (SMD "76X", confirmed) → gain 100.3; DSO-X 4022A,
  v_meas only (no sync). Data: `data/2026-07-08_test_spin.csv`.
- ✓ Clean 8-state staircase at 400 µs (muxes stepping correctly); raw
  pattern + − − + − + + −. **R9 = R10 = 2.0 V → leakage check PASSED**
  (20 mA reaches the bridge).
- ✓ **Offset cancellation works**: demod collapses the 686 mV raw offset
  to ≤ 5 mV (≥130×, limited by the scope's 8-bit quantization over 5
  cycles), reconstructing phase from f since sync wasn't captured.
- ◑ **OPEN ANOMALY**: with 680 Ω + 2.2 kΩ + 20 mA + gain 100.3 the output
  should rail (~75 V); measured a clean 0.686 V — ~109× too small. R9=R10
  rules out leakage; R_G present rules out a missing gain resistor. Left:
  in-operation gain not ~100×, OR the 2.2 kΩ not electrically unbalancing
  the bridge. **Resolve with the ΔV gain check (plan §4 Day 3–4) next
  session — top priority.** Don't calibrate to these magnitudes yet.
- New reusable tool: `analysis/spin_verify_nosync.py` (fold/demod/bridge-
  consistency when only v_meas was captured).
- Plan status (This Week §4/§6.1): done — logic bring-up, emulator+current
  source, R9/R10 leakage check, dynamic spin+demod cancellation. Not done —
  ΔV gain check, static 8-state survey, sync capture, noise floor PSD,
  f-sweep, rail-ripple spectrum. Full table in the journal.

## 2026-07-08 — MODE 1 low-frequency extension (delay cycles)
- Extended the spin firmware's phase-rate range downward. Each phase is
  now emitted as `CYCLES_PER_PHASE = 8` PIO cycles (a `[7]` delay on the
  `set`), so the SM runs at 8·f. This decouples the phase rate from the
  PIO clock-divider floor: a single-cycle phase can't go below ~2.3 kHz
  at the Pico 2's 150 MHz sys clock (max divider 65536), but 8
  cycles/phase drops the floor to **~290 Hz** — so f = 1 kHz now works.
  Verified 1k/5k/40k/100k land on clean divisors; <290 Hz is rejected
  with a clear message. `set_freq` reports the achieved *phase* rate.
- Applied to both `main.py` and `pico2_spin_scope.py` (kept consistent).
- Note: **5 kHz and above need no reflash** — they were always above the
  floor; use `freq 5000` / `start 5000` on the existing firmware. The
  reflash only matters for sub-2.3 kHz rates. Recommended demod range
  (SPECS: 10k–100k for usable BW) is unchanged; the low end is for
  bench visualization. Remember to pass the matching `--f` to
  `hsx_demod_scope_csv.py`.

## 2026-07-08 — firmware split into two modes; second test setup defined
- Firmware reorganized into two self-contained mode files (same J3 pin
  map, same verified phase table): `firmware/pico2/pico2_spin_scope.py`
  (mode 1 — full current-spinning, scope as DAQ, adds `survey()` and
  `scope_notes()`) and `firmware/pico2/pico2_static_bias_p2p4.py`
  (mode 2 — muxes parked in states 2/3/6/7: external source biases
  p2 → p4, amp reads the p1/p3 difference, Pico ADC on GP26 ← J4
  digitizes; 4-state chop cancels amplifier offset, plate offset o does
  NOT cancel — single-axis physics). `pico2_hsx_phase_clock.py` kept as
  heritage, unchanged.
- `main.py` consolidated into a **self-contained single-file build**
  carrying both modes: set `MODE = 1` or `2` (and `DEFAULT_FREQ`) at the
  top, flash only that one file. Lights the onboard LED (alive
  indicator), then runs the selected mode's menu; live object exposed as
  `dev` for the REPL. Added a `predict`/`predict_offset` bridge-offset
  helper to mode 2 (o = I·(R41·R23 − R12·R34)/ΣR → expected v_meas) for
  the emulator plug. The two module files remain as importable libraries
  (RSI 3-board work) mirroring the same logic. Smoke-tested both modes'
  boot paths with the Pico hardware stubbed.
- New doc `docs/second_test_setup_static_bias.md` — the second test
  setup: purpose (health checks, gen-2 raw-offset incoming inspection,
  2023-style continuity, fast-mode fallback), wiring incl. ADC tap and
  optional level-shift network, expected numbers, ADC limits (unipolar,
  ~0.8 mV/LSB — health-check grade only).
- Bring-up plan revised (Jul 8): Day-2/Day-3 firmware references, new
  §6.3, fast-mode item §2.8, Week-3 drift note, risk register.
- Reader-friendly HTML mirrors generated next to the plan docs
  (`.html` beside `.md`); regenerate whenever the markdown changes.
- No changes to any measured value, the phase table, or the demod sign
  convention.

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
