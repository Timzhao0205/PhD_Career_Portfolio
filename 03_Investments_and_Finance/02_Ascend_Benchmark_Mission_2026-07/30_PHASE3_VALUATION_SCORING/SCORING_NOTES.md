Educational benchmark for a paper-trading learning exercise. Simulated allocations, not investment advice or recommendations.

# SCORING_NOTES — cell-by-cell justification for SCORES.csv (initial, pre-red-team)

Scored 2026-07-07 by the orchestrator per 01_MISSION/SCORING_RUBRIC.md. Weights: W1 .20,
W2 .20, W3 .15, W4 .20, W5 .15, W6 .10. Every cell cites the file(s) in SCORES.csv
`cell_sources`; this file explains the anchor mapping. Valuation inputs are as-of
2026-07-07 market close (see VALUATION.csv `price_asof`).

## Global anchor interpretations (applied uniformly, logged before red team)

1. **Verified-false links (W1).** The rubric anchors stop at "0 = UNVERIFIED". Two names
   (000628, 600839) have tier-A evidence that the claimed link does NOT exist. A
   verified-false link scores W1=0 for the claimed channel — the information is
   stronger than UNVERIFIED but the link value is identical (zero). 600839 gets W1=1,
   not 0, because a SEPARATE generic-Huawei ICT-distribution business (长虹佳华, ~37% of
   revenue) is verified at filing grade while being explicitly non-Ascend (company
   denies Ascend AI-server work, 2026-05-13).
2. **W2 on bounded-but-unpointed estimates.** Anchor "0 = NOT-ESTIMABLE" is applied when
   no filing-grade bound exists. Where a filing-grade BOUND exists, the bound is used:
   300308 → ceiling 9.42% (domestic revenue, falling) → "<10%" → 1; 600498 → tier-1
   segment floor 5.7% (likely understated) → 1. This is documented judgment, not anchor
   text; flagged for red-team review.
3. **W4 composite.** 13/14 names are PRICED-FOR-PERFECTION (see VALUATION.csv). Anchor:
   PFP on tier ≤B evidence → 1; PFP on tier-C evidence → 0; 000628 is PFP on a
   *debunked* link → 0. NEUTRAL → 3 (600839 only).
4. **Intermediate integers.** The rubric allows integers 0–5; anchors define 5/3/1/0.
   Values 2 and 4 are used as documented interpolations where evidence sits between
   anchors (each instance justified below).
5. **Tie-breaking.** Rubric: W1, then W4. 002261 vs 301236 (both 2.35) tie on W1=5,
   W4=1; extended tiebreak (documented here, not in the rubric): next-highest-weight
   dimension W2 (tie, 3=3), then W3 (2 vs 1) → 002261 ranks 3rd. 002281 vs 002916
   (both 1.80) are IDENTICAL on every dimension — ranks 10/11 are assigned by ticker
   order and carry no information; treat as a tie for any Spearman computation
   (midrank 10.5).
6. **Scale note.** In the July-2026 pricing regime the market prices the whole chain
   for perfection; totals are compressed and only one name clears 3.0. That is a
   finding about the market, not a defect of the rubric.

## Per-name cell notes

### 688629 华丰科技 — total 3.30, rank 1
- W1=4: own official reply "公司是华为高速背板连接器核心供应商之一" (2024-03-21, repeated
  2026), own reply scopes product to data-center servers/switches [V_688629]. The literal
  昇腾 brand word never appears in any company statement → between anchor A(5) and B(3).
- W2=5: top-1 customer = 60.52% of FY2025 revenue in own filing, corroborated as Huawei
  three independent ways; revenue +131.5% FY2025 → ">30% and growing" [V_688629,
  F_688629]. Caveat: this is ALL-Huawei products (incl. legacy telecom), Ascend-specific
  sub-split undisclosed.
- W3=3: revenue +131.5%, GM 31.44% (up), NM 14.19% (up) BUT operating cash flow negative
  two consecutive years (−3.09M, −2.49M — profit not converting to cash; receivables
  build) and net cash swung negative (−108.32M) [F_688629] → "mixed".
- W4=1: PRICED-FOR-PERFECTION (P/E ttm 216.20x, P/S ttm 33.89x) on tier ≤B evidence
  [VAL_688629].
- W5=5: high-speed backplane connectors = rubric's named technical-barrier layer with
  content-per-system growth in supernode architectures [RB_02 read #2; V_688629].
- W6=1: 60.52% single-customer concentration AND second-sourcing/internalization
  exposure (in-house-HBM precedent shows Huawei's appetite; 西部证券 names two competing
  connector suppliers) [V_688629, S204]. Not scored 0 because connector internalization
  by Huawei has no direct precedent.

### 300308 中际旭创 — total 2.60, rank 2
- W1=3: tier B — iFinD/media screen lists it in the Ascend chain [S011]; own filings/IR
  never name Huawei/Ascend [V_300308].
- W2=1: Ascend-linked revenue bounded 0–9.42% by the domestic-revenue ceiling (falling
  from 13.19%) [V_300308] → "<10%".
- W3=5: revenue +60.25%, GM 42.04% rising, NM 28.24% rising, OCF 10,896M, net cash
  +9,391M — every anchor criterion met [F_300308].
- W4=1: PFP (P/E ttm 83.70x, P/S 24.50x) on tier-B evidence [VAL_300308].
- W5=5: optical modules, global leader, 1.6T edge — rubric's named layer [RB_02;
  V_300308].
- W6=1: top-5 = 75.98%, #1 = 24.06%, US DoD 1260H listing (2026-06-08) targets the
  overseas base that sets the price, and co-packaged-optics is a real
  verticalization-analog threat [V_300308(S213), F_300308].

### 002261 拓维信息 — total 2.35, rank 3 (tiebreak note: see global note 5)
- W1=5: own annual report names the full-stack Huawei partnership (鲲鹏/昇腾/海思/大模型/
  开源鸿蒙 verbatim) [V_002261].
- W2=3: 智能计算 hardware segment 21.7% (H1-2025) to 50.4% (FY2024) of revenue — inside
  10–30% band at latest reading, not clearly growing as a share [V_002261].
- W3=2: revenue −22.79% FY2025; margins volatile; OCF positive; net cash positive; ttm
  core (ex-non-recurring) profit is a LOSS [F_002261, VAL_002261] → weak-mixed.
- W4=1: PFP (headline P/E ttm 606.30x resting on one-off items) on tier-A evidence
  [VAL_002261].
- W5=1: server integrator — commoditized integration margin per rubric anchor [RB_02
  read #1; V_002261].
- W6=1: supplier concentration 81.01% top-5 with Huawei entities 73.5% combined (FY2024),
  customer top-5 72.75% (FY2024), plus a 2026-05-08 regulator warning letter on
  disclosure violations [V_002261(S150,S153)].

### 301236 软通动力 — total 2.35, rank 4
- W1=5: convergent official evidence — own prospectus named Huawei at 53–56% of revenue
  (2018-2020), own 互动易/董秘 replies confirm 鲲鹏/昇腾双优选 partner + 一体机 line,
  Huawei's own Connect-2025 partner list [V_301236]. Caveat: all tier-1 PDFs unparseable
  this mission; evidence is via mirrors/relays (flagged in V file; weakest A in the set).
- W2=3: 19–45% bounded range (hardware segment 45.05% ceiling bundles non-Huawei laptop
  ODM; ~19% lower anchor) [V_301236].
- W3=1: GM fell 19.26→12.46→11.20%, NM 0.59%, OCF swung negative (−242M), net cash
  swung negative, goodwill load from acquisition [F_301236] → deteriorating margins +
  cash burn.
- W4=1: PFP (P/E ttm 718.91x on a fragile +54M ttm residual; P/S 1.07x) on tier-A
  evidence [VAL_301236].
- W5=2: mix now dominated by hardware integration at 4.82% segment GM with an ISV/
  services overlay — between "commoditized integration" (1) and "defensible but
  competitive" (3) [F_301236, RB_02 read #1].
- W6=1: quasi-single-ecosystem dependence (services + hardware + HarmonyOS all
  Huawei-coupled), #1 customer 25.42%, partner-retiering risk [V_301236, F_301236].

### 600498 烽火通信 — total 2.30, rank 5
- W1=5: own board announcement (70.71218% consolidated control of 长江计算) + chairman's
  official briefing reply naming 鲲鹏昇腾整机伙伴 + Nov-2025 SuperPoD launch [V_600498].
- W2=1: NOT-ESTIMABLE precisely, but tier-1 segment floor exists (数据网络产品 5.70%,
  likely understated) [V_600498] → "<10%" floor-based (global note 2).
- W3=2: revenue −12.72% (second consecutive decline), NP −37.98%, thin NM 1.75%; OCF
  strong (+4,773M) but net debt −5.2bn [F_600498] → weak-mixed.
- W4=1: PFP (P/E ttm 184.52x requires the unsized 长江计算 ramp to swamp a shrinking
  legacy business) on tier-A evidence [VAL_600498].
- W5=2: server assembly economics (integrator, anchor 1) plus a genuine optical/DWDM
  component franchise → 2 [V_600498, RB_02].
- W6=3: structural carrier concentration + Huawei-ecosystem common-mode, offset by
  state-parent stability; one-material-concentration profile [V_600498, F_600498].

### 002371 北方华创 — total 2.15, rank 6
- W1=3: tier B for the second-order claim — own filings name "AI算力芯片" as capex driver
  but never SMIC/Huawei; named sell-side + media substantiate the capex-flow logic
  [V_002371].
- W2=0: Huawei/Ascend-specific share NOT-ESTIMABLE (company declined to quantify even
  先进制程 share; exposed-base 93.34% is NOT Huawei-specific and is not credited)
  [V_002371].
- W3=3: revenue +30.85% but NM fell 18.84→14.03% (margin compression), OCF positive,
  net cash shrank to +2,493M; contract liabilities signal backlog [F_002371] → mixed.
- W4=1: PFP (P/E ttm 104.95x after a flat-profit year) on tier-B evidence [VAL_002371].
- W5=4: domestic etch/depo quasi-oligopoly = high technical barrier, but equipment is
  cycle-exposed and not a per-system content layer → between 3 and 5 [V_002371, RB_02].
- W6=3: few-fab customer base (top-5 39.02%), extreme policy common-mode (also the
  tailwind), no verticalization threat [V_002371, F_002371].

### 000034 神州数码 — total 2.00, rank 7
- W1=5: own annual report names 神州鲲泰 Kunpeng+Ascend product matrix [V_000034].
- W2=1: 5.18% of FY2025 revenue (own-brand segment ceiling) [V_000034].
- W3=1: GM 3.40% falling, NM 0.36% falling, OCF −2,426M FY2025, net debt −13.5bn
  [F_000034] → deteriorating margins + cash burn.
- W4=1: PFP (P/E ttm 49.9x on sub-0.4% margins and declining profit) on tier-A evidence
  [VAL_000034].
- W5=1: distribution/integration — commoditized margin layer [RB_02 read #1; V_000034].
- W6=3: diversified customers but supplier-side Huawei dependence + 信创 policy
  common-mode; top-5 customers 43.04% moderate [V_000034, F_000034].

### 688981 中芯国际 — total 1.90, rank 8
- W1=3: tier B — TrendForce ×3 + SemiAnalysis name SMIC for 910C (7nm) and 950PR (N+3);
  own filings never mention Huawei/Ascend across 5 tier-1 documents [V_688981].
- W2=0: NOT-ESTIMABLE — anonymized customers, no named-analyst % estimate found; China
  region 85.6% is context, not Huawei-specific [V_688981].
- W3=2: revenue +16.49%, GM stable ~21.6%, but capex (59,951M) ≈ 3x OCF (20,081M), net
  debt doubled to −44,961M [F_688981] → structurally cash-consuming.
- W4=1: PFP (P/E ttm 246.73x on 7.49% net margin; ~128% A/H premium) on tier-B evidence
  [VAL_688981].
- W5=4: foundry = chain bottleneck with the highest technical barrier, but
  capital-devouring, yield-constrained economics → between 3 and 5 [V_688981, RB_02].
- W6=2: extreme policy common-mode (both the tailwind and the threat), FT-reported
  Huawei-dedicated fabs = internalization-analog, customer concentration undisclosed
  [V_688981].

### 600839 四川长虹 — total 1.80, rank 9
- W1=1: claimed 华鲲振宇 channel tier-A debunked (0% direct; ~0.97% look-through; company
  denies Ascend OEM). Separate generic-Huawei ICT distribution verified at filing grade
  but explicitly non-Ascend [V_600839 + correction note] → 1 per global note 1.
- W2=0: Ascend-specific NOT-ESTIMABLE; claimed channel = 0% [V_600839].
- W3=3: revenue +4.94% slow, GM 9.42% drifting down, NM 0.91% thin (FY2025 NP +40.56%
  on corrected base), OCF positive, net cash +7,813M [F_600839] → mixed.
- W4=3: NEUTRAL — no Ascend premium visible at P/E ttm 40.63x, P/S 0.28x [VAL_600839].
- W5=1: appliance conglomerate + ICT distribution — commoditized layers [V_600839].
- W6=4: diversified conglomerate, low chain common-mode; minority leakage (50-62% of
  consolidated profit) is an attribution issue, not concentration risk [F_600839].

### 002281 光迅科技 — total 1.80, rank 10 (identical vector to 002916; see global note 5)
- W1=1: tier C — the one direct 互动易 question on Ascend-ecosystem status got a
  non-answer; no tier ≤B source names an Ascend link [V_002281].
- W2=0: NOT-ESTIMABLE (anonymized customers; segment not Huawei-specific) [V_002281].
- W3=4: revenue +44.20%, GM stable 23.43%, NM ~7.9% (drifted from 10.22% FY2023), OCF
  positive FY2025 but negative FY2024, net cash +4,047M → strong-mixed [F_002281].
- W4=0: PFP (P/E ttm 177.05x, ~4x PEG-style read) on tier-C evidence [VAL_002281].
- W5=4: optics is the rubric's named layer but Accelink is mid-pack globally with a
  large telecom-legacy mix → 4 not 5 [V_002281, RB_02].
- W6=4: diversified (top-5 48.49%, #1 15.16%), state parent, two end-markets
  [V_002281, F_002281].

### 002916 深南电路 — total 1.80, rank 11 (identical vector to 002281)
- W1=1: tier C — current filings/replies anonymize customers; AI-server PCB share
  self-described "low" (2023) with no update; all Huawei/Ascend attribution is tier-4
  [V_002916].
- W2=0: NOT-ESTIMABLE — #1 customer 7.46% is a ceiling, identity undisclosed [V_002916].
- W3=4: revenue +32.05%, GM 28.32% rising, NM 13.85% rising, OCF +3,838M, small net debt
  −2,511M → strong-mixed [F_002916].
- W4=0: PFP (P/E ttm 77.23x pricing a durable AI mix-shift) on tier-C evidence
  [VAL_002916].
- W5=4: PCB competitive; IC-substrate technical barrier; domestic leader → 4 [RB_02;
  V_002916].
- W6=4: most diversified concentration in the set (top-5 18.42%); 36% international
  adds US-cycle exposure [V_002916, F_002916].

### 002156 通富微电 — total 1.60, rank 12
- W1=1: tier C — zero Huawei/Ascend mentions in 7 primary filings; management non-denial;
  claims trace to self-media only [V_002156].
- W2=0: NOT-ESTIMABLE [V_002156].
- W3=4: revenue +16.92%, GM 14.59% stable, NM 4.36% rising, OCF +6,966M > capex 6,211M,
  but net debt −13.4bn → strong-mixed [F_002156].
- W4=0: PFP (P/E ttm 71.55x with sell-side re-rating on the AI-packaging narrative) on
  tier-C evidence [VAL_002156].
- W5=4: advanced packaging is the rubric's named layer, but OSAT competitive intensity
  and thin historical margins argue below-anchor → 4 [RB_02; V_002156].
- W6=2: 52.29% single customer (attributed AMD) + US-policy common-mode on that
  customer's China business [V_002156].

### 301018 申菱环境 — total 1.55, rank 13
- W1=1: tier C — "H公司" continuity signal is inferential; company declines to confirm;
  Ascend-specific claims are uncited forum posts [V_301018].
- W2=0: NOT-ESTIMABLE (three compounding undisclosed layers) [V_301018].
- W3=3: revenue +39.55%, GM 23.99% (below FY2023), NM 5.15% up, OCF thin +325M vs capex
  375M, small net debt; Q1-2026 NP −47.71% [F_301018] → mixed.
- W4=0: PFP (P/E ttm 231.45x with ttm earnings already contracting) on tier-C evidence
  [VAL_301018].
- W5=4: liquid cooling = content-growth component layer (near-mandatory at 450W/card)
  but a competitive field [RB_02; V_301018].
- W6=3: #1 customer 14.30% ceiling, segments diversified, but the thesis-relevant
  business concentrates in one unconfirmed customer + AI-capex cyclicality [V_301018].

### 000628 高新发展 — total 0.75, rank 14
- W1=0: tier-A debunk — own announcements + two IR replies confirm 0% stake in 华鲲振宇;
  FY2025/H1-2025 filings contain zero Huawei/Ascend/算力 mentions [V_000628].
- W2=0: exposure = 0% by arithmetic [V_000628].
- W3=2: revenue −30.13% (two consecutive declines); GM rising 12.02%; OCF turned
  positive +227M; net debt −1,051M [F_000628] → weak-mixed.
- W4=0: PFP (P/E ttm 156.81x on a ~108M ttm profit, with limit-up days explicitly tagged
  to the debunked narrative) on a verified-false link [VAL_000628].
- W5=1: construction + nascent power-semi — outside the chain's technical layers
  [V_000628, F_000628].
- W6=3: no chain common-mode (the "risk" here is thesis-absence, priced in W1/W2);
  construction cyclicality; concentration undisclosed [V_000628, F_000628].


---

## SUPERSEDE NOTICE (2026-07-07, post-red-team)

The cell values and ranking in the notes ABOVE are the INITIAL (pre-red-team) scores,
retained for audit trail. Six red-team reviews (REDTEAM_*.md) challenged 40 items; every
challenge is adjudicated in REDTEAM_RESPONSES.md, which also states the uniform W2/W4/W6
rulings (R0.1-R0.3), the conceded citation-discipline corrections (R0.4: [S700] adopted
for 688629-W3; 'quasi-oligopoly' and 'contract liabilities signal backlog' struck for
002371; 'tier-1 segment floor' mislabel struck for 600498), and the final post-rescore
board. SCORES.csv now carries the FINAL scores (rank 1..14, zero names >= 3.0). The
non-re-red-teamed risers (600839, 000034, 688981) are disclosed in R0.5 and in the
answer key's uncertainty section.
