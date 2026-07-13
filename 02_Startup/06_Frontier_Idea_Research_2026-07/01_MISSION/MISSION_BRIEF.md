# Autonomous mission brief

Read in order: `CLAUDE.md`, `FOUNDER_PROFILE_SHALLOW.md`, `SOURCE_STANDARDS.md`, `LANE_MAP.md`,
`SCORING_RUBRIC.md`, `MODEL_EFFORT_POLICY.md`, `DELIVERABLES_SPEC.md`, the two JSON templates,
then state. `CLAUDE_CODE_REFERENCE.md` is operator documentation and not research evidence.

## P0 — initialize

Verify folder structure and model-probe records. Log assumptions. The orchestrator must write a
one-page anti-anchoring plan explaining how lane independence and the 2% founder-fit cap will be
enforced. Mark P0 only after files exist.

## P1 — collect a broad source atlas

Dispatch 16 `lane-scout` agents in four waves of four. A scout collects 45–55 candidates, fetches
the best pages, and writes `10_SOURCE_ATLAS/Lxx_<slug>.md` plus `Lxx_raw_sources.json`. Require a
mix of technical feasibility, customer pain/procurement, incumbent products, standards/policy,
and especially US/China evidence. Japan, Taiwan, and South Korea are secondary coverage; India
and Singapore are excluded market evidence. Scouts do not generate final startup ideas.

After each wave, dispatch `source-verifier` agents over its records. They verify peer review,
canonical identity, fetch support, and acceptance/rejection. Merge into the canonical ledger and
checkpoint with `python tools/merge_sources.py`. Continue collecting replacements until the accepted count and mix gates pass. A raw
count does not advance P2.

## P2 — source quality gate and atlas synthesis

Run `tools/validate_sources.py`. Sonnet verifier fixes mechanical failures. Then Fable reads all
lane briefs and a stratified sample of at least 80 accepted records, adjudicates whether the atlas
contains real demand rather than technology enthusiasm, and writes `10_SOURCE_ATLAS/ATLAS.md`.
If any lane is thin or demand-poor, send targeted scouts before proceeding.

## P2A — mandatory India source-origin audit and atlas repair

P3 is blocked. Inspect all 1,118 canonical records and fully adjudicate every accepted record,
starting with `05_STATE/INDIA_SOURCE_ORIGIN_PREFILTER.json` and the 12 non-overlapping batches in
`05_STATE/INDIA_SOURCE_ORIGIN_AUDIT_QUEUE.json`. Dispatch
`india-origin-auditor` (Sonnet 5/high) in independent batches. For academic papers, enumerate
author affiliations from the final publisher page/PDF and structured identity metadata; accept a
mixed Indian/non-Indian paper only when at least one non-Indian co-author affiliation is verified.
For all other source types, verify where the source organization, outlet, lab, company, publisher,
or government body is located. Do not infer from names.

Quarantine every India-origin or unresolved source as `discovery_only`. If it supplied a useful
lead, locate and fetch an independent eligible confirmation before retaining the claim. Synchronize
the canonical and lane ledgers, write `05_STATE/INDIA_SOURCE_ORIGIN_AUDIT.{md,json}`, remove all
unsupported/excluded IDs and derivative claims from lane briefs and `ATLAS.md`, then rerun source
validation. If any reviewed, accepted, peer-reviewed, demand, tier, geography, language, category,
or per-lane gate fails, run additional non-India replacement searches and verification until every
gate passes.

Finally, Fable 5/xhigh reviews a stratified sample of at least 80 accepted audit records, every
multinational exception, and at least 20 exclusions; it writes
`99_AUDIT/P2A_FABLE_ORIGIN_ADJUDICATION.md`. P3 can begin only after the validator passes and this
adjudication says PASS.

## P3 — evidence-first opportunity generation

Treat the existing `SEEDS_A` through `SEEDS_D` files as preserved prior drafts, not candidates for
direct promotion. Regenerate P3 as round 2 from the accepted source atlas using five independent
`idea-architect` dispatches, all Fable 5/xhigh:

1. US industrial, infrastructure, and scientific pain (>=18 seeds).
2. China industrial, infrastructure, and scientific pain, using Chinese primary evidence (>=18).
3. US–China dual-market products with independent demand logic in each country (>=18).
4. Frontier energy/physics wildcards optimized for coolness, elegance, and controllability (>=16).
5. Optional Japan/Taiwan/South Korea side-market or cross-lane concepts (>=10, no forced quota).

Produce at least 80 new `P3R2_*` seeds. Then dispatch `idea-elegance-judge` independently on the
new seeds. It must critique non-obviousness, elegance, controllability, frontier vision, hidden
commodity risk, and whether the US/China logic is truly independent. The judge cannot read the
founder profile. After fixes, the orchestrator deduplicates and freezes at least 48 longlist ideas
across at least 14 lanes. Longlist gates: >=36 credible US cases, >=36 credible China cases, >=24
credible in both, and <=8 primarily dependent on Japan/Taiwan/South Korea. Only then append the
shallow founder-fit note. Write markdown and JSON.

Every seed must be designed for a 2030 company launch and include: current/estimated TRL; the
2026–2029 preparation path that does not assume a fully operating company; a decisive experiment
date and budget; a named 2030–2034 customer/procurement/regulatory/capacity trigger; expected
competition by 2030; why the window will not close before launch; and the kill condition if
commercial readiness slips beyond 2034. Current demand is evidence of pain, not an assumption that
today's market structure persists unchanged.

## P4 — reality checks and scoring

For each longlist idea, dispatch `demand-competitor-analyst` in waves of four to find named buyers,
procurement/filing evidence, closest global and in-scope Asian incumbents, pricing, regulation, and market
arithmetic. Then Fable performs physics and build-path review, applies hard gates, scores with the
rubric, and records uncertainty. Any idea without G1 demand is eliminated, not “promising.”
Refresh time-sensitive 2026 baseline claims and obtain at least two independent 2030 timing
sources per surviving idea, including one primary/official 2028–2035 trigger. Apply G7.

## P5 — adversarial selection

Red-team the highest 32 with `red-team-critic` in waves of four. Each tries to disprove demand,
10x edge, competitor whitespace, reachable budget, and geography. Fable adjudicates score changes
and selects a diversity-compliant final 24 plus top 10 deep dives. Preserve rejected near-misses
and reasons.
Red-team the 2030 timing thesis explicitly: premature window, commoditization, delayed readiness,
incumbent convergence, policy sunset, procurement slippage, and pre-company execution realism.

## P6 — deep dives and geography

Run 10 `deep-dive-analyst` agents in waves of at most four. Each report is 2,500–4,000 words and
uses >=20 unique accepted sources, including >=7 peer-reviewed technical and >=5 primary demand/
competitor/geography sources. In parallel, a geography analyst writes a cross-portfolio map that
gives the United States and China full primary-market treatment. Japan, Taiwan, and South Korea
receive shorter optional side-market sections only where relevant. India and Singapore must not
appear as buyers, beachheads, market-size inputs, entry routes, or recommendations. Publications
may remain as technical evidence only when they pass the P2A source-origin rule. This is commercial/technical research, not
legal advice.
Each deep dive separates durable technical evidence from refresh-sensitive evidence and maps
2026–2029 preparation, 2030 launch, and 2030–2034 customer adoption milestones.

## P7 — Fable synthesis

Using Fable/xhigh, write:

- `60_FINAL_PORTFOLIO/00_EXECUTIVE_PORTFOLIO.md`: ranked 24 with why each is cool and credible.
- `01_IDEA_CARDS.md`: all fixed card fields from the deliverables spec.
- `02_COMPARISON_MATRIX.csv` and `.md`: exact criteria, scores, confidence, lane, buyer, budget.
- `03_FRONTIER_MAP.md`: clusters, big visions, and non-obvious cross-lane connections.
- `04_VALIDATION_ROADMAP_2026_2030.md`: cheapest experiments, customer discovery, decision gates.
- `05_MODEL_AND_EFFORT_REPORT.md`: intended vs actual routes, all downgrades/failures/retries,
  approximate calls/effort, and recommendations for a patch run.

State clearly which ideas are evidence-rich versus speculative. Do not force a winner when
uncertainty overlaps.
The roadmap must extend through 2034 even though its legacy filename ends in 2030: show
pre-company preparation through 2029, launch decisions in 2030, and post-launch validation/sales
milestones for 2030–2034.

## P8 — audit, repair, finish

Run both validator scripts and `source-auditor` (Sonnet/high). Fable/xhigh reads the audit, checks
20 randomly selected accepted sources and 10 load-bearing claims across different ideas, reviews
portfolio diversity, and writes `99_AUDIT/FABLE_ADJUDICATION.md`. Fix every failure and rerun.
Only after both scripts pass and Fable says PASS may the orchestrator write
`99_AUDIT/FINAL_AUDIT.md` with `PASS` and set state to COMPLETE.
