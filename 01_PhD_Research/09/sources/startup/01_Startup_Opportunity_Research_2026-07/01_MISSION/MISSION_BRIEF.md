# MISSION BRIEF — Startup Opportunity Deep Research (2029/2030 Launch)

You are the **orchestrator** of a fully autonomous, multi-agent research mission. Your job is to
produce a rigorous, source-verified analysis of startup opportunities for the founder described in
`01_MISSION/FOUNDER_PROFILE.md`, targeting company formation in **2029/2030**.

Read, in order, before doing anything else:
1. `CLAUDE.md` (operating rules — binding)
2. `01_MISSION/FOUNDER_PROFILE.md`
3. `01_MISSION/SOURCE_STANDARDS.md`
4. `01_MISSION/SCORING_RUBRIC.md`
5. `01_MISSION/DELIVERABLES_SPEC.md`
6. `05_STATE/MASTER_STATE.json` — then resume from the first phase not marked `"complete"`.

**Never ask the user anything.** If information is missing, write the assumption to
`05_STATE/ASSUMPTIONS.md` and proceed. Run until Phase 7 sets `"mission": "COMPLETE"`.

---

## Non-negotiable output requirements

- **≥ 36 distinct candidate ideas** generated (user asked for 20+; overshoot deliberately).
- **12 deep-dive reports** on the top-scoring ideas.
- **≥ 200 unique sources** in `90_BIBLIOGRAPHY/sources.json`, meeting `SOURCE_STANDARDS.md`.
- Idea diversity rules (hard constraints, checked in Phase 3 and Phase 7):
  - ≥ 50% of candidates are **standalone products/systems** (the product itself delivers the
    customer's end value — not a diagnostic, monitoring, or test layer on someone else's system).
  - ≤ 33% of candidates are test/measurement/diagnostic instruments.
  - ≥ 50% of candidates sit **outside** the founder's PhD thesis lane (GaN Hall sensors / fusion
    magnetic diagnostics). His PhD is a skillset, not a directive.
  - Every candidate names a credible **high-end niche beachhead** and a plausible **expansion path**.
  - Every candidate is assessed for **both** a China-first and a US entry sequence.
- Timeframe lens: evaluate markets, technology readiness, and competition **as of 2029/2030**, not
  just today. "Why now (i.e., why 2029)?" is a required section everywhere.

---

## Phase 0 — Initialize (orchestrator, quick)

1. Confirm the folder structure matches `DELIVERABLES_SPEC.md`; create anything missing.
2. Skim `01_MISSION/REFERENCE/` (founder's IEEE Sensors Letters paper) — treat it strictly as
   **capability evidence** (fabrication, packaging, harsh-environment instrumentation, readout
   electronics, working with big-science facilities), never as a topic directive.
3. Set Phase 0 `"complete"` in `MASTER_STATE.json`; append a line to `05_STATE/PROGRESS_LOG.md`.

**After every phase** (and after every subagent wave): update `MASTER_STATE.json` counters, merge
new sources into `90_BIBLIOGRAPHY/sources.json` (dedupe by URL), and append to `PROGRESS_LOG.md`.
Files are ground truth. If context is ever compacted, re-read `CLAUDE.md` + `MASTER_STATE.json`
and continue from the files.

---

## Phase 1 — Landscape scan (10 parallel `domain-scout` subagents)

Launch the `domain-scout` subagent once per domain below. Run them in **two parallel waves of 5**
(wave A: D1–D5, wave B: D6–D10). Give each scout: its domain charter below, the founder-profile
summary paragraph, and the source rules. Each scout writes
`10_PHASE1_LANDSCAPE/D<nn>_<slug>.md` plus `10_PHASE1_LANDSCAPE/D<nn>_sources.json`.

Per-scout quota: **18–25 logged sources**, **4–6 opportunity seeds**, brief ≤ 1,500 words.
Each seed = 3–5 sentences: the pain, who pays, why extreme performance wins, why a 2-5 person
team can enter, China/US angle.

Domain charters (scan each for pain points, buyer segments, incumbent gaps, price points,
2029-relevant inflections; think products, not papers):

- **D01 Extreme power electronics & conversion** — solid-state transformers, MV/HVDC building
  blocks, ultra-fast EV charging, electric aviation & marine power, pulsed power, >99% efficiency
  or >100 W/in³ class converters; WBG (GaN/SiC) as the enabler.
- **D02 AI & data-center hardware infrastructure** — 800 VDC / rack-level power delivery, power
  quality & ride-through, liquid cooling interfaces, busbars/connectors, backup & peak-shaving
  hardware, GPU-cluster electrical instrumentation sold as products.
- **D03 Fusion & big-science supply chain** — what the ~50 private fusion companies and national
  labs must BUY: magnet power supplies, heating/RF systems, HTS magnets and coils, vacuum &
  cryo subsystems, control hardware. Prefer standalone sellable subsystems over diagnostics.
- **D04 Applied superconductivity systems** — HTS coils/magnets as products, superconducting
  motors/generators, compact NMR/MRI magnets, induction heaters, SMES, maglev components,
  cryocooler-integrated turnkey magnet systems; the manufacturing bottlenecks (winding, joints,
  quench protection) as equipment opportunities.
- **D05 Advanced manufacturing & test equipment** — precision automated winding/assembly machines,
  battery formation & grading equipment, burn-in/system-level test, hipot/partial-discharge and
  insulation analyzers, laser-aligned automation cells; "picks and shovels" for electrification.
- **D06 Semiconductor equipment adjacencies (post-cleanroom)** — advanced packaging & hybrid
  bonding periphery, wafer/device test & metrology niches, WBG device reliability/burn-in
  equipment, SiC/GaN test hardware; equipment a small team can build without owning a fab.
- **D07 Space & harsh-environment electronics** — satellite power systems (PPU, PCDU), radiation-
  tolerant power/compute modules, orbital data-center power, downhole/geothermal
  high-temperature electronics; COTS-plus qualification as the business.
- **D08 Instrumentation & sensing products (standalone)** — precision magnetometers & current
  sensors sold as instruments, source-measure units, EMI/EMC gear, quantum-adjacent sensing
  products with classical readout; must stand alone as the product.
- **D09 Medical & scientific systems** — compact NMR/benchtop MRI subsystems, RF/microwave power
  for medical (ablation, proton-therapy periphery), gradient amplifiers, scientific power
  supplies; regulatory-light scientific market first, clinical later.
- **D10 Energy storage, hydrogen & grid edge** — electrolyzer/fuel-cell power conversion,
  grid-forming inverter niches, microgrids for compute campuses, second-life battery test &
  repurposing equipment, DC infrastructure components.

Do not add an 11th domain; breadth beyond this is Phase 2's synthesis job.
Mark Phase 1 complete only when all 10 briefs + source files exist.

## Phase 2 — Candidate generation (orchestrator)

Read all 10 briefs. Synthesize **≥ 36 candidates** (target 40) into
`20_PHASE2_CANDIDATES/CANDIDATES.md` (one section per idea, ID `C01…C40`) and a machine-readable
`20_PHASE2_CANDIDATES/candidates.json`. Enforce the diversity rules now — regenerate to fill gaps
rather than shipping a skewed list. Cross-domain hybrids are encouraged (that's where the
founder's unusual skill mix pays).

Per-candidate template (≤ 300 words each):
`Concept | Extreme edge (the 10x claim) | Beachhead niche (who exactly, ~how many buyers, ASP
guess) | Expansion path | Frontier vision | HW/SW split | TRL & build feasibility by 2029 |
Cleanroom dependence (none/low/med/high) | China-first angle | US angle | Founder-fit note |
Sources [S###] (≥3, Tier 1–2 majority)`

## Phase 3 — Screening & scoring (orchestrator + `red-team-critic`)

1. Score every candidate against `SCORING_RUBRIC.md`. Output
   `30_PHASE3_SCORING/SCORING_MATRIX.md` **and** `SCORING_MATRIX.csv` (one row per candidate,
   one column per criterion, weighted total, rank).
2. Send the top 15 to the `red-team-critic` subagent (parallel waves of 5). It writes
   `30_PHASE3_SCORING/REDTEAM_<Cxx>.md` per idea: strongest bear case, hidden competitors,
   "why this fails by 2031", founder-fit doubts. Adjust scores where the critique lands.
3. Select the **top 12** (respecting diversity rules — if the top 12 violates them, promote the
   next-best compliant candidate and say so). Record selections + rationale in
   `30_PHASE3_SCORING/SELECTION.md`.

## Phase 4 — Deep dives (12 × `deep-dive-analyst`, parallel waves of 4)

One report per selected candidate: `40_PHASE4_DEEPDIVES/DD_<Cxx>_<slug>.md`,
2,000–3,500 words, **≥ 14 unique sources each** (Tier 1–2 majority; Chinese-language sources
required for the China landscape section — the founder reads Chinese natively). Fixed sections:

1. Problem & who has it (named user archetypes; the high-end niche quantified)
2. Product definition & the extreme-performance edge (specs vs. state of the art, with numbers)
3. Technical feasibility & TRL path to a sellable unit by 2029–2031 (BOM sketch, hard parts,
   cleanroom dependence, what can be bought vs. must be built)
4. Competitive landscape — global **and** Chinese players, incl. pricing signals where findable
5. Market: beachhead sizing (bottom-up), adjacent expansion, triangulated TAM/SAM/SOM
6. Go-to-market: China-first sequence AND US sequence; which to lead and why; channel/reference-
   customer strategy for scientific/industrial buyers
7. Regulatory & geopolitical exposure (export controls, dual-use flags, certification burden) —
   coordinate with Phase 5 findings; flag anything that makes China-first structurally hard
8. Capital & milestones: seed→A plan 2029→2032, burn, first-revenue timing
9. Risks & kill criteria
10. Verdict: conviction level + what to validate during the remaining PhD years

## Phase 5 — Policy & geopolitics briefing (`policy-analyst`, 1 agent, runs in parallel with Phase 4)

Output `50_PHASE5_POLICY/POLICY_BRIEF.md` (≥ 25 sources; official/government and top-tier policy
sources dominant; use both English and Chinese sources). Cover, **as of the run date — search for
current status, do not rely on memory**:

- US export-control regime relevant to power electronics, superconductors, semiconductors,
  fusion-adjacent tech (EAR/BIS entity & emerging-tech rules; deemed-export basics for a
  US-trained founder)
- US outbound-investment restrictions and any 2025–2026 legislation affecting US persons
  founding/funding China-facing hardware startups — verify current names, scope, and dates
- CFIUS / inbound implications if the company later raises US capital
- China: current Five-Year Plan priorities (2026–2030), import-substitution programs, subsidies
  and buyer preferences relevant to the domains above; practical realities for a foreign-educated
  founder starting in China
- A neutral decision framework: China-first vs US-first vs parallel, per idea archetype
  (clearly labeled as research, **not legal advice**)

## Phase 6 — Synthesis (orchestrator, using the strongest model)

Write, in `60_PHASE6_SYNTHESIS/`:
- `00_EXECUTIVE_SUMMARY.md` — ≤ 3,000 words. Ranked **Top 7** with one-paragraph theses,
  the comparison table, the biggest surprises, and explicit "what I'd do in your position"
  reasoning under stated assumptions.
- `01_ROADMAP_2026_2030.md` — quarter-by-quarter preparation plan aligned with finishing the
  PhD: skills to build, relationships/customers to develop, cheap validation experiments,
  decision gates (incl. the 2029 China/US structuring decision informed by Phase 5).
- `02_FULL_RANKING.md` — all candidates, final scores, one-line verdicts.

## Phase 7 — Audit & fix (`source-auditor`, then orchestrator)

The auditor verifies and writes `99_AUDIT/FINAL_AUDIT.md`:
- Unique-source count ≥ 200; tier distribution table; zero preprints used as load-bearing support
- Randomly re-fetch **20** cited URLs; confirm each supports its claim (list pass/fail)
- Diversity-rule compliance; deliverable checklist from `DELIVERABLES_SPEC.md` all present
- Broken links / duplicate sources / citation-ID mismatches

Orchestrator fixes every failure the audit finds, re-runs the failed checks, then sets
`"mission": "COMPLETE"` in `MASTER_STATE.json`, appends a closing PROGRESS_LOG entry, and prints
a short completion summary (top 7 ideas + file map) as the final message.

---

## Operating notes

- **Parallelism:** always launch subagent waves as parallel Task calls (5 scouts at once, 4
  analysts at once). Between waves, merge sources and update state.
- **Token discipline:** subagents return summaries and write files — never paste full webpages
  into the conversation. Prefer WebFetch of the best pages over piles of search snippets.
- **Load-bearing numbers** (market sizes, prices, dates, specs) must come from a fetched page,
  not a search snippet, per `SOURCE_STANDARDS.md`.
- If a wave partially fails (a scout returns nothing), rerun just that scout before moving on.
