# START HERE — HSX Readout Hardware Review (Fable 5 prompt pack)

Everything is pre-wired. You paste **one message** and Fable 5 (Claude Code) runs a
6-subtask engineering review of your `hsx_2026_v2` readout board and its 3-axis /
in-vessel scale-up, grounded in the data in this folder, and writes every answer to
disk here.

## What you'll get

A verified answer to each of your six questions, each as its own file under a numbered
folder, plus a synthesis with a decision table and a red-team pass:

- `10_COMPONENTS/` — is the component selection optimal for the *ambient, ≤20 kHz, spun*
  use case; keep-or-swap call per part with datasheet-cited reasons.
- `20_CONNECTIONS/` — netlist/pinout correctness check, focused on the updated Amphenol
  DSUB-9 (J1) and the full signal path.
- `30_3AXIS_ARCH/` — one-big-board vs 6-layer vs 3-stacked-boards trade study.
- `40_PI_FANOUT/` — whether the Raspberry Pi Pico clock fan-out to 3 boards needs
  buffering / more drive / more power.
- `50_FLANGE/` — which Accu-Glass CF sub-D feedthrough to move to for 12 conductors,
  matching the 9D-275's ratings.
- `60_WIRING_SHORTS/` — multi-sensor harness & short-circuit mitigation plan.
- `70_PACKAGING/` — comment on your LCC02046 wire-bond / one-side-routing strategy, with the
  die-contact → LCC-pad → DSUB-9-pin mapping.
- `80_3D_PACKAGING/` — 3–4 glue-free probe-head concepts (your slotted cube refined + genuinely
  different options), a critique of your idea, per-concept CAD renders (iso/top/front/section) +
  STEP/STL, and a weighted decision matrix. Envelope Ø1.25 in × 2.75 cm is enforced.
- `90_SYNTHESIS/` — one-page recommendation table + `DECISION_GATES.md` (the 2–3
  choices only you can sign off) + `RED_TEAM.md`.

## One-time setup

1. Install Claude Code and log in with your account (`claude` → browser login → `/exit`).
2. Put the `hsx_2026_v2` KiCad project folder next to this pack (or note its path) so the
   connection check can read the real netlist. If you can't, the pack ships a faithful
   netlist/BOM snapshot in `01_MISSION/HARDWARE_DATA.md` and the review still runs.

## Run it — one command (Windows PowerShell)

From this folder:

```powershell
.\RUN.ps1
```

That's the whole interaction. `RUN.ps1` launches Claude Code on **Fable 5**, seeds it with
`KICKOFF_PROMPT.txt`, and runs ST1–ST8 + synthesis autonomously with **zero prompts** (it uses
`--dangerously-skip-permissions`; `CLAUDE.md` confines all writes to this folder). It also tries
to install OpenSCAD for the ST8 renders. Keep the window open; watch
`05_STATE\PROGRESS_LOG.md` and the numbered output folders fill in.

- Blocked by execution policy? `powershell -ExecutionPolicy Bypass -File .\RUN.ps1`
- Want enforced guardrails instead of zero-prompt? `.\RUN.ps1 -Mode guarded` (press `a` =
  "always allow" a few times early, per `.claude\settings.json`).
- Stopped (rate limit, sleep, closed window)? `.\RUN.ps1 -Resume` — continues from
  `05_STATE\MASTER_STATE.json`.

**Models & budget:** the run puts **Fable 5 on the critical/creative subtasks** (components,
board architecture, flange, wiring, both packaging subtasks, red-team, synthesis) and a cheaper
fast model on the bounded checks (connections, Pi fan-out), housekeeping on Haiku. Full policy +
rationale in `MODEL_EFFORT_POLICY.md` (edit that table to override). Every switch is recorded in
`05_STATE\MODEL_EFFORT_LOG.md`, the narrative in `05_STATE\RUN_LOG.md`.

Manual fallback (no script): open any Fable 5 chat, attach this whole folder, paste
`KICKOFF_PROMPT.txt`.

## Rules of the road (why this pack is built this way)

- **Search-first on every part fact.** No datasheet number, pinout, or vendor spec is
  taken from memory — each is fetched and cited. See `01_MISSION/SOURCE_STANDARDS.md`.
- **Your constraints are locked in** so the review doesn't drift into problems you don't
  have: the feedthrough flange is the boundary — the **zirconia 3D package + LCC02046 carriers +
  sensors are inside the vessel**, the **readout board is outside at ~ambient**, and 10–20 kHz
  post-spin bandwidth is fine.
- **One open bench item gates the electrical conclusions:** the unresolved ΔV gain check
  (see `CONTEXT_PRIMER.md`). The pack tells Fable 5 not to rest component decisions on
  measured amplitudes until you close it.
- **Files are ground truth.** State is written after every subtask so you can stop and
  resume (`.\` re-run + "resume from MASTER_STATE.json").

## If it stops

Re-run the kickoff and say "resume." It reads `05_STATE/MASTER_STATE.json` and continues
from the first subtask not marked `complete`.
