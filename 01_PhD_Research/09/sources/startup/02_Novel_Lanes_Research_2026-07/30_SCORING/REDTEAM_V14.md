# RED TEAM — V14 Brand-agnostic trolley-assist retrofit interface for mining haul trucks (lane G08)

Date 2026-07-03 · Raw 76.8 · Sources: `30_SCORING/REDTEAM_V14_sources.json` (RT-V14-01..22)

## 1. Novelty verification (G7-NOVEL)

Nearest ledger neighbors checked: **C04** + **PWR-12** (MCS truck-charging modules / depot core): plug-in stationary DC charging for road trucks — different buyer (road-depot operator), connector (MCS plug vs. pantograph/catenary), cert path (road vehicle vs. mine site). **C01/C03** (marine/off-highway MW propulsion inverters): those sell the traction inverter; V14 feeds an EXISTING OEM drivetrain. **R1** (robot actuation) unrelated. No ledger entry covers dynamic current collection for mining haulage. **Verdict: NOVEL — G7 passes on ledger terms.** The duplication is not in the ledger; it is in the commercial market (§3): the category exists and is owned by others.

## 2. Strongest bear case

The buyers already procured this idea — from someone else. BHP/Rio Tinto/Vale ran the industry-wide OEM-agnostic dynamic-charging RFP in 2021–22 (Charge On Innovation Challenge; 8 winners incl. ABB, Siemens, Hitachi, BluVeinXL) [RT-V14-03]. The miners then co-funded **BluVein** (OEM-agnostic slotted-rail dynamic power, "any mine, any vehicle," trucks to 250 t; consortium incl. BHP, Rio, Vale, Freeport, Newcrest) — gen-4 hardware now testing at Heidelberg's Wolffdene quarry with ARENA support, TRL7 expected end-2026, mine trial 2027 under signed MoU [RT-V14-01/02]. BluVein IS V14, ~3 years ahead, with the prospective customers on its cap table. And the "mixed-fleet lock-out" premise is already false in the field: FQM's Sentinel hauls Komatsu 860E/960E AND Liebherr T 284 **on the same trolley line** — each OEM kit injects into its own drivetrain; the wire is the interoperability layer [RT-V14-04]. By 2031 V14 is a consortium-less follower selling the one layer OEMs will never open.

## 3. Hidden competition the one-pager missed

- **BluVein1/XL** (Olitek+Evias JV) — the literal product, buyer-funded [RT-V14-01/02].
- **Caterpillar Dynamic Energy Transfer** (MINExpo, Sep 2024): energy to diesel-electric AND battery trucks in motion, arm fits "multiple truck models," MineStar Command integration [RT-V14-08].
- **Komatsu**: trolley assist "factory-fit or retrofit kit"; 830E-5s shipped since 2019 factory-prepped for retrofit; autonomous trolley 2025; onboard kits with Wabtec [RT-V14-05/06/07].
- **ABB eMine**: explicitly markets "open, OEM-agnostic" trolley/charging ("any truck equipped with the trolley interface... can be connected"); Aitik/Kevitsa/Copper Mountain infrastructure; Los Pelambres with Komatsu [RT-V14-11/21].
- **Siemens**: Sicat TT/SIMINE trolley line; Charge On winner with trolley + 6C LTO in-cycle charging; Sishen runs 29 trolley 860E-1Ks on Siemens drives [RT-V14-12/20, RT-V14-03].
- **Hitachi**: Kansanshi trolley fleet since 2012; world-first full-battery **+ trolley** EH4000 commissioned Apr 2026 [RT-V14-09/10]. Husab commissioned trolley 2023 [RT-V14-21].
- **China (zh search)**: no trolley-retrofit market forming — trade press itself asks why 架线供电 never spread [RT-V14-15]; the Chinese path is battery-swap + autonomy: CATL 骐骥 100 swap stations (Sep 2025, 300 planned), 伯镭科技 ~1,000 unmanned swap mining trucks, 国家能源集团 163 AHS trucks across 12 pits, 湘电 120 t battery truck [RT-V14-16/17].
- **Cautionary corpse**: First Mode — the OEM-agnostic ultra-class retrofit venture ($1.5B valuation 2022, 400-truck Anglo deal) filed Ch.11 Dec 2024; assets to Cummins for $15M [RT-V14-13/14].

## 4. Engineering reality check

2–4 MW at ~1.8–2.6 kV DC = 1,000–2,000 A through a pantograph with wire-acquisition load steps at 20+ km/h on rutting unpaved ramps. Torque/power coordination among wheel-motor inverters, retarding chopper, and line draw lives inside OEM traction software (Wabtec/Siemens/Cat/Hitachi). Without those APIs a third party cannot even author the ISO 19014 functional-safety case — the safety-related control parts are OEM-proprietary [RT-V14-18/19]. Magnuson-Moss does not cover commercial trucks; OEM/dealer warranty and MARC coverage on $5–6M trucks can be denied at discretion [RT-V14-22]. "v1 in 24 months with one mine pilot" ignores that Hitachi needed a Jun 2024–Aug 2025 trial to commission ONE truck [RT-V14-09].

## 5. Willingness-to-pay skepticism

Trolley capex concentrates in line + rectifier substation (Boliden: $31.2M for 4.8 km + 23 trucks; ABB >12 MW substation at Kevitsa) bought from ABB/Siemens and OEM dealers under MARC — no orphaned budget line for a third-party truck kit exists. Revealed preference: miners pooled money into Charge On and BluVein rather than paying merchant retrofitters; Anglo defunded the one retrofit champion it owned. Honest market size: active trolley sites ≈ Kansanshi, Sentinel, Aitik, Kevitsa, Copper Mountain, Sishen, Husab, Los Pelambres (coming), Kristineberg/Ravliden underground — order 10 mines, not 100, each already paired with an OEM+EPC stack. Pilot-to-fleet cycles run 3–5+ years (Kansanshi: 750 m test track 2012 → fleet).

## 6. Founder-fit doubts

Not PhD-lane, but still overscored: the founder's real edges (power density, FPGA control, harsh packaging) are not the bottleneck — OEM drivetrain access, a mining functional-safety organization, dealer/MARC channel politics, and mine-site credibility are, and the founder has none of the four. Seed capital cannot carry a live MW-class wire plus a loaned ultra-class truck.

## 7. Score adjustments (±1, reasons)

| C | Raw→Adj | Reason |
|---|---|---|
| 1 | 4→3 | Bottleneck is OEM APIs/mining channel/safety org — absent from capability graph |
| 2 | 4→3 | Pantograph/DC stage is commodity (Wabtec/Schunk-class); differentiating layer is OEM-locked |
| 3 | 4→3 | ~10 trolley mines worldwide, all OEM+EPC-paired; Sentinel proves mixed fleet solved at the wire |
| 4 | 4→3 | Underground plank collides with BluVein1/Epiroc-ABB-Boliden; autonomy layer is MineStar/Komatsu turf |
| 5 | 4→3 | OEM-agnostic RFP ran 2021–22; winners at TRL7 by end-2026 — 2029 entry is post-window |
| 6 | 3→2 | Cross-OEM MW injection without OEM cooperation: no ISO 19014 case, warranty/MARC denial |
| 7 | 4→3 | BluVein + Cat DET + OEM retrofit kits + ABB/Siemens occupy every layer |
| 8 | 4→3 | China chose battery-swap (CATL 骐骥, ~1,000 swap trucks); zh press: trolley never spread |
| 9 | 4→4 | Unchanged — decarb mandates real, no export exposure |
| 10 | 3→2 | Kansanshi 2012→2016; Hitachi 2024–26 for one truck; seed cannot fund the pilot |
| 11 | 4→4 | Unchanged — standalone if it existed |

**Adjusted total: 58.8** (was 76.8; −18.0 — worst stress delta in cohort).

## 8. Steelman

BluVein is still pre-TRL7 and slotted-rail (not catenary); Cat DET is unproven at fleet scale; nobody serves BelAZ/SANY/XCMG-heavy pits in CIS/Africa/Belt-and-Road that Western OEM kits ignore. If the founder signed ONE OEM lacking a trolley kit (a Chinese truck maker chasing export pits) as co-development anchor, the interface thesis revives — but as an OEM partnership, not the scored merchant retrofit product.

**Recommendation: KILL (occupied whitespace + OEM-gated feasibility, not ledger novelty). Kill-probability 90%. Do not advance; pull a reserve seed.**
