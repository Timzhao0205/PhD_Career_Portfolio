# DD_C10 — Precision Magnet & Scientific Power Converters (WBG-native, fusion/accelerator/lab)

Candidate: C10 · Phase 3 score 88.4 (rank 2), red-teamed to ≈80 · This deep dive **explicitly resolves the four REDTEAM_C10 objections** (marked ▶RT-1…▶RT-4 inline). Sources: `DD_C10_sources.json` (28 unique, 16 Tier 1–2, 9 Chinese-language). Section 7 is **provisional** (no Phase 5 POLICY_BRIEF existed at write time).

---

## 1. Problem & who has it

Three named archetypes:

- **The fusion magnet-systems lead at a DOE Milestone company** (8 awardees: CFS, Thea, Type One, Tokamak Energy, Realta, Zap, Xcimer, Focused Energy; program opened to additional teams June 2025 [DD-C10-11][DD-C10-13]). Their machines need dozens of *actively controlled* coil circuits — fast control, error-field correction, RMP, trim — plus kA-class DC for magnet test stands. In FIA's 2026 supply-chain survey, **48% of respondents flagged power systems and power components as a bottleneck**, the top-cited category; total private-fusion supply-chain spend was **$538M in 2025, projected $681M in 2026** [DD-C10-14]. 69% of suppliers say they lack long-term demand visibility — i.e., incumbents are not tooling up for fusion [DD-C10-14].
- **The stellarator/mirror coil-array architect.** Thea Energy's whole thesis is replacing 3D coils with arrays of planar coils, *each individually driven and software-controlled* (Canis 3×3 demo at ±140 A per coil, 20 K, >3 T at coil [DD-C10-16]). Coil-array architectures convert magnet complexity into **power-converter count** — the converter becomes the product that shapes the plasma. WHAM (the mirror the founder's HSX network sits one lab over from) and Realta continue this line [DD-C10-15].
- **The accelerator power-engineering group without a big in-house team.** A modern ring upgrade is a power-supply avalanche: ALS-U ($590M project [DD-C10-17]) plans *individual* supplies per storage-ring magnet — order 1,200 units (per the project's power-supply paper; count from full text, abstract verified [DD-C10-08]); APS-U installed >2,200 supplies (lab statements; snippet-level, peripheral). Big labs (CERN) design their own and license the drawings out rather than buy catalog [DD-C10-05] — small facilities, hadron-therapy centers, and university labs can't.

The pain is not "ppm supplies don't exist" (they do — §4). It is: **precision + fast dynamics + kA-class + modern telemetry, delivered commercially at private-industry speed**, in a market where the incumbents are either sub-kW catalog products or multi-year custom-quote projects, and where fusion buyers themselves report power systems as their top supply bottleneck [DD-C10-14].

## 2. Product definition & the extreme-performance edge (▶RT-4 resolved)

**The red team is right about the physics, and the one-pager was wrong:** ppm-class stability does *not* live in the switch. It lives in the measurement chain — DCCT, ADC, voltage reference, thermal design — as CERN's own precision-measurement literature makes explicit (LHC-class converters achieve their few-ppm performance through the DCCT+ADC chain [DD-C10-06]), and as Magna-Power demonstrates commercially by bolting a temperature-stabilized fluxgate DCCT option (<50 ppm) onto an otherwise ordinary catalog supply [DD-C10-04]. **Restated edge — what WBG actually buys:**

1. **Control bandwidth.** SiC/GaN switching at 100s of kHz gives closed-loop bandwidths (kHz-class) that thyristor/IGBT supplies cannot reach — this is what fast-control/RMP/vertical-stability and coil-array applications need. CERN-affiliated work published in *JINST* shows exactly this direction: a **modular, scalable SiC-MOSFET converter targeting 0.9 ppm current accuracy without active filters**, using interleaving to kill ripple [DD-C10-07]. The concept is validated in the literature but **not productized as a kA-class catalog line by anyone** (§4).
2. **Precision dynamics per liter and per dollar.** Higher switching frequency shrinks magnetics and filters. ITER's converter plant needs **two 150-m buildings (9,400 m²) and ~5 km of water-cooled busbar** for 44+12 converter units at 0.10–1.35 kV DC [DD-C10-10][DD-C10-09]. National labs don't care about floor space (red team is right); **compact pilot plants and factory-built fusion machines do** — their converter hall is capex, schedule, and siting.
3. **Honest density claim: 2–4× at system level, not 10×.** After the DCCT, output filter, dump circuit, and cooling, the red team's "degrades to 2–3×" is approximately correct; we adopt it. The 10× claim is retired.
4. **EMI is a cost, not a footnote.** Fast edges inject common-mode noise that fights the ppm floor and nearby diagnostics; the mitigation (interleaving, CM chokes, spread-spectrum, layout) is exactly the founder's precision-instrumentation-plus-power-electronics intersection. This is the *hard part that is also the moat*.

**Product line (v1, 2029–2031):** (a) **"FastCoil" rack converter** — bipolar 4-quadrant, 5–50 kW/module, ±(50–1000) A via paralleled SiC modules, ≤10 ppm/8 h with integrated DCCT option, ≥2 kHz closed-loop bandwidth, 100 kHz telemetry over Ethernet, arbitrary waveform, N+1 modular paralleling to multi-kA; (b) **magnet test-stand system** — 1–10 kA/≤50 V assembled from the same modules with quench-safe energy dump; (c) **fleet software**: sequencing, coil-array orchestration API, calibration/drift analytics — the HW+SW split the founder wants. Spec targets sit deliberately in the hole between CAENels (≤100 A catalog) and OCEM/Danfysik custom MW projects (§4).

## 3. Technical feasibility & TRL path

- **Buy:** SiC modules/dies (Wolfspeed/Infineon/onsemi), commercial DCCTs initially (Danisense/LEM class, few-ppm parts exist off the shelf [DD-C10-06]), FPGA/MCU control, standard rack mechanics. **Build:** interleaved power stage, precision analog front end, control firmware, calibration rig, software stack. **Zero cleanroom dependence.**
- **Bench-provable without a reactor:** a 2-module 100 A prototype demonstrating ≤10 ppm/8 h and kHz bandwidth into an inductive load is a <$50K, two-person-year artifact — publishable against the JINST benchmark [DD-C10-07].
- **Hard parts (red team's founder-fit doubts, engaged):** (i) kA-class verification needs a water-cooled load bank and HV interlock floor — realistically **$300–700K of test infrastructure**, deferrable by selling ≤300 A products first and renting university/partner test floors (UW-Madison mirror/HSX connections) for kA validation; (ii) NRTL/CE/EMC (UL 61010, IEC 61000-class EMC) — budget $150–300K and 6–9 months for the first family; (iii) solo founder must hire a power-magnetics engineer and a compliance-experienced ME by month 12 — this is a 3–5 person company by first shipment, not solo.
- **TRL path:** TRL4 bench 2027 (during PhD, as validation) → TRL6 pilot units with a design-partner fusion company 2030 → TRL8 catalog family 2031. v1 in 18 months post-founding is credible **only** for the ≤300 A rack product; kA systems are integration projects layered on it.

## 4. Competitive landscape (▶RT-1 and ▶RT-2 resolved)

**Where the red team's incumbents actually sit (all verified against vendor pages):**

| Player | Verified position | The hole they leave |
|---|---|---|
| CAENels FAST-PS-M | Catalog digital supplies, **30–100 A, 600–900 W, 1U**, 50 ppm/FS, 5 kHz loop, 300 kHz switching [DD-C10-01] | Sub-kW only. No kA, no 4-quadrant high power, no fusion-grade dump/interlock integration |
| Danfysik | SYSTEM 9700 at **10 ppm**, standard line 0.75–100 kW, MW custom [DD-C10-02] | High-stability but slow-dynamics DC; customs are project-quoted; no fast coil-array story |
| OCEM | Custom to **50 kA, 5 ppm**, 3,500 converters delivered, JT-60SA/SPIDER, hadron therapy [DD-C10-03] | Pure custom-project house ("full customer service… 30 years"); no catalog, no fast commercial cycle |
| Magna-Power | Catalog to 10 kA/unit, 54 kA systems, <50 ppm with DCCT option, sold for tokamak coils & HTS test [DD-C10-04] | Crude dynamics (current-source SCR-based heritage), no ppm-class *control* bandwidth, no scientific telemetry/orchestration |
| CERN designs | 4-quadrant to 80 kW / 1,800 A; licenses manufacturing folders out [DD-C10-05] | Proves labs self-design; also proves the designs are licensable — a startup can *legitimately license* a CERN folder as a starting point |
| Jema Energy | ITER coil/heating converters, MAST-U TF (red-team [RT-C10-04]) | Utility-scale thyristor plant EPC; does not serve the fast/aux/test-stand layer commercially |

**▶RT-1 verdict:** the objection **lands against the original "ppm catalog" framing and kills it** — CAENels+Danfysik already own that phrase. It does **not** cover the actual gap: *fast-dynamics, telemetry-rich, modular converters from 5 kW to multi-kA sold as product with weeks–months lead time*. CAENels stops at 900 W [DD-C10-01]; everyone above that is custom-quote [DD-C10-02][DD-C10-03]. The JINST work shows the technical direction is real and unproductized [DD-C10-07]. Caveat kept from the red team: **no source evidences willingness-to-pay for lead time** — that is validation experiment #2 (§10).

**▶RT-2 verdict (what layer remains buyable):** correct that CS/PF main converter plants go to Jema/Rongxin-class EPCs and that CFS vertically integrates — the CFS–Realta deal explicitly bundles magnets with cryo/power/structure ("multi-billion dollar" potential) [DD-C10-15]. **But China's own tender record proves the fast/auxiliary layer is procured separately even on flagship machines:** BEST's 内真空室快控电源 (in-vessel fast-control supplies) and HL-3's RMP 电源升级 were discrete tenders won by Actionpower in Dec 2025 [DD-C10-24]; BEST's 磁体电源系统 went to 新风光 for **¥108M** with the magnet-power *energy-storage* system a separate **¥81M** award [DD-C10-23]. The buyable startup layer = fast/aux/trim converters + magnet test stands + coil-array drive — not the GW thyristor plant, and not CFS itself as a customer.

**China landscape (Chinese-language sourcing):**

- **荣信汇科 (Rongxin Huike):** member of the SWIP-led consortium that signed the **ITER ELM-PS contract at ITER HQ on 2026-01-22** [DD-C10-25]; participates in ITER main-coil/VS1 power, HL-3, and the CFQS-T quasi-axisymmetric stellarator test platform; second STAR-Market IPO attempt in progress (SSE inquiry response filed 2026-03) [DD-C10-28].
- **爱科赛博 (Actionpower, SSE-STAR 688719):** the closest Chinese analog of this candidate — precision fast/correction/RMP magnet supplies; won BEST fast-control and HL-3 RMP upgrades within one December [DD-C10-24].
- **英杰电气 (Injet, 300820):** power supplies for HL-3, EAST, BEST, Chengdu "天府造太阳"; its own board secretary states fusion is still a small revenue share and mostly research-institute stage (2025-05) [DD-C10-26].
- **Demand context:** BEST (合肥, built by 聚变新能) completes **end-2027** targeting 20–200 MW fusion power demonstration [DD-C10-19][DD-C10-20]; Huachuang Securities counts **¥17.6B of BEST-ecosystem tenders Q1–Q3 2025, ¥3.9B in November alone, ¥2.4B awarded in early December**, and projects **¥146.5B** of announced domestic fusion project investment (BEST ≈ ¥14.5B, CFEDR ≈ ¥100B) [DD-C10-23]. (A snippet-level source claims a different BEST total; the fetched ¥14.5B figure is used. Discrepancy noted.)
- **Policy tailwind:** the CPC Central Committee's 15th Five-Year-Plan proposals name 核聚变能 (fusion energy) alongside quantum and 6G as a "future industry" growth point [DD-C10-21][DD-C10-22] — guaranteeing continued domestic tender flow *and* continued domestic-champion capture of it.

## 5. Market: beachhead sizing (bottom-up), then triangulation

**Beachhead = US/EU/UK/JP fusion fast-magnet-power + magnet test stands + small-facility precision supplies.**

Bottom-up arithmetic (2029–2032 annual run rate, ex-China):

- **Segment A — fusion device fast/aux converters.** Devices plausibly in construction/commissioning ex-China 2029–2032: SPARC→ARC, Infinity Two, Eos, Tokamak Energy demo, Zap scale-up, Realta prototype, 1–2 European/Japanese — take **8 devices / 3 yr ≈ 2.7/yr**. Fast/aux/trim converter content per device: **10–40 units × $60–250K ≈ $1.5–6M** (midpoint $3.5M; benchmark: one BEST magnet-power tender = ¥108M ≈ $15M for the *full* magnet-power system, of which fast/aux is a slice [DD-C10-23]). → **≈$9M/yr (range $4–16M)**.
- **Segment B — HTS magnet test-stand & qualification supplies.** ~25 active magnet programs (milestone companies [DD-C10-11], integrators, labs, universities) × ~0.5 systems/yr × $150–400K → **≈$3.5M/yr (range $2–5M)**.
- **Segment C — small accelerators, hadron-therapy, quantum/university labs** reachable without FAR past-performance: **$2–4M/yr** (OCEM alone has shipped "hundreds" of supplies to hadron-therapy centers [DD-C10-03]).

**Beachhead SAM ≈ $15–25M/yr** in the launch window. **SOM: $1.5–4M revenue by 2031–32** (2–3 fusion design partners + one therapy/lab account) — honest and small; this is a wedge, not the business.

Triangulation top-down: FIA-surveyed supply-chain spend $681M (2026, ~half of companies reporting) with power systems the #1 bottleneck category [DD-C10-14]; if power conversion is 5–10% of device capex (ITER's 44-unit, two-building plant scale suggests the low end for tokamaks [DD-C10-10]) and Western private fusion capex reaches $2–4B/yr by 2030, device power conversion ≈ **$100–400M/yr**, of which the fast/aux/test slice at 15–30% ≈ **$15–120M/yr** — brackets the bottom-up figure. Expansion layers: main magnet-power packages ($15–30M/device, China benchmark [DD-C10-23]), ring upgrades (~1,200 supplies/project [DD-C10-08]; ALS-U $590M class [DD-C10-17]), with magnets confirmed as "~one-third of core machine cost" for superconducting fusion devices — the budget line the power hardware rides [DD-C10-18]. TAM (global scientific/precision magnet power) plausibly **$0.5–1.5B/yr by early 2030s — estimate, no fetched market report; treat as indicative.**

## 6. Go-to-market (▶RT-3 resolved: China angle honestly reassessed)

**US-first. The one-pager's "direct CAS/BEST procurement pipeline" claim is retired.** Evidence: every named BEST/HL-3/ITER-China power award went to domestic listed firms or CAS/SWIP consortia [DD-C10-23][DD-C10-24][DD-C10-25]; fusion is now a named 15th-FYP future industry with implicit domestic-preference gravity [DD-C10-21]; and a US-person founder selling dual-use-adjacent kA power systems into CAS institutes faces friction from both governments (§7). **Reassessed China role: (a) competitive-intelligence asset — the founder reads tender documents natively and can price/spec against 爱科赛博 and 荣信汇科 quarterly (a real, rare advantage no US competitor has); (b) supply chain for non-controlled content (magnetics, mechanics, passives); (c) NOT a revenue channel before 2032, if ever.** Skip as market; use as radar and cost base.

**US sequence:** 2026–2028 (in-PhD): publish the SiC ppm-converter benchmark; place one custom fast converter in WHAM/HSX-adjacent experiments as reference. 2029: found; convert 2 milestone-program companies into paid design partners (their PDR→build waves and the program's expansion cohort [DD-C10-13] mean procurement decisions continue past 2029 — the red team's "you arrive after the spec wave" is only half right: the *second* cohort and the build/iteration phase buy 2029–2032). 2030–31: catalog family + NRTL; add one hadron-therapy or university-ring account for non-fusion credibility. Channel: direct founder-led sales; reference-customer strategy identical to how Magna-Power got designed into tokamak test stands [DD-C10-04]. **EU/UK** (Tokamak Energy, Proxima, Gauss) via CE mark in 2031; consider licensing a CERN 4-quadrant manufacturing folder to compress design time and buy instant credibility [DD-C10-05].

## 7. Regulatory & geopolitical exposure — **PROVISIONAL** (no Phase 5 brief existed; coordinate later)

- **Export controls:** catalog programmable DC supplies are generally **EAR99** — Magna-Power publishes exactly this classification for its line [DD-C10-27]. **But** ECCN **3A226** (nuclear-nonproliferation column) captures high-power DC supplies exceeding **100 V and 500 A over 8 h with stability better than 0.1%** (threshold text verified only at snippet level — confirm against the current CCL before relying). A kA-class *high-voltage* precision system can trip it; many practical designs (≤50 V at kA, like Magna-Power's 8 V/10 kA units) sit below the voltage prong. Design-for-classification is feasible and should be deliberate. China sales of tripped items would need licenses; unlikely to be granted for CAS fusion end-users — reinforcing §6.
- **Deemed export:** hiring non-US-person engineers on controlled line items needs review; keep the precision line EAR99-clean where possible.
- **Outbound investment / US-person restrictions:** the 2025 outbound program covers semiconductors/quantum/AI categories; fusion power electronics is not squarely listed (snippet-level; Treasury page unreachable at run time — **verify in Phase 5**). A China-incorporated variant of this company is nonetheless structurally unattractive per §6.
- **CFIUS:** a US-incorporated company taking later Chinese capital in "critical technologies" would invite review; plan cap table US/EU-only.
- **Certification burden:** NRTL (UL 61010-class), CE LVD/EMC for EU; no nuclear licensing — fusion supplies are conventional electrical equipment. Budgeted in §3/§8.

## 8. Capital & milestones (2029→2032)

- **Pre-seed/seed 2029: $2.5–4M** (deep-tech seed ceiling respected). Team of 4–5. Spend: $0.9M/yr payroll ramp, $0.5M test floor (deferred kA), $0.25M compliance, $0.3M inventory.
- **Milestones:** M1 (mo. 9): ≤10 ppm/8 h, 2 kHz-loop 300 A bipolar product demo → 2 paid pilots ($150–400K each; **first revenue 2030**, matching the red team's realistic timing). M2 (mo. 18): NRTL'd catalog family, $1M cumulative revenue. M3 (mo. 30): kA test-stand system delivered to a magnet program; $3–4M ARR run rate; orchestration software attached to ≥1 coil-array customer.
- **Series A 2032 ($8–15M)** on: 2 fusion design wins + non-fusion segment proof + software attach. Burn to A: ≈$3.5M. If Segment A units slip (fusion schedule risk is systemic), the therapy/lab segment must carry M2 — otherwise bridge, not A.

## 9. Risks & kill criteria

**Risks (ranked):** (1) **Procurement reality** — labs buy on FAR/past-performance decade cycles; fusion companies may buy lowest-bid Magna-Power or in-house the fast converters; premium-for-lead-time unproven [red team, adopted]. (2) **Fusion schedule slip** compresses Segment A to near zero in the launch window. (3) **Incumbent response** — CAENels extending FAST-PS up-power, or Danfysik productizing a fast line, erases the hole. (4) **Vertical integration spread** — if CFS-style "magnets including power" bundles become the industry norm [DD-C10-15], only test stands remain. (5) **Solo-founder capital intensity** of kA safety-rated test infrastructure. (6) China closed (accepted, planned around).

**Kill criteria:** kill or pivot if, by **end-2027**: <2 fusion companies will sign an LOI/paid pilot ≥$100K for a fast-converter spec; or bench prototype cannot hold ≤20 ppm/8 h with ≥1 kHz loop at 300 A for <$40K BOM; by **end-2030**: no repeat order from any design partner, or an incumbent ships a kA-class fast-dynamics catalog line at <$1/W; at any point: ≥2 of the 4 largest prospective customers announce in-house or bundled magnet-power sourcing.

## 10. Verdict

**Conviction: MEDIUM** (downgraded from the Phase 3 rank-2 enthusiasm; the red team wins on ▶RT-3 and ▶RT-4, splits ▶RT-1/▶RT-2). The correctly-restated product — *fast-dynamics precision magnet power, 5 kW to multi-kA, sold as a modern commercial product into the fusion build-out, with China as radar not market* — is a real, small, winnable wedge with exceptional founder fit (power electronics × precision instrumentation × big-science credibility × native-Chinese competitive intel). It is a $2–4M-by-2031 wedge that must earn its Series A through expansion, not a standalone rocket. Strong candidate for **merger with C11** (quench protection — same customers, same bench, same modules).

**Cheapest validation experiments (2026–2028, during PhD):**
1. **Benchmark artifact (<$40K, uses Rivas-lab adjacency):** 2-module interleaved SiC bipolar converter, 300 A class, instrumented against a commercial DCCT; target ≤10 ppm/8 h + 2 kHz loop; publish vs. the JINST 0.9 ppm design [DD-C10-07]. Pass/fail is unambiguous.
2. **Willingness-to-pay test (≈$0):** structured interviews + LOI asks with magnet-power leads at ≥8 milestone/expansion-cohort companies [DD-C10-11][DD-C10-13]; count 2026–27 public RFQs for fast/aux converters; the specific question is *"what premium for 12-week delivery vs 18-month custom quote?"* — this directly tests the red team's strongest unresolved objection.
3. **Reference deployment via the Wisconsin network (<$15K):** place one custom fast bipolar supply into WHAM/HSX-adjacent experiments; one operating unit inside a confinement experiment converts diagnostics-side credibility into converter-side credibility before founding.
