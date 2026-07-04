# G02 — Plasma-Industrial Systems

## Landscape
Plasma-industrial = ionized-gas source + PSU + controls + recipe sold as one system, across
four demand pools: (1) surface treatment/activation — mature, $0.9-2.6B by scope, atmospheric
segment growing ~5.5-7.3%/yr to 2032 [G02-01][G02-08]; (2) waste/gas conversion — hazardous-waste
vitrification/gasification (thermal, 5,000-20,000K DC/AC arc torches, MW-class), CO2-to-syngas
(non-thermal/warm plasma, lab-to-early-pilot), VOC abatement (non-thermal + catalyst); (3)
metallurgy/recycling — plasma-arc melting, hydrogen-plasma smelting reduction (a steel/Ti
decarbonization route), e-waste/spent-potliner metal recovery; (4) agriculture/water —
cold-plasma seed treatment, plasma-activated water, PFAS destruction (non-thermal
plasma/plasma-vortex). Across all four, the plasma chemistry is decades-old, open literature;
what buyers pay for is a reliable, high-power-density, precisely-controlled PSU+recipe stack
driving a torch/jet/reactor a chemist or environmental engineer bolted together — a
power-electronics-and-controls problem, not a plasma-physics one, matching the founder's
WBG/HF-power-conversion + FPGA background more than a "plasma startup" profile would suggest.

## Pains & Buyers
Surface treatment: manufacturing lines (auto, medical device, electronics assembly, packaging,
textiles) pay $5k-$8k for a basic atmospheric PSU [G02-08]; pain is uptime and holding
surface-energy spec across web-speed/gas-purity drift — mostly open-loop control today.
Hazardous/industrial waste: buyers are municipal/industrial waste operators under regulatory
pressure — China's Feb-2025 guidance mandates new standalone incineration facilities exceed
30,000 t/yr and cuts landfill share below 10% by 2030 [G02-06]; pain is capex and reliability,
with mega-plants ($400M-$1B) chronically failing on tar formation, feedstock variability, and
weak hydrogen/syngas economics ($6-8/kg H2 vs. market, 40-60 t CO2/t H2 lifecycle) [G02-02].
PFAS: buyers are water utilities and DoD/AFFF sites on a hard EPA clock — NPDWR finalized
April 2024 for six PFAS compounds, 2029 deadline, opt-in extension to 2031 proposed (final rule
due spring 2026) [G02-14][G02-15]; sector compliance costs run $1.5-5.5B/yr, offset by ~$1B in
EPA grants plus $4B in state revolving funds [G02-15]. Agriculture: seed companies/co-ops want
germination consistency and lower pesticide load; USDA is still evaluating cold plasma as an
organic input, so no stable price point exists yet [G02-13]. Metallurgy: steelmakers, Ti
producers, battery/e-waste recyclers want decarbonization and critical-mineral security without
full-plant capex.

## Incumbents & Gaps
Surface treatment: Plasmatreat, Nordson (MARCH), Enercon, Diener, Tantec, 3DT — fragmented
EU/US suppliers, $5k-$8k entry PSUs [G02-08], mostly open-loop atmospheric jets; no dominant
Chinese brand surfaced despite China driving much of underlying demand — a gap for a
China-capable entrant. Waste/metallurgy torches: Tetronics (UK, DC transferred-arc, graphite
electrodes) and Europlasma (France, up to 4.0 MW transferred torch, ~1,500-hour electrode life)
are the named Western boutique suppliers — decades-old, electrode-life-limited, not
power-electronics-first. Full-plant gasification keeps failing economically (Tees Valley $1B
abandoned 2016, Plasco bankrupt 2015, Pune withdrawn 2025) [G02-02], while smaller bolt-on torch
modules on existing kilns are the pattern that actually ships: Foshan's 15 t/d plasma-melting
add-on to a 30 t/d kiln, CITIC's Dongguan project pairing a 30,000 t/yr kiln with a 10,000 t/yr
plasma stage [G02-10][G02-17]. CO2 conversion: D-CRBN (Belgium, EU-funded modular ARC/SPARC
reactors, ~2,000 t CO2/m2/yr claimed, up to 50% conversion) is the clearest packaged-system
competitor, still early-commercial, no public price [G02-07]. PFAS destruction: DMAX Plasma
(Potsdam NY, argon non-thermal plasma) and Onvector (MA/PA, plasma-vortex/arc) are US micro-cap
startups selling skids as a polishing stage after IX/RO/foam fractionation [G02-04][G02-05] — no
China-facing plasma-PFAS vendor surfaced. Common thread: none of these incumbents are
power-electronics specialists first; the PSU+controls layer is underserved across every
sub-segment.

## 2029 Inflections
EPA's PFAS compliance deadline (2029, opt-in extension to 2031, extension rule due spring 2026)
creates a hard procurement wave for destruction skids inside the founder's launch window
[G02-14][G02-15]. China's 30,000 t/yr minimum-scale rule plus <10%-landfill-by-2030 target forces
consolidation toward technology-forward, plasma-assisted waste centers through 2029-2030
[G02-06]. Hydrogen-plasma smelting reduction for steel/Ti is patent/licensing-stage now (ORNL,
2023) [G02-09] — 2029 is a pilot/demo window, not volume. Plasma-CO2 conversion and
plasma-nitrogen-fixation are both explicitly pre-pilot: a Nov-2025 review states plasma-NOx
synthesis suffers a "scarcity of pilot-scale developments" and needs techno-economic validation
before industrial translation [G02-11] — 2029 is realistically a first-deployment window, not a
market a startup enters late.

## China Notes
China is the most active state-linked developer of thermal-plasma waste torches. A
nuclear-institute-affiliated program has run plasma-waste R&D since the 1980s (30-300 kW DC arc
torch series, five patents), paused 2006-2019 under a policy requiring centralized medical-waste
centers, and resumed in 2019 with fluorine-organic-waste cracking systems; a 20 t/d system runs
~CNY 50M capex with a 3-year payback [G02-18]. CITIC Envirotech's Dongguan Haixinsha project
(broke ground June 2019) pairs rotary-kiln incineration with a plasma ash/slag stage, targeting
zero-discharge hazardous solid waste at 60,000+20,000 t/yr full build [G02-17]. Foshan's Huoshen
facility runs China's first coupled 30 t/d kiln + 15 t/d plasma-melting system [G02-10]. A
Shanghai official enterprise-outbound service center is explicitly pitching Chinese
thermal-plasma tech (5 MW-class hydrogen-plasma coal cracking, 20-30% energy savings) for
Belt-and-Road critical-mineral-refining exports [G02-12] — Beijing treats plasma-industrial as a
strategic export vertical, favoring a founder with real China networks to source components or
co-develop rather than compete head-on on torches themselves.

## Opportunity Seeds

1. **WBG retrofit PSU + arc-control module for legacy waste/metallurgy torches.**
Tetronics/Europlasma-class torches run ~1,500-hour electrode life on legacy supplies; a SiC
high-power-density PSU with closed-loop arc control, sold as a bolt-on to existing kilns (the
Foshan/Dongguan pattern, not a new mega-plant), targets the reliability gap that has killed
billion-dollar gasification plants. Avoids N08 (industrial pulsed power/PEF processing) by
staying in continuous-arc thermal torches, not pulsed-field processing.

2. **Field-hardened pulsed-arc PFAS destruction skid for utilities/DoD.** EPA's 2029-2031
compliance wave is a real buyer clock; incumbents DMAX and Onvector are chemistry-led, not
power-electronics-led. A harsh-env-packaged, high-power-density pulsed supply purpose-built for
plasma-vortex destruction, sold as a standalone polishing skid after IX/RO, is a clean product.
Avoids C36 (GaN medical ablation OEM platform) by staying in water/environmental remediation,
not tissue ablation.

3. **Compact containerized plasma-arc metal-recovery unit for e-waste/battery recyclers.**
China's nuclear-institute economics (~CNY 50M for 20 t/d, 3-year payback) show the model works;
a smaller (1-5 t/d), higher-power-density containerized version sized for Western
battery-recycling and e-waste plants avoids trucking waste to centralized Tetronics/Umicore-scale
smelters. Avoids C29 (smallsat PPU/PCDU — all space electric-propulsion power counts as
neighbor) by staying in terrestrial DC-arc melting, not spacecraft thrusters.

4. **FPGA closed-loop recipe controller retrofit for atmospheric surface-treatment lines.** The
$2.6-4.2B surface-treatment market runs mostly open-loop $5k-$8k PSUs; an add-on controller card
holding surface-energy spec across web-speed and gas-purity drift is a sellable retrofit, not a
new plasma source, and plays to in-situ sensing experience. Avoids N05 (solid-state RF/microwave
process heat) by controlling existing atmospheric discharge sources, not generating RF process
heat itself.

5. **Containerized on-farm plasma-nitrogen-fixation pilot skid.** A November-2025 review frames
plasma-driven NOx synthesis as explicitly decentralized/complementary to Haber-Bosch, with a
stated pilot-hardware gap; a small team building a gliding-arc-plus-catalyst skid sized for one
farm/co-op could reach a validated 2029 pilot ahead of any Haber-Bosch-scale competitor. Avoids
W-QUAISE (mm-wave/plasma rock-breaking for geothermal) by staying in atmospheric gliding-arc gas
chemistry, not mm-wave rock drilling.
