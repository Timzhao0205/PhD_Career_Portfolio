# CF-5 Gate Record — Rotating-frame heat extraction for NI motor coils

> **Drafting/analysis aid — registered patent attorney review required.** Nothing in
> this record authorizes a filing. Research aid, not legal advice.

**Candidate:** CF-5 — thermal architecture removing heat from a spinning
conduction-cooled NI HTS winding within a fixed cooling-power budget. Anchor exemplar:
Hinetics CRUISE-class conduction-cooled aviation-motor field coils. Aviation-motor
context only.

**Gate run:** W3, 2026-07-10. `models=GATE:fable-5` (intended).

**Model-verification caveat (mandatory):** The actually-served model is NOT verifiable
from inside this session — Anthropic safeguards may transparently route some Fable-5
queries to Opus 4.8, and a Fable self-report is not proof of which model ran. Confirm
against the external transcript at `%USERPROFILE%\.claude\projects\` before any
filing-relevant reliance on these verdicts.

**Evidence reviewed:** `20_SIM/cf5_rotating_frame.py`, `20_SIM/out/cf5_starter.json`,
`20_SIM/thermal_network.py` (`cooling_budget` only), `60_PRIOR_ART/CF-5/ledger.md`
(33 hits, Tiers 1–4, incl. CN/JP/KR-language art).

---

## G-PHYS — Physics correctness: **PASS** (with scope limits binding on W4)

**Model:** series chain dT(RPM) = Q_budget(T_cold) × [R_winding_fixed +
R_joint0·exp(RPM/RPM_char)]. Units check (K/W × W = K): correct. Sign/coupling
direction: correct — larger R at fixed Q gives larger dT; no inverted coupling.
Energy bookkeeping of a lumped steady-state series chain: trivially conserved.
CF-1 tau↔Rc bug: **not inherited** — cf5 imports only `cooling_budget()`, a static
{20 K: 1 W, 30 K: 4 W, 50 K: 20 W} interpolation with no tau or Rc dependence.

**Direction defensibility.** Joint conductance degrading with RPM (contact-pressure
loss, gap growth, runout) is physically defensible **for contact/solid-conduction
rotary interfaces only**. It is NOT general: gas-gap/convective couplings (T3-06 Gas
Blow Coupling; T1-05 interleaved-fin gap) and centrifugally-driven circulation
(T1-06) can *improve* with RPM, and a fully co-rotating cold head (T1-01 Hinetics,
T1-11, T1-12) has no rotating thermal interface at all, so the modeled speed ceiling
does not exist in that architecture. The sim characterizes one architecture class,
not the problem space.

**Prophetic labeling audit: compliant.** `SIMULATED_prophetic: true`; the exp()
parametrization is explicitly labeled "illustrative monotonic contact/gap-degradation
curve … not a measured rotary-joint or heat-pipe test result"; RPM_char, R values,
and the 5 K margin are all flagged prophetic/illustrative with units; console output
is prefixed `[SIMULATED/prophetic]`. Hard rule 6 satisfied.

**Binding limits (carry into any disclosure):**
1. The RPM-degradation effect is an **input assumption, not a simulation result** —
   the sim is arithmetic on an assumed R(RPM). It therefore provides ZERO criticality
   evidence for parameter-window claims (design-around ladder rung 5 is unavailable
   for CF-5 on this evidence). The crossing RPMs (17300 / 9900 / 3700 at 20/30/50 K)
   are artifacts of the unmeasured RPM_char=6000 and must never appear as design
   values or claim limits.
2. Q_budget conflates cryocooler lift *capacity* with actual heat *load* — a worst-case
   proxy, acceptable for a trend plot, not for sizing.
3. Model validity fails long before the 50 K curve's dT_max = 171 K (constant R and Q
   over a ~170 K span is not credible; the winding would be far above any HTS operating
   point). Only the low-dT region is meaningful even as a trend.

Verdict: PASS as a correctly-signed, correctly-labeled illustrative trend model for
contact-joint embodiments; no headline number is load-bearing.

---

## G-NOVEL — Novelty (US + CN + JP + KR + EU): **DUPLICATED**

CF-5 as scoped — "thermal architecture removing heat from a spinning conduction-cooled
NI winding within a fixed cooling budget" — is an architecture-genus claim, and the
genus is comprehensively occupied on **both** sides of the design space, across
multiple jurisdictions, including by the anchor exemplar itself:

**Blocking references (specific):**
- **US 12,506,395 B2 (Hinetics LLC, priority 2021-03-16, granted 2025-12-23, US,
  ACTIVE)** — the anchor company's own patent: rotating cryocooler cold end through a
  hollow driveshaft, radial thermally-conductive straps to the rotor shell. This is
  CF-5's target architecture, verbatim. Companion **US 12,531,457** (high-confidence
  same family; assignee unverified — image-only PDF, manual re-pull required) adds
  flexible straps accommodating cooldown contraction, pre-empting the sim's own
  proposed mitigation ("compliant/redundant joint design").
- **CN 102840708 B (Dongfang Electric, priority 2012-09-29, CN, ACTIVE to ~2032)** —
  rotating two-stage cold head fed via rotary helium seal, second stage conducting to
  the SC magnet via Cu/Al thermal straps. Architecturally near-identical, 9 years
  before Hinetics' priority.
- **WO 2013/133487 A1 (Hyundai Heavy Industries, priority 2012-03-07, KR-origin PCT,
  ceased; national-phase fate unconfirmed)** — 3-stage GM cryocooler mounted inside
  the rotor, copper conduction elements to the SC wire. Same core mechanism, also a
  decade pre-Hinetics. Even if no in-force member survives, it is prior art against
  patentability everywhere.
- The **stationary-cold-head-plus-rotating-interface** variant (the one the CF-5 sim
  actually models) is equally blocked as prior art: US 6,812,601 B2 (AMSC, gas-gap fin
  coupling, expired), US 6,597,082 B1 (AMSC, teaches keeping the cryocooler stationary,
  expired), DE 199 38 986 B4 (1999 priority, cold head in rotor + ferrofluid coupling,
  expired), EP 3104100 B1 (Sumitomo Heavy Industries, staged-seal rotary joint,
  **EP ACTIVE to 2036**), US 2012/0133126 A1 (cryo-rotary joint, magnetic-fluid seal).
  NPL (T3-04, T3-05 KAIST ~2006) shows on-board rotating cryocoolers demonstrated
  20 years ago.

**Patentability vs FTO — keep these separate:**
- *Patentability:* the expired AMSC/DE art plus the two 2012 CN/KR references block
  any claim to the genus (rotating cold head OR stationary cold head + rotary thermal
  interface, with straps) in every one of US/CN/JP/KR/EU. Adding "NI winding" or
  "aviation motor" alone is an application-field limitation (ladder rung 6) — weak,
  and obvious over Hinetics '395 which already IS an NI-adjacent aviation motor.
- *FTO:* US 12,506,395 B2 (in force, ~2041 horizon), CN 102840708 B (in force in CN
  to ~2032), and EP 3104100 B1 (in force in EP to 2036) are live FTO constraints on
  any product practicing these architectures in those jurisdictions. Note the '395
  holder is the anchor exemplar / prospective commercial partner: the rational path
  for the genus is license/partnership, not filing over their own architecture.

**What, if anything, remains undisclosed (honest residue):** None of the 32 IDS_pool
references co-designs the rotating-frame thermal path with **NI-specific turn-to-turn
electrical behavior** (Rc / charging delay / bypass-current heating as a function of
where the strap contacts land on the winding — the CF-1 insight moved into the
rotating frame), and none discloses **RPM-scheduled thermal-margin management**
(sensing or scheduling operating current/ramp against an RPM-dependent joint
conductance model — the CF-2/CF-4 composition). Those are genuinely absent from the
ledger. But they are *different inventions*, not CF-5: CF-5's stated core is the heat
-extraction architecture itself, and that is old. Verdict for CF-5 as scoped:
**DUPLICATED**. Recommendation: kill CF-5; if desired, spin the residue as a new
candidate (CF-5b, "NI-aware rotating-frame thermal co-design / RPM-scheduled margin
governor") and send it back through W1 harvest and W2 simulation on its own merits —
do not smuggle it through under CF-5's gate record.

**Duty of candor:** all 32 Tier 1–3 hits remain in CF-5's IDS_pool and must accompany
any successor candidate's disclosure that builds on this record.

---

## G-CLAIM — Claim survivability: **NOT REACHED** (prerequisite failed: DUPLICATED)

Per gate rules G-CLAIM runs only on NOVEL/NARROW-NOVEL candidates. For completeness,
the shaping note that would apply to a successor candidate: the only ladder rungs with
life are rung 3 (enabling sub-solution: NI turn-to-turn/strap-landing co-design that
makes rotating-frame conduction cooling actually work for an NI coil) and rung 1
combined with CF-2/CF-4 (system claim: rotor + joint-conductance model + RPM-scheduled
current/ramp governor). Rung 2 (different mechanism, e.g. gas-blow coupling) is blocked
by T3-06/T1-05; rung 4's "compliant strap" topology is narrowed by US 12,531,457;
rung 5 is unavailable on current evidence (see G-PHYS limit 1); rung 6 is worthless
here. Cost: any survivor is a narrow improvement patent that likely still needs a
license under Hinetics '395 for US practice — patentability ≠ FTO.

---

## Hard-rule compliance check

- **Prong-a (ownership scope):** CF-5 is aviation-motor rotor thermal architecture —
  presumptively OUTSIDE the funded lanes (HSX plasma diagnostics, GaN/AlGaN Hall-effect
  devices, battery magnetic imaging). Explicit Hall-sensing adjacency check: the CF-5
  sim and all reviewed embodiments contain **no sensing element at all** (pure passive
  thermal architecture); no Hall-effect measurement appears anywhere in the candidate
  or ledger. **No adjacency flag.** Caution forward: a CF-5b variant adding
  *rotor-frame field/current sensing* should be re-checked at that time; prefer
  temperature/voltage-tap sensing framings.
- **No GaN** in any CF-5 text: confirmed.
- **Forbidden application word:** absent from this record and from the CF-5 sim/ledger
  patent-facing text: confirmed.
- **No outreach/posting/filing:** none performed; record written to private repo only.

**Verdicts:** G-PHYS = PASS (illustrative-trend scope only) · G-NOVEL = DUPLICATED ·
G-CLAIM = not reached. CF-5 does not advance to W4.
