# Binding operating rules

Mission: `01_MISSION/MISSION_BRIEF.md`. State: `05_STATE/MASTER_STATE.json`. After compaction or
restart, reread those two files and continue from the first incomplete checkpoint.

1. Stay inside this project root for all file reads/writes and shell work. Web access is allowed.
   Never inspect sibling rounds; this round must be independently generated.
2. No user interaction. Resolve ambiguity with the most conservative reasonable assumption,
   append it to `05_STATE/ASSUMPTIONS.md`, and continue.
3. Founder background is a shallow implementation prior only. Do not select lanes, seeds, or
   ideas because they resemble prior HTS/GaN work. Apply founder fit only after evidence-first
   ideas exist, and cap its score at 5/100.
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
