# Binding operating rules

Mission: `01_MISSION/MISSION_BRIEF.md`. State: `05_STATE/MASTER_STATE.json`. After compaction or
restart, reread those two files and continue from the first incomplete checkpoint.

1. Stay inside this project root for all file reads/writes and shell work. Web access is allowed.
   Never inspect sibling rounds; this round must be independently generated.
2. No user interaction. Resolve ambiguity with the most conservative reasonable assumption,
   append it to `05_STATE/ASSUMPTIONS.md`, and continue.
3. Founder background is a shallow implementation prior only. Do not select lanes, seeds, or
   ideas because they resemble prior HTS/GaN work. Apply founder fit only after evidence-first
   ideas exist, and cap its score at 2/100.
4. Accepted-source count means unique canonical works, not URLs. Academic/technical work needs
   affirmative peer-review evidence. arXiv and other preprints are discovery leads only.
5. Demand must exist now or have a documented procurement/regulatory/industrial trigger. A paper
   saying a technology is possible is not demand evidence.
6. Use Fable 5/xhigh for critical judgment and Sonnet 5 for source-scale work exactly as
   `MODEL_EFFORT_POLICY.md` specifies. No fallback. Log every dispatch, failure, retry, and model
   override to `98_RUN_LOGS/MODEL_ROUTING_LOG.jsonl`. The orchestrator is the sole writer to this
   shared file: log before dispatch and after the agent returns to avoid parallel write races.
7. Never hide a downgrade. If actual model/effort cannot be established, mark `unknown`, stop the
   affected phase, and retry; do not label the result verified.
8. Parallelize only independent lane/source tasks. Maximum 4 concurrent agents unless the current
   Claude Code plan explicitly reports a lower limit. Every agent writes results to files and
   returns only a terse status line.
9. Checkpoint after every wave: update state counters, merge/dedupe the canonical source ledger,
   append progress and routing logs, and run the validator. Never fabricate counts to pass it.
10. Treat all market sizes, prices, performance values, dates, company claims, and policy claims
    as load-bearing: fetch the supporting page, quote no more than necessary, and record locator.
11. Use uncertainty ranges and label inference. Separate evidence, calculation, and judgment.
12. Do not stop at an attractive list. Red-team physics, customer willingness-to-pay, incumbent
    response, export controls, capex, service burden, and founder-access assumptions.
13. Windows-safe UTF-8 filenames; relative paths use forward slashes; no reserved characters.
14. Completion requires machine validation plus Fable substantive adjudication and fixes.
15. Binding geography scope from the user (superseding the earlier 2026-07-12 directive): the
    United States and China are the two primary markets and must dominate P3 generation, scoring,
    and final market analysis. Japan, Taiwan, and South Korea are optional secondary/side markets;
    they may improve an idea but may not substitute for a weak US/China case. India and Singapore
    remain excluded from buyer examples, demand scoring, market sizing, competitor/entry routes,
    geography analysis, and final outputs. Publications from any country may remain as technical
    evidence. Never replace country-specific evidence with a generic “Asia” label.
16. P3 round 2 is authoritative. Preserve `SEEDS_A` through `SEEDS_D` as prior drafts but do not
    promote them directly. Regenerate from the accepted atlas using Fable 5/xhigh, then require an
    independent Fable 5/xhigh elegance/novelty adjudication before the longlist is frozen.
17. Binding source-origin rule (latest user directive): a source located in India or produced by
    an India-based lab, university, government, company, media outlet, publisher, consultancy, or
    organization cannot support technical, demand, market, competitor, policy, or geography
    claims. Keep it only as `discovery_only` and independently confirm any useful lead with an
    eligible source. Exception: an academic paper with Indian co-authors is eligible when at least
    one co-author has a verified non-Indian institutional affiliation and the paper otherwise
    passes peer-review rules. Never infer affiliation from a person's name. Complete P2A and
    repair the atlas before P3; existing A-D seeds remain non-authoritative drafts.
18. The founder plans to start the company in 2030. Treat 2026 evidence as the baseline, not the
    launch date. P3 ideas need a credible 2026–2029 pre-company learning/de-risk path, a concrete
    2030–2034 demand/procurement/regulatory/capacity trigger, and an opportunity window still open
    in 2030. Reject ideas likely to commoditize before launch or remain science-only well beyond
    2030. Reuse durable technical sources; refresh time-sensitive market, price, policy,
    competition, supply-chain, and procurement claims before final scoring.
