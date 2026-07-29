# MISSION BRIEF V2 — Novel-Lanes Research & Final Showdown (2029/2030 Launch Decision)

You are the **orchestrator** of Round 2. Round 1 (the sibling mission, outputs copied into
`00_PRIOR_CORPUS/GEN3/`) plus two earlier generations (`00_PRIOR_CORPUS/GEN1_GEN2/`) produced
~100 concepts, a saturated thesis basin, and a reigning slate. Your job is different from
Round 1: **search only the lanes never covered, generate genuinely NEW candidates, stress them
with the identical rubric, and then run one final merged showdown against the incumbent
best-of-best** so the founder gets his final "best of the best" list for a 2029/2030 launch.

Read, in order: `CLAUDE.md` · `01_MISSION/FOUNDER_PROFILE.md` · `01_MISSION/EXCLUSION_LIST.md`
· `01_MISSION/SOURCE_STANDARDS.md` · `01_MISSION/SCORING_RUBRIC.md` ·
`01_MISSION/DELIVERABLES_SPEC.md` · `05_STATE/MASTER_STATE.json` (resume from first incomplete
phase). Never ask the user anything; log assumptions to `05_STATE/ASSUMPTIONS.md`; run until
Phase 7 sets `"mission": "COMPLETE"`.

## Non-negotiables

- **≥ 12 genuinely novel candidates** (target 14). "Novel" is defined in EXCLUSION_LIST.md and
  enforced at Phase 2 and audited at Phase 7. Zero regenerations of excluded concepts.
- **Zero HTS/superconductivity candidates.** The single allowed HTS idea is the incumbent C12
  cluster (user rule: max 1 HTS idea; slot taken). Gate G6-HTS in the rubric enforces this.
- **≤ 2 candidates from the founder's PhD lanes** (GaN sensing / fusion diagnostics / battery
  magnetic imaging), each flagged and given extra red-team scrutiny. PhD = skillset, not topic.
- Diversity: ≥ 50% standalone products; ≤ 3 test/measurement/diagnostic instruments; every
  candidate assessed for China-first AND US entry; Magnefy wall (no transformer condition
  monitoring) absolute.
- **Merged bibliography ≥ 200 unique sources, of which ≥ 100 gathered fresh in this mission.**
  Prior-ledger reuse is allowed per SOURCE_STANDARDS.md.
- Same 11-criterion rubric, gates, and adjustment discipline as Round 1 — scores must be
  directly comparable to the incumbents' final scores. Timeframe lens: 2029/2030.

## Phase 0 — Init & corpus ingest (orchestrator)

1. Verify `00_PRIOR_CORPUS/GEN3/` contains the Round-1 finals (the launcher copies them from
   the sibling folder). If a listed file is missing, note it and proceed on what exists.
2. Build `05_STATE/exclusion_ledger.json`: start from the baked list in EXCLUSION_LIST.md, then
   parse every candidate/idea ID and name out of GEN3 (candidates.json, 02_FULL_RANKING.md,
   SATURATION rows) and GEN1_GEN2 (RID tables in june25, CL clusters, and ALL worker candidate
   IDs in the five frontier files, e.g. PWR-xx/SEM-xx/BIO-xx/IND-xx/EXT-xx, plus radar wedges).
   Each entry: id, name, 8-word gist, source file.
3. Write `60_FINAL_SYNTHESIS/INCUMBENTS.md`: the five incumbent theses with their **final
   scores frozen** from GEN3/02_FULL_RANKING.md — C12 cluster 83.6 (incl. C33/C11/C15 modules),
   C10 76.8, C06-pivot 74.8, C01/C03 69.6, C27 68.0 — each with a 10-line evidence summary and
   kill gates. Incumbent scores are **not** re-derived in this mission.
4. Update state; log.

**State discipline (all phases):** after every phase and wave, update MASTER_STATE.json
counters, merge/dedupe `90_BIBLIOGRAPHY/sources.json`, append one PROGRESS_LOG.md line. Files
are ground truth after any compaction.

## Phase 1 — Gap-lane landscape (8 × `domain-scout`, two parallel waves of 4)

These eight lanes were **never chartered** in any prior generation (verified against the
saturation report's gap register). Each scout receives its charter + the founder summary + the
relevant exclusion entries, and writes `10_GAP_LANDSCAPE/G<nn>_<slug>.md` +
`G<nn>_sources.json` (12–18 fresh sources, 3–5 opportunity seeds, ≤ 1,200 words). Seeds must
steer AWAY from the listed excluded neighbors.

- **G01 Battery & storage manufacturing beyond the cell** — module/pack assembly automation,
  laser-weld and interconnect QC systems, gigafactory EOL equipment niches, storage-container
  integration hardware. Excluded neighbors: C19 (SSB presses), C20 (formation), C40
  (second-life grading), CL-13 (dry electrode). The founder's battery magnetic-imaging skill is
  usable but its direct productization counts as PhD-lane.
- **G02 Plasma-industrial systems** — atmospheric/low-pressure plasma sources + power +
  controls sold as systems: surface treatment, waste/gas conversion, plasma torches for
  metallurgy/recycling, agriculture/water plasma. Excluded neighbors: C35 (accelerator RF), N03
  (gyrotron PSU), C29 (spacecraft PPU/PCDU — space electric-propulsion power counts as its
  neighbor), C36 (medical ablation OEM). "Plasma" is a user-named sector — treat seriously.
- **G03 Ocean & marine electrification** — ocean-energy PTO power electronics, electric
  workboat/port-craft charging systems, offshore autonomous-infrastructure power, marine
  microgrids. Excluded neighbors: N04 (subsea inductive docking), C01/C03 (USV power bricks),
  C04 (MCS modules).
- **G04 Industrial process electrification beyond RF/induction** — electric calciners and
  >1000 °C resistive systems, ultrasonic/UV process systems, electro-thermal storage discharge
  interfaces, industrial heat-pump power stages at extreme lift. Excluded neighbors: N05
  (solid-state microwave heat), C16 (HTS induction), RID-015 (thermal storage module).
- **G05 Photonics & laser systems integration (no fab)** — industrial laser system integration
  niches, free-space optical communication terminals (ground/air), laser wireless power
  delivery, precision beam-control electronics. Excluded neighbors: CL-09 (CPO assembly), C25
  (overlay metrology), RID-100 (optical assembly cell).
- **G06 Quantum & big-physics support electronics, room-temperature** — scalable control/
  readout racks, ultra-stable timing & synchronization distribution, precision bias/flux
  sources, FPGA-based feedback instruments sold as products. Excluded neighbors: C31 (OPM), C32
  (Rydberg), C34 (SMU), N06 (cryogenic power electronics), C10 (magnet converters).
- **G07 Circular economy & critical-materials equipment** — magnet/rare-earth recycling
  process equipment, e-waste separation systems (eddy-current, electrostatic, sensor-sorting),
  black-mass and electrolyte recovery hardware, urban-mining automation. No prior neighbors —
  fully virgin lane.
- **G08 Rail, mining & heavy-industry electrification niches** — catenary-free/battery tram
  and shunter power systems, trolley-assist and pit electrification hardware, tunneling machine
  power, port crane electrification retrofits. Excluded neighbors: C04 (MCS), C09 (SST blocks),
  C38 (GFM PCS).

## Phase 2 — Novel candidate generation (orchestrator)

Synthesize **≥ 12** candidates (`V01…`) into `20_CANDIDATES/CANDIDATES.md` + `candidates.json`.
Round-1 template PLUS a mandatory **Novelty declaration**: nearest excluded neighbor (by id),
and 2–3 sentences on the material difference (different buyer segment or product category — a
re-parameterized variant does not qualify; when in doubt, it's a variant → drop and generate a
replacement). Enforce all diversity rules and gates now, including G6-HTS. Cross-lane hybrids
encouraged.

## Phase 3 — Scoring & full red team

1. Score all candidates on the identical rubric → `30_SCORING/SCORING_MATRIX.md` + `.csv`.
2. `red-team-critic` on **every** candidate (parallel waves of 5) → `30_SCORING/REDTEAM_Vxx.md`;
   apply ±1 adjustments with written reasons. Red team must independently verify each novelty
   declaration — a disguised duplicate is a kill.
3. Select top 5 for deep dives (respecting diversity rules) → `30_SCORING/SELECTION.md`.

## Phase 4 — Deep dives (5 × `deep-dive-analyst`, waves of 3 then 2)

Round-1 format: 10 sections, 2,000–3,500 words, ≥ 14 unique sources each (Chinese-language
sourcing mandatory for the China section), plus section 11: **Novelty defense** (why this
survived the exclusion test). Output `40_DEEPDIVES/DD_Vxx_<slug>.md` + sources json.

## Phase 5 — Policy delta (`policy-analyst`, parallel with Phase 4)

Do NOT redo the Round-1 policy brief. Read `GEN3/POLICY_BRIEF.md` (if present) and verify only
what may have CHANGED since its date, as of today: Affiliates-Rule reactivation status
(2026-11-09 waypoint), COINS/31 CFR 850 implementation progress, any new export-control or
Chinese-policy action touching the eight gap lanes. Output `50_POLICY_DELTA/POLICY_DELTA.md`
(10–18 fresh sources, official-source-dominant) with per-lane China/US posture notes.

## Phase 6 — FINAL SHOWDOWN (orchestrator; this is the file the user reads)

1. Apply the Round-1 comparability convention to the new candidates: deep-dived V-candidates
   carry their full adjusted scores; red-teamed-but-not-deep-dived carry `RT-adj − 8.9e`;
   neither → `raw − 11.4e` (same statistics as Round 1; mark `e`).
2. `60_FINAL_SYNTHESIS/00_FINAL_SHOWDOWN.md`: one merged ranked table — 5 incumbents (frozen
   scores) + all V-candidates (aligned scores) — followed by: **The Best-of-the-Best Top 5**
   with one-paragraph theses; an explicit verdict on whether ANY V-candidate displaces C12 as
   primary or upgrades the fallback chain (C06 → C01/C03 → C27 → C23); the biggest surprises;
   honest statement of evidence-class differences.
3. `60_FINAL_SYNTHESIS/01_ROADMAP_IMPLICATIONS.md`: do NOT edit the Round-1 roadmap; state
   what (if anything) changes in it — new tripwires, a new fallback insertion, or "no change,
   here's why" — with the 2026 H2 action deltas.
4. `60_FINAL_SYNTHESIS/02_MERGED_FULL_RANKING.md`: all ~112+ concepts across all generations,
   id + name + final/expected score + one-line verdict + source generation. The single
   reference table for everything ever considered.
5. Regenerate `90_BIBLIOGRAPHY/BIBLIOGRAPHY.md` (merged, tier-grouped, zh bilingual, reused
   sources marked).

## Phase 7 — Audit & fix (`source-auditor`, then orchestrator)

`99_AUDIT/FINAL_AUDIT.md`: novelty audit (re-check every V against the exclusion ledger — any
duplicate = FAIL → orchestrator replaces and re-runs pipeline for that slot); merged unique
sources ≥ 200 with ≥ 100 fresh; tier mix per standards; re-fetch 15 random citations
(bias to load-bearing numbers and reused-source claims); quota/diversity/gate checks incl.
0 HTS and ≤ 2 PhD-lane; deliverables checklist. Fix, re-check, set COMPLETE, print the
Best-of-the-Best Top 5 + file map.

## Operating notes

Parallel waves as specified; subagents write files and return one-line summaries only; no full
webpage dumps in conversation; load-bearing numbers only from fetched pages; if a wave member
returns thin, rerun just that member. Effort policy is set by the launcher (session = max) and
per-agent frontmatter (scouts/auditor pinned high for source gathering); do not override it.
