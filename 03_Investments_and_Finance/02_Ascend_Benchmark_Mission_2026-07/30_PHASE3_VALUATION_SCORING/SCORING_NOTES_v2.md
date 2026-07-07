Educational benchmark for a paper-trading learning exercise. Simulated allocations, not investment advice or recommendations.

# SCORING_NOTES_v2 — accuracy patch

## §1 Baseline scores for the 5 PP1 additions (per A19)

Scored 2026-07-07 by the orchestrator per 01_MISSION/SCORING_RUBRIC.md, applying v1's A12
anchor interpretations unchanged. These baselines are the "v1" column the PP2
critical-reviewers rescore against; they are NOT final v2 scores. Weights: W1 .20, W2 .20,
W3 .15, W4 .20, W5 .15, W6 .10.

### 688347 华虹公司 — baseline 1.85
| Cell | Score | One-line basis |
|---|---|---|
| W1 | 3 | Tier B: named tier-3 chain (TrendForce/Reuters) ties the Ascend buildout to sister-entity Huali, not yet 688347's own filings (V_688347) |
| W2 | 0 | Verified 0% current-consolidated exposure (Huali unclosed, pending CSRC); prospective NOT-ESTIMABLE → rubric 0 (V_688347; VERIFIED_WATCHLIST row) |
| W3 | 2 | Documented interpolation: FY23–25 revenue −3.3/−11.4/+20.2%, GM 27.1→18.7 (CNY basis) and NM 11.9→2.2 deteriorating, but OCF positive and net cash 12.8bn (F_688347) |
| W4 | 1 | PRICED-FOR-PERFECTION on tier-B evidence; P/E ttm 1141x, deal value ≈1.5% of mktcap cannot explain it (VAL_688347) |
| W5 | 3 | Foundry layer is bottleneck-grade, but 688347's current base is competitive mature-node, one step below 688981's 7nm scarcity position (V_688347; RB_02) |
| W6 | 3 | Diversified customers (top-5 34.18%) but high policy common-mode + Huawei own-fab (SiCarrier-adjacent) verticalization vector (F_688347; V_688347) |

### 688141 杰华特 — baseline 1.70
| Cell | Score | One-line basis |
|---|---|---|
| W1 | 3 | Tier B: 国盛证券 named-analyst Ascend-chain deep-dive places its DrMOS/multiphase ramp in the Ascend power section; own AR silent (V_688141) |
| W2 | 0 | NOT-ESTIMABLE (anonymous #1 customer 30.04% not equatable per A8; DC-DC 53.29% product cut not server-specific) → rubric 0 (V_688141) |
| W3 | 1 | Persistent cash burn: NM −40.98/−35.94/−27.01%, OCF negative 3 straight FYs, swing to net debt −1,814.50M (F_688141) |
| W4 | 1 | PRICED-FOR-PERFECTION on tier-B evidence; no earnings floor, P/S 27.63x (VAL_688141) |
| W5 | 3 | Power-stage silicon has real barriers and AI content-per-system growth, but not on RB_02's premium-layer list and domestically crowded (RB_02; V_688141) |
| W6 | 3 | One material concentration: anonymous #1 customer ~26–31% for 3 straight years (F_688141; V_688141) |

### 002436 兴森科技 — baseline 1.25
| Cell | Score | One-line basis |
|---|---|---|
| W1 | 1 | Tier C Ascend-specific (generic-Huawei cooperation is tier A but predates FY2025 vintage and is not Ascend-specific) (V_002436) |
| W2 | 0 | NOT-ESTIMABLE; FCBGA (Ascend-relevant) subsidiary = 0.37% of revenue and loss-making → rubric 0 (V_002436) |
| W3 | 2 | Documented interpolation: revenue +23.7% and GM recovering 15.9→19.6, but NM 1.88%, FY25 OCF negative, net debt 4.35bn widening (F_002436) |
| W4 | 0 | PRICED-FOR-PERFECTION on tier-C evidence → rubric 0 (VAL_002436) |
| W5 | 3 | Substrate/PCB layer qualifies as technical-barrier, but 002436's substrate position is subscale and self-described underperforming — one step below incumbent 002916's W5=4 (V_002436) |
| W6 | 3 | Moderate concentration (#1 = 13.06%) but policy common-mode + execution dependence on domestic AI demand (V_002436; F_002436) |

### 688535 华海诚科 — baseline 1.50
| Cell | Score | One-line basis |
|---|---|---|
| W1 | 1 | Tier C weakest-hop: EMC→OSAT hop documented, OSAT→Ascend hop capped at C by this mission's own 002156 finding; Hubble 3.00% equity is affinity, not revenue (V_688535) |
| W2 | 0 | NOT-ESTIMABLE; GMC (the Ascend-plausible grade) had zero confirmed revenue at last direct clarification → rubric 0 (V_688535) |
| W3 | 3 | Mixed: historically profitable, revenue +38.1% (M&A-boosted, ~2mo 衡所华威), but NM halved to 5.29% and OCF thin; small net debt from convertible (F_688535) |
| W4 | 0 | PRICED-FOR-PERFECTION on tier-C evidence (P/E ttm 746x, P/S 49.8x) → rubric 0 (VAL_688535) |
| W5 | 3 | Documented interpolation: advanced-packaging materials layer has moat potential (HBM-class EMC, domestic substitution), but the premium grade is pre-revenue; core EMC is competitive (V_688535) |
| W6 | 4 | Documented interpolation: genuinely diversified customers (top-5 23.22%, max 7.48%), verticalization implausible; held below 5 by semis policy common-mode (F_688535) |

### 688519 南亚新材 — baseline 2.20
| Cell | Score | One-line basis |
|---|---|---|
| W1 | 3 | Tier B: statutory-relay AR language names 昇腾/超节点 delivery and 华为 certification of NOUYA8U 800G material; own top-5 table names only PCB fabricators (V_688519) |
| W2 | 1 | Bound-mapping per A12: segment ceiling 17.70% contains Huawei+Hygon+telecom+storage; true Huawei/Ascend sub-share plausibly <10% → low band (V_688519) |
| W3 | 3 | Mixed: revenue +55.5%, GM recovering 4.16→11.80, NM 4.60%, but FY25 OCF −83.18M and small net debt (F_688519) |
| W4 | 1 | PRICED-FOR-PERFECTION on tier-B evidence (P/E ttm 215x on a recovering-margin base) (VAL_688519) |
| W5 | 3 | High-speed CCL (M6/M7) has real qualification barriers and AI content growth, but the layer is competitive (生益科技-dominated per RB_02 context) (V_688519; RB_02) |
| W6 | 3 | Pass-through concentration (top-5 = 34.96%, all PCB fabs) + policy common-mode; verticalization implausible (F_688519; V_688519) |

§1 conventions: all A12 global anchor interpretations carry over; W2=0 for NOT-ESTIMABLE
follows the rubric text and v1 precedent (000628, 002281, 002916, 002156, 301018, 688981);
bound-mapping (688519 W2=1) follows A12's ceiling/floor rule; every interpolated integer is
labeled "documented interpolation" above. Baseline totals: 688347 1.85, 688141 1.70,
002436 1.25, 688535 1.50, 688519 2.20. No v1 name is scored, ranked, or referenced
comparatively in this section beyond the two explicitly-cited cell-consistency anchors
(002916 W5, 688981 W2 precedent class).

## §2 PP2 adjudication conventions and change log (final at Gate PG2)

Cross-cutting rulings established this patch (full text in REDTEAM_RESPONSES_v2.md):

- **R0.5 — W4 chain-nexus refinement of R0.2.** The tier governing W4's 0/1 boundary is
  the tier of the CHAIN-RELEVANT growth narrative the price embeds. Tier-1 chain-relevant
  narrative (own-AR AI-server demand) → PFP maps to 1 (002916). Chain-relevant content at
  tier-C/UNVERIFIED → 0 even where a non-chain business is tier-1 strong (002156's AMD
  engine; 688347's excluded-asset story; 000628's debunked story). Non-chain strength is
  priced in W3, never W4.
- **R0.6 — W2 bound conventions.** Point or proven-minimum inside a band → that band
  (002261 at 27.0% point; 301236 at ~1.3% proven minimum). Bound spanning band boundaries
  with no interior point → NOT-ESTIMABLE → 0 (688519, 600839). Ceiling wholly inside one
  band → that band (300308).
- **R0.7 — Regulator-action axis in W3.** Live exchange inquiry / 监管警示 targeting
  P&L-quality dimensions is an R1.3-class aggravator (688519).
- **R0.8 — Entity-scope discipline in W1.** Evidence attaching to an affiliated, unowned
  entity scores the listco's own evidence; a verified-absent mechanism reduces the listco
  link to C-grade residue (688347's Fab-5-only deal perimeter, verified S1350/S1277).

Score movements, v1 (or A19 baseline) → final v2, with the deciding step:

| Ticker | v1/base | FR | Final v2 | Deciding adjudication |
|---|---|---|---|---|
| 688629 | 2.70 | 2.70 | 2.70 | All six cells re-earned (FR) |
| 000034 | 2.00 | 2.00 | 2.00 | Confirmed; W2 "point" relabeled ceiling |
| 300308 | 2.00 | 2.00 | 2.00 | Confirmed; ceiling logic upheld |
| 002916 | 1.80 | 2.00 | 2.00 | W4 0→1 per R0.5(a) |
| 688981 | 1.90 | 1.90 | 1.90 | Confirmed; Hua Hong finding = nuance only |
| 002261 | 1.70 | 1.70 | 1.70 | W2=2 point-in-band rescue (R0.6) |
| 002281 | 1.80 | 1.70 | 1.70 | W6 4→3 (concentration trend) |
| 301236 | 1.60 | 1.60 | 1.60 | Confirmed; first tier-1 artifact obtained |
| 688519 | 2.20 (base) | 2.20 | 1.60 | RT2: W1 4→3, W3 3→2 (R0.7), W5 3→2, W6 3→2 |
| 002371 | 1.55 | 1.55 | 1.55 | Confirmed |
| 301018 | 1.55 | 1.55 | 1.55 | Confirmed ("H公司" stays C) |
| 002436 | 1.25 (base) | 1.45 | 1.45 | W1 1→2 (official-reply interpolation) |
| 600498 | 1.40 | 1.40 | 1.40 | Confirmed |
| 600839 | 2.40 | 1.65 | 1.35 | FR killed R0.1-era W2 premise; RT2 both directions: W1 1→2 up, W4 3→1, W6 4→3 |
| 688535 | 1.50 (base) | 1.35 | 1.35 | W3 3→2 (non-like-for-like M&A) |
| 688141 | 1.70 (base) | 1.70 | 1.25 | RT2: W1 3→2 (R2.1 cap), W5 3→2, W6 3→2; statutory loss-trigger logged |
| 002156 | 1.60 | 1.80 | 1.20 | RT2 reversed FR's W4 via R0.5(b); W3/W5/W6 each one notch down |
| 688347 | 1.85 (base) | 1.85 | 0.85 | RT2 + orchestrator verification: deal buys Fab 5 only; W1/W3/W4/W5/W6 all conceded (R0.8) |
| 000628 | 0.75 | 0.75 | 0.75 | Debunk reconfirmed through 2026-07-04 |

Process note: the two FR upgrades that later reversed (002156 W4; 688519 W1) and the one
that survived (002916 W4) are retained in the FR_ files unedited — the reversal reasoning
lives in REDTEAM_RESPONSES_v2 R5.2/R5.3. This is deliberate: the answer key's learning
value includes seeing a plausible upgrade get killed by a sharper adversarial pass.
