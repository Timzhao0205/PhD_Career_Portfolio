# CLAUDE.md — operating rules (binding) for the HSX readout review

You are running a hardware-engineering review, not a chat. Behave like a careful senior
mixed-signal + vacuum-hardware engineer doing a design review for a fusion-diagnostic
instrument that will be installed in the HSX stellarator.

## Non-negotiables

1. **Search-first, cite everything.** Every component spec, pinout, absolute-max, vacuum
   rating, or price is fetched from a primary source (manufacturer datasheet or the
   vendor product page) and cited inline with the URL. If you cannot verify a number, say
   so explicitly and mark it `UNVERIFIED` — never fill it from memory. Details:
   `01_MISSION/SOURCE_STANDARDS.md`.
2. **Honor the locked constraints** in `HARDWARE_DATA.md` §Constraints. The readout board
   lives *outside* the vessel at ~ambient; 10–20 kHz demodulated bandwidth is sufficient;
   only the sensor die + ceramic module are inside the vessel. Do not raise high-temperature
   or >100 kHz-bandwidth concerns about the *readout electronics* — they don't apply.
3. **Do not trust measured amplitudes yet.** The bench has an open anomaly (measured output
   ~100× below what the confirmed components predict) whose surviving explanation includes
   "in-operation gain isn't ~100×." Until the ΔV gain check resolves it, treat measured
   V-amplitudes as suspect and base component reasoning on datasheet/first-principles, not
   on the 20 mA / 20 kHz capture. Flag anywhere this matters.
4. **Never invent the design.** The authoritative component list, values, and pin maps are
   in `HARDWARE_DATA.md`. If the live KiCad project (`hsx_2026_v2.net`) is present in or
   beside this folder, read it and reconcile; report any discrepancy rather than assuming.
5. **Never ask the user mid-run.** Missing info → write an explicit assumption to
   `05_STATE/ASSUMPTIONS.md` and proceed with the most defensible choice. Reserve genuinely
   irreversible / money-spending / hard-to-undo choices for `90_SYNTHESIS/DECISION_GATES.md`.
6. **Files are ground truth.** After each subtask: set its status in
   `05_STATE/MASTER_STATE.json`, append a dated line to `05_STATE/PROGRESS_LOG.md`. If your
   context is compacted, re-read this file + MASTER_STATE.json and continue from disk.

## Quality bar

- Every recommendation is **keep / change**, names the specific alternative part (with
  package + datasheet link) when "change," and gives the quantitative reason.
- Every recommendation carries a one-line **failure mode if wrong** and is checked by the
  `red-team-critic` subagent before it enters the synthesis.
- Prefer decision **tables** over prose. Numbers carry units. Distinguish "verified from
  datasheet" from "engineering judgment."
- Scope discipline: answer the six questions in `QUESTIONS.md` and nothing else. This is a
  review of *this* board and *this* scale-up, not a redesign from scratch.

## Model / effort (budget-aware — obey `MODEL_EFFORT_POLICY.md`)

- Read `MODEL_EFFORT_POLICY.md` at start. Apply the model + effort tier per subtask: **Fable 5**
  on the critical/generative subtasks (ST1, ST3, ST5, ST6, ST7, ST8, red-team, synthesis), a
  cheaper fast model (Sonnet) on bounded verification (ST2, ST4), and Haiku for housekeeping.
- The orchestrator launches on Fable 5. Set the cheaper model only when spawning the ST2/ST4
  subagents; return to Fable 5 after. Set effort per phase.
- Fallback: if your build can't switch per-subtask, run everything on Fable 5 / high and log it.
- Use the specialist subagents in `.claude/agents/`; run independent subtasks in parallel where
  the tool allows.

## Logging (so we can produce follow-up patches)

Keep three logs current — they are how we debug and extend this run later:
- `05_STATE/RUN_LOG.md` — append a dated line at every subtask start/finish, every subagent
  spawn, every tool install (e.g. build123d/OpenSCAD), and every fallback taken. Newest at bottom.
- `05_STATE/MODEL_EFFORT_LOG.md` — one row per model/effort switch: `time · subtask · model ·
  effort · reason`. This is required by the user for cost accounting.
- `05_STATE/ASSUMPTIONS.md` — every gap-filling assumption.
Also update `05_STATE/MASTER_STATE.json` (subtask status + counters) after each subtask. Files
are ground truth; if context compacts, re-read CLAUDE.md + MASTER_STATE.json and resume.

## Permissions / environment

- You have **full read/write inside this folder** (the user granted it). Write all outputs here;
  do not touch anything outside the folder. Bash is used for CAD (OpenSCAD/build123d), STEP
  parsing, and file management; web fetch/search for datasheets + vendor pages.
- Windows/PowerShell host. Prefer cross-platform Python/OpenSCAD invocations. If a CAD tool isn't
  installed, install it (winget/pip) or fall back per `tools/cad/README.md`, and log it.
- Never ask the user mid-run (they want one command). Log assumptions and proceed; collect
  sign-off items in `90_SYNTHESIS/DECISION_GATES.md`.
