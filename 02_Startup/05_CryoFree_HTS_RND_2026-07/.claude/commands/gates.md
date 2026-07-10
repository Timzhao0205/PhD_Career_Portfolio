---
description: Run the three Fable-5 critical gates (G-PHYS, G-NOVEL, G-CLAIM) on one candidate.
---
For candidate $ARGUMENTS, invoke the fable-adjudicator subagent to run, in order,
G-PHYS then G-NOVEL then G-CLAIM per 10_MISSION/MISSION.md. Require the prior-art
ledger (60_PRIOR_ART/$ARGUMENTS) and the simulation outputs to exist first; if
missing, say so and stop. Write the verdicts to 60_PRIOR_ART/$ARGUMENTS/gates.md.
Log intended `models=GATE:fable-5` and append the down-route-unverifiability note
to PROGRESS_LOG.md. End with the verdict line: NOVEL / NARROW-NOVEL / DUPLICATED /
KILLED, and the one-sentence surviving claim core if any.
