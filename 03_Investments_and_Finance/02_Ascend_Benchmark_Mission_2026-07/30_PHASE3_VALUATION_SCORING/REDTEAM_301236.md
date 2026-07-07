Educational benchmark for a paper-trading learning exercise. Simulated allocations, not investment advice or recommendations.

# REDTEAM_301236 — 软通动力 iSoftStone (SZSE-ChiNext 301236) — adversarial review

Role: red-team-critic. Mandate: attack, not balance. Date: 2026-07-07 (Beijing).
Inputs: V_301236.md, F_301236.md, VAL_301236.md, SCORES.csv row (W1=5 W2=3 W3=1 W4=1
W5=2 W6=1, total 2.35, rank 4/14), SCORING_NOTES.md, SCORING_RUBRIC.md, RB_02,
REDTEAM_002261.md (for its [S717]/[S721] tender and partner-grade evidence, reused
cross-file). New sources this session: [S724]–[S731], ledgered in
90_BIBLIOGRAPHY/frags/rt_301236.json (all fetched 2026-07-07, Chinese-language). One
additional fetch (donews.com mirror) returned an unrelated article and was discarded,
not ledgered. Per SCORING_RUBRIC rules, no score changes without a written orchestrator
response in REDTEAM_RESPONSES.md — challenges C1–C6 below each require one.

## 0. New evidence fetched this session (what it changes)

1. **The core-earnings quarterly split VAL_301236 could not obtain now exists [S724]:**
   Q1-2026 扣非归母净利润 = **-3.60亿** (prior-year quarter **-2.16亿**, loss widened
   66.62%). VAL_301236 wrote "a 'core TTM P/E' cannot be built without inventing a
   number — not attempted." It can now be built without inventing anything:
   core (ex-non-recurring) TTM = FY2025 扣非 41.93M [S303] + Q1-2026 扣非 (-360.0M)
   − Q1-2025 扣非 (-216.0M) = **-102.07M — a trailing core LOSS.** The +54.11M headline
   TTM residual under the 718.91x P/E is non-recurring items all the way down.
2. **Q1-2026 cash mechanics [S724, S726, S727]:** OCF **-34.42亿** in one quarter
   (prior-year Q1 -18.37亿; -87.37% YoY) — versus FY2025 full-year OCF of only -2.42亿
   [F_301236]. Inventory 期末 98.07亿 (+27.19% vs 期初 77.10亿; "+超50亿元" YoY [S726]).
   Short-term borrowings +超20亿 vs end-2025 [S726]. 财务费用 +46.62% YoY, quarterly
   interest >6000万 [S724;S726]. First inventory writedowns booked: 资产减值损失
   5,799.07万, "全部为存货跌价损失及合同履约成本减值损失", plus 信用减值 732.67万 [S727].
   And while the company attributes the loss to "转型期投入增加" [S724], its R&D expense
   FELL -9.03% YoY in the same quarter [S724] — the "investment" is inventory and opex,
   not R&D.
3. **The 定增 completed — and was consumed within a quarter [S725, S730]:** 82,248,103
   new shares at 40.71元 (SZSE approval 2025-11-12; CSRC registration path Dec-2025;
   completion announced 2026-02-04), gross 33.48亿 / net 33.13亿, 6-month lockup.
   Share-count reconciliation: pre-issue ≈952.94M shares (from [S728]'s "1% = 952.94万股")
   + 82.25M = 1,035,189,280 = exactly the f84 count VAL used [S664] — VAL's market cap is
   correct and already includes the placement. But: net proceeds 33.13亿 < Q1-2026
   operating cash outflow 34.42亿 [S730;S724] — the entire equity raise funded roughly
   one quarter of working capital. Placement price 40.71 vs 37.58 close = allottees
   **-7.69% underwater** [S730;S663]; dilution +8.63% of pre-issue share count.
4. **Proceeds double down on the 4.82%-GM layer [S725]:** the four 募投项目 are 京津冀
   软通信创智造基地 (13.81亿), AIPC智能制造基地 (11.75亿), 怀来智算中心一期 (6.63亿),
   计算机生产车间智能升级 (1.6亿) — i.e., ~33.8亿 of new capacity for exactly the
   hardware-manufacturing segment whose gross margin has fallen every reported period
   (5.33% FY2024 → 4.96% 9M-2025 → 4.82% FY2025 [S304;S303]).
5. **Governance/flow signal [S728]:** second-largest shareholder CEL Bravo Limited
   (8.69%) filed a 1%/~3亿 selldown on 2025-05-05 — **two days before** the 定增预案
   (2025-05-07), reason "自身资金安排". Same article: 同方计算机 was already loss-making
   pre-acquisition (2022 -9,934万; H1-2023 -6,346万), and FY2024 largest customer =
   25.38% of sales (unnamed) — consistent with V_301236's FY2025 25.42% [S296], still
   never re-confirmed as Huawei.
6. **The only QUANTIFIED current-period Huawei-silicon revenue found anywhere is
   ~1.3-1.4% of revenue [S729;S300]:** 软通计算机's named wins are the 中国移动
   人工智能通用计算设备(推理型) tranche at **4.27亿** [S729] and a 千万级 矿鸿 retrofit
   tender [S300] — ≈4.3-4.8亿 against FY2025 revenue 350.90亿 ≈ **1.3%**. By contrast,
   软通 is ABSENT from the seven winners of 中国移动's 191.04亿 训练型 智算中心 tender
   (昆仑技术 21.05%, 华鲲振宇 17.54%, 宝德 15.79%, 百信 14.04%, 长江计算 12.28%,
   神州鲲泰 10.53%, 湘江鲲鹏 8.77% — [S717], REDTEAM_002261). Everything between 1.3%
   and the 45.05% segment ceiling is inference.
7. **Even the bull consensus prices no relief [S731]:** 7 covering institutions,
   FY2026E revenue 421.08亿 (+20.0%), EPS +50.57% → implied FY2026E 归母 NP ≈ 206.11M ×
   1.5057 ≈ 310.3M → forward P/E = 38,902.41 ÷ 310.34 ≈ **125.4x on the BULL case**. And
   that case requires Q2-Q4 2026 profit of ≈310.3 + 350.0 = 660.3M vs Q2-Q4 2025's
   404.1M (206.11 + 198.00) = **+63% YoY in the profitable quarters**, right after a
   quarter in which the core loss widened 66.62% [S724].

## 1. Strongest bear case (5 bullets)

- **B1. The trailing business loses money; the 718.91x P/E is an accounting residual.**
  Core (扣非) trajectory: 2022 +8.38亿 → FY2025 +4,193万 (-95% over three years [S726]),
  with 79.6% of FY2025's headline 206.11M profit non-recurring (subsidies, fair-value
  gains) [S303]. Computable core TTM = 41.93 − 360.0 + 216.0 = **-102.07M, a loss**
  [S303;S724]. On FY2025 core profit the multiple is 38,902.41 ÷ 41.93 = **927.8x**; on
  core TTM it is negative/not-meaningful. The +54.11M headline TTM residual [VAL_301236]
  dies on ANY of: one more Q1-like quarter, a few-million rounding swing in the "约"
  quarterly figures (VAL's own fragility caveat), or one goodwill impairment — the
  208.08M 同方 goodwill on the balance sheet [S512;F_301236] is **3.85x** the entire
  ttm residual and 4.96x FY2025 core profit.
- **B2. The hardware pivot is a cash furnace with rising leverage.** Q1-2026 OCF
  -34.42亿 in 13 weeks — 14x the FY2025 full-year outflow (-2.42亿) and larger than the
  entire 33.13亿 net 定增 raised weeks earlier [S724;S730;F_301236]. Inventory 98.07亿 =
  62% of a full year of hardware-segment revenue (158.09亿 [S295]), +超50亿 YoY [S726],
  with the first 存货跌价/合同履约成本 writedowns (5,799.07万) already booked [S727].
  Short-term borrowings +超20亿 in the quarter; 财务费用 +46.62%; net cash was already
  negative (-437.30M) at FY2025-end [S726;S724;S512]. This is a services company
  levering up its balance sheet to carry a low-margin manufacturing working-capital
  cycle it did not previously have.
- **B3. Both legs of the business sit in margin-squeeze layers, and both are still
  compressing.** Services (54.02% of revenue): IT outsourcing that named financial
  media assess as "技术壁垒并不高", GM 21.97% (2022) → 16.5% (2025) under customer
  bargaining power and wage costs [S726] — with Huawei's demonstrated buyer leverage on
  exactly this line (framework-agreement repricing 2H2023 [S304]; ~2,050万 in fines/fee
  withholding 2020 [S308]). Hardware (45.05%): contract-manufacturing integration at
  4.82% GM, falling every period (5.33 → 4.96 → 4.82 [S304;S303]), acquired from a
  seller for whom it was loss-making (-9,934万 in 2022 [S728]). Consolidated GM:
  19.26% → 12.46% → 11.20% [F_301236]. R&D: intensity 2.58% and absolute spend down
  three straight years, then -9.03% YoY in Q1-2026 [F_301236;S724]. No layer here has
  pricing power; the "Huawei ecosystem partner" framing packages a wage-squeezed
  outsourcer stapled to a sub-5%-GM assembler.
- **B4. In the Ascend allocation game it is a mid-tier, marginal player — and the
  verified exposure floor is ~1.3%, not 19%.** Quantified current Huawei-silicon
  revenue in the whole record: 4.27亿 推理型 tender + 千万级 矿鸿 ≈ 1.3% of FY2025
  revenue [S729;S300]. It is absent from the 191.04亿 训练型 tender's seven winners
  [S717, REDTEAM_002261]. Its Huawei-countersigned grade, 鲲鹏/昇腾"双优选" [S301], is
  the MIDDLE of the three grades in this mission's evidence set (领先级 > 优选级 >
  认证级 — 000034 holds 双领先级, 600498 holds 鲲鹏领先/昇腾优选 [V_000034;V_600498 via
  REDTEAM_002261 compilation]). The 19-45% exposure band in V_301236 rests on (floor) a
  2022 PRE-acquisition revenue-mix ratio extrapolated three years forward — V's own text:
  "UNVERIFIED assumption... bounding exercise only" — and (ceiling) a segment that
  bundles the non-Huawei x86 gaming-laptop ODM 机械革命 [S299;S306]. Post-IPO, no filing
  names Huawei as a customer at all; the 25.42%/25.38% top-customer line [S296;S728] is
  identity-unconfirmed by explicit mission rule A8.
- **B5. Flow and dilution: insiders and anchor investors are on the other side.** The
  #2 holder filed a ~3亿 selldown two days before the dilutive 33.48亿 raise was
  unveiled [S728]; the raise added 8.63% to the share count at 40.71 [S730]; the stock
  closed 2026-07-07 at 37.58 [S663], leaving the 15 allottees -7.69% underwater with
  their 6-month lockup expiring ≈late-Aug-2026 [S730]; and the proceeds are committed to
  expanding the lowest-margin layer (信创/AIPC/智算中心 capacity [S725]) whose demand is
  policy-scheduled, not contractual. Meanwhile ZERO of the company's own filed PDFs were
  directly parseable this mission (10/10 failures, V_301236) — every load-bearing number
  in this name's entire file chain is a mirror/relay. A 719x-headline-P/E,
  negative-core-earnings, negative-OCF stock where the direct documentary base is
  unverifiable and the informed money is selling is a fragile long by construction.

## 2. Score audit — every cell, supported or not

| Cell | Current | Supported by files? | Red-team proposal | Challenge |
|---|---|---|---|---|
| W1 | 5 | No — anchor requires own-filing-grade evidence; 0/10 tier-1 parses, all relay; SCORING_NOTES itself: "weakest A in the set" | **4** (aggressive 3) | C1 |
| W2 | 3 | No — the ≥10% floor is a twice-disclaimed extrapolation; only quantified Huawei-silicon floor is ~1.3% | **1** (aggressive 0) | C2 |
| W3 | 1 | Yes — and new Q1-2026 data pushes it toward the 0 boundary; keep 1 only with written reasoning | 1, keep (confirm 0 considered) | C3 |
| W4 | 1 | Yes (anchor floor for tier ≤B PFP) — but core-TTM-negative aggravator must enter the record | 1, keep | C4 (no score change) |
| W5 | 2 | No — both legs sit at the rubric's anchor-1 layers; the +1 "ISV overlay" has zero disclosed revenue | **1** | C5 |
| W6 | 1 | Yes on the anchor text; undercounted aggravators to log | 1, keep | C6 (log + tiebreak) |
| Total | 2.35 (rank 4) | — | **1.20 aggressive / 1.60 primary / 2.00 minimum-concession** | — |

Arithmetic: primary = 4(.20)+1(.20)+1(.15)+1(.20)+1(.15)+1(.10) = 0.80+0.20+0.15+0.20+
0.15+0.10 = **1.60** (ties 002156 at rank ~12 on current totals). Minimum-concession
(only C1→4 and C5→1 land) = 0.80+0.60+0.15+0.20+0.15+0.10 = **2.00** (ties 000034, ~rank
7). Aggressive (C1→3, C2→0, C5→1) = 0.60+0.00+0.15+0.20+0.15+0.10 = **1.20** (~rank 13).
Under every branch, 301236 exits the top-4.

### C1 — W1: 5 → 4 (aggressive 3): relay-only "tier A" cannot earn the direct-filing premium

The rubric's 5-anchor is "tier A (own filing / official IR reply names the business)".
Undisputed: the LINK exists — prospectus-era Huawei revenue percentages [S302;S308],
互动易 product confirmations [S300;S306], FY2025-AR partner language [S301;S303], the
HC2025 一体机 partner list [S012], Huawei's own site [S298]. But W1 measures evidence
STRENGTH, and four defects cap this cell below 5:

1. **Zero direct tier-1 parses — unique among the W1=5 names.** V_301236's own gate
   check: "0 directly-fetched tier-1 PDFs (documented trail of 10 failed attempts)."
   V_301236 itself notes 000034 and 002261 "successfully fetched several of their own
   abstracts/IR records"; 600498's W1 cites a directly-fetched board announcement
   [SCORING_NOTES]. 301236 is the only 5 built entirely on mirrors. Per SOURCE_STANDARDS'
   mirror rule every fetched source in this name's ledger is tier 2/3 — nothing in the
   record is tier-1-as-fetched. Convergent relay mitigates fabrication risk; it does not
   equal direct verification of what the filings say.
2. **The Ascend-specific evidence is 100% relayed; the only direct-from-Huawei fetch
   covers the wrong layer.** [S298] (tier 2, fetched from devicepartner.huawei.com)
   confirms 软通动力 as a "HarmonyOS Connect 鸿蒙智联" partner — the consumer-IoT
   solutions program (智能家居/运动健康/…), tangential to the Ascend/一体机 thesis. The
   thesis-relevant official items — HC2025 一体机 list [S012], "双优选" grade [S301] —
   reach this mission only through 科创板日报/财联社 relays (tier 3 as fetched).
3. **The quantified own-filing numbers are stale and pre-thesis.** The prospectus's
   53.38%/55.45%/55.53%/49.7% Huawei shares are 2018-1H2021 — services outsourcing,
   pre-Ascend-commercial, pre-acquisition [S302;S308]. The CURRENT-period customer
   identity is explicitly unconfirmed (A8; [S296;S728]). So the "own filing names the
   business" element is true of a 2021 document describing a different business mix.
4. **Orchestrator's own precedent binds.** 688629 was interpolated to W1=4 for a LESSER
   defect (brand word 昇腾 absent from company statements, with own-filing fetches
   otherwise succeeding) [SCORING_NOTES]. "All ten own-PDF fetches failed; every citation
   is a relay; current customer identity unconfirmed" is a strictly larger evidence gap
   than "one brand word missing."

**Proposed W1=4.** Aggressive variant 3 if the orchestrator weighs the mirror rule
strictly (all Ascend-specific evidence tier-3-as-fetched = the B anchor's own
definition, "major media"). If 5 is kept, the written response must state why
relay-only convergence outranks the direct-fetch standard applied to 688629, and why
SCORING_NOTES' own "weakest A in the set" caveat has no cell consequence.

### C2 — W2: 3 → 1 (aggressive 0): the ≥10% floor does not exist at filing grade

The 3 rests on V_301236's "19-45%" band [SCORING_NOTES]. Decompose it:

1. **The 19% floor is a non-figure.** It applies the FY2022 PRE-acquisition revenue mix
   of 同方计算机 vs 同方国际 (42.5/57.5 [S299]) to the FY2025 segment. V_301236's own
   labels: "rough extrapolation, explicitly flagged as assumption-dependent, NOT a
   disclosed figure... an UNVERIFIED assumption... Presented as a bounding exercise
   only," and — verbatim — "a clean Ascend/Kunpeng-only point figure is **NOT-ESTIMABLE**
   from disclosed FY2025 data." Global note 2 permits scoring on "filing-grade BOUNDs";
   a three-year-stale mix ratio from a relayed sell-side report is not filing-grade by
   any reading.
2. **The 45.05% ceiling is not Huawei-specific.** It bundles 机械革命/智通国际, an
   x86/Intel-AMD consumer-laptop ODM with "NO Huawei linkage found in any source"
   [V_301236;S299;S306] — and 智通国际 was the LARGER of the two acquired revenue bases
   in FY2022 (54.6亿 vs 40.3亿 [S299]). Mission precedent: 002371's 93.34% exposed base
   was NOT credited precisely because it was not Huawei-specific → W2=0
   [SCORING_NOTES]. Crediting 301236's non-specific segment ceiling while refusing
   002371's non-specific base is inconsistent.
3. **What IS pinned at filing-adjacent grade:** named, dated, quantified Huawei-silicon
   revenue = 4.27亿 推理型 tender [S729] + 千万级 矿鸿 [S300] ≈ **1.3-1.4% of FY2025
   revenue**. The alternative route to ≥10% — "largest customer 25.42% is still Huawei"
   — is barred by the mission's own A8 rule and never company-confirmed post-IPO
   [S296;S728;V_301236].
4. **Band spanning ≠ band membership.** [1.3%, 45.05%] spans the rubric's 0/1/3/5 bands.
   Assigning the middle band is a coin-flip midpoint, not an evidence-based placement.
   Where bounds pinned a band, the orchestrator scored the band (300308: ceiling 9.42%
   → 1; 600498: floor 5.7% → 1). The only pinned band here is "<10%".

**Proposed W2=1** (quantified floor ~1.3%, confirmed product lines, ceiling
non-specific). Aggressive 0 if the orchestrator holds that no Huawei-specific bound
exists at all (V's own NOT-ESTIMABLE sentence). If 3 is kept, the written response must
name the filing-grade fact that places exposure ≥10% without using (a) the disclaimed
2022-mix extrapolation or (b) the A8-barred customer-identity equation.

### C3 — W3: 1 supported; written confirmation that 0 was considered

No score change demanded — but the cell note must absorb the new Q1-2026 facts, which
move this name toward the 0 ("distress signs") boundary: OCF -34.42亿 in one quarter
(-87.37% YoY) vs -2.42亿 for ALL of FY2025 [S724;F_301236]; inventory 98.07亿, +27.19%
in a quarter, 62% of a year's hardware revenue [S724;S295]; first inventory/contract-cost
writedowns 5,799.07万 [S727]; short-term borrowings +超20亿 in the quarter and interest
expense +46.62% [S726;S724]; net placement proceeds (33.13亿 [S730]) < one quarter's
operating outflow; R&D cut -9.03% while losses widen [S724]. The counterweights that
keep it at 1 rather than 0 — completed 33.48亿 raise, +15.79% revenue growth, headline
FY2025 profit — are real [S730;S724], so 1 is defensible. The written response should
say exactly that, and should note the F_301236 net-cash figure (-437.30M, FY2025-end) is
now stale in BOTH directions (raise +33.13亿 in Feb; Q1 outflow -34.42亿 + new ST debt
+20亿 by Mar-31).

### C4 — W4: 1 supported (anchor floor); aggravators must enter the record (no score change)

PFP on tier ≤B evidence → 1 fits the anchor, and stays 1 even if C1 lands (tier-B floor).
But the record must log: (i) **the core TTM P/E denominator is now computable and
NEGATIVE** (-102.07M [S303;S724]) — VAL's open item closes on the bear side; "719x" is
generous framing for a business whose trailing core result is a loss; (ii) FY2025
ex-non-recurring P/E = 927.8x; (iii) even the 7-house bull consensus implies ~125x
forward earnings and requires +63% YoY profit in Q2-Q4 2026 [S731; arithmetic in §0.7];
(iv) the one balance-sheet item (goodwill 208.08M) equals 3.85x the ttm profit base —
a single impairment event flips the headline metric from "extreme" to "meaningless"
[S512;VAL_301236]. W4=1 is the floor only because the rubric has no lower rung for
tier ≤B PFP; the response should acknowledge this name sits at the bottom of the rung.

### C5 — W5: 2 → 1: there is no layer here above the rubric's anchor-1 economics

The 2 was justified as "between commoditized integration (1) and defensible-but-
competitive (3)" on the strength of an "ISV/services overlay" [SCORING_NOTES]. Attack:

1. **The services leg is itself a rubric-anchor-1 layer.** It is IT outsourcing — named
   media verbatim: "该业务本质为IT外包……技术壁垒并不高" — with GM compressed 21.97% →
   16.5% in three years by customer bargaining power and wage/material costs [S726], by
   the company's own regulatory reply compressed every single period since 2022
   (21.25→19.25→17.37→16.61 [S304]), including a unilateral Huawei repricing (2H2023)
   and Huawei fines (2020) [S304;S308]. "Margin-squeeze layer" is the anchor-1 text.
2. **The hardware leg is the anchor-1 exemplar:** whole-machine integration at 4.82% GM
   and falling [S303;S304], competing against ≥7 interchangeable Kunpeng/Ascend OEMs for
   Huawei-granted allocation ([S717], REDTEAM_002261), with the mid-grade 双优选
   certificate [S301].
3. **The "+1 overlay" has no revenue.** HarmonyOS/开源鸿蒙 work is R&D-stage ("推动开源
   鸿蒙PC…研发" [S729]); no fetched source discloses ANY 鸿蒙-attributable revenue; the
   one quantified win is a 千万级 tender [S300] ≈ 0.03% of revenue. An overlay that
   monetizes at rounding-error scale cannot lift a layer score.
4. **Intra-mission consistency.** 002261 — 70.0% software/exam-services revenue at
   materially higher claimed segment GMs plus its own 鸿蒙 line — scored W5=1
   [REDTEAM_002261 §0.1; SCORING_NOTES]. 301236, with LESS software mix (54.02%), LOWER
   software GM (16.5% [S726]), and MORE hardware-integration mix (45.05% at 4.82%),
   scored 2. Same layers, worse mix, higher score — unexplained.
5. R&D behavior confirms no moat-building: intensity 2.58%, absolute spend down three
   consecutive years, -9.03% YoY in Q1-2026 [F_301236;S724].

**Proposed W5=1.** If 2 is kept, the written response must identify the specific
defensible franchise (with a revenue number) that distinguishes 301236's overlay from
002261's, and reconcile the two cells.

### C6 — W6: 1 supported; log undercounted aggravators + re-run the tiebreak

W6=1 fits the anchor (material concentration + verticalization exposure) and is
consistent with 688629 keeping 1 at 60.52% single-customer. No score change demanded.
But the cell note undercounts, and the record must add: (a) the dependence is
TRIPLE-channel — services customer, silicon/allocation supplier, and HarmonyOS ecosystem
— so a single Huawei decision moves all three P&L lines at once [V_301236]; (b) Huawei
has TWICE demonstrated unilateral economics-setting against this specific company
(2H2023 repricing; 2020 fines/fee withholding [S304;S308]); (c) supplier top-5
concentration jumped 26.20% → 56.89% with the hardware pivot [S296] — allocation
dependence now sits on the cost side too; (d) the x86 机械革命 leg adds Intel/AMD supply
and consumer-cycle exposure without hedging any Huawei risk [S299;S306]; (e) flow risk:
15 allottees, -7.69% underwater, lockup expiring ≈2026-08-26 [S730;S663].

**Tiebreak/rank dependency (procedural):** 301236 and 002261 tie at 2.35; rank 3 vs 4
was decided by extended-tiebreak W3 (002261's 2 vs 301236's 1) [SCORING_NOTES note 5].
REDTEAM_002261's C3 attacks that very cell (2→1). If it lands and 301236 is otherwise
unchanged, the documented sequence (W1, W4, W2, W3) exhausts tied and passes to W5 —
where 301236's 2 vs 002261's 1 would FLIP rank 3 to 301236; but if this file's C5 lands
(W5 2→1), the vectors are identical and the pair becomes a formal midrank tie. The
orchestrator must re-run the tiebreak explicitly under whichever cells survive both
red teams, and say so in writing — rank 3/4 as published is path-dependent on two
disputed cells.

## 3. Verticalization test (what if Huawei internalizes / re-tiers the layer)

Every layer 软通动力 occupies is one Huawei decision away from repricing, and Huawei has
exercised each lever at least once. Precedents: in-house HBM shows Huawei absorbing a
supply layer when strategic [RB_02 read #3]; the 2021 divestiture-then-dominance of
超聚变 shows it restructuring the whole-machine layer itself — the ex-Huawei unit now
takes the largest share (21.05%) of the very operator tender class 软通计算机 is absent
from [S721;S717, REDTEAM_002261]. On hardware: Ascend/Kunpeng allocation among 7+
interchangeable OEMs is Huawei's zero-cost dial; 软通计算机 holds the middle 双优选
grade (below 领先级 peers 000034/600498 [V_000034;V_600498 via REDTEAM_002261]), won
only a 4.27亿 推理型 tranche [S729], and its 一体机 SKU shares the HC2025 stage with a
crowd (恒生电子, 新致软件, 金山办公, 深信服, 科大讯飞 et al. [S012;V_301236 DISCOVERY])
— re-tiering two grades of partners upward zeroes 软通's allocation before any 领先级
name feels it. On channel: Huawei can serve the same 大模型 inference demand through
华为云昇腾云服务 instead of partner appliances — 软通 is itself a "华为云全球合作伙伴"
[S301], meaning the channel conflict runs THROUGH its own partner stack; every 一体机
sale a customer defers into Huawei's cloud is 软通 hardware revenue Huawei captures
directly. On services: the 2H2023 framework repricing and 2020 fines [S304;S308] are
documented proof Huawei resets this vendor's service economics unilaterally when its own
margins tighten. On HarmonyOS: the ecosystem owner sets monetization terms; 软通's
开源鸿蒙 work is R&D-stage with zero disclosed revenue [S729]. If Huawei internalizes or
re-tiers, the sequence is mechanical: allocation shifts to 领先级/自有 channels → the
45.05%-of-revenue hardware segment (4.82% GM) deflates while its 98.07亿 inventory
[S724] and the new 33.8亿 of 定增-funded 信创/AIPC capacity [S725] become stranded →
存货跌价 provisions scale up from Q1-2026's 5,799万 [S727] → the 208.08M goodwill fails
its test [S512] → headline ttm profit (+54.11M) flips negative on the first charge. The
thesis does not survive Huawei optimizing its own P&L.

## 4. Common-mode test (what falls with it)

- **Huawei demand/allocation shock:** 301236 falls together with 688629 (60.52%
  single-customer), 002261 (61.29% Huawei procurement), 600498 and 000034 (Kunpeng/
  Ascend OEM allocation) [SCORING_NOTES;REDTEAM_002261]. That is ranks 1, 3, 4, 5, 7 —
  the scoreboard's top half is one correlated Huawei order book; among top names only
  300308 (overseas optics cycle) is orthogonal. 301236 is the widest single conduit:
  customer, supplier-allocation, and ecosystem exposure simultaneously (§2-C6).
- **信创-budget pause:** hits 301236 twice — the existing 信创/domestic-silicon hardware
  line AND the freshly committed 13.81亿 京津冀信创智造基地 + 11.75亿 AIPC base [S725],
  i.e., new capacity built against policy-scheduled demand. Falls with 000034, 002261,
  600498; second-order 002371/688981 (policy common-mode per their W6 notes).
- **Operator AI-capex pause:** its named hardware wins are 中国移动/中国联通 tenders
  [S729]; the same operators anchor 600498, 000034, 002261 ([S717]) — one carrier
  capex decision correlates four universe names.
- **Margin (not just volume) common-mode:** a Huawei-ecosystem downturn transmits to
  301236 through REPRICING before volumes move — precedent 2H2023 [S304] — so
  "revenue holds, margin collapses" scenarios hit it even when headline demand looks
  intact. Any name whose Huawei relationship is service-priced (002261's supplier terms,
  688629's part pricing) shares this channel.
- **Policy reversal (export-control relaxation / Nvidia re-entry):** the substitution
  mandate IS the hardware demand [RB_02 read #4]; 301236's inference-appliance and
  信创-PC lines are substitution products, and the 怀来智算中心 capex [S725] competes
  directly with re-admitted foreign stacks. The x86 机械革命 laptop leg is NOT a hedge —
  it is a consumer-cycle business with Intel/AMD supply exposure [S299;S306] that
  merely dilutes the Ascend story the multiple is paying for.

## 5. Five falsifiable checks (event + date + which side it supports)

| # | Observable event | Check date | Bear side if | Bull side if |
|---|---|---|---|---|
| 1 | H1-2026 业绩预告 (ChiNext trigger: loss/turnaround/±50%) then 半年报: H1 扣非归母净利润 sign and hardware-segment GM | 预告 by 2026-07-15; 中报 by 2026-08-31 | H1 扣非 loss (Q2 fails to offset Q1's -3.60亿 [S724]); hardware GM <5% for a 4th consecutive reading [S304;S303] | H1 扣非 >0 AND hardware GM ≥6% (first reversal of the 5.33→4.96→4.82 slide) |
| 2 | H1-2026 OCF, inventory level, and any new 存货跌价 provisions | 中报 by 2026-08-31 | Cumulative H1 OCF ≤ -20亿; inventory ≥100亿; new writedowns beyond Q1's 5,799万 [S724;S727] | Q2 standalone OCF >0; inventory ≤85亿; no incremental provisions |
| 3 | Goodwill: impairment indicators/charge on 软通计算机/智通国际 (carrying 208.08M [S512]) at interim; formal annual test | 中报 2026-08-31; FY2026 AR ~2027-04 | Any 商誉减值 charge (one charge ≈3.85x the +54.11M ttm residual → ttm flips negative); or ttm 归母 NP already negative on published halves | Explicit clean test WITH hardware GM recovering (removes the stranded-goodwill scenario) |
| 4 | Placement-share lockup expiry: 82.25M shares (7.95% of capital), cost 40.71 [S730], listed late-Feb-2026 | ≈2026-08-26, monitor through 2026-09-30 | Price <40.71 into unlock plus allottee 减持 filings (e.g., 苏州工业园区基金, 诺德/财通) — anchor investors exit at a loss | Price >40.71 and no exit filings by 2026-09-30 — anchors hold underwater positions voluntarily |
| 5 | Huawei Connect 2026 partner materials + HarmonyOS monetization + operator-tender cadence | HC ~2026-09 (HC2025 was 2025-09-20 [S012]); tenders H2-2026 | 软通/软通计算机 absent from 一体机/partner product list; still 优选级 while peers hold/gain 领先级; no named tender ≥5亿; still zero disclosed 鸿蒙 revenue [S729] | Upgrade to 领先级 or named HC2026 product launch with order figures; a 训练型 tender win ≥5亿; first disclosed 鸿蒙/一体机 revenue line ≥1% of revenue |

Bonus (non-scoring) consistency check: FY2026 consensus [S731] requires Q2-Q4 profit
+63% YoY (§0.7) — each quarterly report through 2027-04 tests it mechanically.

## 6. Demand on the orchestrator

Per SCORING_RUBRIC ("Red-team concessions change scores only with a written response in
REDTEAM_RESPONSES.md") and the mission brief (every score challenge answered before Gate
G3): C1 (W1 5→4/3), C2 (W2 3→1/0), C5 (W5 2→1) each require accept/reject with
reasoning; C3 requires written confirmation that W3=0 was weighed with the Q1-2026
facts; C4 requires the core-TTM-negative aggravator logged against W4; C6 requires the
undercounted W6 aggravators logged AND an explicit tiebreak re-run against 002261 under
the post-red-team cells. Silence on any of C1–C6 fails the gate.
