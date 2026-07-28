# P3R2 micro-wave G — final CN top-up (3 seeds)

Generator: idea-architect, claude-fable-5 / xhigh (configured route). Date: 2026-07-13.
Mandate: close the 35/36 CN longlist gap with the three judge-named directions from
`P3R2_ELEGANCE_ADJUDICATION_R2.md` §5 — (a) CN big-science vacuum (L07-045 anchor),
(b) CN accelerator/cyclotron component localization (L05-036 anchor, beyond F-20's HV slice),
(c) CN 800VDC conversion-base retrofit instrumentation (L02-054 anchor, distinct from C-01).
Firewall respected: founder profile and SEEDS_A–D not read. All cited IDs verified in
`90_BIBLIOGRAPHY/sources.json` as `accepted: true` and `verified_non_india_origin` /
`verified_multinational_allowed`; none of the 42 quarantined IDs is cited. Evidence-hygiene
notes: L05-038 and L07-007 are REJECTED records and are not cited; L02-054 is cited only for
its verifier-corrected content; L05-035 order figures and L05-028 backlog claims are treated
as unverified pending re-fetch. India/Singapore excluded throughout; JP/TW/KR secondary only.
[R3 correction 2026-07-13]: the ~12%/78% CN HVDC-vs-UPS penetration figure formerly cited to
L02-048 is likewise UNVERIFIED (raw-ledger WebSearch synthesis; not in the verified record) and
is demoted to not-load-bearing per `P3R2_ELEGANCE_ADJUDICATION_R3.md`; all three seeds below
carry FIX_APPLIED per that ruling.

---

## P3R2-G-01 — Certified UHV conditioning and acceptance systems for China's big-science vacuum supply chain (CN)

- **Product:** A conditioning-and-acceptance island sold to China-registered vacuum-chamber
  fabricators: instrumented vacuum-firing/bakeout station with model-based hydrogen-depletion
  endpoint control (replacing the fixed open-loop recipe), integrated outgassing-rate /
  helium-leak / RGA acceptance metrology traceable to witness standards, and certification
  software producing signed per-chamber acceptance dossiers. Equipment + recurring
  calibration/certification; "treat-to-spec" for vacuum chambers.
- **CN buyer + pain evidence:** IHEP's HEPS insertion-device chamber tender is restricted by
  rule to China-registered manufacturers that are themselves the manufacturer of the offered
  product (L07-045 — [FIX applied: PRC-registration + manufacturer eligibility clause
  independently verified in the primary tender document at ccnta.cn, 2026-07-13; ledger
  claim_supported repair assigned to the orchestrator]) — so domestic fabricators must own the
  conditioning/acceptance craft themselves. That craft is documented as rigid and expensive:
  250 °C/30 h bakeout for >70,000x hydrogen-outgassing reduction (L07-009; material dependence
  L07-008), with no validated faster alternative in the lane. [FIX applied: the former
  "imported metrology channel bifurcating under trade restrictions" reading of L07-053 is
  deleted as an over-read — INFICON FY2025 (Americas −12.4% vs Asia-Pacific +19.2%) is
  market-structure context only; APAC growth evidences continued import availability, so the
  wedge is the tender rule plus the fabricators' capability gap, not an import barrier.]
  Procurement cadence beyond one facility: ASIPP tender pattern (L01-037, L01-038).
- **Mechanism:** in-situ outgassing measurement (throughput + rate-of-rise) drives a
  hydrogen-diffusion depletion model to a measured stop criterion instead of a fixed 30-hour
  recipe; the same instrument set doubles as the acceptance bench (leak, RGA cleanliness,
  outgassing certificate), so conditioning and certification are one workflow.
- **Why incumbents miss it:** furnace makers sell heat, not certified vacuum outcomes;
  instrument vendors (INFICON-class) sell gauges, not process control or dossiers; SAES sells
  coating (L07-037) and is outside the localization rule; institutes build one-off in-house
  benches and never productize; Western integrated suppliers cannot pass the China-registered
  tender rule at all — the rule that blocks them is the wedge for equipment sold *behind* it.
- **Non-duplication vs nearest survivor:** nearest is **A-05** (US merchant NEG-coating and
  low-outgassing surface-engineering *service* line), whose CN variant **B-12 was REJECTED**
  (license-into-China of process know-how = IP leakage; CEPC-lumpy demand). G-01 sells no NEG
  coating, no treatment service, and licenses no coating recipe: it sells conditioning
  equipment + acceptance metrology + certification to CN fabricators, with the moat in
  calibrated reference standards and continuously updated endpoint models (which iterate with
  hardware generations) rather than a one-time transferable recipe, and with demand anchored
  in the tender-rule capability gap plus multi-facility cadence rather than CEPC alone. Also
  distinct from F-22 (RF vacuum capacitors) and F-02's absorbed entry SKU (cryogenic
  leads/feedthroughs — electrical components, not surface/process engineering).
- **Decisive experiment + budget:** 2027-Q4, $300k — instrumented bench on 316L witness
  chambers: measured-endpoint control reproducing the >70,000x H2 reduction benchmark
  (L07-009) with ≥30% cycle-time reduction vs 250 °C/30 h over N=10 runs; in-situ rate-of-rise
  agreeing with lab-standard throughput measurement within ±20%.
- **TRL:** 4.
- **2026–2029 plan:** endpoint-model publication + bench build (2026–27); 2028 validation via
  a non-CN accelerator-lab cooperative agreement (complementary to A-05, not competing) + CN
  channel scouting, licensed-entity design, IP split frozen; [FIX applied: BINDING 2028
  evidence gate — document that CN facilities impose vacuum-acceptance requirements on
  fabricators at delivery (tender technical annex, facility vacuum-acceptance spec, or
  fabricator quality requirement), the buyer-existence proof that fabricators (not institutes)
  own conditioning/acceptance; no 2029 paid pilot without it]; 2029 paid pilot with one
  China-registered chamber fabricator; [FIX applied: BINDING P4 pre-promotion condition —
  re-date the 2021-vintage L07-045 anchor AND evidence >=2 additional CN chamber-class tenders
  (HEPS follow-on/CSNS/ASIPP-pattern) to establish multi-tender cadence beyond CEPC; name a
  NIM-class CN metrology anchor for witness-standard traceability] (rule 18).
- **Named 2030–2034 trigger:** CEPC construction approval under the 15th Five-Year Plan — the
  funded pre-construction program is evidenced by IHEP's CEPC-specific klystron prototypes
  (L05-012, L05-013); approval means ~100 km of vacuum sections procured under
  China-registered-manufacturer rules. Secondary cadence: HEPS-pattern follow-on/upgrade
  tenders (L07-045) and ASIPP fusion power/vacuum upgrades (L01-037/038 pattern).
- **2030 competition (incl. domestic substitution):** SAES (constrained by localization rule),
  Western metrology vendors selling gauges, not process control or certification dossiers
  ([FIX applied: L07-053 retained as market-structure context only — imports remain available,
  APAC +19.2% FY2025]), domestic furnace makers, institute in-house benches, and the main
  threat — a large CN fabricator internalizing the bench or a CAS institute publishing a free
  reference recipe.
- **Access/window risk:** foreign founder cannot bid tenders; sells to eligible fabricators
  via licensed CN entity (margins mid; manufacturing conceded). IP risk = bench absorption,
  countered by calibrated standards + model updates. Dominant timing risk = CEPC slip (the
  B-12 defect), priced via the BINDING P4 pre-promotion cadence requirement (re-dated L07-045
  + >=2 additional CN chamber-class tenders) and kill gates.
- **Kill date:** 2034-12-31; interim: no paid CN fabricator pilot by end-2029; CEPC unapproved
  AND no non-CEPC facility-driven order by end-2032.
- **Vision:** chambers ship with measured outgassing certificates the way steel ships with
  mill certs — across accelerators, fusion, quantum and semiconductor chamber supply chains,
  extending to XHV acceptance where gauge physics is still open (L07-002, L07-001).
- **Nearest substitutes:** fixed-recipe in-house bakeout (status quo); outsourced treatment
  (A-05-class, US only); buying a furnace and gauges separately without certification.
- **Key uncertainty:** will fabricators pay for certified conditioning equipment, or will
  facility specs stay loose enough that open-loop recipes suffice? (2029 pilot gate answers.)
- Sources — demand: L07-045, L01-037, L01-038, L07-053; technical: L07-009, L07-008, L07-001,
  L07-002, L05-012, L05-013; competitors: L07-037, L07-036, L07-053.
- **[FIX applied 2026-07-13 R3]:** L07-053 "bifurcation constrains imports" over-read deleted
  (INFICON kept as market-structure context only — APAC +19.2% = continued import
  availability); BINDING 2028 fabricator-owns-acceptance evidence gate added before the 2029
  paid pilot; multi-tender cadence proof beyond CEPC (re-dated L07-045 + >=2 additional CN
  chamber-class tenders) made a BINDING P4 pre-promotion condition; judge's primary-source
  verification incorporated (PRC-registration + manufacturer clause confirmed at ccnta.cn
  2026-07-13; L07-045 ledger claim_supported repair assigned); NIM-class metrology anchor
  named as P4 task. Verdict: FIX_APPLIED (N7/E7/C6/V6/T5).

---

## P3R2-G-02 — Merchant beam-exit windows, X-ray conversion targets, and target-interface consumables for China's irradiation and isotope fleet (CN)

- **Product:** cross-platform qualified family: Ti-alloy foil exit-window assemblies with
  engineered cooling frames and statistically certified burst margins; water-cooled Ta/W
  X-ray conversion-target assemblies for e-beam→X-ray sterilization at post-2025 energy
  limits; cyclotron target-interface hardware; foil-health monitoring (IR + rupture detection,
  <10 ms vacuum-protection interlock); certified per-lot datasheets + consumables program.
- **CN buyer + pain evidence:** China Isotope & Radiation / Atom Hi-Tech centrally procured
  three self-shielded cyclotrons for the named Haikou, Nanyang, and Nanchong isotope centers
  (L05-036) — every center consumes target foils/windows continuously once operating. CGN
  Dasheng's listed e-beam accelerator business is active and expanding (L05-035; contract
  figures pending text-extractable re-fetch — not load-bearing). ISO 11137-1:2025 raised
  allowable e-beam energy 10→11 MeV and X-ray 5→7.5 MeV (L05-042) — [FIX applied: a PERMISSIVE
  change, not a mandate: re-qualification demand arises only where operators choose to uprate
  for throughput, so uprating adoption is a BINDING 2028 evidence gate, not an assumed
  fleet-wide wave]; beam-facing vacuum interfaces
  are documented as "among the most common issues" in high-power vacuum-electronic devices
  (L05-014 — adjacent-interface evidence, honestly labeled). US expansion chapter (not counted
  as a primary leg): cargo-linac converter demand context (L05-033) and the ARDAP ecosystem
  channel (L05-031).
- **Mechanism:** thermo-mechanical foil engineering under scanned-beam heat flux (cooling-frame
  design, burst-margin statistics from instrumented cycling), laminated water-cooled Ta/W
  converters for ~100 kW-class beam power, and machine-protection instrumentation that turns a
  consumable into a monitored subsystem.
- **Why incumbents miss it:** OEMs (IBA/L3-class, Varex, CGN Dasheng) treat windows/targets as
  captive internal spares tied to their machines — [FIX applied: "no merchant, certified,
  cross-platform supplier exists" is held as JUDGMENT pending the PRE-PROMOTION BINDING P4
  merchant-targetry map (ARTMS/Comecer-class + IBA's own target business)]; operators are
  locked to OEM pricing/lead times; [FIX applied: the 2025 energy-limit change (L05-042) is
  permissive — where operators uprate, OEMs must re-qualify, an opening contingent on uprating
  adoption (2028 evidence gate)]; in CN, imported spares face localization pressure.
- **Non-duplication vs nearest survivor:** nearest are **C-09** (canonical merchant
  modulator/drive-chain platform — shares CN demand anchors L05-035/036; this is evidence
  overlap, not concept overlap, exactly the F-10/F-11 precedent: C-09 drives the beam, G-02
  owns where the beam exits the vacuum) and **F-09** (RF-vacuum windows/couplers sold into
  vacuum-electron-device primes for the RF path — different physics: foil thermo-mechanics
  under particle-beam flux vs RF dielectric windows; different buyers: operators/isotope
  centers/aftermarket vs tube primes; different economics: consumables vs qualified
  internals). Merged C-10's dose-metrology content is not reproduced — G-02's monitoring is
  machine-protection interlock, not dosimetry.
- **Decisive experiment + budget:** 2027-Q3, $350k — 60 kW-class beam-equivalent heat-flux
  test cell: foil assembly surviving ≥2,000 thermal cycles at 11 MeV-era flux with measured
  burst margin ≥3x rated differential; Ta converter coupon cycling; rupture-detection
  interlock <10 ms to isolation-valve trigger. [FIX applied: VALIDITY LIMIT declared —
  surrogate heat flux validates thermo-mechanics and interlock speed only, NOT
  radiation-driven foil degradation (embrittlement, blistering); beam-time validation is bound
  into the 2028 co-development gate.]
- **TRL:** 4.
- **2026–2029 plan:** 2026–27 failure-mode/patent map + test cell + decisive experiment;
  2028 BINDING gate — co-development/evaluation agreement with one named operator or OEM
  rebuild channel (CN via licensed entity), plus P4-grade verification of the 2021–2035
  medical-isotope plan primary text and re-extraction of L05-035/L05-028 figures; [FIX
  applied: second BINDING 2028 evidence gate — named operators/OEMs actually uprating to
  11 MeV/7.5 MeV under ISO 11137-1:2025, else the ISO trigger de-weights to CN consumables +
  localization demand only; beam-time validation of radiation-driven foil degradation via the
  co-development partner]; 2029 paid qualification order for spares on one installed machine
  class; JV IP split contractualized before any CN manufacturing.
- **Named 2030–2034 trigger:** the CNNC / China Isotope & Radiation centralized-procurement
  cadence — follow-on cyclotron/isotope-center tenders after the 2024 three-center round
  (L05-036), under the named Medium-and-Long-Term Medical Isotope Development Plan
  (2021–2035; primary text to be fetched in P4 — flagged, not yet atlas-verified). Parallel:
  continued EtO-replacement/X-ray adoption under ISO 11137-1:2025 (L05-042) served by CGN
  Dasheng-class capacity (L05-035).
- **2030 competition (incl. domestic substitution):** OEM in-house spares (IBA — L05-028
  identity-level only; Varex internal targets — L05-033; CGN Dasheng in-house — L05-035;
  CPI-class tube/system houses — L05-050); [FIX applied: specialty merchant targetry houses
  (ARTMS/Comecer-class + IBA's own target business) — PRE-PROMOTION BINDING P4 incumbency map
  for the cyclotron-target leg; if merchant targetry is already served, re-scope to the
  e-beam/X-ray window+converter leg where the merchant white space is more plausible];
  CNNC-ecosystem machine shops copying foil geometry — the certified burst-statistics dossier
  + interlock integration is the anti-copy wedge. [FIX applied: portfolio pre-agreement —
  G-02 joins the R2 beam-components portfolio evaluation (F-09/F-20, with C-09/D-07 adjacency)
  at P4; at most one funded beam-components company.]
- **Access/window risk:** consumables for SOE-adjacent buyers must be made in-country —
  licensed JV manufactures, founder retains foil-bonding/qualification and monitoring IP;
  copying and CNNC-internal preference are real and priced in the kill gates. Honest gap:
  window/target failure *economics* are inferred (L05-014 + consumables logic), not yet
  documented — the 2028 co-development gate is binding for exactly this reason. Market must be
  sized bottom-up from fleet counts in P4; claimed as a beachhead wedge, not a big TAM.
- **Kill date:** 2034-12-31; interim: no operator/OEM co-development agreement by end-2028 →
  stop; no paid qualification on an installed fleet by end-2030 → fold to licensing the
  qualification/monitoring package.
- **Vision:** the merchant beam-facing-consumables company for the irradiation economy —
  windows, converters, targets and their health instrumentation across sterilization, isotope
  production, cargo scanning, and FLASH-era machines where interface thermal loads only grow
  (L05-023, L05-024).
- **Nearest substitutes:** OEM spares contracts (status quo); in-house machine-shop foils;
  running windows to failure with scheduled replacement.
- **Key uncertainty:** whether operators/OEMs will buy reliability-critical beam-facing parts
  from a merchant supplier (the F-09 "internal art" question, here softened by the consumable
  replacement cycle and — where uprating adoption is evidenced — the permissive 2025
  energy-limit opening).
- Sources — demand: L05-036, L05-035, L05-042, L05-033; technical: L05-014, L05-042, L05-023,
  L05-024; competitors: L05-028, L05-033, L05-035, L05-050.
- **[FIX applied 2026-07-13 R3]:** "ISO 11137-1:2025 forces fleet-wide re-qualification"
  corrected to a PERMISSIVE uprating change with a BINDING 2028 evidence gate (named uprating
  operators/OEMs, else the ISO trigger de-weights to CN consumables + localization only);
  merchant-targetry incumbency map (ARTMS/Comecer/IBA targets) made PRE-PROMOTION BINDING for
  the cyclotron-target leg with pre-agreed re-scope to the e-beam/X-ray window+converter leg;
  surrogate-flux validity limit declared in the decisive experiment with beam-time validation
  added to the 2028 gate; beam-components portfolio pre-agreement with F-09/F-20 (C-09/D-07
  adjacency) recorded — at most one funded. Verdict: FIX_APPLIED (N6/E6/C6/V6/T6).

---

## P3R2-G-03 — DC-conversion acceptance and commissioning instrumentation for the UPS→HVDC/800VDC transition (US+CN)

- **Product:** portable acceptance island + protocol software: GaN-based swept-impedance
  bus-stability analyzer (source/load impedance overlap and stability margins on live
  240/336/±400/800VDC buses), insulation/ground-fault characterization for unearthed IT DC
  networks, hot-swap/inrush transient capture, and automated signed acceptance dossiers mapped
  to IEC 62477-1 (L02-112) and OCP/GB frameworks. Out-of-path measurement — it qualifies power
  hardware; it is not power hardware.
- **CN buyer + pain evidence:** the CN opportunity is the *conversion base*, resting on
  verified deployment anchors — Delta/Alibaba Panama 240VDC in Zhejiang/Jiangsu (L02-048),
  Autrans/East-Data-West-Computing (L02-049), architecture churn (L02-054). [FIX applied: the
  "~12% HVDC vs 78% UPS (~2021)" penetration figure is UNVERIFIED (not in the verified
  L02-048 record; raw-ledger WebSearch synthesis only) and NOT load-bearing; P4 must re-source
  an eligible CN installed-base/penetration figure before final scoring.] So 2030–2034 CN work
  is converting existing UPS halls across at least three architectures — Panama 240VDC
  (L02-048), ±400V transitional and 800V (L02-054) — while Chinese engineering coverage names
  SiC voltage-rating, LLC resonant
  conversion, and isolation design as core unresolved hurdles (L02-054, verifier-corrected
  content). Buyers: Alibaba-lineage operators and their integrators — Delta China (L02-048),
  Shenzhen Autrans supplying Alibaba datacenters and East-Data-West-Computing parks (L02-049);
  component uncertainty in the domestic chain (sole mainland NVIDIA-list chip supplier without
  disclosed orders — L02-050) sustains third-party verification demand.
- **US leg:** NVIDIA-specified 800VDC for 2027 Kyber/Rubin-Ultra racks (L02-043) and OCP
  Mount Diablo standardizing multiple PSU architectures (Google/Meta/Microsoft — L02-044);
  even direct SiC suppliers say the transition "will take time to scale" (L02-047) — the slow
  part is integration/qualification, which is this product's market. New conversion stages
  (e.g., 800V-to-6V boards, L02-046) all need site-level qualification.
- **Mechanism:** power-hardware perturbation injection + wide-band impedance spectroscopy on
  live buses, Middlebrook/passivity margin computation, pattern-injection ground-fault
  localization on IT networks, and standardized test sequences — the acceptance dataset
  compounds into a cross-vendor library no single equipment vendor can replicate.
- **Why incumbents miss it:** instrument majors sell general meters, not system-level DC
  acceptance; integrators self-certify their own gear and will not warranty mixed-vendor
  halls; insulation-monitoring vendors sell devices, not commissioning toolchains; DC site
  acceptance has no standard (IEC 62477-1 is converter safety — L02-112; the decade-old
  SST/IEC 60076 mismatch shows how slowly DC standards adapt — L02-036).
- **Non-duplication vs nearest survivor:** nearest is **C-01** (canonical 800VDC in-path
  protection/hot-swap unit, which absorbed A-01 analytics and B-03 damping). C-01 lives in
  the power path and interrupts faults; G-03 is out-of-path measurement + acceptance evidence
  for the whole conversion project — C-01-class hardware is among the things G-03 qualifies.
  This mirrors the endorsed protection-vs-measurement split (E-14/F-06), but with commercial
  (non-State-Grid) CN buyers, avoiding the condition that downgraded F-06's CN leg. Evidence
  hygiene: G-03 relies only on L02-054's verifier-corrected content, not the uncorroborated
  grounding/hot-swap claim that C-01's text cites. Also distinct from C-05/C-22 (offline qual
  benches in other lanes) and F-19 (fluid operations/consumables).
- **Decisive experiment + budget:** 2027-Q2, $300k — injector/analyzer prototype on a 100 kW
  800VDC testbed with deliberately mis-tuned LLC stages: predict instability from measured
  impedance overlap and validate against observed oscillation across ≥20 configurations;
  hot-swap transient capture benchmarked against reference instrumentation. [FIX applied:
  testbed assumed as loaner/partner hardware (OCP-member or integrator lab); the $300k covers
  injector/analyzer build and test time, not testbed ownership.]
- **TRL:** 4.
- **2026–2029 plan:** method benchmarks + OCP power-workstream participation (2026–27);
  prototype + decisive experiment (2027); 2028 paid pilot audits — one US commissioning firm,
  one CN integrator via HK/CN licensed entity; [FIX applied: 2029 BINDING gates split per
  market — (US) no US frame agreement by end-2029 → US leg folds to niche lab tooling; (CN) no
  CN integrator frame agreement by end-2029 → CN leg downgrades to license-only with the
  honest flag change applied (F-06 precedent)] + P4 re-source of an eligible CN
  installed-base/penetration figure (the ~12%/78% figure is unverified, not load-bearing),
  evidence for the 8–12-year refresh-cycle inference, and re-verified SOE procurement cadence
  per rule 18.
- **Named 2030–2034 trigger:** US — post-2027 scaling of NVIDIA's 800VDC production
  architecture (L02-043) and OCP Mount Diablo spec revisions (L02-044). CN — (a) refresh-cycle
  conversion of the legacy UPS installed base (verified deployment anchors L02-048/L02-049)
  [FIX applied: the ~12%/78% penetration figure is UNVERIFIED and not load-bearing — P4
  re-source required; the 8–12-year refresh cycle is labeled INFERENCE and must be evidenced
  in P4]; (b) implementation programs under the April 2026
  national AI-energy action plan, Guo-Neng-Fa-Ke-Ji [2026] No. 34 (L14-036 — verified content
  only; the trade-press "100% liquid-cooling mandate" is debunked and NOT relied on);
  (c) East-Data-West-Computing park expansion (L02-049). SOE telecom HVDC
  collective-procurement cadence is named as a channel and flagged P4-verify.
- **2030 competition (incl. domestic substitution):** integrator self-certification (Delta,
  Huawei-ecosystem, Autrans — L02-048/049); [FIX applied: instrument majors' DC-acceptance
  roadmaps (Keysight/Chroma/Hioki/Fluke) and CN certification institutes (CQC/CEPREI-class
  service-only testing) — PRE-PROMOTION BINDING P4 competitor map; the third-party-acceptance
  willingness thesis must survive it]; protection vendors bundling diagnostics;
  Innoscience-based domestic designs maturing (L02-050).
- **Access/window risk:** datacenter-adjacency declared: demand is anchored to
  retrofit/acceptance of the existing installed base and per-project commissioning spend —
  the downturn-resistant slice (F-19 precedent) — not to incremental AI capex; a total DC
  investment freeze would still slow it (stated, not hidden). Core demand risk: operators may
  accept vendor self-certification — the 2029 frame-agreement gate is binding. CN margins on
  instrument + per-project license via licensed entity; hardware is copyable, so the moat is
  the validated methodology + cross-vendor sequence library + dossier credibility. State-Grid
  work is explicitly out of scope.
- **Kill date:** 2034-12-31; [FIX applied: per-market 2029 downgrade gates — no US frame
  agreement by end-2029 → US folds to niche lab tooling; no CN integrator frame agreement by
  end-2029 → CN downgrades to license-only (honest flag change, F-06 precedent)]; interim: no
  US commissioning design-in AND no CN integrator frame agreement by end-2031 → kill;
  OCP-standardized acceptance suite implemented by entrenched instrument majors before 2031 →
  fold to niche lab tooling / license the sequence library.
- **Vision:** the acceptance-and-evidence layer for all DC electrification — datacenter halls,
  1500VDC (L02-044), DC industrial parks, megawatt EV charging, shipboard/microgrid DC.
- **Nearest substitutes:** vendor self-certification (status quo); general-purpose scopes +
  meggers + ad-hoc scripts; certification-institute service engagements.
- **Key uncertainty:** willingness to pay for third-party acceptance versus accepting
  integrator self-certification — the same merchant-vs-internal question every measurement
  seed carries, here sharpened by multi-architecture heterogeneity.
- Sources — demand: L02-043, L02-044, L02-048, L02-049, L14-036; technical: L02-054, L02-046,
  L02-112, L02-036, L02-010; competitors: L02-048, L02-049, L02-050, L02-047.
- **[FIX applied 2026-07-13 R3]:** the ~12%/78% HVDC-vs-UPS penetration figure demoted to
  explicitly UNVERIFIED and not load-bearing (raw-ledger WebSearch synthesis; not in the
  verified L02-048 record) with P4 re-source required, and the 8–12-year refresh cycle labeled
  inference to be evidenced; the 2029 frame-agreement gate split per market (US → niche lab
  tooling; CN → license-only with honest flag change, F-06 precedent) in plan and kill fields;
  instrument-major (Keysight/Chroma/Hioki/Fluke) + CN certification-institute (CQC/CEPREI-class)
  competitor map made a PRE-PROMOTION BINDING P4 condition; judge's note applied — decisive
  experiment assumes loaner/partner testbed hardware. Verdict: FIX_APPLIED (N5/E7/C7/V7/T6).

---

## Wave-G self-checks

- Exactly the three judge-named directions; no SEEDS_A–D content read or reused; no surviving
  canonical duplicated — nearest survivor named per seed with the concrete difference
  (G-01 vs A-05/rejected-B-12; G-02 vs C-09/F-09; G-03 vs C-01).
- CN legs: all three cite country-specific eligible CN/zh sources (L07-045, L01-037/038,
  L05-035/036, L02-048/049/050/054, L14-036); access paths (licensed entity/JV, equipment
  behind the tender rule) stated with margin/IP risk; no generic "Asia" claims.
- Rejected/unverified records handled: L05-038, L07-007 not cited; L05-035 figures, L05-028
  backlog, and the L14-036 "100% mandate" explicitly not load-bearing.
- Datacenter cap: G-03 is the only datacenter-adjacent seed and self-declares
  retrofit-slice framing; G-01/G-02 have no datacenter dependence.
- 2030 contract complete per seed: TRL, 2026–2029 plan, decisive experiment with date+budget,
  named 2030–2034 CN trigger, 2030 competition incl. domestic substitution, window rationale,
  kill date ≤2034.

## Generic EE/CE transfer note (appended post-freeze)

All three seeds run on standard electrical/computer-engineering competencies — instrumentation
and metrology design, power-conversion and thermal-interface engineering, embedded control and
signal processing, and qualification/test-protocol development — transferable across the pool
without reference to any specific founder background.
