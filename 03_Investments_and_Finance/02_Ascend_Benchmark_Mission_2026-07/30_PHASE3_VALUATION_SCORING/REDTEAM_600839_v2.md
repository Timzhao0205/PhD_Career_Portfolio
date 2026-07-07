Educational benchmark for a paper-trading learning exercise. Simulated allocations, not investment advice or recommendations.

# REDTEAM_600839_v2 — re-red-team (accuracy patch), 四川长虹 (SSE 600839). Critic date 2026-07-07.

Target: the CURRENT SCORES_v2.csv row — W1=1, W2=0, W3=2, W4=3, W5=1, W6=4, total 1.65 (v1 2.40, Δ−0.75
via FR_600839's reversal of the R0.1 consistency rescore). Mandate: attack in BOTH directions — (A) was
the demotion itself flawed (did FR miss filing-grade evidence that the 长虹佳华 ICT segment is
predominantly Huawei-linked)? (B) does even the demoted row still overcredit? Inputs: V_600839.md,
F_600839.md, VAL_600839.md, FR_600839.md, REDTEAM_RESPONSES.md R0.1, SCORES_v2.csv. Budget: 4/4
WebFetches used. New sources [S1250]–[S1255] in 90_BIBLIOGRAPHY/frags/rt2_600839.json (2 fetched
tier-≤2, 1 fetched tier-1 HKEX document, 1 tier-1 fetch-failed-password-protected, 1 located-not-fetched,
1 snippet-marked; all statuses recorded honestly). Chinese-language search used throughout.

## 0. Headline: the direction-A attack was run with the subsidiary's own numbers — and it FAILED, which strengthens the demotion; the same fetches overturn three OTHER cells' premises

This critic did what neither V, F, nor FR did: went to 长虹佳华's own disclosure layer. Three new facts:

1. **The ICT segment IS 长虹佳华, ~1:1.** CJH FY2025 revenue HK$438.26亿 [S1250, results dated
   2026-03-31] vs 600839's ICT综合服务 FY2025 ¥406.43亿 [S257;S258;S1174]. Implied cross-rate
   40,643/43,826 = 0.9274 CNY/HKD — squarely a plausible 2025-average HKD/CNY rate, i.e. the segment
   and the subsidiary are the same book to within FX/rounding (≥~99%). The mission had only assumed
   this ("rolls up 长虹佳华, among possibly other ICT units", F §5).
2. **The segment is NOT a Huawei-enterprise-ICT block — it is 43% CONSUMER-product distribution.**
   CJH's own FY2025 分部 split [S1250]: ICT消费者产品分销 HK$188.19亿 (+5.37%; 42.94% of CJH; 业务溢利
   2.81亿, margin 1.49%); ICT企业产品分销 HK$161.05亿 (+13.68%; 36.75%; 溢利 4.24亿, margin 2.63%);
   其他业务 HK$89.02亿 (+11.85%; 20.31%; 溢利 1.04亿, margin 1.17%). Sum exact (438.26). In group
   terms: enterprise-ICT distribution ≈ 36.75% × 37.35% ≈ **13.7% of 600839 revenue**; consumer
   distribution ≈ 16.0%; other ≈ 7.6%.
3. **The Huawei link is real at company voice, including AI hardware.** CJH's own website Huawei brand
   page [S1251, fetched 2026-07-07, undated marketing page] lists distributed Huawei product lines
   including 智能边缘设备 / **AI服务器 / AI加速卡** under 人工智能. No 昇腾/Atlas/鲲鹏 wording, no
   share, no authorization tier. Zero 华为 mentions anywhere in CJH's FY2025 results coverage [S1250].
   Also: CJH's stock code is **3991** (main board) per its own HKEX document [S1252] — V_600839's
   "8016.HK" label is a stale GEM-era code carried from the prior corpus, evidence that no CJH-side
   document had been touched before this patch.

Consequence for direction A: R0.1's premise ("verified ~37.35%-of-revenue Huawei-ICT distribution
segment... filing-grade Huawei-linked point in the >30% band") is now **arithmetically unrecoverable**,
not merely unattributed. Even granting 100% Huawei share of the entire enterprise sleeve, the ceiling is
~13.7% of group revenue — below the >30% band by ~2.7x. FR's W2 demotion survives its strongest
challenge and comes out stronger. But facts 1–3 simultaneously impeach the current row's W1 ("tier C
only"), W6 ("common-mode ~nil", "confined... distribution sleeve"), and the W2 cell's cited basis. The
row is directionally right and cell-wise wrong.

## 1. Strongest bear case against the current row's correctness (5 bullets)

1. **W2's cited basis is stale even though its integer is right.** The cell rests on "no fetched source
   breaks out a Huawei-specific share" (FR §1) — an absence argument. A tier-1-grade decomposition now
   EXISTS [S1250] and settles the question structurally: 42.94% of the "Huawei-ICT" segment is consumer
   -product distribution, the enterprise sleeve caps any Huawei-enterprise share at ~13.7% of group
   revenue, and the Huawei sub-share of both sleeves remains unattributed (multi-band span → 0 per
   R0.1). Meanwhile the untested filing-grade path to W2=3 is documented but unfetched: snippet-grade
   claims of "65%+ of CJH revenue from Huawei-authorized distribution" and "IT分销 top-5 supplier
   purchases 51.94% (2023)" sit in a password-protected parent bond doc [S1253] and its 募集说明书
   sibling [S1254] — 65% × 37.35% ≈ 24.3% of group revenue would land in the 10–30 band. Evidence gap,
   designated check #1.
2. **W1=1 is factually superseded.** The FR justification line — "surviving generic-distribution link is
   snippet/tier-C only" — is no longer true: the link now has company-voice support naming AI-hardware
   distribution [S1251] plus the subsidiary's own tier-1 filing trail [S1250;S1252]. The mission's own
   precedent (FR_002436: official generic-Huawei company statement, not Ascend-specific → W1=2,
   documented interpolation) maps this to 2, not 1.
3. **W4=3 (NEUTRAL) survives only on the stalest, least-recurring earnings basis.** On-file multiple
   ladder: 30.48x FY2025 headline → 40.63x TTM → 76.52x current-quarter-annualized (both vendors' own
   field, [S677;S678] via VAL) → ≈332.6x FY2025 core-扣非 (FR §3's own arithmetic). 90.83% of FY2025
   headline attributable NP is non-recurring ((988.89−90.64)/988.89, F §2.0), and both the latest year
   and latest quarter printed 扣非 declines of −78.35%/−78.09% (F §2.0/§6). Names with 177x and 231x
   ttm carried PRICED-FOR-PERFECTION flags in this mission (VAL_002281, VAL_301018); 600839's only
   recurring-basis multiples sit at 246x EV/core to 333x P/core. The FR's shield — "PFP requires a
   priced growth story" — is an extra-rubric criterion; W4's anchor text prices expectations, not
   narratives.
4. **W6=4 runs a double standard on the same unknown.** In W2, Huawei dependence is unknowable →
   score 0; in W6, the same dependence is "~nil" → policy common-mode ~nil → score 4. The V §B debunk
   verifies non-dependence on 华鲲振宇 server manufacturing only — it says nothing about Huawei
   distribution dependence, which is real at company voice [S1251] and unquantified. Add: the top-5
   customer table is MISSING all 3 years (F §3) while the anchor's first clause is literally
   "diversified customers"; and a live concentration-RAISING corporate action is on file — the CJH
   privatization (60.13% → toward 100%, [S260], in approval 2026-05-13 [S257;S258]) recaptures
   ≈¥1.48亿 of minority profit (39.87% × HK$4.01亿 × 0.9274 [S1250]) ≈ a +15% uplift to FY2025
   attributable NP, ALL of it Huawei-channel-linked economics, while extinguishing CJH's own HKEX
   disclosure stream. The direct in-universe comp cell — 000034, a Huawei-ICT distributor with BETTER
   disclosure and a filing-grade (if small) Huawei point — carries W6=3.
5. **The channel the row treats as a side-sleeve is plausibly 600839's entire core-profit engine.**
   Bounded illustration (HKFRS-vs-PRC-GAAP and FX caveats flagged): CJH attributable profit HK$4.01亿
   ≈ ¥3.72亿 [S1250]; 600839's 60.13% share ≈ ¥2.24亿 ≈ 22.6% of group attributable NP (¥9.89亿) —
   and ≈ 2.5x the group's ENTIRE FY2025 扣非 core profit (¥0.91亿 [S1175]). Ex-CJH, 600839's core
   operations approximately break even or worse in FY2025. A Huawei-channel shock is therefore a
   core-earnings event, not the "confined to the unquantified distribution sleeve" footnote in the
   W6 rationale — while remaining exactly as NOT-ESTIMABLE for W2 as the row says. The row's cells do
   not share one consistent model of this channel.

## 2. Score audit — every cell, current → verdict → proposed

| Cell | Cur | Verdict | Proposed | Reasoning |
|---|---|---|---|---|
| W1 | 1 | **CHALLENGE** | **2** | "Tier C only" is superseded by fetched company-voice evidence: CJH's own site names Huawei AI服务器/AI加速卡 distribution [S1251]; subsidiary's tier-1 trail [S1250;S1252] confirms the business at filing grade (Huawei-silent, which caps it). Not Ascend-specific, undated page, subsidiary voice not 600839 IR → not 3. Exact precedent: FR_002436 W1=2 (official generic-Huawei statement above C-floor, documented interpolation). Also correct V's stale "8016.HK" → 3991 [S1252] in the answer key. |
| W2 | 0 | **CONFIRM — but replace the cell's basis and purge R0.1 from its source chain** | **0** | Direction-A attack run and failed: segment ≈ CJH 1:1 (0.9274 implied rate); CJH's own split shows 42.94% consumer / 36.75% enterprise / 20.31% other [S1250], so the R0.1 ">30% band point" is arithmetically dead (enterprise ceiling ≈13.7% of group revenue) and any real Huawei share spans the 10% boundary → NOT-ESTIMABLE → 0 per R0.1's own rule. Demand 1: cite [S1250] as the cell's evidence, not the absence argument. Demand 2: the cell_sources string still carries "REDTEAM_RESPONSES(R0.1 consistency rescore)" — an invalidated ruling — annotate as superseded. Recoverable to 3 ONLY by a filing-grade Huawei share ≥26.8% of CJH revenue (= 10% of group): see check #1. |
| W3 | 2 | CONFIRM (challenge considered, declined) | 2 | Anchor-1 margin prong is literally present (GM 11.18→10.02→9.42; 扣非 −78.35% FY2025, −78.09% Q1-2026; OCF down 3 straight years) but the R1.3 convention (anchor-1 element + offsetting positives → 2) is satisfied by net cash +¥7,813M and positive OCF all 3 years [F §1/§2.4] — the offsets 600498 lacked when its W3 went to 1. Consistent. |
| W4 | 3 | **CHALLENGE** | **1** | The NEUTRAL flag is denominator-dependent: it holds at 30.48x/40.63x (headline/TTM) and fails at 76.52x (vendors' own current-run-rate field [S677;S678]) and ≈332.6x core-扣非 (FR §3). With 90.83% of FY2025 headline NP non-recurring and the two most recent prints showing core profit −78% while price implies ¥741.9M TTM earnings continuing, the market cap embeds either indefinite non-recurring gains or a sharp core recovery — a priced expectation. Mission precedent flags PFP at 177x/231x ttm (002281, 301018 cells). P/S 0.28x is not exculpatory: VAL itself rules P/S "not on its own a valuation signal" for this mix. If PFP is accepted, the tier question follows: the debunked narrative is unpriced (VAL) and the surviving link is A/B-at-generic-Huawei under this file's W1 finding → 1, not 0 (000628's "PFP on debunked narrative → 0" does not transfer because there the price rode the debunked story). If the orchestrator holds NEUTRAL, the written response must reconcile why 76.52x-run-rate/333x-core with a 91%-non-recurring base is "unremarkable" when 177x/231x were not. |
| W5 | 1 | CONFIRM — strengthened | 1 | New tier-1-grade confirmation of anchor-1 economics from inside the layer: CJH blended business-profit margin 1.85% (8.09/438.26), enterprise sleeve 2.63%, consumer 1.49% [S1250]; segment GM 3.43%, lowest of 8 (F §5). Commoditized distribution margin-squeeze, verbatim anchor. |
| W6 | 4 | **CHALLENGE** | **3** | Four independent grounds: (i) symmetry — W2 scores the Huawei share as unknowable; W6 may not score the same unknown as ~nil ("symmetric snippet discipline" cuts both ways); (ii) the anchor's "diversified customers" clause is unsupported — top-5 customer table MISSING ×3 FYs (F §3), and the rubric's own rule is "a cell that cannot be supported scores 0, not a guess" — segment diversification (real, 8 segments, max 41.72%) rescues it to 3, not 4; (iii) verticalization/channel risk is understated: the sleeve is ≈22.6% of attributable NP and ≈2.5x group core profit (§1 bullet 5), Huawei-silent in its own results [S1250], at 1.85% business-profit margin — no buffer against a Huawei channel-policy shift; (iv) consistency: 000034 (same layer, same vendor dependence, better disclosure) sits at W6=3; the privatization concentrates the exposure further (+15% attributable-NP recapture, all Huawei-channel-linked [S260;S1250]). One material concentration/verticalization exposure = anchor 3. |

**Proposed row if all challenges accepted: 2, 0, 2, 1, 1, 3 → total = 0.40+0.00+0.30+0.20+0.15+0.30 =
1.35** (vs current 1.65; net further DOWN despite the W1 upgrade — the two directions of this
re-red-team do not cancel, they both land). Challenges requiring written response per rubric rule:
**W1 (1→2), W4 (3→1), W6 (4→3), W2 (integer confirmed; basis/citation correction demanded).**

## 3. Verticalization test — what if Huawei internalizes the layer (precedent: in-house HBM)

Distribution is the cheapest layer Huawei can internalize: unlike HBM it needs no fab, only a channel
-policy decision (direct/named-account fulfillment, 华为商城/云直销, or simply licensing more 总代s and
squeezing spreads), and Huawei's demonstrated appetite (R0.3's reading of the in-house-HBM precedent)
plus its practice of handling the largest Ascend deployments directly means the highest-value flows may
never enter distributor books at all. For 600839 the exposure is asymmetric in exactly the way the
current W6=4 rationale misses: revenue optics would lose some slice of a 37.35% segment, which sounds
survivable, but the segment IS 长虹佳华 [S1250], 长虹佳华 is ≈22.6% of attributable NP and ≈2.5x group
core 扣非 profit (§1 bullet 5), and its business-profit margins (1.49–2.63% by sleeve, 1.85% blended
[S1250]) provide zero absorption capacity — a 总代-license addition or spread cut of ~2pp erases the
sleeve's profit entirely. Post-privatization, 600839 owns ~100% of that P&L instead of 60.13% [S260],
so the same shock scales up ~1.66x at the attributable line. And because the 华鲲振宇 channel is
verified-false [V §B] and the equity look-through is ≈0.11% illustrative [V §C], the distribution sleeve
is 600839's ONLY live Huawei linkage: verticalization does not merely dent the thesis, it deletes the
last reason this name is in an Ascend-benchmark universe at all, reverting it to a 0.3–0.9%-net-margin
appliance conglomerate whose core operations ex-CJH approximately broke even in FY2025.

## 4. Common-mode test — policy reversal / Huawei demand shock shared with other portfolio names

Split the two shocks; the current row conflates them. (a) **Ascend-policy reversal** (e.g. US re-licenses
competitive NVIDIA China SKUs, or Beijing slows domestic-substitution procurement): 600839's verified
Ascend exposure is ~0 (tier-A debunk [V §B]; no Ascend attribution anywhere in the surviving channel
[S1174;S1250]), so this shock largely bypasses it — the one prong of W6's reasoning that survives audit,
and it makes 600839 structurally anti-correlated to the portfolio's Ascend-beta names in a
policy-reversal scenario. (b) **Generic Huawei demand/channel shock** (enterprise capex cut, renewed
handset supply constraints, channel-policy shift): this hits CJH's consumer AND enterprise distribution
volumes simultaneously [S1250] and is SHARED with every distribution/integration-layer name in the book
— the same Huawei enterprise-channel demand pool feeds 000034's cells, and adjacent services names
(002261, 301236 cells) monetize the same ecosystem budget. In that scenario 600839's supposed
diversification does not diversify the scored exposure: the appliance 58% of revenue carries ~0.3–0.9%
net margin economics, so the P&L-relevant book is concentrated in exactly the common-mode sleeve. Net:
W6's "low policy common-mode" is defensible only for shock (a); shock (b) is a material, shared,
unpriced common mode — one more reason the cell reads 3, not 4.

## 5. Five falsifiable checks (observable event + date + which side it supports)

1. **CJH FY2025 annual report, Directors' Report "major customers and suppliers" section** (published
   on HKEX ~2026-04 if still listed — locate via hkexnews.hk or changhongit.com/investor/list-466.html;
   check by 2026-07-31; the parent bond 募集说明书 [S1254] is the fallback carrier). Largest-supplier
   share of purchases ≥~50% + any filing-grade Huawei naming → supports direction A: W2 resurrection
   toward 3 (65%-snippet path, 24.3% of group revenue, 10–30 band) and W1→3. Largest supplier <30% or
   unnamed → confirms multi-vendor NOT-ESTIMABLE → current W2=0 stands permanently.
2. **CJH privatization completion or lapse** (600839 SSE 公告 + HKEX delisting notice; watch through
   2026-12-31). Completion → stake 60.13%→~100%, ≈+15% attributable-NP recapture, Huawei-channel
   concentration UP → supports W6=3 (this critique). Lapse/withdrawal → concentration static and CJH's
   own disclosure stream survives → weakens check-density argument, W6=4 more defensible.
3. **600839 2026 半年度报告 (due by 2026-08-31): ICT segment growth and any 华为/昇腾 attribution in
   the segment narrative.** Segment growth <+5% YoY (vs FY2025's +10.19%) while Ascend-chain names
   accelerate → confirms the segment is not an Ascend beneficiary → demotion side. Segment >+15% WITH
   the filing itself naming 华为/算力 demand → supports W1/W2 upgrades (direction A).
4. **Same 半年报, H1-2026 扣非净利润.** 扣非 still down >50% YoY (Q1 ran −78.09% [F §6]) → confirms the
   core-earnings collapse is persistent → supports W4=1 (this critique). 扣非 recovery to ≥~¥2.0亿
   half-year (≈FY2024 run-rate) → headline multiple re-anchors to a real recurring base → W4=3 NEUTRAL
   defensible.
5. **Huawei China channel-policy event during 2026 (check quarterly through 2026-12-31, Chinese-language
   sources: 华为官网渠道公告 / 通信产业报 / 财联社).** Huawei adds mainland 总经销商 for
   computing/storage/enterprise lines or moves Ascend/Atlas fulfillment direct → verticalization prong
   live → supports W6≤3. Conversely, a NEW dated CJH-specific 昇腾/Atlas distribution authorization
   announced by Huawei or CJH → first Ascend-specific link at tier ≤B → supports W1→3 and reopens W2.

## Sources (new this file; full entries in 90_BIBLIOGRAPHY/frags/rt2_600839.json)

- [S1250] 格隆汇 via 网易, CJH (03991.HK) FY2025 annual results (2026-03-31): HK$438.26亿 rev +9.6%;
  attributable profit HK$4.01亿 +5.69%; 3-segment split 188.19/161.05/89.02亿 with 业务溢利
  2.81/4.24/1.04亿; zero 华为/昇腾 mentions. tier 3, zh, fetched 2026-07-07.
- [S1251] 长虹佳华官网华为品牌页: distributed lines include 智能边缘设备/AI服务器/AI加速卡; no
  昇腾/Atlas/鲲鹏, no share, undated. tier 2 (company official website), zh, fetched 2026-07-07.
- [S1252] CJH AGM proxy form, HKEXnews 2025-04-17: Stock Code 3991; FY2024 final dividend HK$0.05.
  tier 1 (company HKEX document), fetched 2026-07-07.
- [S1253] 中信证券主承销商核查意见 (长虹控股集团 2024 债券), SSE static PDF, 130pp, 2024-11-11 —
  fetch-failed (password-protected on Read-tool cache fallback); snippet layer attributes to it "IT分销
  2023 前五大供应商采购占比51.94%" — snippet-marked, not load-bearing. Designated check-#1 fallback.
- [S1254] 长虹控股集团 2024 债券募集说明书, SSE static PDF — located, not fetched (budget); likeliest
  tier-1 carrier of IT分销 supplier structure/Huawei naming. Designated check-#1 fallback.
- [S1255] 腾讯新闻转载 "被超50个概念包围..." (2025-02-21) — snippet-marked carrier of the 总经销商
  authorization list and "65%+ revenue from Huawei-authorized distribution" claim; NOT fetched, never
  load-bearing; recorded as the W2-resurrection hypothesis to be tested by check #1.

Reused: [S257;S258;S260;S261;S262] via V_600839; [S532;S533;S534] via F_600839; [S677;S678] via
VAL_600839; [S1174;S1175] via FR_600839. FX note: 0.9274 CNY/HKD is the implied cross-rate of the two
filed revenue figures (¥40,643M / HK$43,826M), used only for bounded illustrations and flagged at each
use; no external FX quote was fetched, so no derived CNY figure here is presented to more than 3
significant figures.
