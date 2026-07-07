# MISSION_BRIEF — Ascend Benchmark: filing-verified scoring of the supply-chain universe

Objective: produce a fully traceable model answer to the question "which listed names in
the Ascend/Kunpeng supply chain best merit inclusion in a paper learning portfolio today,
and why" — packaged so the founder can attempt the same question independently from the
Phase-1/2 evidence and then grade himself against the key. Educational benchmark;
simulated allocations; not investment advice.

## Universe
Start = the 13 names in 00_PRIOR_CORPUS/WATCHLIST.csv. Phase 1 may add up to 5 names
discovered with tier ≤B evidence during verification (hard cap 18). No name is silently
dropped: failed verification stays in the universe as UNVERIFIED with reasoning (that IS
a finding). Names spanning both Nvidia-chain and Ascend-chain demand (e.g., optics) get
an explicit exposure-split note.

## Phases, quotas, gates

### P0 — Setup
Read prior corpus; write universe list to 05_STATE (names only, no ordering); init state.

### P1 — Verification (filing-auditor × 4/wave)
Per name: latest annual + interim report fetched; 互动易/上证e互动 replies searched;
evidence tier assigned (A/B/C/UNVERIFIED); Huawei-linked revenue exposure estimated with
method, or NOT-ESTIMABLE.
Outputs: `10_PHASE1_VERIFICATION/V_<ticker>.md` per name + `VERIFIED_WATCHLIST.csv`
(schema: ticker,exchange,name,layer,tier,exposure_est_pct,exposure_method,key_quote,src_ids).
**Gate G1:** 100% of universe audited; every name has ≥2 fetched primary sources or a
documented search trail explaining why not.

### P2 — Fundamentals (fundamentals-analyst × 4/wave)
Per name: 3-FY revenue+YoY, gross/net margin, OCF, capex, net debt/cash, top-5 customer
concentration, R&D intensity.
Outputs: `20_PHASE2_FUNDAMENTALS/F_<ticker>.md` + `FUNDAMENTALS.csv`
(ticker,fy,revenue,rev_yoy_pct,gm_pct,nm_pct,ocf,capex,net_cash,top5_conc_pct,rd_pct,src_ids).
**Gate G2:** no empty cell without a MISSING justification; all load-bearing figures
verified:"fetched".

### P3 — Valuation + scoring (valuation-analyst × 4/wave, then orchestrator, then red-team-critic × 3)
Per name: date-stamped price/market cap; P/E ttm, P/S (EV/EBITDA where inputs exist),
arithmetic shown; implied-expectations paragraph with PRICED-FOR-PERFECTION / NEUTRAL /
SKEPTICALLY-PRICED flag. Orchestrator scores every name per 01_MISSION/SCORING_RUBRIC.md
into `SCORES.csv` (one row per name, one column per weighted dimension + total + rank),
each cell citing the file that supports it. Red team attacks the top 6; orchestrator
answers every challenge in writing (`REDTEAM_RESPONSES.md`) and rescores where conceded.
**Gate G3:** every score cell traceable; every red-team challenge answered; final
SCORES.csv is post-rescore.

### P4 — Benchmark portfolio + self-test kit
- `BENCHMARK_PORTFOLIO.csv`: fictional 100,000 CNY across 4–6 names + cash remainder
  (name,ticker,amount_cny,weight_pct,thesis_1line,exit_trigger,review_date).
- `ANSWER_KEY_BENCHMARK.md`: full reasoning — final ranking with per-name paragraph,
  what separated in/out names, portfolio construction logic (diversification across
  layers, common-mode policy risk cap), top-3 uncertainties.
- `SELF_TEST.md`: instructions for the blind attempt — read 10_/20_ only; fill
  01_MISSION/SELF_TEST_MY_ATTEMPT_TEMPLATE.md; then open the key and score:
  (a) Spearman rank correlation between attempt and key rankings (formula + worked
  example included), (b) allocation overlap %, (c) disagreement log — for each
  divergence, whose evidence was stronger and what concept explains the gap; (d) map
  each gap to a LEARNING_ROADMAP stage to study next.
- `PREDICTIONS_APPEND.csv`: ≥5 falsifiable 6–12-month predictions with confidence %
  (same schema as the lab's PREDICTIONS_LOG.csv) for the founder to merge and later score.
- `BENCHMARK_WORKBOOK.xlsx` via python3+openpyxl — tabs: Verified_Universe,
  Fundamentals, Valuation, Scores, Portfolio, Sources. Values only (no live formulas
  needed); every tab's header row notes the as-of date.
**Gate G4:** disclaimers on every file; spoiler boundary intact; xlsx opens via openpyxl
round-trip test.

### P5 — Audit (source-auditor × 1)
Ledger ≥60 unique sources post-dedupe, Tier-1 primary filings ≥25, zero Tier-4
load-bearing; 20-figure number-truth spot re-fetch; quota, spoiler-boundary, and workbook
checks. Output `99_AUDIT/AUDIT_REPORT.md`. Mission COMPLETE only on PASS or on FAIL with
every fix applied and re-audited.

## Sizing guidance (honest estimates, not promises)
13–18 names × (2–4 filing fetches + quote fetch) + red team ≈ 60–120 web fetches and a
few hundred file operations. Expect 1–2 five-hour session windows. If a session or weekly
cap interrupts: state is on disk; relaunch with `RUN_BENCHMARK.ps1 -Resume`.
