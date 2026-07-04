# DD_C15 — Turnkey Cryocooler-Integrated Compact HTS Magnet Modules for OEM Instrument Builders

**Candidate:** C15 · **Analyst date:** 2026-07-03 · **Sources:** DD_C15_sources.json (23 unique; 6 Tier 1, 6 Tier 2; 8 Chinese-language)
**Red-team input:** `30_PHASE3_SCORING/REDTEAM_C15.md` (kill-probability estimate 70%) — its three core objections are addressed explicitly in §1, §2, §4 and §5.

---

## 1. Problem & who has it

The original C15 framing — "nobody sells HTS magnets as catalog components; sell them to benchtop-NMR OEMs" — does not survive contact with the evidence. The correct problem statement, after research, is narrower:

**Instrument and test-stand builders who need >2.35 T, switchable, or large-bore fields cannot buy compact cryogen-free magnets quickly, and in the US they cannot buy them domestically at all.**

Named archetypes with verified demand signals:

- **Fusion companies and magnet labs needing background-field and conductor-test magnets.** Fusion supply-chain spending hit **$434M in 2024, up 73% from ~$250M in 2023**, with a further ~25% growth to ~$543M projected for 2025; 63% of fusion companies worry about precision-manufacturing supplier availability for *future* needs [DD-C15-21]. Every REBCO coil program needs Ic-in-field QC and insert-test background fields.
- **Gyrotron OEMs.** Gyrotrons need 3–7 T superconducting beam magnets; Cryomagnetics has supplied CPI (the leading US gyrotron maker) with cryogen-free five-coil systems since 2014 [DD-C15-23]. Fusion ECRH pilots multiply this demand.
- **High-frequency EPR / relaxometry / benchside-NMR OEMs.** W-band (94 GHz) EPR requires ~3.5–6 T swept superconducting fields — CIQTEK builds its own 6 T dry split-pair for the EPR-W900 [DD-C15-20]. Fast-field-cycling NMRD requires a *switchable* 3 T magnet — physically impossible with a permanent magnet — which is exactly what Stelar bought from HTS-110 [DD-C15-14].
- **US science infrastructure.** The 2024 National Academies report finds US high-magnetic-field capability falling behind Europe/Japan/China and recommends NSF/DOE **double** support for HTS wire and the domestic industrial base within three years [DD-C15-08].

**Red-team resolution (2) — who actually needs HTS vs Halbach:** conceded and adopted. Benchtop NMR at ≤100 MHz (≤2.35 T) standardized on permanent Halbach arrays precisely to avoid cryogenics; that market is small and slow ($143M in 2025, 3.8% CAGR, top-3 hold ~74%) [DD-C15-22] and Nanalysis's entire product line ($19.4M product revenue FY2024) runs on permanent magnets [DD-C15-07]. HTS is only justified where the field is **>2.35 T** (300–400 MHz benchside NMR, W-band EPR), **switchable/fast-ramping** (FFC-NMRD, beamlines), **large-bore/high-field** (fusion test stands, neutron scattering), or **mass/cryogen-constrained** (gyrotrons in the field). The beachhead must be rebuilt on those segments — see §5.

## 2. Product definition & the extreme-performance edge

**Product (revised):** a standardized family of conduction-cooled REBCO magnet modules — magnet + cryostat + single GM/pulse-tube cryocooler + power/quench electronics + field-control and homogeneity-mapping software — in two lines:

- **Line A (beachhead): background-field / test magnets.** 5–12 T, 100–300 mm room-temperature bore, fast ramp (LNI-style winding), operation at 20–50 K, delivered in <6 months. Sold to fusion companies, wire makers, and labs.
- **Line B (expansion): OEM instrument magnets.** 3–7 T class for EPR/FFC/gyrotron/benchside-NMR OEMs, wall-socket power (<1.5 kW), <200 kg.

**State of the art with numbers.** HTS-110's shipping/announced products define the bar: the Stelar 3Tracer 2.0 magnet is 3 T, 56 kg, <500 W, air-cooled, single-phase, first deliveries late 2026 [DD-C15-14]; its 300 MHz (7.05 T) benchside NMR magnet is ~180 kg, <1.2 kW, ~50 K operation, pre-release with commercial release expected 2027 and a 6-month lead time [DD-C15-15]; the same ecosystem (Robinson Research Institute, Wellington) published an ultra-compact <400 mm-long 1.5 T-class NI REBCO brain-MRI magnet with controlled contact resistance (7 µΩ·m²), single PT-93 cryocooler at ~30 K, <30 s emergency ramp-down [DD-C15-05].

**Where a real engineering edge still exists (and where it does not):**

- *Not an edge:* "solving epoxy cracking." Delamination under thermal-mismatch stress is open literature — REBCO c-axis strength <10 MPa, delamination initiating ~90 K on cooldown, mitigations (low-CTE ~5×10⁻⁶ K⁻¹ impregnants, dry/paraffin winding, controlled-resistance NI) all published [DD-C15-03][DD-C15-04]. Every vendor iterates on the same fixes. Red-team point conceded.
- *Genuine hard problems a manufacturing-automation specialist can own:* (a) **NI/LNI charge dynamics** — plain NI layer-wound coils show field-delay time constants of ~500 s, reducible to ~0.1 s with intra-layer NI winding architecture [DD-C15-06]; productionizing fast-ramp *and* self-protecting windings is a winding-process problem, i.e., the founder's C12 asset. (b) **Reproducibility at ppm level** — a 9.4 T all-REBCO NMR magnet at KBSI missed its <1 ppm homogeneity design by ~123 ppm, driven by screening currents (even harmonics) and conductor-thickness inconsistency (odd harmonics); the authors conclude sub-ppm uniformity is "barely possible" with current approaches [DD-C15-02]. Persistent-mode 400 MHz with HTS joints exists only as a RIKEN-class research artifact (drift 3×10⁻⁵ ppm/h) [DD-C15-01]. **Consequence:** ppb-class spectroscopy magnets are *not* a credible 2029 startup product; test/background magnets with 10–100 ppm-class requirements are.

**Red-team resolution (1) — what tier remains genuinely unserved:** not the category (HTS-110 occupies it, with a 400 MHz/9.4 T family announced "over the next two years" [DD-C15-14][DD-C15-13]), but **US domestic manufacture, delivery speed, and fusion-adjacent capacity**. HTS-110 is a small NZ boutique currently absorbing large beamline projects (12 T split-pair delivered to ILL; 14 T ESS contract) [DD-C15-13]; Tokamak Energy's TE Magnetics (launched Sept 2024, reported $125M raise Nov 2024) targets defense/science systems, not fast-turn catalog modules [DD-C15-16]. Nobody offers a **US-built, <6-month-lead-time, fast-ramp background-field magnet line** for the fusion test economy. That is the defensible residual — smaller and less product-like than the original thesis.

## 3. Technical feasibility & TRL path to a sellable unit (2029–2031)

**Buy vs build.** Everything critical is purchasable except the winding and integration know-how: REBCO tape (street prices for PLD tape now $15–30/m in volume, though 2024 saw a 300 km supply deficit at 12 mm width — 3,400 km demand vs 3,100 km production [DD-C15-19]); GM/pulse-tube cryocoolers (Sumitomo, Cryomech — the same units incumbents use [DD-C15-23][DD-C15-05]); current leads (commercial). Must be built in-house: coil winding (automated NI/LNI winder — direct C12 reuse), cryostat/thermal design, quench-management electronics, field-mapping software. **Cleanroom dependence: none.**

**BOM sketch, Line A 7 T / 150 mm bore unit:** REBCO tape ~3–6 km ≈ $60–180K at 2029 prices; cryocooler + compressor $25–45K; cryostat/vacuum $20–40K; power supply + electronics $15–25K; leads/instrumentation $10–20K → **BOM $130–310K against a $400–900K ASP** (BAQIS paid RMB 1.65M ≈ $230K for a small *domestic-only* dry variable-temperature research magnet system in April 2025 — the low end of the price band [DD-C15-09]; large background magnets clear $1M).

**TRL path:** subscale NI/LNI coil pack with published thermal-cycling data (2027–28, in-PhD) → first 5 T/100 mm prototype within 12 months of founding (2030) → two paid pilot units + Ic-test-stand product (2030–31) → Line B OEM design-ins (2031+, 2–4 yr qualification cycles). Realistic first *sellable* unit: **late 2030**, not 24 months from a 2029 start for an OEM-qualified platform as the one-pager claimed.

## 4. Competitive landscape — global and China

**Global (all verified this mission):**

| Player | Position | Evidence |
|---|---|---|
| **HTS-110 (NZ)** | The incumbent for exactly this product: catalog cryogen-free HTS magnets (NMR 300 MHz pre-release 2027, 0–3 T NMRD, scattering, Helmholtz, fast-ramp dipoles), OEM design-in shipping via Stelar (3Tracer 2.0, June 2026), 12 T ILL delivered / 14 T ESS contracted, family roadmap to 400 MHz/9.4 T | [DD-C15-13][DD-C15-14][DD-C15-15] |
| **TE Magnetics / Tokamak Energy (UK)** | HTS magnet division launched 2024-09-03; fusion, defense (GA submarine program), science; 200+ patents | [DD-C15-16] |
| **Cryomagnetics (US)** | Cryogen-free LTS systems incl. gyrotron OEM line for CPI since 2014; US-domestic but LTS-centric, project lead times | [DD-C15-23] |
| **Robinson Research Institute (NZ)** | Feeds HTS-110 technology, e.g., ultra-compact 1.5 T NI REBCO MRI magnet | [DD-C15-05] |
| Others (red-team confirmed, not re-verified) | Magnetica/Scientific Magnetics, MR Solutions, Sumitomo, Bruker in-house | [REDTEAM_C15] |

**China (中文检索):**

- **健信超导 (Jansen, SSE STAR 688805, listed 2025-12-24):** "全球最大的超导磁体独立供应商" (largest independent superconducting-magnet supplier); by 2024 installs #5 globally in MRI superconducting magnets. Two share figures circulate — **4.2%** global superconducting-magnet share (red-team/prospectus figure) vs "磁共振磁体全球市场占有率约十分之一" (~10%, likely including permanent magnets) [DD-C15-17][DD-C15-18]; both are reported here, unaveraged. 1.5 T 无液氦 (helium-free) magnet in mass production, designated 国际首台（套）in 2021; customers include GE Healthcare, Fujifilm, 联影, 万东; IPO funds an additional **600 helium-free/high-field magnets per year** plus 3.0 T line upgrades and 7.0 T R&D; 2025 Q1–3 revenue RMB 393M (+37.3%) [DD-C15-17][DD-C15-18].
- **上海超导 (Shanghai Superconductor):** >80% of China's 2G tape market; 1,100 km produced in 2024, plans 2,500 km (2025) → ~13,000 km (2028); STAR IPO filed to raise RMB 1.2B [DD-C15-19]. Domestic tape for domestic magnet makers — a structural cost advantage inside China.
- **国仪量子 (CIQTEK):** vertically integrated — designed its own 6 T dry split-pair superconducting magnet for the W-band EPR-W900 rather than buying a module [DD-C15-20]. A representative datum: capable Chinese instrument OEMs *self-supply* rather than buy Western modules.
- **中科院电工所 (CAS IEE):** 32.35 T all-superconducting user-magnet world record (2019); deep state-funded magnet capability [DD-C15-12].
- **Procurement signals (招标):** Beijing Quantum Institute's April 2025 tender for a dry variable-temperature superconducting magnet system (RMB 1.65M) states **"本项目不允许采购进口产品"** — imported bids invalid [DD-C15-09]. Contrast 2021, when Peking University's helium-free magnet tender was won by Oxford Instruments (UK) [DD-C15-10]. The import door has visibly narrowed in four years. Shanghai's 2024 new-materials plan explicitly directs acceleration of 超导带材、电缆、磁体 application development [DD-C15-11].

**Red-team resolution — China angle inverts: confirmed.** Selling magnet modules *into* China against 健信/上海超导 cost structures and domestic-only procurement is not credible for a US-person founder. China appears in this thesis only as a competitor benchmark and (pre-Nov-2026 truce) a materials-supply consideration.

## 5. Market: beachhead sizing (bottom-up), expansion, TAM/SAM/SOM

**Red-team resolution (3) — counting the real annual buyer pool, with arithmetic:**

**Segment A — fusion-adjacent test & background-field magnets (US + allied):**
- Buyer pool: ~45 private fusion developers globally (FIA surveyed 22 in 2025 [DD-C15-21]); assume **20–25 with superconducting magnet programs**; plus **~15 national labs/universities/wire makers** (MIT PSFC, NHMFL, LBNL, FNAL, ORNL; EU/JP/KR equivalents) running HTS conductor/insert testing.
- Purchase rate: 0.3–0.5 systems per active buyer per year (test stands are capital purchases, not consumables) → **11–20 units/yr**.
- ASP: $300K (small Ic-test/variable-temperature systems; cf. RMB 1.65M BAQIS floor [DD-C15-09]) to $1.5M (large-bore background magnets); mid $500–700K.
- **Bottom-up: 11–20 × $0.5–0.7M ≈ $6–14M/yr today**, growing with fusion supply spend (+73% in 2024, +25% projected 2025 [DD-C15-21]).

**Segment B — gyrotron beam magnets:** gyrotron OEMs (CPI, Thales, Canon) plus fusion ECRH programs; each gyrotron needs a 3–7 T cryogen-free magnet [DD-C15-23]. Estimated 15–30 magnets/yr globally by 2029–30 × $200–400K → **$3–12M/yr** (uncertainty high; no public unit census).

**Segment C — analytical OEM modules (W-band EPR, FFC-NMRD, 300–400 MHz benchside NMR):** est. 30–60 instruments/yr worldwide across these niches × $60–150K magnet content → **$2–9M/yr**, with HTS-110 already designed into the flagship account (Stelar) [DD-C15-14] and Chinese OEMs self-supplying [DD-C15-20]. The magnet-as-50–100%-of-instrument-price arithmetic in the original one-pager is rejected: an OEM module must sit ≤~35% of system BOM, which restricts Line B to instruments priced ≥$200K — i.e., *not* the $30–150K benchtop-NMR class.

**Beachhead SAM (A+B+C, 2029–30): ≈ $11–35M/yr.** SOM for a solo-founded entrant reaching 15–25% of Segments A+B by 2032: **$2.5–5M revenue/yr.** This is a viable high-margin boutique, not yet a venture-scale product company.

**Top-down triangulation.** (i) FIA 2024 supply-chain spend $434M [DD-C15-21]; if magnet-related purchases (systems + coils, excl. tape) are 5–15% of that, third-party magnet demand from fusion alone is $20–65M/yr — consistent with Segment A plus large project work. (ii) China's HTS tape market was RMB 790M in 2024 (+77%), forecast RMB 10.5B by 2030 (53.9% CAGR), with fusion RMB ~300M and MCZ RMB ~60M of 2024 downstream demand [DD-C15-19] — the demand pull is real but concentrated in fusion/large systems, not instrument modules. (iii) Benchtop NMR at $143M/3.8% CAGR [DD-C15-22] confirms the *original* beachhead was the wrong one.

**TAM/expansion:** independent-supplier MRI magnet economics (健信: ~RMB 500M/yr revenue at ~40% gross margin, 4.2–10% global share [DD-C15-17][DD-C15-18]) show what the module business becomes if compact MRI/veterinary/interventional imaging adopts cryogen-free HTS at scale; the NASEM push to rebuild US magnet capability [DD-C15-08] and fusion growth give a credible $200–500M/yr accessible frontier by the mid-2030s. State uncertainty: ±50% on all forward segment numbers.

## 6. Go-to-market

**Lead: US-first. China-first is structurally closed** (domestic-only tenders [DD-C15-09], entrenched subsidized incumbents [DD-C15-17], and §7 export-control friction). US sequence: (1) 2029–30 — DOE SBIR/ARPA-E-adjacent non-dilutive funding plus 2–3 paid pilot test magnets to fusion companies and one national lab (reference customers; procurement is spec-driven and fast for <$1M line items); (2) 2030–31 — Ic-test-stand catalog product with published lead time (<6 months vs incumbents' project queues [DD-C15-15]); (3) 2031+ — OEM design-ins (gyrotron, EPR) once reliability data exists. Channel: direct + conference presence (ASC, MT, EUCAS); scientific buyers purchase from spec sheets and papers — publish the coil-reliability dataset. **China role:** none as a market initially; monitor tape suppliers (Faraday Factory Japan and US MetOx as non-PRC hedges given 2024's 300 km tape deficit [DD-C15-19]) and revisit Chinese OEM sales only if §7 posture changes.

## 7. Regulatory & geopolitical exposure (coordinated with `50_PHASE5_POLICY/POLICY_BRIEF.md`)

Per the Phase 5 brief, archetype (i) — compact HTS magnets for instrument OEMs — is legally open in both the US and China today, but sits near three controlled clusters [POLICY_BRIEF §1, §5 row i; P-10, P-11, P-15]:

- **ECCN 3A001.e.3** (superconducting solenoidal electromagnets, with MRI-type exclusions) and **3A201** nuclear overlay can capture magnet modules; **1C005** captures superconductive composite conductors. Classification is a product-requirements decision to make in 2027–28: where physics allows, design below control parameters and inside the MRI-exclusion geometry [POLICY_BRIEF §1, §7 logic].
- **3A904 cryocoolers** (Sept-2024 quantum rule): sub-4 K pulse-tube coolers drag a controlled item into the BOM. Design choice: GM/PT operation at 20–50 K — where REBCO wants to run anyway [DD-C15-05][DD-C15-15] — keeps the BOM clear.
- **OISP/COINS:** magnets and winding machines are *not* covered sectors today, but Treasury's sector-adding authority (regs due ~March 2027) makes superconducting/fusion a plausible future designation; marketing anything as "quantum sensing with military/intel applications" activates prohibited/notifiable categories now [POLICY_BRIEF §2].
- **Materials:** China's rare-earth export-licensing regime (Sm, Gd, Tb, Dy) remains in force and the broader truce is suspended only to Nov-2026 — a structural supply risk for US-based REBCO magnet production; qualify two non-PRC tape sources early [POLICY_BRIEF §4; DD-C15-19].
- **Certification:** staying out of clinical imaging avoids ISO 13485/FDA entirely for Lines A/B; fusion/lab customers need CE/UL and pressure/cryo safety files only.

Bottom line: **US-first is also the compliance-minimal path**; a China-facing leg would put the founder's winding "technology" at deemed-export risk the moment any product classifies above EAR99.

## 8. Capital & milestones (2029→2032)

- **2029 H2 (found):** $500K–1M pre-seed/SBIR. Build winder v2 + subscale coil reliability rig. Team: founder + 1 cryo-mechanical engineer (the acknowledged skill gap) + 1 technician.
- **2030:** $2.5–4M seed. Prototype 5–7 T/100–150 mm unit; 2 paid pilots ($0.8–1.5M bookings). Burn ~$1.5M/yr. **First revenue: mid/late 2030.**
- **2031:** Catalog Ic-test stand + background magnet line; 4–6 units shipped ($2.5–4M revenue); one OEM design-in started (gyrotron or EPR). Cryo test infrastructure capex $0.7–1M cumulative — the seed-capital-vs-qualification-cost ratio the red team flagged is manageable *only* because Line A units are themselves revenue.
- **2032:** Series A ($8–15M) gated on: ≥$4M trailing revenue, ≥1 fusion frame agreement, reliability dataset (≥50 thermal cycles, MTBF evidence) published. If gates miss → stay a profitable 8-person boutique or fold capability into C12.

## 9. Risks & kill criteria

**Top risks (ranked):**
1. **Incumbent closure of the gap (highest).** HTS-110 ships its 300→400 MHz family on schedule (2027–28) [DD-C15-14][DD-C15-15] and scales capacity; TE Magnetics' $125M-class war chest takes the fusion test-magnet niche [DD-C15-16]. A 2029 entrant then has no wedge beyond "US-built + lead time."
2. **Beachhead lumpiness.** 11–20 units/yr industry-wide (Segment A) means two lost deals = a lost year; fusion capex is milestone-driven and deferrable [DD-C15-21].
3. **Physics ceiling on product ambition.** ppm/ppb spectroscopy-grade fields remain out of reach of NI REBCO manufacturing tolerance [DD-C15-02]; if the analytical segment demands them, Line B never opens.
4. **Tape supply/price.** 2024's 300 km deficit and fusion pre-buys [DD-C15-19]; rare-earth controls post-Nov-2026 [POLICY_BRIEF §4].
5. **Solo-founder cryogenics gap.** Cryostat/MTBF engineering is half the product and outside the founder's demonstrated stack — needs a hire or co-founder by day one.

**Kill criteria (explicit):**
- By **end-2027** (during PhD): <5 of 15 interviewed fusion/gyrotron/OEM buyers express concrete willingness to buy a US-built module at ≥$400K with <6-month lead → kill.
- By **end-2028**: HTS-110 (or TE Magnetics) demonstrably quoting <6-month leads on catalog test magnets *and* a shipped 400 MHz benchside product at <$200K → kill Line B, re-scope or kill company thesis.
- By **mid-2031**: no second paid unit or no fusion frame agreement → wind down to C12.
- Any time: COINS/BIS designates superconducting magnet tech as a covered/controlled sector in a way that blocks allied-country sales → re-evaluate immediately [POLICY_BRIEF §2].

## 10. Verdict

**Conviction: LOW-to-MEDIUM** — Low for the candidate as originally framed (catalog HTS modules for benchtop-NMR-class OEMs: the whitespace is occupied by HTS-110 and the named beachhead deliberately chose permanent magnets); **Medium** for the salvageable reframe (US-built fast-turn background-field/test magnets riding fusion supply-chain growth), which is a real but boutique-scale business — and is best held as the **vertical-integration expansion of C12** (the winding-machine thesis) rather than a standalone lead bet. The two share one asset (production NI/LNI winding know-how) and one customer community, and C12's customers (magnet makers) conflict with C15's competitors only if both run simultaneously — sequence C12 first, C15 as its application-proof lab and optional product line.

**Cheapest validation experiments for 2026–2028 (in-PhD):**
1. **Buyer census ($0, 2026–27):** 15 structured interviews — 8 fusion magnet leads, CPI, 2 EPR/NMR OEMs, 2 national labs, 2 wire makers — on test-magnet sourcing, prices paid, lead times, and US-origin preference. Kills or confirms Segment A in one quarter.
2. **Reliability wedge experiment (~$15–30K, 2027–28):** wind subscale NI and LNI coil packs on the existing winder design, run ≥50 thermal cycles + ramp-rate characterization, publish (SUST/IEEE TAS). Directly tests whether automated winding yields a measurable reliability/ramp advantage — the entire differentiation claim [DD-C15-04][DD-C15-06].
3. **Incumbent tracking ($0, standing):** HTS-110 400 MHz family pricing/lead times, TE Magnetics product moves, 健信 high-field exports, REBCO $/kA-m quarterly. Feeds the 2028 go/no-go.

---
*All load-bearing figures fetched per SOURCE_STANDARDS; ranges reflect genuine uncertainty and conflicting figures are reported side-by-side (健信 4.2% vs ~10% share; benchtop NMR $124–183M). This section is research, not legal advice.*
