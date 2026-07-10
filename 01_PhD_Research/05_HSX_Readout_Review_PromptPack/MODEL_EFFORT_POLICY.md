# MODEL_EFFORT_POLICY — which model + effort per subtask, and why (my recommendation)

You asked me to spend budget efficiently but keep **Fable 5 on the most critical parts**. Here
is the allocation the orchestrator must apply and LOG. The principle: Fable 5 (high effort) on
anything **irreversible, generative, safety-/vacuum-critical, or that you explicitly care about**;
a cheaper fast model on **bounded verification/lookup**; the cheapest on **housekeeping**.

| Subtask | Model | Effort | Why this tier |
|---|---|---|---|
| ST1 components | **Fable 5** | medium | you explicitly want the "optimal part" call; judgment-heavy |
| ST2 connections | Sonnet | medium | bounded netlist/pinout verification against given maps |
| ST3 3-axis architecture | **Fable 5** | **high** | irreversible board decision; wide trade space |
| ST4 Pi fan-out | Sonnet | low–medium | bounded capacitance/drive calculation |
| ST5 flange | **Fable 5** | **high** | spends money + changes mechanical fit; vacuum-critical |
| ST6 wiring & shorts | **Fable 5** | medium–high | your #1 worry; a short kills a sensor (safety) |
| ST7 packaging wire-bond | **Fable 5** | **high** | in-vessel, hermeticity, bond map correctness |
| ST8 3D packaging design | **Fable 5** | **high** | most generative; in-vessel; envelope-critical; CAD |
| red-team-critic | **Fable 5** | **high** | the check that catches the costly wrong answer |
| synthesis + decision gates | **Fable 5** | **high** | your sign-off artifacts must be right |
| housekeeping (file parse, BOM CSV, logs, image mgmt) | Haiku | low | mechanical, cheap, high-volume |

## How it's enforced (automatic — no manual switching)
- `RUN.ps1` launches the orchestrator on **Fable 5** (`--model claude-fable-5`). Fable-5 subtasks
  therefore run on the launch model by default.
- When the orchestrator spawns a subagent for **ST2 or ST4**, it sets the cheaper model on that
  spawn (Task-tool `model` option, or `/model` around the call), then returns to Fable 5.
- Housekeeping steps (parsing STEP, writing CSV/logs, moving renders) run on **Haiku**.
- Effort is set per phase by the orchestrator before each subtask and restored after.
- **Every** switch is written to `05_STATE/MODEL_EFFORT_LOG.md` (see CLAUDE.md §Logging) so we can
  see cost vs. subtask and produce follow-up patches.

## Fallbacks (keep it one-command robust)
- If your Claude Code build doesn't support per-subagent model/effort, **run everything on Fable 5
  at high effort** — more tokens, same correctness. Log that this fallback was taken.
- If budget runs low mid-run, the orchestrator finishes the Fable-5 critical subtasks first
  (ST3/5/7/8 + red-team + synthesis) and may drop ST2/ST4 to a shorter pass — and logs it.

## You can override
Edit this table before running; the orchestrator reads it at start and obeys it. To force
"maximum accuracy, ignore budget," set every row to Fable 5 / high and note it here.
