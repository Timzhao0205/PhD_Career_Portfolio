# W3 Fable Gates — CF-1: Dual-function turn-to-turn interface

> **Drafting/analysis aid — registered patent attorney review required.** This record
> authorizes no filing. All references cited here are in the CF-1 `IDS_pool`
> (duty of candor; design-around ≠ concealment).

- **Candidate:** CF-1 — spatial map jointly setting turn-to-turn contact resistance
  (Rc) and radial thermal conduction to the cold head in a conduction-cooled NI HTS
  pancake, targeting a Pareto front no uniform interface can reach.
- **Date:** 2026-07-10 · **Adjudicator stage:** W3 · `models=GATE:fable-5` (intended)
- **Evidence reviewed:** `20_SIM/thermal_network.py`, `20_SIM/out/cf1_starter.json`
  (incl. KNOWN_ISSUES), `60_PRIOR_ART/CF-1/ledger.md` + `sources.json` (all tiers,
  incl. non-English hits), `10_MISSION/MISSION.md`.
- **Independent numeric verification performed** (not accepting W2's own reasoning):
  re-derived R_char by hand for cu/ss, re-ran `thermal_solve` across G_ch ∈
  {0.1, 1, 4, 20} W/K and T_cold ∈ {20, 30, 50} K, recomputed the Pareto front on
  **unrounded** values, and swept the disturbance location (spot_turn 5 vs 20).

### Model-identity caveat (mandatory)
Intended model logged as `models=GATE:fable-5`. The actually-served model is **not
verifiable from inside this session** — Anthropic safeguards may transparently route
some Fable-5 queries to Opus 4.8, and a Fable self-report (this session self-reports
`claude-fable-5`) is **not proof** of which model ran. Confirm against the external
transcript at `%USERPROFILE%\.claude\projects\` before any filing-relevant reliance
on these verdicts.

### Hard-rule compliance check
Prong-a (ownership): CF-1 is coil interface thermal/electrical co-design — no HSX
plasma-diagnostics, no GaN/AlGaN, no battery magnetic imaging, and **no Hall-sensing
adjacency** (no sensing element anywhere in the candidate). Presumptively outside the
funded lane; counsel confirms. No GaN, no "stellarator" in any patent-facing text here.

---

## G-PHYS — physics correctness: **REVISE (passable to G-NOVEL)**

### The flagged tau<->Rc direction: W2 fix is CORRECT
The KNOWN_ISSUES entry (`tau_rc_narrative_direction`) was adjudicated independently:

1. **Formula direction verified by hand.** tau = L/R_char with R_char = Σ
   rho_ct/(2π·r_i·w) over the 29 interfaces. Hand recomputation: cu → R_char =
   1.828e-4 Ω, tau = 0.596 s; ss → R_char = 7.310e-2 Ω, tau = 0.0015 s. Units check:
   [Ω·m²]/[m²] = Ω; H/Ω = s. Matches the JSON exactly. Higher rho_ct → higher
   R_char → **shorter** tau.
2. **Direction matches physics and the published record.** In the NI lumped-circuit
   model the charging delay is the L/R time of the radial bypass path; raising the
   turn-to-turn resistance speeds field settling. This is precisely why
   metal-insulation (stainless co-wound) coils were introduced — to shorten the
   notorious charging delay of bare-contact NI coils (Hahn et al. NI/MI literature;
   Bonura 2019, ledger T3-2, gives the Rc data family). The W0 narrative ("uniform
   stainless gives the LONGEST tau") was the inversion; **W2 correctly fixed the
   narrative to match the formula, not vice versa.** The headline effect does not
   depend on an unresolved sign or units error in this coupling.
3. **Conservation verified.** `cold_head_load` = q_spot = 0.5 W **exactly**, for every
   G_ch and T_cold tested (0.1–20 W/K; 20–50 K), and scales with q_spot (0.3 W in →
   0.3 W out). This is correct, not suspicious: at steady state the cold-head link is
   the model's only sink, so all injected power must exit there regardless of
   G_ch/T_cold — those parameters set temperatures, not the through-power. The
   G-matrix stamping and the Dirichlet-via-conductance boundary (q[N-1] += G_ch·T_cold)
   are standard and sign-correct; peak ΔT falls monotonically as G_ch rises (13.05 K
   at 0.1 W/K → 8.55 K at 1 W/K for uniform ss), as it must.

### Why REVISE, not PASS — three fixes required before filing-grade reliance
- **R1 (rounding artifact in the headline Pareto claim).** On **unrounded** values,
  `uniform:ss` (tau 0.001491 s, ΔT 8.546 K) is **not dominated** by
  `spatial:ss-core/cu-drain[2]` (tau 0.001542 s, ΔT 7.671 K) — the JSON's exclusion
  of uniform:ss from the front comes from rounding tau to 4 decimals. The defensible
  statement is: spatial maps strictly dominate uniform **cu, brass, and hast** and
  populate non-dominated intermediate trade points (e.g. cu-drain[10]: 280× shorter
  tau than uniform cu at identical 0.560 K peak ΔT) that **no uniform interface
  reaches**; uniform ss survives only as the extreme min-tau corner. Fix: compute the
  front on full-precision values and restate the acceptance claim accordingly.
- **R2 (cooling budget is decorative — units conflation).** `cooling_budget()` returns
  a lift budget in **W**, but it is used directly as `G_ch` in **W/K**. Worse, since
  the steady-state load always equals q_spot = 0.5 W < every budget level, the "fixed
  cooling-power budget" **never binds** — the three cooling levels differ only through
  the 0.5/G_ch temperature drop. The claim "Pareto front under a fixed cold-head
  power budget" is not yet evidenced. Fix: enforce the budget as a constraint (e.g.
  background + AC-loss load approaching Q_budget, or T_cold rising along the
  load-line as load grows) with dimensionally distinct G_ch.
- **R3 (disturbance-location robustness).** With the hot spot moved to inner turn 5,
  the ss-core/cu-drain[10] map gives peak ΔT = 14.5 K (vs 0.56 K when the spot sits
  inside the drain zone) — the advantage is spot-location dependent because the inner
  ss core lies on the heat path. Fix: evaluate worst-case over spot_turn (or a
  disturbance-probability map) before asserting the Pareto claim; this also directly
  feeds any parameter-window (ladder rung 5) claim.
- Noted limitations (acceptable for a starter, disclose in the prophetic examples):
  radial-only 1-D network; interface thermal resistance proxied by interlayer bulk k
  over pitch (no true contact resistance); no Joule heating from bypass currents
  during ramp; temperature-independent k; min(k) interface pairing is a crude but
  conservative choice.

**Verdict: REVISE.** The core coupled effect (one material choice sets both Rc and
the radial thermal drain; a designed radial map reaches trade points no uniform
interface reaches) is **real, sign-correct, and conservation-consistent** — passable
to G-NOVEL. R1–R3 must land before any disclosure quotes the Pareto numbers or any
parameter window.

---

## G-NOVEL — novelty (US + CN + JP + KR + EU): **NARROW-NOVEL**

### The genus is taken
- **EP4078630A1 / WO2021122522A1 (Tokamak Energy, EP granted, active).** Explicitly
  teaches that by varying regions/connections of a partially insulating turn-to-turn
  layer, "the thermal properties of the partially insulating layer can be varied
  **independently of the electrical properties**," and separately teaches
  **circumferential** variation of effective inter-turn resistance (l/lc-triggered
  regions). This kills any broad claim to "engineering electrical and thermal
  properties of the turn-to-turn interface non-uniformly / independently."
  **Blocking jurisdiction: EP (in force).**
- **US11101060B2 (Tokamak Energy, granted 2021, active; family EP4012730A1,
  WO2019150123A1, JP national phase, KR102631117B1 per CF-3 ledger).** Windowed
  partially-insulating layer with spacing varied along the coil; also a
  metal-insulator-transition (VO2-class) interface. **Blocking jurisdiction: US
  (in force), plus EP/JP/KR/AU family.** Note its spatial variation is aimed at
  keeping per-turn resistance **constant** — the opposite design goal from CF-1's
  deliberate radial gradient — but as 103/inventive-step art it still teaches
  spatially programming the same interface layer.
- **Wang/Hahn "graded-resistance" NPL (IEEE TAS ~2017; exact citation unconfirmed —
  ledger gap #5 MUST be closed before filing).** Patterned resistive-conductive
  layers at **selected** turn-to-turn contacts — a designed, non-uniform Rc map. Its
  objective is hot-spot containment / field preservation / self-protection, **not** a
  cryocooler cold-head power budget, and it does not co-optimize thermal conductance
  to a cold head. Prior art for patentability (NPL blocks claims, not products — no
  FTO effect).
- **US20060071747A1 (Bar-Ilan/RICOR, abandoned).** States CF-1's conduction-cooled
  turn-to-turn thermal-bottleneck problem almost verbatim, solves it **uniformly**
  (ceramic-filled epoxy). Abandoned status makes it weak as a blocker but it remains
  prior art for the problem statement and is 103 motivation-to-combine fuel:
  "conduction-cooled coils need better turn-to-turn thermal paths" is on the record
  since 2004.
- KR101665038B1 (KBSI, granted, KR): uniform conductive impregnation — confirms
  uniform interface engineering is old in KR too. T2-2/US12196792 and T3-3: spatial
  Rc **measurement/as-built variability**, not designed maps — distinguishable but
  belongs in the IDS_pool (already there).

### Does the claimed differentiator survive? Yes — narrowly
No single reference discloses CF-1's combination: (i) a **designed radial** map
(inner high-Rc charging zone → outer high-conductance drain to the cold head), (ii)
of a **coupled-property** interface (one material/pressure choice sets both Rc and k
— the opposite premise from Tokamak's independent-decoupling-via-bridges mechanism),
(iii) jointly optimized against a **cryocooler cold-head budget** in a cryogen-free
coil, (iv) with Pareto evidence. Tokamak varies circumferentially or to homogenize;
Wang/Hahn grades for self-protection with no cold-head/thermal-drain objective;
Bar-Ilan is uniform. The honest assessment: **the value is in this narrow
combination, not the genus** — a broad "spatially non-uniform turn-to-turn interface"
claim is DUPLICATED; the radial/coupled/cold-head-budget combination is novel but
sits one KSR-style motivation argument away from a 103 (Wang/Hahn's spatial grading +
Bar-Ilan's conduction-cooled thermal motivation + Tokamak's interface engineering).
Non-obviousness will need the objective evidence the sim is supposed to supply —
which is why G-PHYS R1–R3 matter.

### Patentability vs FTO (do not conflate)
- **Patentability:** the art above shapes/blocks claim breadth → adjust claims (G-CLAIM).
- **FTO:** Tokamak's US11101060B2 and EP4078630A1 are **in force**. Their claims
  recite perforated/windowed insulating layers and HTS-bridge structures; a CF-1
  embodiment built by **zone-switched metallic co-winding with no insulating layer
  and no bridges** likely does not read on those claims — but that is a claim-chart
  exercise for counsel, not a conclusion of this gate. If it reads: design around
  (the co-wind mechanism already does) or license. Wang/Hahn NPL has no FTO effect.

**Verdict: NARROW-NOVEL.** Blocking references for anything broad: EP4078630A1 (EP),
US11101060B2 (US + family JP/KR/EP/AU), Wang/Hahn IEEE TAS NPL (patentability only).
Preconditions before W4 reliance: close ledger gaps #1 (native CNIPA/J-PlatPat/KIPRIS
pass), #2 (US12196792 OCR), #3 (CN115485868A full claims — title-level match to
"HTS field coil," plausibly another Tokamak national-phase entry; must be resolved),
and #5 (pin the Wang/Hahn citation).

---

## G-CLAIM — surviving core + design-around ladder: **SURVIVES, NARROWED**

### Surviving claim core (one sentence)
A cryocooler-conduction-cooled no-insulation HTS coil whose turn-to-turn interface
consists of at least two co-wound metallic interlayer zones arranged **radially** —
a higher-contact-resistivity zone over inner turns and a continuous
high-thermal-conductance drain zone extending unbroken to the cold-head interface —
wherein each zone's contact resistivity and thermal conductivity are coupled
properties of a single interlayer material (no perforated insulator, no discrete
bridges), and the zone boundary is selected so that charging time constant and
worst-case hot-spot temperature rise jointly meet targets within the cryocooler's
rated cooling capacity.

### Design-around ladder (ranked application to the Tokamak-anchored 102/103 threat)
1. **Combination/system claim — USE (primary).** Claim the coil **in combination
   with** the cryocooler/cold head of finite rated capacity and the radial zoned
   interface. Distinguishes every bath-cooled reference and Tokamak's tokamak-coil
   framing; strongest against 102.
2. **Different mechanism — USE (build into the independent claim).** CF-1's mechanism
   is **coupled-property material zoning** (the material choice sets Rc and k
   together; the invention is the spatial allocation resolving that conflict).
   Tokamak's mechanism is the opposite: **decoupling** via windows/HTS bridges so
   thermal and electrical vary independently. A limitation like "wherein the contact
   resistivity and thermal conductivity of each zone are joint properties of a single
   continuous metallic interlayer, the interface being free of apertured insulating
   layers and discrete conductive bridges" is both a 102/103 distinction and an FTO
   moat. This is the single highest-value adjustment.
3. **Enabling sub-solution — USE (dependent + method claim).** The drain-continuity
   requirement (the high-conductance zone must form an unbroken radial series path
   from the protected region to the cold head — one ss interface in series ruins the
   drain, as the sim's min(k) pairing shows) is the non-obvious "what makes it
   actually work." Also claim the manufacture method: switching co-wind interlayer
   material at a predetermined turn during winding.
4. **Architecture/topology — USE as dependents.** Radial zoning per se (vs Tokamak's
   circumferential variation); OD-adjacent drain abutting the cold-head plate;
   axially graded variant across a pancake stack; in-process material switch.
5. **Parameter windows — DO NOT USE YET.** Criticality evidence is insufficient:
   the sim's budget never binds (R2) and the front has a rounding artifact (R1).
   After the G-PHYS revisions produce a worst-case-spot criticality curve
   (e.g. drain-fraction window where both tau and ΔT targets hold at Q_budget),
   a window dependent becomes available. Write the rung into the spec now (no new
   matter later) but do not lean on it.
6. **Application-field — fallback only.** "Cryogen-free rotating-machine field
   coils" limitation: weak for patentability, useful for FTO posture and a CN
   utility-model parallel filing.

### Recommended adjustment and its cost
File with an independent claim = rung 1 (combination) + rung 2 (coupled-single-
material mechanism, bridge/aperture disclaimer) + rung 3 (drain continuity), with
rungs 4–6 as dependents/spec fallbacks. **Gain:** clears EP4078630A1/US11101060B2 on
mechanism and Wang/Hahn on objective+structure; maximizes grant odds while keeping
the commercially operative embodiment (zone-switched co-wind is exactly how a
Hinetics-class conduction-cooled coil would be wound). **Cost in scope:** surrenders
(a) bridge/perforated-insulation implementations of a radial map (Tokamak owns that
mechanism anyway), (b) circumferential-only and homogenizing maps, (c) bath-cooled
applications, (d) generic "non-uniform interface" breadth. Acceptable: what is
surrendered is either owned by others or commercially marginal to the cryogen-free
thesis.

**Verdict: surviving core as stated; primary adjustment = mechanism-limited
combination claim (rungs 1+2+3).**

---

## Gate summary

| Gate | Verdict | One-line reason |
|---|---|---|
| G-PHYS | **REVISE** (passable) | tau<->Rc direction independently confirmed correct (W2 fix right; matches MI/NI literature; conservation exact) — but fix Pareto rounding artifact, non-binding/units-conflated cooling budget, and spot-location robustness before quoting numbers. |
| G-NOVEL | **NARROW-NOVEL** | Genus (non-uniform electro-thermal interface engineering) blocked by EP4078630A1 (EP) / US11101060B2 (US, in force) + Wang/Hahn NPL; the radial + coupled-property + cold-head-budget combination is not disclosed anywhere found. |
| G-CLAIM | **SURVIVES, NARROWED** | Mechanism-limited combination claim (coupled single-material zoning, no bridges/apertures, drain continuity, cryocooler-budget context) clears the Tokamak family and preserves the commercial co-wind embodiment. |

Next: G-PHYS revisions R1–R3 in a W2 patch, close ledger gaps #1/#2/#3/#5, then W4
disclosure drafting on the rung-1+2+3 core. All verdicts are drafting/analysis aid —
**registered patent attorney review required; no filing authorized by this record.**
