Educational benchmark for a paper-trading learning exercise. Simulated allocations, not investment advice or recommendations.

# REDTEAM_002261 — 拓维信息 Talkweb (SZSE 002261) — adversarial review

Role: red-team-critic. Mandate: attack, not balance. Date: 2026-07-07 (Beijing).
Inputs: V_002261.md, F_002261.md, VAL_002261.md, SCORES.csv row (W1=5 W2=3 W3=2 W4=1
W5=1 W6=1, total 2.35, rank 3/14), SCORING_NOTES.md, SCORING_RUBRIC.md, RB_02.
New sources this session: [S716]–[S721], ledgered in 90_BIBLIOGRAPHY/frags/rt_002261.json
(all fetched 2026-07-07, Chinese-language). All other [S###] are the input files' own
citations. Per SCORING_RUBRIC rules, no score changes without a written orchestrator
response in REDTEAM_RESPONSES.md — challenges C1–C6 below each require one.

## 0. New evidence fetched this session (what it changes)

1. **FY2025 segment split — the cell Phase 1/2 could not obtain — now exists at tier 3
   [S716]:** 国产智能计算 (hardware) = CNY 856M = 27.0% of revenue; 软件及考试服务 =
   2,219M = 70.0%; 鸿蒙 = 96M = 3.0%. Passes the only available arithmetic check
   (8.56+22.19+0.96 = 31.71亿 = S145's tier-1 total revenue exactly). Its segment GROSS
   MARGINS (7.8%/25.6%/41.6%) do NOT reconcile to the tier-1 blended gross profit
   (implied 674.8M vs actual 517.8M [S145;S444]) — margins flagged unreliable, revenue
   split usable as single-source tier-3.
   → Derived: FY2025 hardware revenue 856M vs FY2024 hardware 2,071.7M (50.44% × 4,107.17M
   [S151;S145]) = **-58.7% YoY collapse of the thesis segment.**
2. **China Mobile 2024–2025 新型智算中心 tender winner table [S717]:** total ~CNY 191.04亿
   (excl. tax, 公示 2024-05-16); shares: 昆仑技术(超聚变) 21.05%, 华鲲振宇 17.54%, 宝德
   15.79%, 百信 14.04%, 长江计算 12.28% (~23.46亿), 神州鲲泰 10.53%, 湘江鲲鹏 (Talkweb)
   **8.77% (~16.75亿) — smallest of the seven winners.**
3. **Warning-letter specifics [S718]:** decision (2026)18号 received 2026-05-07; five
   individuals warned INCLUDING chairman 李新宇, plus 宋鹰, 宋隽逸, both board
   secretaries (龙麒, 邢霓虹); rectification within 3 months (≈2026-08-07) + written
   report within 15 working days after, copied to SZSE. V_002261 had the finding but not
   the chairman's inclusion or the deadline clock.
4. **Verticalization precedent [S721]:** 2021-11-08 registry change — Huawei's own x86
   server unit 超聚变 transferred to 河南超聚能; per [S717] that entity (昆仑技术/超聚变)
   now holds the LARGEST share (21.05%) of the very tender Talkweb ranked last in.
5. **Information-pollution exhibits [S719, S720]:** tier-4 claims of "90–100亿 in-hand
   orders", "5,000 units of 昇腾950P in 2026", "双钻石伙伴" (contradicts the company's own
   认证级 certificates in S145); stockstar headline "近1年无研报覆盖" (2026-05-08)
   directly conflicts with S623's "4 buy ratings in 90 days" (2026-03-02). Adds to the
   already-flagged S154 fabrication (claimed >50亿 Ascend revenue vs 31.71亿 actual TOTAL
   revenue [S145]).
6. **Negative result, third mirror:** the full FY2025 annual report (公告编号 2026-009,
   ~214pp) is password-protected at the 10jqka notice mirror too (Read attempt today),
   matching F_002261's finding on the sina mirror. **No session this mission has read the
   FY2025 customer/supplier concentration tables at tier 1.** Every load-bearing
   concentration number on this name is a tier-3 restatement.

## 1. Strongest bear case (5 bullets)

- **B1. The core business loses money and the headline P/E is an accounting artifact.**
  Ex-non-recurring net profit: FY2023 +15.67M → FY2024 -101.29M → FY2025 -40.19M [S145];
  TTM ex-NR = **-23.31M, a trailing LOSS** [VAL_002261 from S145;S146]. The positive
  headline (FY2025 +63.74M; Q1 2026 +61.46M) is manufactured by non-recurring items —
  Q1 2026 alone booked +69.21M of non-recurring gains including a CNY 66.00M
  receivables-impairment-provision reversal [S146]. At CNY 28.80 (2026-07-07 close
  [S621;S622]) the market pays 606.30x a profit that does not exist on a core basis, and
  11.55x sales of a business whose revenue FELL -22.79% in FY2025 [S145; VAL_002261].
- **B2. The Ascend-thesis segment collapsed -59% in the chain's boom year.** 智能计算
  revenue: ~2,071.7M / 50.44% of revenue (FY2024 [S151;S145-derived]) → 856M / 27.0%
  (FY2025 [S716]). This happened while universe peers grew +131.5% (688629), +60.25%
  (300308), +44.20% (002281), +39.55% (301018), +32.05% (002916), +30.85% (002371)
  [SCORING_NOTES citing the F_ files]. A company whose Huawei-hardware line more than
  halves during the sector's best year is losing allocation/share, not riding the wave —
  and the 27% ceiling still bundles Kirin-9000C/X PCs and Kunpeng-only servers, so the
  Ascend-specific slice is strictly smaller and unquantified [V_002261].
- **B3. No allocation moat: smallest of seven interchangeable integrators, and it buys
  from its own bigger rival.** In China Mobile's 191.04亿 AI-server tender, 湘江鲲鹏 took
  8.77% — last of seven winners; 华鲲振宇 took 2x that (17.54%) and ex-Huawei 超聚变 took
  21.05% [S717]. 华鲲振宇 is simultaneously Talkweb's **#2 supplier at 12.24% of FY2024
  procurement** [S150;S437] — Talkweb partially resells the kit of the competitor that
  outranks it. Commodity-integrator economics confirmed by the claimed 7.8% FY2025
  hardware gross margin [S716, flagged] vs the 16.33% company blend [S145;S444].
- **B4. The filings the whole tier-A story rests on carry a regulator-stamped
  false-records finding.** 湖南证监局 decision (2026)18号: director 宋隽逸 never actually
  performed his duties, his father 宋鹰 acted in his place, and board resolutions AND
  periodic reports therefore contained 虚假记载 (false records); the CHAIRMAN and both
  board secretaries are among the five warned; rectification deadline ~2026-08-07
  [S153;S718]. The abstaining director declined to vouch for the accuracy of BOTH
  documents this mission's W1=5 is built on (FY2025 AR summary, Q1 2026 report)
  [S145;S146 cover pages]. A 606x-multiple stock whose board-process disclosures were
  formally found false, booking judgment-dependent impairment reversals to stay
  headline-positive, is a governance-and-earnings-quality compound risk.
- **B5. Double-sided Huawei chokehold, unreadable FY2025 tables, and a polluted
  information environment.** Procurement: top-5 suppliers = 81.01%, Huawei Investment
  Holding alone = 61.29% (FY2024, two independent tier-3 restatements [S150;S437]); a
  June-2026 tier-3 analysis claims 63.46% Huawei procurement dependence for what is
  plausibly FY2025 [S716, single-source]. Customers: top-5 = 72.75% of FY2024 revenue
  [S437]; the widely-circulated "Huawei #2 customer at 25.6%" remains snippet-grade —
  today's search results recirculated the same 25.6%/29.43%/12.09亿 numbers mislabeled as
  "2025年前三季度" when the arithmetic (29.43% × 4,107.17M = 1,208.7M = 12.09亿) proves
  they are FY2024 — nobody, including this mission, has tier-1 access to any FY2025
  concentration table (password-protected at three mirrors). Meanwhile the bull numbers
  refute each other: >50亿 2025 Ascend revenue (S154, debunked by S145), >80亿 2026
  revenue (S624, internally inconsistent), 60–70亿 2026 target and 90–100亿 in-hand
  orders [S716;S719, unverifiable], "4 buy ratings in 90 days" [S623] vs "no research
  coverage in a year" [S720 headline]. On this name, the load-bearing negative facts are
  tier-1 and the entire upside case is tier-3/4 noise.

## 2. Score audit — every cell, supported or not

| Cell | Current | Supported by files? | Red-team proposal | Challenge |
|---|---|---|---|---|
| W1 | 5 | Partially — link existence yes; filing-reliability premium no | **4** | C1 |
| W2 | 3 | No longer — new FY2025 point shows in-band but collapsing | **1** (fallback 2) | C2 |
| W3 | 2 | No — flattered by OCF timing; core loss 2 consecutive years | **1** | C3 |
| W4 | 1 | Yes (anchor floor for tier-A PFP) | 1, keep — aggravators must be logged | C5 (no score change) |
| W5 | 1 | Yes — reinforced by new evidence | 1, keep | — |
| W6 | 1 | No — undercounts dual-sided concentration + live regulator action | **0** (fallback 1 with written literalism defense) | C4 |
| Total | 2.35 (rank 3) | — | **1.50 aggressive / 1.95 minimum-concession** | C6 (rank/tiebreak) |

Proposed-total arithmetic: aggressive = 4(.20)+1(.20)+1(.15)+1(.20)+1(.15)+0(.10) =
0.80+0.20+0.15+0.20+0.15+0.00 = **1.50** (≈ rank 13 of 14 on current totals);
minimum-concession = 4(.20)+2(.20)+2(.15)+1(.20)+1(.15)+1(.10) = 0.80+0.40+0.30+0.20+
0.15+0.10 = **1.95** (≈ rank 8). Either way 002261 exits the top tier.

### C1 — W1: 5 → 4 (evidence strength is impaired, not pristine)

The anchor for 5 is "tier A (own filing / official IR reply names the business)". The
link EXISTS at tier A — not disputed: [S145] names Kunpeng/Ascend as the 兆瀚 technical
base, [S148]/[S155] corroborate. But W1 measures evidence STRENGTH, and three defects cap
this cell below the pristine-filing premium:

1. **Regulator-impaired filings.** The exact documents carrying the tier-A language are
   the periodic reports in which 湖南证监局 found 虚假记载 (false records) about
   board-review status, warning five officers including the chairman [S153;S718]; the
   one director positioned to dissent abstained on BOTH [S145;S146]. The finding is
   narrow (governance process, not financials), but "own filing" earns the 5 because it
   is presumed the most reliable evidence class — that presumption is formally damaged
   here in a way it is not for any other W1=5 name (301236, 600498, 000034 carry no
   equivalent regulatory finding per their V files).
2. **Partnership language is a status claim, not a transaction record.** "全方位战略合作"
   is self-description. The only Huawei-COUNTERSIGNED artifacts disclosed are 认证级
   certificates: "昇腾万里伙伴计划**认证级**昇腾**部件**伙伴" and "鲲鹏展翅伙伴计划认证级
   鲲鹏整机伙伴" [S145, quoted in V_002261]. Note what that says: on the ASCEND side the
   company's own filing discloses a **component-partner** certificate, not an Ascend
   整机 (complete-machine) certificate — while the mission's own files show peers holding
   named HIGHER grades: 000034 神州鲲泰 "鲲鹏+昇腾双**领先级**" [V_000034;S106], 600498
   长江计算 "鲲鹏领先级、昇腾**优选级**整机硬件伙伴" [V_600498;S246], 301236 "鲲鹏、昇腾
   双**优选**" [V_301236]. Three named tiers appear across this mission's evidence
   (领先级/优选级/认证级); Talkweb's disclosed grade is the lowest of them and the only
   one that is component-level (not 整机) on Ascend. Scoring 002261's W1 identical to
   000034's (both 5) while their Huawei-countersigned credentials differ by two named
   grades is an intra-mission inconsistency. Where 认证级 sits in Huawei's hierarchy was
   never established by any fetched source — an evidence gap the 5 glossed over.
3. **Zero tier-1 quantitative corroboration.** No purchase order, no customer table, no
   supplier table for ANY year has been read at tier 1 this mission (full ARs
   password-protected at three mirrors — re-confirmed today). The commercial magnitude
   behind the partnership words rests entirely on tier-3 restatements.

Precedent: the orchestrator already interpolated W1=4 for 688629 on a LESSER defect (the
brand word 昇腾 absent from company statements, everything else clean). A
regulator-found false-records finding inside the citing documents is a stronger defect.
**Proposed W1=4.** If the orchestrator keeps 5, the written response must explain why
filing-reliability impairment costs nothing in W1 while the same warning letter is also
absorbed costlessly into W6=1 (see C4) — it cannot be priced nowhere.

### C2 — W2: 3 → 1 (fallback 2): the exposure is in-band but collapsing

The 3 was set on "21.7% (H1-2025) to 50.4% (FY2024), inside 10–30% at latest reading,
not clearly growing as a share" [SCORING_NOTES]. The new FY2025 point [S716] replaces
that range: 27.0% — inside 10–30%, yes. But:

1. **Anchor grammar.** W2 anchors: "5 = >30% AND growing; 3 = 10–30%; 1 = <10% **or
   flat**". The "or flat" branch makes non-growth an independent route to 1. Talkweb's
   Huawei-linked segment is not flat — it fell **-58.7% in absolute revenue** (2,071.7M →
   856M) and -23.4pp in share (50.44% → 27.0%) in one year [S151;S716;S145-derived]. If
   "flat" scores 1, "halved" cannot score 3.
2. **The 27.0% is a ceiling for the wrong quantity.** The segment bundles Kirin PCs and
   Kunpeng-only servers [V_002261]; the Ascend-chain-specific share is strictly <27% and
   no source establishes a floor above 10%. The mission credits segment ceilings (global
   note 2), but a ceiling credited as a mid-band point should at least carry the
   trajectory penalty.
3. **Direction matters for the thesis.** W2=3 names are supposed to be meaningfully
   levered to the Ascend ramp. FY2025 proved the opposite lever: chain boomed, segment
   halved (B2). The exposure that exists is exposure to Huawei's allocation decisions,
   not to Ascend end-demand.

**Proposed W2=1** (in-band ceiling, sharply shrinking, Ascend-specific unquantified).
Minimum concession: 2, as a documented interpolation "in-band but confirmed declining."
The response must state which reading of "or flat" governs, because it decides the cell.

### C3 — W3: 2 → 1: earnings quality, not just "weak-mixed"

Facts: revenue -22.79% [S145]; core (ex-NR) result negative TWO consecutive fiscal years
(-101.29M, -40.19M) and negative TTM (-23.31M) [S145;S146;VAL_002261]; GM 16.33% still
4.2pp below FY2023's 20.52% [S436;S444;S446]; R&D expense CUT -24.7% over two years
(195.91M → 147.46M) while the story is an AI ramp [S444;S446]; headline profit both
periods manufactured by non-recurring items, dominated by receivables-impairment
reversals (+66.00M in Q1 2026 alone) [S145;S146]. The two props holding the cell at 2 —
positive OCF and net cash — are the weakest-quality items in the set: FY2025 OCF
(+778.22M) is 12x headline net profit, i.e., largely collection of old receivables
against a shrinking revenue base (a liquidation-flavored inflow, not earnings), and it
had already reversed to **-252.08M (-607.56% YoY) by Q1 2026** with net cash eroding
607.55M → 548.75M [S145;S146]. Anchor 1 = "deteriorating margins or persistent cash
burn": core net margin went positive → negative → negative; that IS deterioration, and
the cash-burn pattern has resumed in the newest quarter on record. Additional aggravator:
impairment-reversal-driven headline profit at a company whose disclosure processes just
drew a regulator rectification order [S718] is precisely the configuration where reported
"quality" deserves the discount. **Proposed W3=1.** If the orchestrator keeps 2, the
written response must justify counting FY2025 OCF as quality evidence despite the Q1 2026
reversal, and must reconcile with 301236's W3=1 (headline-profitable, OCF -242M) — the
current scoring pays 002261 a premium for cash that Q1 2026 shows is already leaving.

### C4 — W6: 1 → 0: the risk stack is the worst in the universe

Anchor 0 = "single-customer + internalization precedent (cf. in-house HBM)". Substance:

- **Quasi-single-source supplier side:** Huawei Investment Holding = 61.29% of FY2024
  procurement; Huawei-system combined ≈73.53%; top-5 = 81.01% [S150;S437]; claimed
  63.46% Huawei dependence in the June-2026 tier-3 analysis (plausibly FY2025, single
  source) [S716]. For an integrator, the allocation-granting supplier IS the
  single counterparty that decides revenue — economically equivalent to single-customer.
- **Concentrated customer side on top:** top-5 = 72.75% of FY2024 revenue [S437], led by
  China Mobile and (snippet-grade) Huawei itself — Huawei plausibly sits on BOTH sides
  of the P&L.
- **Internalization/re-tiering precedent, live and specific:** in-house HBM [RB_02 read
  #3]; Huawei's structural re-org of the 整机 layer itself (x86 divestiture 2021
  [S721]); seven interchangeable integrators splitting one tender with Talkweb LAST at
  8.77% [S717]; and Talkweb's own #2 supplier is competitor 华鲲振宇 [S150;S437].
- **Plus a risk class no other name carries:** a live regulatory rectification order
  with an open deadline (~2026-08-07) and the chairman among the warned [S718], and a
  parent-company accumulated deficit of -1,098.49M that legally blocks dividends [S145].

Consistency test: 002156 scored W6=2 with ONE 52.29% customer + policy common-mode
[SCORING_NOTES]. 002261 carries dual-sided concentration AND re-tiering exposure AND a
live regulator action AND dividend incapacity — currently priced only one notch lower.
**Proposed W6=0.** Fallback: if 0 is refused on strict "single-customer" literalism
(#1 customer ~29% is China Mobile, not >50%), the written response must (a) say so
explicitly, and (b) identify which cell prices the warning letter, because W6=1's note
lists it without it moving anything.

### C5 — W4: 1 supported; aggravators must enter the record (no score change)

PFP on tier-A evidence → 1 fits the anchor. But log: (i) on core earnings the P/E
denominator is NEGATIVE (-23.31M TTM) — "not meaningful" is worse than "606x" [VAL];
(ii) the -26% drawdown from 39.05 (2026-03-06 [S624]) to 28.80 [S621] did NOT normalize
the multiple — the de-rating so far removed froth, not expectation; (iii) P/S 11.55x on
a 16.33% GM implies ~71x gross profit for a shrinking-revenue integrator. W4=1 is the
floor only because the rubric has no lower rung for tier-A PFP; the response should
acknowledge this name sits at the bottom of that rung.

### C6 — Rank/tiebreak dependency (procedural)

Rank 3 vs 301236 (both 2.35) was awarded via extended tiebreak W3: 2 vs 1
[SCORING_NOTES global note 5]. If C3 lands (W3 2→1), the documented tiebreak sequence
(W1 tie 5=5 — or 4 vs 5 if C1 lands — then W2, then W3) flips or collapses the rank even
before totals move. The rank-3 position of this name hangs on its single most disputed
cell; the response must re-run the tiebreak explicitly under whatever cells survive.

## 3. Verticalization test (what if Huawei internalizes / re-tiers the layer)

The integrator layer is the easiest in the whole chain for Huawei to restructure,
because it already has — twice. Upstream, in-house HBM shows Huawei absorbing chain
value inward when strategically useful [RB_02 read #3/S003]; at the 整机 layer itself,
Huawei divested its x86 server business in 2021 [S721], and that divested entity
(昆仑技术/超聚变) now takes the LARGEST share (21.05%) of the China Mobile AI-server
tender in which Talkweb's 湘江鲲鹏 came last of seven at 8.77% [S717]. Ascend silicon
allocation among those seven-plus integrators is Huawei's unilateral, zero-cost lever:
no acquisition, no announcement — it simply ships more kits to 华鲲振宇 (already 2x
Talkweb's tender share, already Talkweb's own #2 supplier [S150;S437]) or promotes its
closest affiliates, and 兆瀚's pipeline re-tiers toward zero. Talkweb's disclosed
standing gives it no protection: its own filing shows the lowest-grade Huawei
certificates in this mission's evidence set (认证级, component-level on Ascend), versus
优选级/领先级 peers [S145;V_000034;V_600498;V_301236]. The FY2025 record — hardware
segment -58.7% while the chain boomed [S716;S151] — is observationally consistent with
such re-tiering ALREADY operating, and with the FY2025 concentration tables unreadable
at tier 1, the mission cannot exclude it. If Huawei zeroes the allocation, ~27% of
revenue at ~7.8% claimed gross margin [S716] evaporates with no contractual recourse in
evidence, while 61–63% of procurement remains Huawei-priced [S150;S437;S716] — Huawei
can also squeeze margin without ever formally cutting the cord. The software/考试 and
鸿蒙 lines (73% of revenue [S716]) would survive, but they are not why this name is
rank 3: the Ascend thesis dies, and with it the W1/W2 rationale.

## 4. Common-mode test (what falls with it)

- **One tender, three portfolio candidates:** 002261 (湘江鲲鹏 8.77%), 600498 (长江计算
  12.28%), 000034 (神州鲲泰 10.53%) are winners inside the SAME China Mobile 191.04亿
  award [S717]; China Mobile is also (snippet-grade) ~29% of Talkweb's FY2024 revenue.
  A single operator smart-compute capex pause hits ranks 3, 5, and 7 simultaneously.
- **Huawei demand/allocation shock:** falls together with 301236 (quasi-single-ecosystem,
  its own W6 note), 688629 (60.52% single-customer Huawei), 000034, 600498. That is
  ranks 1, 3, 4, 5, 7 — the top of the scoreboard is substantially ONE correlated
  Huawei-integrator/supplier trade; among top names only 300308 (overseas/Nvidia optics
  cycle) is largely orthogonal.
- **Policy reversal (信创 budget pause, or export-control relaxation reopening Nvidia
  supply):** RB_02 read #4 — the substitution mandate IS the demand. For 002261
  specifically the hit is double-barreled: the Ascend/Kunpeng hardware line AND the
  信创-flavored software/鸿蒙 overlay (73% of revenue) are the same policy bet. Falls
  with 000034, 301236, and second-order 002371/688981 (whose W6 notes already flag
  extreme policy common-mode).
- **Portfolio implication for Phase 4:** with max-2-per-layer and ≤40%-per-layer
  constraints [SCORING_RUBRIC], note that layer caps do NOT capture this cross-layer
  common-mode: an integrator (002261) + a connector maker (688629) + an ISV (301236)
  are different layers but one Huawei order book.

## 5. Five falsifiable checks (event + date + which side it supports)

| # | Observable event | Check date | Bear side if | Bull side if |
|---|---|---|---|---|
| 1 | H1 2026 业绩预告 (SZSE main-board forecast trigger: sign-change or ±50%) | by 2026-07-15 | Loss forecast, or a positive forecast explicitly resting on non-recurring items again; or silence followed by weak actuals | Forecast of positive 扣非 (ex-non-recurring) profit |
| 2 | H1 2026 interim report: revenue trajectory + 智能计算 segment share | by 2026-08-31 | Revenue flat/down YoY (vs H1 2025's 1,306.40M [S147]) or hardware share ≤25% — kills the 60–70亿 2026 narrative [S716] | Revenue ≥ +20% YoY AND hardware share ≥30% with GM not collapsing |
| 3 | Core-profit sign: H1 2026 扣非归母净利润; and share of headline profit from impairment reversals | by 2026-08-31 | Third consecutive core-loss period (after FY2024, FY2025 [S145]); reversals ≥50% of headline NP again | First positive core half-year since FY2023; reversals immaterial |
| 4 | Warning-letter closure: rectification (3 months from 2026-05-07) + written report (+15 working days), copied to SZSE [S718]; watch for escalation | ~2026-08-07 rectification; report ≈2026-08-28 | Escalation to 立案调查 (formal investigation), further regulatory measures, restatement, or missed deadline — retroactively voids the W1 filing premium | Clean closure, board seat regularized (宋隽逸 replaced or actually serving), no follow-up |
| 5 | (a) Any tier-1-readable FY2025/H1-2026 supplier-concentration datapoint (SZSE inquiry reply, 互动易, readable AR mirror); (b) Huawei partner-tier status at 华为全联接大会 season | by 2026-09-30 | (a) Huawei procurement share ≥65% (deepening, corroborating S716's 63.46%); (b) 湘江鲲鹏 still 认证级/component-level on Ascend | (a) Huawei share ≤55% (diversifying); (b) upgrade to 优选级/领先级 昇腾整机伙伴 |

Bonus market-structure check (non-scoring): next operator AI-server central tender award
(cadence suggests H2 2026 [S717]) — 湘江鲲鹏 share ≥15% supports the bull re-tiering
story; ≤8.77% or absence supports the bear allocation-loss story.

## 6. Demand on the orchestrator

Per SCORING_RUBRIC ("Red-team concessions change scores only with a written response in
REDTEAM_RESPONSES.md") and the mission brief (orchestrator must respond to every score
challenge before Gate G3): C1 (W1), C2 (W2), C3 (W3), C4 (W6) each require an
accept/reject with reasoning; C5 requires the aggravator acknowledgment on W4; C6
requires an explicit tiebreak re-run. Silence on any of C1–C6 fails the gate.
