<!-- Research aid — not legal advice. Automated research pipeline output. Patentability, FTO, inventorship, and ownership (incl. Stanford SU-18 / sponsor obligations) require a registered patent attorney before any filing, disclosure, or reliance. -->

# ID_03 — Thermal-Aware Current Steering in a Cryogen-Free Conduction-Cooled HTS Coil (CF-3)

> **Research aid — not legal advice.** Prophetic/simulated content is labeled and MUST NOT be
> blended with measured data. No filing is authorized by this document.

> **READ FIRST — status of this candidate.** CF-3 is the **weakest of the six W3 survivors.**
> It cleared the Fable-5 gates only as **NARROW-NOVEL (PROVISIONAL)** and its supporting
> simulation was found by G-PHYS to be an **artifact that is not yet valid comparative
> evidence** for the claimed mechanism. This disclosure is drafted to *preserve priority
> optionality and record the inventive concept*, NOT because the evidence is filing-ready. Two
> gating actions (a mandatory EP4078630B1 granted-claims pull, and a full simulation rebuild)
> must complete before any filing investment. See **Known Limitations / Required Pre-Filing
> Work** and **Counsel Questions** below.

---

## 1. Title

Thermal-aware current steering in a cryogen-free, conduction-cooled no-insulation (NI) or
partially-insulated high-temperature-superconductor (HTS) coil, in which turn-to-turn bypass
conductance is actively and spatially modulated according to a stored map of thermal conduction
from each turn to a cryocooler cold head, under a fixed cryocooler cooling-power budget.

## 2. Field

Cryogen-free / conduction-cooled HTS components cooled by a cryocooler of **limited cooling
power** with **no LN₂ and no cryogen bath**. Specifically, NI / partially-insulated HTS field
windings whose turn-to-turn current-sharing behavior is engineered or controlled to manage
hot-spot risk within a fixed cold-head lift budget. Anchor operating regime: conduction-cooled
NI HTS field coils.

## 3. Problem / Background

In a conduction-cooled NI (or partially-insulated) HTS coil, heat generated at or near a turn
must reach the cryocooler cold head through a solid conduction path. That path is **not uniform
across the winding**: turns differ in their thermal conduction to the cold head depending on
radial position, azimuthal position relative to the cold-head strap, contact quality, and
build tolerances. Under a **fixed, limited** cryocooler lift budget there is no bath to buffer a
local disturbance, so a turn with poor conduction access to the cold head is disproportionately
exposed to hot-spot growth if transport current lingers there during a disturbance or charge
transient.

Existing NI/PI current-management art (see IDS_pool) engineers or controls turn-to-turn current
sharing on the basis of **electromagnetic** criteria — field/critical-current (I/Ic) profile,
screening-current-field (SCF) equalization — or on the basis of **reactive, local quench
physics** (a bypass that goes resistive where it is already hot), or via a **single global**
power-supply feedback loop. None of the art found conditions the *spatial* bypass pattern on a
**known/measured map of thermal conduction to the cold head** under a **fixed cryocooler power
budget**. That is the gap this disclosure addresses.

**Problem statement:** given a per-turn (or per-zone) map of thermal conduction to the cold head,
route transport current *away from* turns with poor cooling access — proactively and in
operation — so peak hot-spot ΔT is held down without exceeding the cryocooler's fixed lift
budget.

## 4. Summary

A cryogen-free, conduction-cooled NI/partially-insulated HTS coil system in which turn-to-turn
bypass conductance is **spatially resolved** and **actively modulated in operation** according
to a **stored map of thermal conduction from each turn (or zone) to the cryocooler cold head**,
so as to redistribute transport current away from turns with poor cold-head cooling access while
holding total heat load within the cryocooler's fixed lift budget. The stored map may be measured
or modeled; the invention lies in *acting on a cold-head-conduction map to set/modulate spatial
bypass conductance*, not in acquiring the map (map acquisition is owned by third-party art —
see IDS_pool US 12,196,792 — and is expressly disclaimed as inventive subject matter here).

Sensing that informs actuation is **thermal (temperature sensors) and/or terminal-electrical
(voltage/current) only.** No magnetic/Hall-effect sensing of current distribution is claimed or
disclosed (see Explicit Exclusions §8 and the Hall-sensing compliance note).

## 5. Independent Claim (active, map-driven, system-level core)

> Drafted to the G-CLAIM recommended shape (ladder rungs 1 + 2): a cryocooler-budget-constrained
> system practicing **active, spatially-resolved** bypass modulation driven by a **stored
> cold-head thermal-conduction map.** Passive fixed placement is intentionally NOT the
> independent subject matter (that ground is occupied by the Tokamak Energy art) and appears only
> as an at-risk dependent claim (§6).

**Claim 1.** A cryogen-free superconducting coil system comprising:

- **(a)** a high-temperature-superconductor (HTS) winding of a plurality of turns wound as a
  no-insulation or partially-insulated coil, adjacent turns being coupled by a turn-to-turn
  bypass conductance;
- **(b)** a cryocooler having a cold head thermally coupled to the winding by a solid conduction
  path and no cryogen bath, the cryocooler having a fixed cooling-power (lift) budget at an
  operating temperature;
- **(c)** a plurality of spatially-distributed bypass elements, each associated with a respective
  turn or zone of the winding, each having a bypass conductance that is **adjustable in
  operation** between at least two states;
- **(d)** a stored map representing, for each of a plurality of turns or zones, a value of thermal
  conduction from that turn or zone to the cold head, the map being previously measured or
  modeled;
- **(e)** one or more sensors arranged to sense a coil state by **temperature and/or by terminal
  electrical measurement** (voltage and/or current), the sensors being free of magnetic-field /
  Hall-effect current-distribution sensing;
- **(f)** a controller configured to modulate, in operation, the bypass conductance of individual
  bypass elements as a function of said stored cold-head thermal-conduction map **(d)** and of the
  sensed coil state **(e)**, so as to redistribute transport current away from one or more turns
  or zones identified by the map as having comparatively poor thermal conduction to the cold head;
- **(g)** wherein the controller constrains the modulation such that total heat load delivered to
  the cold head is held within the cryocooler's fixed lift budget **(b)**.

**Comment (not part of claim):** Element **(d)**'s "measured or modeled" language must survive
the EP4078630B1 review (§9); if that specification ties bridge geometry/placement to cooling-path
topology, element **(d)** may need to be narrowed to *measured* and/or *dynamically updated*
maps, or the passive route abandoned entirely. Element **(f)**'s "modulate in operation" is the
principal distinguisher over all granted art found and should not be weakened to
"set at winding time" (that weaker scope is the at-risk dependent claim §6, rung "P").

## 6. Dependent Claims (ladder rungs; no rung 5)

> Ladder per G-CLAIM. **Rung 5 (parameter-window / criticality claims) is OMITTED entirely** —
> G-PHYS is REVISE and the simulation provides no valid criticality evidence; such claims are
> forbidden until the rebuilt coupled simulation exists (§9). Do not add numeric operating
> windows to this disclosure later without new supporting matter.

**Claim 2 (rung 1, combination detail).** The system of claim 1, wherein the cold head is
coupled to the winding by a discrete conduction strap at a defined azimuthal location, and the
stored map **(d)** represents conduction to that strap location.

**Claim 3 (rung 2, active mechanism — strongest rung).** The system of claim 1, wherein each
bypass element comprises a switchable or variable interposer whose turn-to-turn conductance is
set by the controller to at least two distinct values during operation, and wherein the
controller lowers the effective current retained in a poorly-cooled turn or zone by raising the
bypass conductance that diverts current around it.

**Claim 4 (rung 2, per-zone actuation).** The system of claim 3, wherein the bypass elements are
grouped into azimuthal or radial zones, and the controller actuates zones independently
according to per-zone values of the stored map.

**Claim 5 (rung 3, enabling sub-solution — parallel method).** A method of operating the system
of claim 1, comprising transforming the stored per-turn cold-head-conduction map into a spatial
bypass-conductance pattern that satisfies **both** a hot-spot margin target **and** a
charging-delay (ramp) target **subject to** the cryocooler's fixed lift budget, and applying that
pattern via the bypass elements — **without** claiming acquisition or measurement of the map
itself (map acquisition disclaimed; see IDS_pool US 12,196,792).

**Claim 6 (rung 3, dual-objective detail).** The method of claim 5, wherein the transformation
resolves a conflict between the hot-spot-margin objective and the charging-delay objective by
allocating bypass conductance preferentially to turns/zones the map identifies as poorly cooled.

**Claim 7 (rung 4, architecture/topology).** The system of claim 1, wherein the bypass elements
are azimuthally zoned and referenced to the physical cold-head strap location, the map and
actuation being resolved in the azimuthal coordinate rather than purely radially.

**Claim 8 (rung 4, rotating-frame variant — composes with CF-5).** The system of claim 7,
wherein the winding operates in a rotating frame and the azimuthal bypass pattern is referenced
to a rotating-frame cold-head coupling.

**Claim 9 (rung 6, application-field limitation — weak for patentability).** The system of
claim 1, embodied as a cryogen-free field coil, framed for utility-model / FTO positioning only.

**Claim P (PASSIVE PLACEMENT — DEPENDENT, EXPRESSLY FLAGGED AT-RISK).** The system of claim 1,
wherein at least some bypass elements have a **fixed** turn-to-turn conductance set at winding
time according to the stored map **(d)**, concentrating higher bypass conductance at turns the
map identifies as poorly cooled.
> **AT-RISK FLAG:** This passive/fixed-placement species is at material risk of being swallowed
> by the Tokamak Energy art (EP4012730A1 / KR102631117B1 and especially EP4078630B1). Per
> G-NOVEL, if EP4078630B1's granted claims/description tie bridge placement to cooling-path
> topology, **Claim P must be deleted** and only the active claims (1–8) survive. Claim P is
> retained here solely to keep the option open pending the mandatory EP4078630B1 pull (§9); it is
> **not** presented as independently patentable subject matter.

## 7. Embodiments

- **E1 — Active switchable-interposer coil.** Per-turn or per-zone switchable interposers between
  turns; a controller reads the stored cold-head-conduction map, reads temperature and terminal
  electrical state, and raises bypass conductance around map-identified poorly-cooled turns so
  transport current preferentially routes through better-cooled turns — subject to the lift
  budget. (Primary embodiment; supports claims 1, 3, 4.)
- **E2 — Zoned azimuthal actuation referenced to the cold-head strap.** Bypass zones indexed to
  azimuthal angle from the physical cold-head strap; map is azimuthally resolved. (Claims 4, 7.)
- **E3 — Rotating-frame variant.** As E2 but with a rotating-frame cold-head coupling; composes
  with CF-5. (Claim 8.)
- **E4 — Map→pattern controller as a method.** The transformation of a cold-head-conduction map
  into a bypass pattern meeting hot-spot-margin AND charging-delay targets under the lift budget,
  implemented in a controller/firmware. (Claims 5, 6.)
- **E5 — Passive wound-in placement (AT-RISK).** Fixed higher-conductance bypass at
  map-identified poorly-cooled turns, set at winding time. Retained only pending EP4078630B1
  review; see Claim P flag. (Claim P.)
- **Sensing across all embodiments:** temperature sensors and/or terminal voltage/current only.

## 8. Explicit Exclusions

- **No magnetic / Hall-effect current-distribution sensing** anywhere (compliance with CLAUDE.md
  Rule 1 funded-lane Hall-sensing adjacency check). Current state is inferred from temperature
  and/or terminal electrical measurement only.
- **No wide-bandgap III-nitride (Rule-2-excluded) semiconductor** material, device, or example
  anywhere; the winding and bypass elements are HTS conductor plus normal metal only.
- **No fusion-device application framing** anywhere (Rule 3); the CF-5 "rotating-frame"
  composition is described only as a conduction-cooled / cryogen-free rotating HTS winding.
- **Map acquisition/measurement is disclaimed** as inventive subject matter (owned by third-party
  art US 12,196,792); the invention is the *use of* a cold-head-conduction map to set/modulate
  bypass conductance.
- **No parameter-window / criticality claims** (rung 5 omitted; see §6, §9).
- **Not framed on I/Ic, field, SCF, or quench-self-regulation** as the steering basis — the
  steering basis is expressly *thermal conduction to the cold head under a fixed cryocooler
  budget*, to distinguish the IDS_pool art.

## 9. Prophetic Examples

> ⚠️ **STRONG CAVEAT — SIMULATED / PROPHETIC, AND NOT YET VALID COMPARATIVE EVIDENCE.** ⚠️
> The numbers below are **SIMULATED / prophetic (present tense)** and are **NOT** measured data;
> they MUST NOT be blended with any measured data. **More importantly, the G-PHYS gate found the
> present simulation to be an ARTIFACT that does not support the claimed mechanism.** These
> examples are included ONLY to describe the *intended* effect and to bound what a *rebuilt*
> simulation must show — they are **not** evidence of non-obviousness and **must not be cited as
> such** (number-truth discipline; `20_SIM/out/cf3_starter.json` is correctly labeled prophetic,
> but its comparison is not evidentially valid even as a prophetic example).
>
> **Specifically, per `60_PRIOR_ART/CF-3/gates.md` (G-PHYS = REVISE):**
> 1. The `min(k[i], k[i+1])` interface rule makes the "naive" evenly-spaced-copper **baseline
>    thermally inert by construction** — it cannot improve no matter how much copper it receives
>    (naive peak ΔT is identical, 25.4098 K, for n_cu = 2…12). "Steered beats naive in every
>    case" therefore follows from the discretization rule, **not from physics.**
> 2. The fault location (`spot_turn = 2`) is **co-located** with the steered copper block, a
>    cherry-pick/circularity; in a 1-D series network, position within the fault→sink path does
>    not matter, so the reported advantage is not a genuine placement advantage. The sweep that
>    matters (worst-case/expectation over fault location) was never run.
> 3. **The claimed mechanism — current steering — is absent from the model.** No electrical/
>    current-flow network was simulated; the load is a fixed 0.5 W injected at a fixed node
>    (`cold_head_load` is trivially 0.5 W in every row). What was simulated is a *thermal* drain-
>    placement effect (CF-1's), wearing CF-3's label. **No conclusion about current
>    redistribution can be drawn.**
>
> **Prophetic Example 1 (intended effect only — currently unsupported).** In a rebuilt,
> per-interface-material, electrically-coupled model, concentrating adjustable bypass conductance
> at map-identified poorly-cooled turns is *expected* to reduce peak hot-spot ΔT relative to a
> fairly-modeled uniform baseline at equal bypass budget, while holding cold-head load within the
> fixed lift budget. **The magnitude is unknown until the rebuild;** the present ~0–34% figures
> in `cf3_starter.json` are artifacts and are expressly **not** relied upon.
>
> **Prophetic Example 2 (what the rebuild must demonstrate).** Over a *sweep of fault location*
> (worst-case and expectation), active map-driven modulation is *expected* to outperform both a
> fairly-modeled uniform placement and a passive fixed placement — this is the comparison that
> would, if it holds, support the inventive step. It has **not** been demonstrated.

## 10. IDS_pool (duty of candor — full ledger; all 19 hits, including damaging ones)

> Design-around ≠ concealment. Every art item the engine found is listed. A patent granted to us
> ≠ freedom to operate. Bibliographic gaps flagged in `60_PRIOR_ART/CF-3/ledger.md` remain open.

**Closest / most damaging (Tier 1 patents):**
1. **EP4012730A1 / WO2019150123A1 / AU2019214510A1 / CN114512293A / KR20220025932A /
   KR102631117B1** — Tokamak Energy, "Partially-Insulated HTS Coils," priority 2018-02-01.
   Spatially-staggered turn-to-turn resistance windows controlling current distribution. EP
   withdrawn; **KR102631117B1 granted (in-force FTO exposure in KR).** *Blocks spatial-bypass-
   placement genus.*
2. **EP4078630B1** — Tokamak Energy, "HTS Linked Partial Insulation," priority 2019-12-20,
   **granted 2023-11-15, in force.** HTS bridges self-regulate (local quench → resistance rise),
   pushing current toward cooler/slower-quenching regions; thermal & electrical properties
   independently tunable via geometry. **THE decisive reference — G-NOVEL is PROVISIONAL pending
   a pull of its granted claims + INPADOC family; if bridges are tied to cooling-path topology,
   CF-3's passive species DROPS TO DUPLICATED.** Also an FTO watch item in EP/KR.
3. **US 11,094,438 B2 / US 11,551,840 B2** (+ US20190088391A1 / US20220102040A1) — Florida State
   Univ. Research Foundation (Hahn/Larbalestier), priority 2016-05-06. Active PI feedback control
   of NI HTS magnet — *blocks "active control" framed as a single global knob.*
4. **US 11,581,115 B2** — SNU R&DB Foundation (Hahn et al.), priority 2019-04-19. Engineered
   spatial *temperature* map via heaters to shape current/field — *blocks "impose a thermal map
   to steer current" framed broadly.*
5. **US 12,196,792 B2** — assignee UNCONFIRMED (ledger Gap 1). Non-destructive measurement of
   turn-to-turn resistivity distribution — *owns the map-acquisition step; CF-3 must claim
   use-of-a-map, not acquisition.*
6. **US 10,861,626 B2 / US20190074118A1** (WO2017039299A1) — KERI, priority 2015-09-04.
   MIT-material temperature-triggered autonomous bypass — *blocks "bypass that responds to local
   temperature" per se.*
7. **CN115485868A** — Tokamak Energy, priority 2020-05-04, granted 2026-04-07. Spatially-graded
   edge-cladding removal to hold I/Ic (field-profile-driven).
8. **WO2013180802A1 / US 9,117,578 B2** — MIT (Hahn/Iwasa/Bascunan), priority 2012-03-13.
   Multi-width NI winding; fixed-at-winding-time geometric current steering.

**Tier 4 (low relevance, logged for candor):**
9. **US 8,823,476 B2** — Samsung (Harrison), priority 2011-10-11, expired. Bulk on/off
   shape-memory/gas switch for coil power.

**Tier 3 — NPL (background/adjacent):**
10. "Hot-Spot Modeling of REBCO NI Pancake Coil…" — MIT (PMC/IEEE).
11. **"Control of turn-to-turn contact resistivity in resistively insulated REBCO coils"** —
    arXiv 2604.15587. *On-mechanism title, UNREAD (ledger Gap 6) — must be read before filing.*
12. "Explicit Turn Resolution with Anisotropic Homogenisation… 3D Magneto-Thermal FE Simulation
    of NI HTS Magnets" — arXiv 2605.31009.
13. "Surface Contact Approximation for Magneto-Thermal FEA of NI HTS Coils" — arXiv 2605.28574.
14. "Electromagnetic-Thermal-Mechanical Characteristics With Active Feedback Control in an NI
    HTS Magnet" — Science China Phys. Mech. Astron. (corroborates ref. 3).
15. "Determining Operating Current of NI Field Coil in HTS Generators" — ResearchGate.
16. "Current Bypassing and Transient Stability in a Partially Insulated HTS Coil" — IEEE TAS
    8239865.
17. "Electromagnetic Behaviour and Thermal Stability of a Conduction-Cooled, No-Insulated 2G-HTS
    Coil at Intermediate Temperatures" — Cryogenics (closest NPL to CF-3's *operating regime*).
18. "Turn-to-Turn Contact Resistance Measurement of NI REBCO Pancake Coil: External Field
    Dependence" — IEEE TAS 9392348 (corroborates ref. 5).
19. "Experimental and Numerical Study on Current Distribution in Parallel Co-Wound NI Coils" —
    arXiv 2507.08552.

**Total: 19 references. All remain in IDS_pool regardless of any novelty verdict.**

## 11. Known Limitations / Required Pre-Filing Work

> This section is deliberately prominent. **The current evidence does not yet support the claimed
> mechanism and is NOT filing-ready.** Two gating actions must complete first.

**A. Simulation rebuild required (G-PHYS = REVISE).** The present sim
(`20_SIM/cf3_current_steering.py` → `out/cf3_starter.json`) is an artifact. Before any parameter
claim, non-obviousness argument, or filing reliance, the sim MUST be rebuilt to:
1. **Assign interface material per interface**, removing the `min(k[i], k[i+1])` rule that makes
   the naive baseline inert by construction.
2. **Add a coupled electrical NI bypass network** so transport current actually redistributes in
   response to bypass placement/actuation, with **Joule heating from the redistributed current as
   the load** — not a hand-placed fixed `q_spot`. (This simulates the *claimed* mechanism, which
   is currently absent.)
3. **Sweep fault location (`spot_turn`) across all turns**; report **worst-case and expectation**
   over fault position, not a single co-located fault.
4. **Fix the W vs W/K units** of the cold-head boundary (treat the lift budget as a load-line
   constraint, not a conductance).
5. On pulling in the electrical side, **independently verify the tau↔Rc direction** against NI/MI
   literature (Hahn et al.) — the CF-1 known issue (`tau_rc_narrative_direction`) must not be
   inherited.

**B. Mandatory prior-art pull — could kill this candidate (G-NOVEL PROVISIONAL).**
- **Pull EP4078630B1's full granted claim set + description + INPADOC family (Espacenet).** The
  ledger contains only an abstract paraphrase. **If the specification ties bridge geometry/
  placement to cooling-path / cold-head topology, CF-3's passive species drops to DUPLICATED and
  Claim P must be deleted; if the *active, map-driven* concept is also disclosed, the entire
  candidate may collapse.** This pull is a hard gate on filing.
- Also pull the full EP4012730A1 family tree (ledger Gap 5).
- Close **ledger Gap 1** (US 12,196,792 assignee/priority via PatentsView/USPTO) and **Gap 6**
  (read arXiv 2604.15587 — on-mechanism, currently unread).
- JP/KR/CN coverage was via Google-Patents family proxies, not native J-PlatPat/KIPRIS/CNIPA
  browses (ledger Gaps 2–4); "no JP-only hit" is a negative search result, **not clearance.**

**C. Claim-scope consequences.**
- No rung-5 parameter-window claims exist or may be added until (A) lands.
- Claim P (passive placement) is provisional pending (B).
- Element (d)'s "measured or modeled" may need narrowing to "measured/dynamically-updated"
  depending on the EP4078630B1 read.

**D. FTO (distinct from patentability).** Even if CF-3's active species grants, a product whose
bypass sites also self-regulate thermally (any real HTS bridge does, to some degree) may practice
EP4078630B1 (EP) and KR102631117B1 (KR). A patent granted to us ≠ freedom to operate; counsel
FTO analysis required in EP/KR regardless.

**E. Model-served caveat.** The W3 gate verdicts were intended for Fable 5, but the actually-
served model is not verifiable from inside the session (Anthropic safeguards may route some
Fable-5 queries to Opus 4.8). Confirm against the external transcript
(`%USERPROFILE%\.claude\projects\`) before filing-relevant reliance.

## 12. Counsel Questions

1. **Investment gate:** CF-3 is **the shakiest of the six survivors.** Given (a) the current sim
   is an artifact that does not demonstrate the claimed current-steering mechanism, and (b) novelty
   is provisional pending the EP4078630B1 claims pull that could drop it to DUPLICATED — **does
   this candidate merit filing investment now, or should it be deferred** until the sim is rebuilt
   (§11.A) and EP4078630B1 is read in full (§11.B)? Our recommendation is **DEFER** (see report).
2. **EP4078630B1 dispositive read:** Do EP4078630B1's granted claims/description tie bridge
   placement to cooling-path / cold-head conduction topology, or to active/measured-map-driven
   modulation? If yes to either, which of Claims 1–8 / Claim P survive?
3. **"Active in operation" as the inventive hinge:** Is *active, spatially-resolved, in-operation*
   modulation driven by a stored cold-head-conduction map sufficiently distinct from (i) FSU/Hahn
   global feedback (US 11,094,438 / 11,551,840), (ii) SNU heater-imposed thermal maps
   (US 11,581,115), and (iii) KERI temperature-triggered bypass (US 10,861,626) to carry inventive
   step in US/EP/KR/JP/CN?
4. **Map-use vs. map-acquisition line:** Is the disclaimer of map acquisition (US 12,196,792)
   drawn cleanly enough that Claim 5's method does not read on the measurement art?
5. **Ownership two-prong (SU-18 / sponsor):** Confirm CF-3 (cryogen-free coil thermal/current-
   distribution work) is outside the funded lane (HSX plasma diagnostics / the III-nitride
   Hall-effect device lane / battery magnetic imaging). The Hall-sensing adjacency was affirmatively excluded (§8); please verify no
   subject-matter (prong-a) exposure.
6. **Rotating-frame composition (Claim 8 / CF-5):** any inventorship/ownership entanglement with
   CF-5 to resolve before either files?

---

> **Research aid — not legal advice.** No filing is authorized by this document. Simulated content
> is labeled prophetic/present-tense and is not blended with measured data. All prior art found is
> retained in IDS_pool per the duty of candor. Registered patent attorney review required before
> any filing, disclosure, or reliance.
