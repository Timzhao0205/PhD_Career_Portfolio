# CF-4 Fable-5 Gate Record — "Cold-Head-Budget Ramp Governor"

> **Drafting/analysis aid — not legal advice.** Every verdict below requires registered
> patent attorney review before any filing, disclosure, or reliance. This gate does not
> authorize a filing.

**Candidate:** CF-4 — charge/ramp controller bounding AC + eddy ramp loss to the *measured
instantaneous* cryocooler headroom (live cold-head lift budget) instead of a fixed
worst-case ramp-rate limit.

**Wave:** W3 · **models=GATE:fable-5** (intended) · effort=high · Adjudication date: 2026-07-10
**Evidence reviewed:** `20_SIM/cf4_ramp_governor.py`, `20_SIM/out/cf4_starter.json`,
`60_PRIOR_ART/CF-4/ledger.md`, `60_PRIOR_ART/CF-4/sources.json` (20 tool-verified hits,
incl. JA/ZH/KO-language entries), plus an independent numerical re-execution of the
simulation by this gate (see G-PHYS).

**Model-verification caveat (mandatory):** The intended model for this gate is
`GATE:fable-5`. The **actually-served model is NOT verifiable from inside this session** —
Anthropic safeguards may transparently route some Fable-5 queries to Opus 4.8, and a Fable
self-report is not proof of which model ran. This session was additionally launched with an
explicit harness-level model override after a first launch failed on the literal `fable-5`
identifier (see PROGRESS_LOG W3 entry). Before any filing-relevant reliance on these
verdicts, confirm the served model against the external transcript at
`%USERPROFILE%\.claude\projects\`.

---

## G-PHYS — physics correctness: **REVISE** (effect real; shipped artifact needs three fixes before disclosure use)

**Verified sound:**
1. **No acausality.** The dynamic governor uses only `hd[i]` at the current step
   (`cf4_ramp_governor.py` line 75); no future headroom information leaks into the control
   law. Confirmed by code read, not just output inspection.
2. **Arithmetic independently reproduced.** This gate re-ran the model from scratch:
   headroom min 1.500 W / mean 3.752 W; t_wc = 134.16 s, t_nom = 84.83 s, t_dyn = 94.7 s,
   naive violations = 784 — all match `cf4_starter.json` exactly.
3. **The headline effect is mathematically robust, not a tuning artifact.** With
   q ∝ rate², achievable rate ∝ √headroom. Because √ is concave, the time-average of
   √hd(t) strictly exceeds √min(hd) whenever headroom varies — the dynamic governor's
   advantage over static worst-case follows from Jensen's inequality for ANY time-varying
   headroom curve, not from the particular exponential-recovery + ripple shape chosen.
4. **Units and energy accounting are consistent** (W throughout; q = k·rate² with
   k in W per normalized-rate²; progress = ∫rate·dt against a normalized target).
5. **Robustness probe (this gate, new):** re-simulated with a 20% headroom margin reserve
   (govern to 0.8·hd) AND a 2 s sensor lag: governor completes in 105.3 s — still a
   **21.5% saving vs static worst-case, with 0 true violations**. The effect survives
   realistic de-idealization; this is why the verdict is REVISE, not KILL.

**Defects requiring revision (the fixes):**
1. **`dynamic_governor.violations = 0` is tautological, not a finding.** The control law
   sets q_ramp = hd(t) exactly, so zero violations holds by construction (the code even
   says so in a comment). As shipped, the sim operates at literally zero thermal margin;
   any measurement noise or lag would flip ~half the steps into violation. **Fix:** govern
   to α·hd(t) with α < 1 (e.g. 0.8) and report the saving at that margin; never cite the
   as-shipped "0 violations" as simulated evidence in a disclosure.
2. **Headroom is exogenous.** hd(t) is a prescribed curve; the ramp heat deposited by the
   governor does not feed back into cold-head temperature or subsequent lift. In a real
   conduction-cooled system, a governor consuming 100% of headroom drives the cold-head
   state and hence future headroom. **Fix:** close the loop with a first-order cold-head
   thermal ODE (lift = load-line(T_coldhead), T_coldhead driven by parasitic + ramp load)
   before any parameter-window (ladder rung 5) claim is drafted.
3. **Perfect, instantaneous headroom sensing is assumed.** **Fix:** model sensor/estimator
   latency and error explicitly (this gate's 2 s-lag probe suggests the effect survives,
   but the shipped artifact should demonstrate it).

**Non-blocking note:** the "naive fixed-nominal" comparator is a deliberate strawman
(mean-headroom rate with no safety logic); acceptable as a bounding illustration, but the
disclosure's prophetic example should lead with static-vs-dynamic, which is the fair
comparison. All results remain prophetic/simulated and must be labeled as such per
CLAUDE.md rule 6.

**G-PHYS verdict: REVISE.** Core effect is real and robust (independently confirmed to
survive 20% margin + 2 s lag at 21.5% time saving); the shipped artifact must be revised
per fixes 1–3 before its numbers appear in any disclosure, and no parameter-window claim is
supportable until fix 2 is done.

---

## G-NOVEL — novelty (US + CN + JP + KR + EU): **NARROW-NOVEL**

**Blocking references (patentability — the genus is old):**

- **US6094333A (Sumitomo Electric, US, priority 1997-10-24, expired).** Teaches controlling
  energization of a refrigerator-conduction-cooled HTS coil so that generated heat
  (resistive + AC losses) stays below an "effective cooling curve" derived from the
  refrigerator's **rated** cooling capacity plus measured thermal resistance, with a
  real-time variant that reduces current when monitored temperature/voltage crosses preset
  thresholds. This **anticipates or renders obvious the genus**: "bound coil
  energization/ramp losses to a refrigerator-cooling-capacity constraint." No claim to
  that genus survives.
- **JP2000012326A (Toshiba, JP, priority 1998-06-26, expired).** Claim 4 controls magnet
  power-supply output from a temperature-sensor signal; the system co-adjusts compressor
  inverter frequency and excitation to keep magnetization/demagnetization speed within a
  non-quench range. This **anticipates or renders obvious**: "modulate excitation rate in
  real time from a measured refrigerator/coil thermal-state signal." No claim to
  temperature-feedback ramp modulation as such survives.

**What the art does NOT teach (the surviving sliver):** Neither reference teaches a
controller that (a) **estimates the instantaneous available headroom in power units** —
live lift capability minus present measured load, i.e. a continuously updated watt budget,
as opposed to US'333's precomputed rated-capacity curve or JP'326's temperature signal used
as a coarse margin proxy with threshold/range logic — and (b) **continuously inverts a
stored ramp-loss model q(dI/dt)** each control cycle to solve for the maximum ramp rate
whose *predicted* dissipation tracks a bounded fraction of that live watt budget. US'333 is
feedforward-against-a-static-curve plus reactive threshold trip; JP'326 is temperature-domain
feedback. CF-4's watt-domain, model-inverting, headroom-following law is a distinct
species. That distinction is real but **narrow** — an examiner combining US'333 + JP'326 +
T3-02 (pulse-tube transient-cooling-power measurability, ScienceDirect) has a plausible
obviousness path, so claims must recite the headroom *estimator* and the loss-model
*inversion* as positive limitations, not just "real-time."

**Honest genus assessment:** the idea "don't ramp faster than the fridge can absorb" is
~25+ years old in both US and JP. The value here is entirely in the narrow combination
(live watt-domain headroom estimation + per-cycle loss-model inversion), per the discipline
that value usually lies in a narrow combination, not the genus.

**FTO (distinct from patentability):**
- US6094333A, JP2000012326A, US9014769B2 (Samsung): all **expired** — full novelty-blocking
  force, zero infringement risk.
- **US11094438 / US11551840B2 / WO2017193129A1 (Florida State Univ. Research
  Foundation / NHMFL): ACTIVE through 2037-05-08.** Their claims cover PI feedback control
  driving an NI HTS magnet's supply current so measured field tracks a reference ramping at
  a **fixed predetermined rate**. A CF-4 product on NI coils that implements the governor
  via a field-tracking inner loop could read on these claims. Design-around: CF-4's
  rate setpoint is *derived from measured headroom, not predetermined* — arguably outside
  their literal claim language — but **counsel must read the granted claims of both US
  patents in full** before any NI-coil product implementation; license or avoid
  field-tracking inner loops otherwise.
- US9305691B2 (Toshiba dual-cooling-unit) is active but architecturally distinct; low FTO
  risk for a pure controller.

**Verdict confidence limits:** the W1 ledger has honest gaps — no native CNIPA/J-PlatPat/
KIPRIS/Espacenet-CQL pass, no structured CPC walk, and Fujikura/Furukawa/SuperPower/Bruker/
Siemens Healthineers/MIT got no dedicated assignee pass. Given CLAUDE.md's China
no-grace-period rule, this NARROW-NOVEL is **provisional pending the flagged follow-up
harvest**, and mandatorily re-verified before filing.

**Duty of candor:** US6094333A, JP2000012326A, US9014769B2, US9305691B2, the FSU/NHMFL
family, and all Tier-3/4 entries remain in CF-4's `IDS_pool` and must be disclosed to the
USPTO in any filing. Design-around ≠ concealment.

**G-NOVEL verdict: NARROW-NOVEL** — genus blocked by US6094333A (US) + JP2000012326A (JP);
the live-watt-budget-estimation + loss-model-inversion species survives, subject to the
follow-up-search caveat.

---

## G-CLAIM — survivability + shaping: claim the estimator + inversion, not the genus

**Surviving claim core (one sentence):** A ramp governor for a conduction-cooled
superconducting winding that, in each control cycle, computes an instantaneous
thermal-headroom estimate in power units from measured cryocooler state (cold-head
temperature/trajectory against a characterized load line, minus present measured load) and
sets the winding ramp rate by inverting a stored ramp-loss model q(dI/dt) so that predicted
AC + eddy dissipation continuously tracks a bounded fraction α < 1 of that live headroom —
as distinguished from a precomputed rated-capacity curve (US6094333A) or
temperature-threshold feedback (JP2000012326A).

**Design-around ladder walk:**
1. **Combination/system:** governor + headroom estimator + loss-model inverter + margin
   fraction, as a system claim on a cryocooler-conduction-cooled winding. Strongest rung;
   draft the independent claim here.
2. **Different mechanism:** watt-domain power-balance control vs the art's
   temperature-domain feedback (JP'326) and static-curve feedforward (US'333). This IS the
   novelty argument — recite it structurally (headroom computed in units of power from a
   stored load-line characterization).
3. **Enabling sub-solution:** the real-time headroom *estimator* itself — inferring live
   lift budget of an operating cryocooler from cold-head temperature trajectory + load-line
   model (T3-02 shows transient cooling power is measurable but does not teach an
   estimator-in-the-control-loop). Claim as a dependent method; this is what makes the
   known genus actually work.
4. **Architecture/topology:** (a) NI-winding variant where the loss model includes radial
   bypass-current dissipation and charging-delay dynamics (composes with CF-1/C10;
   distinct from the FSU fixed-rate field-tracking family — and avoid a field-tracking
   inner loop for FTO); (b) rotating-frame conduction-cooled variant (composes with CF-5,
   Hinetics CRUISE-class relevance).
5. **Parameter windows (α margin fraction, estimator update rate):** **NOT SUPPORTABLE
   YET** — the sim provides no criticality evidence and G-PHYS fix 2 (load-coupled
   headroom) is prerequisite. Do not draft rung-5 claims until the revised sim maps the
   α-vs-violation-vs-time-saving trade.
6. **Application-field:** limit to cryogen-free/conduction-cooled windings (already the
   theme); weak for patentability, useful for a CN utility-model parallel filing.

**Recommended adjustment (maximizes grant odds while preserving commercial scope):** Draft
the independent claim at rungs 1+2+3 combined — controller that (i) computes a live
power-unit headroom estimate from measured cryocooler state and a stored load-line
characterization, (ii) predicts ramp dissipation via a stored AC+eddy loss model, and
(iii) each control cycle solves for the maximum ramp rate keeping predicted dissipation
≤ α·headroom, α < 1 — with the estimator and the model inversion as positive limitations,
plus dependents for the NI-loss-model and rotating-frame architectures (rung 4). Write
every rung, including the not-yet-supported rung-5 windows described qualitatively, into
the spec now (no new matter later), but present rung-5 claims only after the revised sim.

**Cost in scope:** this surrenders (a) simple temperature-threshold ramp derating
(JP'326 territory), (b) precomputed-capacity-curve schemes (US'333 territory), and
(c) coarse staged/lookup-table rate schedules keyed to temperature bands — a competitor
could approximate CF-4's benefit with a 3–5-step temperature-banded rate table without
infringing. Acceptable: that surrendered territory is expired art and free to everyone
anyway; the continuous watt-domain governor captures most of the achievable ramp-time
recovery (sim: 29% ideal, 21.5% at realistic margin+lag) and is the commercially
differentiated behavior.

---

## Ownership / hard-rule checks (CLAUDE.md rule 1 — mandatory per-candidate)

- **Prong (a) subject-matter scope:** ramp-rate control of conduction-cooled HTS windings
  vs cryocooler headroom. No overlap with HSX plasma diagnostics, no semiconductor-device
  content, no battery magnetic imaging. **Presumptively outside the funded lane.**
- **Hall-sensing adjacency (explicit flag as required):** the headroom estimator uses
  temperature/power/compressor-state sensors — no Hall sensing in the core. One caution:
  any embodiment that measures magnetic field (e.g. an FSU-style field-tracking inner
  loop) could drift toward Hall-sensor implementations; keep field sensing out of the core
  claims (also helps FTO vs the FSU family) and, if a field-measurement dependent claim is
  ever wanted, route it through counsel first. **No block; adjacency flagged and bounded.**
- Rules 2/3 verified for this document: no prohibited device technology, no prohibited
  application word in patent-facing text (framing is conduction-cooled/cryogen-free HTS
  windings).

---

## Summary block

| Gate | Verdict | One-line reason |
|---|---|---|
| G-PHYS | **REVISE** | Effect real (independently reproduced; Jensen-robust; survives 20% margin + 2 s lag at 21.5% saving) but shipped artifact's 0-violation figure is tautological and headroom is exogenous — apply fixes 1–3 before disclosure use. |
| G-NOVEL | **NARROW-NOVEL** | Genus (bound ramping to refrigerator capacity/temperature) blocked by US6094333A (US) + JP2000012326A (JP), both expired; live watt-domain headroom estimation + per-cycle loss-model inversion survives. Provisional pending flagged CN/assignee follow-up searches. |
| G-CLAIM | **Estimator + inversion core** | Independent claim at ladder rungs 1+2+3 (power-unit headroom estimator + loss-model inversion + α<1 margin); NI and rotating-frame dependents; rung-5 windows deferred until revised sim; surrenders temperature-banded/staged schemes (expired-art territory anyway). FSU/NHMFL family (active to 2037) needs counsel FTO read before any NI field-tracking implementation. |

**Disposition:** CF-4 proceeds to W4 disclosure drafting as a NARROW-NOVEL survivor,
conditioned on (a) the G-PHYS sim revisions before any prophetic example cites governor
safety numbers, and (b) counsel review of the FSU/NHMFL granted claims. All verdicts are
drafting/analysis aid only — registered patent attorney review required; this gate
authorizes no filing.
