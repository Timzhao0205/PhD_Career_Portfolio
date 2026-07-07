Educational benchmark for a paper-trading learning exercise. Simulated allocations, not investment advice or recommendations.

# REDTEAM_600498 — 烽火通信 FiberHome (SSE 600498)

Red-team brief: attack, do not balance. Scored row under attack (initial, rank 5 of 14):
W1=5, W2=1, W3=2, W4=1, W5=2, W6=3, total 2.30. Inputs: V_600498.md, F_600498.md,
VAL_600498.md, SCORES.csv, SCORING_NOTES.md, 01_MISSION/SCORING_RUBRIC.md, A12
(05_STATE/ASSUMPTIONS.md), 00_PRIOR_CORPUS/RB_01+RB_02. New sources this session:
[S732]–[S738], ledgered in 90_BIBLIOGRAPHY/frags/rt_600498.json (all zh-language fetches,
accessed 2026-07-07). Headline: **six of six cells disputed; the W2 "floor" convention fails
its own A12 mechanics (a 5.7% floor maps to no unique band), the sleeve carrying a 184.52x
ttm P/E has a documented arms-length price of ¥2.0bn from Dec-2023 [S732], and the fully
consolidated NCI line says the sleeve earns ≈zero. Corrected row totals 1.20 (rank ~13).**

---

## 1. Strongest bear case (5 bullets)

- **B1 — 184.52x trailing earnings on a P&L that is still deteriorating in every period
  fetched.** FY2025: revenue −12.72% (second consecutive decline), attributable net profit
  −37.98% to ¥435.8M, net margin 1.75%; Q1-2026: NP −30.44% YoY, net margin 0.85% even as
  revenue recovered +11.40% — the growing mix dilutes margin [F_600498 §1/§6; VAL_600498].
  Balance sheet moves the same direction: net debt −¥5,207.64M widening three straight years,
  short-term borrowings +36.43% to ¥6,930M, ¥804M inventory write-down flagged as the FY2025
  key audit matter, receivables ¥14,811M ≈ 59% of revenue with a ¥2,482M bad-debt provision
  [F_600498 §2.4; V_600498]. The single strength (OCF +¥4,773M) coexists with all of it.
- **B2 — The sleeve carrying the premium is unsized by design, and the one consolidated trace
  where its profit MUST appear is negative.** No standalone 长江计算 revenue/NP exists in any
  of ~30 sources fetched across three sessions [V_600498 exposure §; F_600498 §5]; an investor
  question on the official IR platform asking exactly that (Q1-2024 revenue/NP) shows no
  company reply [S738]; the FY2025 annual-report summary never names 长江计算 in any fetched
  rendering [V_600498, S239/S240/S248]. Meanwhile 长江计算 is 29.28782% outside-held, so
  29.29% of its net income must flow to the NCI line — and FY2025 NCI allocation was a LOSS of
  −¥59.79M (FY2023 −¥16.58M, FY2024 only +¥7.49M) [F_600498 §1]. F's own caveat (NCI not
  attributable to 长江计算 specifically) noted; but no fetched fact is consistent with a large,
  profitable server subsidiary, and every fetched fact is consistent with breakeven-or-loss
  integrator economics — RB_02 read #1: integrators get "highest revenue certainty, thinnest
  margins (Huawei keeps chip+software value)". Its own municipal sponsor grades it in 产值
  (gross output), not profit: "冲刺百亿目标" [S737] — the scale-KPI signature of a strategic
  cost center (task tension d).
- **B3 — In every fetched award table 长江计算 is an allocation-taker ranked 3rd–5th, and on
  the Ascend side it is certified two bands below its rivals.** 中移动 2023–24 试验网 AI
  training: 昆仑技术 40.96%, 华鲲振宇 30.08%, 烽火通信 20.48% (3rd) [S735]; 中移动 2024–25
  智算中心 ¥191.04亿/8,054台: 长江计算 12.28% — FIFTH behind 昆仑 21.05%, 华鲲振宇 17.54%,
  宝德 15.79%, 百信 14.04% [S735]; 中移动 2025–26 推理型: one of SIX names splitting ~¥34亿
  of CANN packages [S736]; 中国电信 2026–27: one of FIVE ARM-A winners at 20% [S733; S243].
  Certification: 长江计算 = 昇腾优选级 [S246] vs 华鲲振宇/昆仑技术 = 昇腾战略级 [S734 + V_600839
  §B context] — the two 战略级 houses out-rank it in every tender above, and 华鲲振宇 alone
  booked ¥12.64bn revenue in 2024 [S259 via V_600839]. The "top-3 Ascend integrator" frame in
  circulation is tier-4-only [S242] and is contradicted by this fetched arithmetic.
- **B4 — The verified 2026 backlog is Kunpeng CPU boxes, not Ascend AI.** China Telecom
  >¥1.6bn = 鲲鹏处理器-based ARM-A general-purpose servers [S243]; China Mobile >¥1.9bn = ARM
  PC-server packages [S249] — reverse-auction 集采 categories split 5+ ways on price [S733].
  The Ascend-specific fetched backlog is a shared, per-vendor-undisclosed slice of ~¥34亿
  (6 vendors) [S736]. Yet the ¥100.5bn intraday market-cap print (2026-06-16) rode an investor
  question about Huawei's own Atlas 950 SuperPoD answered with a product-launch sentence — no
  order, no yuan figure [S244; S673]. The narrative is AI; the order book is commodity ARM.
- **B5 — The only arms-length price on record for 长江计算 is ¥2.0bn — set Dec-2023 at 5.1x
  book, with 烽火 declining to buy more.** The board-approved round: pre-money ¥1,500.6M
  (valuation base 2023-06-30) against 2022 audited net assets of ¥296.4M; ¥500M new money from
  11 subscribers (国开系, 越秀系, 广州国资, 武汉系, 光大金控) → post-money ≈¥2,000.6M;
  cross-check 94.27% × 150,060/200,060 = 70.71%, matching the announced 70.71218% [S732].
  烽火's own holding vehicle WAIVED its priority subscription right rather than fund the round
  [S732; S235]. At round terms the 70.71218% stake = ¥1,414.7M = **1.8% of today's ¥77.32bn
  market cap** [VAL_600498, S671]. And 70.71218% is the PROPOSED post-transaction figure from a
  拟-stage board resolution — no tier ≤B source since Dec-2023 confirms completion at those
  exact terms; post-2023 corroboration of the % is tier-4 only [S242].

---

## 2. Score audit — every cell, supported or corrected

Weights: W1 .20, W2 .20, W3 .15, W4 .20, W5 .15, W6 .10. Current total 2.30 (arithmetic
verified: 1.00+0.20+0.30+0.20+0.30+0.30).

| Cell | Current | Supported by cited file? | Red-team proposal | Delta |
|---|---|---|---|---|
| W1 | 5 | **PARTLY** — anchor text met via IR reply, but stake % is proposal-grade/stale and the filings themselves are silent | **4** | −0.20 |
| W2 | 1 | **NO** — V's own verdict is NOT-ESTIMABLE; the 5.7% "floor" maps to no unique band under A12's own mechanics | **0** | −0.20 |
| W3 | 2 | **WEAK** — margin prong of anchor-1 is met on its face; only OCF holds it up | **1** | −0.15 |
| W4 | 1 | **CONTESTED** — priced narrative (AI ramp size) has no tier ≤B carrier; same fork as 688629 W4 | **0** | −0.20 |
| W5 | 2 | **NO** — the +1 bump credits a shrinking carrier franchise that is not the chain layer; the group's chain-optics live in sibling 002281 | **1** | −0.15 |
| W6 | 3 | **NO** — both anchor-1 conditions present; "state-parent stability" offset is extra-rubric | **1** | −0.20 |

Corrected row: W1=4, W2=0, W3=1, W4=0, W5=1, W6=1 → **total 1.20** (falls from rank 5 to
~rank 13, between 301018 1.55 and 000628 0.75).

**Sensitivity (single concessions):** W2 1→0 alone → 2.10 (drops behind 002371 2.15, rank
5→6). W6 3→1 alone → 2.10. W1 alone → 2.10. W4 alone → 2.10. W3 or W5 alone → 2.15 (ties
002371; W1 tiebreak keeps 600498 5th). Keystone pair W2+W6 → 1.90 (ties 688981; W1 tiebreak
→ rank 8). 600498 is below the 3.0 portfolio bar either way; what is at stake is (a) the
rank-5 slot in the user's answer key and (b) Phase-4 integrator-layer slot competition
against 002261/301236/000034 under the max-2-per-layer rule.

### W1 = 5 → propose 4

Rubric 5-anchor ("own filing / official IR reply names the business") is met on its face: the
chairman's 2026-06-16 reply names 鲲鹏昇腾生态整机合作伙伴 [S244] and the 2023 board resolution
establishes control [S235/S236/S241]. Three defects keep this below archetype-A: (1) **the
actual filings are silent** — the FY2025 AR summary contains zero 长江计算/昇腾 mentions in
every fetched rendering [V_600498], and the one 问董秘 reply fetched for contrast (2025-09-10)
declined to name either [S245]; V itself concedes the evidence "does not literally clear '≥2
fetched tier-1-hosted sources'" and is mirrors-only both halves. (2) **The load-bearing
70.71218% is proposal-grade and 31 months stale**: it is the 拟-stage post-transaction figure
from公告 2023-048; no fetched tier ≤B source confirms completion/registration at those exact
terms, and post-2023 corroboration of the % is tier-4 [S242] — the chairman's "控股子公司"
confirms control, not the number [S244]. New this session: no 2024–2026 增资/IPO-辅导 event was
found in zh-search (documented, [S732] note), so no dilution is EVIDENCED — but absence-of-
confirmation ≠ confirmation. (3) The Ascend-specific half rests on one briefing sentence plus
a certification the subsidiary's own site dates only approximately [S246]. Precedent: 301236
kept W1=5 with a "weakest A in the set" caveat; if the orchestrator holds 5 here, the written
response must (a) affirm the 301236 parallel explicitly and (b) adopt the stake-currency caveat
(70.71218% = announced terms, unconfirmed completion) into SCORING_NOTES. Otherwise 4.

### W2 = 1 → propose 0 — THE KEYSTONE CELL

The scoring note reads: "NOT-ESTIMABLE precisely, but tier-1 segment floor exists (数据网络产品
5.70%, likely understated) → '<10%' floor-based (global note 2)." Five attacks:

1. **The mission's own P1 verdict is NOT-ESTIMABLE.** V_600498: "quoting a single %, or even
   the naive 5.70% 数据网络产品 floor, as 'the' Ascend exposure would misrepresent the state of
   disclosure. NOT-ESTIMABLE is the honest answer." Rubric anchor: NOT-ESTIMABLE = 0. Rubric
   header: "A cell that cannot be supported scores 0, not a guess."
2. **A floor cannot map to the "<10%" band — only a ceiling can.** A12 permits "filing-grade
   BOUNDS... mapped to the matching band." For 300308 the 9.42% domestic-revenue CEILING
   genuinely bounds Ascend share from above, so "<10%" follows. A 5.70% FLOOR is consistent
   with 5.7%, 15%, or 25% exposure — it selects no band. Mapping a floor to the lowest band it
   touches is not a bound-based score; it is the guess the rubric header forbids.
3. **It is not even a floor of the scored quantity.** No source establishes that ANY
   长江计算/Ascend revenue books inside 数据网络产品 — V's own §3 flags that 长江计算 likely
   books "substantially inside the much larger 通信系统设备 segment." New tier-2 evidence makes
   containment arithmetically impossible: 长江计算 产值 ¥75亿 in 2024 [S737] vs the segment's
   FY2024 ¥11.44亿 [F_600498 §5] — 6.6x too big. Segment forensics agree: 数据网络产品 FY2025
   (¥14.20亿) is still BELOW FY2023 (¥15.77亿) — a line allegedly housing a
   7.5x-in-three-years subsidiary shrank over the window — and its 39–44% gross margin is
   component/software-class, incompatible with integrator economics (301236 hardware segment GM
   4.82%; 000034 whole-company GM 3.40% [SCORING_NOTES]).
4. **The same new evidence spans TWO bands, which is the definition of not-estimable.** If
   产值 ≈ revenue, exposure ≈ 75/285.49 = 26.3% of FY2024 consolidated revenue → band 3
   (10–30%). If 产值 is a municipal gross-output metric (likely; the source never says 营收
   [S737]), the GAAP share is unknown. Under A12's own mechanics there is no "matching band" —
   the mechanism outputs nothing → 0. Note the perversity of the current cell: the retained
   bound (5.7% segment, tier-3-carried) is LOWER-tier than the excluded one (产值, tier-2
   government portal). Also a citation-discipline defect: the note calls 5.70% a "tier-1
   segment floor" — the segment figures are carried by S531/S239/S240 (all tier 3); nothing
   tier-1-hosted parsed for this ticker (8 documented failures, V_600498).
5. **Consistency across the 14 names.** 002371's 93.34% exposed-base: "NOT Huawei-specific and
   is not credited" → 0. 688981's China-region 85.6%: "context, not Huawei-specific" → 0.
   600839 → 0. For 600498, a number whose relationship to the thesis quantity is UNKNOWN was
   credited as a band selector. One standard; pick it; apply it to all 14.

Propose **W2=0**. If the orchestrator instead admits the tier-2 产值 datum as bound-eligible,
the honest outputs are still 0 (bands 1 and 3 both live; no unique band) — writing 3 would
require treating 产值 as GAAP-revenue-equivalent, which NUMBER-TRUTH discipline forbids.

### W3 = 2 → propose 1

Anchor 1 is disjunctive: "deteriorating margins OR persistent cash burn." The margin prong is
met on its face: attributable net margin 2.46% → 1.75% → 0.85% (FY2024 → FY2025 → Q1-2026,
monotone) with NP −37.98% then −30.44% [F_600498 §1/§6]; quality-of-earnings deteriorates in
parallel (¥804M inventory write-down as THE key audit matter; ¥2,482M AR provision; NCI loss
absorption −¥59.79M) [V_600498; F_600498 §1]; net debt widened every year (−1,741.51 →
−4,935.53 → −5,207.64M) and short-term borrowings +36.43% [F_600498 §2.4]. The sole
anchor-3-or-better element is OCF (+¥4,638M/+¥4,773M, > capex both years). The current 2 rests
entirely on letting OCF strength overrule the margin prong; peers with falling margins AND
negative OCF took 1 (301236, 000034), and 000628 took 2 with GM RISING and OCF positive —
600498's margins are falling, so it belongs below 000628's profile, i.e. at 1, not level with
it at 2. If the orchestrator retains 2, the written response must state that the disjunctive
margin prong was subordinated to OCF and why the Q1-2026 0.85% net margin does not tip it.

### W4 = 1 → propose 0

Global note 3 splits 1 vs 0 by the evidence tier "on" which the PFP price rests. The question
(same fork the 688629 red team posed): tier of the LINK, or tier of the PRICED NARRATIVE? What
the multiple prices, per VAL_600498's own words, is "长江计算's verified-but-unsized
Ascend/Kunpeng ramp to swamp a legacy telecom-equipment business whose consolidated profit is
still shrinking." The ramp's SIZE has no tier ≤B carrier anywhere (W2 audit above); the scale
narrative ("top-3", first-batch CM384) is tier-4 [S242] and contradicted by fetched award
tables (5th at 12.28% in the ¥191.04亿 tender [S735]); the tier-A material is qualitative
partnership language [S244]. The tier ≤B growth evidence that DOES exist (>¥1.6bn + >¥1.9bn
2026 wins [S243; S249]) is Kunpeng general-purpose ARM — the wrong product line for the AI
premium, and low-margin 集采 at that [S733]. Add the one market price of the crown jewel:
¥2.0bn post-money Dec-2023, stake = 1.8% of today's cap [S732; VAL] — "perfection" is
literal. Names whose priced narrative was tier-C took 0 (002281, 002916, 002156, 301018).
Propose 0. Minimum alternative: hold 1, but the written response must state the "link-tier
governs W4" rule explicitly and confirm it was applied identically to 688629's W4 challenge.

### W5 = 2 → propose 1

The chain layer 600498 occupies is server integration — the rubric's own anchor-1 example
("commoditized integration/distribution margin-squeeze layer"), and RB_02 read #1 names the
mechanism ("Huawei keeps chip+software value"). Now quantified: 5–7 vendors per award, shares
reallocated tender-by-tender, reverse-auction pricing [S733; S735; S736]. The +1 bump in
SCORING_NOTES ("a genuine optical/DWDM component franchise") fails three ways: (1) RB_02 read
#2's technical-barrier optics layer means AI-datacenter optical MODULES — in this group that
franchise sits in SIBLING listco 002281 光迅科技 (same 中国信科集团 parent [V_002281
background]), not in 600498, whose own optical lines are carrier transmission systems and
fiber-cable; (2) those lines are the SHRINKING part — 通信系统设备 −16.40% at 18.81% GM,
光纤及线缆 −0.95% at 25.17% GM [F_600498 §5] — a moat that loses 16% of revenue and 65bp of GM
in one year is not defending anything; (3) peer consistency: 002261 (integrator + software
overlay) took 1; 301236 took 2 for an overlay that is >50% of revenue and ecosystem-coupled;
600498's "overlay" is a declining legacy business unrelated to the chain. The one genuinely
high-margin line (数据网络产品, 39.28% GM) is 5.70% of revenue and below its FY2023 level.
W5=1.

### W6 = 3 → propose 1

Rubric: 3 = "one material concentration OR verticalization exposure"; 1 = both. 600498 has
both, and the note's own text lists both before inventing an offset:

1. **Material concentration — realized, not just structural.** Carrier customers dominate
   (通信系统设备 74.86% of revenue); FY2025's −12.72% was DRIVEN by operator capex rotating
   away, per the company's own AR-summary industry language [V_600498, S237/S238]. The top-5
   figure (≈35.77%) is color-grade and F could not verify it in any year (MISSING, F_600498
   §3) — an unverifiable concentration measure argues for conservatism, not credit. The thesis
   sleeve adds supplier-side single-dependence: 100% of its CPUs/NPUs are Huawei-allocated.
2. **Verticalization exposure — live.** Huawei kept its own Atlas machine business (RB_01) and
   pulled HBM in-house within one generation (RB_02 read #3, the rubric's named precedent);
   it re-grades integrators annually on a certification ladder where 长江计算 sits at 优选级,
   below 战略级 华鲲振宇/昆仑技术 [S246; S734]; award tables show reallocation costs Huawei
   nothing [S735].
3. **"Offset by state-parent stability" is not a rubric anchor.** No W6 anchor credits
   ownership identity; the same state parent did not lift 002281's or any other name's W6.
   Strike it or defend it in writing.

Comparator: 002156 took W6=2 for one 52.29% customer + policy common-mode. 600498 carries a
realized customer concentration, a single-ecosystem supplier dependence on the thesis sleeve,
AND an annual re-certification lever in the customer/supplier's hands. Anchor reading: both
conditions → **1**. Concede 2 only with a written finding that carrier concentration is
non-material — against the fact that it just cut revenue 12.72%.

---

## 3. Verticalization test

If Huawei internalizes more of the integrator layer — or simply re-weights it — 600498's
thesis has no contractual or technical floor, because the layer is an allocation Huawei
constructs: Huawei co-built 长江计算's assembly line [S247], sole-sources its Kunpeng/Ascend
silicon, sets its partner grade (优选级, third band, vs 战略级 for 华鲲振宇/昆仑技术 [S246;
S734]), and competes above it with its own Atlas/SuperPoD machines — the very product the
2026-06-16 investor question was about [S244; RB_01]. The in-house-HBM precedent (RB_02 read
#3) demonstrates appetite for absorbing layers HARDER than rack integration; server assembly
is the chain's lowest-barrier layer by the rubric's own anchor. What protects the slot is
politics, not economics: 中国信科 state parentage, Wuhan/Hubei sponsorship (the municipality
literally publishes its 产值 targets [S737; S247]), and carrier 集采 rules that require
multiple domestic suppliers [S733]. But political allocation protects the slot's EXISTENCE,
not its size or margin — the award tables already show 长江计算 taking 12–22% behind the two
战略级 houses in every fetched round [S735; S736], and the 5.1x-book ¥2.0bn Dec-2023 round
[S732] plus the negative FY2025 NCI allocation [F_600498 §1] suggest the slot earns ≈nothing
today. Note also the structural awkwardness the current scores ignore: 烽火/中国信科 compete
head-on with Huawei for the same carrier optical-transmission capex (red-team inference from
the segment facts) — a rival's listed subsidiary is an odd candidate for privileged Ascend
allocation when purely-aligned vehicles (华鲲振宇, 昆仑技术) exist one tier up. In an
internalization or re-tiering scenario the listco loses an unsized, possibly-unprofitable
revenue stream; the STOCK loses the ~86% of its ¥77.32bn cap that the disclosed P&L cannot
support (illustration: FY2025 attributable NP ¥435.8M × even 25x ≈ ¥10.9bn ≈ 14% of cap
[F_600498; VAL_600498]).

## 4. Common-mode test

The cleanest common-mode demonstration in the universe is a single procurement document:
中移动's 2024–25 智算中心 award table contains 长江计算 (600498, 12.28%), 神州鲲泰 (000034,
10.53%), and 湘江鲲鹏 (002261, 8.77%) as co-winners [S735], and the 2025–26 CANN inference
packages add 软通计算机 (301236) to the same sheet [S736]. Ranks 3, 4, 5, 7 of the current
answer key are lines in one buyer's award table, upstream of one chip allocator. A Huawei
demand shock (production interruption, NVIDIA re-admission reducing Ascend urgency, an
AI-capex digestion pause) or a 信创 pause hits 002261, 301236, 000034, 600498 in the same
direction and season, with 688629 (rank 1) as the most concentrated expression of the same
factor and 688981/002371 second-order — the same cluster the 688629 red team flagged; 600498's
inclusion is now documented at award-table grade. On a carrier-capex CUT, 600498 is uniquely
double-exposed among the four: the same three carriers fund BOTH its legacy optical systems
(74.86% of revenue, −16.40% FY2025 when they rotated 网→算 [F_600498 §5; V_600498]) AND its
server sleeve's tenders [S733; S735; S736] — rotation already cost it ¥36.6亿 of segment
revenue in one year while the compute side won back unsized slices at integrator margins; an
absolute cut removes both legs simultaneously, and drags 002281 (carrier optical, same group)
with it. For Phase 4: under the max-2-per-layer rule 600498 competes with 002261/301236/000034
for integrator slots; any two of the four is one trade on one allocator's calendar, and 600498
is the copy with the worst disclosed P&L trajectory of the four [F_600498 §1].

## 5. Five falsifiable checks

| # | Observable event | Window | Bear if | Bull if |
|---|---|---|---|---|
| C1 | H1-2026 半年报: first standalone 长江计算 line in 主要控股参股公司分析 (the section P1 identified as the likely disclosure location), + sign of the NCI allocation, + 数据网络产品 segment YoY | by 2026-08-31 (statutory) | Still no standalone disclosure AND NCI allocation negative again — the unsized-and-unprofitable reading survives its best chance to die | Standalone 长江计算 revenue ≥¥3bn for H1 with positive net profit — kills B2 and forces W2 re-scoring on filing-grade data (this is the check [S738]'s unanswered IR question baselines) |
| C2 | Stake currency: any 公告 confirming completion/registration of the 2023 增资 at 70.71218%, a NEW 长江计算 capital round, or 分拆/上市辅导 filing | now → 2026-12-31 | New dilutive round with 烽火 again waiving rights, or stake reported <70% — proposal-grade % was stale, W1 caveat vindicated | IPO/辅导 process launched — forces standalone audited financials and re-marks the stake far above the Dec-2023 ¥2.0bn [S732] |
| C3 | Next carrier AI-TRAINING 集采 award table (中移动 2026–27 智算 or 中国电信 AI算力服务器 round; H2-2026 expected on the 2024/2025 cadence — snippet-grade calendar), or any tier ≤B disclosed SuperPoD/超节点 order with a yuan figure | now → 2027-03-31 | 长江计算 share <15% or absent while 战略级 华鲲振宇/昆仑 lead again — allocation-taker pattern [S735] holds | Top-2 position or >25% share in a ≥¥5bn CANN training package, or a named SuperPoD order ≥¥1bn — the Nov-2025 launch [S244] converts to revenue |
| C4 | Huawei partner re-certification: does 长江计算 announce 昇腾领先级 or 战略级 (its own site announced 优选级 ~2025-01 [S246]; 昆仑's 战略级 dates 2024-02 [S734]) | now → 2027-03-31 | Still 优选级 into a third year — Huawei's own grade keeps it second-class on the Ascend side | Upgrade announced on yctco.com.cn/Huawei channels — Huawei-graded Ascend scale crossed the higher gate; weakens B3 |
| C5 | Q3-2026 report: attributable NP YoY and short-term-borrowings level | 三季报 by 2026-10-31 | NP still negative YoY (third consecutive down year forming) or ST borrowings >¥7.5bn — the 184.52x multiple loses its E a third time | NP +≥30% YoY with GM mix improvement — first P&L evidence the ramp outruns the legacy decline |

---

## New sources fetched this session (zh-language, logged in frags/rt_600498.json)

- **[S732]** 上海证券报 mirror of 公告 2023-048 (same URL as ledgered [S235]), 2023-12-07, tier 3,
  re-fetched for the related-party-transaction financials P1 did not extract — 长江计算 2022
  audited net assets ¥296.4M; pre-money ¥1,500.6M (base 2023-06-30); price 4.2966元 per 1元
  registered capital; 11 subscribers; both incumbent holders waived priority rights; 拟-stage.
- **[S733]** 新浪科技, 2026-06-24, tier 3, fetched — China Telecom 2026–27 tender: ~¥11.5bn,
  40,000 units; ARM-A 28,000 units to 5 winners incl. 长江计算; C86 ~¥3.3bn to 中兴/新华三/浪潮;
  Kunpeng ecosystem ~¥8.161bn = 70.7%.
- **[S734]** 河南昆仑技术官网, 2024-02-23, tier 2, fetched — 昆仑技术 昇腾战略级 + 鲲鹏领先级
  dual certification; comparative anchor against 长江计算's 昇腾优选级 [S246]. Tier ladder
  thresholds (战略/领先/优选 ≥¥20亿/10亿/5亿) are search-snippet color only, non-load-bearing.
- **[S735]** 澎湃新闻, 2024-05-17, tier 3, fetched — 中移动 2024–25 智算中心 ¥191.04亿/8,054台
  award shares (长江计算 12.28%, 5th) and 2023–24 试验网 shares (烽火通信 20.48%, 3rd); the
  common-mode award table containing 000034/002261-linked entities.
- **[S736]** 新浪科技, 2026-01-12, tier 3, fetched — 中移动 2025–26 推理型: 类CUDA packages
  >¥17亿 vs CANN packages ~¥34亿 split among 6 incl. 长江计算 and 软通计算机; per-vendor amounts
  undisclosed (the circulating ¥5.97亿/22.22% figures remain snippet-grade, not used).
- **[S737]** 武汉市投资促进局, 2025-02-24, tier 2, fetched — 长江计算 产值 ¥1bn (2021) → ¥7.5bn
  (2024), ¥10bn 2025 target; wording is 产值 throughout, never 营收; the scale-mismatch datum
  behind the W2 attack.
- **[S738]** 全景路演 IR platform question page, undated (question references Q1-2024), tier 3,
  fetched — direct investor request for 长江计算 standalone revenue/NP shows no company reply
  ("暂无回复信息"); documents the disclosure void; non-load-bearing for any figure.
- Documented non-results (no S-IDs): vzkoo sell-side report 403; cnr.cn 央广网 9M-2024
  "营收超40亿" article 404 (that figure therefore remains snippet-grade and is NOT used);
  kjj.wuhan.gov.cn 404.

## Bottom line for the orchestrator (written response required per rubric before G3)

Eight challenges: six cell disputes (W1 5→4, W2 1→0 [keystone], W3 2→1, W4 1→0, W5 2→1,
W6 3→1; corrected total 1.20) plus two discipline defects — (i) SCORING_NOTES calls the W2
basis a "tier-1 segment floor" when the carrying sources are tier-3 and no tier-1 host parsed
for this ticker; (ii) W6's "offset by state-parent stability" cites no rubric anchor — strike
or justify. Minimum bar for keeping the current row: answer the floor-vs-ceiling logic in W2
(a floor cannot select the "<10%" band; the new tier-2 产值 datum puts band 3 in play, so
either both bounds count or neither does), reconcile W4's tier test with the identical fork in
REDTEAM_688629, and adopt the stake-currency caveat (70.71218% = 拟-stage terms, completion
unconfirmed at tier ≤B) in writing even if W1=5 is retained.
