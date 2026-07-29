# Cocktail Dilution Sensor — Claude Code project memory

## What this is
Product development of a real-time dilution / ABV sensor for stirred
cocktails ("smart barspoon" family). Sensing core: fine-pitch
interdigitated capacitive electrodes (permittivity → ABV) + NTC
thermistor (temperature compensation + thermodynamic dilution model)
+ IMU gating, fused by a mode-of-histogram burst estimator. Owner:
Yiming "Tim" Zhao. Personal-time project — see hard rules. This is a
PRODUCT-DEV folder (build/measure/iterate), not an autonomous research
mission: interactive sessions, human in the loop.

## Read first, in order
1. `NOTES.md` — running log, newest first. Read at session start;
   append via `/log` only.
2. `10_SENSING_DESIGN/SPECS.md` — one-page quick reference: physics
   constants, target specs, part numbers, calibration targets.
   **Check it before re-deriving any number.** `/specs <q>` is cheap.
3. `01_PRODUCT/REQUIREMENTS.md` — quantified product requirements.
4. `40_EXPERIMENTS/PLAN_P0_dipstick.md` — active experiment plan.
5. `05_STATE/DECISIONS.md` — decisions already made; don't relitigate
   silently.

## Folder map
- `01_PRODUCT/` — brief, requirements, feasibility, risk register.
- `05_STATE/` — MASTER_STATE.json, PROGRESS_LOG.md, ASSUMPTIONS.md,
  DECISIONS.md. Update after any milestone.
- `10_SENSING_DESIGN/` — sensing architecture, SPECS quick reference,
  estimator spec.
- `20_HARDWARE/` — BOM (csv + notes), `electrodes/` (IDE coupon PCB),
  `readout/` (FDC2214 chain).
- `30_FIRMWARE/` — XIAO nRF52840 Sense firmware (Phase 1+).
- `40_EXPERIMENTS/` — protocols, run-log template, `data/` (raw CSVs;
  gitignored above 1 MB — summarize into run logs).
- `50_ANALYSIS/` — Python: calibration surface fit, mode estimator.
- `90_REFERENCES/` — sources ledger.
- `98_CLAUDE_METRICS/` — Claude Code activity logs + analyzer
  (see "Activity recording" below).

## Key physics & targets (verified this project — don't re-derive)
- εr(water, 25 °C) ≈ 78.4; εr(EtOH, 25 °C) ≈ 24.3. Water tempco
  ≈ −0.37 %/°C — temperature compensation is mandatory.
- Whisky-on-ice trajectory: ~40–45 % ABV at pour → ~20–28 % ABV at
  full melt-in; liquid goes 20–25 °C → about −5 °C. Calibrate 0–60 %
  ABV, −8 to +30 °C.
- Fringing-field sensing depth ≈ electrode pitch. Coupons at 150 /
  200 / 300 µm pitch, ENIG, guard ring; parylene-C passivation (SNF).
- FDC2214: 4 ch, 28-bit, I²C; sensor-to-chip run < 10 cm.
- Ground truth: gravimetric standards (0.01 g balance) + strain-and-
  weigh surviving ice (mass balance → exact dilution).
- Sugar breaks single-modality sensing (3 unknowns): whisky+ice only
  for v1. Full-cocktail = second modality = out of scope until P0/P1
  pass.

## Hard rules
1. Stay inside this folder; web via WebSearch/WebFetch for parts,
   pricing, datasheets — never for settled SPECS facts.
2. Never invent or "correct" a measured value. SPECS.md and run logs
   in `40_EXPERIMENTS/` are bench truth; disagreement gets flagged in
   NOTES.md, not papered over.
3. PERSONAL-TIME WALL: no Stanford/SNF resources may be assumed in
   product plans except where explicitly marked (parylene coating is
   flagged as a dependency to remove before commercialization). No
   Senesky-group IP. Keep this separable from PhD work.
4. NO FOOD-SAFETY CLAIMS. Benchtop hardware is not food-safe; every
   protocol involving real spirits ends with "label and dump." Product
   packaging materials (316L, FDA-compliant coatings) are a Phase-2
   design input, not something to assert prematurely.
5. Ethanol + electronics: calibration standards from 190-proof are
   flammable; protocols must keep heat sources away and note ventilation.
6. Budget band: Phase 0 ≤ $400; Phase 1 ≤ $1.5K cumulative. Flag
   anything above as STRETCH.
7. Windows host: forward-slash relative paths, UTF-8, no characters
   illegal on Windows filenames.
8. Style: terse, quantitative, engineer-voice; every file readable
   standalone.

## Session workflow
- Launch `claude` from THIS folder so `.claude/` (commands, agents,
  hooks) is picked up.
- `/log <note>` → NOTES.md. `/specs <q>` → cheap SPECS lookup.
  `/deep <problem>` → Opus escalation for correctness-critical physics
  (estimator math, calibration algebra, electrochemistry drift).
  `/metrics [args]` → summarize Claude Code activity logs.
- Agents: `sensing-physicist` (reviews estimator/physics derivations),
  `test-protocol-designer` (turns questions into bench protocols),
  `sourcing-scout` (part availability/pricing, web).
- After any milestone: update 05_STATE (MASTER_STATE.json + one line
  in PROGRESS_LOG.md), and record irreversible choices in DECISIONS.md.

## Model & effort — tuned for cost; adjust freely
Defaults (`.claude/settings.json`): `model: opusplan`,
`effortLevel: medium`. Personal overrides → gitignored
`.claude/settings.local.json`. Escalation ladder, cheapest first:
- Trivial lookups → `/specs` (Haiku, SPECS.md only, no web).
- Routine edits, BOM updates, plotting, protocol drafting → defaults.
- Correctness-critical or stuck (mode-estimator statistics, ε(T,ABV)
  fit residuals, drift root-cause, thermistor lag compensation) →
  `/deep`, or `/model opus` + `/effort high` for a stretch, then step
  back down.
- Web only for volatile facts (stock, pricing, errata) — never for
  repo-settled numbers.

## Activity recording (performance analysis) — ACTIVE
Hooks in `.claude/settings.json` append one JSON line per event to
`98_CLAUDE_METRICS/logs/activity_YYYY-MM.jsonl`: session start/end
(with source, configured model + effort, transcript path), every tool
call (name, duration_ms, effort, outcome), turn boundaries, and
subagent completions. Prompt *content* is never logged — only lengths.
The logger is fail-safe (always exits 0, prints nothing). Analyze with
`/metrics` or `python 98_CLAUDE_METRICS/analyze_activity.py`
(`--transcripts` adds best-effort per-model token usage parsed from
Claude Code's own session transcripts). If hooks misbehave, `/hooks`
shows what's wired; deleting the hooks block in settings.json disables
recording without touching anything else.
