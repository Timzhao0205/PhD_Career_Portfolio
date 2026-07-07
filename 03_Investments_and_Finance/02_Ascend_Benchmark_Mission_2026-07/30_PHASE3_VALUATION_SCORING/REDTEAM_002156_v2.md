Educational benchmark for a paper-trading learning exercise. Simulated allocations, not investment advice or recommendations.

# REDTEAM_002156_v2 — 通富微电 (TFME, SZSE 002156) — re-red-team (accuracy patch)

Attack brief, 2026-07-07. Row under attack (SCORES_v2.csv): W1=1, W2=0, W3=4, W4=1, W5=4, W6=2, total **1.80** —
a top-8 entrant created by FR_002156's W4 0→1 upgrade (+0.20, exactly the entry margin over the v1 total 1.60).
Inputs: V_002156.md, F_002156.md, VAL_002156.md, FR_002156.md, SCORES_v2.csv, SCORING_RUBRIC.md,
REDTEAM_RESPONSES.md (R0.2/R0.3/R2.5/R2.6), RB_02, PROGRESS_LOG. Fetch budget 4/4 spent: 3 delivered
([S1258]–[S1260], zh searching done per rule 7), 1 timed out (eet-china, logged snippet-only [S1262]).
New sources S1258–S1264 in 90_BIBLIOGRAPHY/frags/rt2_002156.json. **Four score challenges below (W3, W4, W5, W6)
require written responses before this gate passes.** Headline: the W4 upgrade rescored an ASCEND-benchmark cell on
a NON-Ascend narrative under a rule that is codified nowhere and contradicts the Gate-G3 standard of record; and the
name's two stories — AMD engine, Ascend optionality — share one US-policy failure mode, so they are mutually
corrosive, not additive.

---

## 1. Strongest bear case (5 bullets)

- **B1 — This top-tier slot is occupied by a non-Ascend thesis; the Ascend-evidenced content of the score is 0.20 of 1.80.**
  Seven tier-1 documents contain zero 华为/昇腾/海思/鲲鹏 characters ([S131], re-confirmed [S1206]); exposure is
  NOT-ESTIMABLE by the mission's own audit (V_002156). The cells that produce 1.60 of the 1.80 (W3+W4+W5+W6) are
  earned by the AMD/export franchise — 52.29% single customer, 66.59% export revenue [S131] — i.e., 89% of the score
  answers a question the benchmark did not ask. The instrument that lifted it into the top tier (W4 0→1) keys on the
  tier-1 AMD narrative, extending a principle whose own origin case (FR_002916: tier-1 **AI-server** growth, a
  chain-relevant layer) at least had chain nexus. 002156 is the only name whose W4=1 rests on a narrative with zero
  Huawei/Ascend content. That is a smuggled thesis, not an adjudication.
- **B2 — The 52.29% cliff has a demonstrated policy trigger and an undefined scope.** AMD's 8-K (event 2025-04-15):
  a new US license requirement on MI308 products to China/D:5 with charges "up to approximately $800 million" and
  "no assurance that licenses will be granted" [S1258] — one BIS rule repriced the majority customer's China AI line
  overnight (licenses re-granted ~3 months later, [S1261] snippet — whiplash in BOTH directions inside one quarter).
  Meanwhile the load-bearing "80%" comfort statistic ("公司是AMD最主要的封测供应商，占其相关产品的80%以上"
  [S131/S133]) never defines 相关产品: TFME's official word on the AI line is only "公司有涉及AMD芯片Instinct
  MI300的封测项目" — participation confirmed, work-scope and value share undisclosed [S1259] — while the premium
  2.5D/3D step of that line (SoIC+CoWoS) is reported at TSMC, with CoWoS-class mass production held only by
  TSMC/Samsung/Intel ([S1264], snippet). No file or fetched source quantifies TFME's share of AMD's **AI-accelerator
  packaging value**. Evidence gap stacked on a 52.29% concentration.
- **B3 — The Ascend optionality is not free upside; it is self-canceling, and its socket has named occupants.**
  If the tier-C rumor ever converted to fact, packaging Huawei AI silicon would stack US-export-control exposure onto
  a company whose majority customer is US (the MI308 precedent shows the license regime's reach [S1258]) — the bull's
  "AMD+华为双绑定" [S141] stacks two exposures with one failure mode (flagged as scenario logic, not sourced law).
  And the visible Ascend packaging path already runs elsewhere: tier-3 reporting of Huawei's quad-chiplet packaging
  patent names SMIC process + JCET (长电科技) lines ([S1262] snippet); the same tier-4 ecosystem that generated the
  TFME rumor assigns the "国产先进封装独苗" seat to 盛合晶微 with a claimed 3-year Huawei lock ([S1263] snippet) —
  the rumor set is internally contradictory, which is exactly what tier C means. TFME's own IR cedes the adjacent
  HBM-packaging space to international IDMs [S133 §J].
- **B4 — PRICED-FOR-PERFECTION on a debt-funded treadmill with a dated contract cliff.** 71.55× ttm / 84.94× FY25
  P/E; compression to 25× at the 2026-07-07 cap needs NP 2.86× ttm ≈ 42%/yr for 3 years (FR_002156 §3's own
  arithmetic) against delivered NM of 4.36% (FY25) and GM that FELL in the boom year (14.84→14.59%) [F_002156].
  Cumulative FY23–25 FCF = −832.28 − 676.36 + 754.58 = **−754.06M**; net debt −13,357.21M (≈11× FY25 attributable NP,
  +40% vs FY23; cash 5,410.08M vs interest-bearing debt 18,767.29M) [S425/F_002156]; capex = 22.2% of FY25 revenue.
  The +224.55% Q1-26 NP print is a 1.66%→4.40% quarterly-NM base effect (derived from [S616]/[S135] figures). And the
  last disclosed term of the AMD cooperation agreement runs to **2026 — this year** ("公司与AMD的合作协议已续签到
  2026年", as of 2022-02-23 [S1260]); no file documents the current term. Renewal economics are a live, dated unknown
  beneath a 71× multiple.
- **B5 — The "advanced packaging premium" cell is anchored to a rubric line this name does not occupy at tier ≤B.**
  The W5 premium anchor is "advanced packaging per RB_02 read #2" — an Ascend-supernode content-per-system argument.
  TFME's tier-1-evidenced franchise is flip-chip-led volume packaging (≈70% of revenue [S133 §I]) for an export/AMD
  chain; its own AR lists the chiplet high-density HPC packaging project as 研发进行中 — R&D in progress, not a
  commercial line [S131 §D]; HBM packaging is ceded [S133 §J]; GM 14.59% and NM 4.36% are service-layer economics,
  not barrier pricing (FR_002156's own W5 note concedes this). The premium tier of its flagship customer's AI line is
  internalized upstream at the foundry ([S1264] snippet). Demonstrated content growth in the wrong chain was
  adjudicated at G3 as not earning the RB_02 premium (R2.5) — the same logic is unapplied here.

---

## 2. Score audit — every cell (weights .20/.20/.15/.20/.15/.10; current total 1.80, arithmetic verified)

| Cell | Current | Supported by files? | Red-team proposal | Delta |
|---|---|---|---|---|
| W1 | 1 | **YES** — tier C (V_002156; FR §1 re-confirmed [S1206]); rubric maps C→1 | 1 (confirm) | 0 |
| W2 | 0 | **YES** — NOT-ESTIMABLE, residual-slicing refused per NUMBER TRUTH; R0.1-consistent | 0 (confirm) | 0 |
| W3 | 4 | **CONTESTED** — criteria-counting hides magnitude; anchor-3 "mixed" is the literal fit | **3** | −0.15 |
| W4 | 1 | **NO** — conflicts with the written G3 standard (R0.2); upgrade rule uncodified; application unsupported | **0** | −0.20 |
| W5 | 4 | **CONTESTED** — G3 chain-mismatch precedent (R2.5) unapplied; premium sub-layer pre-commercial | **3** | −0.15 |
| W6 | 2 | **CONTESTED** — both anchor-1 prongs present; FR's two dismissals fail on fetched facts | **1** | −0.10 |

Proposed corrected row: 1,0,3,0,3,1 → **1.20**. Even conceding ONLY W4 — the most rule-bound challenge — the total
returns to 1.60 and the rubric's W1-first tiebreak pushes this name back out of the top tier: the entire re-ranking
event this file was triggered by rests on that single cell.

**W3 4→3.** The 5-anchor is conjunctive (growth AND stable/rising margins AND positive OCF AND net cash). FR's
"meets 3 of 4, cap at 4" counts prongs; the anchor-3 word "mixed" prices magnitude: (i) the net-cash miss is
−13,357.21M, widening 40% over two years, ≈11× FY25 attributable NP [F_002156]; (ii) the margin prong is only
half-met — GM fell 14.84→14.59% in the record year; the NM rise (0.76→2.84→4.36%) is low-base recovery, the very
point VAL_002156 §3 makes; (iii) OCF covered capex in one year of three; cumulative 3-yr FCF −754.06M — growth is
debt-funded (interest-bearing debt +34% FY23→FY25 [F_002156 §net-cash]). Growing revenue + positive OCF against a
widening leveraged capex treadmill and a slipping GM is the definition of "mixed" → 3.

**W4 1→0 (the load-bearing challenge).** Three independent grounds:
(a) *Rule of record.* R0.2 (REDTEAM_RESPONSES.md, the Gate-G3 written adjudication) fixes the 0-vs-1 boundary to
"the P1 evidence TIER LETTER of the Huawei/Ascend link," explicitly REBUTTING critics who wanted the priced-narrative
gap handled in W4, "priced through W1/W2/W6 — not double-priced in W4." 002156's link letter is C; PFP + C → 0. The
contrary "narrative-evidence" principle exists only in a PROGRESS_LOG batch note ("principle to be applied … and
codified in consolidation", 2026-07-07 17:30 line) and in FR citations — SCORING_NOTES_v2 §2 is still "(reserved)";
no codified supersede of R0.2 exists on disk. A rubric-standard reversal that moves a name into the top tier must
meet at least the documentation bar R0.2 itself met.
(b) *Category error even if codified.* The principle's origin (FR_002916) credited a tier-1 narrative INSIDE the
chain layer under test; its other applications (FR_002261, FR_301236, FR_600498) credited tier-A/B **Huawei-subject**
narratives. 002156 is the sole extension to a narrative with zero chain nexus (AMD/export). In an Ascend answer key,
W4=1-via-AMD converts a 0.20-weight Ascend cell into a reward for owning a good non-Ascend business — the same
scoring-the-wrong-chain artifact G3 corrected elsewhere (R2 headnote; R2.5).
(c) *Unsupported even on its own terms.* What the 71.55× multiple prices is the FORWARD path (≈42%/yr NP CAGR ×3yrs,
NM ~11.8% vs 4.36% delivered — FR §3), which no tier ≤B source evidences; the only above-spot carrier is a tier-3
bank opinion (Citi 80 [S1207/S138]), and the older AMD/Meta-only anchor (群益 65, 2026-02-25 [S139]) sat BELOW the
2026-07-07 close. The claim embedded in W4=1 — that the tier-C Ascend rumor contributes nothing to the multiple — is
not established by any file: the tier-4 Ascend wave ran "loudly on roughly the same timeline" (VAL §3), and the one
on-file price-anomaly artifact (2026-01-20 异常波动公告 [S136]) is unattributed. Rubric preamble: "A cell that cannot
be supported scores 0, not a guess."

**W5 4→3.** The current 4 already carries FR's three within-layer docks (chiplet 研发进行中 [S131 §D]; HBM ceded
[S133 §J]; 14.59%/4.36% economics). What is missing is the fourth, adjudicated dock: RB_02 read #2's premium is
Ascend-supernode content-per-system; TFME's demonstrated advanced-packaging content growth is in the overseas/AMD
chain while its Ascend participation is tier C — precisely the configuration G3 scored down under R2.5 ("content
growth … demonstrated in the overseas chain"). Layer membership real, qualification barriers real, pricing power
absent, premium sub-layer pre-commercial, premium step of the flagship AI line internalized upstream ([S1264]
snippet) → anchor-3 "defensible but competitive" verbatim.

**W6 2→1.** Anchor-1 = concentration AND verticalization/displacement, both present: (i) concentration is severe and
六年 structural, not cyclical — Customer-1 52.29% FY25 / 50.35% FY24 / 59.38% FY23 [S131/S433], with AMD-attributed
share ≥49% every year since 2019 (37.73→51.39% 2016–2020 [S1260]); bilateral lock ">80% of AMD's relevant products"
[S131]. (ii) FR dismissed the second prong on two grounds that fail: "the Huawei-verticalization axis does not
apply" — the rubric's W6 text is customer-agnostic ("verticalization threat", not Huawei-verticalization), and R0.3
reads the precedent as demonstrated appetite; "no internalization precedent is on file" — an evidence gap, now
closed: these plants WERE the customer's in-house backend until 2016-04-29 (85% bought for $371M; AMD retains 15% of
通富超威苏州/槟城 [S1260]), the premium step of the customer's AI line is already captured upstream (SoIC/CoWoS at
the foundry, [S1264] snippet, with TFME's official MI300 scope undisclosed [S1259]), and the cooperation agreement's
last disclosed horizon is 2026 [S1260] — allocation is contract-renewal-contestable, and TFME's own Penang 3nm
validation [S137 via V §M] shows the out-of-mainland migration channel is real and in use. Add the same-customer
policy common-mode demonstrated at $800M scale [S1258]. Concentration + displacement/verticalization + policy
common-mode on one counterparty = anchor-1 → 1. (Not 0: the 0-anchor's internalization-precedent prong points the
wrong way for AMD itself — 2016 was a DIVESTMENT — and 52.29% is not the 0-anchor's near-total block; cf. the R2.6
configuration.) Note: FR's own text already concedes "worse than anchor-3"; the interpolation direction it then chose
(up to 2) contradicts the anchor text it quoted ("both" → 1).

---

## 3. Verticalization test (both vectors)

**Huawei internalizes (precedent: in-house HBM, RB_02 [S003]):** the marginal P&L damage to TFME is ~zero — W1/W2
already price the link at C/NOT-ESTIMABLE — but the equity damage is not: the only Ascend content in a 71.55× ttm
multiple is the tier-C rumor layer, and every internalization datum (Huawei quad-chiplet packaging patent on
SMIC+JCET lines [S1262] snippet; 盛合晶微 "独苗" 3-year-lock narrative [S1263] snippet; TFME's own concession that
HBM packaging stays with international IDMs [S133 §J]) deflates exactly that layer, so the name absorbs
Ascend-narrative downside with no evidenced Ascend upside. **AMD in-sources / re-shores:** full re-insourcing is
implausible — AMD is fabless and SOLD these plants (85% for $371M, 2016) — but the operative displacement is already
running on two channels: upward, the premium 2.5D/3D step of the AI line sits at TSMC (SoIC+CoWoS; CoWoS-class mass
production held by TSMC/Samsung/Intel only, [S1264] snippet) while TFME's confirmed MI300 role is scope-undisclosed
"封测项目" [S1259]; outward, the US policy push that produced the MI308 license regime [S1258] pressures
mainland-located packaging of US AI silicon generally, the JV cooperation agreement's last disclosed term ends 2026
[S1260], and the migration path out of the mainland JVs (Penang, 3nm validated [S137]) is one AMD allocation decision
wide. Both vectors converge on the same end-state: TFME retains mid-tier volume packaging at 14.59% GM on both
customers' chains and never owns the premium tier on either — which is the opposite of the W5/W6 configuration the
current row prices.

## 4. Common-mode test

TFME's primary common-mode is **US policy acting through AMD**, a different axis from the Huawei-demand common-mode
of the portfolio's other names — but it is not diversification, it is inversion with shared sentiment beta. Channels:
(1) US tightening (MI308-class rule extension, OSAT-location restrictions): 52.29%-customer revenue and the 66.59%
export book take the hit ([S1258]; [S131]) while the domestic-substitution names rally — TFME is SHORT the
portfolio's core scenario. (2) US loosening (license expansion per the 2025-07 resumption pattern [S1261] snippet):
TFME's AMD engine strengthens, but the Ascend-substitution premium deflates portfolio-wide — including the tier-C
rumor layer inside TFME's own 71.55× multiple. (3) A Huawei demand shock (order cut, Ascend digestion pause)
transmits to TFME almost purely through A-share AI-theme sentiment — its earnings channel is C/NOT-ESTIMABLE — an
asymmetric trade: no evidenced fundamental participation in the portfolio's upside scenario, full multiple
participation in the sentiment unwind (the stock already prints unattributed 异常波动 events [S136]). (4) The tail
common-mode: an actual confirmed TFME-Ascend win — the portfolio's best-case event — would itself be a US-policy
event for TFME's majority customer relationship (B3). Within this benchmark, holding 002156 alongside the Huawei
names hedges customer mix but doubles sentiment beta and adds a policy exposure that fires in BOTH policy directions.

## 5. Five falsifiable checks

| # | Observable event | Date | Bear if | Bull if |
|---|---|---|---|---|
| 1 | H1-2026 report (statutory deadline 2026-08-31): 华为/昇腾/海思 mentions; chiplet HPC project status vs 研发进行中 [S131 §D]; any AMD-agreement renewal disclosure beyond 2026 [S1260] | by 2026-08-31 | Still zero mentions, project still R&D, no renewal disclosed → tier C stands, W5 premium stays pre-commercial, contract cliff live | Tier-1 昇腾 naming (W1 rescore up) or multi-year renewal disclosed (W6 relief) |
| 2 | AMD Q2-2026 results/10-Q (~2026-08-04): China/MI-series guidance; any packaging/test footprint statement (mainland vs Penang/US/Taiwan) | 2026-08-15 | China guidance cut, or allocation shift language away from mainland JVs → W6=1 confirmed | TF-AMD mainland expansion reaffirmed with volume commitments |
| 3 | New BIS/Commerce action extending AI-chip license regime or touching China-located OSAT of US AI silicon | by 2026-12-31 | Any such rule → common-mode fires; B2 confirmed | Durable license framework with sustained grants → AMD engine de-risked (supports FR's W4 reading against this file) |
| 4 | Q3-2026 report (due by 2026-10-31): GM vs 14.59%, net debt vs −13,357M | 2026-10-31 | GM <14% or net debt beyond −15bn → W3=3 confirmed (treadmill) | GM ≥16% AND net debt stable/shrinking → W3=4 defensible |
| 5 | Tier ≤B attribution of 910C/910D-generation Ascend packaging to a named OSAT (sell-side/major media supply-chain work) | by 2026-12-31 | Names JCET/盛合晶微/in-house → TFME optionality dead; W5 Ascend-anchor void; B3 confirmed | Names TFME → W1 C→B, B1/B3 collapse, this file's category-error attack fails |

---

Sources: on-file S131, S132, S133, S135, S136, S137, S138/S1207, S139, S140, S141, S424–S433, S425, S614–S616, S1206
(V_/F_/VAL_/FR_002156 as cited); RB_02 [S003]; G3 record REDTEAM_RESPONSES.md R0.1–R0.3, R2.5, R2.6. New this session
(frags/rt2_002156.json): **[S1258] fetched** AMD 8-K 2025-04-15/16; **[S1259] fetched** TFME MI300 官方回复 relay
2024-03-15; **[S1260] fetched** 21世纪经济报道 2022-02-23 (JV genesis $371M/85-15, AMD share 37.73→51.39%, 协议续签到
2026年); [S1261], [S1262], [S1263], [S1264] snippet-grade, marked, non-load-bearing. Search trail (zh, per rule 7):
「AMD MI308 出口管制 许可 8亿美元 减值 中国 2025」「通富微电 AMD 2016年 收购 苏州 槟城 封测厂 85% 合资」「AMD MI300
CoWoS 台积电 先进封装 通富微电 后段 测试」「华为 自建 先进封装 产线 2.5D 昇腾 封装 内制」.
