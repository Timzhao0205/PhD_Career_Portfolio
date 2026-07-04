# MISSION BRIEF V3 — C12 + C10: Startup Strategy, Competitor Map & Patent Whitespace

You are the **orchestrator** of Round 3. Rounds 1-2 converged: **C12 (NI/MI-HTS coil winding
cells + C33 QC module + recipe software, 83.6)** is the primary bet and **C10 (fast-dynamics
precision magnet power converters, 76.8, absorbing the C11 quench-protection line)** is the
paired second. Saturation is confirmed; no more idea generation. Round 3 answers three
questions the founder must act on during 2026-2028, before a 2029/2030 founding:

1. **Who exactly will we compete with, and which of their customers' problems remain unsolved?**
2. **Where is the patent whitespace in these fields — in the US AND China?**
3. **Which specific inventions should the founder conceive, prototype cheaply, and file on
   personal resources so a defensible IP position exists at PhD completion?**

Read, in order: `CLAUDE.md` · `01_MISSION/FOUNDER_PROFILE_V3.md` ·
`01_MISSION/IP_GROUND_RULES.md` · `01_MISSION/PATENT_SEARCH_PLAYBOOK.md` ·
`01_MISSION/TECH_CLUSTERS.md` · `01_MISSION/SOURCE_STANDARDS.md` ·
`01_MISSION/DELIVERABLES_SPEC.md` · `00_PRIOR_CORPUS/DEEPDIVES/DD_C12_*.md`, `DD_C10_*.md`,
`DD_C11_*.md`, `DD_C33_*.md` · `00_PRIOR_CORPUS/00_FINAL_SHOWDOWN.md` ·
`00_PRIOR_CORPUS/POLICY_DELTA.md` · `05_STATE/MASTER_STATE.json` (resume from first incomplete
phase). Never ask the user anything; log assumptions; run until Phase 6 sets
`"mission":"COMPLETE"`.

## Non-negotiables
- Scope is the **C12 cluster** (machine + C33 inline-QC module + recipe/traceability software)
  and **C10** (converter family + C11 protection/dump integration + fleet software). C11 and
  C33 are modules inside the two strategies, never standalone tracks.
- **Patent truth rule** (CLAUDE.md §3) on every patent number, everywhere.
- **>= 150 fetch-verified patent records** across the ledger, **>= 50 CN-family**; every
  cluster covers US + CN and checks WO/EP/JP/KR families where surfaced.
- **10-14 invention disclosures**, each red-teamed; target **>= 6 FILE-CANDIDATE** survivors;
  every disclosure passes the Stanford/UIUC wall and the <= $25K build rule (STRETCH <= $60K
  flagged).
- Every strategy claim traceable to a competitor card, unsolved-register entry, patent record,
  or prior-corpus deep dive. No unreferenced market numbers.
- Chinese-language searching mandatory for CS-B, CS-G, and the CN side of every patent cluster.

## Phase 0 — Init & corpus ingest (orchestrator)
1. Verify 00_PRIOR_CORPUS contains the four deep dives + showdown + policy delta + incumbents
   (launcher syncs from sibling; shipped copies are fallback). Note any missing file, proceed.
2. Extract into `05_STATE/BASELINE.md` (<= 800 words): (a) the C12 and C10 theses in 5 bullets
   each; (b) the already-known competitor set per lane (from DD §4 tables); (c) the
   already-known unsolved-problem hypotheses (from DD §1-2); (d) the 2026-2028 validation
   experiments the strategies must arm (ASC-2026/MT-29 interviews; C10 willingness-to-pay
   probe; C11 detection-latency benchmark; tabletop NI rig; SUST/TAS publication plans that
   Rule 6 must re-sequence).
3. Initialize `30_PATENTS/patent_ledger.json` = `[]` and confirm `90_BIBLIOGRAPHY/sources.json`
   exists (create `[]`). Update state; log.

## Phase 1 — Competitor deep map (8 × `competitor-analyst`, two waves of 4)
Each analyst gets one segment charter below + BASELINE.md + the relevant DD §4. Output per
segment: `10_COMPETITORS/CS_<X>_<slug>.md` (<= 1,600 words; 4-8 competitor cards) +
`CS_<X>_sources.json` (>= 12 fresh) + `20_UNSOLVED/U_<X>.md` (3-8 structured unsolved-problem
entries). Card fields: identity/ownership; product line with **specs and price signals**;
2024-2026 moves (acquisitions, tenders won, product launches); patenting posture (assignee
name variants for Phase 2 — do NOT fetch patents yet); channel & lead time; **observed
weaknesses/gaps with evidence**. Unsolved entries follow the U-schema in DELIVERABLES_SPEC.

- **Wave 1 (C12 side):**
  - **CS-A West winding & coil-production equipment.** Seeds: Broomfield, Ridgway (Tokamak
    Energy), Supertek/BOW, Aumann/Marsilli-class e-mobility winders probing SC tape; mandate:
    discover any 2025-2026 entrant selling REBCO/NI-capable machines or retrofits.
  - **CS-B China winding/coil equipment & industrial HTS producers (zh).** Seeds: CAS
    Hefei/HFIPS equipment + 招标/中标 sweeps (绕线机/绕制/超导磁体), 联创超导, 健信超导,
    上海超导 (tape QC/rewind adjacency), 能量奇点; mandate: name every disclosed 干式绕线 or
    winding-line capability and any equipment offered for external sale.
  - **CS-C Vertical integrators & coils-as-product.** CFS, TE Magnetics/Ridgway, Proxima,
    Thea (planar coil factory concept), Energy Singularity: evidence for/against selling
    machines or coils to third parties; what their existence removes from the buyable market.
  - **CS-D Coil/tape QC & instrumentation (C33 space).** Seeds: THEVA TapeStar-class Ic
    mapping, tape-vendor QC offerings (Faraday Factory/SuperPower/Fujikura/Shanghai
    Superconductor), magnet test-stand instrumentation, fiber-optic/acoustic quench- and
    defect-detection instrument vendors; mandate: who sells inline (during-winding) QC today —
    if nobody, document the absence with evidence.
- **Wave 2 (C10 side):**
  - **CS-E West precision catalog supplies.** Seeds: CAENels, Danfysik, Heinzinger, Delta
    Elektronika, iseg, Matsusada, TDK-Lambda; mandate: verify the reported Kepco BOP
    wind-down and who (if anyone) captured the orphaned bipolar-lab niche; map the exact
    power/precision/bandwidth envelope each vendor tops out at.
  - **CS-F Custom/project houses & lab self-supply.** OCEM, Jema, Magna-Power, CERN
    design-licensing program, plus discovered EPC/project vendors; lead times, project sizes,
    what they refuse to productize.
  - **CS-G China fusion/accelerator power (zh).** 爱科赛博 (Actionpower), 荣信汇科, 英杰电气 +
    tender sweeps (BEST/CRAFT/HL-3/EAST 电源 中标 2025-2026); specs and prices from tender
    documents; mandate: quarterly-updatable competitive-intel template the founder can rerun.
  - **CS-H Fast-control, coil-array drive & quench-protection electronics (C11 absorber
    space).** D-TACQ-class acquisition/control, PXI/FPGA plasma-control vendors, any
    HTS-specific quench-detection instrument sellers, Thea-style in-house array drives;
    mandate: who could bundle converters+protection before 2029.

Orchestrator then merges all `U_<X>.md` into `20_UNSOLVED/UNSOLVED_REGISTER.md` (dedupe,
assign U-### ids, severity-rank; 20-40 entries expected). Update state.

## Phase 2 — Patent landscape US+CN (10 × `patent-scout`, two waves of 5)
One scout per cluster P01-P10 in `01_MISSION/TECH_CLUSTERS.md`, following
`PATENT_SEARCH_PLAYBOOK.md` exactly. Inputs: cluster charter + UNSOLVED_REGISTER +
the Phase-1 assignee lists. Output: `30_PATENTS/PL_<Pnn>_<slug>.md` + `PL_<Pnn>_patents.json`
(fragment; orchestrator merges into `patent_ledger.json` after each wave, deduping families).
Per cluster: **15-25 fetch-verified patents** (US+CN mix; include the 3-8 most blocking with
independent-claim gists), assignee × filing-year picture, expiry/status notes (mark status
"as displayed — verify before reliance"), and **3-6 whitespace hypotheses** each explicitly
tied to U-### entries where possible. Wave 1: P01-P05 (C12 side). Wave 2: P06-P10 (C10 side).
Merge ledger; update state.

## Phase 3 — Whitespace adjudication (orchestrator)
Cross UNSOLVED_REGISTER × the ten PL files → `40_WHITESPACE/WHITESPACE_REGISTER.md`:
15-25 W-## entries, each: gap statement; linked U-###; nearest prior art (P-### + one-line
distance); scores on the rubric below; **call: INVENT (feeds Phase 4) / TRADE-SECRET
(protect as data/process secret, do not file) / MONITOR (real gap, wrong owner or wrong
window)**. Select the top 10-14 INVENT slots balancing: >= 4 C12-side, >= 4 C10-side, >= 2
software/data-method, >= 1 joint C12×C10 (e.g., winding-cell ↔ converter/QC interface).

**Whitespace rubric (0-5 each, /25):** Demand evidence (strength of U-### links) · Openness
(prior-art distance in BOTH US and CN) · Founder buildability <= $25K on personal resources ·
Moat value to the 2029 wedge (does a granted claim actually block the incumbent response
paths named in Phase 1?) · Two-jurisdiction viability (claim type filable US+CN;
software/method claims note CN examination posture).

## Phase 4 — Invention disclosures (4 × `invention-designer` per wave; then 5 × `ip-redteam` per wave)
For each selected W-slot, one designer writes `50_INVENTIONS/ID_<nn>_<slug>.md` per the
11-part template in DELIVERABLES_SPEC (problem→concept→plain-language claim sketch→
embodiments→<= $25K build plan→Stanford/UIUC wall assessment→patent-vs-secret call→
publish/file sequencing→US/CN route incl. CN utility-model dual-filing option→design-around
resistance→counsel questions). Then EVERY disclosure gets `50_INVENTIONS/IPRT_<nn>.md` from
`ip-redteam`: hunt >= 3 closer prior-art references (fetch them; add to ledgers), obviousness
attack, enablement/budget realism, Stanford-contamination probe, design-around ease, strategic
value; verdict FILE-CANDIDATE / REWORK / DROP. Orchestrator reworks REWORKs once (designer
pass 2) or demotes to DROP. Alternate designer and red-team waves until all slots resolved.

## Phase 5 — Strategy synthesis (orchestrator; these are the files the founder reads)
1. `60_STRATEGY/STRATEGY_C12.md` (2,000-3,000 words): positioning & wedge restated on Phase-1
   evidence; product staging (v1 machine scope → C33 QC module → recipe/traceability SW);
   moat architecture = FILE-CANDIDATE patents + trade-secret register + data flywheel +
   reference customers; GTM refresh naming which competitor weaknesses (by CS-card) each play
   exploits; pricing posture vs verified price signals; 2026-2028 PhD-period action plan with
   IP sequencing woven into the existing validation experiments; updated risk/kill deltas
   (only deltas — Round-1 gates stay frozen).
2. `60_STRATEGY/STRATEGY_C10.md` (same structure; include the CERN-folder licensing decision,
   the Kepco-gap finding if verified, and the C11 absorption plan).
3. `60_STRATEGY/CLUSTER_PLAYBOOK.md` (1,000-1,800 words): C12↔C10 sequencing (which leads,
   shared customers, one company vs two products), shared-bench economics, hiring plan
   deltas, and the **ASC-2026 interview script additions**: 8-15 questions derived directly
   from U-### entries and ID disclosures (probe willingness-to-pay on the specific gaps).
4. `60_STRATEGY/IP_ROADMAP_2026_2029.md`: quarter-by-quarter filing calendar (provisionals →
   12-month conversions/PCT → CN national phase/utility models) reconciled with the
   publication plans; cost table built from **fetched current** USPTO/CNIPA/WIPO fee pages
   (verify — do not trust remembered fees) plus attorney-cost bands marked estimate; entity &
   assignment plan (individual/personal-LLC filings → assign to NewCo at founding);
   trade-secret register with handling rules; micro-entity caveats.
5. `60_STRATEGY/00_EXEC_BRIEF.md` (<= 900 words): the whole round on two pages — top unsolved
   problems, top whitespace, the FILE-CANDIDATE list with dates and costs, the three
   strategy calls, and what to do in 2026-H2.
6. Regenerate `90_BIBLIOGRAPHY/BIBLIOGRAPHY.md` (tier-grouped, zh bilingual) and a
   human-readable `30_PATENTS/PATENT_INDEX.md` (by cluster, then assignee).

## Phase 6 — Audit & fix (`source-auditor`, then orchestrator)
`99_AUDIT/FINAL_AUDIT.md`: **patent re-fetch audit** — 15 random ledger records re-fetched,
title+assignee must match (any mismatch = find and fix the corruption, then re-sample);
15 random non-patent citations re-fetched; quotas (>= 150 patents, >= 50 CN, >= 120 fresh
sources, tier mix per standards); **Stanford-wall table** — every ID_nn listed with its wall
verdict and the rule-6 sequencing line; disclaimer-header presence check on all 40/50/60
files; Magnefy/HTS-drift scan; deliverables checklist. Fix, re-check, set
`"mission":"COMPLETE"`, print the FILE-CANDIDATE list + 00_EXEC_BRIEF path + file map.
