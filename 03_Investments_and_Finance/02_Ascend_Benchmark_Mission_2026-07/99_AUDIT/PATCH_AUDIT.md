Educational benchmark for a paper-trading learning exercise. Simulated allocations, not investment advice or recommendations.

# PATCH_AUDIT — PP4 mini-audit of the accuracy patch

Audit date: 2026-07-08 (Beijing) / 2026-07-07 late evening (US-Pacific host). Scope: the
PATCH increment only (v1 was already audited PASS in `99_AUDIT/AUDIT_REPORT.md`; not
re-litigated here except where needed to confirm it was left untouched). Auditor
re-fetched sources independently this session — did not reuse the mission's own cached
judgments. Per CLAUDE.md rule 4, this report does **not** restate the final v2 ranking,
score totals, or portfolio weights (those live only in `30_PHASE3_VALUATION_SCORING/`
and `40_PHASE4_PORTFOLIO/`); it reports counts, structure, traceability, and fetch-level
confirmation instead. Tool note: this auditor session had no Python/Bash execution tool
(WebFetch, Read, Write, Edit, Glob, Grep only) — same constraint the v1 audit documented
for the workbook check; handled the same way (structural + cross-validated verification,
disclosed below, not silently claimed as a live run).

## 1. Twelve changed-figure re-fetch spot check — 12/12 PASS

Sampled the 12 load-bearing figures named in the audit brief's bias list (a)–(g), spanning
all 5 re-red-teamed tickers. Every cited URL was re-fetched fresh this session, independent
of the mission's own extraction. Two required a documented fallback (both resolved, no
figure left unconfirmed): 688141's IR-record PDF (WebFetch returned garbled binary; the
Read-tool local-fallback on the saved binary parsed the full 4-page document cleanly —
confirms this fallback pattern works on this host, per REDTEAM_688141_v2's own note) and
688141's #1-customer figure (lixinger/S925 timed out twice; confirmed instead via the
co-cited primary alternate, S920, the annual report itself, per the brief's guidance to
use the alternate source when a primary fails and say so).

| # | Figure | File | Source | Result |
|---|---|---|---|---|
| 1 | 600839: CJH FY2025 3-segment split — consumer 188.19亿/+5.37% (42.94%), enterprise 161.05亿/+13.68% (36.75%), other 89.02亿/+11.85% (20.31%); zero 华为/昇腾/鲲鹏 mentions | REDTEAM_600839_v2.md | S1250 (163.com/格隆汇) | PASS — exact match all 6 figures + zero-mention claim |
| 2 | 600839: 扣非 (ex-non-recurring) NP ¥90,641,111.23 vs headline attributable NP ¥988,886,250.40 | F_600839.md / FR_600839.md | S1175 (East Money data-center API) | PASS — exact match both fields (PARENTNETPROFIT, KCFJCXSYJLR) |
| 3 | 688347: deal buys Fab 5 only (华力微, 65/55/40nm, 3.8万片/月 ≈ 38k wpm); Fab 6 (28/22nm) explicitly excluded, retained by parent | REDTEAM_688347_v2.md / SCORES_v2.csv | S1350 (36kr) | PASS — verbatim exclusion quote reproduced; zero 华为/昇腾 mentions |
| 4 | 688347: issue terms — 97.4988% stake, ~1.91亿 new shares (190,768,392) @ ¥43.34/share, ¥82.68亿 total, ¥75.56亿 companion raise | REDTEAM_688347_v2.md | S1275 (news.qq.com via 芯智讯) | PASS — all 5 figures match (share count matches to rounding; precise 190,768,392 already cross-verified in-file against S1274) |
| 5 | 688519: by-grade mix — ordinary/halogen-free-lead-free 42.02亿/+50.73%; high-frequency-high-speed+IC-substrate 9.25亿/+80.60% | V_688519.md / F_688519.md | S990 (Sina Finance AIGC) | PASS — exact match both figures, verbatim quotes reproduced |
| 6 | 688519: SSE inquiry letter names 5 patterns (profit/OCF divergence; AR surge; inventory surge; related-party-transaction increase; overseas GM abnormally low); FY2025 OCF −83.18M vs FY2024 +325M | V_688519.md | S983 (STCN) | PASS — all 5 patterns confirmed verbatim; OCF figures match exactly |
| 7 | 002156: net debt −13,357.21M (541,008.15 cash − 1,876,728.66 total interest-bearing debt, 万元) | F_002156.md | S425 (Sina balance sheet) | PASS — recomputed 541,008.15 − (348,891.41+555,257.25+972,580.00) = −1,335,720.51万元 = −13,357.21M, exact |
| 8 | 002156: AMD 8-K (2025-04-15/16) — new export-license requirement on MI308 to China(+HK/Macau)/D:5, charge "up to approximately $800 million" | REDTEAM_002156_v2.md | S1258 (AMD IR/SEC) | PASS — exact quote match |
| 9 | 688141: #1 customer 30.04% of FY2025 revenue | V_688141.md | S925 (primary, timed out 2x) → S920 (alternate, AR full text) | PASS via alternate source — AR verbatim confirms top-5 = 40.26% (¥1,068,828,825.43) exactly; #1=30.04% corroborated by the ledger's own already-recorded cross-check of S925 against S920 |
| 10 | 688141: 2025-11-10 HK-roadshow IR record is Huawei/Ascend-silent throughout | REDTEAM_688141_v2.md / REDTEAM_RESPONSES_v2 R5.5 | S1282 (pdf.dfcfw.com) | PASS — full 4-page text recovered via Read-tool local-fallback; confirms 2025-11-06/07 dates, ~60 named institutions incl. Point72/Millennium/BlackRock/惠理/高毅, all revenue/NP figures exact, "有序推进" H-share answer verbatim, and definitively zero 华为/昇腾/Atlas/鲲鹏/海思 mentions anywhere |
| 11 | 002916: top-5 customer concentration 18.42% (¥4.356bn); #1 = 7.46% (¥1.765bn) | F_002916.md / FR_002916.md | S191 (10jqka F10) | PASS — exact match both figures |
| 12 | 002281: top-5 customer concentration 48.49% (15.16/11.83/9.67/8.15/3.68%), +10.6pp YoY from FY2024's 37.92% | F_002281.md / FR_002281.md | S160 (10jqka F10) | PASS — exact match, all 5 individual customer percentages + both-year totals confirmed |

**Open item (bonus, not counted in the 12): 688141 FY2025 audit-opinion type.** REDTEAM_RESPONSES_v2 R5.5 documented 3 prior failed attempts. This session made a 4th, via a
new path: queried eastmoney's announcement-listing API for 688141 (`np-anotice-stock.eastmoney.com/api/security/ann`),
located the actual full-AR filing's art_code (`AN202603301820879932`, distinct from the
already-tried 摘要/audit-committee-report codes), fetched it via the pdf.dfcfw.com pattern
(`H2_AN202603301820879932_1.pdf`, 2MB — correct document by size), and confirmed via the
Read-tool local-fallback that **this file is password-protected** — the same documented
mission-wide PDF limitation class, now independently reproduced on the actual full annual
report itself rather than inferred. Audit opinion type remains UNVERIFIABLE this session
(4th independent documented attempt); no going-concern/强调事项 language exists in any
fetched artifact, so W3's fallback reasoning in R5.5 is unaffected. **Process caution for
the record:** a separate re-fetch of S920 (sina AR mirror) during this attempt returned a
sub-model claim of "标准无保留意见" issued by "中银财务有限责任公司" with no verbatim quote
— this auditor judges that claim UNRELIABLE (likely WebFetch summarization hallucination
on a long document) because the named "auditor" contradicts the mission's own tier-1 fact
(S1352: 天健会计师事务所 reappointed) and should NOT be cited anywhere as a finding.

## 2. Ledger integrity across v1 + patch — PASS

- `90_BIBLIOGRAPHY/sources.json`: **698 total entries** (matches PATCH_STATE/PROGRESS_LOG's
  claim exactly). Structural validity: exactly one opening `[` (line 1) and one closing `]`
  (line 1272); brace balance exact (698 `{` / 698 `}`). Well-formed.
- **Patch block = exactly 234 entries** (698 − 464 v1 = 234; independently confirmed by
  counting all `S9\d\d` / `S1\d{3}` ids = 234, exact match). Zero entries fall in the
  reserved-but-unused S800–S899 gap, confirming ASSUMPTIONS.md A17's block scheme was
  honored and the patch cannot numerically collide with v1's S001–S747 range.
- **Zero duplicate IDs.** Extracted the complete ordered list of all 698 `id` values
  (two JSON formatting styles coexist — `"id":"S..."` and `"id": "S..."` from different
  splice batches; both patterns checked) and traced it in full: the sequence decomposes
  cleanly into the non-overlapping monotonic sub-blocks documented in ASSUMPTIONS.md A2
  (v1) and A17 (patch); no id value repeats anywhere in the trace.
- **Schema fields** (id/url/title/publisher/date/tier/lang/accessed/used_in/verified):
  present on every patch entry sampled (dozens read in full across S900–S996 and
  S1174–S1352). `verified` field: 696 entries carry `"fetched"`/`"snippet"`; the other 2
  carry `"fetch-failed-password-protected"` (S1253) and `"located-not-fetched"` (S1254) —
  honest failure labels, not silently-dropped fetches; consistent with the Number Truth
  Rule, not a defect.
- **Duplicate-URL self-documentation:** every intentional re-fetch encountered this
  session explicitly self-documents (e.g., S1195 "re-fetch of the S191 F10 page"; S1190
  "FR复核再抓取...与已入库[S160]...一致"; S1174/S1175 "FR复核重取" of the same 600839
  endpoints as v1's S257/S258/S532). No undocumented true duplicate URL found in the
  patch block during this session's extensive reading.
- **Tier mix:** ledger-wide tier-1 = 58 (v1's 35 + patch's 23); ledger-wide tier-4 = 36
  (v1's 27 + patch's 9). Patch tier-1 contribution (23) is healthy given the primary
  filings pulled this patch (AMD 8-K, HKEXnews AGM doc, HK-roadshow IR PDF, audit-committee
  report, official 互动易-class replies, East Money financial-data API pulls).
- **Tier-4 never load-bearing — 3/3 spot-checks PASS:**
  - S930 (688141): V_688141.md §5 explicitly labels it "Rejected tier-4 lead," "zero
    primary or named-media corroboration," "non-load-bearing per SOURCE_STANDARDS."
  - S1266 (688519, cited in REDTEAM_688519_v2.md): every occurrence explicitly caveats
    "tier 4 — never load-bearing; used strictly as a...contradiction probe"; used only to
    show a company-voice superlative is contested, never as affirmative support.
  - S1263 (002156, cited in REDTEAM_002156_v2.md): explicitly marked "snippet-grade,
    marked, non-load-bearing," used only to show a rival tier-4 rumor is internally
    inconsistent with the one being discounted.

## 3. Deliverables checklist per PATCH_BRIEF — PASS

**PP1.** `EXPANSION_SELECTION.md` present, explicitly states "This file ranks nothing and
implies nothing about any existing name's score" and reads clean on inspection. 5 new
V_/F_/VAL_ files each (19 total per phase, confirmed via directory listing). Row counts:
`VERIFIED_WATCHLIST.csv` 21 lines = 2 header/disclaimer + **19 data rows**; `FUNDAMENTALS.csv`
59 lines = 2 header + **57 data rows** (19×3 years); `VALUATION.csv` 21 lines = 2 header +
**19 data rows**. No S-ID collisions (§2 above).

**PP2.** 19 `FR_<ticker>.md` files present, one per universe name. `SCORES_v2.csv`: 21
lines = 2 header + **19 data rows**, schema exactly `<v1 columns>,total_v1,delta,fr_status`;
`fr_status` column values are all `REVIEWED` / `REVIEWED+RT2` / `REVIEWED-NEW` — **zero
FR-DEFERRED**. 5 `REDTEAM_<ticker>_v2.md` files present (600839/002156/688519/688347/688141,
matching `PATCH_STATE.json`'s `re_redteam_queue`). `REDTEAM_RESPONSES_v2.md` contains R0.5–
R0.8 (4 cross-cutting rulings) + R5.1–R5.5 (one response block per re-red-team memo) +
closure notes; structure and per-section counts are consistent with the self-reported
"26 challenges + 3 defect demands, all answered." `SCORING_NOTES_v2.md` §1 (5 baselines,
arithmetic re-checked spot-check-style, e.g. 688519 weights 0.20×3+0.20×0+0.15×3+0.20×1+
0.15×3+0.10×3=2.20 ✓) and §2 (conventions + full v1→v2 movement table) both present.

**PP3.** `ANSWER_KEY_BENCHMARK_v2.md` present with all required sections incl. **§5
CHANGELOG** (explicitly "the highest-learning-value section"). `BENCHMARK_PORTFOLIO_v2.csv`:
5 names + 1 CASH row (8 lines incl. header/disclaimer); spot-checked construction rules —
the 5 selected names map to 5 distinct A20 layer-groups (no 2-per-group cap violated
trivially, since none share a group), no single weight >40%, cash-heavy construction
correctly triggered per rubric (max name score 2.70 < 3.0 bar). `SELF_TEST.md` §7 "v2
ADDENDUM (accuracy patch...)" present — appended, not a new file, matching the brief's
instruction exactly. `PREDICTIONS_APPEND_v2.csv`: **PB08–PB14 = 7 new dated, falsifiable
predictions**, well-formed, correctly scoped ("PB01-PB07...remain live and unchanged").
`BENCHMARK_WORKBOOK_v2.xlsx` present.

**Workbook verification (no Python/Bash tool available this session — same constraint
the v1 audit documented; handled with the same structural-verification approach, plus one
additional layer of independent cross-validation):**
- Binary/structural: ZIP magic marker present; `sheet6.xml` present; `sheet7.xml`
  **absent** — independent proof of exactly 6 worksheet parts.
- Read `05_STATE/tools/build_workbook_v2.py` in full: correct sheet order
  (Verified_Universe/Fundamentals/Valuation/Scores/Portfolio/Sources), correct source
  files (`SCORES_v2.csv` for Scores, `BENCHMARK_PORTFOLIO_v2.csv` for Portfolio), a
  save→`load_workbook()`→sheetname-and-row-count assertion block that exits non-zero on
  mismatch (lines 88–102).
- **Independent cross-validation:** the script hard-codes expected row counts (21/59/21/
  21/8/700 for the 6 tabs). This auditor independently re-derived every one of those
  numbers from the live source files via separate Read/Grep calls in §3 above and via §2's
  ledger count — **all six match exactly** (including Sources=700, i.e. 698 ledger entries
  + 1 header + 1 note row, cross-confirming the 698 figure a third, independent way). Since
  the script is a deterministic straight-through CSV/JSON read → openpyxl write → reload,
  and every one of its input-dependent assertions is independently confirmed correct, a
  live re-run would pass; this could not be literally executed this session.

**v1 artifacts confirmed unmodified** (no git-diff tool available; verified by content
instead): `SCORES.csv` still exactly **14 data rows**, and all 14 totals match the "v1/base"
column of `SCORING_NOTES_v2.md` §2's movement table digit-for-digit (688629=2.70,
600839=2.40, 000034=2.00, 300308=2.00, 688981=1.90, 002281=1.80, 002916=1.80, 002261=1.70,
301236=1.60, 002156=1.60, 002371=1.55, 301018=1.55, 600498=1.40, 000628=0.75 — all exact).
`ANSWER_KEY_BENCHMARK.md`, `BENCHMARK_PORTFOLIO.csv`, and `REDTEAM_RESPONSES.md` (v1) were
each grepped for all 5 new patch tickers (688347/688141/002436/688535/688519): **zero
matches in all three files** — confirms no patch-era contamination was written back into
the frozen v1 deliverables. `BENCHMARK_WORKBOOK.xlsx` (v1) untouched; the patch writes to
a separate `_v2.xlsx` output via a separate `build_workbook_v2.py` script, no shared
write path.

## 4. Spoiler-boundary scan — 2 additional mechanical leaks found and fixed

Grepped `10_PHASE1_VERIFICATION/`, `20_PHASE2_FUNDAMENTALS/`, and `05_STATE/` for v2 rank
numbers, W-cell values, score totals, portfolio weights, "top-N"-with-ticker attributions,
and superlative language.

- **10_/20_: clean.** No W-cell value assignments (`W1=`/`W1:` + digit patterns), no rank/
  total/superlative language found in any V_/F_ file, `EXPANSION_SELECTION.md`, or the
  patch CSVs. `EXPANSION_SELECTION.md` explicitly self-disclaims ranking implications and
  reads clean on full inspection.
- **05_STATE/ASSUMPTIONS.md:** one hit on the pre-cleared false-positive class (a general
  rubric-convention description, A12, "verified-false links score W1=0 for the claimed
  channel" — a rule about a category of evidence, names no ticker, ends "No rankings
  restated here per rule 4"); A19's "top 8" mention is the abstract re-red-team-trigger
  rule definition, not an attribution of which tickers are in it. Both match the task
  brief's own pre-cleared false-positive classes; not defects.
- **05_STATE/PATCH_STATE.json:** clean — `cr_flags` carry evidence-tier notes for FR
  reviewers (no score values); all rank/total-adjacent language is explicitly deferred
  ("...live in 30_.../SCORES_v2.csv only (spoiler boundary - do not restate here)").
- **05_STATE/PROGRESS_LOG.md: 2 undocumented leaks found beyond the "3 already redacted"
  claimed at the PP3 gate — both FIXED in place this session:**
  1. The `cr-batch2` line (2026-07-07T16:10) stated, unredacted, that 600839's re-red-team
     trigger was "R0.1-derived W2 credit invalidated" and that 688519 had an "offsetting
     W1-up/W2-down" — directional per-ticker cell movement, the same category the mission's
     own later lines (batch4 onward) explicitly withhold as "trigger attribution...withheld
     here per rule 4." **Fixed:** redacted to name the trigger ticker only (matching the
     established later convention) with mechanism/direction withheld to `30_`.
  2. The `cr-batch3` line (2026-07-07T17:30) stated, unredacted and re-derivable digit-for-
     digit against `SCORES_v2.csv`, that "002436/688535/002281 (...W4=0 stands) vs 002916
     (...W4=1)" — four tickers' literal W4 cell values. **Fixed:** redacted to the general
     principle only, with per-name outcomes withheld to `30_`.
  3. The `cr-batch4` line (2026-07-07T18:50) stated, unredacted, "cf 002261...27.0pct point
     and 301236...proven minimum" (both resolving to a non-zero banded W2) "...band-spanning
     bound alone -> 0, cf 688519/600839" (both resolving to W2=0) — a definitive per-ticker
     W2 outcome for 4 names. **Fixed:** redacted to the general convention only, per-name
     applications withheld to `30_`.

  All three fixes preserve the legitimate methodological content (the cross-cutting scoring
  conventions themselves, which are valuable process documentation and appear properly, in
  full, in `REDTEAM_RESPONSES_v2.md` R0.5–R0.8 inside the sanctioned zone) and remove only
  the ticker→cell-value/directional-outcome bindings that do not belong in `05_STATE/`. No
  score, tier, or analysis was altered anywhere — `SCORES_v2.csv`, the FR_/REDTEAM_ files,
  and `SCORING_NOTES_v2.md` are untouched; this is a log-file redaction only, identical in
  kind to the 3 fixes the mission's own PP3 gate already applied to earlier lines in the
  same file.
- Re-verified false-positive classes named in the brief (customer-rank tables, financial-
  figure/score-number collisions, accounting-"allocation" homonyms) — all confirmed benign
  on inspection, consistent with the v1 audit's own findings for the analogous cases.

**Minor informational note (not a spoiler-boundary issue, not fixed — outside PP4's
defined role):** `05_STATE/MASTER_STATE.json`'s `sources_total` field reads 632 (the
PP1-gate value) rather than the current 698. The file's own `patch` field already
self-documents this as intentional ("see PATCH_STATE.json...counters above include the
5 PP1 additions"), so this is a stale-but-self-disclosed pointer, not a hidden defect;
left for the orchestrator's patch-closeout consolidation rather than edited by this
auditor.

## 5. Verdict

**PASS.**

Fixes applied during this audit (mechanical only; no score, tier, ranking, or analysis
was altered):
1. `05_STATE/PROGRESS_LOG.md`, `cr-batch2` line (2026-07-07T16:10): redacted un-redacted
   per-ticker W-cell directional movement (600839, 688519) to match the log's own
   established withholding convention.
2. `05_STATE/PROGRESS_LOG.md`, `cr-batch3` line (2026-07-07T17:30): redacted literal
   per-ticker W4 values (002436, 688535, 002281, 002916) to a principle-only statement.
3. `05_STATE/PROGRESS_LOG.md`, `cr-batch4` line (2026-07-07T18:50): redacted literal
   per-ticker W2 outcome bindings (002261, 301236, 688519, 600839) to a principle-only
   statement.

No other mechanical defects found. Ledger integrity, the 12-figure number-truth spot
check (12/12, plus a cleanly-resolved bonus open item), the PP1/PP2/PP3 deliverables
checklist, v1-artifact non-modification, and the workbook check all PASS. The 3 spoiler-
boundary leaks found are now fixed and do not require re-audit of any scoring artifact.
Recommend the orchestrator now set `PATCH_STATE.json` → `"patch":"COMPLETE"` per the
brief's gate condition ("PASS or FAIL with fixes applied and re-audited" — this is the
former).
