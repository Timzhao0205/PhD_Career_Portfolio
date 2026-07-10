<!-- Research aid — not legal advice. Automated research-pipeline output. Patentability,
     freedom-to-operate, inventorship, and ownership (including Stanford SU-18 / sponsor
     obligations) are fact-specific legal determinations requiring a registered patent
     attorney before any filing, disclosure, or reliance. This document authorizes nothing
     and is an internal invention disclosure for attorney review only. -->

# Invention Disclosure ID_02 — Thermal-Margin-Aware Quench Detection for Conduction-Cooled HTS Windings

**Candidate:** CF-2 · **Wave:** W4 (disclosure drafting) · **Prepared:** 2026-07-10
**Gate status carried in:** G-PHYS = REVISE · G-NOVEL = NARROW-NOVEL (CONDITIONAL) · G-CLAIM = SHAPED combination claim
**Status:** DRAFT — internal only. NOT FILED. NOT CLEARED. Registered patent attorney review required before any use.

> **Research aid — not legal advice.** Every quantitative result herein is SIMULATED / prophetic and is
> presented in present tense; no measured hardware data appears anywhere in this document, and no simulated
> number is blended with measured data in any figure, table, or example. Two open risks materially condition
> everything below and are flagged in-line and in §11: **(i)** the novelty verdict is CONDITIONAL on obtaining
> the full text of IEEE Xplore #9893361, not yet in hand; and **(ii)** the independent claim's
> cryocooler-telemetry-input element currently rests on the narrowing *intent* of the mechanism, **not** on
> differential simulation proof (the present sim shows no case where tracking cryocooler state, rather than
> turn position, changes the detection outcome).

---

## 1. Title

**Thermal-Margin-Aware Quench Detection for a Conduction-Cooled High-Temperature-Superconducting Winding Using Per-Location Baseline Thresholds Derived from a Cryocooler-State-Driven Conduction Thermal Model.**

---

## 2. Field of the Invention

<!-- Research aid — not legal advice. -->

This disclosure relates to quench detection and protection for high-temperature-superconducting (HTS) windings
that are **conduction-cooled by a cryocooler of limited cooling power, with no liquid-cryogen bath** (no LN₂,
no He bath). More specifically, it relates to setting quench-detection trip thresholds by reference to a
spatially resolved, cryocooler-state-dependent temperature/thermal-margin map of the winding, rather than to a
fixed or bath-referenced setpoint. Exemplary target windings include conduction-cooled no-insulation (NI) /
metal-insulation (MI) field coils of the class used in aviation-scale superconducting motors, and
conduction-cooled HTS inserts and coils generally.

---

## 3. Problem / Background

<!-- Research aid — not legal advice. -->

In a liquid-cryogen bath, the coolant provides a large, spatially uniform thermal buffer: local heat is absorbed
by boil-off and the winding sits near a single bath-pinned temperature. A quench-detection (QD) threshold
calibrated to that pinned temperature is reasonable because the no-fault operating temperature is roughly the
same everywhere and roughly constant in time.

Conduction cooling with a limited-power cold head removes that buffer. Heat must travel to the cold head through
solid conduction, so the no-fault temperature is **location-dependent** — inner turns far from the cold-head sink
run warmer than well-cooled turns near the sink — and it is **cooling-state-dependent** — as the cryocooler's
available lift changes (duty cycle, cold-head temperature drift, compressor/motor state, capacity fade,
recovery after an excursion), the whole no-fault temperature profile shifts. A single fixed threshold cannot be
correct across both axes at once:

- Set the threshold loose enough not to false-trip on the warmest no-fault location (or the warmest cooling
  state), and it becomes **insensitive** to a genuine incipient quench at a better-cooled location, whose small
  absolute temperature excursion hides beneath the fixed level.
- Set it tight enough to catch those better-cooled locations, and it **false-trips** on the ordinary no-fault
  gradient as soon as position or cooling state shifts the baseline.

The published literature explicitly flags this: HTS's large temperature margin and slow normal-zone propagation
make fixed voltage thresholds unreliable (see §10, NPL items), and conduction-cooled REBCO motor-coil work names
quench detection and rapid thermal management as open challenges. The closest single reference (IEEE #9893361,
see §8 and §10) addresses the cooling-state dependence by **forecasting a temperature-rise trajectory** used as a
trigger; the gap this disclosure targets is a *spatially resolved, per-location* thermal-margin referencing tied
to **live cryocooler-state telemetry** — the version a limited-cooling-power product actually needs.

---

## 4. Summary

<!-- Research aid — not legal advice. -->

A quench-detection system for a conduction-cooled HTS winding continuously recomputes, for **each of a plurality
of sensing locations**, that location's own model-predicted **no-fault baseline temperature (or thermal margin)**,
using a **conduction thermal model of the winding** that takes **live cryocooler-state telemetry** as an input,
and trips when a location's measured quantity exceeds its local baseline **plus a margin**. Trip sensitivity
thereby tracks both spatial position in the winding and the instantaneous cooling state, instead of any fixed or
bath-referenced setpoint. The distinguishing mechanism, relative to the closest art, is **threshold referencing**
(subtracting a per-location modeled baseline from the measurement) driven by **cryocooler operating state**,
rather than forward-forecasting a single lumped temperature-rise trajectory driven by magnet current.

**Scope deliberately surrendered (per G-CLAIM):** the genus of "any model-based or adaptive QD threshold" is not
claimed. A competitor using a lumped, current-driven temperature-rise forecast (as in IEEE #9893361) is outside
the independent claim by design. The protected space is the spatial + cryocooler-telemetry-referenced
implementation.

---

## 5. Independent Claim (combination / system — rung 1 with rung-2 distinctions as express limitations)

<!-- Research aid — not legal advice. Claim language is a drafting aid for counsel, not a filing-ready claim. -->

**Claim 1.** A quench-detection system for a high-temperature-superconducting (HTS) winding that is
conduction-cooled by a cryocooler and operated without a liquid-cryogen bath, the system comprising:

- **(a)** a plurality of sensing locations distributed across the winding, each sensing location associated with
  a respective sensor configured to produce a measured signal indicative of a local condition of the winding at
  that location (e.g., a local temperature or a local voltage);

- **(b)** a telemetry interface configured to receive **live cryocooler-state telemetry** representing an
  instantaneous cooling state of the cryocooler, the telemetry comprising one or more of: a cold-head
  temperature, a cryocooler load-line position, and a compressor or drive-motor operating state;

- **(c)** a conduction thermal model of the winding, executable on a controller, that represents heat transport
  through the winding to a cold-head sink and that takes the cryocooler-state telemetry of element (b) as an
  input, and that computes, for each of the plurality of sensing locations, a respective **model-predicted
  no-fault baseline** for that location under the current cooling state;

- **(d)** a comparator, for each sensing location, configured to compute a **per-location trip threshold equal to
  that location's model-predicted no-fault baseline of element (c) plus a margin**, and to assert a
  location-specific quench indication when the measured signal of element (a) for that location exceeds its
  per-location trip threshold; and

- **(e)** a protective-action interface responsive to an asserted quench indication, configured to initiate a
  protective action selected from at least one of: energizing a dump circuit, energizing a co-wound or
  distributed heater, and derating transport current,

  wherein the per-location trip thresholds of element (d) are **continuously recomputed** as the cryocooler-state
  telemetry of element (b) changes, such that trip sensitivity tracks both the spatial position of each sensing
  location within the winding and the instantaneous cooling state of the cryocooler, rather than any fixed or
  bath-referenced setpoint.

> **Caveat carried on element (b)/(c) — material for counsel.** The narrowing force of this claim rests on the
> cryocooler-telemetry input being an operative, outcome-changing element. As of this draft the supporting
> simulation demonstrates the *spatial per-location* half of the mechanism (element (d) catching faults a fixed
> threshold misses) but does **not** yet demonstrate a case where varying the cryocooler-state input **changes
> the detection outcome** — across the three simulated cooling budgets the miss set is nearly identical and there
> are zero false trips (see §9 and §11). Element (b)/(c) therefore currently rests on the *intent* of the
> mechanism and on the physical argument that a shifting cooling state shifts the no-fault baseline, not on
> differential simulation proof. The degraded-cooling sweep in §11 is required to convert this from intent to
> evidence before any filing decision.

---

## 6. Dependent Claims (ladder rungs 3, 4, 6 — rung 5 deliberately OMITTED)

<!-- Research aid — not legal advice. Rung 5 (numeric parameter-window / criticality-based) claims are
     intentionally NOT drafted; see the note at the end of this section and §11. -->

**Rung 3 — enabling sub-solution (what makes the adaptive-threshold idea actually work on a resource-limited
controller):**

- **Claim 2.** The system of claim 1, wherein the conduction thermal model computes the per-location no-fault
  baselines by **linear superposition** of per-location single-source thermal solutions, such that a change in
  cryocooler-state telemetry triggers a low-cost recomputation of the baseline map suitable for execution on an
  embedded magnet controller.

- **Claim 3.** The system of claim 1, further comprising a **false-trip suppression** function that, during a
  cryocooler ramp, capacity-degradation, or recovery transient indicated by the telemetry of element (b),
  updates the per-location baselines to the transient cooling state so that the comparator does not assert a
  quench indication on the shifted no-fault profile.

- **Claim 4.** The system of claim 1, wherein each per-location no-fault baseline is computed from (i) the
  cryocooler-state telemetry and (ii) an estimate of ordinary background loss in the winding, and the comparator
  references the measured signal to that location's baseline by subtracting the baseline from the measured
  signal before comparison against the margin.

**Rung 4 — architecture / topology:**

- **Claim 5.** The system of claim 1, wherein the winding is a no-insulation (NI) or metal-insulation (MI)
  winding, and the conduction thermal model is co-designed with a **spatial interface-conductance map** of the
  winding's turn-to-turn interface, such that the per-location baselines account for the location-dependent
  radial thermal drain to the cold head. *(Composes with candidate CF-1's spatial interface-conductance map;
  disclosed here as an embodiment to preserve support — no new matter later.)*

- **Claim 6.** The system of claim 1, wherein the cryocooler-state telemetry of element (b) is conveyed across a
  **rotary coupling** to a controller for a rotating conduction-cooled motor field coil, and the per-location
  baselines are recomputed in the rotating frame.

- **Claim 7.** The system of claim 1, wherein the plurality of sensing locations comprises sensors at a
  plurality of radial turn positions of a pancake or racetrack winding, arranged such that the per-location
  thresholds differ between a turn nearer the cold-head sink and a turn farther from the cold-head sink.

**Rung 6 — application-field limitation (weak for patentability; retained for FTO positioning and a possible CN
utility-model parallel):**

- **Claim 8.** The system of claim 1, wherein the winding is a field coil of a conduction-cooled aviation-class
  superconducting motor.

- **Claim 9.** The system of claim 1, wherein the winding is a coil of a conduction-cooled HTS insert for
  magnetic-resonance or nuclear-magnetic-resonance apparatus.

> **Rung 5 (parameter windows) intentionally omitted.** No numeric threshold, margin value, or
> criticality-based parameter window is claimed. Per G-CLAIM, rung-5 claims are embargoed until the simulation
> (i) has its `cooling_budget()` units defect fixed and (ii) produces actual criticality evidence (a sweep
> showing a specific margin/threshold window is critical). Asserting a specific numeric margin as "critical"
> now — on a sim with a units conflation and no criticality sweep — would be unsupported and is not done. See
> §11.

---

## 7. Embodiments

<!-- Research aid — not legal advice. -->

1. **Baseline embodiment (temperature sensing).** Temperature sensors at a plurality of turn/azimuth positions;
   a conduction thermal model of the winding driven by cold-head temperature and load-line telemetry computes
   each location's no-fault baseline temperature; each comparator trips on (measured − baseline) > margin; on
   trip, a dump circuit and/or co-wound heater fires.

2. **Voltage-sensing embodiment.** The per-location measured signal is a local voltage across a winding
   segment; the conduction thermal model supplies a per-location expected no-fault signal under the current
   cooling state, and the comparator references measured to modeled per segment. (Kept to temperature/voltage
   sensing only — see the prong-a constraint in §8.)

3. **NI/MI co-designed embodiment (composes with CF-1).** The thermal model incorporates a spatial
   interface-conductance map; the per-location baselines and the interface-conductance map are co-optimized so
   that both the radial thermal drain and the detection thresholds are spatially resolved.

4. **Rotating-frame embodiment.** For a conduction-cooled NI motor field coil, telemetry crosses a rotary
   coupling and baselines are recomputed on a rotating-frame controller (Hinetics CRUISE-class conduction-cooled
   field-coil use case as the anchor application).

5. **Cheap-recompute embodiment.** Baselines are maintained by linear superposition so that a cooling-state
   change costs one inexpensive map update, suitable for an embedded controller.

**Explicitly excluded from all embodiments:** Hall-effect-sensor-based detection is **not** an embodiment of this
invention (see §8). No GaN/AlGaN device or material is used, described, or claimed anywhere.

---

## 8. Explicit Exclusions

<!-- Research aid — not legal advice. -->

The following are expressly carved out of the claimed invention:

1. **Lumped / global temperature-rise forecast schemes not tied to per-location conduction mapping.** A scheme
   that forecasts a single coil-level (lumped) temperature-rise trajectory and trips on that forecast — without a
   *spatially resolved, per-location* no-fault baseline map of the winding — is **excluded**. This genus is
   carved out because IEEE #9893361 ("Temperature Rise Forecast," see §10) likely covers it: it forecasts an
   apparently lumped, coil-level temperature-rise trajectory validated under poor-refrigeration conditions.
   Claim 1 requires the per-location baseline map (element (c)/(d)) precisely to sit outside this genus.

2. **Forward-forecasting a temperature trajectory as the trigger** (as opposed to *referencing* a measured
   signal to a per-location modeled baseline) is excluded from the independent claim's mechanism. The claimed
   mechanism subtracts a modeled per-location baseline; it does not forecast a rise trajectory.

3. **Current-driven / electromagnetic modeled quantity as the trip driver** (e.g., a digital twin modeling coil
   current or inductance non-uniformity, as in IEEE #10412643) is outside the claim, whose model input of
   interest is **cryocooler operating state**, not magnet current.

4. **Static / preset / bath-referenced thresholds** (voltage, current-imbalance, diode-gated, or
   bridge-comparator) — the incumbent field — are outside the claim by the "continuously recomputed … rather than
   any fixed or bath-referenced setpoint" limitation.

5. **Hall-effect-sensor-based quench detection is excluded** (both to distinguish FSU's US10515749 family and to
   avoid the user's funded Hall-device subject-matter lane entirely — hard rule 1, prong a). Sensing is limited
   to temperature and voltage.

---

## 9. Prophetic Examples

<!-- Research aid — not legal advice. Every number in this section is SIMULATED / prophetic, present tense,
     and NOT blended with any measured data. -->

> **PROMINENT DIFFERENTIAL-EVIDENCE CAVEAT — read before relying on any number below.** These examples support
> the **spatial per-location** half of the mechanism (element (d)). They do **not** yet provide differential
> evidence for the **cryocooler-telemetry** half (element (b)/(c)): across the three simulated cooling budgets
> the set of faults missed by the fixed rule is nearly identical (5 / 6 / 6 of 30), driven by radial *position*,
> and there are **zero** false trips at any cooling level — so there is currently **no simulated case in which
> tracking cryocooler state, rather than turn position, changes the outcome**. Additionally, the
> `cooling_budget()` function in the source model returns a lift budget in **watts (W)** but is consumed as a
> conductance in **W/K**; this units conflation means **no numeric threshold or ΔT below may appear in a filing
> or be relied upon** until G_ch is re-derived from a physical strap/joint model (see §11). The *qualitative*
> position-driven headline is robust to the units slip (the missed turns are the well-cooled outer turns at every
> positive conductance); the specific numbers are not yet filing-grade.

**Source:** `20_SIM/cf2_quench_margin.py`, `20_SIM/out/cf2_starter.json` (SIMULATED_prophetic = true).

**Model (prophetic).** A linear 1-D radial conduction network, one node per turn, N = 30 turns, cold-head sink at
the outer diameter through conductance G_ch; a uniform interface is used to isolate the detection-threshold
question from CF-1's interface-material question. A no-fault baseline profile is built by linear superposition of
single-turn solutions under an assumed background loss; a fault-precursor heat pulse is injected at each turn in
turn; two trip rules are compared under identical dense per-turn sensing (the fair comparison — the fixed rule is
given the same sensors, isolating the *thresholding logic*, not sensor count):

- Assumed (not measured) parameters: background loss 0.01 W/turn; fault pulse 0.30 W; margin 3.0 K; the fixed
  threshold is calibrated once at T_cold = 20 K as (max no-fault ΔT) + 3 K.
- **Fixed rule:** trip if (T at fault turn − T_cold) exceeds the single calibrated threshold.
- **Local (claimed) rule:** trip if (T at fault turn − that turn's own no-fault baseline) exceeds the margin.

**Prophetic result (SIMULATED — qualitative headline only; numbers pending units fix).**

| Quantity (SIMULATED/prophetic) | Value |
|---|---|
| Total fault cases swept (30 turns × 3 cooling budgets) | 90 |
| Faults missed by the fixed rule but caught by the local per-location rule | 17 |
| Cases both rules detect | 55 |
| False trips by either rule on the no-fault baseline | 0 |
| Missed set per cooling budget (20 K / 30 K / 50 K) | 5 / 6 / 6 |

**Interpretation (prophetic).** The 17 additional catches are turns ~18/19–23 at every cooling level: a fault
near the well-cooled outer diameter produces a small *absolute* excursion that hides beneath a threshold
calibrated at the worst-case inner turn, but stands out clearly against that same outer turn's own low no-fault
baseline. This is the spatial-map advantage. **Honest characterization of the ~18 "neither-detects" outer-turn
cases:** these are defensible — the best-cooled locations, under a 0.3 W pulse, yield a local rise below the 3 K
margin — but they are stated explicitly rather than left silent; the effect is real, not an artifact, and it does
not depend on the units error.

**What these examples do NOT show (restated for counsel):** they do not exercise element (b)/(c) differentially.
The degraded-cooling scenario in §11 — where the fixed rule false-trips on a shifted no-fault baseline or misses
under recovered margin while the telemetry-referenced rule tracks it — is the missing evidence and is required
before this disclosure's independent-claim telemetry element is supported by simulation.

---

## 10. IDS_pool (duty of candor — full ledger; damaging references included)

<!-- Research aid — not legal advice. Every reference the harvest found is listed, including the items that most
     hurt CF-2. Design-around is claim-shaping in view of the art, never concealment of it. -->

**Closest / most damaging art (top priority for counsel):**

| # | Reference | Assignee / venue | Juris. | Why it matters |
|---|---|---|---|---|
| 1 | **IEEE Xplore #9893361 — "A Quench Protection Method for HTS Coils Based on Temperature Rise Forecast" (2022, NPL)** | academic (author/institution unconfirmed) | worldwide (NPL) | **SINGLE CLOSEST ART.** Conduction-cooled HTS coils; predictive temperature-rise **forecast** trigger validated under "poor refrigeration conditions." **Full text NOT obtained — novelty is CONDITIONAL (see §11). MANDATORY full-text pull before any filing decision.** |
| 2 | **IEEE Xplore #10412643 — "Overcurrent Quench Detection of Parallel-Wound NI HTS Coil Based on Digital Twin Method" (2024, NPL)** | academic | worldwide (NPL) | Real-time model-referenced trip logic for NI HTS coils is known; modeled quantity is electromagnetic (current/inductance), not a thermal-margin map. Fences the genus. |
| 3 | **CN122194022A — "A quench detection system and method for superconducting magnets"** | Suzhou/Shanghai Xinghuan Junen (Energy Singularity) | CN | Pending; preset-threshold bridge/comparator. **Live FTO watch item** — active 2026 Chinese fusion-HTS filer in CF-2's neighborhood; secondary-source only. **CNIPA-direct verification MANDATORY (China ≈ no grace period).** |

**Fixed-threshold contrast art (supports the gap; proves the space is heavily patented):**

| # | Reference | Assignee | Juris. | Note |
|---|---|---|---|---|
| 4 | US11101059B2 (US20180294077A1) | Tokamak Energy Ltd | US | Static predetermined voltage threshold; indirectly-cooled HTS. |
| 5 | US7876100B2 | General Electric | US | Fixed voltage thresholds; contemplates 4 K cryocooler MRI. |
| 6 | GB2514372A | (GB family — verify) | GB | Fixed voltage threshold; discusses both bath and pulse-tube cryocooler cooling. |
| 7 | US7649720B2 | Florida State Univ. Research Foundation | US | Pre-calculated (geometry-based, not real-time) temperature-rise targets; event-reactive. |
| 8 | US10515749B2 / US11217373B2 | Florida State Univ. Research Foundation | US | Current-imbalance detection via **Hall-effect sensors** — adjacency flagged; CF-2 excludes Hall sensing (§8). |
| 9 | US11190006B2 (US20200091702A1) | Tokamak Energy Ltd | US | Material-based energy absorption; event-based detection. |
| 10 | US12578370B2 (US20230384356A1) | University of Houston System | US | Reflectometry (Q-factor) sensing; no threshold adaptation. |
| 11 | CN102214911B | IEE-CAS | CN | Fixed diode voltage thresholds; no thermal/cooling-state logic. |
| 12 | CN101446610B | China Electric Power Research Institute | CN | Analog comparator; static comparison; no temperature/cooling-state input. |
| 13 | US20190074118A1 ("smart insulation," MIT-material) | Korean-origin (verify) | US (KR priority?) | Passive fixed-physical-temperature phase transition; not telemetry-driven recompute. Adjacent; fetch full text for IDS. |

**Rationale-supporting / background NPL and other:**

| # | Reference | Note |
|---|---|---|
| 14 | arXiv 2507.20178 (conduction-cooled REBCO racetrack, aircraft motors, 30 K) | Names quench detection + rapid thermal management as open challenges; post-hoc only. Supports unmet need. |
| 15 | Instruments 5(3):27 (2021), OSTI #1812231 (Fermilab) | Survey: HTS large thermal margin makes fixed voltage thresholds unreliable. Supports problem statement. |
| 16 | arXiv 2112.00823 (Fermilab QPM) | Baseline QD electronics reference (fixed-threshold voltage taps + DAQ). |
| 17 | arXiv 2603.29740 (CEA digital twins) | Full text NOT extracted (corrupted PDF) — relevance UNCONFIRMED; retry before relying/dismissing. |
| 18 | US20160178716A1 / CN107110928B (GE-family) | Cryocooler-interruption "ride-through"; cryogen buffering, not threshold referencing. |
| 19 | EP2624262A2 | Cryocooler-magnet system; no confirmed QD-threshold content — full-text review flagged. |
| 20 | KERI conduction-cooled magnet press coverage (KR) | Program exists (NbTi, 4.9 K); no patent-level QD detail — re-check KIPRIS directly. |
| 21 | Hinetics CRUISE-program public disclosures | Anchor exemplar assignee; **no Hinetics QD patent located** — dedicated USPTO/WIPO assignee search recommended (potential most-load-bearing art / self-collision check). |

---

## 11. Known Limitations / Required Pre-Filing Work

<!-- Research aid — not legal advice. These are gating items; several are MANDATORY before any filing decision. -->

**Novelty is CONDITIONAL, not settled:**

1. **[MANDATORY] Obtain and analyze the full text of IEEE #9893361.** The NARROW-NOVEL verdict is explicitly
   provisional on abstract-level information. If the full text discloses (i) spatial resolution of the winding
   temperature, or (ii) cryocooler/cold-head state as a model input, the gap narrows to nothing and the verdict
   falls to DUPLICATED. **Do not draft or file claims that survive only if the abstract is the whole story.**
   G-NOVEL and G-CLAIM must be re-run after full-text review.

**Simulation evidence gaps (the independent claim's telemetry element is not yet proven):**

2. **[MANDATORY] Add a degraded-cooling / cooling-state sweep to supply differential evidence for element
   (b)/(c).** As drafted, the sim shows the spatial half only; the miss set is nearly identical (5/6/6) across
   cooling budgets and there are zero false trips, so **no simulated case shows cryocooler state (vs turn
   position) changing the outcome.** Required: reduce G_ch by 2–5× at fixed nominal T_cold, and/or drift T_cold
   upward as capacity fades, and show (a) the fixed rule false-trips on the shifted no-fault baseline or misses
   under recovered margin, while (b) the telemetry-referenced rule tracks it. Until this lands, element (b)/(c)
   rests on mechanism *intent*, not proof.

3. **[MANDATORY] Fix the `cooling_budget()` units conflation (W vs W/K).** The function returns a lift budget in
   watts but is consumed directly as G_ch in W/K. Every numeric threshold/ΔT in `cf2_starter.json` inherits this
   defect and **none may appear in a filing or prophetic example until G_ch is derived properly** (e.g.,
   cold-head strap/joint conductance sized so the load-line is respected at the operating point). Regenerate
   `cf2_starter.json` after the fix.

4. **Add a model-error robustness sweep.** Perturb k / G_ch by ±20–50% between "truth" and "baseline model" to
   show the 3 K margin is not knife-edge and to honestly characterize the outer-turn "neither-detects" cases.
   Real deployments have sparse sensors (the sim assumes one per turn) and nonzero model error (the sim uses an
   exact baseline); the margin must absorb both.

**FTO and China / no-grace-period:**

5. **[MANDATORY] CNIPA-direct verification of CN122194022A and a family / co-pending sweep of the Energy
   Singularity / Xinghuan Junen assignee.** Seen only via secondary source. Given China's effectively-no-grace-
   period rule and this assignee's 2026 filing cadence, any priority filing should precede any enabling
   disclosure of CF-2 anywhere (this engine writes to the private repo only — compliant).

**Coverage gaps to close before a filing-relevant decision:**

6. One direct-database refresh pass — J-PlatPat / KIPRIS / CNIPA / Espacenet (JP/KR especially were seen via
   mirrors only in W1).
7. Dedicated USPTO/WIPO assignee-name search for **Hinetics** (anchor exemplar; potential most-load-bearing art
   or self-collision — flag any user connection to or awareness of Hinetics IP to counsel).
8. Full text of US20190074118A1 ("smart insulation") and EP2624262A2; retry arXiv 2603.29740 extraction.

**Model-served caveat (from the gate run):** the actually-served model for the Fable-5 gates is not verifiable
from inside the session; intended routing `models=GATE:fable-5` is logged, but confirm against the external
transcript (`%USERPROFILE%\.claude\projects\`) before any filing-relevant reliance on the gate verdicts.

---

## 12. Counsel Questions

<!-- Research aid — not legal advice. -->

1. **#9893361 dispositive read:** Once the full text is in hand, does it disclose spatial resolution or a
   cryocooler/cold-head-state model input? If either, does CF-2's independent claim survive, and on what
   distinction?
2. **Element (b)/(c) support:** Is the cryocooler-telemetry-input limitation adequately supported for filing on
   mechanism intent plus the §9 spatial evidence, or must the degraded-cooling differential sim (§11 item 2)
   land first? What is the enablement/§112 exposure of claiming a telemetry-driven baseline without a differential
   example?
3. **Claim mechanism framing:** Are the express "referencing (not forecasting)" and "cryocooler-state (not
   magnet-current)" distinctions strong enough to distinguish #9893361 and #10412643, or should they be
   tightened further?
4. **Scope surrender:** Is surrendering the lumped-forecast genus (§4, §8) acceptable, or is there a defensible
   intermediate claim between the lumped genus and the spatial+telemetry species?
5. **FTO — CN122194022A:** After CNIPA-direct verification, does the Energy Singularity family create an FTO
   concern distinct from the patentability analysis? Does the China-no-grace-period posture change filing
   sequencing?
6. **Hall-sensor exclusion:** Is the §8 carve-out of Hall-effect sensing sufficient to keep CF-2 clear of both
   FSU's US10515749 family and the user's funded Hall-device subject-matter lane (hard rule 1, prong a)?
7. **CF-1 composition (Claim 5):** Does co-disclosing the CF-1 spatial interface-conductance map here create any
   inventorship/ownership entanglement between the two candidates that should be structured deliberately?
8. **Ownership / SU-18:** Given personal-resource development (prong b), does the subject matter (prong a) sit
   clear of any Stanford / sponsor obligation, and is a priority filing warranted before further work?

---

<!-- Research aid — not legal advice. Internal invention disclosure for attorney review only. NOT FILED.
     No document is submitted anywhere by this engine. -->
