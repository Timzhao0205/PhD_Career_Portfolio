---
description: FULLY AUTONOMOUS run. Execute the entire pipeline (W0->W5) end to end without stopping for review, honoring budget and all hard rules. One command; Claude Code finishes the rest.
---
You are running the complete Cryogen-Free HTS discovery pipeline AUTONOMOUSLY.
Do NOT stop between waves for user review. Run W0 through W5 to completion, then halt.

Setup:
1. Read CLAUDE.md and 10_MISSION/MISSION.md fully. Obey every hard rule.
2. Read 80_STATE/RUN_STATE.json. If `budget_tokens.ceiling` is 0, set it to
   2000000 (default autonomous ceiling) and record A## in ASSUMPTIONS.md. If the
   user passed a number as $ARGUMENTS, use that as the ceiling instead.
3. Determine the resume point from RUN_STATE.phase/wave. If a prior run was
   interrupted, CONTINUE from the last incomplete wave, do not restart.

Execute in order, using the model routing in CLAUDE.md (delegate to the named
subagent per stage; log intended `models=role:model` every stage):
  W0 scaffold verify -> W1 prior-art harvest (all 7 CF candidates, multilingual
  US/CN/JP/KR/EU) -> W2 simulation (build on the CF-1 thermal starter; fix the
  known tau<->Rc coupling bug as part of G-PHYS) -> W3 the three Fable-5 gates
  per candidate in order (G-PHYS, G-NOVEL, G-CLAIM) -> W4 disclosure drafting for
  every NOVEL/NARROW-NOVEL survivor -> W5 synthesis + RUN_REPORT.

Autonomy rules (decide and proceed; never block on the user):
- After each wave: run `python tools/check_runlog.py`, update RUN_STATE.json,
  append a PROGRESS_LOG line, record assumptions as A##. Then continue to the
  next wave automatically.
- Budget governor: before each wave, estimate remaining budget from the metrics
  logs. If >90% of ceiling consumed, finish the current wave, write a RESUME_HERE
  note in RUN_STATE.notes, and STOP cleanly (a later `/autorun` resumes). Otherwise
  keep going.
- Candidate pruning: kill any candidate scoring <2 on cryogen_free_relevance or
  prong_a_safety; stub funded-lane-adjacent candidates BLOCKED-PENDING-COUNSEL and
  continue with the rest. Never halt the whole run for one bad candidate.
- Fable gates: log intended `models=GATE:fable-5` and the down-route-unverifiability
  caveat every time (see CLAUDE.md). Proceed on the served result; flag in
  RUN_REPORT which gates should be transcript-verified before filing reliance.
- If a web search / fetch fails, retry once with a reformulated query, then record
  the gap in the ledger and move on. Do not stall.
- Never violate a hard rule to make progress. If a rule blocks an action, log why
  and route around it.

Completion:
- At W5, write 10_MISSION/RND_STRATEGY_CryoFree.md (ranked survivors, flagship,
  budget-phased sim+prototype plan, kill gates) and
  98_CLAUDE_METRICS/RUN_REPORT.md (models-per-stage, budget spent, Fable-gate
  outcomes + which to transcript-verify, recommended reruns).
- Print a final 6-line summary: waves completed, candidates surviving, flagship,
  budget spent, gates needing transcript verification, single recommended next
  human action. Then STOP.
