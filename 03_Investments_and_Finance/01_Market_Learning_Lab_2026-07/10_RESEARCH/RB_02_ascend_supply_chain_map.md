# RB_02 — Ascend/Kunpeng supply-chain map (listed names, by layer, with evidence tiers)

Educational analysis for a paper-trading learning exercise. Not investment advice.
Date: 2026-07-05 | Status: DRAFT — every tier-C row needs a filing check | Cites: [S###]

## Method note (read first)
Huawei is private and does not name suppliers; SMIC and most others never confirm Huawei
as a customer either. Therefore almost every "X supplies Ascend" claim below originates
in Chinese financial media or stock forums. The evidence tier is the whole game:
- **A** — the supplier's own filing / exchange announcement / official investor-Q&A reply
  substantiates the link (none earned yet; upgrading rows to A is mission M2).
- **B** — major financial media, sell-side research, or data-vendor screens (iFinD) name it.
- **C** — forum/Weibo/blog chatter. Leads only. A tier-C claim repeated across ten posts
  is still tier C.
Second trap: "in the chain" ≠ "moves the P&L." Always check what % of the company's
revenue the claimed Huawei business could plausibly be (e.g., Innolight [300308] is
chain-listed [S011] but earns predominantly from the overseas/Nvidia optics cycle —
different thesis entirely).

## The map

| Layer | Name (ticker) | Claimed role | Tier | Src |
|---|---|---|---|---|
| Foundry | 中芯国际 SMIC (688981 / 0981.HK) | Ascend fabrication on 7nm-class DUV; capacity+yield = chain bottleneck | B | S010 S013 S016 |
| Memory | (in-house) | 950PR ships with Huawei in-house HBM — displaces external-HBM theses | B | S003 |
| Packaging | 通富微电 (002156) | 2.5D/3D advanced packaging for Ascend | C | S009 |
| Pkg materials | 华海诚科 (688535) | Molding compound for Ascend | C | S009 |
| Test | 强一股份 | MEMS probe cards for 910B/950PR test; claimed sole supplier | C | S007 |
| Server integrators | 高新发展 (000628) ←华鲲振宇→ 四川长虹 (600839); 拓维信息 (002261); 神州数码 (000034); 烽火通信 (600498, via 长江计算); 软通动力 (301236) | Build/distribute Ascend servers; highest revenue certainty, thinnest margins (Huawei keeps chip+software value) [S010] | B–C mixed | S009 S011 S012 |
| Optical | 光迅科技 (002281); 华工科技 (000988); 中际旭创 (300308) | Supernode interconnect optics (800G/1.6T) | C / C / B | S009 S011 |
| Connectors | 华丰科技 (688629); 意华股份 (002897) | High-speed backplane connectors; 688629 claimed dominant Ascend share | C | S009 |
| PCB/CCL/substrate | 深南电路 (002916); 兴森科技 (002436); 生益科技; 南亚新材 (688519) | AI-server boards, CCL, ABF substrate | B–C | S009 S010 |
| Liquid cooling | 英维克 (002837); 申菱环境 (301018); 飞荣达 (300602); 高澜股份 | High-density cooling; ~450W/card class parts make liquid cooling near-mandatory [S007][S010] | C | S008 S009 |
| Power | 泰嘉股份 (002843, via 深圳雅达); 杰华特 (688141); 欧陆通 | Server PSU / DrMOS / DC-DC | C | S009 |
| Switching | 盛科通信 | Cluster ethernet switching silicon | C | S008 |
| 2nd-order: fab tools | 北方华创 (002371); 中微公司 (688012) 等 | If SMIC adds Ascend capacity, capex flows to domestic equipment | B (as logic), n/a (as fact) | S013 |
| ISV / apps layer | 科大讯飞 (002230); 软通动力; 润和软件 等 | Ascend-based all-in-one machines, model migration [S010: highest-margin, least-certain layer] | B | S010 S012 |

## Structural reads (from the tiered evidence, not from forums)
1. **Value distribution**: one research framing — integrators get certainty w/ squeezed
   margins; component makers (optics/PCB/cooling) get technical moats + content growth;
   software/migration gets the margin upside with execution risk [S010].
2. **Systems-over-die strategy**: Huawei compensates constrained single-chip performance
   with very large interconnected clusters [S010][S016] → interconnect layers (optics,
   connectors, switching) carry disproportionate content per FLOP. Testable.
3. **Verticalization risk**: in-house HBM [S003] shows Huawei absorbing chain value inward;
   any supplier thesis needs a "what if Huawei internalizes this too?" paragraph.
4. **Demand is policy-coupled**: export controls + domestic-substitution mandates are the
   tailwind [S016]; a policy reversal is the common-mode risk across every row above.

## Standing exercises
- E1 (Stage 1): pick any tier-C row → find the company's latest annual report on cninfo +
  its 互动易 replies → upgrade to B/A with quote, or mark UNVERIFIED in WATCHLIST.csv.
- E2 (Stage 2): estimate claimed-Huawei-revenue as % of total revenue for two names;
  compare their YTD price moves — is the exposure already priced?
- E3 (Stage 3): one prediction per month from read #2 or #3, logged with confidence.
