---
description: Execute one pipeline wave to its checkpoint, updating RUN_STATE and PROGRESS_LOG.
---
Read CLAUDE.md and 10_MISSION/MISSION.md. Execute Wave $ARGUMENTS end-to-end to its
checkpoint, using the model/effort routing in CLAUDE.md (delegate to the named
subagent per stage). At the checkpoint: run `python tools/check_runlog.py`, update
80_STATE/RUN_STATE.json (phase pointer, wave counter, models map, budget used/left,
gate results), append one line to 80_STATE/PROGRESS_LOG.md in the form
`W$ARGUMENTS | models=role:model[xN] | effort=… | ts=… | notes=…`, record any
autonomous decisions in 80_STATE/ASSUMPTIONS.md (A##), then STOP and print a
2-line summary + budget spent. Do not roll into the next wave without a new command.
Honor every hard rule; if a candidate trips the prong-(a) gate, stub it BLOCKED-
PENDING-COUNSEL and continue with the rest.
