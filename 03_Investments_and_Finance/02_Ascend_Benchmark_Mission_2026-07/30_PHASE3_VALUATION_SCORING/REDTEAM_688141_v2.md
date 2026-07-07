Educational benchmark for a paper-trading learning exercise. Simulated allocations, not investment advice or recommendations.

# REDTEAM_688141_v2 — 杰华特 Joulwatt Microelectronics (688141.SH) — re-red-team, accuracy patch, 2026-07-07

Red-team brief: attack, do not balance. Row under attack (SCORES_v2.csv, "REVIEWED-NEW", never previously
red-teamed): **W1=3, W2=0, W3=1, W4=1, W5=3, W6=3, total 1.70** (weight arithmetic re-checked:
0.60+0+0.15+0.20+0.45+0.30 = 1.70 exact). Inputs: V_688141.md, F_688141.md, VAL_688141.md, FR_688141.md,
SCORES_v2.csv, SCORING_NOTES_v2.md §1, 01_MISSION/SCORING_RUBRIC.md, SOURCE_STANDARDS.md,
REDTEAM_RESPONSES.md (R0.1/R0.2/R0.3 standards; R1.1/R2.1 precedents), RB_02. Sibling v2 red-teams cited
for consistency arguments only (REDTEAM_688519_v2, REDTEAM_688347_v2 — responses pending). New sources
this session: [S1282]–[S1285], ledgered in 90_BIBLIOGRAPHY/frags/rt2_688141.json (S1286–S1289 unused).
WebFetch budget 3/4 spent (§trail); zh-language searches throughout per rule 7. Headline: **the W1=3 pays
a full tier-B score to a single analyst team's section placement that no second source — and, decisively,
not the company itself, at a Hong Kong roadshow in front of Point72/Millennium/贝莱德/高毅 [S1282, tier 1,
newly parsed this session] — has ever seconded; while W6=3 books the benign half of an anonymous-#1 fork
whose bull half (it's Huawei) the row simultaneously cashes in W1. Both halves cannot be true at once.**
Five score challenges + one record-correction demand; all-accepted delta −0.45 (total 1.25). Every
challenge requires a written response in REDTEAM_RESPONSES_v2 before Gate PG2/G3 passes.

---

## 1. Strongest bear case (5 bullets)

- **B1 — The Ascend link is one analyst's contextual placement, seconded by nobody, counter-framed by the
  company eight times.** The entire B rests on 国盛证券 2025-05-06 placing "杰华特DrMOS和多相控制器产品已
  量产爬坡" inside its Ascend-chain power section — with V_688141's own caveat that the report "does NOT
  state a direct 杰华特→Huawei/Atlas supply contract" [S924]. Against that single outlet: (i) the FY2025 AR
  full text — zero 华为/昇腾/鲲鹏 anywhere [S920]; (ii) IR replies of 2025-05-21 (15 days AFTER S924)
  framing the same DrMOS/multiphase family as "Intel VR14及Intel IMVP9.3平台" work, no customer named
  [S1154]; (iii) **new this session, tier 1, directly parsed:** IR活动记录表 编号2025-007 — a Hong Kong
  roadshow 2025-11-06/07 before ~60 global institutions (Point72, Millennium, BlackRock, Templeton, 高毅,
  惠理…), chairman presenting, growth attributed to "公司重点投入的计算、汽车等领域产品逐步实现规模化量产";
  华为/昇腾/Atlas/鲲鹏/海思 appear NOWHERE, no customer is named, and the H-share Q&A is answered with
  boilerplate [S1282]. If an Ascend anchor-customer story existed and were speakable, a pre-H-share-IPO
  roadshow to global funds is where it pays maximum dividends; the company passed. (iv) Even the sell side
  is not unanimous: 国信证券's OWN multiphase deep-dive (2025-02-05, relayed [S1284]) covers the identical
  product line as generic MPS-substitution "增量蓝海" and never mentions 华为/昇腾. (v) The only artifact
  asserting "绑定华为昇腾" is a rejected tier-4 blogger post [S930].
- **B2 — The anonymous-#1 fork: both halves are bearish, and the row books the bull half of each.** One
  never-named customer has held 26–31% of revenue for three straight years (FY2025: 30.04% ≈ CNY 798M)
  [S925;S920]. Fork A (it is Huawei-linked): then the row carries single-ecosystem concentration ~30% PLUS
  live verticalization/re-tiering exposure to the one customer with a demonstrated internalization appetite
  (R0.3, in-house HBM) — W6's "exactly one concentration, no verticalization" basis fails. Fork B (it is
  NOT Huawei-linked): then the Ascend thesis has **zero revenue anchor** — 30% of the book belongs to a
  mystery non-Huawei OEM, W1's 3 decorates a business the thesis cannot reach, and the 27.63x P/S
  capitalizes a customer the company has anonymized aggressively since IPO, when related-party "A公司" was
  its largest customer and the prospectus declined to describe its background [S926]. There is no fork
  under which W1=3 and W6=3 are simultaneously earned.
- **B3 — The cash story is worse than "persistent burn": the last two reported quarters broke the only
  improving trend the bull case had.** OCF negative three straight FYs (−291.43/−360.44/−323.50M), net cash
  +632.25M → net DEBT −1,814.50M, 资产负债率 36.89→49.50→65.18% [F_688141]. New arithmetic from
  [S1282]+[S920]: Q4-2025 revenue = 265,502.48 − 194,242.49 = 71,259.99万 = 712.60M, a **−5.63% QoQ decline**
  (vs Q3's 755.08M) in the domestic-AI boom quarter; Q4-2025 归母 = −71,712.42 − (−45,990.80) = −25,721.62万
  = −257.22M vs Q3's −164.82M — then Q1-2026 −276.00M [S921;S923]: **two consecutive quarters of sequential
  loss-widening** into the 2026-07-07 quote (no Q4-2024 single-quarter comparator on file; seasonality not
  excludable — the direction still contradicts the "conversion under way" narrative). Liquidity coverage,
  computable from F_688141's own components and absent from every file narrative: debt due <12mo = 75,879.79
  + 36,955.50 = 112,835.29万 (1,128.35M) vs 货币资金+交易性 = 47,417.00万 (474.17M) → **0.42x coverage**
  while burning ~324M/yr of OCF. The funding plan is an HK IPO that has already lapsed once (applied
  2025-05-30, resubmitted 2026-01-13 [S928]) with no hearing-passage record findable as of 2026-07-07
  (search trail; June-2026 hearing-wave coverage does not name 杰华特 [S1285 snippet]).
- **B4 — Cohort-half economics inside a documented price-war layer.** GM 27.40→27.35→26.37→25.32% (Q1-26) —
  four consecutive reported periods of decline [S923;F_688141] — while the domestic analog recovery cohort
  prints GM >45% and turns profitable in the same window (思瑞浦 GM>45% 扭亏, 圣邦/帝奥微 GM>45%, 晶丰明源
  扭亏) [S1283]. The layer's pricing is regulator-documented as war-damaged: US analog imports' unit prices
  fell 52% cumulative 2022–2024 (3.36→1.62 元/颗), domestic weighted unit gross profit −40.86% (2023 vs
  2022), MOFCOM anti-dumping probe alleging >300% dumping by TI/ADI/Broadcom/onsemi opened 2025-09 [S1283].
  In multiphase/DrMOS specifically — the product the thesis prices — 国信证券 places incumbency with
  overseas MPS/英飞凌/瑞萨/AOS and puts 杰华特/晶丰明源/芯朋微 at "客户导入和批量销售初期" [S1284]: an
  early-stage challenger at 1.9% global DC-DC share [S928 color], not a moated incumbent.
- **B5 — Priced for a perfection nobody can even define.** 27.63x FY2025 sales / 25.37x TTM with P/E n/a —
  no profitable fiscal year or quarter anywhere in the record [VAL_688141]. Unlike every other
  PRICED-FOR-PERFECTION name on the board, there is no earnings floor of ANY size under the multiple; the
  growth being capitalized ("计算领域") bundles PC/server/storage and cannot be decomposed to AI-servers,
  let alone to Ascend (W2 NOT-ESTIMABLE; DC-DC line 53.29% spans PC/auto/industrial/comms [S920]); and the
  H-share raise the balance sheet needs is simultaneously an unquantified dilution overhang the W4 cell
  never logged.

---

## 2. Score audit — every cell, supported or corrected

Weights .20/.20/.15/.20/.15/.10. Current row 3,0,1,1,3,3 = 1.70 (arithmetic verified).

| Cell | Current | Supported by cited files? | Red-team proposal | Δ |
|---|---|---|---|---|
| W1 | 3 | **NO** — letter B stands, substance is single-outlet, relationship-free, company-contradicted; R2.1 caps a substance-thin B at 2 | **2** | −0.20 |
| W2 | 0 | **YES** — R0.1 literally applied; both ceilings span bands; A8 respected; [S1282] adds no split | 0 (hold) | 0 |
| W3 | 1 | **YES with gaps** — attacked both directions per brief; 1 survives both, subject to audit-opinion verification + aggravator log | 1 (hold + demands) | 0 |
| W4 | 1 | **CONTESTED basis** — R0.2 letter-rule survives at B; Ascend leg of the priced narrative has no relationship-grade carrier; aggravator stack unlogged | 1 (hold + mandatory log; conditional 0) | 0 |
| W5 | 3 | **WEAK** — early-stage challenger position, cohort-half GM falling 4 periods, price-war layer economics | **2** | −0.15 |
| W6 | 3 | **NO** — fork unresolved (B2); R0.3 defeats the "no power-stage precedent" defense; related-party anonymization precedent unpriced | **2** (conditional 1) | −0.10 |

All-accepted total: **1.25** (delta −0.45). W1-only concession: 1.50. Every challenge requires a written
response per SCORING_RUBRIC ("Red-team concessions change scores only with a written response").

**Challenge 1 — W1 3→2 (documented interpolation; tier letter B unchanged).** (i) The controlling ACCEPTED
precedent is R2.1 (300308): tier letter B stood, yet the score was capped at 2 because "the substance is
one bare stock-code clause… the documented-interpolation convention caps a substance-thin B at 2 (the
688981 comparison — named dies, multiple outlets — shows what a full 3 looks like)." Map 688141 onto that
ruler: ONE outlet [S924]; the sentence describes a product ramp, not a counterparty; the verifier's own
caveat concedes no supply relationship is asserted; there is no Huawei-side artifact of any kind; and the
company's own voice — now EIGHT+ Huawei-silent artifacts, including the tier-1-parsed HK roadshow record
[S1282] and the Intel-platform IR framing [S1154] — actively assigns the product family a different
platform context. 688981's full-3 substance (named dies, multiple outlets) is absent on every axis.
(ii) Ladder consistency: 688629 holds W1=3 on a triangulated 60.52% Huawei-corroborated DIRECT customer
with brand-silent filings (relationship-without-prose, REDTEAM_RESPONSES R1.1); 300308 holds 2 on
prose-without-relationship. 688141 is prose-without-relationship — single-outlet prose at that — and its
prose is weaker than 300308's in one respect: the 国盛 sentence never even asserts chain membership as a
fact, it locates a product ramp inside a chapter. If 688141 holds 3, the row pays one analyst's page layout
what 688629 paid for a triangulated 60% customer; that is the exact inversion REDTEAM_688519_v2 challenge 1
(pending) attacks — prose/context vs relationship. (iii) The second named sell-side covering the identical
product line [S1284] does NOT place it in the Ascend chain — the one Ascend placement is not even the
consensus sell-side framing. Under SOURCE_STANDARDS, single-tier-3 support for the mission's load-bearing
relationship class is exactly the thin case the interpolation convention exists for. (iv) The Hubble leg
stays zero-weighted (FR flag (a)): register identity (云通大业 rename question) remains unresolved — this
session's zh-search found no 减持/rename record either way (trail) — so the B rests 100% on S924. Propose
**2**. Restoration path to 3 stated in check 4.

**Challenge 2 — W2 0 CONFIRMED (attacked both directions; no change).** Up-attack fails: [S1282] gives a
tier-1 growth attribution ("计算、汽车等领域") but no segment split — "计算" bundles PC/server/storage, so
no band is selectable; the 30.04% #1 stays non-equatable per A8; the DC-DC 53.29% cut spans four
end-markets [S920]. Down-direction is already the floor. R0.1 literally applied, consistent with the
NOT-ESTIMABLE class (V_688141; FR_688141). Audit note for the record: if the HK prospectus ever prints a
customer or segment table (check 1), W2 must be re-run before any Phase-4 reuse of this row.

**Challenge 3 — W3 hold at 1, BOTH directions attacked per brief; two written demands.** Up-case (→2),
stated fairly: NM improved three straight FYs (−40.98→−27.01%), revenue +58.15% FY2025 and +44.80% Q1-2026,
GM stable ~26–27%, R&D 36% of revenue is optionality, FY2023 was net-cash, and the company claims 7
consecutive quarters of YoY revenue growth [S1282]. DISMANTLED: (i) the NM-improvement trend broke in
Q1-2026 (−36.08%) [VAL_688141], and the new sequential arithmetic (B3) shows loss-widening in BOTH of the
two most recent reported quarters plus a QoQ revenue decline in Q4-2025 — the trajectory argument now cuts
against the up-case; (ii) the rubric's anchor-1 text ("persistent cash burn") is met literally three FYs
running, with the burn GROWING in absolute terms while the balance sheet swung to −1,814.50M net debt;
(iii) ladder: 600498 holds W3=1 with a POSITIVE net margin and positive OCF (REDTEAM_RESPONSES R5.3);
lifting a −27%-NM, negative-OCF, net-debt name to 2 inverts the ladder. Down-case (→0, distress): the
0.42x coverage of <12mo maturities (B3) at a ~324M/yr OCF burn is a distress-shaped balance sheet — but
anchor 0 ("distress signs") is not evidenced on file: no going-concern language, no default, no regulator
action in any fetched source, and FY2025 financing CF +713.85M shows debt access open [F_688141]. The gap:
**nobody in P1/P2/FR ever fetched the FY2025 audit opinion type.** Demands: (a) verify the FY2025 audit
opinion (standard unqualified + no going-concern emphasis → 1 stands; anything else → 0 question reopens);
(b) log the liquidity-coverage arithmetic (0.42x; 1,128.35M due <12mo vs 474.17M liquid) as a W3 aggravator
in the answer key. Also for the record: FR's own not-0 rationale leans on "H-share raise pending [S928
color]" — a contingent, twice-filed, unpriced event doing load-bearing work in W3 while its dilution twin
is absent from W4 (see challenge 4). One event cannot be counted only where it helps.

**Challenge 4 — W4: hold 1 under protest per R0.2 + MANDATORY aggravator log; conditional 0.** The letter
rule (R0.2: A/B→1 when PRICED-FOR-PERFECTION) survives my W1=2, which is an interpolation, not a letter
change (precedent: R2.4 — "conditionality not triggered by the W1=2 interpolation"). But the
FR_002916/FR_002156 practice reads the tier of the PRICED NARRATIVE, and here the narrative being
capitalized at 27.63x sales is "AI-server power content growth AT JOULWATT": its carriers are tier-1 for
GENERIC computing growth ("计算领域…规模化量产" [S1282]; "服务器领域渗透率显著提升" [S929 relay of AR
language]) and single-outlet-B-with-no-relationship for the Ascend leg [S924] — i.e., sector prose, not
Joulwatt-specific AI evidence. If the orchestrator rules the priced narrative is specifically the
Ascend/domestic-AI story (VAL_688141's own reading: the mission "cannot confirm how much (if any) of the
58% revenue growth… is actually AI/Ascend-linked"), R0.2's own logic yields 0. Formal proposal: hold 1 +
log, conditional 0. The aggravator log (precedent: R1.4, C5-002261, C4-301236; sibling demands pending in
REDTEAM_688519_v2 ch.4 and REDTEAM_688347_v2 C5) must record: (a) **27.63x/25.37x sales with P/E n/a — the
only PFP structure on the board with no earnings floor of any size** (perfection multiplied by an undefined
base); (b) **HK-IPO dilution overhang**: terms unquantified anywhere on file, application lapsed once,
resubmission 2026-01-13 approaching its own 6-month validity window with no hearing record as of 2026-07-07
[S928; S1285 snippet; trail]; (c) the **W3/W4 double-count tension** (challenge 3); (d) **Q1-2026 margin
break + two consecutive quarters of sequential loss-widening** (B3 arithmetic) — the price is underwriting
an inflection the two most recent prints move away from.

**Challenge 5 — W5 3→2 (documented interpolation).** The cell reads "real barriers + AI content growth,
defensible but competitive" and stops at the layer level. The adjudicated within-layer-position method
(002281 precedent, applied in R1.5/R2.5) requires discounting THIS name's position: (i) incumbency in
multiphase/DrMOS sits with MPS/英飞凌/瑞萨/AOS; 杰华特 is named by 国信 as one of three domestic entrants
at "客户导入和批量销售初期" [S1284] — the thesis prices an entrant, not a franchise; (ii) demonstrated
economics are cohort-half: GM 26.37%→25.32% falling four straight reported periods vs the domestic analog
recovery cohort's >45% GM with profit inflection [S1283;S923] — margin-squeeze evidence at name level,
anchor-1 grammar; (iii) the layer's pricing environment is regulator-documented war damage (unit import
prices −52% 2022–2024; domestic unit gross profit −40.86% in one year [S1283]), and the current repair
depends on a policy shield (anti-dumping probe) that can be traded away (§4); (iv) 1.9% global DC-DC share,
#13 global analog [S928 color] — subscale. Honest counterweights keep this at 2, not 1: 36% R&D intensity
[F_688141], Intel VR14/IMVP9.3 platform qualification as capability proof [S1154], genuine multiphase
technical barriers and content-per-system growth ("增量蓝海" [S1284]). "Defensible but competitive"
describes the LAYER; this name's demonstrated position within it is entrant-with-half-cohort-margins.
Propose **2**.

**Challenge 6 — W6 3→2 (documented interpolation), conditional 1; plus a consistency demand.** The current
basis ("exactly one material concentration; no documented power-stage verticalization/internalization
precedent → 3") fails on three grounds. (i) R0.3 (ACCEPTED) rejects layer-specific-precedent reasoning: the
in-house-HBM parenthetical defines Huawei's demonstrated APPETITE — demanding a power-stage precedent is
the exact move R0.3 struck down. DrMOS/multiphase is an AVL-governed, standards-defined (Intel VR/SVID
grammar [S1154]) merchant-silicon slot that the board owner can re-tier at zero switching cost, and the
named substitute bench (晶丰明源/芯朋微 at the same entry stage [S1284], plus the overseas incumbents)
exists today. (ii) The fork (B2): if the anonymous #1 is Huawei-linked — the reading W1's 3 implicitly
monetizes — then concentration AND verticalization exposure are BOTH present → anchor-1 territory; if it is
not, the concentration remains and acquires a governance aggravator: the anonymization habit dates to the
IPO, when the largest customer was a RELATED PARTY the prospectus declined to describe [S926]. The row
cannot hold W1=3 on the Ascend-through-#1 imagination and W6=3 on its negation; a written fork election is
demanded. (iii) Policy common-mode is understated: the name's margin repair is coupled to the anti-dumping
shield [S1283] (§4), and its funding to the HK window — two policy/market common-modes on top of the
customer concentration. Between "one concentration" (3) and "both" (1) → propose **2**; **conditional 1**
if the answer key adopts the Huawei-linked reading of the #1 customer anywhere in this row's narrative.

**Record-correction demand (no score change).** FR_688141 flag (b) recorded the 2025-08-12/2025-11-10 IR
records as unverifiable (QQ-hosted PDF password-protected). The 2025-11-10 record IS verifiable — the
eastmoney-hosted original parsed cleanly this session [S1282] and confirms FR's inference (Huawei-silent,
no customer named) at tier 1. The answer key's W1 narrative should cite S1282 as the verified artifact
rather than an inference from silence, and the mission's PDF-failure trail should note the
pdf.dfcfw.com host as a working fallback for QQ/cninfo-blocked 公告 PDFs.

---

## 3. Verticalization test

If Huawei internalizes the board-power layer, 688141's thesis does not degrade — it evaporates, and
invisibly. The in-house-HBM precedent's adjudicated meaning (R0.3) is appetite to control choke points;
board-level VRM (multiphase controller + DrMOS) is a smaller step than HBM was: it is standards-grammar
silicon (VR/SVID-class specs [S1154]) on mature BCD-class analog processes, the exact profile HiSilicon
already handles for its own devices' power-management ICs (handset-PMIC self-design is widely relayed but
was findable only at tier-4 grade this session — logged as a verification target, not load-bearing), and
Huawei already owns the power ARCHITECTURE above the chip: the very report anchoring W1 notes "Atlas系列
服务器电源模块也在升级" [S924] — the module layer that decides whose DrMOS lands on the board is Huawei's
own. Because no 杰华特→Huawei relationship was ever disclosed by anyone (B1), internalization — or its
cheaper cousin, re-tiering the AVL to 晶丰明源/芯朋微 [S1284] or a HiSilicon design — would produce no
observable event: no contract termination, no announcement, just an anonymous #1 (or a hoped-for future
customer) that quietly never grows. Under Fork A (#1 is Huawei-linked, ~30% of revenue [S925]), the same
move is a 30%-of-revenue single-decision shock into a balance sheet with 0.42x short-maturity coverage
(B3). The one mitigant is also the indictment: Joulwatt's verified server-power qualifications are
Intel-platform [S1154], so the Ascend option Huawei could kill was never verified to exist — which is
precisely why the row should not be paying W1=3 for it.

---

## 4. Common-mode test

**Huawei/domestic-AI demand shock (shared with the whole board).** 688141's variant is the most opaque and
the highest-beta: the transmission channel (anonymous #1, 30.04%) is unobservable until a concentration
table prints months later, and the 27.63x-sales/no-earnings structure [VAL_688141] has the furthest to
fall of any PFP cohort member on a single bad Ascend datapoint — there is no E for the de-rating to stop
on. **Policy reversal, wire 1 (US export relaxation / Nvidia return).** Domestic-chain urgency drops
board-wide; 688141 is partially and ironically hedged — its company-voice server credentials are
Intel-platform [S1154;S1282] — but the 27.63x multiple is not priced off the Intel business, so the hedge
protects revenue while the valuation story still de-rates. **Policy reversal, wire 2 (688141-specific
within this portfolio): the analog anti-dumping shield.** The domestic analog cohort's 2025 margin repair
is coupled to the MOFCOM probe on US analog imports (>300% alleged dumping, initiated 2025-09) [S1283]; a
US-China settlement that suspends or trades away the probe re-opens the TI/ADI price war on the entire
domestic analog space — within this portfolio only 688141 carries that wire, and it carries it with the
least buffer (GM 25–26%, NM −27% to −36%, net debt). **Financing-window common-mode.** The W3 not-0
rationale and the burn-bridge both run through the HK IPO window (resubmitted 2026-01-13, no hearing
record as of 2026-07-07 [S928; S1285 snippet]); an HK-window closure (market-wide event, shared with every
A+H aspirant) simultaneously fires the W3 down-case and removes W4's implicit rescue. A Huawei demand
shock and an HK-window shock are correlated through the same macro trigger — the portfolio should treat
them as one wire, not two.

---

## 5. Five falsifiable checks

1. **HK application resolution by 2026-07-31** (the 2026-01-13 resubmission's 6-month validity window
   closes mid-July; observable on HKEXnews/杰华特公告). Hearing passed + PHIP published → BULL, and the
   PHIP's mandatory customer/supplier disclosures become the fork-resolver (check 3) — fetch immediately.
   Second lapse or withdrawal → BEAR (funding leg fails; W3 aggravator fires; W4 dilution overhang converts
   to a refinancing overhang).
2. **H1-2026 interim (due 2026-08-31): sequential loss and OCF.** Q2-2026 归母 loss wider than Q1's
   −276.00M (third consecutive sequential widening) or H1 OCF at/below −200M → BEAR (W3 hold-at-1
   vindicated, 0-question reopens against the maturity wall); loss narrowing QoQ + OCF improvement + GM
   back above 26% → BULL (FR's trajectory reading recovers; my B3 becomes seasonality).
3. **First customer-identity artifact — HK prospectus/PHIP or FY2026 AR (whichever first; outer date
   2027-04-30): the #1 customer.** Named or described as Huawei/Huawei-affiliated → BULL for the thesis
   (W1 letter path to A; W2 becomes estimable at ~30% band) — this is the single biggest upside risk to
   this red-team's W1/W6 challenges, stated openly. Described as a non-Huawei OEM/ODM (PC, auto,
   industrial) → BEAR (Fork B confirmed: the Ascend thesis loses its only conceivable revenue anchor;
   W1's decoration argument vindicated).
4. **Any tier ≤B artifact asserting a 杰华特→Huawei/Atlas SUPPLY relationship by 2026-12-31** (own filing,
   IR reply naming 华为/昇腾, named-media or named-sell-side stating a customer relationship rather than
   chain-section placement; or a Huawei-side artifact). Appears → BULL: W1 restoration to 3 (letter B with
   relationship substance) or 4-path; my challenge 1 withdraws. Instead, a 2026-vintage Ascend-chain update
   from any named house that drops 杰华特 or slots 晶丰明源/芯朋微/南芯 in the power position → BEAR
   (single-outlet placement was noise, not signal).
5. **MOFCOM analog anti-dumping ruling (preliminary ruling watch from 2026-09-19, one year after
   initiation; final by ~2027-03).** Affirmative duties on TI/ADI/Broadcom/onsemi interface/driver chips →
   BULL for the whole domestic analog cohort's pricing including 688141 (W5 up-pressure; margin-repair
   tailwind). Suspension/withdrawal/negotiated settlement → BEAR (price-war shield removed against a
   −27%-NM, net-debt balance sheet; W5=2 vindicated and W3 stress amplifies).

---

## Search/fetch trail (zh-language, per rule 7)

Searches (7): 「杰华特 哈勃 减持 云通大业 股东」(no rename/减持 record either way — register ambiguity
UNRESOLVED; stcn "华为参股的A股名单" color only); 「杰华特 华为 昇腾 服务器 电源 DrMOS 供应」(no second
named tier-3 source asserting a supply relationship; hits are Zhihu/blog tier-4 relays of S924's framing —
search-engine synthesis text pattern-completed a "supplier" claim unsupported by the underlying links,
discarded per NUMBER TRUTH RULE); 「模拟芯片 价格战 2025 德州仪器 降价 国产 内卷 毛利率」(→S1283);
「海思 电源管理芯片 自研 PMIC 华为 服务器 供电」(HiSilicon PMIC self-design claims found only at tier-4
grade — logged as color/verification target, never load-bearing); 「杰华特 港股 IPO 聆讯 上市 2026」(→
pdf.dfcfw.com IR record URL surfaced; no hearing record); 「多相电源 DrMOS 竞争格局 MPS 芯源系统 英飞凌
杰华特 晶丰明源 南芯」(→S1284; 国信 PDF original located but relay sufficed); 「杰华特 H股 港交所 递交
失效 通过聆讯 2026年6月」(June-2026 hearing-wave coverage does not name 杰华特 [S1285 snippet]; absence of
record ≠ record of absence — framed only as "no hearing-passage record findable as of 2026-07-07").
Fetches (3/4 budget): (1) pdf.dfcfw.com H22_AN202511101778725654_1.pdf → WebFetch text layer garbled;
saved binary parsed page-by-page via local PDF read — full text recovered = **S1282** (tier 1); (2)
finance.sina.com.cn 2025-09-19 analog price-war/anti-dumping piece = **S1283**; (3) stcn.com 国信证券
multiphase relay = **S1284**. 4th fetch unspent.

## Sources this session

[S1282] 杰华特微电子投资者关系活动记录表 编号2025-007（香港路演 2025-11-06/07；东方财富公告PDF原件）—
  2025-11-10, tier 1, fetched (binary parsed). 9M-2025 营收 194,242.49万 (+63.01%), Q3单季 75,507.88万
  (+71.18%, 环比+14.54%); 9M 归母 −45,990.80万, Q3单季 −16,481.81万; 全文无华为/昇腾/Atlas/鲲鹏/海思;
  未点名任何客户; H股问答仅"有序推进".
[S1283] 新浪财经: 盈利逐步修复，国产模拟芯片摆脱"低价绞杀" — 2025-09-19, tier 3, fetched. MOFCOM
  反倾销立案（TI/ADI/博通/安森美, 倾销幅度>300%, 进口单价2022–2024累计−52%）; 国内单位内销毛利润
  2023较2022 −40.86%; 2025H1恢复期同行毛利率>45%/扭亏名单.
[S1284] 证券时报网: 国信证券——多相电源是增量蓝海市场 看好国产化机遇 — 2025-02-06, tier 3, fetched.
  海外MPS/英飞凌/瑞萨/AOS主导; 杰华特/晶丰明源/芯朋微"进入客户导入和批量销售初期"; 全篇无华为/昇腾.
[S1285] 证券时报网: 港股IPO"疯狂一周"：19企递表14家聆讯10股齐发 — 2026-06, tier 3, **snippet only**
  (headline-grade; used solely as color for check 1's context; 杰华特 absent from the named hearing wave).
Full entries: 90_BIBLIOGRAPHY/frags/rt2_688141.json (S1286–S1289 unused). All other [S###] cites reference
entries already ledgered by V_/F_/VAL_/FR_688141.
