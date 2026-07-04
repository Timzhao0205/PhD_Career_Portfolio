# RED TEAM — C01: MW-class ruggedized SiC PEBBs for marine/off-highway/defense integrators

Reviewer stance: adversarial. Current matrix score 75.2, rank 15 — still too generous.

## Strongest bear case

The one-pager treats "PEBB" as whitespace when it is in fact a 30-year-old Navy program whose
productization was just awarded to a prime: ONR placed a $10.4M PEBB/HMMC **Phase 3** rapid-
prototyping order with GE Vernova Naval Systems for exactly the SiC-MOSFET modular building
blocks C01 proposes [RT-C01-01]. The named beachhead [S007] is therefore already occupied by the
incumbent the Navy chose. Outside defense, "MW bricks for integrators" is not underserved — it is
the core catalog of Danfoss (iC7-Marine modular liquid-cooled converters; Editron 30 kW–6 MW;
Danfoss Silicon Power selling *custom SiC power stacks* as a product line) [RT-C01-02][RT-C01-03]
[RT-C01-04], ABB (Onboard DC Grid, a modular DC power platform scaling to ~50 MW, plus a
"Compact" variant) [RT-C01-05], Sensata/Dynapower (defense-grade conversion, 100 kW–36 MW)
[RT-C01-06], and BorgWarner/Cascadia Motion (CM350SiC, 800 V iM-225W, explicitly marine/mining/
Class-8) [RT-C01-07]. A solo founder enters in 2029/2030 as the fifth-best-capitalized vendor of
a product category that already exists, with no cost, channel, or qualification advantage. Most
likely failure mode: two years of demos, zero design wins, because integrators default to
qualified incumbents for anything that can sink a vessel.

## Hidden competition

- **GE Vernova Naval Systems** — ONR PEBB/HMMC Phase 3, SiC-based, submarines to DEW loads [RT-C01-01].
- **Leonardo DRS Naval Power Systems** — >$3B Columbia-class electric-propulsion awards; owns the prime channel [RT-C01-08].
- **Danfoss** — iC7-Marine + Editron + custom SiC/IGBT power stacks: the exact "brick to integrators" model, DNV-typed [RT-C01-02][RT-C01-03][RT-C01-04].
- **ABB** — Onboard DC Grid modular platform, 10+ years installed base [RT-C01-05].
- **Sensata/Dynapower** — military-grade rectifiers/inverters/DC-DC to 36 MW [RT-C01-06].
- **BorgWarner/Cascadia Motion** — ruggedized SiC inverters for marine/off-highway [RT-C01-07].
- **China:** 中国船舶712所 — the state-designated marine electric-propulsion integrator with its own converter lines [RT-C01-09]; 中船赛思亿 (CSSC-SETH) — domestic series-produced marine frequency-converter power modules [RT-C01-10]; 汇川技术 — full marine propulsion-drive solutions [RT-C01-11]. The "China angle" is a CSSC-captive supply chain; a US founder sells nothing into it, and cannot serve both CSSC and the US Navy from one entity.

## Physics/engineering reality check

">100 W/in³ plus shock/vibe/salt" is a packaging-and-margin trade, not defensible physics: density
quoted at the brick level evaporates once filters, contactors, cold plates, and MIL-DTL-901
Grade-A heavyweight barge-shock qualification are added — the demanding, expensive test the plan
never budgets [RT-C01-12]. Incumbents already ship SiC stacks; nothing in C01's spec requires
knowledge they lack.

## Market skepticism

No cited source shows an integrator *buying* third-party bricks at $50–150K; [S007] is an ONR
program page (funding primes, not seed startups), [S014] is a DEW prime's own funding, [S022] is
Chinese aviation strategy. Marine integrators' actual behavior — buying from Danfoss/ABB or
building in-house (712所) — contradicts the catalog thesis. Worse, "catalog" and "integrator" are
in tension: every vessel/vehicle program wants custom voltage, cooling, envelope, and class-society
paperwork, which drags the startup into 18-month NRE projects — the very thing it claims to abolish.

## Founder-fit doubts

Solo founder vs. DoD reality: qualified-vendor lists, ITAR registration, DFARS/CMMC compliance,
3–5-year procurement cycles, and primes that demand financial-viability audits before designing in
a component that strands a ship if the vendor folds. No marine channel, no class-society (DNV/ABS/
shock) experience, and MW-class test infrastructure (dyno loads, MW supplies, shock/vibe rigs)
is $2–5M capex — far beyond seed scale. First revenue plausibly 2032+, after 2029/2030 launch.

## Score adjustments (±1)

- **C3 Beachhead: 4 → 3** — Navy PEBB already awarded to GE Vernova; primes don't buy bricks from seed-stage solos [RT-C01-01].
- **C7 Whitespace/moat: 3 → 2** — Danfoss/ABB/Dynapower/Cascadia ship this category today [RT-C01-02..07].
- **C8 China+US: 3 → 2** — CSSC-captive Chinese chain plus ITAR wall makes the dual angle illusory [RT-C01-09][RT-C01-10].
- **C10 Capital efficiency: 3 → 2** — MW test + heavyweight shock qualification is multi-$M pre-revenue [RT-C01-12].

## Steelman rebuttal

A believer would note the incumbents sell either full systems or custom stacks with long NREs,
not a fixed-price, short-lead qualified *catalog* at Vicor-like usability — and that dozens of
small yards, USV builders, and mining OEMs can't get Danfoss's attention below ~$5M orders.
GE Vernova's award proves the Navy wants PEBBs and creates SBIR/STTR side-doors a technically
elite founder can exploit; the wedge is speed and density at the tier incumbents ignore.

---
**Verdict:** Candidate C01 · kill probability ~80% · biggest objection: the "whitespace" is
occupied — ONR's PEBB productization is already contracted to GE Vernova and the commercial tier
is Danfoss/ABB/Dynapower catalog territory, leaving a solo seed founder no defensible entry.
