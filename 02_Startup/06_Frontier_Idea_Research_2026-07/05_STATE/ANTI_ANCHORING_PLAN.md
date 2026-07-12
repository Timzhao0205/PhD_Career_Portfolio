# Anti-anchoring plan — P0 (orchestrator, Fable 5/xhigh)

Written 2026-07-12. Purpose: guarantee that lane selection, source collection, idea generation,
scoring, and final selection are driven by external evidence, not by the founder's prior work in
HTS magnets, magnetic sensing, GaN power, or fusion diagnostics.

## Threat model

1. Lane anchoring: search lanes quietly biased toward the founder's thesis vocabulary.
2. Seed anchoring: idea architects reaching for familiar physics instead of evidenced pain.
3. Score anchoring: "founder fit" leaking into demand, competition, or edge scores.
4. Selection anchoring: near-ties resolved toward familiar domains.
5. Vocabulary anchoring: scoring "coolness" higher for concepts that sound like prior work.

## Enforcement mechanisms

1. **Fixed lane map before evidence.** The 16 lanes in `01_MISSION/LANE_MAP.md` were frozen
   before any collection. Scout prompts describe the founder only as "technically fluent hardware
   founder" — no CV, no thesis topic, no technology names from prior rounds. The orchestrator
   will not add, remove, or reweight lanes based on founder familiarity.
2. **Scouts collect, never pitch.** P1 agents are forbidden from generating startup ideas, so no
   familiarity-driven concept can enter through the evidence layer.
3. **Founder profile quarantined until seeds freeze.** `idea-architect` agents read atlas lanes
   and accepted sources first, write and freeze seed records, and only then append a one-sentence
   generic EE/CE transfer note. The orchestrator checks architect outputs for premature founder
   references and regenerates any batch that violates this.
4. **Hard 5/100 cap.** Founder skill transfer is scored last, capped at 5 points, and can never
   offset a failed hard gate (G1–G6). Selection at P5 will be checked for stability with founder
   fit set to zero: if zeroing fit changes which ideas enter the final 24, the affected ranks are
   re-adjudicated on the other 95 points and the check is recorded in `99_AUDIT`.
5. **Structural diversity gates.** Final 24: >=12 lanes, <=3 ideas/lane, <=4 superconductivity/
   HTS ideas total, <=6 diagnostic/test-only products. These caps bind regardless of scores, so a
   familiarity cluster cannot dominate even if it scores well.
6. **Red-team anchoring probe.** Each red-team review must answer: "Would this idea survive if
   the founder had a different PhD?" — i.e., does the evidence stand without founder-adjacent
   enthusiasm. KILL/HOLD verdicts on anchoring grounds are adjudicated on evidence only.
7. **Routing transparency.** Every dispatch is logged to `98_RUN_LOGS/MODEL_ROUTING_LOG.jsonl`
   with requested/actual model and effort; the P8 audit re-checks that no scout brief cites the
   founder profile and that founder-fit notes appear only in post-freeze fields.

## Independence rule restated

Cross-lane links may be reported, but no lane is discarded or de-prioritized because another lane
is more familiar. All 16 lane maps must exist before the architect combines anything.
