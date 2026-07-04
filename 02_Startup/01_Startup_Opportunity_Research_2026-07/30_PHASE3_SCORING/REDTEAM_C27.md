# RED TEAM — C27: 300°C-native power-conditioning modules for geothermal/downhole tools

**Verdict summary: kill probability ~80%. The merchant 300°C niche already has DOE-funded incumbents, and the buyers are an oligopoly that builds in-house.**

## Strongest bear case

The addressable market by 2031 is a rounding error, and it is already served. The one-pager treats ">375°C EGS wells" [S158][S159] as demand, but that is FORGE research-program language, not commercial procurement: the actual commercial EGS fleet (Fervo Cape Station, Sage, Eavor) drills mostly in the 175–230°C band precisely so it can use standard oilfield tools; Fervo's single 500°F (260°C) well is an envelope-push press release, not a tool order book [RT-C27-08]. Meanwhile the merchant high-temperature electronics slots are occupied: Honeywell's DM300 ASIC family on HTSOI4 already operates at 300°C and is sold into MWD/drilling [RT-C27-03][RT-C27-04], and Ozark IC has spent a decade and 22 SBIR/STTR awards (~$9M) building exactly "300–500°C geothermal data-logging and drilling electronics," shipping its AQ-200 XNode [RT-C27-01][RT-C27-02]. A 2029 solo entrant arrives third into a micro-market during an oil capex downturn.

## Hidden competition (what the one-pager missed)

- **Honeywell Aerospace**: HTMOS/HTSOI product line, 225°C continuous for 5 years, DM300 at 300°C, already designed into MWD control and permanent monitoring [RT-C27-03][RT-C27-04].
- **Ozark Integrated Circuits**: DOE-funded 300–500°C geothermal electronics, DOE SBIR Phase II for high-temperature directional-drilling communications — the same beachhead, same funder [RT-C27-01][RT-C27-02].
- **CISSOID**: 225°C SOI/SiC gate drivers, power-supply chips and intelligent power modules sold into oil & gas for 20 years [RT-C27-05]; Tekmos plays the same band.
- **Service-major in-house programs**: Halliburton already fields LWD for geothermal wells with static temperatures to 325°C [RT-C27-06]; Baker Hughes holds the exclusive power-unit contract for Fervo's Cape Station [RT-C27-08]. SLB, Halliburton and Baker Hughes dominate MWD/LWD [RT-C27-09] and vertically integrate tool electronics — they buy chips, not third-party modules.
- **National labs**: Sandia packages 300°C systems and has patented 400°C AlGaN/GaN downhole sensing electronics [RT-C27-10][RT-C27-11]; NASA Glenn's 500°C SiC ICs are license-ready [RT-C27-12]. Labs license to incumbents, compressing any startup edge.
- **China**: domestic players (CNOOC Welleader, Bohai Drilling's 230°C components) lag at the 175°C threshold [RT-C27-13][RT-C27-14] — confirming the China angle is weak, but also confirming how small and hard this market is even for state-backed programs.

## Physics/engineering reality check

The module is only as strong as its weakest passive, and at 300°C the shelf is nearly bare: standard power ferrites have Curie points ≤250°C (300°C ferrite exists only as research material) [RT-C27-15]; electrolytics are impossible; high-temp MLCC/film-cap offerings top out around 200–260°C with derating [RT-C27-16][RT-C27-17]. "Buys dies" is also shaky — no commercial GaN power FET is qualified near 300°C junction, so C27 quietly implies custom die, contradicting "low cleanroom dependence." Everyone hits the same passives wall; the founder's GaN physics does not unlock it. "24 months to qualified module" ignores 1,000+-hour life test plus field trials on someone else's drill string.

## Market skepticism

Who signs the PO? Commercial EGS developers number about six (Fervo, Sage, Eavor, GreenFire, Teverra, Zanskar) [RT-C27-07] and they buy drilling services from Baker Hughes/Halliburton, not power modules. Independent MWD builders (APS Technology, Scientific Drilling, Gyrodata) are small and cost-driven. The WTP evidence cited is DOE program pages [S158][S147], not customer contracts. And the oil/gas "expansion" market is contracting: upstream capex is falling a second consecutive year in 2026, EIA sees WTI averaging ~$51, and the US oil rig count is down 33% since 2022 [RT-C27-18][RT-C27-19] — HT-tool R&D is the first line item cut.

## Founder-fit doubts

Solo Stanford EE PhD, zero oilfield channel. Downhole sales run through Houston relationships, field-trial slots on customer rigs, and multi-year qualification (shock/vibration, HPHT autoclave, mud exposure) that requires capital equipment a seed budget strains to buy. Sales cycles of 2–4 years against a 2029/2030 launch means first revenue ~2032. The "telemetry/health firmware" software story is thin — incumbents' tools already do downhole health monitoring.

## Score adjustments

- **Market size/beachhead: −1** — ~6 EGS developers plus an in-house-building MWD oligopoly [RT-C27-07][RT-C27-09].
- **Competition/moat: −1** — Honeywell DM300 and Ozark IC already occupy merchant 300°C [RT-C27-01][RT-C27-04].
- **Timing/macro: −1** — second straight year of upstream capex cuts into the launch window [RT-C27-18].
- **TRL/feasibility: −1** — 300°C passives/magnetics are research-grade, not catalog parts [RT-C27-15][RT-C27-16].
- **Founder-fit (technical): +1 justified only if superhot (>300°C) GaN die work is the actual product; as a module play, keep as-is.

## Steelman rebuttal

A believer would say the incumbents sell chips and data loggers, not integrated power-conversion modules — the power-dense 300°C DC-DC/motor-drive slot is genuinely empty, and Fervo's 260°C well shows commercial EGS is marching toward it. DOE superhot programs will pay for the qualification a seed company can't, and the same module wins aero-engine and space-adjacent markets that decouple it from oil prices. If geothermal's venture wave compounds through 2031, the first native-300°C power module owns a defensible, physics-gated niche.
