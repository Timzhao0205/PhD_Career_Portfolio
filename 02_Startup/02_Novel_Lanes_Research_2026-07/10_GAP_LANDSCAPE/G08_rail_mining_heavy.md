# G08 — Rail, Mining & Heavy-Industry Electrification Niches

## Landscape
Four markets share one physics base — pantograph/contact-line/cable-reel power transfer to a
moving or semi-fixed heavy machine — at different maturity points. Open-pit trolley-assist is
~50 years old in concept but only now scaling: Boliden's Aitik line (Sweden, 2018-) and Copper
Mountain's Canadian first (2022) are joined by Komatsu's autonomous dynamic-trolley 980E (2025)
and the Boliden/Epiroc/ABB underground battery-trolley truck (Kristineberg 2024; full-scale
Ravliden line, 5 km/750 m depth, ordered). Port RTG electrification is a mature cable-reel/
conductor-rail retrofit category now bifurcating into battery-buffered ("E-Hybrid," 2025) and
fully battery RTGs (first order April 2025). TBM/tunnel MV power is already electric at
multi-MVA scale (3.7-7.4 MVA/Herrenknecht site) but hand-engineered per project. Rail shunter
electrification splits between new-build modular platforms (CRRC VELFORCE, June 2026) and
one-off diesel-to-battery conversions (Heidelberg's 600 kWh "Battery Bill," April 2026).

## Pains & buyers
Mine operators (Boliden, Hudbay/Copper Mountain, Rio Tinto, Codelco, Fortescue) fund
electrification against diesel opex and carbon exposure: a 270-tonne-class haul truck burns
170-227 L/hr, and haulage is roughly 25-30% of a mine's Scope 1 emissions. Port
authorities/terminal operators (Georgia Ports, GCT, Gdynia) buy RTG retrofits against energy
cost and blackout risk, not just emissions. Quarry/industrial-rail operators (Heidelberg) and
tunneling EPCs (which rent, not own, TBM power gear) want bolt-on kit, not a new asset class.
Shared pain: the diesel/hybrid installed base is huge and slow to turn over — Georgia Ports
alone still runs roughly 100 non-cable-reel RTGs at one terminal — while full electrification
(new corridor, crane, or locomotive) needs capital and lead time most buyers can't absorb at
once, favoring narrow bolt-on power electronics over full-system EPC.

## Incumbents & gaps (price points)
- **Surface trolley-assist**: ABB eMine, Cat, Komatsu, Liebherr sell proprietary
  pantograph/drivetrain packages; capex concentrates in line/substation build, not the truck kit
  — Boliden spent $31.2M (2020-21) adding 4.8 km of line and converting 23 trucks across two
  mines. Gap: brand-agnostic pantograph-to-drivetrain interface electronics for older,
  non-OEM-integrated fleets.
- **Underground trolley**: brand-new, unstandardized — Kristineberg's 800 m/13%-grade test
  (2024) and the Ravliden order are ABB/Epiroc/Boliden-exclusive; Epiroc's own charging system
  (global, April 2026) is brand-agnostic for charging only, not dynamic trolley pickup. Gap:
  hardened, vendor-neutral underground trolley + peak-shaving battery buffer.
- **Port RTG retrofit**: cable-reel/conductor-rail is commoditized; new cranes run ~$1.9M/unit
  (Georgia Ports' 2019 order: 20 units, ~$38M). Konecranes' 2025 E-Hybrid needs only 60 kW grid
  feed vs. 400 kW for a direct cable-reel/busbar unit; the first purely battery RTG order landed
  April 2025 (GCT); Gdynia's EU-funded 7-crane retrofit (15 kV/41 t, 2023-25) pencils to a EUR
  10.9M NPV and >EUR 4.4M opex savings through 2033. Gap: vendor-agnostic battery-buffer retrofit
  for the large independent RTG fleet bought from many OEMs over decades.
- **TBM/tunnel MV power**: Herrenknecht/Danfoss/ABB drives are mature (Danfoss's Cogeis retrofit:
  5x225kW = 1,125kW into a 600-tonne TBM cutting a 22%-grade tunnel); every project re-engineers
  its own mobile substation/trailing-cable scheme. Gap: standardized, redeployable
  MV-distribution/voltage-compensation skid for repeat contracts.
- **Rail shunters**: new-build TSI-class battery platforms (CRRC VELFORCE) compete with bespoke
  diesel-to-battery conversions (Positive Traction's 600kWh Battery Bill). Gap: standardized
  conversion power-pack (drive+battery+BMS) for the large aging-diesel-shunter installed base.

## 2029 inflections
Industry roadmaps have pulled "zero-emission haul trucks at scale" forward from a 2040 view to
before 2030. Komatsu's autonomous dynamic-trolley truck (2025) and Boliden's full-scale
underground line (post-2025) should be in commercial ramp by 2028-29. Konecranes has committed
to a fully electric variant across its entire port-equipment line by 2026 — meaning 2027-29 is
when battery-buffer RTG retrofits move from first-order novelty to fleet-replacement decisions
at ports holding large legacy cable-reel bases. China's TBM export duopoly (CRCHI 33.8%
domestic share; China Railway Engineering Equipment Group 39.4% global share for 11 straight
years, exporting a 15.7m machine to Australia in 2025) ships machines faster than field-power
practice standardizes, opening a 2027-30 window for portable MV/voltage-compensation gear sold
alongside exported machines.

## China notes
CRRC's VELFORCE/Xuankun family (battery/hydrogen/diesel-hybrid variants for mines, ports,
steelworks; unveiled June 2026) signals the state OEM wants the new-build shunter segment; the
retrofit tail of China's existing diesel/hybrid shunter and RTG fleets stays open to smaller
suppliers. CRCHI and China Railway Engineering Equipment Group dominate TBM manufacturing and
export faster (34+ countries, Australia 2025) than standardized field-power infrastructure
follows. Tongli Heavy Machinery, with battery partner Qiyuan, delivered a 91-tonne battery-swap
(~7-minute swap) mining truck to Rio Tinto's Oyu Tolgoi project in Mongolia (Nov 2024) — a
China-origin battery-swap channel distinct from trolley-assist. IEA notes China's electric-truck
fleet already clusters on short, predictable routes around ports, mines, and steel plants — the
duty cycle favoring trolley/swap hardware over generic megawatt charging.

## Opportunity seeds
1. **Brand-agnostic pantograph-to-drivetrain retrofit interface** for open-pit trolley-assist,
   sellable across haul-truck OEMs (Cat, Komatsu, Liebherr, BelAZ, SANY, XCMG) rather than
   bundled with one vendor's truck. Avoids **C04** (MCS truck-charging modules): the buyer is a
   mine fleet operator, not a road-depot operator, and the interface is a rail-style current
   collector, not a plug-in MCS connector — a different product category and certification path.
2. **Hardened underground trolley pickup + peak-shaving battery buffer**, sold as a standalone
   power stage to underground hard-rock miners retrofitting existing loaders/trucks. Avoids
   **C01/C03** (marine/off-highway MW inverters): the product is the trolley-interface/buffer
   stage feeding an existing drivetrain, not a new traction inverter, and the buyer is a mine
   electrical engineer, not an off-highway OEM powertrain group.
3. **Vendor-agnostic battery-buffer retrofit kit for existing RTG cranes**, letting any-OEM
   cable-reel/conductor-rail RTG drop its grid-feed requirement the way Konecranes' E-Hybrid does
   for its own fleet — sold into the large independent crane base Konecranes/ZPMC don't already
   own. Avoids **C09** (MV-800VDC SST blocks): no solid-state-transformer stage, just a
   low-voltage buffer at the crane's native drive bus; also stays clear of **G03**'s water-side
   scope by remaining strictly land-side.
4. **Redeployable mobile MV-distribution/voltage-drop-compensation skid** for TBM/tunneling
   contractors, shippable project-to-project rather than engineered once and scrapped, sold to
   tunneling EPCs as rental-grade hardware. Avoids **C09** (SST blocks) by staying
   conventional-transformer/switchgear-based plus dynamic-compensation electronics, never a
   solid-state-transformer product.
5. **Standardized diesel-to-battery shunter conversion power-pack** (drive+battery+BMS,
   TSI/rail-EMC-certified) for quarry, port, and steelworks operators converting an existing
   diesel switcher rather than buying a new CRRC/Nexrail locomotive. Avoids **C01/C03**
   (off-highway propulsion inverters): rail traction duty cycle, voltage class, and certification
   path (TSI, rail EMC) differ materially from a marine/off-highway inverter line.
