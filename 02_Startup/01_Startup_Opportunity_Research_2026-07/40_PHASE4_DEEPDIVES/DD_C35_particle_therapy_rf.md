# DD_C35 — Modular Solid-State RF Amplifier Cassettes for Compact Particle-Therapy Accelerators

**Candidate:** C35 · **Sources:** DD-C35-01…23 (logged in `DD_C35_sources.json`) · **Date:** 2026-07-03
**Red-team input:** `30_PHASE3_SCORING/REDTEAM_C35.md` (kill-probability ~85%) — each objection is addressed explicitly in §4, §5, and §10.

---

## 1. Problem & who has it

Accelerator RF power is living through a forced technology migration. The vacuum-tube supply base has collapsed to near-monopoly: the Uppsala/ESS design team states there is "only one vacuum tube manufacturer worldwide" for the relevant high-power tubes, with prices recently up ~40% and half-year lead times, while tube lifetime is 5,000–10,000 h against up to 100,000 h for solid-state power amplifiers (SSPAs) [DD-C35-01]. Argonne is replacing four 1 MW klystron systems at the Advanced Photon Source with twelve 160 kW solid-state systems "primarily due to klystron obsolescence" [DD-C35-02]. CERN is replacing SPS 200 MHz tetrodes with SSPAs [DD-C35-01].

Named archetypes who feel this pain:

- **RF group leader at a mid-size light source or national lab** (≈50+ light sources worldwide, operational or under construction [DD-C35-07]) running 30–200 kW CW tube stations at 100–500 MHz with a dying spares pipeline.
- **Chief engineer at a proton/carbon-therapy OEM** (IBA, Varian/Siemens, Hitachi, Sumitomo, Mevion, ProTom; plus Chinese entrants [DD-C35-14]) whose clinical uptime guarantees hang on RF availability; Varian's ProBeam cyclotron already runs a 72 MHz solid-state chain built from ~120 × 1.25 kW LDMOS modules.
- **Medical-isotope cyclotron operator** — the IAEA database counts ~1,300 cyclotron facilities for radionuclide production worldwide [DD-C35-05][DD-C35-08]; each carries a 10–100 kW-class RF system whose tube or first-generation amplifier ages out.

The honest restatement after red-teaming: the *problem* (tube obsolescence) is real and well-sourced, but it is **already being solved commercially** — the question examined below is whether any defensible slice remains for a 2030 solo-founder entrant.

## 2. Product definition & the extreme-performance edge

**Product as pitched:** field-swappable 1–5 kW VHF/UHF GaN or LDMOS cassettes, N+1 combinable to 20–200 kW, with the differentiating twist of **integrated digital LLRF and per-cassette health analytics** (phase/gain drift, transistor junction-temperature prognostics, predictive swap scheduling) — sold as OEM subsystems and as tube-replacement retrofits.

**Specs vs. state of the art (the uncomfortable numbers):**

| Parameter | State of the art (shipping) | C35 claim |
|---|---|---|
| Module power | 1.6 kW LDMOS (Ampleon ART2K0FE), 73% at 352 MHz [DD-C35-01] | 1–5 kW, comparable |
| System power | 350 kW at 101 MHz delivered to CERN by BTESA (2021–22); 400 kW ESS design; 160 kW × 12 at APS by R&K [DD-C35-18][DD-C35-01][DD-C35-02] | 100+ kW combinable — no advance |
| Efficiency at cyclotron VHF | 68–71% published (83.2 MHz modular 20 kW SSPA for a 10 MeV cyclotron — academic prior art, Korea) [DD-C35-04] | same physics, same transistors |
| Redundancy/hot-swap | BTESA CERN system: modular, prototype passed 1,000 h supercycle test; APS design "particular attention to reliability and redundancy" [DD-C35-18][DD-C35-02] | incremental packaging improvement |
| LLRF integration | Typically separate (labs build their own digital LLRF; HEPS pairs each 200 kW SSA with a digital LLRF system built by IHEP [DD-C35-03]) | **the only genuinely open slot** |

The red team is right that the *amplifier* has no 10x edge: at 30–110 MHz where cyclotrons live, cheap LDMOS matches GaN, and 73%-efficient 1.6 kW modules are catalog parts [DD-C35-01]. The residual technical differentiation is a **tightly integrated cassette = PA + digital LLRF + prognostics**, a systems/software claim (founder-fit: FPGA + instrumentation), not a device-physics claim. That is a real gap — labs hand-roll LLRF today — but it is an integration convenience, not an order-of-magnitude edge, and it fails the mission's "extreme performance" bar.

## 3. Technical feasibility & TRL path (2029–2031)

- **BOM sketch (5 kW, 100 MHz cassette):** 4 × 1.5 kW LDMOS pallets (~$1–2K/transistor class), Gysel/Wilkinson combiner, circulator + load, 50 V bus converter, Zynq-class FPGA LLRF (direct sampling at VHF is easy), water-cooled cold plate, CAN/EtherCAT health bus. Est. BOM $8–15K; target ASP $30–60K. All COTS; **cleanroom dependence: none.**
- **Hard parts:** (i) combining and phase-tracking at 50–200 kW system level — solved art but requires expensive test infrastructure; (ii) **the reliability dossier** — buyers of 100,000 h claims want fleet-hours a startup cannot have by 2031; (iii) 100 kW-class dummy loads, water plant, and shielded test cell: realistically $1.5–3M of test capex, at the edge of a deep-tech seed.
- **TRL path:** 1–5 kW cassette + LLRF demonstrable in 12 months post-founding; 20–50 kW combined rack in 24 months; OEM/laboratory qualification 12–36 months beyond that (tender cycles, acceptance testing). First *qualified* revenue realistically 2032, not 2030 — the red team's "dies waiting for qualification" scenario is the base case unless the beachhead is a small retrofit sale, not an OEM design-in.

## 4. Competitive landscape (resolving red-team point 1: what, if anything, remains)

**Global incumbents (all verified this mission):**

- **BTESA (Spain):** 350 kW/101 MHz SSA for CERN replacing tube amplifiers, 50 kW prototype validated 2021 incl. full-reflection and 1,000 h tests; IPAC 2026 lineup spans 4 kW–200 kW CW/pulsed, 101–1500 MHz — including **11 × 100 kW pulsed at 750 MHz explicitly for proton therapy** and 200 kW CW/175 MHz for IFMIF-DONES [DD-C35-18][DD-C35-17]. It has also manufactured 180 SSAs for the CERN PS.
- **R&K (Japan):** won the APS klystron-replacement program — twelve 160 kW/352 MHz systems, each two 85 kW cabinets + 48-way combiners; APS bought a 32 kW unit commercially off the shelf to validate combiners [DD-C35-02].
- **Cryoelectra (Germany):** named SSPA supplier to BESSY; the Varian ProBeam 72 MHz solid-state chain is Cryoelectra-built (CRE-312C-class, 150 kW) — i.e., a proton-therapy OEM already *outsources* RF, but to a 20-year incumbent [DD-C35-01].
- **IBA (Belgium):** offers its own SSPA at 176 MHz for MYRRHA [DD-C35-01] — a seller, not a buyer.
- **RFHIC (Korea):** GaN-on-SiC amplifiers 2 kW (50–500 MHz) to 30 kW (1.3 GHz) positioned squarely at accelerators/LINACs [DD-C35-19]. Plus Thales (pulsed 200 MHz for CERN SPS), Rohde & Schwarz (MAX IV, Solaris), Ampegon (PSI 500 kW) [DD-C35-01].

**What remains (red-team question 1, answered):**

1. **Tube-replacement retrofit for the installed base** — real demand (APS, CERN precedents), but procured via public tenders that incumbents win on fleet-hours; a new entrant can realistically capture only **sub-100 kW retrofits at small facilities** (university cyclotrons, older isotope machines) where tender sizes are too small for BTESA/R&K economics.
2. **LLRF-integrated cassettes** — genuinely under-served (incumbents ship RF power; LLRF stays lab-built [DD-C35-03]); this is the only defensible product concept, and it drifts C35 toward a *controls/instrumentation* business.
3. **Wider buyer pool** (research accelerators, isotope cyclotrons, industrial e-beam) — exists and is quantified in §5, but every sub-segment already has a qualified supplier; breadth adds TAM, not a moat.

**China landscape (Chinese-language research, resolving red-team point 3):**

- **成都沃特塞恩 (Chengdu Wattsine):** accelerator-dedicated solid-state sources **10 W–350 kW**, frequencies 31.02/71/85/107/162.5/324/1300 MHz, CW and pulsed, 40–59% efficiency, referencing synchrotron sources, XFEL and CIADS; closed a **¥200M B round (2024-01)** with state-linked investors [DD-C35-15][DD-C35-16]. This is a direct, funded domestic incumbent for exactly C35's product.
- **IHEP self-supply:** HEPS pairs each 166.6 MHz superconducting cavity with a **200 kW SSA + digital LLRF** specified in-house [DD-C35-03][DD-C35-21] — big-science RF in China is CAS-internal plus domestic vendors.
- **国睿科技/CETC-14:** supplies high-voltage pulsed power (klystron modulators) to SSRF rather than SSAs [DD-C35-20] — the red team slightly overstated this one, but it does not change the picture.
- **合肥中科离子 (CAS Ion Medical, CIM):** its domestic 240 MeV superconducting proton cyclotron SC240 passed acceptance at HUST and, per 2025-05 reporting, set a shortest-delivery record with a "complete industrial chain from R&D design to batch production" [DD-C35-13] — Chinese therapy OEMs are vertically integrating, not shopping for foreign cassettes.
- **Policy demand exists but is fenced:** the NHC "十四五" plan allocates **41 proton/heavy-ion systems** (of 117 Class-A devices; plan issued 2023-06-29), with 8 more added for private hospitals in 2024 [DD-C35-09][DD-C35-10][DD-C35-11]; 2024 status: 7 centers operating, 17 under construction, 8 of the 17 domestic-branded [DD-C35-12]. The quota funds 国产替代, and Shanghai-government messaging around 艾普强 frames the sector explicitly as breaking import monopopoly [DD-C35-22]. **China channel for a US-person founder: effectively closed** — confirming the red team, with the added fact that Wattsine's funding and product breadth make even a China-domiciled newco a late entrant.

## 5. Market: bottom-up beachhead, expansion, TAM/SAM/SOM (resolving red-team point 2)

**Widened beachhead definition:** all merchant accelerator RF (therapy + isotope cyclotrons + research accelerators), not just the ~5–7 therapy OEMs.

**Bottom-up arithmetic (units × ASP; ASP assumptions flagged):**

- *Particle therapy:* 128 facilities operating (2023: 110 proton + 15 carbon; ~133 by May 2025 per PTCOG-derived reporting) [DD-C35-06] → net adds ≈ 5–10 systems/yr globally plus China's 41+8 pipeline over ~5 yr ≈ 8–10/yr [DD-C35-09][DD-C35-12]; assume 15–20 newbuilds/yr worldwide. RF content: ~150 kW/system (ProBeam-class); at an assumed merchant price of $5–10/W (own estimate — no public $/W found), RF value ≈ $0.8–1.5M/system → **$12–30M/yr**, of which the *outsourced* share (Varian-style) is perhaps half → **$6–15M/yr merchant**.
- *Isotope cyclotrons:* ~1,300 installed [DD-C35-05]; assume 4–6%/yr newbuild+RF-refit rate (est.) = 50–80 units/yr × 20–50 kW × ~$150–300K RF each → **$10–20M/yr**.
- *Research accelerators (light sources, spallation, ADS, colliders):* >50 light sources [DD-C35-07]; lumpy tenders — APS bought 12 × 160 kW systems in one program [DD-C35-02]; HEPS ~5+ × 200 kW [DD-C35-03]; ESS 400 kW stations [DD-C35-01]. Estimate 3–6 major programs/yr globally at $5–15M each → **$25–60M/yr** (the incumbents' core).
- **Total merchant accelerator SSA market ≈ $40–95M/yr globally.** This brackets and confirms the red team's "<$50M/yr for therapy alone is generous" — the *therapy-only* slice is $6–15M/yr merchant.

**Top-down triangulation:** whole proton-therapy market estimates conflict badly — $444M (2021)→$1.58B (2031) [DD-C35-14] vs. "global proton equipment ~€270M (2023)" [DD-C35-11] vs. ~$1.7–2.2B (2025) from US market-research houses (snippet-level). Taking systems revenue of $0.5–1.5B/yr and RF at 3–5% of system value (150 kW × $5–10/W on a $30–50M system; Chinese tenders ran ¥220–380M/unit, 2020–2025 [DD-C35-11 reporting]) gives $15–75M/yr therapy RF total (in-house + merchant) — consistent with the bottom-up.

**SAM for a 2030 entrant** (sub-100 kW retrofits + LLRF-integrated cassettes, US/EU/friendly-Asia only, China excluded): ~$15–30M/yr. **SOM by 2033:** $1–4M/yr — one to three small facility retrofits plus cassette pilot sales. That is a niche engineering business, not a venture-scale beachhead.

## 6. Go-to-market

- **US-first (only viable lead):** reference-customer path runs through national labs, not hospitals: (1) place a demo LLRF+PA cassette with one lab RF group (SLAC/ALS/TRIUMF-class) via SBIR/DOE-accelerator-stewardship money; (2) win one sub-100 kW tube-replacement tender at a small facility; (3) only then approach an OEM (Mevion/ProTom, the two least vertically integrated) about second-sourcing. Expect 3–5 yr from first contact to OEM design-in — the killer identified by the red team stands.
- **China:** do not attempt as a US person. 国产化 quota funding + Wattsine + CAS self-supply [DD-C35-15][DD-C35-03][DD-C35-13] leave no import slot at this component level; the Phase-5 finding that archetype (g) is "parallel-friendly" is legally true but commercially moot.
- **Channel economics warning:** hospitals buy uptime from OEM service contracts; a cassette vendor captures none of that premium — the downtime narrative in the one-pager does not convert into cassette pricing power.

## 7. Regulatory & geopolitical exposure (per `50_PHASE5_POLICY/POLICY_BRIEF.md`)

The policy brief rates this archetype (g) **✅/✅/✅ — the rare parallel-friendly case**: medical end-use, typically below RF-power ECCN thresholds, not OISP-covered; the binding gates are medical-regulatory (NMPA in CN; FDA/CE carried by the integrating OEM) plus China's 2026 domestic-procurement preference. Verified against the CCL this mission: ECCN 3A001.b.4 controls *microwave* solid-state amplifiers with thresholds set in the multi-GHz range; kW-class VHF/UHF accelerator amplifiers sit below those parameters and are plausibly EAR99/3A991 [DD-C35-23] — **provisional; classify per final design, and note pulsed high-peak-power variants can approach 3A228/3A229 territory (counsel)**. Nuclear-adjacent end-users (ADS programs like CIADS/MYRRHA) and CAS institutes trigger Entity-List screening on the customer side, not item-side. Net: regulation is the *least* of C35's problems — a notable inversion of most candidates.

## 8. Capital & milestones (if pursued despite §10)

- **2029 H2 (found):** $500K pre-seed/SBIR; 2 kW cassette + LLRF demo; burn ~$30K/mo.
- **2030:** seed $2.5–3.5M; 20–50 kW combined rack; test infrastructure ($1.5–2M of the round — the dominant capex, as red team warned); first lab pilot placement.
- **2031–2032:** first retrofit tender win ($0.5–1.5M revenue); OEM evaluation unit. Series A only clears if an OEM LOI or ≥$3M tender backlog exists by mid-2032.
- Realistic first revenue 2031; cash-flow breakeven not before 2034. The 100 kW test-cell requirement makes this one of the least capital-efficient candidates in the portfolio at seed scale.

## 9. Risks & kill criteria

**Top risks (ranked):**
1. **Incumbent saturation:** BTESA/R&K/Cryoelectra/RFHIC/Thales/R&S globally, Wattsine + CAS in China, and OEMs (IBA) that self-supply — the product already exists at every power level C35 proposes [DD-C35-01][DD-C35-02][DD-C35-17][DD-C35-15].
2. **Qualification clock vs. runway:** 3–5 yr tender/design-in cycles against a 24-month seed runway.
3. **No pricing power:** component vendor beneath OEM service contracts; distressed end-market operators (bond defaults at US proton centers, per red team).
4. **China exclusion** removes the founder's structural advantage entirely.

**Kill criteria (explicit):**
- By **2027-12**: fewer than 2 of 10 interviewed facility RF leads / OEM engineers express concrete second-source intent with budget → kill.
- By **2028-06**: no US lab agrees to host a pilot cassette (even free) → kill.
- If Wattsine, BTESA, or R&K ships an integrated LLRF-in-cassette product line before founding → kill (the last differentiator gone).
- If seed diligence prices required test infrastructure above $2M with no shared-facility alternative (lab partnership) → kill.

## 10. Verdict

**Conviction: LOW (recommend NO-GO as a standalone company).** The red team's core findings survive verification on every load-bearing point: the merchant market is real but small ($40–95M/yr across *all* accelerator RF, $6–15M/yr in therapy), incumbent-saturated at production grade, tender-driven, and closed in China by funded 国产替代. Widening the buyer pool (red-team question 2) roughly triples the TAM versus therapy-only but adds zero moat. The single surviving asset — founder-fit for an **LLRF-integrated, prognostics-rich cassette** — is better deployed as a *product line inside C10* (precision scientific power converters), which shares the identical customer base (labs, fusion, accelerators) with a far better gap analysis.

**Cheapest validation experiments for 2026–2028 (do these regardless — they de-risk C10 too):**
1. **~$0, 2027:** 10 structured interviews with RF group leaders (APS-U, ALS, TRIUMF, one isotope-cyclotron OEM, Mevion) on tube pain, second-source appetite, and whether integrated LLRF would change a tender spec. Pass bar: ≥2 "we'd pilot it" with names attached.
2. **<$2K, 2027:** attend one IPAC/CWRF workshop; count open SSA tenders, bidders, and award prices to harden the $/W and market-size estimates above.
3. **<$15K, 2028:** bench-build a 1–2 kW VHF cassette with FPGA LLRF and health telemetry in the lab; use it as the demo artifact for experiments 1's follow-ups — and as the seed of C10's regulation stack if C35 is killed.

---
*23 unique sources; Tier 1–2 = 12/23; zh sources = 11. All load-bearing figures `verified:"fetched"` except where marked snippet/estimate. See `DD_C35_sources.json`.*
