# HSX Hall-effect sensor readout — Claude Code project memory

## What this is
Bring-up, verification, and calibration of an AlGaN/GaN Hall-effect
sensor readout board (current-spinning + AD8429 in-amp) for installation
in the HSX stellarator (UW-Madison), target August 2026. Owner: Yiming
"Tim" Zhao, Stanford EE PhD. This system supersedes the voltage-bias,
uncalibrated readout of the 2023 IEEE Sensors Letters deployment.
Trajectory, budget rules, and slash commands live one level up in
`../CLAUDE.md` — this file carries the technical memory.

## Read first, in order
1. `NOTES.md` — running log, newest first. Read at the start of every
   session; append a dated entry only when asked (or via `/log`).
2. `docs/SPECS.md` — one-page quick reference: phase table, pin maps,
   gains, expected numbers, cal targets. **Check it before re-deriving
   any number.** `/specs <question>` queries it cheaply.
3. `docs/hsx_readout_bringup_and_calibration_plan.md` — the week-by-week
   plan (procedures, testbench design, risk register). Source of truth
   for the project plan.
4. `../01_Publications/tim_ieee_sensors_letters_GaN_Hall_sensor_in_HSX_2023.pdf`
   — the 2023 paper this project supersedes.

## Folder map
- `docs/` — plan + SPECS quick reference.
- `firmware/pico2/` — Pico 2 (RP2350) MicroPython/PIO clock source:
  `pico2_hsx_phase_clock.py` (module), `main.py` (boots into menu, safe),
  `README.md` (full wiring table with Pico physical pins, flashing,
  usage, scope handshake).
- `analysis/hsx_demod_scope_csv.py` — host-side demod for a 2-channel
  scope capture (v_meas + sync only; a0/a1/a2 never go to the scope).
- `circuit/` — LTspice netlist, KiCad netlist, rendered schematics,
  gerber/order package (`hsx_setup_v1_Y23.zip`).

## Key facts (verified against both netlists — don't re-derive)
- 100 µA current bias (S_I ≈ 60 V/A/T), not the 2023 paper's 0.4 V.
- 8-phase table: `state = (a2<<2)|(a1<<1)|a0`; demod sign
  **+1 if a0 == a2 else −1** (a1 irrelevant). Full table in SPECS.
- AD8429, G ≈ 100.3 (R_G ≈ 60.4 Ω, reads 59.8 in-circuit).
- J3: 1=a2, 2=a1, 3=a0, 4=en — **no ground pin**.
- As-built R9 = R10 = 100 Ω (current-sense, DMM-confirmed).
- Emulator: 4×649 Ω ring + 33 kΩ **in parallel** across pins 1–6 →
  ±26 mV steps. Never in series (rails the amp).

## Known gotchas (verify before power — plan §2 has detail)
- EN is pulled down on the PCB — drive ≥ 2 V or the board is dead.
- Bond logic ground to GND1 separately (no ground pin on J3).
- Bias source is external (J2/J7); the sim's ideal source doesn't exist.
- RS6-2415D DC/DC makes the ±15 V rails — expect switching spurs.
- Demod BW ≈ 1–2 kHz at f = 40 kHz — record raw v_meas for fast events.

## Working with this repo
- Bench/lab engineering, not production software: favor correctness and
  clear derivations, but don't gold-plate one-shot scripts.
- Anything touching the phase table, sign convention, or
  offset-cancellation algebra: cross-check against SPECS and the plan
  before changing — a sign error here is silent and costs a bench day.
  That's `/deep` territory if it resists.
- Datasheet facts (AD8429, ADG1209, ADG5236, RS6-2415D) are already in
  the plan and code comments — don't re-fetch unless the bench disagrees.
- Model/effort defaults and escalation rules: see `../CLAUDE.md`.
