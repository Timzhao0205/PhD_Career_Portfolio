Educational benchmark for a paper-trading learning exercise. Simulated allocations, not investment advice or recommendations.

# REDTEAM_002371 — 北方华创 NAURA Technology Group (SZSE 002371)

Red-team brief: attack, do not balance. Scored row under attack (initial, rank 6 of 14):
W1=3, W2=0, W3=3, W4=1, W5=4, W6=3, total 2.15 (arithmetic verified). Inputs: V_002371.md,
F_002371.md, VAL_002371.md, SCORES.csv, SCORING_NOTES.md, 01_MISSION/SCORING_RUBRIC.md,
00_PRIOR_CORPUS/RB_02. New sources this session: [S740]–[S747], ledgered in
90_BIBLIOGRAPHY/frags/rt_002371.json (all zh-language fetches, accessed 2026-07-07).
Headline: **four of six cells disputed (W1, W3, W5, W6; W2 and W4 are supported). Corrected
row totals 1.55 — rank 6 falls to ~12 of 14, below 688981 (1.90), the very name whose capex
the thesis rides on. Two of the disputed cells rest on characterizations that appear in no
mission file ("quasi-oligopoly", "contract liabilities signal backlog"), and the risk cell
was scored while a mission-flagged open item (US Entity-List status) sat unresolved — closed
this session: NAURA and ten subsidiaries have been on the Entity List since 2024-12-02
[S740].**

---

## 1. Strongest bear case (5 bullets)

- **B1 — Priced for a supercycle its own P&L has not printed.** 104.95x TTM P/E and 14.11x
  TTM P/S [VAL_002371, S635/S636] sit on a FY2025 in which revenue grew +30.85% while
  attributable net profit FELL -1.77% (ex-non-recurring -4.22%); gross margin fell
  42.85%→40.10% (-2.75pp), net margin 18.84%→14.03% (-4.81pp); Q4-2025 — the year's highest
  revenue quarter (CNY 12.05bn) — earned a 3.25% net margin (CNY 0.392bn) [S175; F_002371].
  The multiple re-rated from ~81x (2026-05-20, [S186]) to ~105x (2026-07-07, [S635]) in
  seven weeks with no new earnings print in between [VAL_002371]. Even un-reverified
  consensus (+44%/+37%/+28% for 2026-28E) leaves it at ~42x in 2028 [S186; VAL_002371].
- **B2 — The "Ascend link" is a three-hop inference whose only Huawei-specific carrier is
  snippet-grade.** NAURA's own filings and two full earnings-briefing transcripts never
  contain 华为/昇腾/中芯国际; asked point-blank, the company declines to confirm SMIC as a
  customer (S178 Q24), declines to disclose advanced-process order wins (Q25), and declines
  to quantify even the broad 先进制程 share (Q40) [V_002371]. The fetched sell-side that
  earned tier B ([S182], [S185]) argues a Huawei-agnostic, industry-wide capex thesis — the
  watchlist's only Huawei-chain placement of NAURA, [S013], remains `"verified":"snippet"`
  and may not bear load. The one on-book forward-demand datum runs the wrong way: contract
  liabilities 4,291M → 4,203M, -2.06% QoQ [S176; F_002371].
- **B3 — The boom-year prints already show competitive squeeze, not oligopoly pricing.**
  FY2025 attributable-profit growth: NAURA **-1.77%** vs 拓荆科技 +34.67% (revenue +58.87%)
  [S741], 中微公司 +30.69% (revenue +36.62%; etch revenue 98.32亿, +35.12% — rough parity
  with NAURA's own >百亿 etch line [S182]) [S742], 盛美上海 +21.05% (+20.80%; guides
  82-88亿 for 2026) [S743]. All four fish the same domestic-substitution capex pool. Piotech
  at ~1/6 NAURA's revenue carries MORE contract liabilities in absolute terms (48.52亿,
  +62.66% YoY, with a disclosed ~110亿 orders-on-hand) than NAURA (42.91亿, trendless —
  FY2023/24 basis MISSING — and sequentially declining) [S745; S176; F_002371].
- **B4 — Input-side export-control exposure was scored as if absent.** NAURA and ten
  subsidiaries were added to the US Entity List on 2024-12-02 (公告编号2024-080: US
  suppliers need prior BIS licenses to ship controlled items to the company) [S740], in an
  action that also newly controlled semiconductor-manufacturing-equipment and HBM items and
  listed the whole domestic peer cohort (拓荆/芯源微/华海清科/南大光电…) [S744]; BIS's
  2025-09-29 Affiliates Rule retroactively extends listing to >50%-owned affiliates [S746].
  V_002371 explicitly flagged Entity-List status as "an open item for Phase 2"; Phase 2
  never closed it; the W6 cell enumerates risks without it. The company's
  "不会对公司业务产生实质性影响" [S740] is its own unaudited assurance about a licensing
  regime it does not control.
- **B5 — Balance-sheet direction contradicts the fortress framing that props W3.** OCF minus
  capex negative two consecutive years (-473M FY2024, -128M FY2025); net cash down -62% in
  two years (6,554M→2,493M) while interest-bearing debt rose +152% (5,898M→14,844M);
  OCF/revenue 5.4%; inventory CNY 28.6bn ≈ 443 days of FY2025 COGS; and ~CNY 1,842M of
  FY2025 R&D was capitalized (≈25% of R&D investment ≈ 33% of the year's attributable
  profit), with the 开发支出 balance growing +10.9% in Q1-2026 alone — profit quality and
  cash conversion both degrade exactly when the multiple demands acceleration [F_002371;
  S176].

---

## 2. Score audit — every cell, supported or corrected

Weights: W1 .20, W2 .20, W3 .15, W4 .20, W5 .15, W6 .10. Current total 2.15 (verified).

| Cell | Current | Supported by cited file? | Red-team proposal | Delta (total) |
|---|---|---|---|---|
| W1 | 3 | **NO** — tier B was assigned to a different claim than the rubric dimension measures; one-hop and three-hop chains scored identically | **2** (strict reading: 1) | -0.20 |
| W2 | 0 | **YES** — anchor "0 = NOT-ESTIMABLE" matches V's finding; consistent with 600839/688981/002281 practice | 0 (hold) | 0 |
| W3 | 3 | **NO** — anchor-1 text ("deteriorating margins") literally applies; cited justification contains an unsupported positive ("contract liabilities signal backlog") | **2** | -0.15 |
| W4 | 1 | **YES** — PFP on tier-B evidence per global note 3; conditional on W1 disposition (see below) | 1 (hold, conditionally) | 0 |
| W5 | 4 | **NO** — "quasi-oligopoly" appears in no mission file; zero elements of the 5-anchor present; cited RB_02 itself places NAURA outside the named layers | **3** | -0.15 |
| W6 | 3 | **NO** — scored with a mission-flagged open item unresolved (Entity List, now closed [S740]); "no verticalization threat" ignores the documented analog channels | **2** | -0.10 |

Corrected row: W1=2, W2=0, W3=2, W4=1, W5=3, W6=2 → **total 1.55** (rank 6 → ~12 of 14 on
the current board: below 002156's 1.60, tied with 301018's 1.55, tiebreak W1 2>1 puts NAURA
12th; below 688981's 1.90 — the internally consistent ordering, since NAURA's causal chain
to Ascend routes THROUGH 688981 and adds hops).

**Sensitivity (single concessions, vs current board):** W1 alone → 1.95 (rank 8, below
000034, above 688981). W3 alone → 2.00 (ties 000034, loses W1 tiebreak → rank 8). W5 alone
→ 2.00 (rank 8). W6 alone → 2.05 (rank 7). Any single concession drops NAURA out of the top
half; W1+W5 → 1.80 (ties the 1.80 trio). The orchestrator must respond to each cell in
writing before G3.

### W1 = 3 → propose 2 (strict reading: 1)

Rubric dimension: "**Evidence strength of Huawei/Ascend link**"; 3 = tier B (major media /
named sell-side). The defense will be "V assigned tier B, rubric maps tier B → 3." The
attack is that V assigned tier B **to a different claim**: "Tier B for the claim as stated
(2nd-order capex-flow thesis)" — i.e., domestic-fab-capex-flows-to-NAURA. On the rubric's
actual dimension — a Huawei/Ascend link — V's own part-(ii) finding is: "the actual
mechanism connecting Ascend/SMIC-driven demand specifically to NAURA order growth — **is
not found in any tier-1 source**", and the fetched tier-B sources substantiate the flow
without naming Huawei or Ascend anywhere in their NAURA thesis ([S182] names no customer;
[S185]'s fetched text recommends NAURA on industry-wide 制程迭代 + 国产化率 grounds)
[V_002371]. The chain the score actually needs has three hops: (1) Huawei→SMIC fabrication
— tier B, but it lives in V_688981, not in any NAURA source; (2) SMIC-is-a-NAURA-customer —
media characterization only ([S183], explicitly "NOT a NAURA disclosure"), with the company
recording a non-confirmation when an investor named SMIC directly [S178 Q24]; (3)
Ascend-driven capex→NAURA orders — no source at any tier, and the one on-book demand-forward
datum (contract liabilities) declined sequentially [S176]. Consistency test: 688981 scored
W1=3 for hop (1) alone — a one-hop tier-B link. Scoring the three-hop derivative identically
to its own base hop prices the two additional unverified hops at zero evidence cost. RB_02's
own row concedes the point: fab tools are tier "B **(as logic)**, **n/a (as fact)**" — and
W1 grades evidence of a link, not the coherence of a logic. Reverse direction checked per
brief (does second-order framing UNDERSTATE provable exposure?): this session's zh-search
for tender/procurement records surfaced only snippet-grade, mature/specialty-fab
attributions (中芯绍兴, 上海积塔 vintage 2022-23 tender aggregations; strategic-cooperation
language in an aggregator piece) — nothing filing-grade, nothing advanced-node, nothing
Ascend-adjacent; no upgrade path exists. Proposal: **W1=2**, a documented interpolation —
above "tier C only" because each component hop is B-or-better-sourced and NAURA's own tier-1
IR names the "AI算力芯片" demand *category* [S177]; below 3 because no fetched source at any
tier names NAURA in a Huawei/Ascend chain and the compound link's middle hop is
company-non-confirmed. Pre-empting one defense: W2=0 already penalizing non-estimability
does NOT license holding W1 at 3 — the rubric scores evidence strength and materiality
independently, and both cells must stand on their own text.

### W2 = 0 — SUPPORTED (no challenge)

Anchor "0 = NOT-ESTIMABLE" matches V_002371's explicit finding ("Any single-digit or
double-digit 'Ascend exposure %' figure for NAURA would be invented"); the 93.34% exposed
base is correctly not credited (it is the whole domestic capex cycle, not Huawei); treatment
is consistent with 600839, 688981, 002281, 002916, 002156, 301018. The red team notes for
the record that this asymmetry (second-order names take 0 here even when the exposed base is
real and large) is the rubric working as designed, and it makes W1 discipline MORE important
— W1 is the only cell where second-order evidence quality is priced at all.

### W3 = 3 → propose 2

Anchor 1 is "deteriorating margins or persistent cash burn"; anchor 5 requires
"stable/rising margins". FY2025: GM -2.75pp, NM -4.81pp (a 26% relative decline), absolute
profit DOWN (-1.77% headline, -4.22% ex-NR) on +30.85% revenue, Q4 NM 3.25% [S175;
F_002371]. The deterioration is not a one-quarter artifact: Q1-2026 R&D expense again grew
faster than revenue (+36.64% vs +25.80%, company's own stated reason profit lags) [S176],
and the company's margin defense is the soft "有望稳定" [S177]. Cash: OCF−capex negative two
consecutive years (-473M, -128M); net cash -62% in two years while interest-bearing debt
rose +152% to 14,844M; OCF/revenue 5.4%; inventory ≈443 days of COGS [F_002371; S176].
Profit quality: ~CNY 1,842M of FY2025 R&D capitalized ≈33% of attributable profit, with the
capitalized balance still compounding (+10.9% in Q1-2026) [F_002371] — the 14.03% net margin
that anchors "mixed" carries a material accounting cushion. So the cell mixes genuine
anchor-5 elements (revenue growth, positive OCF, positive net cash) with a fully present
anchor-1 element (deteriorating margins) and a two-year negative-FCF record: the documented
interpolation is **2**, not 3. Consistency: 688981 took W3=2 with STABLE gross margins
(~21.6%) because it consumes cash; NAURA has falling margins AND negative FCF AND a
levering balance sheet, yet scored a notch higher. **Citation-discipline defect the
orchestrator must correct in writing:** the cell's justification reads "contract liabilities
signal backlog" — the only in-file contract-liability data are a sequential DECLINE (-2.06%)
and a MISSING FY2023/FY2024 history, and F_002371 explicitly warns against conflating
合同负债 with 在手订单 and records that circulating backlog claims are unverified. New
context sharpens it: Piotech's same line grew +62.66% YoY to 48.52亿 with a disclosed ~110亿
orders-on-hand [S745] — that is what a filing-adjacent backlog signal looks like; NAURA's is
flat-to-down and unquantified. Strike the phrase or re-source it.

### W4 = 1 — SUPPORTED (conditionally; no independent challenge)

PRICED-FOR-PERFECTION is the best-evidenced designation in VAL_002371 (flat-profit year at
~105x; 81x→105x re-rating in seven weeks on no new numbers; forward ~73x/53x/42x even on
un-reverified consensus). Global note 3 maps PFP on tier ≤B evidence → 1; the demand-cycle
evidence being priced (SMIC capex ~flat at $8.1bn [S184/S189]; company's own "维持高位" IR
guidance [S177]) is tier B or better, so 0's "PFP on tier-C evidence" anchor does not fit.
Consistency guard the orchestrator must state in the written response: if W1 is conceded all
the way to 1 (tier-C-equivalent), W4 must be re-examined against its own 0-anchor for
uniformity with 002281/002916/002156/301018; at the red team's proposed W1=2 (mechanism
tier-B, terminal link absent), W4=1 stands.

### W5 = 4 → propose 3

Three attacks. (1) **Anchor fit:** the 5-anchor is "technical-barrier component layer with
content-per-system growth (optics/connectors/advanced packaging per RB_02 read #2)". Fab
tools are none of these — not a component layer, no content-per-system economics, and the
cell's own cited source (RB_02) files NAURA under "2nd-order: fab tools", outside read #2's
named layers. A 4 is an interpolation toward an anchor of which ZERO elements are present;
the only anchored end of that interpolation is 3 ("defensible but competitive").
(2) **"Quasi-oligopoly" is an invented characterization** — the phrase (and any equivalent)
appears in no V/F/VAL file. The in-file record cuts the other way: [S187] makes 中微/拓荆/
华海清科 the subjects of the June-2026 expansion story with NAURA as background; [S185]
recommends NAURA and 中微 side by side. Fresh tier-3 prints quantify the field: in etch —
NAURA's largest line (>百亿 FY2025 [S182]) — 中微's 98.32亿 (+35.12%) is at rough parity and
growing faster [S742]; in deposition, 拓荆 grew +58.87% (PECVD +75.27%) [S741]; 盛美 grew
+20.80% and issues numeric 2026 guidance where NAURA offers none [S743; S177]. FY2025 profit
growth across the four domestic toolmakers: -1.77% (NAURA) vs +30.69%/+34.67%/+21.05% — the
platform leader is the only one whose profit fell, which is margin/mix pressure inside the
boom, the opposite of oligopoly pricing power. A 650亿-valued, IPO-bound entrant (新凯来,
Shenzhen-SASAC-owned, media-attributed Huawei lineage) has additionally entered exactly
NAURA's categories — etch, thin-film deposition, metrology — with 30+ tools shown at
SEMICON China 2025 [S747]. (3) **Cyclicality:** equipment is the chain's most cyclical
layer; NAURA's own Q4-2025 (NM 3.25%) and its own concession that mature-process expansion
"有所放缓" [S178 Q28] show the cycle turning inside the thesis window. Consistency: 002281
took 4 IN the rubric's named layer (optics) after position discounts; 688981 took 4 as the
chain's literal bottleneck. Awarding the same 4 to a layer outside the chain, with funded
domestic rivals outgrowing it in every major category, compresses a real difference.
**W5=3** — the anchor text "defensible but competitive" describes this company almost
verbatim.

### W6 = 3 → propose 2

(1) **The cell was scored with a mission-flagged open item unresolved.** V_002371:
Entity-List status "flagged as an open item for Phase 2 rather than assumed either way";
F_002371 never touches it; SCORES.csv cites only V+F for W6. Closed this session: NAURA and
ten subsidiaries listed 2024-12-02 (公告2024-080) [S740]; the same action controlled
additional SME items and listed the domestic peer cohort wholesale [S744]; the 2025-09-29
Affiliates Rule extends coverage retroactively to >50%-owned affiliates [S746]. Input-side
supply of US-origin subsystems/components to NAURA now runs through a license regime with
presumption of denial — a risk channel entirely absent from the cell's enumeration, and one
the company's own "不会产生实质性影响" cannot settle. (2) **"No verticalization threat" is
too narrow.** Fabs will not internalize toolmaking, but the rubric's verticalization concept
(RB_02 read #3: the ecosystem absorbing chain value inward, cf. in-house HBM) has two live
analogs here: domestic competitors substituting within the same protected capex pool
(quantified in FY2025 prints [S741/S742/S743]), and the Huawei ecosystem standing up its own
toolmaker — 新凯来, media-attributed 华为星光工程事业部 lineage, Shenzhen-SASAC-owned,
etch/depo/metrology, IPO-bound [S747] — precisely the vendor a Huawei-dedicated fab
(FT-reported, per V_688981's record) would prefer. The Ascend-specific slice of capex — the
only slice this watchlist thesis rides — is the slice most exposed to that in-ecosystem
routing. (3) **Concentration is rising, not stable:** top-5 customers 27.88%→39.02% in one
year, #1+#2 = 23.97% of revenue, all unnamed [F_002371; S179/S470] — two anonymous fabs are
a quarter of revenue, and a single fab's digestion year is material. Anchor arithmetic: the
cell claims neither of the 3-anchor's disjuncts (it concedes diversification and denies
verticalization) and rests the 3 entirely on policy common-mode — but NAURA's policy
common-mode is EXTREME and two-sided (demand: subsidy/policy-coupled domestic capex; supply:
its own Entity-List status [S740]), which is exactly the profile that put 688981 at W6=2.
Hold NAURA at 3 only with a written explanation of why its policy common-mode is materially
milder than SMIC's when both are Entity-Listed and both live on the same policy-coupled
capex pool. **W6=2.**

---

## 3. Verticalization test

Fabs do not internalize toolmaking, so the in-house-HBM precedent does not map onto 002371
as customer-absorption — it maps as **chain restructuring around the layer**, and every
enabling condition is already observable. First, the domestic-substitution mandate that
constitutes NAURA's demand tailwind accelerates every domestic vendor equally: the same
policy yuan that flows to NAURA flows to 中微 (etch at parity, 98.32亿 +35.12% [S742]),
拓荆 (deposition, +58.87%, contract liabilities +62.66% to an absolute level ABOVE NAURA's
[S741; S745]), and 盛美 (+20.80% with numeric 2026 guidance [S743]) — the moat is around the
LAYER, not around NAURA, and FY2025 already shows the leader growing slower than two of
three rivals with the only negative profit print of the four. Second, the Huawei ecosystem
is doing to tools what it did to HBM: 新凯来 — founded from a team media-attribute to
Huawei's 星光工程事业部, wholly owned through Shenzhen SASAC, valued ~650亿 with a 2027 IPO
target — showed 30+ tools across etch, thin-film deposition, and metrology at SEMICON China
2025 [S747]. If Huawei-dedicated fab capacity (FT-reported, per V_688981) buys
in-ecosystem tools, the Ascend-specific slice of domestic capex — the only slice the
watchlist thesis claims for NAURA — is the FIRST slice to be routed away, while NAURA keeps
the commodity remainder of the cycle. Third, on any licensing détente the same fabs prefer
incumbent imported tools for the highest-value steps (NAURA's own disclosures describe its
position as validation-stage penetration: "验证广度和导入深度均显著加快" [S177] — i.e.,
still being designed in, not designed around). NAURA's counter-moves (platform breadth,
R&D at 18.49% of revenue — a quarter of it capitalized [F_002371]) defend share by spending,
which is precisely the mechanism by which FY2025 margins already compressed; at ~105x
trailing earnings the thesis has no cushion for a world where the protected pool is shared
three-or-four ways and the premium slice defects to an in-ecosystem entrant.

## 4. Common-mode test

NAURA does **NOT** share the direct Huawei-order common-mode: it has no Huawei order book,
so the shock that simultaneously hits 688629/002261/301236/600498/000034 (a Huawei
procurement pause, retiering, or Ascend share loss to another chip) reaches NAURA only
lagged and diluted, via fab-capex plans. Its common-mode is the **domestic-capex/policy
factor**, and the tightest coupling in the universe is with **688981**: SMIC's capex IS the
claimed transmission channel (guided ~flat ~$8.1bn 2026 [S184/S189]), so a Big-Fund pacing
slowdown, a subsidy retrenchment, or a fab digestion year takes both names down together —
holding 002371 and 688981 in one Phase-4 book is one policy trade held twice. Weaker
same-direction couplings: 000034/301236 via the 信创/domestic-IT-spend policy channel.
What is unique to NAURA — and absent from the current W6 — is that the policy variable
bites in BOTH directions: escalation (further US controls) helps its demand side but now
squeezes its own inputs (Entity List since 2024-12-02 [S740]; Affiliates Rule 2025-09-29
[S746]); reversal (a US-China framework re-licensing AMAT/LAM/TEL sales to SMIC-class fabs,
or NVIDIA re-admission reducing the urgency of domestic AI-chip capacity) deflates the
substitution premium AND lets its customers buy imported tools again. NAURA is short a
détente on both sides of its own income statement. The genuine diversifiers against this
factor in the universe remain 300308 (global/NVIDIA optics cycle — plausibly HELPED by a
reversal) and 600839 (low chain coupling).

## 5. Five falsifiable checks

| # | Observable event | Window | Bear if | Bull if |
|---|---|---|---|---|
| C1 | H1-2026 半年报: GM / NM / attributable NP (H1-2025 base: NP 3.208bn = Q1 1.581 + Q2 1.627 [S175]) | by 2026-08-31 (statutory) | GM <40.10% or H1 NP ≤3.21bn (margin "stabilization" [S177] falsified; consensus 8.0bn FY [S186] needs ~4.0-4.6bn H1) | GM ≥42% AND H1 NP ≥4.3bn (+34% — margin-accretive growth finally printed) |
| C2 | 合同负债 at 2026-06-30 (H1 report) and 2026-09-30 (三季报 by 2026-10-31), vs 4,291M (2025-12-31) / 4,203M (2026-03-31) [S176] | 2026-08-31 / 2026-10-31 | ≤4.2bn again (third consecutive flat/down reading — capex-flow-to-orders logic unfunded on the company's own book) | ≥5.0bn, or any filing-grade 在手订单 disclosure (closing the gap vs Piotech's disclosed ~110亿 [S745]) |
| C3 | SMIC quarterly capex realization vs its "roughly flat ~$8.1bn" 2026 guidance [S184/S189] | H1 results ~Aug 2026; Q3 ~Nov 2026 | H1-2026 capex <$3.5bn annualized short of guidance, or guidance cut — the thesis's transmission channel shrinks at the source | run-rate ≥$4bn/half or guidance raised |
| C4 | Export-control events, BOTH directions: (a) BIS/enforcement action restricting subsystems/components to listed Chinese toolmakers or invoking the Affiliates Rule against a NAURA affiliate [S740; S746]; (b) US-China framework re-licensing advanced-tool sales to SMIC-class fabs | now → 2026-12-31 | either (a) input squeeze materializes, or (b) substitution premium deflates — the double-edge cuts | status quo, or fab-level tightening WITHOUT toolmaker-input escalation (pure demand tailwind, W6 challenge weakened) |
| C5 | Peer H1-2026 prints (中微/拓荆/盛美, all by 2026-08-31) + 新凯来 milestones (fab validation win, IPO filing) [S747] | by 2026-08-31 (prints); → 2027-06-30 (新凯来) | NAURA again bottom-half of the four on revenue growth, or 新凯来 announces a validated etch/depo acceptance at an advanced-logic fab — share-shift/verticalization-analog confirmed | NAURA top-2 on revenue growth AND NP growth ≥ revenue growth (platform leverage returns; W5 challenge conceded by events) |

---

## New sources fetched this session (zh-language, logged in frags/rt_002371.json)

- **[S740]** 上海证券报/中国证券网, 2024-12-04, tier 2, fetched — NAURA 公告2024-080: company
  + 10 subsidiaries added to US Entity List 2024-12-02; company impact statement verbatim.
  Closes V_002371's flagged open item.
- **[S741]** 证券时报, 2026-04-27, tier 3, fetched — 拓荆科技 FY2025: revenue 65.19亿
  +58.87%, NP 9.27亿 +34.67%, PECVD +75.27%.
- **[S742]** 财联社, 2026-02-27, tier 3, fetched — 中微公司 FY2025: revenue 123.85亿
  +36.62%, NP 21.11亿 +30.69%, etch 98.32亿 +35.12%, R&D投入 30.23% of revenue.
- **[S743]** 证券时报, 2026-03-02, tier 3, fetched — 盛美上海 FY2025: revenue 67.86亿
  +20.80%, NP 13.96亿 +21.05%; 2026 guidance 82-88亿.
- **[S744]** 21世纪经济报道, 2024-12-04, tier 3, fetched — Dec-2024 BIS action scope: 136
  Chinese entities incl. 拓荆/芯源微/华海清科; new SME/HBM item controls.
- **[S745]** 新浪科技(转投影时代), 2026-04-28, tier 3, fetched — 拓荆 contract liabilities
  48.52亿 +62.66%, orders-on-hand ~110亿, OCF 36.33亿 — the backlog-contrast datum.
- **[S746]** 商务部 mofcom.gov.cn, 2025-09-29, tier 1, fetched — BIS Affiliates Rule (50%
  penetration, retroactive) and MOFCOM response; escalation-trajectory evidence.
- **[S747]** C114通信网, 2025-09-08, tier 3, fetched — 新凯来: 30+ tools across
  etch/deposition/metrology at SEMICON China 2025, ~650亿 valuation, 2027 IPO target;
  ownership chain and Huawei-lineage attribution carried at tier 4 via parallel fetch,
  signal-only, non-load-bearing.

## Bottom line for the orchestrator (written response required per rubric before G3)

Seven challenges: four cell disputes (W1 3→2 — a three-hop logic scored at its base hop's
tier; W3 3→2 — anchor-1 "deteriorating margins" literally present plus two-year negative
FCF; W5 4→3 — zero 5-anchor elements, "quasi-oligopoly" unsupported, peers outgrowing the
leader; W6 3→2 — scored with the Entity-List item open, verticalization-analogs ignored;
corrected total 1.55, rank ~12) and three written-response items regardless of score
disposition: (i) strike or re-source W3's "contract liabilities signal backlog"; (ii)
strike or source W5's "quasi-oligopoly" characterization; (iii) incorporate [S740]/[S744]/
[S746] (Entity List + Affiliates Rule) into the W6 record even if the score is held. W2=0
and W4=1 are supported as scored (W4 conditionally: it must fall to 0 only if W1 is ever
reclassified to tier-C-equivalent). The structural point for the answer key: on the current
board NAURA at 2.15 outranks 688981 at 1.90 while depending on 688981's capex for its own
thesis and adding two unverified hops to 688981's own tier-B link — any consistent
disposition of these challenges restores the derivative below its base.
