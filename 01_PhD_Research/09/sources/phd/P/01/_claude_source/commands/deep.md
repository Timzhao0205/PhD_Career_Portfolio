---
description: Escalate one hard problem to Opus with deep reasoning
argument-hint: describe the stubborn problem
model: opus
---
ultrathink

This is an escalated, correctness-critical request — the session default
(opusplan/medium) was judged insufficient for it. Treat it as bench
engineering where a wrong answer costs a lab day:

- Re-derive from first principles AND cross-check against
  `02_HSX_Hall_Sensor_Readout/docs/SPECS.md` and the verified facts in
  the project CLAUDE.md before concluding. If they disagree, say so
  explicitly rather than silently picking one.
- Sign conventions, the 8-state phase table, and offset-cancellation
  algebra are the historical failure points here — check those twice.
- End with: your confidence, and the single bench measurement that
  would confirm or refute the conclusion.
- This costs more than a normal turn. Once resolved, remind the user
  that the session continues on the cheaper default.

Problem: $ARGUMENTS
