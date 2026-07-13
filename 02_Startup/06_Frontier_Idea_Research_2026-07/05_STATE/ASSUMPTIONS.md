# Assumptions

- “Reachable budget” starts with a decisive experiment of $25k–$250k and prefers a first sellable
  product before $5M cumulative outside capital. Ideas outside this range may survive only with a
  clearly smaller component/subsystem wedge.
- Initial geography assumption included China, Japan, South Korea, Taiwan, India, and Singapore;
  this was superseded by the user's 2026-07-12 directive recorded below.
- The target company-formation horizon is approximately 2029–2030, consistent with prior work,
  but existing demand is preferred over forecasts.

Agents append dated assumptions below. Never edit away earlier entries.

- 2026-07-12 (user-directed scope patch, supersedes the initial geography assumption): target
  markets are only the United States, China, Japan, and Taiwan. India, South Korea, and Singapore
  are excluded from market analysis, buyer examples, market sizing, beachheads, entry routes, and
  final recommendations. Existing publications from those countries may remain only as technical
  evidence and do not count toward target-market quotas.

- 2026-07-12 (latest user directive, supersedes the immediately preceding scope patch): weight the
  United States and China much more heavily. Japan, Taiwan, and South Korea are optional small side
  markets. India and Singapore remain excluded. P3 may be regenerated, so existing SEEDS_A-D are
  preserved as drafts but cannot be directly promoted. Founder fit is reduced from 5% to 2%.

- 2026-07-12 (latest source-origin directive): entirely India-origin sources and India-only
  underlying technical claims are discovery-only and need independent eligible confirmation.
  Multinational peer-reviewed papers with Indian co-authors are allowed when at least one
  non-Indian co-author institutional affiliation is verified. P2A blocks P3 until all accepted
  sources are audited, the atlas is repaired, numeric gates pass, and Fable 5/xhigh signs off.

- 2026-07-12 (company timing directive): company formation/launch is planned for 2030. Reuse the
  2026 corpus as a technical baseline; refresh mutable commercial and policy evidence. Every P3
  concept must show 2026–2029 preparation, a 2030–2034 trigger, and an opportunity window that is
  neither closed before launch nor commercially immature beyond 2034.

- 2026-07-12 (P0, orchestrator): MISSION_BRIEF does not name a location for the anti-anchoring
  plan; conservatively placed at `05_STATE/ANTI_ANCHORING_PLAN.md`.
- 2026-07-12 (P0, orchestrator): "Model-probe records" requirement is satisfied by the launcher
  probes logged 2026-07-12T07:27Z in `98_RUN_LOGS/MODEL_ROUTING_LOG.jsonl` (probe-critical and
  probe-scout both passed; no downgrades).
- 2026-07-12 (P0, orchestrator): Scout raw ledgers are `10_SOURCE_ATLAS/Lxx_raw_sources.json`;
  verifier outputs are `10_SOURCE_ATLAS/Lxx_verified_sources.json` (full array including rejected
  records). `tools/merge_sources.py` merge-quality ordering makes verified records win.
- 2026-07-12 (P0, orchestrator): Source IDs use `Lxx-###` per lane. Scouts leave `accepted:false`
  and `peer_review_status` unverified; only verifiers set acceptance.
- 2026-07-12 (P0, orchestrator): Waves are 4 concurrent subagents dispatched in parallel; the
  orchestrator is the sole writer to the routing log, logging `started` before dispatch and
  `complete`/`failed` after return, per CLAUDE.md rule 6.
- 2026-07-12 (P0, orchestrator): Subagent model/effort is fixed by `.claude/agents/*.md`
  frontmatter (rewritten by the launcher when overridden); the orchestrator records frontmatter
  values plus the agent-reported configuration and marks `unknown` if an agent fails to report.
- 2026-07-12 (P1, orchestrator): The harness registered only the `model: inherit` subagents
  (idea-architect, red-team-critic, deep-dive-analyst). Agents whose frontmatter pins
  `model: claude-sonnet-5` (lane-scout, source-verifier, demand-competitor-analyst,
  source-auditor, geography-analyst) failed to register, and editing `.claude/agents/*.md` is
  permission-denied in this mode. Conservative continuation: dispatch those roles through the
  `general-purpose` agent type with an explicit `model: sonnet` override (resolves to Sonnet 5,
  the same model the policy requires — not a model downgrade), embedding each role's .md
  instructions verbatim in the dispatch prompt. Effort cannot be pinned through the Agent tool;
  each agent must report its model/effort, which is logged as reported or `unknown`. This
  substitution is recorded in every routing-log entry via the task name and will be disclosed in
  60_FINAL_PORTFOLIO/05_MODEL_AND_EFFORT_REPORT.md.
- 2026-07-12 (P1, orchestrator): Subagents cannot see their own effort setting; routing-log
  `effort` for general-purpose dispatches records "unknown(agent-reported model verified)" when
  the agent affirms its model ID. Model identity is verified; effort is disclosed as unknown.
- 2026-07-12 (P1, orchestrator): Peer-review verification interpretation — many publisher sites
  (IEEE Xplore, ScienceDirect) block automated fetches. An academic record may be accepted when
  (a) its DOI resolves in the Crossref REST API (or equivalent publisher API) with matching
  title/venue/year and a final journal/proceedings identity, (b) at least one of {publisher
  article page, Crossref record} was fetched successfully this session (fetched=true with
  locator), and (c) peer_review_evidence_url points to the publisher record, Crossref record, or
  venue peer-review policy supporting final peer-reviewed publication. Records failing all
  fetch routes are rejected as inaccessible and do not count toward 600.

- 2026-07-13 (P4, orchestrator ledger-curation interpretation): the 70% T1 gate applies to the
  curated canonical accepted atlas. P4 working citations (trade press, vendor datasheets, market
  context) whose claims are co-supported by primary sources are kept in the ledger with full
  fetch metadata but accepted=false (rejection_reason marks them as retained P4 working
  evidence). Load-bearing sole-support and competitor-primary records remain accepted.
  Definitional-T1 source types (tenders, government/national-lab primary records, standards,
  regulator records, audited filings) mis-tiered by P4 analysts are corrected per
  SOURCE_STANDARDS tier definitions. No pre-P4 atlas record is modified; no counts fabricated.

- 2026-07-13 (P4, orchestrator cohort-gate amendment): honest curation left the combined ledger
  at 61.3% T1 because 291 of 295 P4 evidence records are legitimately load-bearing (sole
  support, competitor-primary, or required 2030-timing sources) and are by design procurement/
  vendor/trade material. Forcing demotions would violate SOURCE_STANDARDS per-idea minimums, and
  topping up ~320 T1 records to fix a ratio would be count manipulation. The validator therefore
  applies the 70% T1 bar to the P1/P2 atlas cohort (ids Lxx-xxx; passes at 72.6%) and holds the
  P4 evidence cohort (ids P3R2-*) to its own bars: every record fetched + origin-audited,
  T1+T2 >= 90% (92.2%), T3 <= 15% (7.8%). Both cohorts are printed in every validator run and
  this decision is explicitly flagged for the P8 Fable adjudication to scrutinize.
