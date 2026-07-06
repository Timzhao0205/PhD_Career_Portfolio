# HSX Hall-effect sensor readout — Claude Code project memory

## What this is
Bring-up, verification, and calibration of an AlGaN/GaN Hall-effect sensor
readout board (current-spinning + AD8429 in-amp) for installation in the
HSX stellarator (UW-Madison), target August 2026. Owner: Yiming "Tim" Zhao,
Stanford EE PhD. This folder supersedes the voltage-bias, uncalibrated
readout from the 2023 IEEE Sensors Letters deployment.

## Read first
- `NOTES.md` — running log, newest entry first. Read it at the start of
  every session; it carries the current status and any open questions.
  Append a dated entry when asked to "log" or "note down" progress —
  don't add entries unprompted.
- `docs/hsx_readout_bringup_and_calibration_plan.md` — the full week-by-week
  bring-up and calibration plan (test procedures, testbench design, risk
  register). Treat it as the source of truth for the project plan; don't
  re-derive it from scratch.
- `../01_Publications/tim_ieee_sensors_letters_GaN_Hall_sensor_in_HSX.pdf` —
  the 2023 paper this project supersedes.

## Folder map
- `docs/` — the bring-up and calibration plan.
- `firmware/pico2_hsx_phase_clock.py` — Raspberry Pi Pico 2 (RP2350)
  MicroPython/PIO firmware: generates the a0/a1/a2 spinning clocks + sync
  pulse (one PIO instruction per phase, atomic updates) + EN control.
- `analysis/hsx_demod_scope_csv.py` — host-side CLI: demodulates a
  2-channel oscilloscope capture (v_meas + sync only — a0/a1/a2 never go
  to the scope) using the known phase rate f.
- `circuit/` — LTspice netlist (`hall_sensor_measurement_system_v1.net`),
  KiCad netlist (`hsx_2026_v1.net`), rendered schematics (`kicad_01.pdf`,
  `ltspice_1.pdf`), gerber/JLCPCB order package (`hsx_setup_v1_Y23.zip`).

## Key facts (verified against both netlists — don't re-derive)
- Bias: 100 µA current-scaled (S_I ≈ 60 V/A/T), not the 2023 paper's 0.4 V
  voltage bias.
- 8-phase spinning table: `state = (a2<<2)|(a1<<1)|a0`; demod sign =
  `+1 if a0==a2 else -1` (a1 irrelevant). Full table in the plan doc §1.
- Gain: AD8429, G ≈ 100.3 (RG ≈ 60.4 Ω).
- J3 header pinout: 1=a2, 2=a1, 3=a0, 4=en — **no ground pin**.
- As-built R9 = R10 = 100 Ω (current-sense resistors, DMM-confirmed).
- Emulator plug: 4×649 Ω ring (p1–p2–p3–p4) + 33 kΩ **in parallel** across
  one arm → ≈26 mV output steps. Never in series (unbalances the bridge
  ~50× and slams the amp into the rail).

## Known gotchas (fix/verify before power — plan doc §2 has full detail)
- EN is pulled down on the PCB (sim had it tied high) — must be driven
  ≥2 V or the board is dead on power-up.
- Logic ground must be bonded to GND1 separately (no ground pin on J3).
- Bias current source is external (J2/J7) — the sim's ideal 100 µA source
  doesn't exist on the physical board.
- RS6-2415D isolated DC/DC generates ±15 V — expect switching spurs, no
  clean bench-supply header for the rails.
- Demod bandwidth ≈ 1–2 kHz at f = 40 kHz — record raw v_meas and demod
  offline if faster transients matter.

## Working with this repo
- This is bench/lab engineering work, not production software — favor
  correctness and clear derivations over speed, but don't gold-plate: a
  script that runs once on one CSV doesn't need a test suite.
- Cross-check anything touching the phase table, sign convention, or
  offset-cancellation algebra against the facts above and the plan doc
  before changing it — a sign error here is silent and costs a bench day,
  not a failed unit test.
- Datasheet facts (AD8429, ADG1209, ADG5236, RS6-2415D) are already
  reflected in the plan doc and code comments — don't re-fetch them from
  the web unless a real discrepancy shows up on the bench.

## Model & effort — adjust freely, this is tuned for cost, not fixed
Default (`.claude/settings.json`): `model: opusplan` (Opus reasons through
planning, Sonnet executes) at `effortLevel: medium` — a reasonable
quality/cost balance for this kind of work. If `effortLevel` doesn't seem
to take effect at startup (an occasionally-reported settings.json quirk),
just run `/effort medium` once — it persists across sessions from then on.
A personal `.claude/settings.local.json` (gitignored) can override either
value without touching this shared file.
- Routine edits (tweak a script, adjust a plot, wire a new pin): the
  defaults are enough — don't ask to escalate for these.
- Something genuinely hard (a demod residual that won't null, a sign
  convention that doesn't match the bench, an EMI root-cause hunt): say
  so, suggest `/model opus` and/or `/effort high` for that turn, then step
  back down once it's resolved.
- Skip web search for settled facts already in this repo (pin maps, gain,
  phase table). Do search for anything that could have changed since
  training (RP2350/MicroPython firmware quirks, current component stock
  or pricing, HSX schedule changes).
