# RED TEAM — V03 Vendor-agnostic thermal-battery discharge power stage & controls

Date 2026-07-03 · Raw 81.2 · Sources: 30_SCORING/REDTEAM_V03_sources.json (RT-V03-01..11)

## 1. Novelty verification (G7-NOVEL)

Three nearest ledger neighbors: **PWR-15** (100-hour-optimized LDES power-conversion + BoP
skid), **RID-013** (LDES PCS, HOLD), **RID-015** (700 °C particle storage module). Also checked
**C39** (electrolyzer rectifiers — grid-to-electrochemical-load, different load, not duplicate),
**C09** (MV→800 VDC SST — different output, clean), **RID-026** (hybrid-plant supervisory
controller — V03's dispatch software overlaps it). Versus RID-015 the declaration holds: V03
sells no medium. Versus PWR-15/RID-013 it holds only while the "discharge power stage" is a real
electronics category. It is not (see §3): strip the hollow discharge claim and what remains is a
grid-facing power-conversion + BoP + dispatch skid sold to LDES developers — thermal batteries
ARE LDES; buyer segments coincide. That is "same product, new adjective" territory. **Verdict:
VARIANT (borderline)** — per ledger rule, borderline = excluded unless the material-difference
justification survives verification. It half-survives (SCR resistive control ≠ bidirectional
PCS topologically), so this is not an automatic G7 kill, but the differentiating half of the
declaration is factually empty. Recommend G7 borderline-fail → reserve.

## 2. Strongest bear case

By 2031 V03 is a controls-integration consultancy, not a product company. The premise inverts
reality on both sides of the bank. **Discharge:** Rondo discharges with a circulating blower,
water injection, and an OTSG/HRSG under patented in-house AI controls [RT-V03-01];
Brenmiller/Kraftblock/EnergyNest discharge into steam generators, turbines, Stirling or ORC
[RT-V03-10]; Antora discharges through proprietary TPV cells from its own 2 MW/yr fab
[RT-V03-04]. There is no common electronics product to standardize — only blowers on commodity
ABB/Danfoss VFDs, valves, and DCS. **Charge:** where electronics do live, merchant products
already exist at catalog: Watlow POWERSAFE integrates MV heater + SCR + PLC/HMI to 7,200 V /
20 MW [RT-V03-02]; Chromalox DirectConnect does 4,160 V multi-MW at ~99% [RT-V03-03]. The
one-pager's "no merchant product at any price" is false today.

## 3. Engineering reality check

"Common discharge interface" fails physics-of-the-product: heat leaves as mass flow (air/steam/
salt), not current. The inverter analogy fails because PV strings share a DC port; heat banks
share no electrical port. Across brick (air), salt (salt-to-steam HX), particle (particle-to-air),
TPV (semiconductor), the only shared layer is supervisory software — a DCS/optimizer, not a
"power stage." The extreme-edge claim thus attaches to no extreme electronics spec anywhere.

## 4. Hidden competition (missed by the one-pager)

China: 东方电热 300217.SZ wins 6 kV 熔盐电加热器及其控制系统 frameworks (Huaneng Xi'an Thermal
Institute) [RT-V03-05]; CSPPLAZA publishes an entire vendor directory of referenced molten-salt
heater/control suppliers [RT-V03-06]; park procurement runs EPC 总承包 with these packages.
West: Kanthal 1.3 MW/800 °C TES heater prototype [RT-V03-08]; Kyoto Group self-supplies the
"world's largest electrical heater for molten salt" at 93% [RT-V03-07]; PARAT electrode boilers
(0–75 MW, ~10 kV, >350 °C steam, 250 MW on German grid regulation) deliver dispatchable
power-to-steam with no thermal bank at all [RT-V03-09]. And the named buyer universe — Thermal
Battery Alliance members Rondo, Antora, ETS, RedoxBlox — are vertically integrated in-housers
whose controls ARE their margin story [RT-V03-11].

## 5. Willingness-to-pay skepticism

Nobody quoted. Integrators treat controls as core IP (Rondo: "patented AI controls"). Chinese
EPCs already buy heater+controls from listed domestic suppliers at SOE-procurement prices; a
$200–800K foreign controls layer on top of a Supcon/Hollysys DCS is an unfundable line item.
The "second-wave integrators" who supposedly pay are unnamed because they barely exist yet.

## 6. Founder-fit doubts

Not PhD-lane, but over-scored: the real work is SCR firing control, PLC/DCS glue, and blower VFD
specification — 50/60 Hz resistive loads need no WBG density, no fast dynamics, no harsh-env
packaging. The founder's actual edge sits idle; any industrial-controls house matches v1.

## 7. Score adjustments (±1, reasons)

| C | Raw→Adj | Reason |
|---|---|---|
| C1 | 4→3 | Commodity controls engineering; rare-combo edge unused |
| C2 | 3→2 | No extreme electronics spec; 1,500 °C lives in bricks; MV SCR = 40-yr parity |
| C3 | 4→3 | Named buyers in-house (Alliance); "second wave" unnamed; parks buy EPC bundles |
| C4 | 5→4 | Inverter analogy collapses — no common port; expansion reduces to software |
| C5 | 4 | Park/ETS/Heat Shot windows real and dated — keep |
| C6 | 4 | Trivially feasible — keep (weakness priced in C7) |
| C7 | 4→3 | Whitespace falsified: Watlow/Chromalox/Kanthal/东方电热 + electrode-boiler substitute |
| C8 | 5→4 | China channel EPC-locked around 300217.SZ; no entry wedge shown |
| C9 | 4 | No regulatory exposure — keep |
| C10 | 4 | Catalog hardware but pilot host must be a non-competitor — net keep |
| C11 | 4→3 | No standalone value without someone else's bank; controls un-outsourceable |

**Adjusted total: 67.6** (raw 81.2, −13.6).

## 8. Steelman

If heat batteries proliferate to dozens of sub-scale integrators and park EPCs, none will match
Rondo-grade dispatch intelligence, and a neutral price/process co-optimization layer (the
"Power Factors of heat") could win as software-first, pulling charge-side hardware later. The
Thermal Battery Alliance could even standardize interfaces a neutral vendor rides. But that is
a software company thesis, not this power-stage one-pager.

---
**VERDICT — V03 · Kill-probability: 85% · Biggest objection: the product's premise inverts
reality — discharge is thermal/mechanical BoP (or Antora's proprietary TPV) with no common
electronics to sell, while the charge side where electronics exist is already served by merchant
catalog (Watlow 20 MW/7.2 kV, Chromalox, 东方电热 6 kV heater+controls) and integrators keep
controls as core IP · Novelty: VARIANT (borderline PWR-15/RID-013 re-parameterization; G7
justification only half-survives).**
