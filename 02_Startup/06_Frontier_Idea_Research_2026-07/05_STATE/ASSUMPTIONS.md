# Assumptions

- “Reachable budget” starts with a decisive experiment of $25k–$250k and prefers a first sellable
  product before $5M cumulative outside capital. Ideas outside this range may survive only with a
  clearly smaller component/subsystem wedge.
- Major Asian markets include China, Japan, South Korea, Taiwan, India, and Singapore; relevance
  varies by lane and must be evidence-based.
- The target company-formation horizon is approximately 2029–2030, consistent with prior work,
  but existing demand is preferred over forecasts.

Agents append dated assumptions below. Never edit away earlier entries.

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


