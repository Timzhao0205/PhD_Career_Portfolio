# Autonomous mission brief

Read in order: `CLAUDE.md`, `FOUNDER_PROFILE_SHALLOW.md`, `SOURCE_STANDARDS.md`, `LANE_MAP.md`,
`SCORING_RUBRIC.md`, `MODEL_EFFORT_POLICY.md`, `DELIVERABLES_SPEC.md`, the two JSON templates,
then state. `CLAUDE_CODE_REFERENCE.md` is operator documentation and not research evidence.

## P0 — initialize

Verify folder structure and model-probe records. Log assumptions. The orchestrator must write a
one-page anti-anchoring plan explaining how lane independence and the 5% founder-fit cap will be
enforced. Mark P0 only after files exist.

## P1 — collect a broad source atlas

Dispatch 16 `lane-scout` agents in four waves of four. A scout collects 45–55 candidates, fetches
the best pages, and writes `10_SOURCE_ATLAS/Lxx_<slug>.md` plus `Lxx_raw_sources.json`. Require a
mix of technical feasibility, customer pain/procurement, incumbent products, standards/policy,
and US/Asian evidence. Scouts do not generate final startup ideas.

After each wave, dispatch `source-verifier` agents over its records. They verify peer review,
canonical identity, fetch support, and acceptance/rejection. Merge into the canonical ledger and
checkpoint with `python tools/merge_sources.py`. Continue collecting replacements until the accepted count and mix gates pass. A raw
count does not advance P2.

## P2 — source quality gate and atlas synthesis

Run `tools/validate_sources.py`. Sonnet verifier fixes mechanical failures. Then Fable reads all
lane briefs and a stratified sample of at least 80 accepted records, adjudicates whether the atlas
contains real demand rather than technology enthusiasm, and writes `10_SOURCE_ATLAS/ATLAS.md`.
If any lane is thin or demand-poor, send targeted scouts before proceeding.

## P3 — evidence-first opportunity generation

Dispatch `idea-architect` (Fable/xhigh) in independent batches: process, infrastructure,
scientific, transport/space, and wildcards. Produce at least 64 rough seeds. The orchestrator
deduplicates and selects at least 48 distinct longlist ideas across at least 14 lanes. Only now
append the shallow founder-fit note. Write markdown and JSON.

## P4 — reality checks and scoring

For each longlist idea, dispatch `demand-competitor-analyst` in waves of four to find named buyers,
procurement/filing evidence, closest global and Asian incumbents, pricing, regulation, and market
arithmetic. Then Fable performs physics and build-path review, applies hard gates, scores with the
rubric, and records uncertainty. Any idea without G1 demand is eliminated, not “promising.”

## P5 — adversarial selection

Red-team the highest 32 with `red-team-critic` in waves of four. Each tries to disprove demand,
10x edge, competitor whitespace, reachable budget, and geography. Fable adjudicates score changes
and selects a diversity-compliant final 24 plus top 10 deep dives. Preserve rejected near-misses
and reasons.

## P6 — deep dives and geography

Run 10 `deep-dive-analyst` agents in waves of at most four. Each report is 2,500–4,000 words and
uses >=20 unique accepted sources, including >=7 peer-reviewed technical and >=5 primary demand/
competitor/geography sources. In parallel, a geography analyst writes the cross-portfolio US,
China, Japan, South Korea, Taiwan, India, and Singapore entry/constraint map using current primary
sources. This is commercial/technical research, not legal advice.

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

## P8 — audit, repair, finish

Run both validator scripts and `source-auditor` (Sonnet/high). Fable/xhigh reads the audit, checks
20 randomly selected accepted sources and 10 load-bearing claims across different ideas, reviews
portfolio diversity, and writes `99_AUDIT/FABLE_ADJUDICATION.md`. Fix every failure and rerun.
Only after both scripts pass and Fable says PASS may the orchestrator write
`99_AUDIT/FINAL_AUDIT.md` with `PASS` and set state to COMPLETE.
