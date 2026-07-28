# P3R2 elegance/novelty adjudication — independent second pass

Adjudicator: independent judge, claude-fable-5 / xhigh (configured route; no delegation).
Date: 2026-07-13. Inputs: `P3R2_A_us_pain`, `P3R2_B_china_pain`, `P3R2_C_dual_us_cn`,
`P3R2_D_wildcards`, `P3R2_E_jptwkr_side` (100 seeds: A=22, B=22, C=22, D=20, E=14),
`10_SOURCE_ATLAS/ATLAS.md` (including negative findings), `05_STATE/INDIA_SOURCE_ORIGIN_AUDIT.md`.
Firewall respected: the founder profile and the prior `SEEDS_A–D` drafts were **not** read; no
founder-fit content appears below. Seed files were not modified.

## 1. Methodology

Each seed scored 0–10 on **novelty, elegance, controllability, vision, timing-robustness**, with
verdict PROMOTE / FIX / REJECT.

- **Convergence-as-obviousness test.** The five batches were generated independently. When the
  same product appears in 3–5 batches, that is direct experimental evidence that "three smart EE
  founders reading the same atlas" converge on it. Cross-batch duplicates therefore cap novelty
  at 3–4 regardless of quality. This single finding dominates the adjudication: the 100 records
  reduce to ~46 distinct concepts (Section 2).
- **Atlas negative findings enforced:** no electrolyzer-stack economics (L11 overcapacity), no
  grid-forming-services reliance (NESO zero awards), no two-phase cooling without a post-Novec
  fluid plan, enthusiasm zones (EHD, plasma chemistry, metamaterials, EM launch) require a named
  demand bridge or explicit wildcard framing, and the two verified media-vs-primary gaps (L13
  "100% localization", L14 "100% liquid-cooling mandate") must not be load-bearing. Seeds were
  checked individually; violations are called out per seed.
- **Quarantine check:** no seed cites any of the 42 India-origin quarantined source IDs
  (grep across all five JSON files: zero matches). Clean.
- **2030 launch contract:** each seed judged for (a) pre-company 2026–2029 feasibility without an
  operating company (lab access, grant-scale budgets, LOI realism), (b) specificity of the
  2030–2034 trigger (named program/procurement/regulation vs vibes), (c) probability the window
  closes before 2030 (commoditization, incumbent absorption) or opens only after 2034
  (science-only, undated government programs), (d) meaningfulness of the kill date.
- **US/China independence (batch C):** demand logic must be independently evidenced per country;
  a real US case plus a mirrored "China will need the same" assertion is scored as fake-dual.
- **Selectivity convention for duplicates:** each duplicate cluster gets one canonical seed
  (PROMOTE, or FIX if the canonical itself needs repair); other members are REJECT with
  `duplicate_of` set and an explicit import note listing any unique content the orchestrator
  should merge into the canonical. This is a merge instruction, not a quality insult.

Verdict totals: **21 PROMOTE, 25 FIX, 54 REJECT.** 25 duplicate clusters spanning 62 seeds.

## 2. Duplication map (25 clusters)

| # | Cluster (same product, different wrapper) | Canonical | Duplicates / partials |
|---|---|---|---|
| 1 | 800VDC rack-inlet protection module | **C-01** | A-01, B-03, E-01 |
| 2 | MVDC hybrid solid-state breaker (hardware) | **A-02** | B-04 (blend w/ #1) |
| 3 | DC protection relay + HIL/compliance qualification | **E-14** | C-16; A-03 partial (field-MW emulator kept separate as FIX) |
| 4 | Tailored-voltage-waveform / closed-loop IEDF bias | **A-10** | C-06, B-05, E-03; B-21 adjacent (merge) |
| 5 | Cycling-rated PCHE recuperators | **C-08** | A-12, B-07, E-08 |
| 6 | Standardized solid-state pulsed-power modulator platform | **C-09** | A-07, B-09, D-05, E-05; C-20 adjacent (merge) |
| 7 | FLASH/UHDR beam-current & dose metrology | **D-09** | A-08, C-10 |
| 8 | Compact e-beam/X-ray sterilization machine | **D-08** (FIX) | A-09 |
| 9 | HTS quench detection + protection | **D-01** | A-04, C-17, E-07 (half) |
| 10 | REBCO tape/conductor QC & acceptance metrology | **D-02** | B-10, C-11, E-07 (half) |
| 11 | Mid-scale kW-class cryoplant skids | **C-12** (FIX) | B-11, D-03 |
| 12 | NEG coating / low-outgassing surface line | **A-05** | B-12 |
| 13 | Cryogenic I/O interconnect + 4K mux for quantum | **E-04** | A-06, D-17 |
| 14 | Precision laser-diode driver modules | **C-13** (FIX) | A-18, B-19 |
| 15 | Coherent-beam-combining phase control | **D-10** | A-17 |
| 16 | Low-ripple rectification retrofit (electrolysis/electrowinning) | **C-07** | A-19, B-13 |
| 17 | Recuperative battery-formation power | none (both rejected) | A-20, E-06 |
| 18 | Multi-MW heavy-fleet charging systems | **A-21** | C-15; B-14 partial (kept as FIX) |
| 19 | Liquid-cooling thermal test/metrology | **C-05** | A-15, B-02 |
| 20 | Flywheel transient buffering for AI power | **D-19** (FIX) | B-18 |
| 21 | Rad-tolerant GaN PPU platform | **A-13** | D-15, E-10 |
| 22 | 300 C-class harsh-environment electronics platform | **A-14** | B-17, D-14, E-09 |
| 23 | Ka-band metamaterial ESA radar tile | **D-18** (FIX) | E-12 |
| 24 | 2-micron EUV drive laser | **D-11** (FIX) | E-13 |
| 25 | sCO2 turbomachinery seals/bearings | **C-19** (FIX) | B-08 |
| — | Two-phase direct-to-chip loop | **B-01** | C-04 partial (FIX: adopt B-01 mechanism) |

## 3. Per-seed adjudication

Scores are Novelty / Elegance / Controllability / Vision / Timing.

### Batch A — US pain (22)

**A-01 — 3/7/7/6/7 — REJECT (duplicate of C-01).** Quadruple cross-batch convergence (A-01,
B-03, C-01, E-01) proves this is the single most obvious seed the atlas produces; the lane brief
practically dictates it. Well built, but C-01 is the stronger canonical (dual-market, same
evidence). Import into C-01: fleet-wide DC-arc-signature learning angle and the UL/IEC listing
path emphasis.

**A-02 — 5/6/6/8/6 — PROMOTE.** The MVDC breaker is the atlas's documented "showstopper" — a
genuinely hard, decade-scale switching problem with no incumbent product category, and the
productization-discipline wedge against per-project incumbents is credible. Risks judged real
but acceptable: MVDC adoption may stay point-to-point (window could slip past 2034), and the
$1.5M first experiment strains a pre-company budget — the 2026–28 plan should lean on ARPA-E
DC-GRIDS/ORNL facilities explicitly. Kill date 2034 is meaningful.

**A-03 — 6/6/7/6/5 — FIX.** Field-deployable MW-scale ride-through verification is a real
instrument gap and PRC-029-1 is a dated regulatory trigger, but the demand mechanism is
unproven: NERC compliance may settle on EMT-model evidence, which would strand the hardware.
Fixes: (1) obtain documented evidence (regional entity guidance or owner-operator LOIs) that
field hardware verification will be required or paid for; (2) drop the GFM-attestation leg
unless a US operator spec exists — the AEMO precedent is not a US buyer and NESO's zero awards
is an atlas negative finding; (3) keep as the field-hardware complement to E-14, not a rival.

**A-04 — 4/7/6/7/7 — REJECT (duplicate of D-01).** Same product as D-01/C-17/E-07. D-01 has the
sharper mechanism (co-wound Rayleigh fiber + CLIQ-class extraction) and the better decisive
experiment. Import into D-01: the acceptance-test protocol/warranty framing for merchant magnet
sales.

**A-05 — 6/7/8/5/7 — PROMOTE.** Single-source (SAES) global supply, a US sovereignty preference,
process know-how moat, cheap decisive experiment, and buyers who already specify NEG coating.
Vision ceiling is modest (niche scale) and SAES adding US capacity is the honest kill risk, but
as a wedge business with near-zero science risk it earns its slot. Only one other batch
converged on it (B-12, China variant) — moderately non-obvious.

**A-06 — 4/6/6/7/6 — REJECT (duplicate of E-04).** Triple convergence (A-06, D-17, E-04). E-04
is the most complete variant (adds cryo-LNA integration and the SEEQC–ITRI manufacturing
wedge). Import: A-06's channels-per-watt sales framing.

**A-07 — 3/6/7/6/7 — REJECT (duplicate of C-09).** Five-way convergence makes the modulator
platform the pool's second most obvious concept. C-09 carries the dual-market demand set.
Import: A-07's IEC 60060-1:2025 acceptance-protocol emphasis.

**A-08 — 5/7/8/5/6 — REJECT (duplicate of D-09).** Same UHDR metrology gap, same two source
papers. D-09's hybrid cavity+Faraday architecture and cheaper experiment make it canonical.
Import: the ISO 11137-1:2025 sterilization-QA channel detail.

**A-09 — 4/5/5/6/5 — REJECT (duplicate of D-08; weaker variant).** The in-house/factory-floor
sterilization model fights the industry's contract-sterilization structure and adds per-site
radiation-licensing friction the seed underweights; the EtO regulatory driver is admittedly not
in the accepted ledger. D-08 (merchant machine breaking the duopoly) is the better-shaped bet.

**A-10 — 4/8/7/8/7 — PROMOTE (canonical for cluster 4).** Closed-loop ion-energy control is the
pool's best physics-leverage wedge: the control variable (IEDF) is the process, incumbents sell
sources not measurement, and the pre-company plan is a genuine university-lab program.
Novelty capped by four-way convergence. Merge in: C-06's two-entity export partition (US
leading-edge / CN >=28nm) as the company structure, E-03's KR validation channel, and B-21's
arc/ESC-event detection as a product feature. Export-control counsel is a 2027 gate, not an
afterthought.

**A-11 — 5/6/7/5/5 — FIX.** The transient-MFC thesis is plausible (SEMI E17 codifies the pain)
but rests on two technical sources and a hope that Horiba/Brooks/MKS stay slow; OEM
qualification stickiness plus incumbent catch-up could close this before 2030. Fixes: (1)
evidence that a tool OEM or panel integrator will dual-source on transient specs (paid eval or
LOI by 2028); (2) broaden the technical base beyond L06-026/034; (3) quantify throughput value
in $/tool/year to justify the switching cost.

**A-12 — 3/6/6/7/6 — REJECT (duplicate of C-08).** Import: the catalog-frames-with-lead-times
commercial framing and the STEP Phase 2 / TerraPower buyer detail.

**A-13 — 4/6/6/7/6 — PROMOTE (canonical for cluster 21).** Real 50-year non-convergence, a
supplier base consolidated into a missile-focused parent, and a rad-tolerant GaN wedge with a
publishable SEE dataset as the pre-company artifact. SDA EP content honestly flagged as
unconfirmed — P4 must close it. Merge in: E-10's ECSS/AIAA qualification framing and JAXA–
Furukawa validation pattern; D-15's SEE-map-first sequencing. Prime vertical integration is the
standing risk; per-coil/per-bus module economics partially hedge it.

**A-14 — 5/6/7/8/8 — PROMOTE (canonical for cluster 22).** The strongest demand-timing story in
the harsh-environment family: funded drilling programs (SUPERHOT, FORGE) racing past the 225 C
commercial ceiling exactly as the two incumbent IC lines exit (CISSOID last-time-buy, Honeywell
legacy). Four-way convergence caps novelty, not quality. Merge in: E-09's packaging-first
qualification strategy and JP decommissioning-robotics side market; D-14's 400 C SiC-JFET tier
as the roadmap. In-house capture by SLB/Halliburton is the honest ceiling on share.

**A-15 — 4/7/8/6/7 — REJECT (duplicate of C-05).** Import: the post-PFAS fluid-qualification rig
line and the 1%-closure calorimetry spec — C-05's product list should absorb both.

**A-16 — 4/5/5/6/5 — FIX.** The TIM pain is real and documented, but "co-designed per package"
is consulting dressed as product, and Honeywell/Shin-Etsu/Indium can outspend the moment the
segment proves. Fixes: (1) define a productized SKU + qualified dispensing process license
(materials system + application equipment, not engineering services); (2) anchor-packager LOI
by 2028; (3) head-to-head reliability delta vs two incumbent metal TIMs on a standard vehicle —
already in the experiment, make it the kill gate.

**A-17 — 4/7/6/7/6 — REJECT (duplicate of D-10).** D-10's channel-scalable controller
(16→1,000+ channels, ASIC path) is the crisper canonical. Import: ruggedized deformable-mirror
control and the NNSA EYC demand leg.

**A-18 — 3/6/7/5/6 — REJECT (duplicate of C-13).** Triple convergence. Import: diode-health
telemetry as the differentiator language.

**A-19 — 4/6/7/6/6 — REJECT (duplicate of C-07).** Import: the US tankhouse/H2Hub beachhead
sequencing and the measurement-and-verification protocol for financiers.

**A-20 — 3/5/6/5/3 — REJECT.** Hidden-commodity finding: Chroma/Hioki/Digatron/PEC already ship
recuperative formation lines; the residual wedge ("plant-level pooling + grid services") is a
feature incumbents can bolt on before 2030. Demand evidence is market-structure-only; named US
plant demand admittedly absent. Twin seed E-06 self-labels "highest commoditization risk in
this batch" — the label is correct for both.

**A-21 — 4/5/6/6/6 — PROMOTE (canonical for cluster 18).** Demand quality is the draw: EPA Clean
Ports money is obligated, FLXdrive and Cat 793 XE fleets are named, and the harsh-duty
(dust/vibration/45 C) niche is unserved by truck-EVSE vendors. Elegance is honestly mediocre —
this is an integration play, and OEM-bundled charging (Wabtec/Cat) is the structural threat;
CARB repeal shows the regulatory floor can move. Merge in: C-15's dual-standard option and
B-14's interface-personality concept as optional modules. Keep because demand evidence is
top-decile even if physics leverage is not.

**A-22 — 5/6/6/7/7 — PROMOTE.** Respects the plasma enthusiasm-zone rule by anchoring on paid,
delivered DoD PFAS destruction; the wedge (verified destruction + fluorine mass balance in a
container) is a defensible instrument-plus-reactor combination; SCWO competition honestly
named. EPA-driver re-sourcing is correctly flagged for P4. One of only two L01 survivors, which
also protects lane diversity.

### Batch B — China pain (22)

**B-01 — 7/8/7/7/7 — PROMOTE.** The one mechanism-level original in the entire thermal family:
sub-atmospheric two-phase water/low-GWP loops that are leak-safe by physics (air leaks in),
PFAS-independent by design, with the ITRI 2.4 kW/chip result as existence proof and GB 40879 as
a dated, correctly-quoted trigger (the seed explicitly refuses the debunked "100% liquid
mandate"). Foreign-founder access is honestly routed through licensing/ODM design-in. This is
what a China-primary seed should look like. C-04 should adopt this mechanism (see C-04).

**B-02 — 4/6/8/6/7 — REJECT (duplicate of C-05).** Import: T/CIEP 0263-2025 clause-scripted
reporting and the sell-benches-to-domestic-certification-labs channel strategy.

**B-03 — 3/6/6/6/6 — REJECT (duplicate of C-01).** As a standalone China-first play it is
dominated by Huawei/Delta in-house engineering and Autrans-class incumbents; the licensing
route survives only as the CN chapter of C-01. Import: virtual-impedance bus-oscillation
damping and capacitor-health telemetry features.

**B-04 — 3/6/6/6/6 — REJECT (duplicate blend of C-01 + A-02).** The "park/industrial mid-layer"
between rack vendors and State Grid houses is a real observation, but the product set is the
same SSCB + arc-detection stack already canonical elsewhere; CCC/GB certification and JV
requirements erase the margin for a foreign entrant by 2030.

**B-05 — 4/7/6/7/4 — REJECT (duplicate of A-10).** The seed's own export-control paragraph
("SEVERE... counsel before any China engagement") concedes the lawful channel may not exist for
advanced-node RF subsystems into AMEC/NAURA. That is not a fixable footnote; it is the thesis.
The CN opportunity survives only as the partitioned >=28nm line inside A-10's structure.

**B-06 — 6/7/7/6/6 — FIX.** The ESC electronics gap (clamp-force observer, arc-safe declamp,
multi-zone thermal drive) is a genuinely under-picked subsystem with real coupled-physics
content, and the ceramics-maker channel is clever. But the seed itself admits the China demand
evidence is inferential — no named tender or program. Fixes: (1) P4 must produce a named ESC
localization program, tender, or a ceramics-maker co-development LOI; (2) scope initial product
to mature-node/panel/display tools to stay inside the export-control lane; (3) confirm the
electronics half is not already bundled by AE/MKS in a way that forecloses the socket.

**B-07 — 3/6/6/6/6 — REJECT (duplicate of C-08).** Import: graded-channel/compliant-header
mechanism language and the CNNC "first-set" follow-on procurement logic. The RMB100bn
single-source TAM stays flagged.

**B-08 — 4/6/5/6/5 — REJECT (duplicate of C-19; self-labeled optional).** Narrow SAM,
JV-only access, institute buyers. C-19 carries the concept with the same honesty and a US leg.

**B-09 — 3/6/7/6/6 — REJECT (duplicate of C-09).** Nuclear-SOE procurement (CGN) is
foreign-hostile; the seed's own access mitigation (HK trading structures) is thin. Import: the
3 kV brick + per-stage droop correction implementation detail and CIRC/Atom Hi-Tech tender
evidence into C-09's CN chapter.

**B-10 — 4/6/7/6/7 — REJECT (duplicate of D-02 + D-01).** Bundles two canonicals (tape QC +
quench electronics). Import into D-02: the per-meter "conductor passport" data-infrastructure
framing and Chinese buyer set (Shanghai Superconductor, WST, ASIPP).

**B-11 — 4/5/5/6/5 — REJECT (duplicate of C-12; self-labeled optional).** The seed concedes the
atlas has essentially no competitive intel on the Chinese cryo industry; that mapping belongs
to the C-12 FIX.

**B-12 — 4/6/6/5/4 — REJECT (duplicate of A-05).** The licensed-cell-into-China model runs
head-on into IP leakage in a process-know-how business, with lumpy CEPC-dependent demand and a
China-only bid rule that makes the licensee, not the founder, the accumulating asset.

**B-13 — 4/6/6/6/5 — REJECT (duplicate of C-07).** Sungrow as simultaneous buyer and
power-electronics giant is correctly identified as the decisive threat — which is exactly why
the CN-primary standalone fails while C-07's dual structure (US electrowinning beachhead)
survives. Import: Kuqa underperformance-retrofit evidence and degradation-weighted scheduling
IP language.

**B-14 — 7/5/6/6/5 — FIX.** Genuinely non-obvious standards-arbitrage insight (GB/T swap vs IEC
MCS non-recognition) with named export programs (XCMG–Fortescue, SPIC Oyu Tolgoi). But the
product exists only if the swap ecosystem exports and Western sites accept dual-standard
hardware — a contingency, not a demand base. Fixes: (1) by 2028, documented evidence that one
named export program will procure dual-standard interface hardware; (2) pre-agree the fold-in
path: if swap fails offshore, this becomes an interface-personality module inside A-21; (3)
keep the certification-burden moat argument, it is the best part.

**B-15 — 3/5/6/5/4 — REJECT.** Mid-market industrial plasma power in China is a
features-per-yuan knife fight the seed itself describes; Hengyunchang/Injet moving down-market
plus domestic price collapse make this a commodity trap by 2030. The arc-quench IP does not
carry a company against that cost curve.

**B-16 — 4/5/6/6/4 — REJECT.** Open-hardware White Rabbit means the hardware is born commodity;
what remains is support-and-integration — consulting-shaped revenue against Chinese institute
control groups that publish at ISSCC level and self-supply. Add China-only procurement rules
and US quantum export-control scoping, and there is no defensible product core for a 2030
foreign entrant.

**B-17 — 4/5/6/6/4 — REJECT (duplicated by A-14 canonical).** The seed's own demand paragraph
concedes the atlas contains no named Chinese HT-electronics procurement and the L15 brief
documents the transparency asymmetry. A China-primary company on inferential demand fails the
mission's demand rule; the CN option can be revisited from A-14 if evidence appears.

**B-18 — 3/5/6/5/5 — REJECT (duplicate of D-19).** Demand-bridge admitted absent (no named
Chinese flywheel-datacenter buyer); the Piller precedent is a US/Western data point. D-19
carries the concept where the precedent actually is.

**B-19 — 3/6/7/5/6 — REJECT (duplicate of C-13).** Import: the price-war-driven up-market
OEM pivot logic (Han's/Raycus filings) as the CN demand chapter of C-13.

**B-20 — 2/4/6/4/3 — REJECT.** Self-labeled "weakest-thesis seed... kept as a discardable
extra" on 2021-vintage data against entrenched domestic incumbents with >50% buyer
concentration. Correctly self-diagnosed; discard.

**B-21 — 5/6/7/5/6 — FIX.** Real gap (generator-agnostic arc/ESC-event protection with only one
open-literature detection method), but the seed admits small ASP and a patent thicket. Fixes:
(1) complete the FTO analysis before any further investment; (2) merge as the event-detection/
forensics layer of A-10 (or bundle with B-06) rather than a standalone company; (3) mature-node
scope for export-control safety.

**B-22 — 6/7/7/6/6 — FIX.** Excitation-free ESR/RUL tracking via synchronous demodulation of
existing switching ripple is elegant and the failure physics is canonical; the honest risk is
being a feature inside vendor telemetry. Fixes: (1) one named design-win path — a PSU/UPS
vendor or third-party maintenance operator problem statement with an LOI by 2028; (2) define
the retrofit SKU + cross-vendor failure-database network effect as the moat; (3) keep the
US secondary market active so the company is not access-hostage to CN design-ins.

### Batch C — dual US/CN (22)

**C-01 — 4/7/7/7/7 — PROMOTE (canonical for cluster 1).** The best-evidenced version of the
pool's most convergent idea: genuine independent demand legs (OCP/NVIDIA 800V scaling in the
US; documented CN 800V integration pain L02-054 plus a low-penetration conversion base), honest
export-separability analysis, sensible dual-entity plan. It must absorb the cluster: A-01's
fleet arc-analytics, B-03's oscillation damping, E-01's arc-ROC dataset and TW/JP supply
wedges. Main structural risk remains hyperscaler/NVIDIA spec absorption — the kill trigger is
correctly defined.

**C-02 — 6/7/7/6/5 — FIX.** Electrolytic-free pulsed-load buffering via film caps + partial-power
conversion is a clean mechanism, and only one batch produced it. But it lives one OCP spec
revision away from absorption into reference PSUs/BBUs (the seed says so itself). Fixes: (1)
codify the kill trigger — if NVIDIA/OCP specs an in-rack buffer or Delta/Vicor ship one by
end-2029, fold into C-01 as a feature; (2) quantify cost parity vs brute-force electrolytic
banks + BBU (the incumbent "good enough"); (3) get one integrator eval agreement by 2028.

**C-03 — 5/6/5/8/4 — FIX.** The certification-first SST thesis ("the blocker is certification,
not physics") is a real insight and OCP Mount Diablo's SST track is new demand the ARPA-E decade
lacked — but the atlas's own negative finding (10+ years funded, still standards-blocked) plus
$25–60M v1 capex makes this the batch's most schedule-fragile seed. Fixes: (1) hard 2028 gate on
IEC 60076-24-class progress and an OCP SST procurement signal; (2) pre-company scope strictly
limited to the HF-insulation/PD dataset and standards participation; (3) if the gate fails,
re-batch as a wildcard rather than carry MW-class capex risk.

**C-04 — 4/6/6/7/6 — FIX.** Correctly respects the post-Novec rule and the regulatory triggers
are genuinely independent (AIM Act vs GB 40879/T-CIEP). But as written it is a positioning play
("fluid-agnostic loop") without a mechanism edge, walking into ZutaCore/Accelsius/LiquidStack
plus Envicool. Fixes: (1) adopt a defensible loop architecture — merge B-01's negative-pressure
mechanism as the primary variant (leak-safe + fluid-flexible is a real wedge; me-too pumped
two-phase is not); (2) keep the fluid-menu qualification dataset as the second moat; (3) retain
the 2031 fluid-availability kill trigger.

**C-05 — 5/7/8/7/8 — PROMOTE (canonical for cluster 19).** Picks-and-shovels with documented
spec chaos as the demand driver (GB200 TDP/flow contradictions verified in-atlas), independent
US/CN legs (OCP ecosystem vs T/CIEP + GB PUE acceptance), trivial export exposure, tiny capex,
and a first experiment that doubles as marketing. TAM ceiling honestly flagged. Absorb A-15
(fluid-qual rigs, calorimetry closure spec) and B-02 (CIEP standards-body strategy).

**C-06 — 4/7/6/8/6 — REJECT (duplicate of A-10).** The best contribution is structural: the
US-entity/CN-entity (>=28nm) export partition, which A-10 must adopt. Kept out only because two
canonical TVW seeds would be one too many.

**C-07 — 5/7/7/7/6 — PROMOTE (canonical for cluster 16).** The one L11 play the atlas
affirmatively licenses: power-quality economics (documented 5–14% lever) orthogonal to stack
overcapacity, with a US electrowinning beachhead hedging hydrogen policy fragility and honest
recognition that Western OEM order books are shrinking. Sungrow verticalization is the CN-side
kill condition and is correctly monitored. Incumbent rectifier names must be sourced in P4 (the
seed flags this itself).

**C-08 — 4/6/6/7/6 — PROMOTE (canonical for cluster 5... PCHE cluster).** Both demand legs are
real and independent (STEP/Part 53/advanced-reactor BOP; Chaotan One + Xinjiang first-set).
Cycling qualification + code documentation is the right wedge for a component with no
acceptance standard. Manufacturing capex is the honest burden; the CN retrofit TAM stays
single-source-flagged until P4 triangulates. Absorb A-12 (catalog framing), B-07 (compliant-
header mechanism), E-08 (KAERI/Hanwha channel, TC Energy–Hanwha MOU).

**C-09 — 4/6/7/7/7 — PROMOTE (canonical for cluster 6).** Five-way convergence says obvious;
the demand set says durable (Varex cargo growth, EtO-replacement capacity, ARDAP base, CGN
Dasheng order book as CN mirror with honest access caveats). Absorb D-05's open-interface
standard strategy — that is the differentiating move incumbents (ScandiNova/Jema) cannot
follow without cannibalizing closed cabinets — plus E-05's hot-swap serviceability spec and
A-07's IEC acceptance protocol. C-20's SSPA line folds in as a product extension.

**C-10 — 4/7/7/5/5 — REJECT (duplicate of D-09; fake dual).** The CN leg is a mirrored
assertion — CGN Dasheng "needs the same dosimetry" with no CN procurement or regulatory
evidence. The US leg is already canonical in D-09.

**C-11 — 4/6/7/7/7 — REJECT (duplicate of D-02).** Import: the 10 kA cable/CICC acceptance
station and the financier/insurer data-package framing — both strengthen D-02's expansion path.

**C-12 — 5/6/5/7/5 — FIX.** The mid-band cryogenics gap (W-to-kW at 20 K) is plausibly real and
strategically valuable, but the competitive claim rests on one vendor spec sheet; the seed and
its B-11 twin both concede the incumbent map (Air Liquide/Linde turbo-Brayton lines, Stirling
vendors, Chinese makers) was never built. Export entanglement with quantum controls is flagged
but unresolved. Fixes: (1) P4 competitor mapping of the 100 W–2 kW @ 20 K band before any
promotion; (2) export-control scoping with the CN leg treated as license-only upside; (3)
staged capex — turboalternator subscale first, no full skid before a named buyer LOI.

**C-13 — 4/6/6/6/6 — FIX.** Merchant driver modules face the classic component squeeze:
in-house NIH at IPG/Raycus/Han's on one side, analog-semi reference designs on the other. The
TMI-aware pump-modulation firmware is the only durable differentiator on offer. Fixes: (1) 2028
OEM buy-vs-build discovery with documented willingness (two paid evals); (2) two-entity
US(DEW)/commercial partition from day one; (3) if OEM appetite fails, fold the driver line into
D-10's phase-control stack as its power stage.

**C-14 — 4/5/6/6/5 — REJECT.** The US leg leans on a tiny universe of torch OEMs that build
supplies in-house; the CN leg cites ASIPP PF-converter and RMP tenders — big-science bespoke
converters, not a merchant industrial-plasma-supply market — making the dual case a category
error. Core plasma-chemistry demand is an atlas enthusiasm zone. The remediation-anchored
version of this idea already exists as A-22, which is the better vehicle.

**C-15 — 4/5/6/6/5 — REJECT (duplicate of A-21).** The CN leg is demand-without-access: SOE
mine tenders and CATL/SPIC swap ecosystems are documented, but a foreign merchant charging
vendor has no realistic route against vertically integrated domestic stacks. A-21 carries the
funded US demand; import the dual-standard cabinet option and station-DC-backbone concept.

**C-16 — 4/6/7/6/6 — REJECT (duplicate of E-14).** Same relay-and-qualification wedge; E-14's
open-benchmark strategy is sharper. Import: the CN factory-acceptance-test license market and
State Grid test-institute channel as E-14's side market.

**C-17 — 4/7/6/7/6 — REJECT (duplicate of D-01).** The seed honestly concedes the CN leg may be
export-blocked and invites its own re-batching. D-01 is the same product with a cleaner US
anchor.

**C-18 — 3/6/6/6/3 — REJECT.** Self-declared "highest commoditization risk in batch C" is
accurate: Vicor/Delta/Infineon/Navitas reference ecosystems plus Innoscience-based CN designs
make 800V-to-PoL bricks a parity race by 2030, and the seed's own kill logic ("if 2030 sees
stable multi-vendor supply at parity, there is no wedge") is the expected outcome.

**C-19 — 5/6/6/6/5 — FIX.** Cartridge-ized rotor support for sCO2/ORC machines is a sound
component play with named unresolved physics (L04-113), but it is 100% levered to someone
else's commercialization pace. Fixes: (1) 2028 gate on machine-build signals (STEP Phase 2
hardware orders, CNNC follow-on units); (2) pair with C-08 as one high-temperature-components
company — shared buyers, shared test infrastructure — rather than two subscale ventures; (3)
seal-major (John Crane/EagleBurgmann-class) response mapping in P4.

**C-20 — 4/6/7/6/5 — FIX (merge into C-09).** Envelope-tracked GaN SSPA blocks are a legitimate
product line but the standalone company faces lumpy government-lab procurement and CN domestic
preference; the seed self-labels discardable. Fix: fold into C-09 as the RF-drive product
family; keep the 20 kW / >=68% chain-efficiency demo as that line's decisive experiment.

**C-21 — 5/6/5/7/5 — FIX.** "Delete the AC middle" has genuine independent policy legs (US 24/7
procurement economics; CN green-power direct-connection framework, correctly cited to the
fetched primary). But the competitor set (Sungrow, Huawei, GE Vernova, solar-inverter majors)
is the harshest in the pool and protection immaturity cuts both ways. Fixes: (1) named US
campus/IPP DC-coupling pilot commitment by 2028 or re-batch; (2) position protection
coordination (with A-02/E-14 lineage) as the wedge, not efficiency; (3) CN participation as
license-out only; (4) cap v1 capex below the stated $30M ceiling.

**C-22 — 6/7/7/7/7 — PROMOTE.** The most intelligent response to the L11 contradiction in the
pool: monetize uncertainty itself with degradation-truth benches and financier-facing datasets;
demand survives both hydrogen boom and consolidation branches. Chroma-sideways entry is the
real threat and is named. Low capex, clean pre-company path, honest flag on the missing
industry-standard citation (P4 to re-source).

### Batch D — wildcards (20)

**D-01 — 5/8/7/8/7 — PROMOTE (canonical for cluster 9).** The best-specified quench seed:
co-wound Rayleigh fiber + RF/acoustic fusion + CLIQ-class extraction, a falsifiable 2027
experiment (>=100 ms warning, <1% false trigger), and honest treatment of the no-insulation
substitution risk. Demand timing (post-SPARC pilot-plant magnet builds, DOE milestone renewal)
is as dated as fusion allows. Absorb A-04's acceptance-protocol framing, E-07's precursor-
dataset moat and KEPCO/LS cable-monitoring side market; CN participation only if counsel clears.

**D-02 — 6/8/8/7/8 — PROMOTE (canonical for cluster 10).** Best instrument seed in the pool:
contactless reel-to-reel Ic mapping at line speed with a <$150k decisive experiment, buyers on
both sides of a documented QC trust gap, and demand that scales with conductor volume rather
than fusion success (low-beta). The THEVA in-house-scanner risk is honestly carried as
judgment. Absorb C-11's cable/CICC acceptance stations and insurer data packages; B-10's
conductor-passport framing and CN buyer set.

**D-03 — 4/6/5/6/5 — REJECT (duplicate of C-12).** Import: the catalog-price/6-month-lead-time
product definition — it is the crispest statement of the value proposition in the cluster.

**D-04 — 7/8/4/8/3 — REJECT.** Beautiful physics (the conductor is its own breaker), wrong
buyer: hyperscalers are the most uptime-conservative purchasers on earth and will not adopt
cryogenic distribution inside the 2030–2034 window; the atlas's own negative finding (no repeat
third-party HTS cable orders) applies with more force to a startup busway than to utility
cable. Elegant science without a credible buyer inside the window — the archetypal rejection
this review exists to make.

**D-05 — 5/7/7/7/7 — REJECT (duplicate of C-09).** The open-interface "OCP of pulsed power"
strategy is the single most valuable idea in the modulator cluster and must survive the merge
into C-09; the standalone seed does not.

**D-06 — 6/6/5/7/3 — REJECT.** The seed's own risk line settles it: if the next-gen Z decision
slips and private IFE stalls, "the market is grants, not products." Government-concentrated
buyer base, undated anchor procurement, rep-rated switch physics still open — science-only well
past 2030 as a business.

**D-07 — 7/7/5/6/4 — FIX.** Genuinely non-obvious (nobody else touched energy recovery on the
installed tube fleet) and the 78.5%-vs-90% gap is documented. But the buyer set is small,
retrofit-at-rebuild only, and OEMs (CPI/Thales/Canon) internalize MSDC the moment it works —
this smells like a licensing/NRE business, not a company. Fixes: (1) fleet-size and $/point-of-
efficiency arithmetic from named facilities; (2) an OEM/rebuilder channel agreement in
principle by 2028; (3) explicit decision at 2029: license the IP or fold into C-09's platform.

**D-08 — 5/6/5/7/5 — FIX (canonical for cluster 8).** The duopoly-backlog opening is real and
dated; the SSPA-driven cost thesis is plausible but unproven; the EtO regulatory driver is not
yet in the accepted ledger. Fixes: (1) re-source the EtO forcing function from an eligible
primary (EPA NESHAP/FDA pathway documents) in P4; (2) validate the solid-state-RF vs klystron
cost crossover with quotes, not curves, by 2028; (3) confirm incumbent backlog persistence in
2027 — if IBA/L3 clear and cut prices, kill; (4) absorb A-09's in-house-cell variant as a
deployment option, not a separate seed.

**D-09 — 6/8/8/6/6 — PROMOTE (canonical for cluster 7).** A documented, unresolved metrology
failure (two independent groups), a cheap decisive experiment, regulator-shaped demand on two
legs (FLASH qualification, ISO 11137-1:2025), and an honest small-TAM admission. Exactly what a
niche-instrument seed should be; pairs commercially with C-09/D-08.

**D-10 — 5/8/7/8/7 — PROMOTE (canonical for cluster 15).** The merchant phase-control engine is
the right abstraction level for the CBC wave: pure electronics/controls leverage on a
documented channel-scaling wall, with dual-use industrial sales hedging prime NIH. ITAR
segregation is manageable. The 16→128→1,000-channel pre-company ladder is realistic lab work.

**D-11 — 7/7/5/8/3 — FIX (canonical for cluster 24).** The pool's best-disciplined moonshot:
model-only 5% CE, TRL 2, one dominant buyer — and a kill gate (experimental CE by 2028, dead by
2032 otherwise) that makes it an honest option purchase rather than a company plan. Fixes: (1)
adopt E-13's stricter formulation — kill if tin-droplet CE >4% at relevant rep-rate is not
demonstrated by end-2033 — and its Gigaphoton second-buyer hedge; (2) state plainly that the
most likely successful exit is acqui-license by the incumbent source suppliers; (3) no capital
beyond the consortium experiment until the gate passes.

**D-12 — 7/8/5/7/4 — FIX.** EHD in-plate flow control is the most elegant wildcard in the pool
and the seed handles the enthusiasm-zone rule honestly (both 2025 reviews' no-deployment
finding cited against itself). Still an enthusiasm zone: no named buyer wants EHD, they want
kilowatts removed. Fixes: (1) demand bridge — one named cold-plate OEM or COOLERCHIPS-lineage
partner co-development by 2028; (2) the 2027 experiment must beat the best mechanical-pump
plate on CHF/hotspot-following, not just demonstrate modulation; (3) fluid intersection check
(dielectric + non-PFAS + low-GWP) is a hard gate.

**D-13 — 7/7/7/6/6 — PROMOTE.** Non-obvious (unique in pool), physically clean (latent-heat
magazine vs peak-rated chiller), and aimed at a documented GAO-named SWaP gap with a dated
program ladder (JLWS scaling). Risks (150 kW plateau, PCM cycle life, prime in-house) are named
and testable by the 2027 brassboard. Best defense wildcard in the batch.

**D-14 — 5/6/6/7/6 — REJECT (duplicate of A-14).** The 400 C SiC-JFET tier and FORGE
field-trial step import directly into A-14's roadmap; a second harsh-environment platform
company is not needed.

**D-15 — 4/6/6/7/6 — REJECT (duplicate of A-13).** Import: SEE-map-first sequencing and the
honest "qualified-once, reused-everywhere" qualification-file framing.

**D-16 — 5/6/5/7/3 — FIX.** The merchant multi-team PCU position is clever, but this is a
subcontract option on a government program that has already re-baselined once; if flight
procurement slips past 2034 there is no market. Fixes: (1) treat as a held option — studies and
SBIR only, no hardware capex until FSP downselect/flight dates are contracted (2028 checkpoint);
(2) validate the 25–50 kWe parallel-unit architecture against the actual RFI spec with at least
two of the three concept teams expressing subcontract interest; (3) explicit fold-down path to
terrestrial micro-Brayton (C-19/C-08 adjacency) if FSP dies.

**D-17 — 5/7/6/7/6 — REJECT (duplicate of E-04).** Import: the SFQ/cryo-CMOS substitution-risk
paragraph — the most honest competitive statement in the cluster — and the 4x/2yr
roadmap-validation framing.

**D-18 — 5/6/6/6/5 — FIX (canonical for cluster 23).** The Army's published $300k/unit target
is a real, dated spec — but a single $250k Phase I SBIR topic plus an inaccessible Chinese
comp (Guangqi) is a thin demand base, and Echodyne-class incumbents already occupy adjacent
bands. Fixes: (1) by 2028, a second named program office, prime teaming agreement, or Phase II
award — one SBIR topic cannot carry a company thesis; (2) P4 incumbent mapping (Echodyne,
Metawave-class, prime AESA cost curves); (3) keep E-12's KR allied-variant channel as upside
only.

**D-19 — 5/6/6/6/6 — FIX (canonical for cluster 20).** The Piller SHIELDX selection proves the
architecture is procurable and the microcycle-aging argument against BESS is real. But this is
a fast-follower against an incumbent with the reference install, and BESS cost decline plus
NVIDIA-side software smoothing could shrink the niche to harmonics scale. Fixes: (1) 2026-27
instrumented load-spectrum study with a datacenter partner to size the actual buffering
requirement (the claimed niche must be measured, not asserted); (2) quantified cycle-life
economics vs Piller synchronous machines and vs BESS at measured microcycle rates; (3) CN
market only as license note (B-18 rejected).

**D-20 — 8/7/5/7/4 — FIX.** Highest-novelty seed in the pool (nobody else touched >1,400 C
hydraulics) with a real moat-by-suffering (lifetime data at temperatures where everything
dissolves). But demand is hostage to the liquid-metal architecture winning against solid-media
storage — an architecture bet the seed itself flags. Fixes: (1) 2028 gate: at least one
liquid-metal thermal-battery developer with a commercial order book (Fourth Power-class), else
kill; (2) broaden the buyer hypothesis to solar-thermochemical/metallurgy pilots so the bet is
not single-architecture; (3) keep first capital at the molten-tin-loop scale ($300k) — no
scale-up before the gate.

### Batch E — JP/TW/KR side (14)

**E-01 — 3/7/7/6/7 — REJECT (duplicate of C-01).** Import: the arc-signature ROC dataset as a
moat artifact, and the concrete TW (Delta/COMPUTEX ecosystem) and JP (ROHM device
co-qualification) side-market wedges — the best-articulated secondary-market logic in the
cluster.

**E-02 — 7/8/7/6/6 — FIX.** The vapor-quality-servo "ECU of two-phase" is a genuinely original
control-layer abstraction with the right side-market plan (NTT verification hub, ITRI chain,
GS Caltex fluids). The honest doubt is whether a control module without the loop is a company
or a feature. Fixes: (1) two OEM development agreements by 2028 demonstrating buy-vs-build
appetite; (2) if OEMs balk, merge into the B-01/C-04 loop stack as its control layer; (3)
two-phase shipment-share checkpoint (kill trigger already defined) enforced.

**E-03 — 4/7/6/7/6 — REJECT (duplicate of A-10).** Import: Samsung co-authorship as leading-edge
pull evidence and the KR diagnostics validation channel.

**E-04 — 5/7/6/7/6 — PROMOTE (canonical for cluster 13).** The most complete cryo-I/O variant:
flex + 4K mux + LNA against the fridge heat budget, with a credible TW manufacturing wedge
(SEEQC–ITRI) and JP/KR reference markets. Substitution risks (SFQ, cryo-CMOS, optical links)
imported from D-17 must stay on the record. Government-dependent capex cycles cap timing at 6.

**E-05 — 3/6/7/6/7 — REJECT (duplicate of C-09).** Import: hot-swap-<30min serviceability spec
and the KR (Vitzro Nextec/PAL) manufacturing-validation channel.

**E-06 — 3/5/6/5/3 — REJECT.** Same hidden-commodity finding as A-20, self-diagnosed
("highest commoditization risk in this batch"). Incumbents already ship recuperation; the
remaining wedge is a feature.

**E-07 — 4/7/6/7/6 — REJECT (duplicate straddling D-01 + D-02).** Split-import: the published
precursor-detection dataset moat and KEPCO/LS cable-monitoring side market go to D-01; the
conductor/joint QA benches and tape-supplier partnerships (Furukawa/Fujikura) go to D-02.

**E-08 — 3/6/6/6/5 — REJECT (duplicate of C-08).** Import: KR consortium channel
(KAERI/Jinsol/Hanwha), MHI-Turboden adjacency note, and the explicit pre-commitment TAM
triangulation task for the China retrofit figure.

**E-09 — 4/6/7/7/7 — REJECT (duplicate of A-14).** Import: packaging-first qualification
strategy (die-attach/ceramic stack as the true bottleneck), the 1,000 h powered-soak evidence
artifact, and the JP Fukushima-decommissioning side market.

**E-10 — 4/6/6/7/6 — REJECT (duplicate of A-13).** Import: ECSS-E-ST-20-20C / AIAA S-122
qualification framing, JAXA–Furukawa J-SPARC pattern, and KARI as an emergent KR buyer.

**E-11 — 6/6/5/6/4 — FIX.** Package-level CPO thermal control (+/-0.5 C at laser sites) is a
real spec nobody sells, and Taiwan-assembly reality grounds the channel. But the window is
narrow on both sides: CPO volume may slip (LPO substitution) or OSAT roadmaps may absorb the
lid before a 2030 entrant arrives. Fixes: (1) 2028 gate on CPO volume-ramp evidence plus one
switch-vendor/OSAT co-development agreement; (2) explicit LPO-substitution monitor; (3) frame
Coherent-as-buyer-and-competitor risk with a defensive IP plan.

**E-12 — 4/5/6/5/5 — REJECT (duplicate of D-18).** Import: the KRISS-to-KER transfer precedent
as the allied-variant model.

**E-13 — 6/6/5/7/3 — REJECT (duplicate of D-11).** Import: the CE->4%-by-2033 kill gate and the
Gigaphoton second-customer hedge — both sharpen D-11.

**E-14 — 6/7/7/8/6 — PROMOTE (canonical for cluster 3).** "SEL of DC grids" is the right
abstraction: protection intelligence and vendor-neutral qualification rather than the breaker
itself, with an open-benchmark strategy that converts research chaos (algorithms re-derived
paper-by-paper) into an ownable acceptance standard. Dated US anchors (Southern Spirit 2029
construction, PRC-029 compliance) plus a real KR localization side market. Absorb C-16's CN
factory-acceptance license angle; coordinate scope with A-02 (hardware) and A-03 (field
emulator). Honest risk: converter vendors refusing third-party protection in their stations.

## 4. Summary table

| Seed | N | E | C | V | T | Verdict | Duplicate of |
|---|---|---|---|---|---|---|---|
| A-01 | 3 | 7 | 7 | 6 | 7 | REJECT | C-01 |
| A-02 | 5 | 6 | 6 | 8 | 6 | PROMOTE | — |
| A-03 | 6 | 6 | 7 | 6 | 5 | FIX | — |
| A-04 | 4 | 7 | 6 | 7 | 7 | REJECT | D-01 |
| A-05 | 6 | 7 | 8 | 5 | 7 | PROMOTE | — |
| A-06 | 4 | 6 | 6 | 7 | 6 | REJECT | E-04 |
| A-07 | 3 | 6 | 7 | 6 | 7 | REJECT | C-09 |
| A-08 | 5 | 7 | 8 | 5 | 6 | REJECT | D-09 |
| A-09 | 4 | 5 | 5 | 6 | 5 | REJECT | D-08 |
| A-10 | 4 | 8 | 7 | 8 | 7 | PROMOTE | — |
| A-11 | 5 | 6 | 7 | 5 | 5 | FIX | — |
| A-12 | 3 | 6 | 6 | 7 | 6 | REJECT | C-08 |
| A-13 | 4 | 6 | 6 | 7 | 6 | PROMOTE | — |
| A-14 | 5 | 6 | 7 | 8 | 8 | PROMOTE | — |
| A-15 | 4 | 7 | 8 | 6 | 7 | REJECT | C-05 |
| A-16 | 4 | 5 | 5 | 6 | 5 | FIX | — |
| A-17 | 4 | 7 | 6 | 7 | 6 | REJECT | D-10 |
| A-18 | 3 | 6 | 7 | 5 | 6 | REJECT | C-13 |
| A-19 | 4 | 6 | 7 | 6 | 6 | REJECT | C-07 |
| A-20 | 3 | 5 | 6 | 5 | 3 | REJECT | (pair w/ E-06) |
| A-21 | 4 | 5 | 6 | 6 | 6 | PROMOTE | — |
| A-22 | 5 | 6 | 6 | 7 | 7 | PROMOTE | — |
| B-01 | 7 | 8 | 7 | 7 | 7 | PROMOTE | — |
| B-02 | 4 | 6 | 8 | 6 | 7 | REJECT | C-05 |
| B-03 | 3 | 6 | 6 | 6 | 6 | REJECT | C-01 |
| B-04 | 3 | 6 | 6 | 6 | 6 | REJECT | C-01/A-02 |
| B-05 | 4 | 7 | 6 | 7 | 4 | REJECT | A-10 |
| B-06 | 6 | 7 | 7 | 6 | 6 | FIX | — |
| B-07 | 3 | 6 | 6 | 6 | 6 | REJECT | C-08 |
| B-08 | 4 | 6 | 5 | 6 | 5 | REJECT | C-19 |
| B-09 | 3 | 6 | 7 | 6 | 6 | REJECT | C-09 |
| B-10 | 4 | 6 | 7 | 6 | 7 | REJECT | D-02 |
| B-11 | 4 | 5 | 5 | 6 | 5 | REJECT | C-12 |
| B-12 | 4 | 6 | 6 | 5 | 4 | REJECT | A-05 |
| B-13 | 4 | 6 | 6 | 6 | 5 | REJECT | C-07 |
| B-14 | 7 | 5 | 6 | 6 | 5 | FIX | — |
| B-15 | 3 | 5 | 6 | 5 | 4 | REJECT | — |
| B-16 | 4 | 5 | 6 | 6 | 4 | REJECT | — |
| B-17 | 4 | 5 | 6 | 6 | 4 | REJECT | A-14 |
| B-18 | 3 | 5 | 6 | 5 | 5 | REJECT | D-19 |
| B-19 | 3 | 6 | 7 | 5 | 6 | REJECT | C-13 |
| B-20 | 2 | 4 | 6 | 4 | 3 | REJECT | — |
| B-21 | 5 | 6 | 7 | 5 | 6 | FIX | — |
| B-22 | 6 | 7 | 7 | 6 | 6 | FIX | — |
| C-01 | 4 | 7 | 7 | 7 | 7 | PROMOTE | — |
| C-02 | 6 | 7 | 7 | 6 | 5 | FIX | — |
| C-03 | 5 | 6 | 5 | 8 | 4 | FIX | — |
| C-04 | 4 | 6 | 6 | 7 | 6 | FIX | — |
| C-05 | 5 | 7 | 8 | 7 | 8 | PROMOTE | — |
| C-06 | 4 | 7 | 6 | 8 | 6 | REJECT | A-10 |
| C-07 | 5 | 7 | 7 | 7 | 6 | PROMOTE | — |
| C-08 | 4 | 6 | 6 | 7 | 6 | PROMOTE | — |
| C-09 | 4 | 6 | 7 | 7 | 7 | PROMOTE | — |
| C-10 | 4 | 7 | 7 | 5 | 5 | REJECT | D-09 |
| C-11 | 4 | 6 | 7 | 7 | 7 | REJECT | D-02 |
| C-12 | 5 | 6 | 5 | 7 | 5 | FIX | — |
| C-13 | 4 | 6 | 6 | 6 | 6 | FIX | — |
| C-14 | 4 | 5 | 6 | 6 | 5 | REJECT | — |
| C-15 | 4 | 5 | 6 | 6 | 5 | REJECT | A-21 |
| C-16 | 4 | 6 | 7 | 6 | 6 | REJECT | E-14 |
| C-17 | 4 | 7 | 6 | 7 | 6 | REJECT | D-01 |
| C-18 | 3 | 6 | 6 | 6 | 3 | REJECT | — |
| C-19 | 5 | 6 | 6 | 6 | 5 | FIX | — |
| C-20 | 4 | 6 | 7 | 6 | 5 | FIX | merge→C-09 |
| C-21 | 5 | 6 | 5 | 7 | 5 | FIX | — |
| C-22 | 6 | 7 | 7 | 7 | 7 | PROMOTE | — |
| D-01 | 5 | 8 | 7 | 8 | 7 | PROMOTE | — |
| D-02 | 6 | 8 | 8 | 7 | 8 | PROMOTE | — |
| D-03 | 4 | 6 | 5 | 6 | 5 | REJECT | C-12 |
| D-04 | 7 | 8 | 4 | 8 | 3 | REJECT | — |
| D-05 | 5 | 7 | 7 | 7 | 7 | REJECT | C-09 |
| D-06 | 6 | 6 | 5 | 7 | 3 | REJECT | — |
| D-07 | 7 | 7 | 5 | 6 | 4 | FIX | — |
| D-08 | 5 | 6 | 5 | 7 | 5 | FIX | — |
| D-09 | 6 | 8 | 8 | 6 | 6 | PROMOTE | — |
| D-10 | 5 | 8 | 7 | 8 | 7 | PROMOTE | — |
| D-11 | 7 | 7 | 5 | 8 | 3 | FIX | — |
| D-12 | 7 | 8 | 5 | 7 | 4 | FIX | — |
| D-13 | 7 | 7 | 7 | 6 | 6 | PROMOTE | — |
| D-14 | 5 | 6 | 6 | 7 | 6 | REJECT | A-14 |
| D-15 | 4 | 6 | 6 | 7 | 6 | REJECT | A-13 |
| D-16 | 5 | 6 | 5 | 7 | 3 | FIX | — |
| D-17 | 5 | 7 | 6 | 7 | 6 | REJECT | E-04 |
| D-18 | 5 | 6 | 6 | 6 | 5 | FIX | — |
| D-19 | 5 | 6 | 6 | 6 | 6 | FIX | — |
| D-20 | 8 | 7 | 5 | 7 | 4 | FIX | — |
| E-01 | 3 | 7 | 7 | 6 | 7 | REJECT | C-01 |
| E-02 | 7 | 8 | 7 | 6 | 6 | FIX | — |
| E-03 | 4 | 7 | 6 | 7 | 6 | REJECT | A-10 |
| E-04 | 5 | 7 | 6 | 7 | 6 | PROMOTE | — |
| E-05 | 3 | 6 | 7 | 6 | 7 | REJECT | C-09 |
| E-06 | 3 | 5 | 6 | 5 | 3 | REJECT | (pair w/ A-20) |
| E-07 | 4 | 7 | 6 | 7 | 6 | REJECT | D-01+D-02 |
| E-08 | 3 | 6 | 6 | 6 | 5 | REJECT | C-08 |
| E-09 | 4 | 6 | 7 | 7 | 7 | REJECT | A-14 |
| E-10 | 4 | 6 | 6 | 7 | 6 | REJECT | A-13 |
| E-11 | 6 | 6 | 5 | 6 | 4 | FIX | — |
| E-12 | 4 | 5 | 6 | 5 | 5 | REJECT | D-18 |
| E-13 | 6 | 6 | 5 | 7 | 3 | REJECT | D-11 |
| E-14 | 6 | 7 | 7 | 8 | 6 | PROMOTE | — |

## 5. Longlist candidates and structural findings

### 5.1 Candidates for the longlist freeze

Honest distinct-concept count after deduplication is **46**, not 55. Padding to 55 with
duplicates would be dishonest; the orchestrator should freeze from the 46 below and use the
listed alternates only if a canonical fails P4.

**PROMOTE (21):**
A-02, A-05, A-10, A-13, A-14, A-21, A-22, B-01, C-01, C-05, C-07, C-08, C-09, C-22,
D-01, D-02, D-09, D-10, D-13, E-04, E-14.

**FIX — longlist-eligible after stated repairs (25):**
A-03, A-11, A-16, B-06, B-14, B-21 (merge into A-10), B-22, C-02, C-03, C-04 (merge with B-01),
C-12, C-13, C-19 (pair with C-08), C-20 (merge into C-09), C-21, D-07, D-08, D-11, D-12, D-16,
D-18, D-19, D-20, E-02, E-11.

**Named alternates (rejected duplicates whose unique content must be imported and which can
stand in if their canonical dies in P4):** E-01/A-01 (for C-01), C-06 (for A-10), D-05 (for
C-09), C-11 (for D-02), A-04/E-07 (for D-01), A-15/B-02 (for C-05), E-09/D-14 (for A-14),
E-10/D-15 (for A-13), C-16 (for E-14).

**Strongest ten overall (diversity-weighted):** B-01, D-02, A-10, C-05, E-14, D-01, C-22,
A-14, D-10, C-01. These span thermal, superconducting, semiconductor, grid-protection,
electrochemical-test, harsh-environment, photonics, and datacenter-power clusters with at
least six distinct primary lanes.

### 5.2 Structural gaps and warnings for the orchestrator

1. **Generation yield.** 100 records → ~46 distinct concepts. Cross-batch duplication was
   systematic: six concepts appeared 3–5 times each (rack protection, TVW bias, PCHE,
   modulators, quench detection, harsh-env platform, PPU, cryo I/O). Any P4 novelty claims for
   these clusters must acknowledge that independent regeneration converged on them — they are
   strong ideas but provably obvious to atlas readers; differentiation must come from execution
   artifacts (datasets, standards positions, qualification dossiers), not the idea.
2. **China-primary coverage collapses under dedup.** Only B-01 survives as a China-first
   PROMOTE; B-06, B-14, B-22 survive as FIX. Nearly all other B seeds were access-constrained
   mirrors of A/C concepts. The realistic China strategy across the pool is licensed CN legs of
   dual-market canonicals (C-01, C-05, C-07, C-08, C-09, A-10, D-02). Recommendation: satisfy
   US/China quotas by preserving explicit CN chapters inside merged canonicals rather than
   resurrecting rejected B seeds.
3. **Portfolio skew to test/instrumentation.** C-05, C-22, D-02, D-09, A-03, E-14(part),
   plus metrology elements elsewhere: excellent wedges, but several are small-TAM; the longlist
   should not over-index on instruments at the expense of subsystem/platform plays.
4. **AI-datacenter concentration.** Roughly a quarter of distinct concepts ride the same
   macro-trigger (the atlas's dominant demand engine). That is evidence-following, not error,
   but the final portfolio should cap datacenter-correlated picks to survive a capex-cycle
   downturn.
5. **Underserved lanes after adjudication:** L10 (one canonical, A-21), L01 (one canonical,
   A-22), L16 wildcards (only D-13, D-18, D-19 survive in any form). L07 is represented only via
   A-05 and C-12. If the orchestrator wants lane breadth, these are the places a targeted
   regeneration wave would add value — not more datacenter power seeds.
6. **Enthusiasm-zone discipline held.** D-12 (EHD) and D-18 (metamaterials) are correctly
   wildcard-framed with bridges demanded; B-20, B-15, C-14, D-04, D-06 were the seeds that
   leaned on enthusiasm zones or mismatched buyers and are rejected.
7. **Quarantine compliance.** No seed cites quarantined India-origin sources; no repair needed.
8. **Timing-contract outliers.** Windows likely closing before 2030: C-18, A-20/E-06 (commodity
   race), parts of B-15. Windows likely opening after 2034: D-04, D-06, D-16 (program-gated),
   D-11 (physics-gated). All are rejected or option-gated accordingly.
