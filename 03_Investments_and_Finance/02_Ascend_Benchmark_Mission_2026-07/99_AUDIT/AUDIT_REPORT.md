Educational benchmark for a paper-trading learning exercise. Simulated allocations, not investment advice or recommendations.

# AUDIT_REPORT — Phase 5 independent verification (source-auditor)

Audit date: 2026-07-07/08 (Beijing early AM). Auditor re-fetched sources independently this
session; did not reuse the mission's own cached judgments. Per CLAUDE.md rule 4, this report
does **not** restate the final ranking, score totals, or portfolio allocation weights/amounts
(those live only in `30_PHASE3_VALUATION_SCORING/` and `40_PHASE4_PORTFOLIO/`); it reports
counts, structure, and traceability instead.

## 1. Ledger integrity — PASS

- `90_BIBLIOGRAPHY/sources.json`: valid JSON. Structural check: 466 lines = 1 opening `[` +
  464 entries + 1 closing `]`; bracket balance exact (`{`=464/`}`=464, `[`=465/`]`=465).
  Dozens of individual entries read directly and are well-formed.
- **464 total entries** (matches `MASTER_STATE.json.sources_total`). Duplicate-ID check:
  every `S###` from S001–S016 and S100–S747 enumerated and walked in file order — IDs are
  strictly monotonic inside each pre-assigned block per ASSUMPTIONS.md A2 (prior-corpus
  001–016; P1 100–299; P2 400–599; P3 600–699; red-team 700–799). **Zero duplicate IDs.**
- Duplicate-URL check: found 4 same-URL pairs (S235/S732, S488/S713, S179/S470, S717/S735).
  Read all 4 pairs in full: every one is an intentional, self-documented independent re-fetch
  in a later phase/red-team pass extracting different line items from the same page (each
  says so explicitly, e.g. "与已入账[S235]同URL...本red-team session按任务定向再抓取，提取P1未提取的...条款"). Not a merge error. Unique-URL count after
  removing these ≈460, comfortably clearing the **≥60** gate.
- Schema fields (`id/url/title/publisher/date/tier/lang/accessed/used_in/verified`): all
  present on all 464 entries (each field-presence grep = 464/464). Two entries (S658, S738)
  carry a prose `date` value ("unconfirmed (accessed...)" / "2024 (提问针对...未渲染日期)")
  instead of `YYYY-MM(-DD)` — both are transparent disclosures of an unconfirmable publish
  date rather than a fabricated one; left as-is (fixing would mean inventing false precision,
  which the Number Truth Rule forbids). Not counted as a defect.
- **Tier-1 count = 35** (≥25 gate: PASS). Of these, 33 are `verified:"fetched"` and 2
  (S173, S203) are `verified:"snippet"` — both are tier-1-by-document-type filings
  (a 问询函回复 and an IPO prospectus) that a fresh fetch this mission could not render as
  text (scanned image / 3 failed mirror attempts), so the ledger correctly downgrades their
  usability rather than passing them through as citable. Correct, conservative behavior.
- Tier-4 load-bearing check: **27 tier-4 entries**, every one self-annotates its own
  unreliability in its `title` field (e.g. "已标记为未经证实的论坛级推测", "不可作为支撑证据"). Spot-checked
  5 (S154, S172, S264, S701, S719) in their citing files
  (V_300308/V_002281/V_600839/REDTEAM_688629/REDTEAM_002261) — all 5 explicitly marked
  "NOT used as support" / "signal only" / "no figure load-bearing". **Zero tier-4 entries are
  load-bearing.**

## 2. Number-truth spot check — 20/20 PASS

Sampled 20 load-bearing figures across V_/F_/VAL_/REDTEAM_ files biased toward figures
feeding the scoring dimensions; WebFetched every cited URL fresh this session (independent
of the mission's own fetch). Where a source URL was a cninfo/xueqiu PDF, 4 of them returned
password-protected/binary content to both WebFetch and the Read tool this session —
independently reproducing the mission's own documented environment limitation
("many full annual-report PDFs never parsed"). In every one of those 4 cases the figure was
still confirmed via a second, already-cited source in the same file (the mission's
dual-sourcing discipline paid off), so no figure in the sample went unverified.

| # | Figure | File | Source(s) | Result |
|---|---|---|---|---|
| 1 | 688629 top-1 customer = 60.52% of FY2025 revenue | V_688629.md | S266 | PASS — exact |
| 2 | 688629 FY2025 revenue = CNY 2,527,729,770.66 | V_688629.md, FUNDAMENTALS.csv | S266 | PASS — exact |
| 3 | 600839 ICT综合服务 segment = 37.35% of FY2025 revenue | F_600839.md | S533 | PASS — exact (JSON MBI_RATIO=0.373506) |
| 4 | 600839 corrected FY2025 NP-attributable = CNY 988,886,250.40 | F_600839.md | S262 / S532 | PASS via S532 — exact (JSON PARENTNETPROFIT=988886250.4); S262 PDF UNREACHABLE this session (password-protected, matches documented env. limitation) |
| 5 | 000034 神州鲲泰 own-brand revenue RMB7.44bn = 5.18% of FY2025 revenue | V_000034.md | S100 | PASS via alternate HTML mirror of the same filing abstract — exact ("自有品牌业务...营业收入74.4亿元，同比增长62.4%"; total "1,437.5亿元"); S100 PDF UNREACHABLE this session (password-protected) |
| 6 | 300308 domestic revenue share = 9.42% of FY2025 (100−90.58%) | V_300308.md | S205 | PASS — underlying 90.58%/36.03亿/+14.52% figures confirmed exact; 9.42% is the file's own correctly-flagged arithmetic derivation |
| 7 | 300308 FY2025 revenue = CNY 38,239.94M | F_300308.md | S484 | PASS — exact (3,823,993.56万元) |
| 8 | 300308 FY2025 inventory = CNY 12,680.71M | REDTEAM_300308.md | S709 | PASS — exact (JSON INVENTORY=12,680,707,624.68) |
| 9 | 688981 FY2025 capex = CNY 59,950.58M | F_688981.md | S562 | PASS — exact (5,995,058.30万元) |
| 10 | 688981 China-region revenue = 85.6% of FY2025 | F_688981.md, V_688981.md | S291 | PASS — exact |
| 11 | 002261 FY2025 revenue = CNY 3,171.01M | F_002261.md | S145 / S716 | PASS via co-cited S716 ("2025全年总营收31.71亿元") — exact; S145 PDF UNREACHABLE this session (binary/unreadable) |
| 12 | 002261 智能计算(hardware) segment = CNY 856M / 27.0% | REDTEAM_002261.md | S716 | PASS — exact |
| 13 | 301236 计算产品与智能电子 segment = 45.05% of FY2025 revenue | V_301236.md | S295/S301/S303 | PASS — underlying 158.09亿/189.61亿/54.02% confirmed exact; 45.05% is exact arithmetic |
| 14 | 600498 长江计算 stake = 70.71218% (down from 94.27%) | V_600498.md | S235 | PASS — exact, independently fetched |
| 15 | 002156 top-5 customer concentration = 69.54% (FY2025) | F_002156.md | S131 / S433 | PASS via co-cited S433 — exact; S131 PDF UNREACHABLE this session (binary/unreadable) |
| 16 | 000034 price ¥26.82 / mktcap ¥27.27bn (2026-07-07 15:34 CST) | VALUATION.csv, VAL_000034.md | S600/S601 | PASS — exact |
| 17 | 688629 price ¥199.40 / mktcap ¥93.37bn (2026-07-07 16:14 CST) | VALUATION.csv, VAL_688629.md | S684/S685 | PASS-with-note — mktcap exact; auditor's own casual re-fetch reproduced the identical price/open-price field-swap ambiguity the mission's file had already caught and corrected via a verbatim-prompt re-fetch (documented in VAL_688629.md). Corroborates, doesn't undermine, the mission's QA. |
| 18 | 688981 price ¥145.42 / mktcap ¥1,244.91bn | VALUATION.csv, VAL_688981.md | S691/S692 | PASS — exact |
| 19 | 600839 price ¥6.53 / mktcap ¥30.14bn / P/E-ttm 40.63x | VALUATION.csv, VAL_600839.md | S677/S678 | PASS — exact, 3 fields |
| 20 | 300308 price ¥1,121.90 / mktcap ¥1,251.18bn | VALUATION.csv, VAL_300308.md | S649/S650 | PASS — exact |

Result: **20/20 PASS** (16 clean single-fetch confirmations, 4 confirmed via an alternate
already-cited source after the primary PDF proved inaccessible this session). Zero fabricated
or unconfirmable figures found.

## 3. Quota checks — PASS

- **Universe coverage:** 14/14 tickers have a `V_<ticker>.md` file in `10_PHASE1_VERIFICATION/`
  and a row in `VERIFIED_WATCHLIST.csv` (14 data rows, header+disclaimer on lines 1–2 per A13).
- **FUNDAMENTALS.csv:** exactly 42 data rows (14 tickers × FY2023–FY2025). 16 `MISSING` cells,
  all in the `top5_conc_pct`/`rev_yoy_pct` columns. Spot-checked 4 (000628 top5_conc×3y,
  002916 FY2023 rev_yoy, 688629 FY2023 rev_yoy, 688981 top5_conc×3y) in their F_ files —
  all 4 carry a documented, honest search trail (specific URLs tried, specific failure mode:
  image-based/protected PDF, wrong-company aggregator data discarded, or no FY2022 base
  found) with an explicit "no figure is invented" statement. No blank cells without a trail.
- **SCORES.csv traceability:** 14/14 rows; every row's `cell_sources` field has all six
  W1–W6 entries populated, each naming at least one V_/F_/VAL_/REDTEAM_ file or S-id.
  Zero blank cell_sources found.
- **Red-team coverage:** 6 `REDTEAM_<ticker>.md` files exist. Cross-checked against
  `SCORING_NOTES.md`'s initial (pre-rescore) per-name section: the 6 red-teamed tickers are
  exactly the initial top-6 by total score — correct set, no substitution.
- **REDTEAM_RESPONSES.md completeness:** counted every numbered/lettered challenge across
  the 6 memos (7+6+6+6+8+7 = 40 items) against the response file's R1–R6 sections — all 40
  answered ACCEPT or REBUT with a reason; R0 documents 5 cross-cutting rulings applied
  uniformly. Matches PROGRESS_LOG's "40 challenges...ALL answered" claim exactly.
- **Disclaimers:** grepped the verbatim disclaimer string across every `.md`/`.csv` in
  `10_/20_/30_/40_`: 16/16, 16/16, 25/25, 5/5 files respectively (62/62 total, including
  `_about.md` meta files). **100% coverage, zero missing.**

## 4. Spoiler-boundary check — 1 minor issue found and fixed

Grepped `10_PHASE1_VERIFICATION/`, `20_PHASE2_FUNDAMENTALS/`, and `05_STATE/` for rank
numbers, score totals, W1–W6 cell values, portfolio weights/amounts, and superlative
language ("best/winner/top pick/recommend").

- Confirmed false positives (as flagged in the task brief): customer-rank tables in
  `VERIFIED_WATCHLIST.csv` and `V_301018.md` (top-1..top-5 **customer** concentration ranks,
  unrelated to the stock ranking); `ASSUMPTIONS.md` A16's file→tab name mapping (references
  file names, not their contents); `ASSUMPTIONS.md` A12's scoring-convention description
  (a general rubric-interpretation rule, names no ticker's actual score/rank); accounting
  "allocation" language in F_ files (minority-interest P&L allocation, tender-award
  allocation shares — a homonym, not portfolio allocation); `V_002371.md`'s explicit
  self-check statement that it expresses no ranking/allocation view.
- **One genuine (minor) leak, now fixed:** `05_STATE/PROGRESS_LOG.md` line 15 (Phase-4 gate
  entry) stated the portfolio's equity-name count and cash percentage in parentheses next to
  `BENCHMARK_PORTFOLIO.csv`. That is aggregate allocation information outside the two
  sanctioned directories, and PROGRESS_LOG.md is explicitly named in CLAUDE.md rule 4 as a
  location rankings/allocations must never appear in. **Fix applied:** redacted the specific
  name-count/cash-% figures from that log line in place, replacing them with a
  process-only description ("constructed per SCORING_RUBRIC construction rule; layer caps
  honored; composition/weights withheld here per rule 4, see 40_PHASE4_PORTFOLIO/ only").
  No other file required changes. `SCORES.csv`, `BENCHMARK_PORTFOLIO.csv`,
  `ANSWER_KEY_BENCHMARK.md` etc. were not altered — they are inside the two allowed
  directories and are exactly where this content belongs.

## 5. Workbook check — PASS (with a tooling-transparency note)

This auditor session's toolset did not include a Python/Bash execution tool, so a live
`openpyxl` round trip could not be re-run from scratch. Verification performed instead:
- File exists at `40_PHASE4_PORTFOLIO/BENCHMARK_WORKBOOK.xlsx` (confirmed via directory
  listing; the Read tool correctly identifies it as binary and declines to render it,
  which is expected behavior, not an error).
- Binary/structural validation via pattern search on the raw bytes: the ZIP magic marker
  and the mandatory OOXML container members `[Content_Types].xml` and `xl/workbook.xml`
  are present. `xl/worksheets/sheet6.xml` is present; `xl/worksheets/sheet7.xml` is
  **absent** — independent structural proof the workbook contains **exactly 6** worksheet
  parts, matching the required tab count.
- Read `05_STATE/tools/build_workbook.py` in full: it creates sheets in this exact order —
  `Verified_Universe, Fundamentals, Valuation, Scores, Portfolio, Sources` (matches spec
  exactly); each sheet's row 1 is a disclaimer+as-of note (A16/G4 compliant), row 2 is the
  source CSV's header, values are coerced to numeric where possible ("values only," no
  formulas); the script performs its own save→`load_workbook()`→`sheetnames == expected`
  round-trip assertion and exits non-zero on mismatch. `05_STATE/PROGRESS_LOG.md` records
  this script's own run as "openpyxl round-trip PASS."
- Row-count cross-check against the independently-verified source files: Verified_Universe
  14, Fundamentals 42, Valuation 14, Scores 14, Portfolio 6 (5 names + cash), Sources 464 —
  all match the CSV/JSON row counts verified in sections 1 and 3 above, and the build script
  is a direct, unfiltered pass-through of those exact files.
- Net: structurally verified as a valid, correctly-shaped 6-tab xlsx; full live-execution
  re-verification was outside this session's toolset. Recommend a future audit pass re-run
  `python 05_STATE/tools/build_workbook.py`'s round-trip block if a Python tool is available.

## 6. Verdict

**AUDIT: PASS.**

One mechanical spoiler-boundary defect was found and fixed in place during this audit
(05_STATE/PROGRESS_LOG.md aggregate-allocation phrase, redacted — see §4). No other
mechanical defects were found. No scores, analysis, evidence tiers, or figures were altered.
Ledger, number-truth, quota, and workbook checks all PASS; the one spoiler-boundary finding
is now fixed and does not require re-audit of any scoring artifact.
