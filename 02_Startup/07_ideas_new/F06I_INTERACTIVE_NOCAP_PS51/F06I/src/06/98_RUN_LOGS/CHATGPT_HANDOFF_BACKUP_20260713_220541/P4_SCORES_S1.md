# P4 Gate-and-Score Scorecards — Batch S1

Adjudicator: Fable 5 (claude-fable-5), xhigh effort. Scored 2026-07-13 from frozen longlist records (`_subset_S1.json`), refreshed evidence files (`30_SCREENING/EVIDENCE/`), and atlas spot-checks. Founder fit capped at 2/100, judged only from `founder_fit_note`. US/China primary-market rule and India/Singapore exclusions enforced throughout.

**Batch result: 17 ideas — 9 ADVANCE, 8 ELIMINATED. Scored mean 62.6, range 51.0–74.0. 32 pass_marginal gate verdicts.**

| # | Idea | Verdict | Score |
|---|---|---|---|
| 1 | P3R2-A-02 MVDC hybrid SSCB | ADVANCE | 55.2 |
| 2 | P3R2-A-03 PRC-029 grid emulator | ELIMINATED (G1) | — |
| 3 | P3R2-A-05 US merchant NEG coating | ADVANCE | 66.8 |
| 4 | P3R2-A-10 IEDF metrology + waveform bias | ADVANCE | 62.0 |
| 5 | P3R2-A-11 Sub-100ms fast MFC | ELIMINATED (G1, G7) | — |
| 6 | P3R2-A-13 Rad-tolerant GaN PPUs | ADVANCE | 57.2 |
| 7 | P3R2-A-14 300C mixed-signal platform | ADVANCE | 74.0 |
| 8 | P3R2-A-16 Chiplet-era metal TIM | ELIMINATED (G1, G7) | — |
| 9 | P3R2-A-21 Multi-MW harsh-duty charging | ADVANCE | 51.0 |
| 10 | P3R2-A-22 Plasma PFAS destruction | ADVANCE | 61.0 |
| 11 | P3R2-B-01 Negative-pressure two-phase cooling (CN) | ADVANCE | 64.6 |
| 12 | P3R2-B-06 ESC power/control electronics (CN) | ELIMINATED (G1) | — |
| 13 | P3R2-B-14 Dual-standard MW charging converter | ELIMINATED (G1, G7) | — |
| 14 | P3R2-B-22 DC-link capacitor prognostics | ELIMINATED (G1) | — |
| 15 | P3R2-C-01 800VDC rack power-path protection | ADVANCE | 72.0 |
| 16 | P3R2-C-02 Rack pulsed-load energy buffer | ELIMINATED (G7) | — |
| 17 | P3R2-C-03 MV SST power block | ELIMINATED (G4, G7) | — |

---

## P3R2-A-02 — Modular MVDC (1–35kV) hybrid solid-state circuit breaker

| Gate | Verdict | Rationale (short) |
|---|---|---|
| G1 | pass_marginal | Primary filings evidence the DC-buildout wave (L08-033, L08-041, L02-034) but no buyer names an MVDC breaker as a line item; category demand one step removed. |
| G2 | pass | Accepted peer-reviewed SSCB literature (L08-001/003/004/017) + national-lab lineage (L08-051). |
| G3 | pass_marginal | Bounded 2028 experiment, explicit budget — but $1.5M and national-lab access needed. |
| G4 | pass | Hitachi (L08-052), Siemens/GE, plus DG Matrix/Atom Power (P3R2-A-02-S01/S02); non-cosmetic but narrowing. |
| G5 | pass | Demonstrated interruption physics; staged capital; multiple triggers. |
| G6 | pass_marginal | No MVDC-SSCB certification standard exists — entrant must drive standards; export benign. |
| G7 | pass | Southern Spirit 2029/2032 (L08-041, primary in-window) + 800VDC phasing (P3R2-A-02-S04); window 2029→2034. |

**Physics/build:** Hybrid SSCB physics (UFD + SiC branch + MOV) demonstrated at HVDC demonstrator scale and research scale; nothing at 1–35kV/1–4kA violates physics, but series sharing, di/dt control with no current zero, restrike-free actuation, and MOV dosage over ≥100 ops are open engineering — TRL 3 honest. 2026–29 path sound and publishable; the $1.5M 2028 national-lab experiment is at the outer edge of pre-company feasibility. Hidden showstopper: no MVDC breaker certification standard. Founder owns relaying/trigger electronics; UFD mechanics and kA test campaigns need hires.

| Criterion | Raw | Wt | Evidence |
|---|---|---|---|
| demonstrated_demand | 3 | 9.6 | L08-033; L08-041; L02-034 |
| frontier_coolness_vision | 4 | 12.0 | L08-001; L08-017 |
| high_end_niche_quality | 3 | 6.0 | L08-041; P3R2-A-02-S04 |
| competition_whitespace | 2 | 3.6 | P3R2-A-02-S01/S02; L08-052 |
| reachable_validation_budget | 1 | 1.8 | $1.5M experiment; v1 $10–25M |
| technical_elegance_controllability | 3 | 6.6 | L08-051; L08-017 |
| tenx_technical_edge | 3 | 4.2 | L08-001/003/004 |
| us_china_dual_market_leverage | 2 | 4.0 | US-only; L08-034 |
| launch_window_fit_2030 | 3 | 4.8 | L08-041; P3R2-A-02-S04 |
| expansion_economics | 3 | 1.8 | L08-041 |
| founder_skill_transfer | 2 | 0.8 | founder_fit_note |

**VERDICT: ADVANCE score=55.2 range=[46,63] confidence=medium.** Red-team: breaker-avoiding architectures; SST vendors extending into protection; $1.5M pre-company ask; unlisted-hardware sales assumption.

---

## P3R2-A-03 — Containerized MW grid emulator for NERC PRC-029-1

| Gate | Verdict | Rationale (short) |
|---|---|---|
| G1 | **fail** | Own binding gate kill condition met: Texas RE written guidance (P3R2-A-03-S01) + two corroborations show model-based EMT compliance validated by passive PRC-028-1 recorders (SEL); no buyer for field MW injection. |
| G2 | pass | Accepted atlas technical base. |
| G3 | pass | $600k bounded prototype plan was well-formed. |
| G4 | pass_marginal | SEL and ActionPower found — "no product category" premise wrong. |
| G5 | pass_marginal | Thesis rested on a single market premise now contradicted by primary evidence. |
| G6 | pass | No export/cert issue. |
| G7 | **fail** | Regulatory window opens onto modeling/monitoring spend, not this product. |

**Physics/build:** Back-to-back MW converter playback is mature engineering (TRL 5 honest; ActionPower parallels to 10MVA); build path executable. Fails on product-market fact, not physics.

**VERDICT: ELIMINATED — G1 fail on the seed's own pre-declared gate terms; compliance money flows to EMT consulting and SEL passive recorders. Fold test-sequencing/reporting IP into P3R2-E-14 per pre-agreed path.** Confidence high.

---

## P3R2-A-05 — US merchant NEG-coating / low-outgassing line for UHV/XHV

| Gate | Verdict | Rationale (short) |
|---|---|---|
| G1 | pass | EIC CD-3B ~$67M (P3R2-A-05-S01), PIP-II (S02), DOE QIS $625M (L13-028), ITER tenders (L07-041/042/043). |
| G2 | pass | CERN-lineage peer-reviewed base (L07-001/008/009). |
| G3 | pass | $250k bounded 2027 experiment, independent-lab endpoint — cleanest in batch. |
| G4 | pass | SAES sole merchant incumbent confirmed by fresh negative search (L07-037); US second source non-cosmetic. |
| G5 | pass | Mature physics, small capital, multiply-sourced demand. |
| G6 | pass | No export flags; BABA tailwind honestly caveated. |
| G7 | pass | EIC CD-3B (2030 operations, primary in-window) + PIP-II 2028 + QIS. |

**Physics/build:** TiZrV NEG coating is 20+-year-mature CERN/SAES art; replication is process engineering — TRL 5 honest, $250k first experiment realistic on a university rig. Risk is craft (uniformity in long pipes, activation reproducibility, QA), exactly what the experiment tests. v1 $2–6M credible; service burden low. Kill risks commercial: SAES US capacity add; lumpy accelerator procurement.

| Criterion | Raw | Wt | Evidence |
|---|---|---|---|
| demonstrated_demand | 4 | 12.8 | P3R2-A-05-S01/S02; L13-028; L07-041/042/043 |
| frontier_coolness_vision | 2 | 6.0 | modest vision ceiling (adjudication) |
| high_end_niche_quality | 4 | 8.0 | L07-037; P3R2-A-05-S01 |
| competition_whitespace | 4 | 7.2 | L07-037 + negative search |
| reachable_validation_budget | 4 | 7.2 | $250k; v1 $2–6M |
| technical_elegance_controllability | 4 | 8.8 | L07-001 |
| tenx_technical_edge | 3 | 4.2 | L07-001 (edge is supply, not performance) |
| us_china_dual_market_leverage | 2 | 4.0 | US-only by design |
| launch_window_fit_2030 | 4 | 6.4 | P3R2-A-05-S01/S02 |
| expansion_economics | 3 | 1.8 | L13-028 |
| founder_skill_transfer | 1 | 0.4 | founder_fit_note: low direct fit |

**VERDICT: ADVANCE score=66.8 range=[59,73] confidence=medium.** Red-team: SAES response speed; gap-year revenue; unquantified pricing/TAM; DOE procurement-preference reality.

---

## P3R2-A-10 — Vendor-neutral IEDF metrology + tailored-waveform bias control

| Gate | Verdict | Rationale (short) |
|---|---|---|
| G1 | pass_marginal | US leg passes (L06-039, L06-037); CN leg demand real but undeliverable — NAURA/Piotech Entity-Listed, AMEC VEU-removed (P3R2-A-10-S01/S02). Scored US-primary. |
| G2 | pass | Accepted TVW/diagnostics literature (L06-009/010/011/027). |
| G3 | pass | $450k bounded closed-loop demo; stageable. |
| G4 | pass | Impedans identified as direct vendor-neutral incumbent (P3R2-A-10-S04); closed-loop control non-cosmetic. |
| G5 | pass | Measurement physics proven; modest capital. |
| G6 | pass_marginal | 2027 counsel gate acknowledged, but named CN route very likely blocked; passes only with CN leg struck from base case. |
| G7 | pass | GAO CHIPS 0%→20% by 2030 (T1) + AE platform ramp (L06-039). |

**Physics/build:** RFEAs measure IEDFs commercially today; the hard/novel part is RF-immune in-situ estimation plus closing a waveform loop to ±2eV under drift — aggressive but bounded and genuinely tested by the $450k university-reactor program; TRL 4 fair. Founder fit strong. Showstoppers: OEM interface lock-out, FTO in the B-21 layer, CN export wall.

| Criterion | Raw | Wt | Evidence |
|---|---|---|---|
| demonstrated_demand | 3 | 9.6 | L06-039; L06-037 |
| frontier_coolness_vision | 4 | 12.0 | L06-009; L06-027 |
| high_end_niche_quality | 3 | 6.0 | L06-039 |
| competition_whitespace | 3 | 5.4 | P3R2-A-10-S04; L06-039/049 |
| reachable_validation_budget | 3 | 5.4 | $450k; v1 $4–9M |
| technical_elegance_controllability | 4 | 8.8 | L06-010; L06-011 |
| tenx_technical_edge | 3 | 4.2 | L06-027 |
| us_china_dual_market_leverage | 1 | 2.0 | P3R2-A-10-S01/S02 (CN struck) |
| launch_window_fit_2030 | 3 | 4.8 | L06-037; L06-039 |
| expansion_economics | 3 | 1.8 | L06-018 |
| founder_skill_transfer | 5 | 2.0 | founder_fit_note |

**VERDICT: ADVANCE score=62.0 range=[54,68] confidence=medium.** Red-team: ±2eV closed-loop claim under drift; retrofit channel viability; generator-vendor good-enough inference by 2030; whether china_beachhead should be formally reset to false.

---

## P3R2-A-11 — Sub-100ms no-overshoot fast MFC for ALD/ALE

| Gate | Verdict | Rationale (short) |
|---|---|---|
| G1 | **fail** | No primary buyer/procurement source: SEMI E17 is 2018 vocabulary; Edwards CHIPS award is vacuum pumps; no integrator/OEM LOI or dual-sourcing signal found. |
| G2 | pass_marginal | Only two technical sources; FIX-required broadening not delivered. |
| G3 | pass | $300k bounded bench demo, independent metrology. |
| G4 | pass_marginal | MKS CMA10B already ships the envelope outside the semi line (P3R2-A-11-S01) — gap one qualification cycle wide. |
| G5 | pass | No physics/capital issue. |
| G6 | pass | No barriers. |
| G7 | **fail** | Evidence's own verdict: timing bar "only partially met"; no dated in-window MFC-specific trigger; hoped-for E17 revision uncorroborated. |

**Physics/build:** Pressure-based sensing + MPC valve control to sub-100ms is credible (MKS proves it); TRL 4 honest, experiment executable. Fails on demand and window: concentrated gatekeeper buyer (Ichor: Lam+AMAT = 76% of sales, L07-049), $/tool/year value model spans $15k–$1.4M — not decision-grade.

**VERDICT: ELIMINATED — G1 fail (no primary buyer demand evidence) and G7 fail (no in-window trigger); incumbent catch-up risk acute. Re-batch only if a paid OEM/integrator evaluation or SEMI E17 revision proposal appears.** Confidence medium.

---

## P3R2-A-13 — Modular rad-tolerant GaN PPUs (2–20kW)

| Gate | Verdict | Rationale (short) |
|---|---|---|
| G1 | pass | SDA T3TLu draft solicitation (P3R2-A-13-S01) + industry supply-crunch corroboration (S05) + York/Orbion realized deliveries (S04). SDA-EP condition closed, with complication. |
| G2 | pass | Accepted radiation-effects/PPU literature (L09-103/104 etc.). |
| G3 | pass | $700k heavy-ion + breadboard; SEE maps stageable <$250k. |
| G4 | pass_marginal | Landscape worsened: recapitalized Rocketdyne (S03), York/Orbion integration, Rocket Lab ITAR-free (L09-114). |
| G5 | pass | SEE mitigation is derating/topology work, not new physics. |
| G6 | pass | ITAR/EAR overhead acknowledged (S06); US base case. |
| G7 | pass_marginal | Primary in-window trigger (SDA T3) currently zeroed/paused (S02); window persistence at needed scale genuinely uncertain. |

**Physics/build:** Converter design conventional; frontier claim is destructive-SEE-free GaN switching at full bus voltage at mission LET — a known killer, correctly attacked SEE-map-first (L09-103/104 methods), university-executable; TRL 4 honest. Showstoppers: derating eroding the mass/cost halving; qual-file acceptance without flight heritage; prime vertical integration already materializing.

| Criterion | Raw | Wt | Evidence |
|---|---|---|---|
| demonstrated_demand | 3 | 9.6 | P3R2-A-13-S01/S05/S04 |
| frontier_coolness_vision | 4 | 12.0 | L09-103; L09-104 |
| high_end_niche_quality | 3 | 6.0 | P3R2-A-13-S05 |
| competition_whitespace | 2 | 3.6 | P3R2-A-13-S03/S04; L09-114 |
| reachable_validation_budget | 2 | 3.6 | $700k; v1 $6–15M |
| technical_elegance_controllability | 4 | 8.8 | L09-014; L09-108 |
| tenx_technical_edge | 3 | 4.2 | L09-020 |
| us_china_dual_market_leverage | 1 | 2.0 | US-only; P3R2-A-13-S07 |
| launch_window_fit_2030 | 3 | 4.8 | P3R2-A-13-S01/S02 |
| expansion_economics | 3 | 1.8 | L09-037 |
| founder_skill_transfer | 2 | 0.8 | founder_fit_note |

**VERDICT: ADVANCE score=57.2 range=[48,64] confidence=medium.** Red-team: who buys merchant PPUs in 2030 after prime integration; SEE-derated mass/cost math; T3 funding status 2027; qual acceptance without flight heritage.

---

## P3R2-A-14 — 300C mixed-signal instrumentation platform (SiC/SOI)

| Gate | Verdict | Rationale (short) |
|---|---|---|
| G1 | pass | Baker Hughes/XGS 150MW EGS, 2030 operations (P3R2-A-14-S01); ARPA-E SUPERHOT (S02/S03); SLB-Ormat (S06/L15-041); CISSOID exit realized (S04). Strongest in batch. |
| G2 | pass | Accepted peer-reviewed/government base (L15-001/004/005/009/025/030/031). |
| G3 | pass | $850k bounded 1,000h/300C soak; stageable packaging studies first. |
| G4 | pass | TI/CISSOID/Honeywell/in-house/Ozark/DARPA performers named; merchant 300C platform gap non-cosmetic. |
| G5 | pass | Operating point research-proven; staged capital. |
| G6 | pass | No export regime; industrial qualification. |
| G7 | pass | BH/XGS 2030 target + SUPERHOT/THERMAL timelines; supply gap already realized. Strongest timing case. |

**Physics/build:** 300C mixed-signal SiC/SOI physics-proven (NASA Glenn 500C JFET-R ICs, L15-009/030); honest bottleneck is packaging/die-attach at 300C over 1,000h, which the seed correctly leads with. TRL 4 fair; pre-company path executable via university runs + autoclave tests. Hidden showstoppers: HT foundry supply fragility (the X-FAB exit that killed CISSOID applies to a startup too), mixed-signal yield at temperature, in-house capture by service majors.

| Criterion | Raw | Wt | Evidence |
|---|---|---|---|
| demonstrated_demand | 4 | 12.8 | P3R2-A-14-S01/S02/S06; L15-040 |
| frontier_coolness_vision | 4 | 12.0 | L15-009; L15-026 |
| high_end_niche_quality | 4 | 8.0 | P3R2-A-14-S04; L15-029 |
| competition_whitespace | 4 | 7.2 | P3R2-A-14-S04; L15-031 |
| reachable_validation_budget | 2 | 3.6 | $850k; v1 $8–18M |
| technical_elegance_controllability | 4 | 8.8 | L15-001; L15-009 |
| tenx_technical_edge | 4 | 5.6 | L15-004; P3R2-A-14-S04 |
| us_china_dual_market_leverage | 2 | 4.0 | US strong; CN absence confirmed |
| launch_window_fit_2030 | 5 | 8.0 | P3R2-A-14-S01/S02/S05 |
| expansion_economics | 4 | 2.4 | L15-011; L15-026; L15-030 |
| founder_skill_transfer | 4 | 1.6 | founder_fit_note |

**VERDICT: ADVANCE score=74.0 range=[68,79] confidence=high. Batch leader.** Red-team: HT foundry second source; in-house capture by SLB/Halliburton/BH; DARPA-performer leapfrog; wells-per-year extrapolation.

---

## P3R2-A-16 — Chiplet-era liquid-metal/sintered TIM system

| Gate | Verdict | Rationale (short) |
|---|---|---|
| G1 | **fail** | No primary buyer/procurement source; demand inferred from TDP roadmap + 2023 COOLERCHIPS R&D. Analyst: "FAIL on strict criterion." |
| G2 | pass | Accepted atlas base (L14-014/015/016/018). |
| G3 | pass | $400k head-to-head kill-gate campaign well-designed. |
| G4 | pass_marginal | Chinese standards-backed liquid-metal TIM industry (GB/T 43611-2023, S05) adds contest. |
| G5 | pass_marginal | Unaddressed gallium single-point dependence (98% China supply). |
| G6 | pass_marginal | Gallium export truce expires 2026-11-27 (S03/S04) — material, surfaced only by evidence pass. |
| G7 | **fail** | No primary 2028–2035 demand trigger; substitution risk from direct-liquid architectures; persistence "genuinely uncertain." |

**Physics/build:** Reliability-engineering thesis legitimate (pump-out, intermetallics under cycling); TRL 3 honest; experiment executable. Fails upstream of physics: no buyer evidence possible today, gallium chokepoint unaddressed, architecture substitution live.

**VERDICT: ELIMINATED — G1 fail (no primary buyer/procurement evidence) and G7 fail (no primary in-window demand trigger); gallium chokepoint and direct-liquid substitution compound. Revival requires a packager LOI plus a non-gallium/stockpile strategy.** Confidence medium.

---

## P3R2-A-21 — Ruggedized multi-MW charging (MCS/IEC TS 63379) for ports/rail/mines

| Gate | Verdict | Rationale (short) |
|---|---|---|
| G1 | pass | EPA Clean Ports $2.94B/53 grants (P3R2-A-21-S01, primary) + E&E corroboration (S03) + UP FLXdrive order (S07). Rail leg pilot-scale. |
| G2 | pass | Accepted technical base (L10-050; L14-019/020/021/022). |
| G3 | pass_marginal | $1.2M and MW test yard stretch pre-company feasibility. |
| G4 | pass | EVSE majors, Wabtec/Cat bundles, Fortescue in-house (S05) named. |
| G5 | pass | Envelope proven by Fortescue; obligated funds. |
| G6 | pass | IEC TS 63379 published Feb 2026 (S04); UL/NEC standard practice. |
| G7 | pass_marginal | Grant wave deploys largely before 2030; funding survived one cancellation attempt and stays politically exposed; post-grant scale wave uncontracted. |

**Physics/build:** No new physics — SiC stacks, liquid-cooled 3,000A dispensing, sequencing software; Fortescue's 6MW charger proves the envelope; TRL 5 honest. Integration-and-deployment business with high field-service burden. Showstoppers commercial: OEM bundles, in-house builds at the biggest buyers, political funding reversal.

| Criterion | Raw | Wt | Evidence |
|---|---|---|---|
| demonstrated_demand | 4 | 12.8 | P3R2-A-21-S01/S07; L10-048 |
| frontier_coolness_vision | 2 | 6.0 | integration play (adjudication) |
| high_end_niche_quality | 3 | 6.0 | P3R2-A-21-S01 |
| competition_whitespace | 2 | 3.6 | P3R2-A-21-S05; L10-051/053 |
| reachable_validation_budget | 1 | 1.8 | $1.2M; v1 $8–20M |
| technical_elegance_controllability | 3 | 6.6 | L10-050; L14-019 |
| tenx_technical_edge | 2 | 2.8 | P3R2-A-21-S05 |
| us_china_dual_market_leverage | 2 | 4.0 | US real; CN demand-without-access (S06) |
| launch_window_fit_2030 | 3 | 4.8 | P3R2-A-21-S02 |
| expansion_economics | 3 | 1.8 | L10-040/045 |
| founder_skill_transfer | 2 | 0.8 | founder_fit_note |

**VERDICT: ADVANCE score=51.0 range=[43,58] confidence=medium. Lowest advancing score — strong demand, weak differentiation.** Red-team: merchant-vs-bundle thesis; EPA reversal scenario; rail fleet expansion reality; working-capital cycle.

---

## P3R2-A-22 — Modular plasma destruction for concentrated PFAS streams

| Gate | Verdict | Rationale (short) |
|---|---|---|
| G1 | pass | GAO/NDAA AFFF mandate, >$2.1B, Oct 2026 final deadline (P3R2-A-22-S01) + PyroGenesis $2.25M/300t paid precedent (S02/L01-036). Utility leg delayed by EPA (S03). |
| G2 | pass | Accepted plasma-chemistry base (L01-101/105/112). |
| G3 | pass | $550k bounded skid demo, independent analytical verification. |
| G4 | pass | 374Water materially ahead commercially (S04); PyroGenesis, Aquagga/GA named. |
| G5 | pass_marginal | Economic premise (≤50 kWh/kg competitive with SCWO) is exactly what is unproven. |
| G6 | pass_marginal | Plasma absent from EPA's recognized large-scale destruction technologies (S05); guidance non-binding but the regulator-grade pitch depends on acceptance that doesn't yet exist. |
| G7 | pass_marginal | DoD trigger is a 2026 deadline with an inferential 2030–34 procurement pipeline; EPA delays the utility leg to 2031+. |

**Physics/build:** Plasma PFAS destruction demonstrated at paid scale; nonthermal/hybrid at ≤50 kWh/kg with >99.99% DRE and closed F mass balance is plausible per L01 literature but unproven at concentrate scale — honestly staged as the 2027–28 experiment. TRL 4 fair. Showstoppers: energy economics vs SCWO, HF/corrosion handling, regulatory acceptance.

| Criterion | Raw | Wt | Evidence |
|---|---|---|---|
| demonstrated_demand | 4 | 12.8 | P3R2-A-22-S01/S02; L01-036 |
| frontier_coolness_vision | 4 | 12.0 | L01-101; L01-105 |
| high_end_niche_quality | 3 | 6.0 | P3R2-A-22-S01 |
| competition_whitespace | 2 | 3.6 | P3R2-A-22-S04; L01-034/035 |
| reachable_validation_budget | 3 | 5.4 | $550k; v1 $5–12M |
| technical_elegance_controllability | 3 | 6.6 | L01-112 |
| tenx_technical_edge | 2 | 2.8 | no demonstrated OOM edge vs SCWO |
| us_china_dual_market_leverage | 2 | 4.0 | US-only, CN absence confirmed |
| launch_window_fit_2030 | 3 | 4.8 | P3R2-A-22-S01/S03 |
| expansion_economics | 3 | 1.8 | L01-101 |
| founder_skill_transfer | 3 | 1.2 | founder_fit_note |

**VERDICT: ADVANCE score=61.0 range=[53,67] confidence=medium.** Red-team: kWh/kg economics vs SCWO; EPA technology-list exclusion through 2030; on-site vs ship-to-incumbent procurement; 374Water's compounding install base.

---

## P3R2-B-01 — Sealed negative-pressure two-phase cold-plate loop (CN primary)

| Gate | Verdict | Rationale (short) |
|---|---|---|
| G1 | pass_marginal | Category demand proven (NDRC 970-hao caps, P3R2-B-01-S01; Southern Power Grid liquid-cooling tender, S03); mechanism-specific demand inferential — no buyer names the architecture. |
| G2 | pass | Accepted two-phase literature; ITRI locator limitation flagged. |
| G3 | pass | $250k side-by-side bench with quantitative criteria. |
| G4 | pass | Envicool, Sugon (two-phase immersion shipping, S05), ITRI named; no domestic negative-pressure cold-plate rival found. |
| G5 | pass | Operating point externally validated (ITRI 2.4kW/chip, L14-053). |
| G6 | pass_marginal | Foreign founder cannot sell direct; licensing/ODM/JV is the only route — legal, honestly planned, execution outside founder control. |
| G7 | pass | NDRC 2030 horizon + SAMR GB 40879 revision — two independent primary official in-window sources. |

**Physics/build:** Vacuum-setpoint saturation control and inward-leak fail-safety are genuine mechanisms; TRL 4 fair. Hard engineering: water's huge specific vapor volume subatmospheric (manifold/condenser sizing), noncondensable management, blind-mate vacuum integrity — all testable on the staged path. Showstoppers: single-phase stretching past 2kW/chip, hyperscaler conservatism, licensing-model IP exposure.

| Criterion | Raw | Wt | Evidence |
|---|---|---|---|
| demonstrated_demand | 3 | 9.6 | P3R2-B-01-S01/S03 |
| frontier_coolness_vision | 4 | 12.0 | L14-053; L14-001 |
| high_end_niche_quality | 3 | 6.0 | L14-035; L14-010 |
| competition_whitespace | 3 | 5.4 | P3R2-B-01-S05; L14-043 |
| reachable_validation_budget | 4 | 7.2 | $250k; v1 $3–8M |
| technical_elegance_controllability | 4 | 8.8 | L14-053 |
| tenx_technical_edge | 3 | 4.2 | L14-001/002 |
| us_china_dual_market_leverage | 2 | 4.0 | CN-only; P3R2-B-01-S01 |
| launch_window_fit_2030 | 3 | 4.8 | P3R2-B-01-S01/S02 |
| expansion_economics | 3 | 1.8 | L14-010 |
| founder_skill_transfer | 2 | 0.8 | founder_fit_note |

**VERDICT: ADVANCE score=64.6 range=[55,71] confidence=medium.** Red-team: single-phase carrying 2.5–3kW chips past 2034; licensing-model IP leakage (the B-12 kill logic); noncondensable management at rack scale; domestic negative-pressure product before 2029.

---

## P3R2-B-06 — ESC power/control electronics for Chinese tool OEMs

| Gate | Verdict | Rationale (short) |
|---|---|---|
| G1 | **fail** | Binding condition unmet: no named ESC tender or ceramics LOI; Jiangfeng-KSTE full-stack transfer (P3R2-B-06-S01) and China Ceramics in-house intent (S02) point away from a merchant electronics socket. |
| G2 | pass | Accepted base (L06-004/005/006/007/014/015). |
| G3 | pass | $220k well-formed experiment. |
| G4 | pass_marginal | AE Trek 646 is already a merchant clamp supply (S03) — category exists; differentiation rests on unproven JR observer. |
| G5 | pass | No physics/capital issue. |
| G6 | pass | Mature-node/panel scoping keeps exposure low. |
| G7 | pass_marginal | 15th FYP 2030 horizon real but no ESC-specific trigger. |

**Physics/build:** JR force-observer + safe-declamp is credible, cheap-to-validate instrumentation with strong founder fit; fails on demand structure — domestic players acquire full stacks, and the merchant product already exists (Trek 646).

**VERDICT: ELIMINATED — G1 fail on the seed's own binding condition; counter-evidence narrows the socket. Do not promote without a named design-win from a ceramics maker lacking a full-stack partner.** Confidence medium.

---

## P3R2-B-14 — Dual-standard MW charging/swap interface converter

| Gate | Verdict | Rationale (short) |
|---|---|---|
| G1 | **fail** | Binding condition checked on both named channels and absent: Fortescue built its own 6MW charger (P3R2-B-14-S02); SPIC Oyu Tolgoi is a closed trial through 2026 (S03). |
| G2 | pass | Accepted standards/technical base. |
| G3 | pass | $500k dual-conformance experiment well-formed. |
| G4 | pass_marginal | The "neutral niche" itself has not formed — both ecosystems internalize the interface. |
| G5 | pass_marginal | Entire thesis is one contingent premise (standards-arbitrage option) not observed. |
| G6 | pass | IEC TS 63379 published; no export constraint. |
| G7 | **fail** | Window has not opened and 2026 evidence points toward it closing (vertical integration). |

**Physics/build:** Conventional MW DC-DC with protocol personalities — nothing physical blocks it; the buyer does not exist in evidence.

**VERDICT: ELIMINATED — G1/G7 fail; contingent demand never materialized. Execute pre-agreed fold-in: dual-personality converter becomes P3R2-A-21's interface module.** Confidence high.

---

## P3R2-B-22 — DC-link capacitor/converter health prognostics module

| Gate | Verdict | Rationale (short) |
|---|---|---|
| G1 | **fail** | Binding condition unmet: no PSU/UPS-vendor or maintenance-operator LOI; incumbents (Zhongheng/Kehua/Delta) already bundle predictive-maintenance telemetry (P3R2-B-22-S01 context). |
| G2 | pass | L02-010 canonical reliability physics. |
| G3 | pass | $150k experiment — best budget-to-decisiveness in batch. |
| G4 | pass_marginal | No dedicated rival, but vendor in-house telemetry is the structural default. |
| G5 | pass | Sound fleet-aging logic. |
| G6 | pass | No barriers. |
| G7 | pass_marginal | Gradual fleet-aging window; no discrete named trigger. |

**Physics/build:** Excitation-free ripple-demodulation ESR tracking is elegant, cheap, founder-fit instrumentation; value accrues to converter owners — feature, not product, exactly as the seed's FIX feared.

**VERDICT: ELIMINATED — G1 fail on the seed's own binding condition; per its own fallback framing this is licensable IP, not a standalone company.** Confidence medium.

---

## P3R2-C-01 — 800VDC rack power-path protection unit

| Gate | Verdict | Rationale (short) |
|---|---|---|
| G1 | pass | Best in batch: NVIDIA names the exact gap (L02-043); OCP Diablo 400 defines the interface (L02-044); CN OAII forum co-chaired by Baidu/ByteDance names protection/certification gaps (P3R2-C-01-S03); L02-048 conversion runway. |
| G2 | pass | Accepted SSCB/arc-detection base (L08-001/003/004/017/018–021). |
| G3 | pass | $350k Q2-2027 brassboard, quantitative criteria, founder-scale. |
| G4 | pass | Vertiv/Eaton/ABB Infinitus/LS Electric/DG Matrix/Amperesand/Huawei/Delta named; merchant embeddable layer non-cosmetic; absorption risk proven concrete (DG Matrix in MGX). |
| G5 | pass | Established physics; two evidenced legs. |
| G6 | pass | EAR99-framed electronics; CN gallium regime a documented licensing gate (MOFCOM primary, S02); dual-entity plan workable. |
| G7 | pass_marginal | NVIDIA multi-generation roadmap (S06) + 15th FYP 2030; but window opens 2027 — three years before launch — while funded competitors certify now; flips on OCP/NVIDIA spec absorption by 2028–29. |

**Physics/build:** <100µs 800V/500A hybrid interruption is inside demonstrated art; hard parts (arc discrimination vs 1MW-rack transients, 10,000-cycle hot-swap, integrated precharge/IMD/sequencing) are bounded, bench-testable at founder-prototypable scale — best build-path fit in the batch; TRL 4 honest. Showstoppers competitive: spec absorption, certified incumbent breakers, hyperscaler integration.

| Criterion | Raw | Wt | Evidence |
|---|---|---|---|
| demonstrated_demand | 4 | 12.8 | L02-043; L02-044; P3R2-C-01-S03; L02-048 |
| frontier_coolness_vision | 4 | 12.0 | L08-017; L08-018 |
| high_end_niche_quality | 4 | 8.0 | L02-044; P3R2-C-01-S03 |
| competition_whitespace | 2 | 3.6 | P3R2-C-01-S04 |
| reachable_validation_budget | 3 | 5.4 | $350k; v1 $8–20M |
| technical_elegance_controllability | 4 | 8.8 | L08-018/019/020/021 |
| tenx_technical_edge | 3 | 4.2 | L08-017 |
| us_china_dual_market_leverage | 4 | 8.0 | L02-043/044; P3R2-C-01-S03; L02-048 |
| launch_window_fit_2030 | 3 | 4.8 | P3R2-C-01-S06 |
| expansion_economics | 4 | 2.4 | L02-043; L08-033 |
| founder_skill_transfer | 5 | 2.0 | founder_fit_note |

**VERDICT: ADVANCE score=72.0 range=[63,79] confidence=medium. Batch runner-up; widest score range — outcome hinges on 2027–28 OCP spec revisions.** Red-team: spec-absorption scenario modeling; the 2030-lateness problem vs 2026–27 certified incumbents; nuisance-trip discrimination at real transients; CN route vs Huawei in-house.

---

## P3R2-C-02 — Rack-level pulsed-load energy buffer (electrolytic-free 800V)

| Gate | Verdict | Rationale (short) |
|---|---|---|
| G1 | pass | Both legs evidenced (NVIDIA buffer function, P3R2-C-02-S01/L02-043; OCP L02-044; ByteDance + East-Data-West-Computing, S04; L02-048). |
| G2 | pass | Accepted base (L02-010/022/023/110). |
| G3 | pass | $300k brassboard well-formed. |
| G4 | pass_marginal | Decisive competitor is the platform spec itself — eight named majors building the NVIDIA-specced function. |
| G5 | pass | Established physics. |
| G6 | pass | Export-separable industrial module. |
| G7 | **fail** | NVIDIA already specs rack-adjacent capacitor/supercap buffering into its ecosystem (Oct 2025, S01) with ABB/Eaton/GE Vernova/Hitachi/Schneider/Siemens/Vertiv/Delta named; OCP revision cadence outpaces the end-2029 kill trigger; evidence verdict: window "may narrow or close before 2030." Commoditization before a 2030 launch is more likely than not. |

**Physics/build:** Film-bank + GaN partial-power buffering is sound, founder-fit engineering; TRL 4 honest. Fails on window: the function is becoming a specced platform feature, not a merchant category.

**VERDICT: ELIMINATED — G7 fail (launch-window commoditization/spec absorption). Execute pre-agreed fold-in: buffer/ride-through becomes an option within P3R2-C-01.** Confidence high.

---

## P3R2-C-03 — MV solid-state transformer power block (2.4MW, 10–35kV→800VDC)

| Gate | Verdict | Rationale (short) |
|---|---|---|
| G1 | pass_marginal | Category demand real (OCP SST track, S03; Heron 40GW pipeline as demand proxy; CN 800V adoption), but the hyperscaler RFI naming SST units — the seed's own required signal — was not observed. |
| G2 | pass | Accepted base (L02-001/017/021/029/030/036/107). |
| G3 | pass_marginal | Cheap dataset/standards scope is bounded, but the decisive experiment is gated behind a 2028 hard gate that cannot execute as written. |
| G4 | **fail** | Differentiation void: IEC 60076-24:2020 is published, stable to 2029, wrong device class, no SST work item found (P3R2-C-03-S04); field holds ≥4 funded entrants (Heron $178M/pilot 2027, S01; Hyperscale Power, S02; Enphase-in-OCP, S03; SolarEdge/Navitas) vs the seed's "1–2 startups." |
| G5 | pass_marginal | Certification-gap premise (atlas L02-036) unconfirmed by independent IEC-registry check. |
| G6 | pass | Export separability addressed. |
| G7 | **fail** | Window opens 2027–29 and is likely captured by funded competitors before a certification-first entrant's 2029–2031 product; the 2028 hard gate is likely to fail on both named conditions. |

**Physics/build:** MV SST physics demonstrated (decade of ARPA-E work); restricted pre-company scope admirably cheap. Thesis fails its own foundations: no standards instrument exists to be first on, and commercial entrants are not waiting for certification.

**VERDICT: ELIMINATED — G4 and G7 fail; certification-first differentiation is structurally void and the window is being captured now. Per the seed's own rule, re-batch the HF-insulation/PD dataset + standards-seat track to the wildcard pool; do not commit the $25–60M v1 plan.** Confidence high.

---

## Batch summary

- **Advance (9):** A-14 (74.0), C-01 (72.0), A-05 (66.8), B-01 (64.6), A-10 (62.0), A-22 (61.0), A-13 (57.2), A-02 (55.2), A-21 (51.0). Mean 62.6.
- **Eliminated (8):** A-03, A-11, A-16, B-06, B-14, B-22 (G1 demand-gate failures — five of them on their own binding pre-promotion conditions), C-02 (G7 spec-absorption), C-03 (G4+G7 void differentiation, window capture).
- **Pattern:** every FIX_APPLIED seed whose binding condition demanded a named buyer/LOI failed it on fresh evidence; every PROMOTE-verdict seed except none survived gates, but several (A-02, A-13) are materially weaker than their seeds assumed because competitors moved during 2025–26.
- **Pass_marginal verdicts: 32** across the batch — concentrated in G1 (category-vs-product demand), G6 (CN access/export routes), and G7 (window persistence).
- Diversity note for P5: advancing set spans L08, L07, L06, L09, L15, L10, L01, L14, L02 — 9 distinct primary lanes; two China-beachhead ideas survive (B-01 CN-primary; C-01 dual), which is thin against the final-24 China-beachhead floor and should be watched when other batches merge.
