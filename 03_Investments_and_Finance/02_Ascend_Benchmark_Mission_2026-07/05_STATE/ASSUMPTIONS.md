# ASSUMPTIONS
(mission-time assumptions logged here instead of asking the user)

- **A1 (concurrency, 2026-07-06):** Parallel workers write per-ticker fragment files
  (`10_.../rows/<ticker>.csv`, `90_BIBLIOGRAPHY/frags/p1_<ticker>.json`, and phase-2/3
  equivalents). The orchestrator merges fragments into the canonical CSVs and
  `sources.json` after each wave. End state is identical to SOURCE_STANDARDS; this only
  prevents concurrent-write clobbering of shared files by 4 parallel agents.
- **A2 (source-ID ranges, 2026-07-06):** To prevent ID collisions, each worker receives a
  pre-assigned S-ID block (P1: S100–S299; P2: S400–S599; P3 valuation: S600–S699;
  red team: S700–S799; orchestrator/P4: S800+). Prior-corpus entries keep S001–S016,
  all `verified:"snippet"` (they were never fetched this mission; they are context only,
  never load-bearing).
- **A3 (filing vintage, 2026-07-06):** "Latest annual + interim" = FY2025 annual report
  (A-share/HK, published 2026-03/04) + latest 2026 quarterly report available by today
  (Q1 2026, published 2026-04). 1H2026 interim reports are NOT yet published (due
  ~2026-08) — workers must not claim them.
- **A4 (fiscal years, 2026-07-06):** Phase-2 "3 FY" = FY2023, FY2024, FY2025 (A-share
  fiscal year = calendar year). Plus Q1-2026 where disclosed, marked as quarter.
- **A5 (timezone, 2026-07-06):** Host clock is US Pacific (2026-07-06 22:52 PT =
  2026-07-07 13:52 Beijing). Market-data as-of timestamps use the timezone stated by the
  quote source; workers record the exact datetime string shown by the source.
- **A6 (SMIC listing line, 2026-07-06):** SMIC is analyzed under 688981 (SSE-STAR); the
  0981.HK line is noted where relevant (H-share filings on HKEXnews are valid primary
  sources for the same issuer). Any portfolio row would use the A-share line, since the
  simulation is a 100,000 CNY A-share paper account.
- **A7 (universe additions, 2026-07-06):** Per brief, Phase 1 may add ≤5 names at
  tier ≤B. Additions are decided after wave 3 from (a) prior-corpus tier-B leads and
  (b) names surfaced by wave-1..3 filing audits. Additions receive the same full P1
  treatment in wave 4. No addition implies any ranking.
- **A8 (exposure semantics, 2026-07-06):** `exposure_est_pct` = estimated share of FY2025
  total revenue attributable to Huawei/Ascend/Kunpeng-linked business, method shown.
  Where only a customer-concentration figure exists and the top customer is not proven
  to be Huawei, workers must NOT equate the two silently — the method column must state
  the inference and its weakness, or return NOT-ESTIMABLE.
- **A9 (workbook tooling, 2026-07-06):** `python3` may not exist on this Windows host;
  the Phase-4 workbook uses whichever of `python`/`python3` resolves, with openpyxl
  installed via pip if absent. Values-only workbook per brief.
- **A10 (universe additions, 2026-07-07):** ONE name added in Phase 1: 软通动力 301236
  (ISV / Ascend all-in-one machines) — tier-B lead = 科创板日报 Huawei Connect 2025
  official partner list [S012] + RB_02; fills the ISV layer absent from the initial 13.
  NOT added (reasons, no ranking implied): 科大讯飞 002230 (chain role is predominantly
  Ascend compute BUYER, not supplier — poor fit to a supply-chain universe); 意华股份
  002897 / 航天电器 002025 (bare-list mention in one 西部证券 weekly [S204] with no
  elaboration per two independent reads; layer already covered by 688629 at tier A/B);
  英维克 002837 (did not clear tier ≤B for Ascend during wave-3 verification); 华虹半导体
  688347 (tier-B DISCOVERY in V_688981, surfaced after the additions decision — mature-node
  foundry, secondary to the claim under test; logged here for the founder's own follow-up).
  Universe = 14 names, within the ≤18 cap.
- **A11 (frag quoting defect, 2026-07-07):** The 301018 source fragment escaped literal
  quotes CSV-style ("" instead of \") inside JSON strings, corrupting sources.json on
  merge. Fixed by bounded replace in the S220–S232 block + frag rewrite; full-ledger
  parse now validates (183 entries, no dupes). Wave-4+ worker prompts explicitly require
  backslash-escaping in JSON; orchestrator now parse-validates every frag before splice.
- **A12 (scoring conventions, 2026-07-07):** Rubric anchor gaps resolved and documented
  in 30_PHASE3_VALUATION_SCORING/SCORING_NOTES.md "Global anchor interpretations":
  verified-false links score W1=0 for the claimed channel; filing-grade BOUNDS may
  substitute for point estimates in W2 (ceiling/floor mapped to the matching band);
  intermediate integers 2/4 are documented interpolations; tiebreak extension beyond the
  rubric's W1→W4 is W2→W3→ticker order (ticker-order ties carry no information and are
  treated as midrank ties for Spearman). No rankings restated here per rule 4.
- **A13 (CSV disclaimer convention, 2026-07-07):** Rule 3 requires the disclaimer to
  open EVERY file in 10_/20_/30_/40_, including CSVs. Convention: line 1 = verbatim
  disclaimer, line 2 = CSV header, data from line 3. Consumers (workbook builder,
  self-test instructions) skip line 1.
- **A14 (transport cleanup, 2026-07-07):** Per-ticker rows/ fragment files (transport
  for concurrency-safe merging, per A1) were deleted after byte-identical assembly into
  the canonical CSVs. frags/*.json under 90_BIBLIOGRAPHY are retained as the merge audit
  trail (90_ is outside rule-3 scope).
- **A15 (predictions schema, 2026-07-07):** The lab's PREDICTIONS_LOG.csv is outside this
  mission's readable scope (rule 6; not shipped in 00_PRIOR_CORPUS). PREDICTIONS_APPEND.csv
  therefore uses the schema id,date_made,prediction,falsifier,resolve_by,confidence_pct,
  source_basis,status — believed compatible in spirit; if the lab's column names differ,
  map 1:1 on merge (every concept is present).
- **A16 (workbook build, 2026-07-07):** BENCHMARK_WORKBOOK.xlsx is built by
  05_STATE/tools/build_workbook.py (python+openpyxl, sanctioned by rule 12 for the final
  workbook only). Tab sources: UNIVERSE+VERIFIED_WATCHLIST -> Verified_Universe;
  FUNDAMENTALS.csv -> Fundamentals; VALUATION.csv -> Valuation; SCORES.csv -> Scores;
  BENCHMARK_PORTFOLIO.csv -> Portfolio; sources.json -> Sources. CSV consumers skip the
  A13 disclaimer line; every tab's A1 note carries the disclaimer + as-of date instead.
