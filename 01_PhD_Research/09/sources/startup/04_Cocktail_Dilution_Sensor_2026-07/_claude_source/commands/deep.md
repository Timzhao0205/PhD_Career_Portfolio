---
description: Escalate one hard problem to Opus with deep reasoning
argument-hint: describe the stubborn problem
model: opus
---
ultrathink

This is an escalated, correctness-critical request -- the session
default (opusplan/medium) was judged insufficient. Treat it as bench
engineering where a wrong answer costs a lab day:

- Re-derive from first principles AND cross-check against
  `10_SENSING_DESIGN/SPECS.md`, `10_SENSING_DESIGN/ESTIMATOR_SPEC.md`,
  and the verified facts in CLAUDE.md before concluding. If they
  disagree, say so explicitly rather than silently picking one.
- Historical failure points here: temperature-compensation algebra
  (water tempco vs. mixture), mode-estimator bias under asymmetric
  bubble outliers, electrode drift electrochemistry, and thermistor
  lag during rapid chilling -- check those twice.
- End with: your confidence, and the single bench measurement that
  would confirm or refute the conclusion.
- This costs more than a normal turn. Once resolved, remind the user
  that the session continues on the cheaper default.

Problem: $ARGUMENTS
