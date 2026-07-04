# RED TEAM — V04: MV >1000 °C resistive-heating power controller for calciner/kiln retrofits

Date 2026-07-03 · Raw 79.6 · **RT-adjusted 66.8** · Kill-probability **75%** · Novelty **NOVEL** (G7 pass, with caveat)
Sources: `30_SCORING/REDTEAM_V04_sources.json` [RT-V04-01..17]

## 1. Novelty verification (G7-NOVEL) — first
Three nearest ledger neighbors:
- **C16 (HTS induction billet heaters):** different physics (superconducting-DC induction vs Joule/radiant), different buyer (extrusion shops vs kiln OEMs/cement). Not a variant.
- **N05 (solid-state RF/microwave process heat):** dielectric/RF mechanism, RF-amplifier power chain. Not a variant.
- **C09 / RID-004 / PWR-06 (MV SST blocks, MF-transformer engine):** MV power electronics but datacenter buyers, DC output. V04 outputs regulated 50/60 Hz into heating transformers. Different category + buyer.
No ledger entry covers merchant resistive >1000 °C process-heat power control; declaration survives. **Verdict: NOVEL.** Caveat: novel vs OUR ledger ≠ novel vs the market — the "unserved slot" claim is a market assertion, and it is false (§3). G7 passes; C7 does not.

## 2. Strongest bear case
By 2031 V04 is a feature, not a company. Merchant SCR/thyristor heater control is a 50-year-old field (Chromalox, Watlow/Eurotherm, Advanced Energy, AMETEK HDR, Spang, Control Concepts, CD Automation), and Chromalox DirectConnect already ships the UL 347C-certified MV (2.3–7.2 kV, multi-MW) SCR panels V04 claims don't exist [RT-V04-01/02]. Every named electric-calciner program has its power partner: FLSmidth builds IR/induction calciners in-house (ECem/ECoClay) [RT-V04-10]; Coolbrook is powered and part-owned by ABB (motors + VSDs — rotodynamic, no resistive controller needed) [RT-V04-11]; Kanthal bundles Prothal MW-class heaters + controls and sits inside ELECTRA with Heidelberg [RT-V04-08/09]. The 2029 entrant sells a box nobody's BOM is missing, into a cement sector whose Chinese half is loss-making and whose EU half electrifies on grants.

## 3. Hidden competition (missed by the one-pager)
(a) **Chromalox DirectConnect** MV SCR panels, UL 347C [RT-V04-01]; the cited "stops near 600–1000 °C" [G04-13] describes Chromalox's heater *elements'* process duty, not controller capability — a category error. (b) **AE Thyro-PX** (5000 A/1000 V, explicitly transformer/furnace loads) [RT-V04-03]; **Watlow** POWERGLIDE/ASPYRE + owned Eurotherm EPower [RT-V04-04]; **CD Automation** ships MoSi2/SiC-specific firmware today [RT-V04-06]; **Spang/AMETEK HDR** do custom MV furnace systems. (c) China: **英杰电气 (Yingjie/Injet, 300820.SZ)** — thyristor controllers plus multi-MW polysilicon reduction-furnace supplies (~70% share; Si rods Joule-heated ~1100 °C) [RT-V04-12/13]; graphitization-furnace rectifier sets (2800 °C class) are commodity there; integrated electric rotary calciners (400–1000 °C) list publicly [RT-V04-16]. (d) **Sublime/Electra** are ambient electrochemistry — they buy rectifiers (C39 territory), shrinking the "electrified cement" TAM that ever buys this product [RT-V04-14].

## 4. Physics reality check
">1000 °C process" forces element temps 1100–1600 °C → MoSi2/SiC/graphite. MoSi2 cold resistance ≈ short (10x swing) → tapped step-down transformer, thyristor on primary [RT-V04-05]; SiC ages +3–4x resistance → voltage headroom/taps [RT-V04-07]; graphite wants tens of volts at kA. No element accepts 1–7.2 kV at terminals; the MV interface is a transformer primary — exactly what DirectConnect/Spang switch now. "Universal MV controller" collapses to a configurable transformer-primary family + analytics; a SiC-MOSFET stage adds dv/dt/EMI/failure modes in kiln dust against a 99%-efficient thyristor that costs less. Also unproven: radiant "retrofit sections" inside a gas-suspension preheater — pilots heat gas (Prothal) or use induction/IR, none per-zone radiant at scale.

## 5. WTP skepticism
Conch 2024: revenue −36%, net profit −25% ($1.01B); sector price war/overcapacity through 2025–26 [RT-V04-15/17]. China ETS cement entry ~2027 opens with free benchmark allocation — weak carbon price until 2030s. EU pilots are Horizon/Innovation-Fund money (ELECTRA €20M) — grant-fed demand, the C27 lesson. No buyer quote anywhere supports $250K–1M/zone.

## 6. Founder-fit doubts
Not PhD-lane, but C1=5 leans on UHV/high-T *lab* packaging. MV product reality = IEC 62271/UL 347C arc-flash engineering, creepage/clearance, kiln-site EPC sales into FLSmidth/Sinoma procurement — absent from the graph, no named relationships. At 50/60 Hz thyristor scale the FPGA/high-density edge isn't decisive. 5→4.

## 7. Score adjustments (±1, reasons)
| C | raw→adj | reason |
|---|---|---|
| C1 | 5→4 | MV cert + cement sales cycle outside capability graph |
| C2 | 4→3 | "edge" rests on element-temp/controller conflation; DirectConnect exists |
| C3 | 4→3 | named beachhead programs already partnered (FLS in-house, ABB, Kanthal) |
| C5 | 4→3 | ETS-2027 free allocation + margin collapse pushes WTP past 2030 |
| C7 | 4→3 | merchant slot occupied both tiers, both geographies |
| C8 | 4→3 | "China >1000 °C open" false at power-supply level (Yingjie) |
| C4/C6/C9/C10/C11 | hold | expansion real; C6=3, C10=3 already penalized |

**Adjusted total: 66.8** (Σ=334/5; −12.8 vs raw).

## 8. Steelman
If ELECTRA-class element calcination clears demo scale 2028–2030, kiln OEMs will want a vendor-neutral second source for the power + element-health layer rather than buying Kanthal end-to-end, and no LV SCR incumbent packages dust-rated MV switching with per-zone degradation prediction as one product. Winning 3–5 pilot skids in that window could set the de facto interface before incumbents react — a real path, but narrow, post-2029, and gated on someone else's heat-transfer physics succeeding first.
