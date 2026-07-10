# CF-6 Gate Record — "Thermal-contraction-matched NI interface"

> **Research aid — not legal advice.** Every verdict below is a drafting/analysis aid;
> a registered patent attorney's review is required before any filing, disclosure, or
> reliance. This engine does not authorize filings.

`models=GATE:fable-5` (intended). **Down-route caveat (mandatory):** the
actually-served model is NOT verifiable from inside this session — Anthropic
safeguards may transparently route some Fable-5 queries to Opus 4.8, and the metrics
hook cannot detect this. Additionally, the W3 launch log records that the frontmatter
string "fable-5" was rejected at launch and the run was relaunched with the harness
enum `model="fable"`. Before ANY filing-relevant reliance on the verdicts below,
confirm the served model against the external transcript at
`%USERPROFILE%\.claude\projects\`. A Fable self-report is not proof of which model ran.

Gate order: G-PHYS → G-NOVEL → G-CLAIM. Date: 2026-07-10.

**Prong-a / theme check (Hard Rule 1):** CF-6 is NI-coil turn-to-turn interface
thermal/mechanical/manufacturing engineering. No Hall-sensing adjacency, no HSX
plasma-diagnostics adjacency, no GaN/AlGaN, no battery magnetic imaging. Presumptively
outside the funded lane; no `BLOCKED-PENDING-COUNSEL` tag. No "stellarator" appears in
any patent-facing CF-6 text (Tokamak Energy citations are prior-art references only).

---

## G-PHYS — physics correctness: **REVISE**

Evidence reviewed: `20_SIM/cf6_contraction_matched.py`, `20_SIM/out/cf6_starter.json`,
`20_SIM/thermal_network.py` (thermal_solve, cooling_budget, KNOWN_ISSUES).

### What is sound
1. **Labeling compliance (Hard Rule 6): PASS.** The script header, `ASSUMED_PARAMETERS`
   `note` field ("illustrative exponential contact-degradation-vs-cycling
   parametrization, not a measured thermal-cycling test result"), the JSON
   `SIMULATED_prophetic: true` flag, and every print line are consistently labeled
   prophetic/illustrative. No blending with measured data. All quantities carry units.
2. **Thermal solve direction is correct.** `thermal_solve()` is a standard linear
   1-D radial conduction network; lower interface k → higher radial Rth → higher peak
   hot-spot ΔT for fixed q_spot. Signs, boundary condition (cold-head sink via G_ch at
   OD), and conservation check out. Baseline dT at k=400 (0.5603 K at 20 K) matches
   the CF-1 uniform-cu row exactly — the reuse is faithful.
3. **CF-1 KNOWN_ISSUES tau<->Rc inversion does NOT infect CF-6's headline.** CF-6
   never calls `electrical_tau()`; the headline effect flows only through
   `thermal_solve()`, whose k→dT direction is independent of the flagged (and
   W2-fixed) tau-narrative issue. Verified `rho_ct_placeholder` is genuinely unused by
   `thermal_solve()`.
4. **Qualitative direction is defensible from independent art.** CTE-mismatch-driven
   interface degradation under thermal cycling is a real, published mechanism:
   T3-6 (MIT/Iwasa-Hahn lineage conductive-epoxy NI impregnation) explicitly names
   thermal-contraction-mismatch delamination as the failure mode; T3-12 (Wear 2026)
   models fretting/contact degradation from differential thermal expansion under
   temperature cycles; US11,282,624's own data shows thermal cycling (4.2 K↔273 K)
   RAISED Rc ~4x (0.8 → ~3.1 µΩ·cm², no reset to as-built) — consistent with
   cycling-driven contact-quality loss. "Mismatched degrades faster than matched" is a
   physically reasonable qualitative hypothesis.

### Why REVISE, not PASS (three specific fixes required)
1. **The simulation provides ZERO evidence for the cryogen-free-specific hook — and
   this is the candidate's entire framing.** In this linear model,
   peak_dT_rise = (radial-network ΔdT from degraded k); the G_ch/cooling-budget term
   only shifts the baseline offset. The output proves it: peak_dT_rise_matched is
   0.09155 K and rise_mismatched 1.54888 K IDENTICALLY at all three cooling budgets
   (20/30/50 K). A bath-cooled coil with the same radial-only topology would show the
   same rise. The claimed differentiator ("cryocooler duty cycling + limited cooling
   power makes this worse than bath cooling") is asserted, not simulated. **Fix:**
   model the bath case honestly (distributed face-cooling conductance on every turn,
   not a single OD sink) vs the conduction-only case, and/or compare the dT rise
   against the temperature-dependent current-sharing margin at each cold-head budget,
   so the cryogen-free sensitivity is a computed result rather than a narrative claim.
2. **The headline "~17x" is an input, not a finding.** The 17x ratio
   (1.549/0.0915) follows directly from the ASSUMED k_floor (15 vs 150 W/m/K, a
   hand-picked 10x) and tau (400 vs 3000 cycles) — the thermal solve merely translates
   assumed k into dT. The parametrization is honestly labeled, so this is not a
   candor violation, but no quantitative claim (and in particular NO parameter-window
   claim at G-CLAIM ladder rung 5) may rest on it. **Fix:** derive k_floor/tau anchors
   from published cycling data (US11,282,624 Rc-cycling data via a
   Wiedemann-Franz-type contact analogy; T3-2/T3-3 REBCO cyclic-loading Rc curves) or
   from a first-principles contact-pressure-relaxation model, or measure on the 77 K
   rig.
3. **Monotonic-decay assumption is partially contradicted by the closest measured
   art, and the electrical half of the dual-function claim is unmodeled.**
   US11,282,624 reports that MECHANICAL pressure cycling (~1000 cycles, 2.5–25 MPa)
   DROPPED Rc to ~1/10 of initial — i.e., contact quality can IMPROVE (bedding-in)
   under some cycling modes, opposite in sign to the sim's universal monotonic
   degradation. The exponential-decay proxy is defensible for thermal-cycling-driven
   gap opening but must not be presented as a universal cycling law. Separately, CF-6
   claims the interface holds BOTH Rc and thermal contact, yet Rc(N) is a frozen
   placeholder — the electrical half of the invention has no simulation support at
   all. **Fix:** couple k(N) and rho_ct(N) through one contact-quality state variable
   (they are two responses of one contact area/pressure, exactly as CF-1's material
   table insists), and restrict degradation claims to thermal-cycling modes.

**G-PHYS verdict: REVISE.** Direction qualitatively defensible and labeling compliant;
the effect as simulated is real within the model but the model does not yet support
the candidate's differentiating claim (cryogen-free sensitivity) or any quantitative
statement. No filing-relevant reliance on the 17x number or the cycle-count constants.

---

## G-NOVEL — novelty across US + CN + JP + KR + EU: **NARROW-NOVEL (conditional)**

Ledger reviewed in full (`60_PRIOR_ART/CF-6/ledger.md`, 29 hits incl. CN/JP/KR
native-language entries), plus cross-candidate note below.

### Blocking / limiting references (named, with jurisdiction)
- **US 11,282,624 B2 (US, granted, in force; FSU/NHMFL; priority 2018-02-23) — the
  principal limiting reference.** Claims engineered resistive coatings (Cu-oxide, Cr,
  Ni, Ni-P) and stainless interlayers (Ni/Cu-plated) to control turn-to-turn Rc in
  REBCO coils, AND discloses experimental thermal-cycling (4.2–273 K) and
  mechanical-cycling (~1000 cycles, 2.5–25 MPa) Rc data. This kills any claim to the
  genus "engineered NI turn-to-turn interlayer controlling Rc, characterized under
  cycling." **Critically, per the ledger, its interlayers are selected/engineered for
  Rc value — NOT selected or specified for CTE match to the tape stack, and it
  discloses no compliant contact-pressure-maintenance element and no
  cryocooler-duty-cycle framing.** Characterizing cycling behavior generically is not
  the same as designing the interlayer against it — that delta is the surviving angle,
  and it must be verified against the granted claims' full text by counsel (the ledger
  summary is not a claim chart).
- **T3-6 NPL (Cryogenics, MIT/Iwasa-Hahn lineage, EN).** Already names
  CTE-mismatch/thermal-contraction delamination as THE NI-interface failure mode and
  discloses a design-around (partial-depth impregnation). Blocks the broad framing
  "recognize and mitigate CTE mismatch at the NI interface" as such — problem
  recognition and one mitigation are in the art.
- **T3-4 NPL (IEEE TAS #9769961, likely KR-origin group, EN).** Soldered-metal
  insulation interlayer engineered for BOTH controllable Rc and thermal conductivity,
  tested under conduction cooling below 77 K. Blocks the genus "dual-function
  (Rc + thermal) engineered interlayer under conduction cooling."
- **T3-2/T3-3 NPL (SUST aacd2d, aa5b05, EN).** Cyclic loading + surface coating
  effects on REBCO-to-REBCO Rc — the electrical-degradation-under-cycling half is
  published.
- **US 4,930,318 and US 5,701,742 (US, both likely expired).** Spring-loaded
  (Belleville) and compliant-indium-gasket cryocooler-joint contact maintenance.
  Expired ⇒ patentability art only (no FTO threat), but they anticipate the GENERIC
  "compliant/spring-loaded contact surviving cooldown at a cryocooler interface" —
  any CF-6 compliant-element claim must be turn-to-turn-of-an-NI-winding specific.
- **KR 10-1665038 B1 (KR, granted per mirror; KBSI).** Conductive-particle-impregnated
  NI coil for mechanical robustness — citable against a broad "conductive compliant
  interlayer" claim in KR.
- Tokamak Energy family US 11,101,060 B2 / EP 4078630 A1 / WO 2021/122522 /
  CN 115485868 A / (likely) JP sibling (US/EP/PCT/CN/JP): adjacent turn-to-turn
  interface engineering, different mechanisms (MIT-material, HTS bridges, BLI edge
  removal) — not anticipatory of CTE-matching, but crowd the field for obviousness.

### What is NOT found in the art (the surviving delta)
No reference in the ledger discloses a turn-to-turn NI interlayer whose
**thermal-contraction behavior is itself the engineered design variable** — i.e., an
interlayer compositionally/structurally selected so its integrated contraction
(293 K → operating T) matches the effective contraction of the REBCO tape stack, or a
per-turn compliant element that maintains interface contact pressure across cooldown —
**for the joint purpose of bounding BOTH Rc drift AND turn-to-turn thermal-conductance
drift over repeated cryocooler thermal cycles.** US11,282,624 characterizes cycling
but does not design against it via CTE; T3-6 identifies CTE mismatch but solves it by
partial-depth impregnation (a geometry fix, not a matched-material fix) and addresses
Ic retention, not Rc/thermal-drift co-control; T3-4 engineers the dual function but
not cycling life; the cryocooler-joint patents are not turn-to-turn.

### Verdict: NARROW-NOVEL — conditional on closing logged verification gaps
The genus is DUPLICATED (engineered NI interlayer; dual Rc+thermal under conduction
cooling; CTE mismatch as recognized failure mode; cycling degradation of Rc). Only the
narrow combination above survives. **Conditions before reliance:** (a) mandatory live
KIPRIS/J-PlatPat/CNIPA/Espacenet re-pass — T2-4 (JP 2017-535948), T2-5
(JP 2012-033947), T2-6 (KR KOR1020130130009, title "superconducting coil apparatus
for conduction cooling" — high risk, on-point title, unread claims) and the T4-4 CN
press lead (星环聚能) are unverified and any of them could demote this to DUPLICATED;
(b) full-text pull of T3-2/T3-3/T3-4 and the US11,282,624 granted claim set;
(c) attorney claim chart against US11,282,624.

### Patentability vs FTO (kept distinct)
- **Patentability:** the art above constrains claim breadth (adjust claims — see
  G-CLAIM); the narrow combination appears claimable, subject to the conditions.
- **FTO:** US 11,282,624 B2 is granted and in force (US). A CF-6 product whose
  interlayer also functions as a resistive Rc-control coating could read onto its
  claims even if CF-6's own patent grants. A patent granted to you ≠ freedom to
  operate. Design-around (interlayer whose Rc control is achieved by a mechanism its
  claims don't cover, e.g. purely mechanical contact-pressure maintenance) or a
  license must be assessed by counsel. Tokamak Energy's family is a lesser FTO watch
  item (different mechanisms). US4,930,318/US5,701,742 expired — no FTO risk.
- **Duty of candor:** ALL of the above, including the unverified low-confidence hits
  once verified, remain in `IDS_pool`. Nothing here is to be withheld from an IDS;
  the design-arounds proposed are engineering choices, not concealment.

### Cross-candidate flag for W5 synthesis
**US 5,260,266 A (GE)** — differential thermal-contraction management between 10 K /
50 K lead stations — overlaps CF-7 (conduction-cooled lead/termination co-qual) and
the contraction-management theme generally. Likely expired (1993-era grant) ⇒
patentability art for CF-7, not FTO. Flagged for the W5 synthesis pass and for CF-7's
IDS_pool; it does not read on CF-6's turn-to-turn core.

---

## G-CLAIM — survivability + shaping: **NARROW core survives; combination claim recommended**

### Surviving claim core (one sentence)
A conduction-cooled no-insulation HTS winding in which the turn-to-turn interlayer is
engineered — by matching its integrated thermal contraction (293 K → operating
temperature) to that of the coated-conductor stack, and/or by a per-turn compliant
element maintaining interface contact pressure across cooldown — such that both the
turn-to-turn contact resistance and the turn-to-turn thermal conductance remain within
specified bounds over a specified number of cryocooler thermal cycles.

### Design-around ladder walk
1. **Combination/system (STRONGEST — recommended independent claim).** Conduction-
   cooled NI winding + CTE-matched (or compliant pressure-maintained) turn-to-turn
   interlayer + the DUAL drift bound (Rc AND thermal conductance) over cycling. No
   single reference has all elements; obviousness fight will center on combining
   US11,282,624 (engineered interlayer + cycling data) with T3-6 (CTE-mismatch
   recognition) — rebuttal: T3-6 teaches AWAY from full-contact impregnation toward
   partial-depth geometry, not toward matched-material full contact, and neither
   reference bounds thermal-conductance drift (both are Rc/Ic-focused).
2. **Different mechanism.** Per-turn compliant/spring element (co-wound wavy-metal or
   elastic interlayer) maintaining contact pressure — distinct from all Rc-coating
   art; must be drafted turn-to-turn-specific to clear US4,930,318/US5,701,742's
   generic cryocooler-joint precedent. Also serves as the US11,282,624 FTO
   design-around (Rc set by pressure, not by a resistive coating).
3. **Enabling sub-solution.** The matching RULE: interlayer selected such that
   |∫α dT (interlayer) − ∫α dT (tape stack)| over 293 K→T_op is below a bound tied to
   the contact-pressure-relaxation threshold — claim the selection method +
   method-of-making (wind-time verification). This is the "what makes it actually
   work" layer T3-6 lacks.
4. **Architecture/topology.** Radially graded interlayer (CTE grading tracking the
   hoop-stress/contraction profile from ID to OD); in-process (winding-time) per-turn
   pressure trimming. No art in the ledger shows radial CTE grading.
5. **Parameter windows: NOT AVAILABLE.** The mission permits rung 5 only with sim
   criticality evidence; per G-PHYS, the decay constants and the 17x ratio are assumed
   inputs. Do not draft numeric cycle-life or k-floor windows until the G-PHYS
   revisions land (anchored or measured degradation curves).
6. **Application-field.** "Cryocooler-duty-cycled, cryogen-free operation" limitation —
   weak for patentability (and per G-PHYS currently unsupported by the sim as a
   technical distinction), but retain as a dependent and for a possible CN utility
   model.

### Recommended adjustment (grant odds x commercial scope)
Draft the independent claim at **rung 1** (combination), with the CTE match expressed
as the **measurable integrated-contraction tolerance of rung 3** (functional, testable,
not a bare "matched" adjective), plus a parallel **method-of-making** claim
(winding-time interlayer selection/verification). Put rung 2 (compliant element) and
rung 4 (radial grading) in as independent-worthy dependents and write every rung into
the spec now (no new matter later). **Cost in scope:** substantial — competitors
remain free to use non-CTE-matched interlayers with active thermal management, bath
cooling, or partial-depth impregnation (T3-6's own route); the claim protects only the
matched/compliant-interface route. That narrowness is the honest price of
US11,282,624 + T3-4 + T3-6 existing. Commercial scope preserved where it matters:
Hinetics-class cryogen-free machines and cryogen-free MRI inserts, where cycle-life of
a passive interface is the buying criterion.

**Proceed to W4 drafting ONLY after:** (a) G-PHYS revisions (cryogen-free sensitivity
actually modeled; anchored degradation curves), (b) the live-DB verification pass
(esp. KR KOR1020130130009 and the JP title-only hits), (c) attorney claim chart vs
US11,282,624. Registered patent attorney review required before any filing.
