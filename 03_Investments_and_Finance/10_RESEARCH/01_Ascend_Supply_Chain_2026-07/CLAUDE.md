# CLAUDE.md — project-level rules (in addition to ../../CLAUDE.md, which governs)

1. Read, in order, before any work: ../../CLAUDE.md -> 01_MISSION/MISSION_BRIEF.md ->
   SOURCE_STANDARDS.md -> SCORING_RUBRIC.md -> DELIVERABLES_SPEC.md ->
   05_STATE/MASTER_STATE.json -> 10_CHAIN_MAP/SEED_CHAIN_MAP.md.
2. SEED_CHAIN_MAP.md is untrusted until re-verified: confirm every [REPORTED] against
   the underlying filing where possible; attempt to upgrade tags to [DISCLOSED];
   never downgrade silently - log changes in PROGRESS_LOG.md.
3. Financial-data hygiene: pull numbers from cninfo/exchange filings and company IR
   pages first; press second; never from stock-promo posts. Record CNY figures with 亿
   originals in parentheses. Note report date next to every market cap or multiple.
4. Subagents in .claude/agents/ exist for: filings-analyst, exposure-verifier,
   valuation-analyst, red-team-critic, compliance-gate, source-auditor. Use them in
   parallel where independent; exposure-verifier must sign off before a dossier is
   marked complete.
5. Update 05_STATE after each phase; STOP at human gates defined in MASTER_STATE.json.
6. Outputs are research. If any draft sentence reads as advice ("you should buy"),
   rewrite as evidence + scenario ("evidence supports X; this would be falsified by Y").
