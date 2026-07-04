# RED TEAM — C21: Compact wafer-level burn-in & stress-test cells for WBG power devices

## Strongest bear case
The "affordable gap below Aehr" does not exist. Aehr itself sells the FOX-CP, a low-cost single-wafer burn-in/test system, and the FOX-NP as a lower-capacity qualification entry point [RT-C21-01]; and in China, Semight Instruments (苏州联讯仪器) already ships a full WLBI product family (WLBI370A: 20 wafers HTGB; WLBI3810: 9 wafers HTGB+HTRB; WLBI3800: automated 6/8-inch, ±25 µm, 2,112 die in parallel) and claims 43.6% of the domestic power-device WLBI market — with a STAR-board IPO to fund expansion [RT-C21-02][RT-C21-03][RT-C21-05][RT-C21-05]. Worse, the market itself is tiny and cyclical: SiC WLBI was ~90% of Aehr's $65M FY2024 revenue and collapsed to <40% of $59M in FY2025 when EV demand softened [RT-C21-06] — global SiC WLBI equipment spend through the market leader is on the order of $25–55M/year. A solo founder launching v1 in 2030 enters a sub-$100M, boom-bust niche already bracketed from above (Aehr) and below (Semight) — that is how this dies by 2031.

## Hidden competition (missed by the one-pager)
- **Aehr FOX-CP/FOX-NP** — the incumbent's own down-market products; the one-pager cites Aehr only as "distracted by AI" [RT-C21-01].
- **Semight Instruments** (China) — dedicated SiC/GaN WLBI line, automotive-grade positioning, four SiC reliability product lines per DIGITIMES [RT-C21-02][RT-C21-07].
- **英铂 (YB Semi) OSTINATO WLBI** — second Chinese WLBI vendor [RT-C21-08].
- **华峰测控 (Accotest)** — claims global front-rank position in GaN test, ramping SiC/IGBT [RT-C21-09]; **长川科技 (Changchuan)** covers testers/handlers/probers.
- **Micro Control Company** — 50 years in high-power burn-in, HPB-8 handles >2,000 W/device [RT-C21-10]; **ESPEC** static burn-in systems [RT-C21-11]; **SPEA DOT800T** Si/SiC/GaN discrete testers [RT-C21-12]; **KES Systems** explicitly markets HV SiC burn-in expertise [RT-C21-13]; Chroma is in SiC power module test.

## Physics/engineering reality check
The founder's strength (kV/high-current stress electronics) is not the hard part. The hard part is full-wafer contacting at temperature: 50k+ contacts per touchdown, CTE-matched contactors, per-die current limiting so one shorted die doesn't take out the wafer, vacuum/pressure engagement — precisely the claims in Aehr's patent estate around WaferPak [RT-C21-14]. Avoid full-wafer contact and the product degenerates into a probe station plus a rack — which Semight already sells cheaper. Add kV HTRB across neighboring die at 150–175 °C and you inherit arc-over/partial-discharge management at production tolerances. The "1/10th price" edge evaporates into either patent risk or a me-too bench rig.

## Market skepticism
The beachhead is asserted, not evidenced. GaN power-IC startups largely *don't* buy WLBI: EPC and Navitas qualify via lifetime/test-to-fail studies and tout sub-1 FIT field data without burn-in-heavy screening [RT-C21-15]; GaN lacks SiC's Vth-drift infant-mortality driver, and cash-poor startups rent test houses rather than spend $300K–1M on capex. Second-tier SiC fabs are disproportionately Chinese and buy Semight, not an unknown US solo vendor. Aehr's FY2025 slump shows even Tier-1s cut burn-in capex first in a downturn [RT-C21-06].

## Founder-fit doubts
This is a production-floor system-integration business: wafer handling automation, thermal chucks, SEMI S2/CE safety compliance, 24/7 field service, and apps engineers resident at customer fabs. No fab buys a production tool from a one-person company that cannot guarantee uptime. Development cost of a credible v1 cell is multi-$M — beyond seed scale — and the China channel (the actual demand center) is closed to him. His skills fit C23's bench appliance, not this.

## Score adjustments
- **Competition/whitespace: −1** — FOX-CP + Semight falsify the claimed vacuum.
- **Market size/timing: −1** — leader's SiC WLBI revenue ≈ $25–55M/yr and shrinking in FY2025.
- **Feasibility/capital fit: −1** — production tool + field-service model exceeds solo/seed capacity; 18-month v1 not credible.
- **Founder fit: hold** — measurement expertise is real, but it transfers better to C23.

## Steelman rebuttal
A believer would say: JEDEC JEP203/204 (June 2026) forces mid-tier makers to generate stress data they cannot produce today; Aehr has visibly pivoted to AI processors and Semight can't sell into US/EU fabs under de-risking pressure, so a Western sub-$500K die/module-level (not full-wafer, hence patent-safe) burn-in cell rides the reshoring wave. Start with labs and pilot lines, then grow with the customers into production.

**Kill probability: 85%.**
