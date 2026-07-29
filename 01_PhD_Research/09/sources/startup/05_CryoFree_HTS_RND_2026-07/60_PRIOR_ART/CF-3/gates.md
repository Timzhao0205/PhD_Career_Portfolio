# CF-3 Gate Record — "Thermal-aware current steering"

> **Drafting/analysis aid — registered patent attorney review required.** No verdict
> here authorizes a filing. Research aid, not legal advice.

Wave: W3. Gates run in order G-PHYS → G-NOVEL → G-CLAIM on 2026-07-10.
`models=GATE:fable-5` (intended).

**Model-verification caveat (mandatory):** the intended model for these three gates is
Fable 5, but the actually-served model is NOT verifiable from inside this session —
Anthropic safeguards may transparently route some Fable-5 queries to Opus 4.8, and a
Fable self-report is not proof of which model ran. Before any filing-relevant reliance
on these verdicts, confirm the served model against the external transcript at
`%USERPROFILE%\.claude\projects\`.

---

## G-PHYS — verdict: **REVISE**

**Question:** is "steered placement cuts peak dT vs naive at the same copper budget,
in every swept case" a real effect or an artifact?

**Finding: the headline comparison is an artifact of three compounding modeling
choices. The arithmetic is self-consistent, but the naive baseline is structurally
incapable of benefiting, the fault location is co-located with the steered block, and
the claimed mechanism (current steering) is not simulated at all.**

Evidence, from `20_SIM/cf3_current_steering.py` + `20_SIM/thermal_network.py` +
`20_SIM/out/cf3_starter.json`:

1. **The `min(k)` interface rule makes the naive baseline inert by construction.**
   `thermal_solve` sets the radial resistor between turns i and i+1 to
   `pitch / (min(k[i], k[i+1]) * A_face)`. `naive_placement` uses
   `np.linspace(0, N-1, n_cu)` — for every swept n_cu ≤ 12 with N = 30 the copper
   turns are non-adjacent, so every copper turn is flanked by stainless (k = 3 vs
   400 W/m/K) and `min()` erases it. This is visible in the output: naive peak dT is
   **identical for n_cu = 2 through 12** (25.4098 K at T_cold = 20 K). A baseline that
   cannot improve no matter how much copper it receives is a strawman; "steered beats
   naive in every case" follows from the discretization rule, not from physics.
   Physically, the interface material is a property of each interface, and should be
   assigned per-interface, not as the min over the two adjacent turns' labels.

2. **Fault-location cherry-pick / circularity.** `spot_turn = 2` is fixed, and the
   "steered" strategy concentrates all copper at turns 0..n_cu-1 — i.e. the steered
   map is co-located with the assumed fault. In this 1-D series network (single OD
   sink at turn N-1), the dT reduction comes solely from how many high-k interfaces
   lie in the series path between the fault and the sink; **within that path, position
   does not matter** (series resistances add). So (a) the specific "inner-concentrated"
   pattern carries no advantage beyond covering the assumed fault site — copper at any
   interfaces outward of turn 2 would help identically; and (b) the steered pattern
   actually *wastes* interfaces 0–1 (inward of the fault, dead-ended). Under a fair
   per-interface model, evenly-spaced copper places nearly all of its budget inside
   the fault→sink path and would tie or beat inner-concentration for most fault
   locations. A fault at an outer turn would make "steered" strictly worse. The sweep
   over n_cu and T_cold is not the sweep that matters; the missing sweep is over
   `spot_turn` (worst-case / expectation over fault position).

3. **The claimed mechanism is absent from the model.** CF-3's core is *current*
   steering — redistributing transport current via engineered/controlled bypass sites.
   The simulation contains no electrical network: `electrical_tau` is never called by
   `cf3_current_steering.py`; the heat load is a fixed 0.5 W injected at a fixed node;
   `cold_head_load` is trivially 0.5 W in every row (steady-state energy conservation,
   confirming no coupling). What was simulated is CF-1's *thermal-drain placement*
   effect wearing CF-3's label. No conclusion about current redistribution can be
   drawn from this artifact set.

4. Secondary issues, log for the revision: (a) `cooling_budget()` returns a lift
   budget in **W** (1.0 / 4.0 / 20.0 at 20/30/50 K) but is passed into `thermal_solve`
   as `G_ch` in **W/K** — a units conflation; the "cooling budget" sweep is really a
   sink-conductance sweep, and its only effect on peak dT is the additive
   `q/G_ch` term (0.5 → 0.125 → 0.025 K), which is why the three T_cold blocks are
   near-copies. (b) The CF-1 known issue (`tau_rc_narrative_direction`, see
   `20_SIM/out/cf1_starter.json` KNOWN_ISSUES) does **not** contaminate CF-3's
   headline, because CF-3 never invokes the electrical side — but the fix below will
   pull the electrical network in, so the tau↔Rc direction must be independently
   verified against NI/MI literature (Hahn et al.) at that point.

**Sanity checks that pass:** absolute dT magnitude is consistent with hand
calculation (≈ 27 stainless interfaces × ≈1.95 K/W × 0.5 W ≈ 26 K plus q/G_ch);
signs and boundary conditions are sane; energy is conserved.

**Required fixes to clear G-PHYS (state of the REVISE):**
1. Assign interface material **per interface**, removing the `min()` rule.
2. Sweep `spot_turn` over all turns; report worst-case and expectation over fault
   location, not a single co-located fault.
3. Add the electrical NI bypass network coupled to the thermal network so current
   actually redistributes in response to bypass placement/actuation — i.e. simulate
   the claimed mechanism. Joule heating from redistributed current must be the load,
   not a hand-placed q_spot.
4. Fix the W vs W/K units of the cold-head boundary (load-line as a constraint, not
   a conductance).
Until then, **no parameter-window claims and no non-obviousness argument may cite
cf3_starter.json** (number-truth discipline; the file is labeled prophetic, which is
correct, but its comparison is not evidentially valid even as a prophetic example).

---

## G-NOVEL — verdict: **NARROW-NOVEL (provisional — one required follow-up before reliance)**

Ledger reviewed in full (`60_PRIOR_ART/CF-3/ledger.md`, 19 hits incl. ZH/JA/KO query
coverage and the CN-language Tokamak Energy hit). All hits remain in `IDS_pool`
regardless of this verdict (duty of candor; design-around ≠ concealment).

**The genus is dead.** "Spatially engineered turn-to-turn resistance/bypass sites that
control current distribution in an HTS coil" is squarely disclosed and partly granted:

- **EP4012730A1 family / KR102631117B1 (granted, KR) — Tokamak Energy,
  "Partially-Insulated HTS Coils," priority 2018-02-01.** Spatially-staggered
  resistance windows controlling current distribution and local heating. Blocks any
  claim to spatial bypass-site placement per se. Jurisdictions: EP (withdrawn), KR
  (granted), CN/AU/WO published. Note the patentability-vs-FTO split: the withdrawn
  EP member still blocks *claims* everywhere as published art; the granted KR member
  additionally creates in-force *FTO* exposure in KR.
- **EP4078630B1 (granted 2023-11-15, in force, EP) — Tokamak Energy, "HTS Linked
  Partial Insulation," priority 2019-12-20.** The closest single reference. HTS
  bridges at specific spatial locations self-regulate (local quench → local
  resistance rise) and push current toward slower-quenching / cooler regions;
  thermal and electrical properties independently tunable via geometry.
- **US 11,094,438 / 11,551,840 (granted, US) — FSU/Hahn.** Active feedback current
  control of an NI magnet — blocks "active control" framed globally.
- **US 11,581,115 (granted, US) — SNU/Hahn.** Deliberately engineered spatial
  temperature map (heaters) shaping current/field behavior — blocks "impose a thermal
  map to steer current" framed broadly.
- **US 10,861,626 (granted, US) — KERI.** Temperature-triggered (MIT-material)
  autonomous bypass — blocks "bypass that responds to local temperature" per se.
- **US 12,196,792 (granted, US).** Turn-to-turn resistivity-distribution *measurement*
  — blocks the mapping step itself; CF-3 must claim use of a map, not its acquisition.

**The decisive question posed to this gate:** is EP4078630B1's "current redirected
toward cooler regions" concept *thermal-conduction-to-cold-head-based*, or
*quench-propagation/local-temperature-based*? On the ledger's evidence (abstract-level
paraphrase only), the mechanism is **reactive self-regulation via local HTS
critical-temperature physics during a quench event** — the bridge itself goes
resistive where it is hot; "cooler" means "not yet quenched," with no reference to a
known/measured conduction topology to a cryocooler cold head, and no fixed
cooling-power-budget framing (Tokamak Energy's setting is fusion magnets, not
cryocooler-budget-limited components). On that reading CF-3's core — **proactive**
placement/actuation driven by an **externally known/measured thermal-conduction-to-
cold-head map** under a **fixed cryocooler budget** — is a distinguishable species,
hence NARROW-NOVEL rather than DUPLICATED.

**However, the ledger does not contain EP4078630B1's granted claim set or its
description, only a paraphrased abstract — that is not enough to make this call
final, and I will not guess.** The specification may tie bridge geometry/placement to
cooling-path considerations (the "independently tunable thermal and electrical
properties" language points that direction), and its INPADOC family is unconfirmed
(ledger Gap 5). **REQUIRED FOLLOW-UP before W4 relies on this verdict:** pull the
EP4078630B1 granted claims + description (Espacenet) and full INPADOC family for both
Tokamak Energy filings; also close ledger Gaps 1 (US 12,196,792 bibliographic data)
and 6 (arXiv 2604.15587 — "Control of turn-to-turn contact resistivity…" — title is
on-mechanism and unread). If EP4078630B1's description discloses placing bridges
according to cooling/cold-path topology, CF-3's passive-placement species drops to
**DUPLICATED** and only the active-control species survives.

**Surviving white space (basis for the verdict):** no reference found in US/CN/JP/KR/EU
combines (i) spatially-resolved (per-turn/per-zone) bypass conductance, (ii) placement
or in-operation actuation driven by a known/measured thermal-conduction-to-COLD-HEAD
map (as opposed to a field/Ic map, an SCF map, quench-time self-regulation, or a
global feedback loop), and (iii) a cryogen-free, fixed-cryocooler-power operating
constraint. JP/KR/CN coverage caveat: harvest was via Google-Patents-family proxies,
not native J-PlatPat/KIPRIS/CNIPA browses (ledger Gaps 2–4); treat "no JP-only hit"
as a negative search result, not clearance.

**FTO note (distinct from patentability):** even if CF-3's species claims grant, a
product whose bypass sites also self-regulate thermally (any real HTS bridge does, to
some degree) may practice EP4078630B1 in EP and KR102631117B1 in KR — design-around
or license analysis needed there regardless of CF-3's own grant. A patent granted to
us ≠ freedom to operate.

---

## G-CLAIM — verdict: **surviving core defined; recommended shape = active, map-driven, system-level**

**Surviving claim core (one sentence):** A cryogen-free, conduction-cooled NI/
partially-insulated HTS coil system in which turn-to-turn bypass conductance is
spatially set or actively modulated according to a stored, measured-or-modeled map of
thermal conduction from each turn to the cryocooler cold head, so as to redistribute
transport current away from turns with poor cooling access while holding total heat
load within the cryocooler's fixed lift budget.

**Design-around ladder walk:**
1. **Combination/system:** coil + cryocooler (no cryogen bath) + stored cold-head
   conduction map + placement rule/controller. Distinguishes all four closest refs
   (none is framed on a cryocooler lift budget). Cost: system claim — misses
   component-only sales.
2. **Different mechanism — the strongest rung:** *active, in-operation, spatially
   resolved* modulation of bypass conductance (switchable interposers / per-zone
   actuation) driven by the measured map. Tokamak Energy's art is fixed-at-winding-
   time or passively self-regulating; FSU/Hahn's active control is a single global
   knob; SNU's heaters impose temperature, not bypass conductance. Cost: excludes the
   cheapest (passive, wound-in) embodiment as an independent claim.
3. **Enabling sub-solution:** the map→placement/actuation transformation — converting
   a per-turn cold-head-conduction map (however obtained; do not claim the
   measurement, US 12,196,792 owns that) into a bypass pattern satisfying a hot-spot
   margin AND a charging-delay target under the lift budget. This is the CF-1-style
   two-conflicting-jobs resolution applied to CF-3.
4. **Architecture/topology:** azimuthally-zoned bypass referenced to the physical
   cold-head strap location (all cited art is effectively 1-D radial); rotating-frame
   variant composes with CF-5.
5. **Parameter windows: NOT AVAILABLE.** G-PHYS is REVISE; cf3_starter.json provides
   no valid criticality evidence. Forbidden until the fixed coupled sim exists.
6. **Application-field limitation:** cryogen-free aviation/MRI coil framing — weak for
   patentability, useful for CN utility-model and FTO positioning.

**Recommended adjustment (maximizes grant odds, preserves commercial scope):** draft
the independent claim on rungs 1+2 — *active, spatially-resolved bypass modulation
driven by a stored thermal-conduction-to-cold-head map, in a cryocooler-cooled system
with no cryogen bath* — with rung-3 (the map→pattern method) as a parallel method
claim, and the passive winding-time placement kept **only as a dependent claim,
contingent on the EP4078630B1 claim-set review** required by G-NOVEL. **Scope cost:**
surrenders passive fixed placement as independent subject matter (that ground is
Tokamak Energy's), i.e. the lowest-cost embodiment is protected only narrowly; in
exchange the active claim reads on none of the granted art found and carries the
clearest inventive step. All six rungs must be written into the W4 spec (no new
matter later). W4 must not start until G-PHYS fixes 1–3 are rerun, since the
disclosure's prophetic examples currently have nothing valid to cite.

**Hard-rule compliance check (CLAUDE.md Rule 1):** CF-3 is cryogen-free coil
thermal/current-distribution work — presumptively outside the funded lane (HSX
diagnostics / GaN Hall devices / battery magnetic imaging). **Hall-sensing adjacency
flag:** any embodiment that senses current distribution *magnetically* would drift
toward Hall-sensor territory; W4 drafting must sense via temperature sensors and/or
terminal electrical measurements only, and must contain no GaN and no "stellarator"
(Tokamak Energy citations are fine — cited as art, not framing). No prong-a block.

---

## Verdict summary

| Gate | Verdict | One-line reason |
|---|---|---|
| G-PHYS | **REVISE** | Naive baseline inert by construction (`min(k)` rule), fault co-located with steered block, and no current/electrical physics simulated — headline is an artifact. |
| G-NOVEL | **NARROW-NOVEL (provisional)** | Genus blocked by Tokamak Energy EP4012730A1/KR102631117B1 + EP4078630B1; cold-head-conduction-map-driven, budget-constrained species survives — pending EP4078630B1 granted-claims review (required follow-up, ledger lacks claim text). |
| G-CLAIM | **Active, map-driven, system-level core** | Independent claim on active spatially-resolved bypass modulation from a stored cold-head-conduction map under a cryocooler budget; passive placement demoted to dependent; no parameter windows until sim rerun. |

All three verdicts are drafting/analysis aid only — registered patent attorney review
required before any filing, disclosure, or reliance.
