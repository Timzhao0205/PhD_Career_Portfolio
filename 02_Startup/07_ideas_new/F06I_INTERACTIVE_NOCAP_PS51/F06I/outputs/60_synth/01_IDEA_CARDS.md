# Idea cards — the final 24, in rank order

One card per selected idea. Scores are P4 totals (out of 100); decisions
and residual risk are stage-30 verdicts; budgets are the decisive-
experiment figures from SELECTION.json; deep-dive pointers reference
outputs/50_deep/DEEP. Cards for repair-verdict ideas state their
conditions explicitly.

---

### 1. P3R2-D-02 — Reel-to-reel contactless REBCO tape quality metrology (Tier 1)

Hall-array Ic mapping plus delamination screening as certified acceptance
instrumentation for tape vendors and magnet builders. Score 81.9, high
confidence; survive/medium. Dual-market (US, China; Japan side).
Experiment: $120k blind Ic-correlation campaign, 5% threshold — the
portfolio's cheapest kill. Why now: contract-dated tape volume ramp
(HL-4, 20,000 km/yr target) with acceptance QC captive or conflicted;
the incumbent instrument is Ic-only by its own datasheet. Key kill:
vendor self-QC accepted as-is, or THEVA adds the delamination channel
first. Deep dive: D01.md. Synthesis note: the portfolio's best
ratio of evidence quality to experiment cost; the KLA-of-superconductors
frame survives every red-team scenario.

### 2. P3R2-C-01 — Certified merchant 800 VDC rack protection layer (Tier 1)

Hybrid solid-state breaker + precharge + IMD + hot-swap sequencing as an
embeddable certified shelf. Score 80.5, high confidence; survive/medium.
Dual-market (US, China; TW/JP side). Experiment: $350k brassboard —
<100 µs clearing, 10,000 hot-swap cycles, arc discrimination. Why now:
NVIDIA's own architecture documents name the protection gap for the 2027
Kyber generation; China's OAII forum admits no 800 V certification
regime exists. Key kill: spec absorption — a reference protection design
shipped by shelf vendors before the UL/IEC path completes. Deep dive:
D02.md. Synthesis note: heaviest v1 capital in Tier 1 ($8-20M), bought
down by a cheap decisive experiment and an early-certification strategy.

### 3. P3R2-C-05 — Liquid-cooling conformance metrology and TTVs (Tier 1)

Programmable multi-kW thermal test vehicles, rack-scale load emulators,
and a round-robin conformance protocol. Score 78.3, high confidence;
survive/medium. Dual-market (US, China). Experiment: $150k — 16-zone TTV
plus blind three-lab round-robin. Why now: eight vendors build to
Google's Deschutes spec with no independent conformance method; OCP
still publishes only guidelines. Key kill: OCP releasing a complete
methodology with reference hardware first — managed by the
join-don't-race posture. Deep dive: D03.md. Synthesis note: strongest
founder fit in the portfolio (5/5); TAM ceiling honestly carried, with
licensing economics as the proof burden.

### 4. P3R2-D-10 — Coherent-beam-combining phase-control engine (Tier 1)

Channel-scalable electro-optic phase control (FPGA/ASIC + modulator
front-ends) for directed-energy primes and ultrafast OEMs. Score 78.7,
high confidence; survive/medium. US-only (ITAR by design). Experiment:
$250k — 16 channels, λ/30 rms, >90% combining efficiency under 1g
vibration. Why now: JLWS awards executed ($847M combined ceiling), Navy
beam-control line item awarding from Q4-2026, no merchant vendor
exists. Key kill: primes classify and internalize with no JBCS
carve-out. Deep dive: D04.md. Synthesis note: the design-win window
(2026-2028) runs ahead of the 2030 launch — the plan does the teaming
now as pre-company work; industrial ultrafast is the structural hedge.

### 5. P3R2-E-14 — Multi-terminal DC protection relay + HIL qualification (Tier 1)

Vendor-neutral fault-discrimination relay plus the qualification bench
that sells first. Score 75.5, high confidence; survive/medium.
US-primary (KR side; CN license-only). Experiment: $300k — HIL benchmark
of three published algorithms plus a <1 ms relay prototype. Why now:
three developers hold committed capital (GBX $1.7B awards; Southern
Spirit $2.6B; Grid United pipeline) under FERC 1920, with no neutral
protection authority. Key kill: US DC staying point-to-point with
protection bundled in vendor stations through 2034. Deep dive: D05.md.
Synthesis note: the red-team resequencing (qualification first, relay
second) converts pipeline schedule risk from survival risk to timing
risk.

### 6. P3R2-A-14 — 300 °C mixed-signal instrumentation platform (Tier 1)

SiC/SOI chipset + qualified packaging + modules for superhot geothermal,
downhole, and turbine sensing. Score 74.8, high confidence;
survive/medium. US-only (JP side channel). Experiment: $850k staged —
$250k packaging gate (500 thermal cycles) before the $600k
300 °C/1,000 h drift campaign. Why now: three service majors committed
to superhot projects targeting 2030 while the only merchant HT
mixed-signal line (CISSOID CHT, via X-FAB process termination) went to
last-time-buy — a realized supply gap. Key kill: superhot slipping past
2030, or Ozark/in-house teams capturing the sockets. Deep dive: D06.md.
Synthesis note: most expensive experiment in the portfolio, staged so
packaging failure costs $250k; Ozark's active status precisely restated
per the red team.

### 7. P3R2-D-01 — Merchant HTS quench detection and protection (Tier 1)

Co-wound fiber sensing + deterministic fusion + qualified energy dump,
sold with a certification-grade dossier. Score 72.9, medium confidence;
survive/medium. US-only (KR/JP side; CN licensing footnote only).
Experiment: $250k — instrumented REBCO pancake, ≥100 ms warning, <1%
false triggers. Why now: a merchant magnet market now exists (CFS to
Realta/WHAM) and REBCO quench detection is physically hard in exactly
the way voltage taps cannot fix. Key kill: no-insulation windings
sufficing at pilot scale, or CFS open-sourcing its stack. Deep dive:
D07.md. Synthesis note: the top ten's most conditional demand case —
ecosystem-level, not product-level — with the 2028 co-test milestone as
the explicit conversion test; a call option priced at $250k.

### 8. P3R2-A-10 — Closed-loop ion-energy control for plasma etch (Tier 1)

Wafer-level IEDF metrology fused with tailored-waveform bias control as
a vendor-neutral retrofit. Score 74.2, medium confidence;
**repair**/medium. Dual-market with conditions: US-primary; CN chapter
rebuilt to mature-node scope via non-listed counterparties behind a
hard 2027 counsel gate (original CN customers were Entity-Listed/VEU-
blocked). Experiment: $450k — closed-loop ±2 eV IEDF hold under drift
plus etch-profile correlation. Why now: sub-2 nm control pain is public
in Advanced Energy's own disclosures and no closed-loop product exists
anywhere (Semion is measurement-only, verified). Key kill: integrated
IEDF inference from generator vendors, or OEM data lockdown. Deep dive:
D08.md. Synthesis note: the repair conditions are structural, not
cosmetic — FTO analysis and the CN gate are dated 2027, before
productization.

### 9. P3R2-C-13 — Precision GaN pump-driver and laser-power modules (Tier 2)

Nanosecond-class programmable current drive as a merchant subsystem for
laser OEMs. Score 74.2, medium confidence; **repair**/medium.
Dual-market with conditions: CN leg must re-target Han's Laser (screens
clean) or fully domestic content — Raycus is blocked; two-entity
partition from day one. Experiment: $180k — 8-channel 1 kA driver with
closed-loop TMI trial on a university amplifier. Why now: nLIGHT's
executed JLWS ceiling and record A&D growth pull US drive electronics;
China's fiber-laser price war forces cost-down outsourcing. Key kill:
OEM not-invented-here holding — fewer than two paid evaluations by 2028
folds this into D-10's platform. Synthesis note: Tier 2 because its
buyer set overlaps D-10; the fold-in path is explicit, so capital is
never stranded.

### 10. P3R2-F-01 — Solid-state microsecond RF impedance matching (Tier 2)

Switched SiC/PIN capacitor arrays replacing motorized vacuum-capacitor
matchboxes. Score 73.2, medium confidence; **repair**/medium.
Dual-market with conditions: CN chapter restructured to AMEC-direct
(not Entity-Listed) with counsel-cleared licensing; the HK routing
scheme is dropped. Experiment: $250k — 13.56 MHz/5 kW matcher, <10 µs
re-match versus >100 ms baseline. Why now: pulsed and tailored-waveform
processes tune in microseconds while the flagship incumbent match
remains electromechanical at <500 ms on its own datasheet. Key kill:
AE/MKS integrating solid-state matching as a platform feature before a
merchant design win. Synthesis note: complementary to A-10 (same
chambers, different layer); sequencing them avoids competing for the
same evaluation bandwidth.

### 11. P3R2-A-05 — Merchant NEG-coating and UHV/XHV surface line (Tier 2)

US coating line for accelerator, quantum, EUV, and space-simulation
chambers. Score 72.1, high confidence; survive/medium. US-only (CN
chapter deliberately absent — IP-leakage rejection stands). Experiment:
$250k — TiZrV on 1-m pipes, ≤200 °C activation, sticking coefficients
within 20% of SAES-class, independent outgassing bench. Why now: EIC
long-lead procurement approved and PIP-II completing 2028 against a
sole-source Italian merchant line. Key kill: SAES announcing US
capacity, or accelerator budgets stalling. Synthesis note: the
portfolio's purest sole-source-relief play; high confidence, modest
ceiling, clean geography.

### 12. P3R2-C-09 — Standardized solid-state pulsed-power modules (Tier 1)

Stackable Marx/modulator modules with digital droop control and an open
interface. Score 72.0, medium confidence; survive/medium. Dual-market
(US, China partitioned; KR side). Experiment: $500k staged — two-module
50 kV/500 A stack, 1% droop, mid-campaign module-swap requalification.
Why now: cargo/isotope procurement compounds on both legs while the
incumbent verifiably moves toward more proprietary integration. Key
kill: OEMs refusing external drive chains — no design-in by 2033 (the
seed's own kill, preserved). Deep dive: D09.md. Synthesis note: CGN
Dasheng excluded from the base case (Entity-Listed parent); civilian
tender flow carries the CN leg.

### 13. P3R2-C-22 — Electrolyzer degradation-emulation and bankability benches (Tier 1)

Programmable ripple/intermittency benches with per-mechanism
attribution. Score 71.4, medium confidence; survive/medium. Dual-market
(US, China). Experiment: $250k — 50 kW stress-synthesis bench, 90-day
two-vendor campaign reproducing literature degradation signatures. Why
now: warranties priced ahead of degradation knowledge across ~$5B of
surviving hub cost-share and CN mega-tenders; the incumbent bench
vendor offers no ripple synthesis (verified). Key kill: hydrogen FIDs
collapsing on both legs, or Greenlight adding stress synthesis first.
Deep dive: D10.md. Synthesis note: the portfolio's electrochemical
diversifier — demand drivers uncorrelated with the datacenter, defense,
and fusion legs.

### 14. P3R2-C-08 — Thermal-shock-tolerant printed-circuit heat exchangers (Tier 2)

Merchant diffusion-bonded recuperators qualified for rapid transients
(sCO2 power, heat pumps, hydrogen precooling). Score 69.0, medium
confidence; survive/**high**. Dual-market (nuclear-qualified line
US-only; CNNC-internal sourcing honestly unproven). Experiment: $600k —
subscale core, 1,000 cycles at ≥20 °C/min with 550 °C peaks, ASTM E139
creep data. Why now: NRC Part 53 in force, STEP at supercritical
conditions, first CN commercial sCO2 waste-heat plant generating
revenue; no vendor publishes rapid-transient qualification. Key kill:
no ≥10 MW-class merchant sCO2 order by end-2033, or Heatric/VPE
publishing transient-qualified lines first. Synthesis note: highest
Tier-2 hardware risk per dollar; the transient-qualification dataset is
the moat if the market arrives.

### 15. P3R2-G-03 — DC-conversion acceptance and commissioning instrumentation (Tier 2)

Portable measurement island plus standardized acceptance protocols for
legacy-to-DC power-room conversions. Score 67.8, medium confidence;
survive/medium. Dual-market (CN via licensed entity; State-Grid work
out of scope). Experiment: $300k — GaN perturbation injector on a
100 kW 800 VDC testbed, instability prediction across ≥20
configurations. Why now: the DC transition is architecturally
unconverged and no system-level 800 VDC acceptance solution exists
(Chroma/Keysight/Hioki verified). Key kill: operators accepting vendor
self-certification (no frame agreement by 2029), or instrument majors
shipping DC acceptance suites first. Synthesis note: the measurement
side of C-01's market — deliberately not another in-path power product;
the stale HVDC penetration figures are flagged for re-sourcing and are
not load-bearing.

### 16. P3R2-E-04 — Cryogenic interconnect loader with co-packaged 4 K readout (Tier 2)

Superconducting flex + cryo-CMOS multiplexing + cryo-LNA breaking the
256-channel-per-loader wall. Score 67.9, medium confidence;
**repair**/**high**. US-only (TW/KR partners need case-by-case
licenses). Experiment: $500k — 256-channel flex + 4 K 64:1 mux segment,
<1% crosstalk, <20% coax heat load. Why now: the renewed $625M QIS
program and >1,000-qubit roadmaps collide with dilution-fridge heat
budgets passive cabling cannot solve; Delft/Bluefors ship passive
density (1,536 lines, 4,096 roadmap), leaving co-packaged cold
electronics as the unclaimed layer. Key kill: Delft/Bluefors adding
cold multiplexing to their integrated stack, or modular chip-to-chip
links becoming the scaling norm. Synthesis note: the repair narrowed
this idea to the co-packaged-electronics wedge after the density wedge
was lost — carried at high residual risk, priced accordingly.

### 17. P3R2-D-09 — Charge-buildup-immune FLASH/e-beam dose metrology (Tier 3)

The traceable ammeter for ultra-high-dose-rate beams. Score 67.4,
medium confidence; survive/medium. US-only. Experiment: $150k —
side-by-side cavity vs BCT vs Faraday at a FLASH linac, <1% calorimetry
agreement. Why now: two independent 2025 papers document BCT failure at
FLASH dose rates; NCI already bought this capability class through a
contract vehicle. Key kill: FLASH clinical stall plus PTW converting
its research detector into a traceable commercial reference first.
Trigger to exercise: FLASH clinical-qualification milestones 2028+.

### 18. P3R2-A-22 — Modular plasma destruction for concentrated PFAS streams (Tier 3)

Skid-scale destruction for spent AFFF, IX regenerant, membrane reject.
Score 66.9, medium confidence; survive/**high**. US-only (CN absence
verified bilingual). Experiment: $550k — >99.99% PFOA/PFOS destruction
on real AFFF concentrate at ≤50 kWh/kg with closed fluorine mass
balance. Why now: the AFFF statutory deadline (2026-10) and DoD's
Success-Memo pathway into ~700-site remediation. Key kill: a Success
Memo crowning SCWO for concentrated streams before the plasma
demonstration completes, or energy economics missing 50 kWh/kg.
Trigger: DoD demonstration-program sequencing decisions 2027.

### 19. P3R2-C-04 — PFAS-free pumped two-phase cooling loop (Tier 3)

Hermetic, fluid-agnostic evaporator/condenser co-qualified with
non-PFAS fluids. Score 66.6, medium confidence; survive/**high**.
Dual-market (US/EU regulation-anchored; CN PUE-driven). Experiment:
$400k — 2 kW loop on two candidate non-PFAS fluids vs Novec-era
baselines, 1,000 h degradation assay. Why now: AIM Act 2029 step-down
and EU F-gas 2030 ban collide with 3-5 kW packages — but Chemours'
Opteon 2P50 qualification narrows the wedge to the strictly
non-fluorinated scenario. Key kill: no non-PFAS fluid at
datacenter-scale qualification by 2031, or single-phase water
stretching another generation. Trigger: non-PFAS fluid qualification
progress through 2027-2028.

### 20. P3R2-D-19 — Composite-flywheel kinetic buffers for off-grid AI power (Tier 3)

Containerized magnetic-bearing flywheel strings smoothing GPU-cluster
swings. Score 64.9, medium confidence; survive/**high**. US-only (CN
licensing only). Experiment: $350k — 50 kW/2 MJ composite rotor on AMB
in vacuum, 100k microcycles, <1% loss growth. Why now: a named 400 MW
off-grid AI plant already procured flywheel stabilization; the
DC-native, microcycle-optimized entrant slot is open. Key kill: the
measured load-spectrum study showing rack-level smoothing suffices, or
BESS cycle costs closing the niche. Trigger: the load-spectrum study
result plus the 800 VDC (Kyber) socket materializing in 2027.

### 21. P3R2-F-16 — Inline-metrology plasma surface treatment (Tier 3, CN-primary)

Atmospheric/vacuum plasma cleaning with closed-loop surface-energy
metrology for PCB/advanced packaging. Score 64.8, medium confidence;
survive/**high**. CN-primary (the portfolio's only such structure; TW/KR
second wave; no US leg claimed). Experiment: $200k — lab plasma cell
with inline surface-energy proxy sensing and bond-strength correlation.
Why now: two independent open international tenders in three months; no
incumbent ships closed-loop treat-to-spec. Key kill: no paid premium
beta by 2028, or ACM/Nordson fast-follow. Trigger: a third open tender
naming metrology requirements, or a premium-commitment beta customer.

### 22. P3R2-F-19 — Coolant-health monitoring and conditioning skids (Tier 3)

In-service chemistry/particulate/bio-fouling telemetry with automated
correction for liquid-cooled fleets. Score 64.6, medium confidence;
survive/medium. Dual-market. Experiment: $300k — 12-month
accelerated-aging loop across three commercial coolants with a
failure-signature library. Why now: the 2024-2028 liquid-cooling cohort
reaches fluid mid-life at 2030 under spec regimes that define
installation but not operations. Key kill: CDU vendors bundling
coolant-health services into warranties before a merchant skid lands a
fleet. Trigger: first published fleet fluid-failure incidents, or a
CDU-vendor warranty carve-out appearing.

### 23. P3R2-F-23 — PEM electrolyzer protective-envelope controllers (Tier 3)

Embedded plant hardware shaping current/OCV stress with warranty-grade
black-box logging. Score 63.4, **low** confidence; **repair**/**high**.
Dual-market (CN via clean-counterparty OEM design-in). Experiment:
$300k — 2,000 h short-stack A/B with the binding requirement of
measurable degradation-rate reduction. Why now: degradation-ignorant
warranties are priced into ~$5B of surviving hub debt; underperforming
CN parks face retrofit audits. Key kill: the A/B showing no measurable
reduction, or lenders accepting OEM warranties without third-party
evidence. Synthesis note: deliberately paired with C-22 — bench
qualification (C-22) and embedded enforcement (F-23) are
non-overlapping layers; F-23 exercises only if C-22's attribution
science holds. Trigger: C-22 kill-gate outcome plus one lender
expression of interest.

### 24. P3R2-D-16 — Merchant space closed-Brayton conversion and PMAD (Tier 3)

100 kWe-class converter layer for fission surface power. Score 63.0,
**low** confidence; survive/**high**. US-only by law. Experiment: $500k
— 10 kWe He-Xe turboalternator rig at ≥20% cycle efficiency,
conditional on the 2028 program checkpoint. Why now: NSTM-3 directs a
funded multivendor ≥100 kWe-scalable program with the solicitation
opening now; every team currently rebuilds the converter captive. Key
kill: downselect passing without written subcontract interest from two
teams, or program slip past 2034. Trigger: the ~April-2027 downselect —
the cheapest possible hold until then (tracking only, no hardware).
