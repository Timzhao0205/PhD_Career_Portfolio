# RB_01 — Huawei's 计算 (computing) business: what it is, what's confirmed, where the 70B/200B rumor likely comes from

Educational analysis for a paper-trading learning exercise. Not investment advice.
Date: 2026-07-05 | Status: DRAFT — verification plan open | Cites: [S###] → 90_SOURCES/sources.json

## Question
Rumor as heard: "Huawei sold ~70B RMB (700亿) of 计算 this year and targets 200B RMB
(2000亿) next year." What is 计算, is the number real, and what's the investable angle?

## TL;DR
计算 = Huawei's computing business: **Kunpeng (鲲鹏)** general-purpose Arm server CPUs
(通算) + **Ascend (昇腾)** AI accelerators (智算), plus the boards, Atlas servers,
CloudMatrix/supernode clusters and software (CANN, MindSpore) built on them — so yes,
substantially "AI computing power," but broader than AI chips alone [S004][S015].
Huawei has **never disclosed a standalone revenue figure for it** [S005][S015], so the
70B/200B numbers cannot be officially confirmed — they are estimate/rumor-grade until
traced. Huawei itself is unlisted; any market angle runs through the supplier chain (RB_02).

## 1. What 计算 means, precisely
- Financial-media decomposition: computing splits into 通用计算 (general, Kunpeng CPU)
  and 智能计算 (intelligent, Ascend NPU); these plus compute boards, servers and data-
  center gear sit mostly inside the **ICT infrastructure** reporting segment [S004].
- The chips are designed by HiSilicon (海思), reorganized as the 芯片与器件 (chips &
  devices) unit — the one segment whose revenue Huawei has never published [S015].
- Scale markers Huawei does publish are ecosystem counts, not revenue: 3.8M Kunpeng and
  4.0M Ascend developers, >9,800 partners, >26,000 solutions by end-2025 [S001].

## 2. What is officially disclosed (Tier ≤2)
- FY2025 group revenue 880.9B RMB (+2%), net profit ~68B, R&D 192.3B = 21.8% of revenue
  [S002][S006]. FY2024: 862.1B total [S014].
- ICT infrastructure (the segment containing computing): 375.0B in 2025, +2.6% YoY,
  decelerating from +4.9% in 2024 [S002][S003]. Cloud external revenue 32.16B, −3.5% [S002].
- Management repeatedly credits "ten years of preparation in computing" for AI-driven
  growth — direction confirmed, magnitude never quantified [S014][S001].

## 3. Candidate origins of "70B this year / 200B next year" (all require tracing)
| # | Candidate | Evidence | Tier |
|---|---|---|---|
| a | Media/analyst estimate of computing-product-line or Ascend revenue ≈700亿 for 2025 | Closest official anchor: Huawei VP Ma Haixu said the 2023 Kunpeng+Ascend ecosystem output was 300–400亿, scope undefined [S005]. A ~2x/yr ramp to ~700亿 by 2025 is arithmetically plausible but no primary source located yet | C |
| b | Confusion with **unit** figures: 2025 Ascend shipments estimated at 70–80.5万片 (700–805K chips) [S010]; 2026 shipment target circulating as 75万颗 [S007] | 70万 (chips) vs 700亿 (RMB) garble in retelling | C |
| c | "2000亿" = the widely-shared "2026 Ascend pie" figure in stock-forum posts, alongside claimed hyperscaler orders (ByteDance 25万, Alibaba/Tencent 12万 each) [S007] | Pure social-media chatter; the Sina post aggregating it literally self-labels as not-advice banter | C |
| d | Confusion with the **whole industry chain**: CCID (赛迪顾问) projects the Ascend industry chain incl. servers+software to exceed 3000亿 by 2027 at 35–40% CAGR [S011] — implying ~2000亿-scale around 2026 | Best documented "2000亿-adjacent" number; but it's chain-wide market size, not Huawei revenue | B |

Working hypothesis: the rumor is a compression of (d)+(b) — a ~2000亿 2026 chain-size
estimate plus 2025/2026 unit-shipment figures — restated as if it were Huawei's own
computing revenue. Falsifier: find a named analyst/outlet publishing 700亿-revenue-2025
explicitly (→ OPEN_QUESTIONS Q1).

## 4. Sanity check (order-of-magnitude only — assumptions, not data)
750K accelerators [S007, tier C] × assumed 150–250K RMB system-level value per card ≈
110–190B RMB of chain-wide hardware value. So a 2000亿-scale **ecosystem** in 2026 is not
absurd; attributing it all to Huawei's own top line is unsupported. Note: Huawei's entire
2025 growth was +2% on 880.9B [S002] — a computing line jumping 70B→200B (+130B) in one
year would be visible in group numbers unless offset by declines elsewhere. Treat with
suspicion.

## 5. Verification plan (this is the Stage-1 exercise)
1. Search zh media for 「华为 计算产品线 收入 2025」and named-analyst estimates; log first
   traceable publication of 700亿/2000亿-as-revenue.
2. Huawei FY2026 interim (≈2026-08, Beijing Financial Assets Exchange filing) and annual
   report (≈2027-03): check for any new segment disclosure → resolves prediction P001.
3. Watch Huawei Connect (Sept) keynotes for official Kunpeng/Ascend scale claims.
4. Cross-check demand side: hyperscaler capex disclosures + 运营商 procurement notices
   (e.g., the claimed China Mobile supernode tender [S007, tier C]) against official
   tender platforms.

## Context worth keeping (Tier ≤3)
- Ascend 950PR launched with **in-house HBM**, marketed at a multiple of H20 performance;
  supernode/cluster strategy (384-chip CloudMatrix) compensates single-die limits
  [S003][S016]. Export controls on Nvidia + Beijing self-sufficiency push are the demand
  tailwind [S016]. SMIC 7nm-class DUV with constrained yield is the supply bottleneck
  (yield ≈30% per one deep-dive — tier C, verify) [S010].

## Verdict
Rumor: UNCONFIRMED as Huawei revenue; plausible as garbled ecosystem-size + shipment
figures. Case: RESEARCH-MORE. The investable learning surface is the supplier chain →
RB_02.
