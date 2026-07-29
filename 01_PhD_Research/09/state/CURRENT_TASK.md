# Current stage task

## SHUTDOWN STATUS (2026-07-29) — Fable 5 usage-credit exhaustion

The attempt-1 worker described below was terminated mid-run by the harness:
`"You're out of usage credits. Run /usage-credits to keep using Fable 5 or
/model to switch models."` Its last reported action was "Now IP_COLLAB.md."
`outputs/B50_execution/attempt-1/` holds 2 of 6 required files (ROADMAP.md,
IP_COLLAB.md — the latter possibly mid-write); no RUN_META.md/SELF_CHECK.md;
no verification directory exists. This is a provider usage-credit event, NOT
a model downgrade and NOT a quality failure. Full detail in
`state/SHUTDOWN_CHECKPOINT.md` and `state/ERROR_LOG.md`.

**Do not resume or repair attempt-1 in place.** Per the package's
attempt-numbering policy (a non-accepted target with existing files gets a
fresh next-attempt subdirectory), the restart target is
`outputs/B50_execution/attempt-2/` with a FRESH `pap06-fable-xhigh` worker
(requested Fable 5/xhigh), once Fable 5 usage is available again. The task
below is the ORIGINAL attempt-1 card, preserved for exact re-use as the
attempt-2 instructions (update attempt number references to `2` /
`attempt-2` when delegating).

---

- Stage: `B50_execution`
- Mode: `FULL`
- Attempt: `1` (superseded — next attempt is `2`)
- Target: `outputs/B50_execution/attempt-1/` (superseded — next target is
  `outputs/B50_execution/attempt-2/`)
- Named worker: `pap06-fable-xhigh`
- Requested model: `Fable 5`
- Requested effort: `xhigh`
- Stage specification: `workflow/stages/B50_execution.md`
- Required files: `ROADMAP.md`, `IP_COLLAB.md`, `MANUAL_WORK.md`,
  `SOURCES.csv` plus `RUN_META.md` and `SELF_CHECK.md`
- Allowed immutable inputs: accepted `outputs/B40_portfolio/attempt-1/` plus
  supporting accepted stages (B10, B15, B20, B25, B30) and current official
  sources (web); root policies
- Accepted prerequisite outputs: B40 and supporting stages; accepted pilot
  `pilot/B50_execution/attempt-1/` (its 90-day slice becomes the roadmap's
  first quarter — carry forward, extend to 2034)
- Repair notes: none (this is a fresh-attempt restart after an interruption,
  not a defect repair).

Full-run rules: the complete 2026-2034 roadmap translating B40's portfolio
(5 bridge / 12 watch / 7 stop dispositions; wedges W1/W2). Separate lanes:
research milestones, evidence gates, skill development, customer discovery,
prototype/qualification work, IP screening, regulation/certification,
funding, and launch choices. Use B15 gaps/boundary conditions to define
experiments — never convert literature suggestions into demonstrated
readiness. Include BRANCH POINTS: what changes if Opt2 fails, if a power
bridge fails, if a selected startup direction fails (tie to B30 gates and
B40 falsifiers). IP_COLLAB.md: full IP/FTO question set, collaboration map,
data/publication boundaries, questions for qualified professionals
(screening, not legal advice). MANUAL_WORK.md: all precise human actions
through the roadmap horizon with preparation, evidence, owners, and why not
automatable — no AI impersonation of approvals. SOURCES.csv: current
primary sources for standards/regulatory claims (reuse accepted opens with
notation; new opens only where load-bearing). Dates honest; third-party
dates are targets with owners. PhD-first conflict rule explicit. NO pilot
labels.

Read the stage specification and global policies. Work only in the target.
