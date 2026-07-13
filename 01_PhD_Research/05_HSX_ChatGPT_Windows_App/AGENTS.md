# Autonomous ChatGPT Windows project contract

This folder is a self-contained engineering workspace for ChatGPT Work in the Windows desktop
app. Read this file, `MISSION.md`, `EXECUTION_PLAN.md`, `CHECKPOINT_PROTOCOL.md`, and
`state/PROJECT_STATE.md` before doing any substantive work.

## Operating mode

- Work autonomously until the stopping condition in `EXECUTION_PLAN.md` is met.
- The user has authorized reading and writing inside this folder and running safe local commands
  needed for analysis, CAD inspection, rendering, validation, and checkpointing.
- Do not wait for routine confirmations. Ask only when a missing decision would materially change
  the design or an action would affect anything outside this folder.
- Use live web research for current/vendor/process claims. Prefer primary sources, standards,
  manufacturer data, and peer-reviewed papers. Record direct URLs and exact claim support.
- Never edit `previous_results/`; it is historical evidence. Put all new work in `outputs/`,
  `state/`, or `logs/`.
- Do not create or use Claude configuration, PowerShell runners, CLI launchers, project
  `config.toml`, or hidden automation configuration.

## Checkpoint requirements

- Follow `CHECKPOINT_PROTOCOL.md` exactly.
- Before starting a stage, update `state/PROJECT_STATE.md` to `IN_PROGRESS`.
- Save a durable checkpoint at every stage boundary and after any costly research, CAD generation,
  or major design decision. Do not keep the only copy of useful work in chat context.
- Update `state/WORKLOG.md`, `state/DECISION_LOG.md`, `state/MODEL_EFFORT_LOG.md`, and
  `state/CHECKPOINT_INDEX.md` continuously.
- On any restart, read state and validate existing marker files. Resume from the earliest
  incomplete or invalid stage; never redo a valid completed stage merely because chat context was
  lost.
- If Git is installed, maintain local-only baseline/stage commits. If Git is unavailable, continue
  using file checkpoints without asking the user to install it.

## Model and effort policy

- The recommended parent task is GPT-5.6 Sol with extra-high reasoning.
- Never silently change to a weaker model for a critical decision.
- If the app exposes autonomous per-agent model selection, use Luna/low only for inventory and
  deterministic extraction, Terra/medium for source organization, Sol/high for board architecture,
  and Sol/xhigh for wire-bonding, package design, red-team, and synthesis.
- If per-agent selection is not available, keep the parent Sol/xhigh task for all stages. Record
  actual model/effort and any unavailable control in `state/MODEL_EFFORT_LOG.md`.
- A critical stage must not proceed on a model below Sol unless the user explicitly approves it.

## Binding engineering constraints

- In-vessel sensor, LCC, conductor, joint, insulation, retention, and ceramic parts operate
  continuously in UHV at 250 deg C. Ambient readout electronics remain outside vacuum.
- There are three mutually orthogonal, electrically isolated, four-terminal Hall sensors: twelve
  sensor conductors through the feedthrough.
- The installed three-axis head must fit a 31.75 mm-diameter by 27.5 mm-high envelope, including
  clamps, fasteners, contacts, and harness exits.
- Each bonded sensor plus LCC02046 must be independently removable, reusable, and protected during
  service. No adhesive in the reusable head baseline.
- Prioritize, in order after hard safety/physics gates: fabrication cost, reuse of sensor plus LCC,
  and electrical/mechanical connection quality.
- The recommended ceramic baseline has zero tapped or internal zirconia threads. Prefer smooth
  through-holes, external accessible nonmagnetic fasteners, replaceable nuts/nut plates, identical
  flat ceramic parts, open tool access, and no crossing/hidden bolts.
- Avoid unqualified PEEK, BeCu relaxation assumptions, magnetic nickel/steel near the sensors,
  virtual leaks, trapped volumes, blind nut traps, solder with inadequate continuous-temperature
  margin, and load paths through electrical joints.
- The user's LCC proposal is inner pads 8, 3, 19, 14 with external routes 8->4, 3->9, 19->13,
  18->14. Resolve the pad-14/pad-18 inconsistency and chamfer/orientation before fixing a map.
- Never guess p1-p4 die orientation. Use an orientation-parametric map plus microscope sign-off if
  authoritative orientation evidence is absent.

## Evidence and deliverable quality

- Separate verified fact, calculation, engineering proposal, and unresolved gate.
- Do not treat bake survival or a catalog maximum as continuous-life qualification.
- Unsupported numerical limits must be labeled `ENGINEERING PROPOSAL - VALIDATE`.
- Unresolved fabrication or purchase details must be labeled `HOLD - DO NOT FABRICATE/ORDER`.
- Drawings must agree with tables on pad numbers, chamfer, axes, dimensions, feedthrough pins, and
  units. Use SVG for precise schematics; use a real CAD kernel for STEP/STL inspection when
  available.
- Complete a separate red-team stage before final synthesis.

## Stopping condition

Stop only when every stage marker in `EXECUTION_PLAN.md` exists and passes its acceptance check,
the final artifact set is internally consistent, state says `COMPLETE` or
`COMPLETE_WITH_OPEN_GATES`, and a final checkpoint has been saved.

