# Fable-5 Gate Record — CF-2: Thermal-Margin-Aware Quench Detection

> **Drafting/analysis aid — not legal advice. Registered patent attorney review required
> before any filing, disclosure, or reliance. This record authorizes nothing.**

**Candidate:** QD trip thresholds referenced to a conduction-cooled temperature map
(cryocooler-state telemetry + conduction thermal model of the winding), instead of a fixed
bath-pinned threshold.

**Wave:** W3 · **models=GATE:fable-5** (intended) · effort=high · ts=2026-07-10
**Evidence reviewed:** `20_SIM/cf2_quench_margin.py`, `20_SIM/out/cf2_starter.json`,
`20_SIM/thermal_network.py`, `20_SIM/out/cf1_starter.json` (KNOWN_ISSUES),
`60_PRIOR_ART/CF-2/ledger.md`, `60_PRIOR_ART/CF-2/sources.json`.

**Model-verifiability caveat (mandatory):** The actually-served model for this gate run is
NOT verifiable from inside this session — Anthropic safeguards may transparently route some
Fable-5 queries to Opus 4.8, and a Fable self-report is not proof of which model ran. The
intended routing (`GATE:fable-5`) is logged; confirm against the external transcript at
`%USERPROFILE%\.claude\projects\` before any filing-relevant decision relies on these verdicts.
(Note also the prior W3 log line: the first launch failed hard on the literal "fable-5"
identifier and was relaunched with the harness enum value — the external transcript is the
only authority on what actually served.)

---

## G-PHYS — Physics correctness: **REVISE**

**What the sim actually shows (verified against the code, not the summary text):**
The model is a linear 1-D radial conduction network (constant k, one node per turn, cold-head
sink at the OD through conductance G_ch). Superposition is exact for this network, so the
baseline-profile construction (N single-injection solves summed) is legitimate. A 0.30 W
fault pulse at each of 30 turns × 3 cooling levels is compared under two trip rules:
fixed rule trips on `T(fault turn) − T_cold > 11.224 K` (calibrated once at 20 K as
max-baseline-ΔT + 3 K); local rule trips on `T(turn) − baseline(turn) > 3 K`. Result:
17/90 fault cases caught only by the local rule, 0 false trips by either rule.

**Is the local rule cheating (using information a real instrument couldn't have)?**
No — with one honest idealization. The local rule uses only (a) a measured temperature at the
fault location and (b) a model-predicted no-fault baseline for that same location. Both are
realizable: (a) is a temperature sensor, (b) is exactly what the claimed conduction model +
cryocooler-state input computes. Critically, the FIXED rule is given the *same* dense per-turn
sensing (`Tf[spot_turn] − T_cold`), so the comparison isolates the thresholding logic, not the
sensor count — that is the fair way to run this test. The sim is even generous to the
incumbent: a real "fixed" instrument calibrated at 20 K would more plausibly hold an absolute
trip temperature, which would false-trip wholesale at 50 K operation; the sim re-references
the fixed rule to the current T_cold, understating the advantage. The idealization to flag:
sensors are assumed at every turn, and the baseline model is *exact* (the same network
generates truth and baseline, so model error = 0). Real deployments have sparse sensors and
model error that the 3 K margin must absorb.

**Sign/units/conservation checks:**
- Conductance matrix assembly, sink boundary (`q[N−1] += G_ch·T_cold`), and cold-head load
  (`G_ch·(T[N−1]−T_cold)`) are correctly signed; hotter inner turns, monotone decay toward
  the OD sink — physically sensible for an OD-cooled pancake.
- CF-1's KNOWN_ISSUES tau↔Rc item does **not** contaminate CF-2: `electrical_tau()` (the
  function carrying that issue) is never called here; CF-2 uses only `thermal_solve()` and
  `cooling_budget()`. The flagged issue was a narrative/label inversion, and the formula
  direction (higher rho_ct → shorter tau) is the textbook NI/MI result; either way it is
  orthogonal to CF-2's headline. Checked and cleared.
- **Units defect (must fix): `cooling_budget()` returns a lift budget in W (20 K→1.0 W,
  30 K→4.0 W, 50 K→20 W) but is consumed directly as G_ch in W/K.** Watts are not W/K. This
  is inherited from CF-1's starter. The *qualitative* headline survives it (see below), but
  every numeric threshold/ΔT in `cf2_starter.json` depends on this conflation and none of
  those numbers may appear in a filing or prophetic example until G_ch is derived properly
  (e.g., cold-head strap conductance sized so the load-line is respected at the operating
  point).

**Does the headline depend on the units error?** No, qualitatively. The 17 misses are turns
18/19–23 at *every* cooling level — they are driven by the radial position gradient (fault near
the well-cooled OD produces a small absolute ΔT that hides under a threshold calibrated at the
worst-case inner turn), which persists for any positive G_ch. So the effect is real, not an
artifact of the units slip.

**Why REVISE and not PASS — the bigger gap:** the sim as run demonstrates the *spatial-map*
half of CF-2 but barely exercises the *cryocooler-state-telemetry* half, which is exactly the
element G-NOVEL below leans on. Across the three cooling budgets the miss set is nearly
identical (5/6/6) and false trips are 0/0 everywhere — so there is currently **no simulated
case where tracking cryocooler state (rather than turn position) changes the outcome**. A
claim limitation supported by zero differential evidence is exposed.

**Required fixes (then PASS is expected):**
1. Fix the G_ch units: derive W/K from a physical strap/joint model consistent with the W
   lift budget; regenerate `cf2_starter.json`.
2. Add a degraded-cooling scenario (G_ch reduced 2–5× at fixed nominal T_cold, and/or T_cold
   drifting upward as cryocooler capacity fades) and show (a) the fixed rule false-trips on
   the shifted no-fault baseline or misses under recovered margin, while (b) the
   telemetry-referenced rule tracks it. This is the evidence that makes the cryocooler-telemetry
   limitation more than decoration.
3. Add a model-error robustness sweep (perturb k / G_ch by ±20–50% between "truth" and
   "baseline model") to show the 3 K margin is not knife-edge — and to honestly characterize
   the 18 "neither-detects" outer-turn cases (defensible — those locations are best-cooled and
   a 0.3 W pulse yields <3 K local rise — but say so explicitly rather than leaving it silent).

All outputs remain labeled SIMULATED/prophetic; no measured data is blended. Number-truth
discipline satisfied except for the G_ch units sourcing (fix #1).

---

## G-NOVEL — Novelty across US + CN + JP + KR + EU: **NARROW-NOVEL (conditional)**

*Full ledger reviewed including CN/JP/KR-language hits and the non-patent literature.*

**The broad genus is not available.** "Model-based / cooling-condition-aware temperature
trigger for quench protection of a conduction-cooled HTS magnet" is at minimum rendered
obvious — and possibly anticipated — by:

- **IEEE Xplore #9893361, "A Quench Protection Method for HTS Coils Based on Temperature Rise
  Forecast" (2022, NPL — worldwide patentability effect in all five jurisdictions of
  interest).** This is the closest art. It targets conduction-cooled HTS coils, uses a
  predictive temperature-rise model as the protection trigger, and is validated under
  "poor refrigeration conditions" — i.e., the trigger behavior is refrigeration-state-dependent
  in effect. **Answering the posed key question:** on the abstract-level information available,
  #9893361 forecasts a (apparently lumped, coil-level) temperature-rise *trajectory* driven by
  measured operating quantities and trips on the forecast; it does **not** appear to disclose
  (i) a *spatially resolved* per-location temperature/thermal-margin map of the winding,
  (ii) **live cryocooler-state telemetry** (cold-head temperature, compressor/motor state,
  load-line position) as an explicit model input, or (iii) *per-sensor trip thresholds
  recomputed as that location's modeled no-fault baseline + margin*. That tri-part combination
  is the gap CF-2 can occupy. **HARD CONDITION: the full text of #9893361 has not been
  obtained. This verdict is provisional and MUST be re-run after full-text review** — if the
  paper's model internally uses cryocooler/cold-head state as an input or resolves the winding
  spatially, the gap narrows to nothing and the verdict falls to DUPLICATED. Do not draft
  claims that survive only if the abstract is the whole story.
- **IEEE #10412643 (2024, digital-twin overcurrent QD for NI coils):** establishes real-time
  model-referenced trip logic for NI HTS coils as known; its modeled quantity is
  electromagnetic (current/inductance), not a thermal-margin map — it fences the genus further
  but does not reach the gap.

**The fixed-threshold patent field is contrast art, not blocking art:** US11101059B2 and
US11190006 (Tokamak Energy), US7876100B2 (GE), GB2514372A, US7649720B2 and US10515749/
US11217373 (FSU), US12578370B2 (U. Houston), CN102214911B (IEE-CAS), CN101446610B (CEPRI),
and pending CN122194022A (Energy Singularity / 星环聚能) all trip on *static/preset*
thresholds (voltage, current-imbalance, diode-gated, or bridge-comparator), even where the
magnet is explicitly cryocooler-cooled. They uniformly support the existence of the gap while
proving the problem space is heavily patented — CF-2's independent claim must be a combination,
not a genus.

**Patentability vs FTO — kept distinct:**
- *Patentability:* the operative blocker is NPL #9893361 (plus #10412643). NPL blocks claims;
  it can never block a product. Adjust claims around it (G-CLAIM below).
- *FTO:* no in-force claim found in this harvest reads on cryocooler-telemetry-referenced
  thresholds. **CN122194022A is the live FTO watch item:** a currently-filing Chinese HTS
  fusion-magnet assignee (filed ~04/2026, seen only via a secondary source) whose pending or
  undisclosed co-pending applications could mature into CN claims. Mandatory before any
  filing decision: CNIPA-direct verification of CN122194022A and a family/co-pending sweep of
  this assignee. Given China's effectively-no-grace-period rule and this assignee's cadence,
  any priority filing should precede any enabling disclosure of CF-2 anywhere (this engine
  writes to the private repo only — compliant).
- US20190074118A1 (MIT-material "smart insulation"): passive fixed-physical-temperature phase
  transition, not telemetry-driven recompute — adjacent only; fetch full text for the IDS.

**Coverage caveats carried into this verdict:** no direct CNIPA/J-PlatPat/KIPRIS/Espacenet
session in W1 (CN/JP/KR seen via mirrors only); #9893361 abstract-only; CN122194022A
secondary-source only. NARROW-NOVEL is therefore conditional on: (1) #9893361 full text,
(2) CNIPA-direct check of CN122194022A + assignee sweep, (3) one direct-database refresh pass
(JP/KR especially) before any filing-relevant decision.

**Duty of candor:** every reference above, including #9893361, #10412643, and CN122194022A —
the items that most hurt CF-2 — stays in the IDS_pool and goes to counsel. Design-around is
claim-shaping in view of the art, never concealment of it.

**Prong-a ownership check (hard rule 1):** CF-2 as scoped uses temperature sensors and
cryocooler telemetry — no HSX plasma-diagnostic, GaN/AlGaN, or battery-magnetic-imaging
subject matter. One adjacency flag: FSU's US10515749 family uses **Hall-effect sensors** for
quench detection. CF-2 must not claim or exemplify Hall-sensor-based detection (also avoids
the funded Hall-device lane entirely); keep embodiments to temperature/voltage sensing.
No GaN, no prohibited framing terms in any patent-facing text. Cleared with that constraint.

---

## G-CLAIM — Survivability and shaping (NARROW-NOVEL ⇒ gate runs): **SHAPED — combination claim as below**

**Surviving claim core (one sentence):** A quench-detection system for a conduction-cooled
HTS winding in which each of a plurality of sensing locations has its trip threshold
continuously recomputed as that location's model-predicted no-fault baseline — produced by a
conduction thermal model of the winding driven by live cryocooler-state telemetry — plus a
margin, so that trip sensitivity tracks both spatial position in the winding and the
instantaneous cooling state, rather than any fixed or bath-referenced setpoint.

**Design-around ladder walk:**
1. *Combination/system (STRONGEST — recommended independent claim):* cryocooler +
   telemetry interface + conduction thermal model + spatially distributed sensors +
   per-location baseline-referenced comparator + protective action (dump / co-wound heater /
   current derate). No single reference has this combination; #9893361 lacks (at abstract
   level) the spatial map and the telemetry input; the patent field lacks any dynamic
   referencing at all.
2. *Different mechanism (vs #9893361):* threshold *referencing* — subtract the modeled
   per-location baseline from the measurement — rather than forward-*forecasting* a
   temperature-rise trajectory; and telemetry input = cryocooler operating state rather than
   magnet current. Write both distinctions expressly into the independent claim and spec.
3. *Enabling sub-solution:* the cheap per-location baseline update on cooling-state change
   (linear-superposition map recompute, as the sim demonstrates) and false-trip suppression
   during cryocooler ramp/degradation transients. Claim as dependents; this is what makes the
   known "adaptive threshold" idea actually work on a resource-limited magnet controller.
4. *Architecture/topology:* (a) NI/MI-winding-specific embodiment where the threshold map is
   co-designed with a spatial interface-conductance map (composes with CF-1 — a genuinely
   fresh combination); (b) rotating-frame embodiment (telemetry across the rotary coupling)
   for conduction-cooled motor field coils. Dependents / divisional seeds.
5. *Parameter windows:* **DO NOT CLAIM YET.** The current sim has a units defect and no
   criticality evidence (no sweep showing a margin window is critical). Only after G-PHYS
   fixes 1–3 produce criticality data may a numeric window (e.g., margin as a function of
   telemetry-indicated headroom) be claimed.
6. *Application-field limitation:* conduction-cooled aviation-motor / MRI-insert windings —
   weak for patentability; hold in reserve for FTO positioning and a possible CN utility-model
   parallel filing.

**Recommended adjustment (maximizes grant odds while preserving commercial scope):** draft the
independent claim at rung 1 with the rung-2 distinctions as express limitations — i.e., require
(i) a plurality of sensing locations, (ii) a conduction thermal model of the winding,
(iii) cryocooler-state telemetry as a model input, and (iv) per-location trip thresholds equal
to the modeled local baseline plus a margin. Pre-build rungs 3, 4, and 6 into the spec as
dependents/embodiments now (no new matter later).

**What this costs in scope:** the genus of "any model-based or adaptive QD threshold" is
surrendered — a competitor using a lumped, current-driven temperature-rise forecast exactly as
in #9893361 escapes the claim. That genus was almost certainly unpatentable over the NPL
anyway, so the real commercial cost is modest: the protected space is the spatial +
telemetry-referenced implementation, which is the version a limited-cooling-power
(cryogen-free) product actually needs. Accept the cost.

**Gate-order note:** G-CLAIM's recommendation is conditioned on G-PHYS fixes 1–2 landing
(the telemetry limitation currently has no differential sim evidence) and on the G-NOVEL
hard conditions (#9893361 full text; CNIPA verification). If #9893361's full text discloses
spatial resolution or cryocooler-state input, re-run G-NOVEL and G-CLAIM before drafting.

---

**Summary line:** G-PHYS=REVISE (real effect; fix G_ch W-vs-W/K units + add degraded-cooling
and model-error sweeps) · G-NOVEL=NARROW-NOVEL (conditional on #9893361 full text + CNIPA
check of CN122194022A) · G-CLAIM=combination claim: spatial per-location baseline-referenced
thresholds from a cryocooler-telemetry-driven conduction model; parameter-window rung
embargoed pending sim criticality evidence.

*All verdicts are drafting/analysis aid only — registered patent attorney review required;
this engine files nothing.*
