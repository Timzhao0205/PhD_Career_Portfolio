Educational benchmark for a paper-trading learning exercise. Simulated allocations, not investment advice or recommendations.

# REDTEAM_688347_v2 — 华虹宏力（原华虹公司）Hua Hong (688347.SH / 1347.HK) — re-red-team, accuracy patch, 2026-07-07

Red-team brief: attack, do not balance. Row under attack (SCORES_v2.csv, rank 7, "REVIEWED-NEW", never
previously red-teamed): **W1=3, W2=0, W3=2, W4=1, W5=3, W6=3, total 1.85** (weight arithmetic re-checked:
0.60+0+0.30+0.20+0.45+0.30 = 1.85 exact). Inputs: V_688347.md, F_688347.md, VAL_688347.md, FR_688347.md,
SCORES_v2.csv, SCORING_NOTES_v2.md §1, 01_MISSION/SCORING_RUBRIC.md, REDTEAM_RESPONSES.md (R0.1/R0.2/R0.3
standards; R1.3/R2.1 precedents), RB_02. New sources this session: [S1274]–[S1277], ledgered in
90_BIBLIOGRAPHY/frags/rt2_688347.json (zh-language searches + fetches, accessed 2026-07-07; S1278–S1281
unused). WebFetch budget 4/4 used. Headline: **the mission graded a chain whose middle link connects to the
wrong fab. The acquisition 688347 is executing buys 华力微's mature-node Fab 5 (65/55/40nm, 38k wpm) — every
fetched deal document describes the perimeter in exclusively mature-node terms and none mentions 华为/昇腾/7nm
— while the 7nm/SiCarrier/Ascend substance that earns W1=3 sits at Fab 6, which a company inquiry-reply relay
(snippet-grade, verification mandatory) locates at 上海华力集成电路制造 — a third entity EXCLUDED from the
deal. And the injection itself is not "≈1.5% of mktcap": it issues 190,768,392 new shares (+10.98%) at a
locked 43.34 CNY against a 324.00 market — CNY 61.81bn of market value handed to four state counterparties,
7.48x the disclosed consideration.** Six challenges below (5 cell challenges + 1 defect/verification demand);
all-accepted delta −0.60; conditional floor 0.85. Per SCORING_RUBRIC ("Red-team concessions change scores
only with a written response"), the orchestrator must answer each challenge in writing before Gate PG2/G3.

---

## 1. Strongest bear case (5 bullets)

- **B1 — Company voice is Ascend-silent even in the documents that monetize the story.** Five separate
  own-disclosure channels carry zero 华为/昇腾/Huawei/Ascend occurrences (FY2025 + Q1-2026 relays, ×5
  confirmations [V_688347 "What Hua Hong itself says"]); the restructuring 草案摘要's legible text discusses
  only 12英寸/65/55nm/40nm and shows no Huawei/Ascend/7nm in any readable passage [S1274]; the 问询函回复
  relay describes the deal as "新增3.8万片/月的65/55nm、40nm产能" with no advanced-node or Huawei language
  [S1277]; the 芯智讯 deal explainer — 华为/昇腾/7nm "完全未提及" [S1275]; the Q1-2026 sell-side review —
  no Huawei/Ascend/named AI customer [S1276]. FR_688347's own standard is "silence is informative" because
  the company names an AI customer when it has one — and the one it named is Nvidia (2024, [S912]).
- **B2 — The tier-B evidence attaches to an asset outside the audited scope AND (pending verification)
  outside the post-merger scope.** The 7nm/SiCarrier work is located "at its Hua Hong Fab 6 site" [S909].
  Every fetched deal paper defines the acquired perimeter as Fab-5 mature-node capacity only (38k wpm of
  65/55/40nm [S1277; S914]; appraisal 84.8亿 on 20.0亿 book [S1275]). A search-summary passage of the
  company's inquiry reply — **snippet, NOT load-bearing** — states the split outright: "市场所期待的先进制程
  资产是华虹六厂（上海华力集成电路制造有限公司华力二期），规划工艺水平为28/22纳米技术节点，不构成同业竞争。
  本次收购的标的资产为华力微所运营的…（华虹五厂）…股权." If Fab 6 belongs to 华力集成 and stays with the
  parent, the merger CANNOT deliver the Ascend-linked asset at any date — V_688347's corporate-structure
  section (which assigns Fab 6 to 华力微) and FR_688347 §3b's "pendency is a W4 catalyst" framing both
  inherit the conflation. Evidence gap; closure demanded (C6).
- **B3 — The injection is a dilution event the mission's files carry at 1/7th of its market cost.** Fetched
  terms: 190,768,392 new A-shares at 43.34 CNY/share to 华虹集团 (controlling parent), 上海集成电路基金,
  大基金二期, 国投先导 — a 关联交易 [S1274;S1275]. Cross-check: 826,790.22万元 ÷ 190,768,392股 = 43.34
  exact. At the valued 324.00 close [S1100;S1101] those shares are worth **CNY 61,808,959,008 ≈ 61.81bn =
  10.98% of the pre-deal market cap — 7.48x the 82.68亿 consideration** VAL/FR use as "≈1.5% of mktcap."
  Counterparties' instant mark-to-market: (324.00−43.34) × 190,768,392 ≈ **CNY 53.54bn** (locked 6/12/36
  months [S1274] — i.e., a dated future overhang, not a neutralization). A ≤75.56亿 companion raise to ≤35
  investors stacks on top [S1275]. No 业绩承诺 appears in either fetched deal relay against a +323.59%
  appraisal [S1274;S1275] — unverified whether one exists at all (gap, C4).
- **B4 — Granting the merger everything it claims, the price still doesn't parse.** Huali earns 5.22亿
  (FY2024) / 5.15亿 (2025年1-8月) [S1275]; the regulated related-party appraisal prices it at 84.8亿 ≈
  **16.2x FY2024 earnings** (11.0x annualized Jan–Aug 2025) — while the acquirer trades at a vendor-
  corroborated 1141.08x TTM [S1100; VAL_688347], ~70x the multiple the state itself just accepted for the
  identical asset class inside the same group. Pro-forma-generous P/E (immediate 100% consolidation, Huali
  at its best-ever annualized profit): (563,023.35M + 190,768,392×324) ÷ (493.41M + 772.5M) = 624,832.31M ÷
  1,265.91M ≈ **493.6x**; on Huali's actual FY2024 profit ≈ **615.4x**. The A-line pays 2.07x the H-line for
  the identical claim [S1102;S1105]; the deal itself issues acquirer stock at 43.34 — 72% below even the
  H-line's ~156.20 CNY-equivalent — implying a consideration-basis acquirer valuation of ~75.31bn, 13.4% of
  the A-market cap. One of those two prices is wrong.
- **B5 — Peak-cycle conditions, margin-squeeze results.** At 106.1% FY2025 utilization [S900–S902], 99.7%
  Q1-2026 utilization (already −4.1pp QoQ) [S1276], guided full-year ASP +10–15% (strong products +20–25%)
  [S1276], and an industry hike wave: USD-basis GM is 11.78% (FY2025) [S1015;S902], 13.0% (Q1-26), guided
  14–16% (Q2-26) [S1276]; attributable NM 2.18% FY2025 [F_688347 §2.3]; the TOTAL consolidated result is a
  LOSS three periods running (FY2024 −1,032.18M; FY2025 −807.14M; Q1-2026 −127.23M CNY [F_688347 §2.3/§4]) —
  attributable profit exists only because minority partners absorb −1,183.75M of FY2025 losses. FCF is
  negative all three years (−1,290.91 / −16,173.70 / −7,865.98M; capex 1.25x/5.48x/2.55x OCF [F_688347 §1]),
  net cash −48.6% in two years. This is what the top of the cycle looks like; FY2024 (revenue −11.36%, GM
  10.24% USD) is what the bottom looked like, two years ago.

---

## 2. Score audit — every cell, supported or corrected

Weights .20/.20/.15/.20/.15/.10. Current row 3,0,2,1,3,3 = 1.85 (arithmetic verified).

| Cell | Current | Supported by cited files? | Red-team proposal | Δ |
|---|---|---|---|---|
| W1 | 3 | **NO** — "entity-scope severed" is written into the cell yet costs nothing; the B-substance sits at an unowned entity and (pending C6) at a fab outside even the merger perimeter | **2** (conditional 1 if Fab-6 exclusion verifies) | −0.20 |
| W2 | 0 | **YES** — verified 0% current; prospective NOT-ESTIMABLE; new Huali financials do not create a Huawei share | 0 (hold; audit note) | 0 |
| W3 | 2 | **WEAK** — both anchor-1 elements literally present across the FY window; consolidated-loss and 3-year-FCF facts absent from the cell basis | **1** | −0.15 |
| W4 | 1 | **CONTESTED basis** — R0.2 letter-rule survives at B, but the aggravator stack (dilution wall, 70x-the-appraisal, mission-extreme multiple on verified-0% exposure) is unlogged | 1 (hold + mandatory log; conditional 0) | 0 |
| W5 | 3 | **WEAK** — peak-cycle GM 12–16% USD with total-basis losses is margin-squeeze evidence, not "defensible"; assigned price-war premise honestly inverted but capacity response is building | **2** | −0.15 |
| W6 | 3 | **NO** — verticalization exposure (cell's own basis) + live company-named BIS action + related-party dilution gate + rising 34.18% top-5 = more than "one arm" | **2** | −0.10 |

All-accepted total: **1.25** (delta −0.60). Conditional floor if C6 verification confirms Fab-6 exclusion
(W1→1, W4→0): **0.85**. Every challenge requires a written response per SCORING_RUBRIC.

**C1 — W1 3→2 (conditional 1).** (i) The cell text itself concedes "entity-scope severed," then maps to the
same 3 an unsevered B would earn. The mission's documented-interpolation convention prices substance, not
just letter: R2.1 (300308, ACCEPTED) held the tier letter B but capped a substance-thin B at 2. 688347's
substance is thinner than 300308's in the dimension that matters: the load-bearing sentence is future-tense
("planning to shift"), rumor-attributed inside the wire itself ("is said to be… other sources said" [S909] —
FR's own reading), and entity-ambiguous ("Hua Hong" = group shorthand; the only entity-precise fact chain,
7nm-at-Fab-6-with-SiCarrier [S908;S909], points at an entity 688347 neither owns nor — per B2 — is buying).
(ii) The A8-discipline inconsistency: W2 severs the entity scope and scores the verified 0%; W1 keeps the
unsevered tier and scores the group's press. Either the ownership hop discounts both cells or neither.
(iii) Ladder consistency: 688981 holds W1=3 where B-grade media names SMIC ITSELF as the current Ascend
fabricator (RB_02: "capacity+yield = chain bottleneck"); 688347 gets the same 3 for a reported future plan
about a sister entity. Same score, categorically weaker link = the cell is measuring the group's press
coverage, not the listco's evidence. (iv) New this session: the company's own deal paperwork — the single
place where the Huali story became securities disclosure — is Huawei/Ascend/7nm-silent in every fetched
rendering [S1274;S1275;S1277], extending V's five silent channels to seven. Against this: S907 does name
"Hua Hong Semiconductor" (the listco) as having "joined the move into advanced production" — a genuine
B-grade row that keeps the letter at B and the floor above 1 pending C6. Propose **2**; if C6 verification
confirms the advanced-node asset is excluded from the deal perimeter, the listco-specific substance drops to
a naming-without-mechanism residue and the cell belongs at **1**.

**C2 — W3 2→1.** Rubric anchor 1 = "deteriorating margins OR persistent cash burn"; both elements are
literally present across the scored FY2023–25 window: (a) attributable NM fell in every year — 11.93% →
2.65% → 2.18% — including the +20.18%-revenue recovery year; GM sits ~8.4–9.5pp below FY2023 on both bases
(27.11→18.72 CNY; 21.31→11.78 USD [F_688347 §2.2]); (b) FCF negative all three years (−1,290.91 /
−16,173.70 / −7,865.98M CNY; cumulative ≈ −25.33bn [F_688347 §1, own arithmetic]), net cash −48.6% in two
years (24,963→12,824M), LT borrowings +45% (13,503→19,590M) [F_688347 §2.4]. (c) The consolidated TOTAL
result is a loss in FY2024, FY2025, and Q1-2026 (−1,032.18 / −807.14 / −127.23M) — the enterprise loses
money and the +376.61M headline survives only via −1,183.75M of minority loss absorption [F_688347
§2.3/§4]; neither SCORES_v2's cell basis nor FR §5's W3 line carries this fact. (d) The burn is scheduled to
continue: FAB9 reaches planned capacity end-2026/early-2027 [S1276], FAB9A targets full production early
2027 [S913] — the depreciation wall lands into a guided 14–16% GM [S1276]. Precedent fit: R1.3 (688629,
ACCEPTED 3→2) required only ONE genuinely-present anchor-1 element alongside RISING margins; 688347 has both
elements with FALLING window margins. Mitigants (strongly positive OCF, net-cash balance) are real and are
the likely rebuttal path along with the Q1/Q2-26 recovery prints — but they are anchor-5 fragments, and the
rubric's 1 is disjunctive. Propose **1**; if held at 2, the written response must log the 3-year FCF stack,
the 5.48x FY2024 capex/OCF ratio, and the consolidated-loss fact into the cell basis.

**C3 — W5 3→2 (documented interpolation).** Honesty first: the assigned "price-war environment" premise is
inverted by current evidence — 2026 is an UP-cycle (8-inch utilization ~88–90%, hikes 5–15%, TrendForce
expecting the hike effect to extend into 2027; Morgan Stanley raising Hua Hong's target on BCD/AI-power
demand — all search-snippet grade, marked as such, none load-bearing). The attack therefore stands on what
the up-cycle REVEALS: at >100% utilization, +10–15% guided ASP, and maximum policy tailwind, this asset base
produces 11.8–13.0% USD GM (guided 14–16%) and ~2–3% attributable NM with total-basis consolidated losses
[S1015;S1276;F_688347] — the prior peak (FY2023) managed only 21.31% USD GM, and the demonstrated down-cycle
(FY2024: revenue −11.36%, GM 10.24%) is two years old. A layer whose PEAK economics are mid-teens gross and
whose position must be defended with capex at 1.25–5.48x OCF and 11.4% R&D intensity [F_688347] fits the
rubric's margin-squeeze pole better than "defensible." Within-layer position (the adjudicated 002281/300308
method): the foundry layer's scarcity notch — 7nm DUV, "capacity+yield = chain bottleneck" [RB_02] — belongs
to 688981 (W5=4); 688347's own base is specialty-mature where capacity is being added on every side,
including by the thesis itself (the injected Fab 5 is +38k wpm INTO 65/55/40nm [S1277]; FAB9A +83k wpm
[S913]; utilization already slipped to 99.7%, −4.1pp QoQ, as FAB9 ramps [S1276]) — the hike wave is the
standard setup for the next capacity glut, and the 2026 hikes are themselves partly cost-push (the same
pattern the mission documented for CCL). "One step below 688981's scarcity position" (the cell's own basis)
that ALSO exhibits anchor-1 peak-cycle economics lands at **2**, not 3.

**C4 — W6 3→2 (documented interpolation).** The current 3 reads "one arm" (verticalization/policy) and
stops. Count the live arms: (i) verticalization exposure — the cell's own basis (SiCarrier/Huawei-adjacent
vector; see §3); (ii) policy — not a common-mode abstraction but a MATERIALIZED, company-named action: BIS
is-informed letters directing AMAT/Lam/KLA to halt some tool shipments to "China No.2 Foundry Hua Hong"
(April 2026) [S909], aimed at the exact capacity-expansion program (FAB9/9A ramp) the price requires; (iii)
a related-party dilution gate this session quantifies: +190,768,392 shares (+10.98%) at 43.34 to the
controlling parent and three state funds — CNY 61.81bn at market for an 84.8亿-appraised asset, +323.59%
over book, with NO profit commitment found in any fetched relay [S1274;S1275] (gap: if the appraisal is
income-based, CSRC rules ordinarily require 业绩承诺 — its absence from both fetched deal relays is either a
disclosure hole or an uncushioned integration risk; the written response must establish which), plus a
≤75.56亿 companion raise and a dated post-lock overhang (191M shares carried at 43.34 vs 324.00 market,
locks 6/12/36 months [S1274]); (iv) CSRC registration is a binary gate still open at audit date ("仅待注册
批复" [S913]); (v) customer concentration is not yet "one material concentration" (max single 8.56%) but has
risen every year — 25.66% → 30.09% → 34.18% [F_688347 §3] — and the fetched record adds a perimeter
discrepancy (97.4988% [S1275] vs "100%股权" [S1277] — recorded, not resolved). Anchor 3 tolerates ONE of
concentration/verticalization; 688347 carries verticalization PLUS live policy action PLUS a self-inflicted
execution/dilution stack. Between 3 and 1 → **2**.

**C5 — W4: hold 1 under protest + mandatory aggravator log; conditional 0.** Under R0.2 the 0/1 boundary
keys on the link's tier letter (B → 1 when PRICED-FOR-PERFECTION), so 1 survives my W1=2 (letter unchanged).
Three aggravators must enter the answer key in writing: (a) this is the mission's most extreme multiple
(1141.08x TTM, vendor-corroborated three ways [S1100; VAL_688347]) sitting on the mission's only
verified-0% current exposure [V_688347] — maximum price on minimum verified linkage; (b) the deal framing in
VAL/FR ("≈1.5% of mktcap") understates the event: the market cost of the share consideration is 61.81bn =
10.98% of mktcap (B3), the count expands +10.98% before the companion raise, and pro-forma-generous P/E
still lands at ~494–615x (B4) — the re-rating cannot even be arbitraged by the injection it is nominally
about; (c) the same group just priced foundry earnings at 11.0–16.2x via regulated appraisal [S1275] — an
in-group, same-week-era valuation datum ~70x below the acquirer's market multiple. Conditional: if C6
verification confirms the Ascend-linked asset is outside the deal perimeter AND the orchestrator downgrades
the listco-specific link substance to C-grade residue, R0.2's own letter-logic yields **0**.

**C6 — Defect + mandatory verification (R0.4 class).** Three items. (a) **V_688347 entity conflation:** V's
corporate-structure section assigns BOTH Fab 5 and Fab 6 to 上海华力微电子; the inquiry-reply relay
(snippet) assigns Fab 6 to 上海华力集成电路制造有限公司 ("华力二期," 28/22nm), excluded from the deal as
非同业竞争 — and every fetched deal document's perimeter (65/55/40nm only, 38k wpm, 84.8亿 appraisal on a
~50亿-revenue/5.2亿-profit business [S1274;S1275;S1277]) corroborates the Fab-5-only reading arithmetically:
a perimeter containing a 28/22nm megafab plus 7nm R&D would not appraise at 84.8亿 against 20.0亿 book. The
orchestrator MUST fetch the full 问询回复/报告书 text (candidate URLs surfaced this session: zqrb epaper
2026-03-31 D321 PDF; xueqiu-hosted 草案 PDF; qq finance PDF 1224915484) or an intact HTML relay, and rule on
the perimeter BEFORE Gate PG2 — W1, W4, and the answer key's entire "merger closes the gap" catalyst
language depend on it. (b) **VAL/FR "deal ≈1.5% of mktcap":** true only of the consideration value; as a
measure of the deal's size to existing holders it is off by 7.48x (B3). The figure should be restated or
双-footnoted in both files' narratives. (c) **SCORES_v2 W2 cell basis** "merger pendency is W4 catalyst not
W2 share": the catalyst framing presumes the merger delivers the Ascend-linked asset; per (a) that premise
is unverified and currently disfavored by every fetched deal document. Not a score change by itself — a
correctness-of-record demand.

**W2 = 0 — CONFIRMED (audit note only).** Verified 0% current-consolidated exposure stands [V_688347].
This session adds Huali's actual scale: FY2024 revenue 49.88亿 ≈ 22.4% of a pro-forma combined
(49.88/(172.91+49.88)); annualized Jan–Aug 2025 ≈ 22.9% [S1275; own arithmetic]. Post-close, any Huawei
share would sit inside that ~22–23% slice with no disclosed split → NOT-ESTIMABLE survives consolidation;
and if C6(a) verifies, the 7nm slice of the acquired perimeter is 0% by construction. Any future W2 upgrade
requires a filing-grade Huawei-linked share of the CONSOLIDATED entity, not deal completion alone.

---

## 3. Verticalization test

The in-house-HBM precedent's adjudicated meaning (R0.3) is demonstrated appetite to internalize choke
points, and at the foundry layer Huawei's revealed method is already more than appetite: the 7nm line at
Fab 6 runs "with support from Huawei-backed SiCarrier" [S908;S909] — Huawei's instrument owns the equipment
relationship inside the fab — and Reuters casts Huawei as the ALLOCATOR of production ("planning to shift
part of its AI chip production from SMIC to Hua Hong" [S909]): foundries in this chain are interchangeable
capacity slots that Huawei assigns, not partners with pricing power. If Huawei/SiCarrier stands up captive
advanced-node capacity — the direct extension of the HBM precedent, with SiCarrier already fab-adjacent —
the marginal allocation reverses first, and 688347's version of the story is the most marginal in the chain:
it is future-tense, rumor-attributed, and (per C6) attached to a fab the listco is not even buying, so the
"shift" can be unwound by a single unreported decision, with no contract, filing, or customer line anywhere
in 688347's disclosures to mark its passing [V_688347]. What the listco actually sells into the Ascend
economy — mature-node BCD/power adjacency, the FAB9A "AI电源芯片" 83k wpm plan with no customer attribution
[S913] — is precisely the layer where Huawei's qualification power is cheapest to exercise: multiple
domestic mature foundries (SMIC's own mature lines, Nexchip-class entrants, the group's own Fab 5 now inside
the listco) can be second-sourced at Huawei's discretion, or bypassed outright once SiCarrier-equipped
captive capacity exists. The end state of verticalization here is not Huawei buying a laminate reactor — it
is Huawei never needing to appear in Hua Hong's customer table at all: 688347 holds 12–16%-gross-margin
capacity built at 2.55–5.48x OCF capex for a demand plan it cannot name, while the group retains the one
asset (Fab 6) whose scarcity the A-share price is actually paying for.

---

## 4. Common-mode test

**US policy reversal (Nvidia-class supply resumes to China).** The 1141x multiple is, per VAL_688347's own
implied-expectations reading, a "China-self-sufficiency/scarcity premium… rather than a precise,
information-driven Ascend bet." That premium is the single most reversal-sensitive object in the portfolio:
688347's verified current Ascend revenue is 0% [V_688347], so the ENTIRE excess multiple is narrative beta
shared with the foundry/equipment cohort (688981, 002371) — and 688347 has the longest fall (highest
multiple in the mission on the weakest verified linkage). The A/H structure doubles the exposure: the +107%
A-premium over an H-line that already prices the same cash flows at ~156.20 CNY-equivalent [S1102;S1105] is
the same domestic-scarcity artifact the mission documented for SMIC (+128%); a STAR risk-appetite break
compresses both premia simultaneously — a ~−52% repricing to H-parity on zero fundamental news.
**US policy escalation (the other tail).** Already live and company-named: April-2026 BIS tool-shipment
action against "China No.2 Foundry Hua Hong" [S909]. The same policy axis that inflates the scarcity
narrative constrains the FAB9/9A tool supply the growth story requires — both tails of US policy hurt this
name, a property shared with 688981 but priced at ~4.6x 688981's TTM multiple (1141x vs 247x [VAL_688981;
VAL_688347], cell-consistency cite only).
**Huawei demand shock.** An Ascend volume cut transmits to the whole universe; 688347's channel is
anticipatory (a reported reallocation plan that simply fails to materialize) plus mature-node AI-power
adjacency [S913] — it dies silently, with no disclosed customer line to mark it, while the same shock hits
688981's actual production and the equipment names' order books. Foundry-layer common-mode with 688981 is
already flagged in V_688347 (A20 group); this file adds that the two names' shock topology differs — SMIC
loses revenue it has, Hua Hong loses revenue it never booked but fully priced.
**Merger/securities-policy common-mode.** The consolidation wave (中芯北方 integration at SMIC; 华力微 at
Hua Hong — both pending) is itself policy-sponsored; a CSRC posture shift on STAR-market related-party
injections stalls both, and 688347 carries the added idiosyncratic layer: registration-gate timing, the
97.4988%-vs-100% perimeter discrepancy [S1275;S1277], and a 75.56亿 companion raise that must clear at
post-run-up prices.

---

## 5. Five falsifiable checks

1. **CSRC 注册批复 and closing by 2026-12-31** (guided: H2-2026 completion [S913;S1276]). Registration
   granted and deal closed on schedule → BULL (execution prong of C4 retires). Registration still pending
   at year-end, terms revised, or deal withdrawn → BEAR (C4 vindicated; the answer key's catalyst date
   fails).
2. **Deal-perimeter verification — the C6 gate, checkable immediately and re-checkable at first
   consolidation (first post-close periodic report, no later than the FY2026 annual report ~2027-03/04).**
   Full 问询回复/报告书 text or the consolidated scope shows any 28/22nm-or-below asset (华力集成/Fab 6)
   inside 688347's perimeter → BULL and B2/C1-conditional withdrawn. Perimeter confirms Fab-5-only
   65/55/40nm → BEAR (the Ascend story structurally cannot reach the listco through this deal; W1
   conditional-1 and W4 conditional-0 trigger).
3. **FY2026 annual report (due ~2027-03/04): company voice and customer table.** First-ever 华为/昇腾
   naming in own disclosure, or a new ≥5% customer whose description matches an AI-chip allocation → BULL
   (W1 upgrade path opens). A fourth consecutive Huawei-silent vintage with a stable non-Huawei top-5 →
   BEAR (B1 compounds; the 2024 Nvidia-naming asymmetry [S912] gets one year heavier).
4. **Margin through the depreciation wall: Q2-2026 print (~2026-08) and Q3-2026 print (~2026-11) vs the
   14–16% GM guide [S1276], with FAB9 ramping to planned capacity end-2026/early-2027.** GM lands ≥14% both
   quarters with utilization ≥95% while FAB9 depreciation loads → BULL (C2's forward leg weakens; hold-2
   defensible). GM <14% in either quarter or utilization <95% → BEAR (C2 vindicated: the recovery was
   price-hike froth ahead of a depreciation wall).
5. **Mature-node pricing cadence through 2027-06-30** (TrendForce/财联社 foundry trackers; the up-cycle
   view expects hike effects to extend into 2027 — snippet-grade this session). Hikes hold or extend while
   industry 8-inch utilization stays ≥88–90% → BULL (W5=3 survives at the layer level). First downward
   price adjustment, or utilization rollover as new capacity lands (incl. the injected 38k wpm and FAB9A's
   83k wpm [S1277;S913]) → BEAR (C3 vindicated: peak-cycle arithmetic becomes trough-cycle arithmetic under
   a 1141x multiple).

---

## Search trail (zh-language, per rule 7)

Queries: 「华虹公司 发行股份购买资产 华力微 97.4988% 发行价格 元/股 报告书」, 「成熟制程 晶圆代工 价格战 产能
过剩 2026 华虹 降价」, 「华虹 2026年 一季度 业绩说明会 毛利率 指引 折旧 FAB9 无锡 爬坡」, 「华虹公司 重组
华力微 上交所 问询函 回复 先进工艺 28纳米 审核意见」. Fetched (4/4 budget): [S1274] stockstar 草案摘要
(PARTIAL — encoding-corrupted; only legible passages used); [S1275] 腾讯新闻/芯智讯 deal explainer (parsed);
[S1276] 新浪/光大证券 1Q26 点评 (parsed); [S1277] 新浪财经头条 问询回复 piece (parsed). Snippet-only items
used as color and so marked, never load-bearing: the Fab-6/华力集成 exclusion passage (search summary of the
问询回复 — the C6 verification target); issue-pricing basis "定价基准日前120个交易日均价的80%"; 8-inch
industry utilization 88–90% and 5–15% hikes extending to 2027 (TrendForce relays); Morgan Stanley/Goldman
target-price raises; FAB9 "产能上线约50%". Not found at any tier: any source tying 688347's own consolidated
revenue to Huawei/Ascend (consistent with V_688347's 0% finding); any 业绩承诺 for the Huali injection
(absence in two fetched deal relays — flagged as gap, not asserted as fact).

## Sources this session

[S1274] 证券之星(stockstar.com) 公告转载: 华虹半导体有限公司发行股份购买资产并募集配套资金暨关联交易报告书
  （草案）摘要 — 2025-12-31, tier 3, fetched (PARTIAL — encoding-corrupted; legible: 190,768,392股,
  826,790.22万元, 848,000.00万元/+323.59%, 锁定期6/12/36个月, 65/55nm、40nm 12英寸 language; no
  华为/昇腾/7nm in readable text; full-text verification demanded per C6).
[S1275] 腾讯新闻(news.qq.com) 载 芯智讯: 82.68亿元，华虹半导体拟收购华力微97.4988%股权 — 2026-01-04,
  tier 3, fetched (发行价43.34元/股; 1.91亿股; 四名交易对方; 华力微 FY2023 25.79亿/−3.72亿, FY2024
  49.88亿/5.22亿, 2025年1-8月 34.31亿/5.15亿; 配套募资≤75.56亿; 华为/昇腾/7nm 完全未提及).
[S1276] 新浪财经 转 光大证券(付天姿/董馨悦): 华虹半导体（1347.HK）1Q26业绩点评 — 2026-05-19, tier 3,
  fetched (2Q26指引收入6.90-7.00亿美元/毛利率14.0%-16.0%; 产能利用率99.7% −4.1pp QoQ; ASP指引+10-15%;
  FAB9爬坡时间表; 华力微交割预计2026年下半年; 无华为/昇腾).
[S1277] 新浪财经·财经头条: 华虹公司：对资产重组审核问询函进行回复，本次交易拟收购华力微100%股权 —
  2026-05-29, tier 3, fetched (问询函2026-04-02下发; "新增3.8万片/月的65/55nm、40nm产能"; 纯成熟制程
  披露口径; 无Fab 6/华为/昇腾/先进制程表述; 100% vs 97.4988% 口径差异 recorded-not-resolved).
Full entries: 90_BIBLIOGRAPHY/frags/rt2_688347.json (S1278–S1281 unused). All other [S###] cites reference
entries already ledgered by V_/F_/VAL_/FR_688347 (pp1/pp2/pp3/fr frags) or VAL_688981/RB_02 as noted.
