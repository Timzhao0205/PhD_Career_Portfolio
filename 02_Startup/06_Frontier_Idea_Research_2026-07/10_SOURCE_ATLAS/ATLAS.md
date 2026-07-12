# ATLAS — P2 Fable adjudication of the 16-lane source atlas

Adjudicator: orchestrator, claude-fable-5 / xhigh (the mission's critical route; no delegation).
Date: 2026-07-12. Inputs: all 16 lane briefs (`L01`–`L16`, including T1 top-up addenda), the
canonical ledger (`90_BIBLIOGRAPHY/sources.json`, 1,125 reviewed / 860 accepted), the stratified
80-record sample (`05_STATE/P2_SAMPLE_80.json`, 5 records x 16 lanes, seeded 20260712), and the
validator output (`SOURCE VALIDATION PASS reviewed=1125 accepted=860 peer=484 demand=200 gov=141
industry=142 T1=614`). After the P2 adjudication, the user narrowed the target markets to the US,
China, Japan, and Taiwan. Under the revised market-only count, China/Japan/Taiwan coverage is
228/80 and Chinese/Japanese-language coverage is 79/40. Other-country publications remain only as
technical evidence and must not drive P3–P8 market selection.

## 1. Verdict

**The atlas contains real, dated, named-buyer demand — not merely technology enthusiasm — and it
is fit to feed P3.** Demand evidence is unevenly distributed across lanes (adjudicated per lane in
Section 3), but every lane clears its accepted-count floor, the mission-wide mix gates all pass
with margin, and, critically, the briefs consistently separate paid/contracted demand from
design-win marketing, subsidy announcements, and lab results. Several lanes' most valuable
contribution is a *negative* demand finding (L11's electrolyzer order-book contraction; L08's
grid-forming procurement losses; L10's regulatory reversals) — these are evidence, not defects,
and P3 must respect them.

No additional scout wave is required before P3 (Section 5).

## 2. Sample audit (80 records, stratified 5/lane)

- **Fetch discipline:** 80/80 sampled records carry `fetched: true` with a locator; the two
  validator-caught accepted-but-unfetched records were repaired or rejected before this
  adjudication (L12-036 re-fetched; L14-047, L15-046 rejected; L14-048 re-sourced and retyped).
- **Peer review:** every sampled academic record is `peer_review_status: verified` with a
  Crossref/publisher evidence trail; non-academic records are `not_applicable`. No preprint
  appears as accepted academic support in the sample.
- **Tier honesty:** downgrades went the right direction under pressure — the T1 top-up wave's own
  verifiers demoted press-release-sourced "filings" (Fervo financing, GE Vernova/TenneT, Rocket
  Lab 10-K via aggregator) to T2 rather than inflating T1 to pass the 70% gate. The gate passed
  at 71.4% with those demotions in place, which is the correct order of operations.
- **Borderline demand labels (noted, not blocking):** three sampled records typed `trade_press`
  carry primary demand_evidence_type labels (L16-017 procurement_award via Guangqi's exchange
  disclosures as reported; L15-042 and L08-039 buyer_specification via trade reports of named
  buyer programs). The underlying events are real and named, but P4 must not cite these as the
  *primary* document. Discounting all such borderline records leaves the primary-demand count far
  above the 120 floor (200 counted), so the gate is robust.
- **Claim discipline:** sampled `claim_supported` fields consistently quote only fetch-supported
  content, and several show explicit claim-softening after verification (e.g., L12-036's removal
  of an unconfirmed "$4B TAM"; L13-033's trimming of unfetched gyrotron counts). This matches the
  mission's rule 10/11 requirements.

## 3. Per-lane demand adjudication

Scale: **STRONG** = multiple independent, dated, named-buyer paid/contracted signals;
**MODERATE** = real demand but concentrated, government-dominated, or trial-stage;
**WEAK** = demand mostly prospective/subsidy-narrative. "Enthusiasm zones" are sub-topics where
the literature is strong but buyers are absent — P3 may use them only with an explicit
demand-bridge argument.

| Lane | Demand | Anchor evidence | Enthusiasm zones / cautions |
|---|---|---|---|
| L01 plasma | MODERATE–STRONG | PyroGenesis $27M+$4.1M DoD torch + $2.25M PFAS delivered; ASIPP/AVIC tenders; Nitricity sold out to 2028 | Plasma gasification (documented failure graveyard); VOC abatement (no named buyer); N2/CO2 plasma chemistry pre-industrial |
| L02 power electronics | STRONG | NVIDIA 800VDC ecosystem + OCP Mount Diablo (Google/Meta/Microsoft); Navitas 8-K; Wolfspeed earnings; SAM.gov converter tender | Design-in lists ≠ booked orders (Innoscience "no substantive orders"); MV SST 10+ yrs funded, still standards-blocked |
| L03 superconducting | MODERATE | ITER/US-ITER completed procurements; DOE $415M fusion program; CFS magnet sales (Realta, WHAM); Furukawa–Tokamak Energy supply deal | "Fully commercial" HTS cables are single state-directed installations; no repeat third-party orders shown; rotating-machine HTS dormant since 2007 |
| L04 heat-to-power | STRONG | Fervo 1.75 GW Turboden order + $421M project debt; Google EGS offtake; Strathcona/Proman/SCG purchases; TerraPower BOP awards; CNNC 30 MW commercial sCO2; DOE LPO $1.76B A-CAES | sCO2 still demo-stage in the US; TPV cost claims vendor-only; single-source China retrofit TAM |
| L05 pulsed power/RF/beam | MODERATE–STRONG | Varex $845M (+25% cargo segment); Comet CHF445M; CGN Dasheng RMB340M H1 orders; Thales EUR20M ITER gyrotrons; Jema/ESS modulators; IBA SteriLab contract | IBA/L3 backlog claim trade-sourced; klystron-efficiency gap (90% sim vs 78.5% hw) is open R&D, not product |
| L06 semicon subsystems | STRONG | Advanced Energy $840M semi segment + new-platform ramp; Hengyunchang IPO (RMB1.5B) & Injet orders; AMEC +45% revenue; CHIPS $18M Edwards award; Wolfspeed/Axcelis shipment | China component localization (<12%) narrative runs ahead of reality; subfab power-quality "statistics" untraceable — excluded, keep excluded |
| L07 vacuum/ultraclean | STRONG | ITER live tenders/awards; Ebara–TSMC JDA; Ichor $947.7M (76% two customers); ULVAC ¥521B orders | Incumbent-dominated; dilution-fridge cooling power is a research frontier; 2x TAM disagreement |
| L08 DC grids/protection | STRONG | POWERGRID ~$2.9B tender; Adani→GE Vernova & Hitachi/BHEL awards; GE Vernova ~$10B HVDC backlog + $2.4B/qtr datacenter orders; State Grid RMB1.275B tender; NKT ~EUR2B; Prysmian ~EUR850M | Grid-forming lost NESO Round 2 outright — pipeline share ≠ awarded contracts; DC breakers still a "showstopper"; standards lag |
| L09 space power/EP | MODERATE | NASA $67M AEPS + $18.4M NEXT-C; Gateway PPE named chain; NASA SBIR awards ($850K/$900K); JAXA/Furukawa commercialization | Space Force $905M/$3.5B programs don't confirm EP content; China EP procurement opaque; consultancy TAMs differ 60% |
| L10 heavy electrification | MODERATE–STRONG | Fortescue 300–400 truck orders + 6 MW charger; UP/Vale Wabtec orders; EPA ~$3B Clean Ports awards; YILPORT 53 cranes; Chinese SOE tenders | Regulatory demand is fragile: CARB repeal, IMO adoption slip to ≥2028; three incompatible charging architectures; trials ≠ multi-year fleet economics |
| L11 electrochemical/H2 | WEAK–MODERATE (electrolyzers) / STRONG (niches) | NEOM >2 GW award; Sinopec/China Energy tenders; Plug $187M electrolyzer revenue; Japan CfD winners | **Core finding: Western OEM order books are shrinking while subsidies grow; Chinese capacity ~2x demand.** Real niches: rectifier quality (13–14% energy lever), battery formation/cycling equipment (decoupled from H2 cycle). Seawater/CO2 electrolysis = lab-stage |
| L12 photonics/lasers | STRONG (defense-led) | JLWS $86M/$847M ceiling awards (nLIGHT, LM Aculight); nLIGHT A&D revenue $175.3M; NNSA EYC CD-1 + $26M; DARPA AMPED/POWER; TRUMPF/IPG/Coherent filings | China industrial-laser price war: Han's high-power revenue −6.6% on +30% units; share data 2021-vintage; CPO thermal unsettled |
| L13 quantum/big-science | MODERATE–STRONG | DOE $625M QIS centers; Fermilab–Qblox QICK LOI; Keysight→AIST delivery; SEEQC–ITRI line; ITER I&C tenders | Buyer base is governments+labs; China "100% localization" claim unverified against two primary pages; pricing fully opaque |
| L14 extreme thermal | STRONG (strongest in atlas) | Vertiv $15B backlog, +50% liquid-cooling orders; Google/Meta OCP specs adopted by 7+ vendors; M&A wave (Flex/JetCool, Schneider/Motivair, Trane/LiquidStack, ZutaCore $100M C); COOLERCHIPS $40M named awards; GS Caltex named customers; ITRI 2.4 kW cold plate | China "100% liquid-cooling mandate" is NOT in the primary text — verified contradiction; GB200 TDP/flow specs inconsistent; TAMs differ ~2x; PFAS/Novec fluid supply shock is both risk and opening |
| L15 harsh-env electronics | MODERATE–STRONG | DARPA THERMAL; FORGE $49M+$44M named awards; ARPA-E SUPERHOT $30M; NASA HOTTech; Baker Hughes $2.0B New Energy orders + 300 MW ORC contract; SLB–Ormat EGS pilot; Cat/Rio Tinto autonomous fleet | 250 °C+ electronics: 20 years of programs, no converged platform; CISSOID CHT obsolete + Honeywell exit = live supply gap with existing buyers; 40% TAM disagreement |
| L16 wildcards | MODERATE (two clusters real) | Guangqi RMB516M orders (~RMB2.6B 2025 cum.); Jiaocheng/CATL/BYD ultrasonic welding; Piller flywheel for 400 MW AI datacenter; Army Ka-band metamaterial SBIR; Honda→Enedym | EHD, acoustic levitation/sonochemistry, EM launch, electro/magnetocaloric cooling: strong physics, explicitly no industrial-scale deployment — enthusiasm zones by the lane's own honest account |

## 4. Cross-lane patterns (load-bearing for P3)

1. **The AI-datacenter power/thermal supercycle is the atlas's dominant demand engine**, visible
   independently in seven lanes: 800VDC rack power (L02), datacenter electrification orders and
   MVDC protection gaps (L08), liquid/two-phase cooling (L14), CPO thermal (L12), fab
   expansion/UPW/vacuum (L06/L07), superconducting urban feeders (L03), and flywheel power
   stabilization (L16). Independent corroboration across lanes makes this the best-evidenced
   macro-trigger in the atlas — but L02/L08 correctly show booked backlog is still concentrated
   in a few vendors and geographies.
2. **Defense and government procurement is re-accelerating with real dollar figures** (JLWS
   $847M ceiling; PyroGenesis torches; SDA $3.5B; DARPA THERMAL/AMPED; Army metamaterial radar;
   Guangqi's RMB2.6B China-side mirror). Where civilian demand is trial-stage, defense demand is
   often already contracted.
3. **Dated regulatory/procurement forcing functions exist — and can reverse.** Real: EtO
   replacement backlog (L05), PFAS exit + AIM Act + EU F-gas collision (L14), FuelEU 2030/2035
   (L10), NRC Part 53 (L04). Reversed/slipped: CARB drayage
   repeal, IMO Net-Zero adjournment (L10). P3 ideas premised on regulation must state which kind
   they depend on.
4. **A recurring "lab-strong, industry-thin" failure signature** appears in at least eight
   sub-domains (plasma chemistry, plasma gasification, EHD, sonochemistry/acoustic AM, seawater
   and CO2 electrolysis, solid-state cooling, EM launch, MV SST). The atlas documents both the
   enthusiasm and the missing buyers; P3 must not select these without a specific, evidenced
   demand bridge.
5. **Subsystem whitespace repeats across lanes:** precision power delivery/rectification as an
   under-exploited efficiency lever (L11 electrolyzers/electrowinning, L01 plasma supplies, L05
   modulators); unsolved protection (DC breakers L08, arc detection L06/L08); non-converged
   control/power architectures (PPUs L09, laser drivers L12, cryo-CMOS/interconnect L13);
   packaging/TIM/die-attach (L14/L15). These are demand-adjacent engineering gaps with named
   payers — prime P3 material.
6. **Standards lag is a documented, cross-lane commercial friction** (no sCO2 PTC; no
   accelerator pulsed-power standard; IEC 61803 assumes LCC; JESD51 vs liquid cooling; ISO
   11553-2 (2007) vs handheld lasers; MCS vs Chinese swap standards) — both a risk and a wedge.
7. **Market-size figures are systematically unreliable in these industries** (40%–10x
   consultancy disagreements documented in L01, L03, L07, L09, L10, L12, L14, L15). P4 must do
   bottom-up arithmetic from contract values, filings, and unit counts; the atlas provides those
   primitives (this is why pricing opacity, documented in 10+ lanes, matters).
8. **China evidence has category-dependent transparency:** precise RMB tender disclosure in
   HVDC/mining/semicon-components vs. opacity in space-EP and high-temp electronics; localization
   narratives ahead of component-level reality (L06 <12%); one flagship claim ("100% domestic
   localization", L13) and one policy claim ("100% liquid-cooling mandate", L14) that primary
   sources do NOT support. These two verified media-vs-primary gaps are model examples of the
   claim discipline the mission requires.
9. **Supply-chain shocks are documented openings:** 3M PFAS/Novec exit (L14), CISSOID/Honeywell
   high-temp IC obsolescence (L15), REBCO tape vendor concentration (L03), e-beam sterilization
   duopoly backlog (L05), single-customer concentration at Comet (23.8%) and Ichor (76%)
   (L05/L07).

## 5. Thin-lane decision

No lane is thin by the mission's gates (min accepted 43, all mixes met; the revised target-market
scope still has China/Japan/Taiwan 228/80 and Chinese/Japanese-language 79/40). The residual
weaknesses are **geography-local, not lane-fatal**, and are
documented inside the briefs for P4 follow-up rather than warranting a pre-P3 scout wave:

- Taiwan is thin in L12/L16 (but strong in L02/L13/L14 — mission-level TW coverage exists).
- L11's weak electrolyzer demand is an evidence-based market finding to be *used*, not re-scouted.

Decision: **proceed to P3.** P4 demand-competitor analysts must close the specific flagged items
(primary filings behind aggregator-sourced figures; the L13/L14 China claims; Lockheed's JLWS
share; stale China market-share data) for any idea that relies on them.

## 6. Instructions carried into P3

- Anchor ideas in the demand clusters adjudicated STRONG/MODERATE–STRONG above; enthusiasm zones
  require an explicit bridge (named buyer + dated trigger) or must be framed as wildcards.
- Respect negative findings: no electrolyzer-stack plays priced against Chinese overcapacity; no
  grid-forming-services plays that ignore NESO's procurement outcome; no maritime plays that
  assume IMO timing; no two-phase-cooling plays without a post-Novec fluid plan.
- Founder fit is applied only after evidence-first ideas exist, capped at 5/100 per CLAUDE.md
  rule 3; lane independence per `05_STATE/ANTI_ANCHORING_PLAN.md` remains binding.
