# HSX vector probe / RSI 2026 — Claude Code project memory

## What this is
Design, calibration, and second-HSX-campaign deployment of a 2–3 axis
(vector) AlGaN/GaN Hall-effect probe, and the resulting paper for
**Review of Scientific Instruments** (target submission ~Mar 2027).
Hardware concept: gen-2 sensor dies with **larger bond pads**, one die
per ceramic LCC (same carrier and epoxy process as 2023), LCCs mounted
on 2–3 orthogonal faces of a **ceramic cube**; readout is the project-02
spinning-current board replicated per axis.

**Scope rule (hard):** plasma + magnetic-field measurement in HSX only.
No neutron/gamma radiation experiments — radiation is covered by the
co-authored Van Gorp TCAD paper and may only be cited or mentioned as
outlook.

## Read first
1. `NOTES.md` — running log, newest first.
2. `docs/rsi_experiment_and_publication_plan.md` — the source of truth:
   trajectory analysis, instrument design, calibration plan, campaign
   plan, figure list, timeline, risks. Don't re-plan from scratch;
   amend this doc.
3. `../02_HSX_Hall_Sensor_Readout/docs/SPECS.md` — inherited numbers
   (phase table, gains, pin maps). Gen-2 dies require re-measuring
   plate R before trusting the emulator value and loading factor.

## Decisions already made (challenge only with a reason, then log it)
- Readout scales by **replicating the 02 board ×3** from the existing
  gerbers (`../02_.../circuit/hsx_setup_v1_Y23.zip`); hand assembly.
- **One Pico** fans out shared a0/a1/a2/EN to all boards →
  synchronized spinning across axes; per-board floating 100 µA sources.
- DAQ: DSOX1204G, 4 channels = v_x, v_y, v_z + sync (exactly fills it).
- Vector calibration: 3×3 matrix M via indexed 90° cube rotations in
  the single-axis Helmholtz (3D-printed cradle); in-situ absolute
  anchor via HSX coil-only shots vs computed vacuum field.

## Open decisions (tracked in NOTES.md)
- Feedthrough conductor count → DB-15 vs 2×DSUB-9 (ask Wayne/Thomas).
- Scope memory strategy: ~300 ms window @ 1 MSa/s vs full shot at lower
  f / sample rate vs HSX DAQ channels.
- Commit to 2 axes vs 3 (bond yield and pin budget decide).

## Working style
- Instrument-paper mindset: every performance claim needs a calibration
  path and an uncertainty. The `rsi-editor` agent enforces this on text.
- Cross-project consistency: if a number changes here (e.g., re-measured
  plate R), update `../02_.../docs/SPECS.md` too and log it.
- Model/effort defaults and escalation: see `../CLAUDE.md`.
