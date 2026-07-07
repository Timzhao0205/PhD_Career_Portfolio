# CLAUDE.md — Operating Rules (binding; Market Learning Lab)

Read on session start or after compaction: this file, `00_README_START_HERE.md`,
`05_STATE/PROGRESS_LOG.md`. Files are ground truth. Reader is a technically fluent EE PhD
student learning markets from zero; explain finance concepts on first use, once.

## Hard rules

1. **PAPER-ONLY (absolute).** Never connect to a brokerage, trading API, or payment system.
   Never execute, queue, or draft real orders. Simulated positions exist only as rows in
   `30_FINDINGS/PAPER_PORTFOLIO.csv`. If asked to trade for real, refuse and cite this rule.
2. **NUMBER TRUTH RULE (absolute).** Never write a price, revenue, margin, market cap, or
   any financial figure that was not fetched THIS session from a source recorded in
   `90_SOURCES/sources.json` with `verified:"fetched"`. Model memory is not a source.
   A figure seen only in a search snippet is marked `"snippet"` and may support color only,
   never a load-bearing claim. Inventing or pattern-completing a number is a session-failing
   defect.
3. **NOT FINANCIAL ADVICE.** Every file written to `10_RESEARCH/` and `30_FINDINGS/` opens
   with: "Educational analysis for a paper-trading learning exercise. Not investment
   advice." Verdicts are WATCH / RESEARCH-MORE / DROP + confidence %. No buy/sell/target-
   price language anywhere.
4. Stay inside this folder. Web via WebSearch/WebFetch only. Never touch `../` or other
   portfolio folders.
5. Source discipline per `90_SOURCES/SOURCE_STANDARDS.md`. Chinese-language searching is
   REQUIRED for any A-share, Huawei, or China-policy question; English-only search on these
   topics is a defect.
6. Evidence tiers on every supply-chain claim: A (target company's own filing/exchange
   announcement), B (major financial media or named sell-side research), C (forum/social/
   blog — leads only). Tier C claims may never be load-bearing.
7. State discipline: after each session append one line to `05_STATE/PROGRESS_LOG.md`
   ([ISO date] stage= files_touched= predictions_open=). Park tangents in
   `05_STATE/OPEN_QUESTIONS.md`.
8. Keep the host light: plain CSV/JSON state, no databases, no background daemons, no
   scheduled jobs. Python (pandas, yfinance, akshare) allowed for on-demand scripts saved
   to `40_SCRIPTS/` (create when first needed).
9. Style: terse, quantitative, engineer-voice; every file readable standalone.

## Mission backlog (run on request, in order)

- **M1 — price snapshot script.** `40_SCRIPTS/fetch_watchlist.py`: pull latest close for
  every WATCHLIST.csv row (yfinance for HK/US, akshare for A-shares), write dated snapshot
  CSV to `30_FINDINGS/snapshots/`. No auto-scheduling.
- **M2 — supplier filing audit.** For each tier-C watchlist row: fetch the company's latest
  annual report / investor-relations reply; upgrade to B/A with citation or mark
  UNVERIFIED. Update RB_02 and WATCHLIST.csv.
- **M3 — weekly review assistant.** Read snapshots + open predictions + journal; draft the
  Sunday review for human editing. Never auto-resolve predictions without a fetched source.
- **M4 — calibration scorer.** Compute brier per resolved prediction and running mean;
  append to PREDICTIONS_LOG.csv; plot to `30_FINDINGS/calibration.png`.
