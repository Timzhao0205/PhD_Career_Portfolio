# SEED_CHAIN_MAP.md — first-pass map from the 2026-07-05 scoping session

> Status: SEED. Every item below must be re-verified against Tier-1/2 sources during
> Phase 1 before it can support a dossier. Evidence tags per CLAUDE.md. Source IDs
> (S01…) resolve in 90_BIBLIOGRAPHY/. Units: 1亿 = ¥100M CNY.

## 0. What is being sold ("计算")

- Huawei's computing line = 智算 (Ascend AI: chips → Atlas boards/servers → CloudMatrix
  /Atlas supernodes linking 384+ chips) + 通算 (Kunpeng ARM CPUs → TaiShan servers).
  Reported inside ICT Infrastructure; distinct from Huawei Cloud services. [DISCLOSED
  segment structure; S04, S06]
- Demand context FY2025: Huawei total revenue ¥880.9B, net ¥68.0B, R&D ¥192.3B (21.8%).
  ICT Infrastructure ¥375.0B (+2.6%, decelerating); external cloud ¥32.16B (−3.5%).
  [DISCLOSED; S01, S02]
- Ecosystem markers: 43 mainstream large models pre-trained on Ascend; 200+ open-source
  models adapted (chairman remarks, Feb 2026). [REPORTED; S03]

## 1. Revenue/volume anchors (the "¥70B → ¥200B" adjudication inputs)

| Anchor | Value | Tag | Source |
|---|---|---|---|
| Official ecosystem output, 2023 | ¥30–40B, scope undefined | [DISCLOSED-ish, VP remark] | S05 |
| China AI-chip market 2025 → 2026 | ¥131.6B → >¥180B; Ascend hardware ≥¥90B in 2026 | [ESTIMATE, IDC via secondary] | S07 |
| Huawei share of CN AI chips | 40% (2025) → 50% (2026E); Nvidia → single digits | [ESTIMATE, Bernstein via secondary] | S07 |
| Ascend 950PR 2026 shipment target | ~750k units; samples Jan-26, MP Apr-26, 2H ramp; ByteDance/Alibaba orders; better CUDA compatibility | [REPORTED, Reuters] | S08 |
| Fab capacity | China tripling AI-processor output; Huawei-dedicated fab + 2 more plants | [REPORTED, FT via secondary] | S08 |
| Q1-2026 channel check | Orders >50% of FY25 already; ByteDance ~150 supernode sets, Alibaba/Meituan ~50 each | **[RUMOR — quarantined]** | S09 |
| "¥70B this year / ¥200B next" | **Unverified in any authoritative source** as of 2026-07-05; plausible mid-range estimate + aggressive target | [RUMOR] | — |

## 2. Chain map by tier (listed names only; unlisted in §3)

**T1 Foundry** — SMIC 中芯国际 (688981.SH/0981.HK): sole logic foundry; 910C on 7nm
N+2, reported N+3 for 950-gen. [REPORTED; S10] ⚠️ NS-CMIC prohibited-check (gate).

**T2 Wafer test** — Qiangyi 强一股份 [ticker: verify; STAR, listed late 2025]: probe
cards; ~80% revenue from "Company B" widely presumed HiSilicon; Hubble 4.8%; FY25 rev
¥1.01B (+58%), net ¥395M (+69%); Q1-26 net +698%. [REPORTED citing prospectus/filings; S06]

**T3 Packaging/substrate** — Tongfu 通富微电 (002156.SZ): FY26 revenue target ¥32.3B,
capex ¥9.1B, CPO entering volume; declines to confirm Huawei specifically. [REPORTED;
S06] · JCET 长电科技 (600584.SH), Shennan 深南电路 (002916.SZ): concept-list only,
exposure unproven. [RUMOR→verify; S11]

**T4 Memory** — new 950-gen touts in-house HBM (HiSilicon path); CXMT unlisted.
Insourcing = structural risk to any memory-adjacent thesis. [REPORTED; S08]

**T5 Interconnect** — Huafeng 华丰科技 (688629.SH): high-speed backplane connectors +
cable modules for supernode card-to-card links; **FY25 annual report discloses Huawei =
¥1.53B = 60.52% of revenue**; rev +131.5% FY25; Q1-26 net +230%; Hubble 2.95%, never
reduced; company itself flags Huawei-dependence risk. Strongest [DISCLOSED] exposure
found. [S06] Retail claims of ~70–80% share in 224G class vs Amphenol/Foxconn-affiliates
= [RUMOR→verify].

**T6 Optics** — Yuanjie 源杰科技 (688498.SH): laser chips; Q1-26 rev ¥355M (+321%) ≈
60% of entire FY25; net ¥179M (+1153%); dubbed "new-stock king" — euphoria flag.
[REPORTED; S06] · Accelink 光迅科技 (002281.SZ), Innolight 中际旭创 (300308.SZ):
supernode optics candidates, exposure split with Nvidia chain unclear. [RUMOR→verify; S11]

**T7 Power/analog** — JoulWatt 杰华特 (688141.SH [verify]): Hubble-backed; FY25 rev
+58%. [REPORTED; S06] (Closest tier to investor's domain expertise — prioritize depth
here; map the supernode power architecture: rack PSU → busbar → board VRM.)

**T8 Thermal** — liquid cooling for 600W+ parts: Chuanrun 川润股份 (002272.SZ),
Envicool 英维克 (002837.SZ [verify]): concept-list stage. [RUMOR→verify; S11]

**T9 Integrators (margin-trap tier)** — Digital China 神州数码 (000034.SZ): FY25 AI
biz ¥33.0B (+47.7%); KunTai Kunpeng/Ascend servers ¥7.44B (+62.4%) but net ≈ ¥77.5M ≈
1% margin; Q1-26 profit growth ≪ revenue growth. [DISCLOSED; S06] · Tuowei 拓维信息
(002261.SZ): core business loss-making (FY25 pre-announcement), pivoting to compute
rental targeting 30%+ GM. [REPORTED, Tier-3 analysis of filings; S12] · Others:
Gaoxin Development 高新发展 (000628.SZ, acquiring Huakun Zhenyu), Fiberhome 烽火通信
(600498.SH, Changjiang Computing), iSoftStone 软通动力 (301236.SZ). [mixed; S07, S11]

**T10 Comparative set (not Ascend chain)** — Hygon 海光信息 (688041.SH, x86-compatible
DCU route, 365 models adapted) + Sugon 中科曙光 (603019.SH); Cambricon 寒武纪
(688256.SH [verify]). [REPORTED; S06]

## 3. Structural insights to test in Phase 1–2

1. **Margin asymmetry:** profit concentrates in Hubble-linked upstream components;
   integrators ~1% or losses. If confirmed, tier choice > name choice.
2. **Hubble as chokepoint signal:** Huafeng 2.95%, Qiangyi 4.8%, JoulWatt — map full
   Hubble portfolio overlap with listed chain.
3. **Insourcing frontier:** in-house HBM shows Huawei vertically integrating; which
   tiers are insourcing-proof (connectors? optics? thermal?) vs. exposed?
4. **Opacity workaround:** Huawei discloses nothing → supplier quarterlies +
   concentration tables + 互动易 answers are the ground truth; build the tracking
   calendar (CN reporting: annuals by Apr-30, Q1 by Apr-30, H1 by Aug-31, Q3 by Oct-31).
5. **Everything may be priced:** intraday pumps on the 750k rumor; Huafeng-vs-Innolight
   retail analogies. Phase 3 must include implied-growth math, not just fundamentals.

## 4. Open questions for the deep run

- Exact Qiangyi ticker + verify JoulWatt/Envicool/Cambricon tickers.
- Huafeng: qualified second sources for 224G? contract structure/pricing power?
- Supernode BOM: per-rack content value by tier (connectors vs optics vs power vs
  thermal) — build a bottoms-up ¥/rack model from teardowns and filings.
- 950PR ramp verification via SMIC capex/utilization disclosures and supplier guidance.
- Which names have H-share twins or accessible boards given Stock Connect STAR rules?
