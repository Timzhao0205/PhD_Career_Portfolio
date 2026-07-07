# START HERE — Ascend Benchmark Mission (autonomous answer key for your learning self-test)

One command → Claude Code runs a 6-phase, multi-agent, filing-verified mission: it audits
every supply-chain claim from primary filings, extracts fundamentals, scores the universe
against a fixed rubric, red-teams the leaders, and writes a benchmark paper portfolio —
the ANSWER KEY you'll grade your own analysis against.

Paper-only, simulated 100,000 CNY, not investment advice — the mission's CLAUDE.md makes
those rules binding on every agent.

## What you'll get

- `10_PHASE1_VERIFICATION/` — one filing-audit memo per company: is the Huawei/Ascend
  link real, at what evidence tier, with what revenue exposure (this upgrades the lab's
  tier-C rumor map to filing-grade).
- `20_PHASE2_FUNDAMENTALS/` — 3-year financials per company + FUNDAMENTALS.csv.
- `30_PHASE3_VALUATION_SCORING/` — date-stamped valuations, SCORES.csv per the rubric,
  red-team attacks + written responses. **Spoilers start here.**
- `40_PHASE4_PORTFOLIO/` — ANSWER_KEY_BENCHMARK.md, BENCHMARK_PORTFOLIO.csv,
  BENCHMARK_WORKBOOK.xlsx (Excel, 6 tabs), SELF_TEST.md, PREDICTIONS_APPEND.csv.
- `99_AUDIT/` — independent audit: source ledger ≥60 (≥25 primary filings), 20-figure
  number-truth re-fetch, spoiler-boundary check.

## One-time setup

Same as your 02_Startup missions: Claude Code installed + logged in (Max account). Place
this folder at `PhD_Career_Portfolio\03_Investments_and_Finance\` next to
`01_Market_Learning_Lab_2026-07\` (the launcher syncs the lab's watchlist/briefs as the
mission's input corpus; shipped copies are the fallback).

## Run it

```powershell
cd <path>\PhD_Career_Portfolio\03_Investments_and_Finance\02_Ascend_Benchmark_Mission_2026-07
.\RUN_BENCHMARK.ps1
```

`-Mode guarded` for enforced permission guardrails; `-Resume` after any interruption
(state checkpoints to disk after every phase and wave).

## Usage-budget plan (based on your 2026-07-06 screenshot: Max 20x; weekly All-models 17% used, Fable 28% used, resets Sun 4:00 AM)

- **Orchestrator + red-team + synthesis → Fable** (`--model claude-fable-5`, session
  effort MAX). These are the judgment-heavy steps where accuracy pays; you have ~72% of
  the weekly Fable pool in hand and ~6 days to reset — comfortable headroom.
- **Bulk workers (filing-auditor, fundamentals-analyst, valuation-analyst, source-auditor)
  → pinned to Sonnet** in their agent files. Filing fetch-and-extract doesn't need Fable,
  and this keeps most of the token volume on the all-models pool (83% remaining).
- **Sessions**: a full run is realistically 1–2 of your 5-hour session windows. If the
  session cap hits mid-run, wait for the reset and `.\RUN_BENCHMARK.ps1 -Resume`; nothing
  is lost. Rough expectation — not a guarantee — is a mid-double-digit % draw on the
  weekly Fable pool; glance at Settings → Usage between phases if you're planning other
  Fable work this week.

## Self-test protocol (the actual point)

1. Run the mission to COMPLETE.
2. **Blind attempt first.** Read `10_PHASE1_VERIFICATION/` and `20_PHASE2_FUNDAMENTALS/`
   freely — this is the same evidence base the scorer used. Do NOT open `30_` or `40_`.
3. Copy `01_MISSION/SELF_TEST_MY_ATTEMPT_TEMPLATE.md` to
   `40_PHASE4_PORTFOLIO/MY_ATTEMPT.md` and fill it: your full ranking, your 100K paper
   allocation, your three convictions with confidence %.
4. Now open `SELF_TEST.md` and `ANSWER_KEY_BENCHMARK.md`. Score yourself: Spearman rank
   correlation, allocation overlap, and — most valuable — the disagreement log: for every
   divergence, decide whose evidence was stronger and which LEARNING_ROADMAP stage the
   gap maps to.
5. Merge `PREDICTIONS_APPEND.csv` into the lab's `PREDICTIONS_LOG.csv` and write the
   journal entry. In 6–12 months, the resolved predictions grade BOTH of us.

A benchmark disagreement is not an error signal by itself — the mission can be wrong too
(it says so in its own uncertainty section). The learning is in argument quality, not in
matching the key.
