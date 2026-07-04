# D07 — Space & Harsh-Environment Electronics

## Landscape

Three adjacent categories sit inside this charter. (1) **Satellite electric-power subsystems** —
power processing units (PPUs) conditioning bus power for electric-propulsion thrusters, and power
conditioning/distribution units (PCDUs) managing solar MPPT, battery charge, and bus regulation.
The global small-satellite PCDU segment was valued at roughly $189M in 2024, projected to $299M by
2031 (~7% CAGR) [D07-01]. (2) **Radiation-tolerant power/compute modules** built on a "COTS-plus"
qualification model — screening commercial silicon/SiC/GaN parts to MIL-PRF-19500/883/38534 flows
rather than fabbing dedicated rad-hard silicon — now dominant for LEO constellations because it
"significantly reduces development time and cost" versus ground-up rad-hard design [D07-02].
(3) **Downhole/geothermal high-temperature electronics** — sensor/power electronics that must
survive 200–400°C in oil/gas and enhanced-geothermal (EGS) wellbores, funded by DOE materials
programs since the ARRA era and reaccelerating with the EGS boom [D07-04][D07-15][D07-16]. A
fourth, newer thread — **orbital data-center power** (100kW–GW-class solar/thermal systems for
space-based AI compute) — is early-stage but well-capitalized (Google, NVIDIA-partnered Starcloud,
a16z-backed Orbital, Star Catcher) and is fundamentally a power/thermal problem, not a compute
problem [D07-05][D07-03][D07-06][D07-07].

## Pain points & buyers

- **Thruster/PPU supply crunch.** SDA's ~500-satellite Tranche buildout plus commercial
  constellations created a Hall-thruster/PPU shortage — industry cites system-wide need near "100
  thrusters a month," with Astra's near-bankruptcy (owner of major HET producer Apollo Fusion)
  contributing to delaying SDA Tranche 1 from Sept 2024 to summer 2025 [D07-08]. Buyers: SDA and
  primes — Tranche 1 transport-layer awards ran $382M–$700M per 42-satellite batch (~$9–17M/sat)
  [D07-10] — plus smallsat primes like Terran Orbital and Capella Space forced to redesign around
  unreliable propulsion suppliers [D07-08][D07-09].
- **Hardened-electronics lead times.** Maxar flagged intense competition for space-qualified parts
  as a supply-chain risk on par with propulsion; DoD's Office of Strategic Capital opened ~$1B in
  direct lending across 31 defense supply-chain gap areas, space electronics included [D07-09].
- **Rad-hard fab capacity.** The US is subsidizing rad-hard fabs directly — up to $170M to
  SkyWater for a 90nm SOI rad-hard process, plus Sandia MESA's 150mm→200mm wafer transition —
  because commercial rad-hard supply is bottlenecked in a handful of legacy fabs [D07-11].
- **Downhole thermal ceiling.** DOE-funded work targeted 300°C circuit boards because commercial
  polyimide boards then topped out at 200–250°C [D07-04]; Utah FORGE's own tools are speced only to
  225°C against DOE's >375°C EGS resource target [D07-15][D07-16]. Buyers: oilfield-service majors
  and EGS developers like Fervo Energy (Cape Station: >10MW in a 30-day test, targeting 90MW by
  2026, 400MW by 2028) and DOE's Utah FORGE site (>90% water recovery at ~370°F) [D07-12].
- **Orbital data-center power/thermal bottleneck.** A single 700W H100 needs 1.4m² of 60°C
  radiator; a 100MW orbital data center needs ~2,500 radiators over 2,500m² — IEEE Spectrum:
  "the math won't make sense for several years, if ever"; Starcloud (seeking FCC approval for
  88,000 sats) has deployed one H100 with insufficient radiator capacity [D07-06]. Orbital
  Inference targets ~100kW-class satellites and is still investigating GPU radiation-hardening
  [D07-03]. Buyers: hyperscalers and orbital-startup partners [D07-07][D07-03].

## Incumbents & gaps

PPU/PCDU incumbents are legacy primes — Airbus, Thales, Leonardo, SITAEL (300–1500W PCDUs) — plus
NewSpace suppliers AAC Clyde Space, ST Engineering, Bradford Space, Vectronic Aerospace [D07-01].
None has shown the mass-production cost curve 10,000+-satellite constellations need, a direct
contributor to the SDA bottleneck [D07-08][D07-10]. In rad-hard power semiconductors, Microchip,
Renesas, and Vicor dominate DC-DC supply via COTS-plus — start from a proven commercial part,
requalify to space screening — which cuts dev time but still needs per-device radiation
characterization and restricts component selection while size/weight/efficiency budgets stay fixed
[D07-02]. Gap: rad-hard wide-bandgap devices remain an open reliability problem — a Tier-1 study of
1.2kV SiC devices under 45MeV proton irradiation found breakdown-voltage shifts from under 1%
(best edge-termination, RA-JTE) to 15.2% (worst, field-limiting rings), showing edge-termination is
still a first-order, evolving design variable, not a catalog-level spec [D07-18]. No incumbent
sells a qualified high-power-density WBG converter with radiation performance as a headline spec.
In downhole electronics, most published work is thermal-management workarounds (vacuum flasks,
PCM, active TEC cooling) bolted onto 120–175°C-rated parts rather than electronics that natively
survive 300°C+ [D07-04].

## 2029 inflections

NASA and DOE signed an MOU to deploy a lunar fission surface power reactor "by the early 2030s,"
building on Kilopower/KRUSTY, baselined at ≥40kWe (NASA has separately sought input on ~100kWe
systems under 15 metric tons) — a harsh-environment power-electronics demand pull with a hard
government deadline at the founder's 2029/2030 window, and the project now has a named NASA Glenn
lead confirming active staffing, not just a paper program [D07-13][D07-14][D07-21]. China's
Qianfan alone targets nearly 14,000 satellites by 2030, requiring 7+ satellites/day average —
roughly double Starlink's demonstrated cadence — through a supply chain that, unlike Starlink, is
not vertically integrated, giving independent PPU/PCDU/rad-tolerant suppliers a real opening
[D07-19]. Google's Project Suncatcher targets a two-satellite Planet-partnered launch by early
2027, betting on sub-$200/kg launch by the mid-2030s [D07-07]; Orbital Inference targets a 2027
Falcon 9 prototype and 2028 LA manufacturing line [D07-03] — both land just before the founder's
window, but IEEE Spectrum's own sourcing puts orbital data centers "10 to 20 years" out, arguing
for treating orbital-DC bets as high-variance rather than a 2029/2030 sure thing [D07-06][D07-03].
On geothermal, Fervo's ramp to 400MW by 2028 and DOE's EGS push toward >375°C systems (from a base
where most downhole electronics cap out at 175–225°C) create a multi-year window with no incumbent
high-temperature power module [D07-12][D07-15][D07-16].

## China notes

Beijing Junzheng (北京君正, SZSE:300223) posted FY2025 revenue of RMB4.741B (+12.5% YoY) and net
profit RMB376M (+2.7%), with 82.7% of revenue from overseas markets; Chinese financial commentary
identifies the company as a leading domestic supplier of radiation-tolerant chips for China's LEO
satellites, though the satellite product line's own revenue was not broken out in filings reviewed
and that specific market-share claim could not be independently verified this pass [D07-20].
Qianfan must sustain roughly double Starlink's historical launch cadence through a supply chain
that is explicitly not vertically integrated, a structural opening for independent Chinese
component suppliers rather than one prime capturing the whole stack [D07-19] — a direct China-
market analog to the SDA-driven US thruster/PPU shortage, on a more compressed timeline and larger
satellite count. No Chinese-language evidence surfaced of a comparable domestic push in ultra-high-
temperature downhole/geothermal electronics; that segment still reads as US/EU-dominated.

## Opportunity seeds

**1. Radiation-characterized SiC/GaN power module for next-gen constellation buses.**
Constellations moving to higher bus voltages need switches with radiation performance as a
designed-in, documented spec; Tier-1 proton-irradiation data on SiC edge-termination (sub-1% to
15%+ breakdown-voltage shift by design) shows this remains an active device-engineering problem
[D07-18]. SDA primes, having just absorbed a thruster/PPU shock, would pay for a well-characterized
module rather than a full catalog; a 2–5 person team with WBG device physics depth (the founder's
PhD focus) could own one voltage class, publishing its own radiation data as the differentiator,
without a captive fab. Standalone hardware sold to primes, not a diagnostic service. US
defense/NewSpace is the near-term buyer; a China-market variant could serve Qianfan/Guowang's
non-integrated supply chain via the founder's network, though export controls force two separate
entities.

**2. Qualified 300°C-native power-conditioning module for EGS downhole tools.** Fervo and Utah
FORGE both operate near the ceiling of what downhole electronics survive (FORGE tools speced only
to 225°C against DOE's >375°C target), and the standard fix — vacuum flasks/PCM/active cooling
around 120–175°C parts — adds failure modes rather than removing the constraint [D07-15][D07-16]
[D07-04]. EGS developers already spend millions per well and need production uptime they can't yet
buy [D07-12]. A small team combining WBG fabrication with harsh-environment packaging could sell a
drop-in module to MWD/LWD tool builders as a component, not a service — almost entirely a US/EU
market with no comparable Chinese EGS program found.

**3. Fast-turn COTS-plus rad-tolerant DC-DC converter shop for smallsat primes.** The core pain is
qualification lead time and lot-to-lot supply risk, not device physics — Terran Orbital and Capella
Space both had to redesign around unreliable suppliers, and government subsidy (SkyWater/Sandia,
DoD lending) signals a structural, multi-year hardened-power-parts shortage [D07-09][D07-11]
[D07-08]. A tiny team could own one converter family (e.g., isolated DC-DC in the 300–1500W band
Airbus/SITAEL serve today) and compete on qualification speed and a non-China-dependent supply
chain [D07-01]. Buyers are constellation primes and DoD-adjacent integrators paying a premium for
guaranteed lead time — standalone hardware, not testing-as-a-service.

**4. High-density, radiation-tolerant power-conversion payload for orbital power buses.** Every
serious orbital-data-center effort is power/thermal-constrained, not compute-constrained — Star
Catcher's own thesis is selling "power as shared infrastructure" via optical power-beaming rather
than building compute itself [D07-05]. A team with high-power-density power electronics and
precision analog depth could build a qualified converter or optical-power-receiver module and sell
it as a component into these programs rather than compete to build a data center. Because expert
sourcing puts orbital data centers "10 to 20 years" out, this should be funded as a power-
electronics component bet with near-term PPU/PCDU/converter revenue as the bridge, not a bet on
orbital compute landing by 2029/2030 [D07-06][D07-03].

**5. China-supply-chain-independent PPU/PCDU line for the Qianfan/Guowang buildout.** Qianfan must
sustain roughly double Starlink's cadence through a supply chain built from multiple separate
entities rather than one vertically integrated prime [D07-19]. A founder with native Chinese and a
real industry network could found a China-domiciled PPU/PCDU or rad-tolerant power-module supplier
sized for the 300–1500W smallsat band, competing against incumbents like Beijing Junzheng's
satellite line on delivery speed [D07-19][D07-20][D07-01]. This must be a separate legal entity
from any US-facing hardware business given export-control walls, but it directly matches the
founder's stated dual US/China scope.
