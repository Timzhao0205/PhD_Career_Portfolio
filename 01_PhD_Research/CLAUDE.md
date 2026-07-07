# 01_PhD_Research — Claude Code root memory

Owner: Yiming "Tim" Zhao, Stanford EE PhD (Senesky group). Research
arc: GaN Hall-effect magnetic sensing for fusion diagnostics in the HSX
stellarator (UW-Madison collaboration: Wayne Goodman, Thomas
Gallenberger, Benedikt Geiger).

## Trajectory (use this to frame any planning or writing)
1. **2023 — IEEE Sensors Letters (1st author, published):** AlGaN/GaN
   Hall sensor deployed in-vessel in HSX; 68 shots; voltage-biased,
   uncalibrated (V_off unknown); demonstrated real-time plasma tracking
   via temporal correlation with the diamagnetic loop. Its stated future
   work: absolute calibration, offset stability, lower-noise readout.
2. **2026 — project 02 (active):** current-spinning calibrated readout,
   single axis; HSX install target August 2026. Directly closes the
   calibration + offset items from (1).
3. **2026–27 — project 03 (planning):** 2–3 axis vector probe (ceramic
   cube of LCCs, gen-2 dies with larger pads), second HSX campaign,
   paper targeted at **Review of Scientific Instruments** (~Mar 2027).
4. **Co-authored (in preparation):** Van Gorp, Dawes, Zhao, Senesky —
   TCAD radiation sensitivity modeling
   (`01_Publications/in_preparation/`). Simulation only.

**Scope rule:** Tim's experimental work is plasma + magnetic-field
measurement in HSX only. **No neutron/gamma radiation experiments are
planned.** Radiation belongs to the co-authored TCAD paper; in Tim's
first-author work it may be cited as complementary or mentioned as
outlook, never claimed experimentally.

## Folder map
- `01_Publications/` — published PDFs; `in_preparation/` for drafts.
- `02_HSX_Hall_Sensor_Readout/` — single-axis readout. Technical memory
  in its own `CLAUDE.md`; quick numbers in `docs/SPECS.md`.
- `03_HSX_Vector_Probe_RSI2026/` — vector probe + RSI paper. Plan in
  `docs/rsi_experiment_and_publication_plan.md`.

## Session workflow
- Launch `claude` from THIS folder so `.claude/commands` and
  `.claude/agents` are picked up; both subprojects are reachable.
- Start by reading the active project's `NOTES.md` (newest-first log).
- Log progress with `/log <note>`; look up numbers with
  `/specs <question>`; escalate stubborn problems with `/deep <problem>`;
  manuscript review goes to the `rsi-editor` agent.
- Never invent or "correct" a measured value; SPECS and NOTES record
  the bench truth. If something disagrees, flag it, don't paper over it.

## Model & effort — tuned for cost; adjust freely
Defaults (`.claude/settings.json`): `model: opusplan` (Opus thinks
through plan mode, Sonnet executes) at `effortLevel: medium`. If the
effort setting doesn't take at startup (a known occasional quirk), run
`/effort medium` once — it persists thereafter. Personal overrides go in
a gitignored `.claude/settings.local.json`.

Escalation ladder, cheapest first:
- Trivial lookups → `/specs` (runs on Haiku; reads SPECS.md, no web).
- Routine edits, plots, wiring notes → session defaults; don't ask to
  escalate for these.
- Correctness-critical or stuck (sign conventions, demod residuals,
  offset algebra, EMI hunts) → `/deep` (runs that one turn on Opus with
  deep reasoning), or suggest `/model opus` + `/effort high` for a
  stretch, then step back down once resolved.
- Web search only for things that can change (component stock/pricing,
  MicroPython/RP2350 quirks, HSX schedule) — never for settled repo
  facts like pin maps, gains, or the phase table.
