# RED TEAM — C30: Fast + accurate isolated current-sensor modules for WBG power systems

Verdict summary: the one-pager's core premise — "the speed+accuracy combination is unproductized" — was already false at time of writing. Kill-probability estimate: **75%**.

## Strongest bear case

The white space closed in October 2025. Allegro shipped the **ACS37100**, marketed as the industry's first production-ready **10 MHz TMR** current sensor (50 ns response, 26 mA RMS noise), explicitly targeting GaN/SiC control loops in EVs and AI datacenters [RT-C30-01]. The one-pager's own evidence [S178] is Allegro's *next* release (ACS37017, "highest accuracy," Feb 2026) — i.e., the incumbent is visibly converging speed and accuracy on a quarterly cadence with a captive TMR fab (Crocus, acquired for $420M) and automotive quals. Meanwhile **LEM publicly claims TMR with <1% accuracy and >10 MHz bandwidth** and has a TDK partnership to supply TMR dies for its integrated-sensor line [RT-C30-02][RT-C30-03]. By a 2029–30 launch, a solo founder's module arrives ~4 years behind two incumbents who each announced the same roadmap in 2024–25. That is the kill shot: not that it can't be built, but that it will be a catalog part before Tim incorporates.

## Hidden competition (what the one-pager missed)

- **Allegro ACS37100** — the productized 10 MHz TMR the pager says doesn't exist [RT-C30-01].
- **LEM + TDK** TMR integrated-current-sensor co-development; LEM's whole "sensor IC" push is aimed here [RT-C30-03].
- **Melexis** MLX91229 digital-output sensor for 200–2000 A traction inverters (June 2026) [RT-C30-10]; Infineon XENSIV line iterating annually.
- **Metrology flank:** Hioki **CT6904A** fluxgate, DC–4 MHz at ±0.02% rdg, phase-corrected by the PW8001 analyzer [RT-C30-04]; **Danisense DT-series**, 2 MHz bandwidth with <2 ppm linearity [RT-C30-09]. The "expansion to LEM/Danisense tier" runs into shipping products with 50–500x better specs.
- **Speed flank:** PEM **CWTMini50HF** Rogowski, 30–50 MHz, the default DPT probe [RT-C30-05].
- **China:** the import-substitution angle [S182] is being filled domestically, not by US startups: **希磁 Sinomags** (¥703M 2024 revenue, #1 Chinese magnetic-sensor IDM, IPO underway, own German wafer fab) [RT-C30-07]; **多维科技 MDT** closed-loop TMR transducers claiming 0.1–0.2% total temp drift [RT-C30-06]; **纳芯微 NOVOSENSE** NSM series (100 μΩ, 200 A, 5 kVrms) [RT-C30-08].

## Physics/engineering reality check

"<0.1% *lifetime* accuracy at >10 MHz" is a spec-sheet chimera. (1) There is no practical traceable calibration of current amplitude at 10 MHz to 0.1% — AC-current standards and phase-corrected metrology top out far below; you cannot even *verify* the claim, only the DC/low-frequency portion. (2) A TMR/fluxgate hybrid means a kHz-bandwidth fluxgate loop crossed over to an open TMR path; crossover flatness, phase, and thermal tracking of two dissimilar transducers is exactly where 0.1% dies at production tolerances (conductor position, package stress, magnetization aging). (3) Best-in-class Chinese closed-loop TMR already concedes 0.1–0.2% over temp [RT-C30-06]. The edge evaporates from "0.1% lifetime, 10 MHz" to "~0.5–1% wideband," which is Allegro/LEM territory.

## Market skepticism

Who pays for both specs *simultaneously*? Control loops need speed and tolerate ~1% (buy a $3–8 IC). Efficiency/loss metrology needs accuracy at defined frequencies and already pays $3–10K for Hioki/Danisense [RT-C30-04][RT-C30-09]. DPT rigs need 30+ MHz and tolerate 1–2% (PEM, ~$1–2K) [RT-C30-05]. The $200–2K/channel positioning lands in the gap where no documented buyer sits; the pager cites zero customer evidence of willingness to pay. Automotive inverter design-ins additionally require AEC-Q, PPAP, and dual sourcing — structurally closed to a solo seed-stage vendor.

## Founder-fit doubts

Technical fit is real; commercial fit is not. Component businesses are won on distribution (Digi-Key/Arrow), automotive quality systems, and price — none of which a solo PhD has. "Possible ASIC later" implies $5–15M NRE against Allegro's owned fab. Multi-year qual cycles collide with a 2029 finish and seed budget.

## Score adjustments

- **Whitespace/competition: −1** — headline claim falsified by ACS37100 [RT-C30-01].
- **Defensibility of edge: −1** — spec combination unverifiable/unreachable at production tolerance.
- **Market/WTP: −1** — no identified buyer needs both specs at the proposed price point.
- **Founder fit: hold** — skills genuinely match; the problem is the business, not the person.

## Steelman rebuttal

A believer would say the gap is *form factor and price*, not raw specs: nothing today gives 1–2 MHz-flat, 0.1%-class, phase-characterized measurement in a $500 embeddable module — ICs are inaccurate, Hioki/Danisense are $5K benchtop boxes — and DPT-rig integrators (C23 synergy) plus datacenter power-validation teams would embed dozens per rig. Incumbents chase automotive volume, leaving the test/validation mid-market underserved. Digital self-calibration IP, not the transducer, would be the moat.
