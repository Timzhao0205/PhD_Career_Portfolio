# MISSION — Cryogen-Free HTS Component Patent Discovery Engine

> **Research aid — not legal advice.** Patentability, FTO, inventorship, and ownership
> (incl. Stanford SU-18) require a registered patent attorney before any filing or reliance.

## Objective
Autonomously discover **cryogen-free / conduction-cooled HTS component** inventions
that are (a) patentable with reasonable cost, (b) validatable by cheap simulation +
sub-$1.5K prototypes, (c) checked for duplication across the large HTS-market patent
systems (US, China, Japan, Korea, EU/PCT), and (d) where promising, shaped with
design-around adjustments to raise grant odds. Output: ranked candidate disclosures
+ a phased sim/prototype plan + a full model/effort/budget run report.

## Why cryogen-free is the target (and the core technical insight)
Conduction cooling with limited cold-head power removes the thermal buffer a liquid
bath provides: thermal margin is low and location-dependent, hot spots are dangerous,
and heat must reach the cold head through solid conduction. The validated seed insight
(CF-1) is that **in an NI coil the turn-to-turn interface is a single design layer
doing two conflicting jobs** — it sets contact resistance Rc (electrical bypass /
charging / field quality) AND the radial thermal drain to the cold head. High-Rc
interfaces (stainless) are ~130× worse thermal paths than copper-class ones. Resolving
that conflict spatially is white space that composes with the existing
measure→sense→actuate family.

## Candidate seed set (engine expands to ≥15 via the `cryo-ideator` agent, then prunes)
CF-1 is pre-validated by the chat-session thermal sandbox; treat as flagship.

| ID | Candidate | Core claim hypothesis | CF relevance | Composes with |
|---|---|---|---|---|
| **CF-1** | Dual-function turn-to-turn interface | winding-time engineered interface that JOINTLY sets Rc and radial thermal conductance to the cold head, as a co-optimized spatial map | very high | Patent A write-head; B; C |
| CF-2 | Thermal-margin-aware quench detection | QD thresholds referenced to a conduction-cooled temperature map (cryocooler-state + conduction model), not a bath-pinned temp | very high | Patent B child (ID_09) |
| CF-3 | Thermal-aware current steering | NI bypass / thermal sites redistribute current away from thermally weak cooling paths to cut hot-spot risk under limited cooling | high | Patent C child |
| CF-4 | Cold-head-budget ramp governor | charge/ramp controller bounding AC+eddy loss to measured instantaneous cryocooler headroom | high | C10 converter |
| CF-5 | Rotating-frame heat extraction for NI motor coils | thermal architecture removing heat from a spinning conduction-cooled NI winding within budget (Hinetics CRUISE-class) | very high | C12 platform |
| CF-6 | Thermal-contraction-matched NI interface | interface holding both electrical (Rc) and thermal contact across cooldown/cycling in cryogen-free operation | med-high | Patent A |
| CF-7 | Conduction-cooled lead/termination co-qual | born-qualified current-lead + termination with integrated thermal+electrical acceptance record | medium | C12 leads product |

## Scoring rubric (0–5 each unless noted)
`cryogen_free_relevance` (HARD GATE: kill if <2) · `novelty_headroom` (post-adjudication) ·
`simulate_cheaply` · `prototype_under_1p5k` · `composes_with_existing_IP` ·
`commercial_pull` (Hinetics/aviation/MRI/cable) · `prong_a_safety` (HARD GATE: kill if <2).
Rank survivors by weighted sum with `cryogen_free_relevance` as a multiplier.

## Pipeline (waves — each ends at a resumable checkpoint; update RUN_STATE at each)

**W0 scaffold (haiku, low).** Verify folders, seed `80_STATE/RUN_STATE.json` with
`budget_tokens`, write `_about.md` per subfolder + `Folder_Info.md`. Gate:
`tools/check_runlog.py` green.

**W1 prior-art harvest (sonnet, medium).** Per candidate, structured multilingual
searches across US (USPTO/PatentsView), China (CNIPA + Chinese-language terms),
Japan (J-PlatPat), Korea (KIPRIS), EU/PCT (Espacenet/WIPO PatentScope), plus NPL
(IEEE TAS, SUST, Cryogenics, arXiv). Generate query packs incl. CPC/IPC walks
(H01F6/06, H01F6/04, H02K55/*, F25B, G01R) and assignee watches (Hinetics, GE,
Airbus/UpNext, Toshiba, Mitsubishi, Sumitomo, Fujikura, Furukawa, SuperPower,
Shanghai Superconductor, IEE-CAS, Tokamak Energy, CFS, Bruker, Siemens Healthineers,
Korea Univ/KERI/KAIST, MIT). **Non-English hits captured in original language +
machine translation** (a dup check that reads only English is worthless). Write
`60_PRIOR_ART/<CFid>/ledger.md` + `sources.json` (tiered). Checkpoint: harvest
summary + budget spent; halt for user review.

**W2 simulation (sonnet, medium).** Per surviving candidate, cheapest model of the
core effect. Reuse `20_SIM/id09_substrate/ni_network_sim.py`; add the coupled
electro-thermal network in `20_SIM/thermal_network.py` (CF-1 starter provided).
Deliverables: labeled prophetic examples + claim-element→artifact support table.

**W3 Fable gates (fable-5, high) — order matters.** Per candidate:
G-PHYS (effect real? PASS/REVISE/KILL) → G-NOVEL (NOVEL / NARROW-NOVEL / DUPLICATED,
naming blocking refs + jurisdiction) → G-CLAIM (surviving core + ranked design-around
adjustments per the ladder below). Log intended `models=GATE:fable-5` + down-route
caveat (see CLAUDE.md).

**W4 disclosure drafting (opus, high).** Survivors only (NOVEL / NARROW-NOVEL). Write
`70_DISCLOSURES/ID_##_<slug>.md` on the ID_09 template: problem, field, independent
claim (a)–(g), dependents, embodiments, exclusions, prophetic examples, IDS_pool,
counsel questions. Write EVERY design-around fallback rung into the spec (no new
matter later).

**W5 synthesis (opus, medium).** Rank; write `RND_STRATEGY_CryoFree.md` (flagship,
per-candidate verdict, budget-phased sim+prototype plan reusing the shared 77 K rig,
kill gates) and `98_CLAUDE_METRICS/RUN_REPORT.md` (models-per-stage, budget spent,
Fable-gate outcomes, recommended reruns).

## Design-around ladder (G-CLAIM applies; pre-build into every disclosure)
1 combination/system claim → 2 different mechanism → 3 enabling sub-solution (claim
what makes a known idea actually work — e.g. the spatial co-optimization resolving
the Rc-vs-thermal conflict) → 4 architecture/topology (per-turn/azimuth, in-process,
rotating-frame) → 5 parameter windows (ONLY with criticality evidence from sims) →
6 application-field limitation (weak for patentability; useful for FTO + CN utility
model).

## CF-1 simulation starter (build first in W2)
Validated sandbox result to reproduce/extend: conduction-cooled NI pancake, turn-to-turn
interface sets both Rc and radial thermal drain; copper-class interface ~0.02 K rise
for 0.5 W local vs ~2.65 K for stainless — ~133× swing from the same material choice.
`20_SIM/thermal_network.py` implements the coupled model; extend to: (i) per-turn
thermal nodes + cold-head sink + cryocooler load-line at 20/30/50 K fixed W-budget;
(ii) sweep a SPATIAL interface map (high-Rc lanes where thermally safe; high-conductance
drains to the cold head) to meet a charging-delay target AND keep peak hot-spot ΔT below
current-sharing margin under fixed cooling W; (iii) map the design window vs cooling
power. **Acceptance = a Pareto front (charging-delay vs peak-ΔT vs cooling-W) a uniform
interface cannot reach** — objective non-obviousness evidence for G-NOVEL/G-CLAIM.
