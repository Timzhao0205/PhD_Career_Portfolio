# A10_blind FULL run — method, rubric, and 126/126 coverage proof

- Stage: `A10_blind`
- Mode: `FULL`
- Attempt: `1`
- Worker: `pap06-fable-xhigh` (requested Fable 5 / xhigh)

## Independence statements

- **No prior rankings were read.** I did not read any old or new output, any
  prior-stage output, any prior ranking, `sources/`, `archive/`,
  `verification/`, or the pilot directory's `SELECTION`/`TOP10`/`METHOD`
  content. The rubric below was constructed directly from the stage
  specification (`workflow/stages/A10_blind.md`), not copied from the pilot.
- **No web was used.** No WebSearch and no WebFetch calls were made at any
  point in this stage.
- **Inputs actually read:** `evidence/blind/MANIFEST.json`,
  `evidence/blind/POOL_1.json`, `evidence/blind/POOL_2.json`,
  `evidence/blind/POOL_3.json` (each shard read in full via windowed reads
  until exhausted), plus the root policy files (`SOURCE_POLICY.md`,
  `LIT_POLICY.md`, `MODEL_POLICY.md`, `MODEL_PLAN.md`), `state/CURRENT_TASK.md`
  and the stage specification.
- All judgments rely only on each candidate's own record content (including
  its self-flagged caveats). Source IDs quoted (e.g., `L02-043`) are quoted as
  they appear inside candidate records; I did not verify them externally.

## Rubric (applied to all 126 candidates)

Nine components, scored as coarse ordinal integers 1–5 with a written reason
per component for every selected object. Higher is always better. No decimals,
no weighted totals, no pseudo-precise sums — ranks are holistic ordinal
judgments informed by the component pattern.

1. **severity_and_budgeted_buyer_pain** — is the pain severe, documented in
   the record, and attached to money already budgeted or being spent (orders,
   tenders, grants, backlogs), rather than hypothetical?
2. **technical_feasibility** — TRL as stated, whether the core claim rests on
   demonstrated art vs. modeled-only physics, and integration difficulty.
3. **defensible_edge** — moat quality: datasets, qualification dossiers,
   standards positions, process know-how; discounted where the record itself
   names incumbents able to absorb the wedge.
4. **founder_phd_adjacency** — judged strictly non-circularly: only whether
   the candidate's *own* 2026–2029 pre-company plan is executable in a
   university research setting (equipment scale, budget, publishability,
   partner access), with no assumption about any particular founder's
   background or skills.
5. **capital_time_to_falsification** — first-experiment budget, decisiveness
   of the stated experiment, and v1 capital range; cheap, early, binary
   falsification scores high.
6. **timing_2030_2034** — does the record's own demand-trigger evidence place
   purchasable demand inside 2030–2034 for a company started ~2030, neither
   too early (research-stage buyers) nor too late (commoditized)?
7. **geographic_portability** — breadth and realism of beachhead plus
   secondary markets; CN-only or single-buyer-country plays score low;
   license-only legs counted as partial.
8. **regulatory_safety_friction** — 5 = minimal friction; export-control
   partitions, ITAR, clinical/class-society/utility certification, and
   dual-use review reduce the score.
9. **failure_modes** — 5 = failure modes diffuse across independent demand
   legs with explicit kill gates; 1 = a single fatal, unmitigable external
   dependency.

Per selected object I additionally recorded `uncertainty` (the dominant
unknown), `principal_risk` (the most likely kill), and `falsifier` (the
concrete observable that would disprove the thesis, drawn from the record's
own first experiment or gates).

## Selection procedure

1. Read all 126 records in full, shard by shard.
2. Grouped near-duplicates: this pool contains multiple generations of the
   same concept (A/B seeds, C/D/E merged refinements, F/G later variants),
   with many records explicitly stating what they merged or absorbed. Where a
   cluster exists, I selected at most one representative — normally the merged
   or most disciplined variant — and recorded the others as
   duplicate-superseded rather than pretending the pool holds 126 independent
   ideas.
3. Applied the rubric to every candidate; selected the 24 with the strongest
   holistic pattern, deliberately diversifying across sectors (datacenter
   power/thermal, superconducting systems, pulsed power/beams, semiconductor
   subsystems, electrochemical power, heavy electrification, space, photonics,
   harsh-environment electronics) so the shortlist is a portfolio, not one
   thesis repeated.
4. Ranked 1–24 holistically; TOP10 = ranks 1–10.

## Tie handling

Where two candidates showed comparable component patterns, ties were broken in
this order: (a) lower capital and faster/cheaper decisive falsification;
(b) stronger already-paid (vs. anticipated or inferential) demand evidence in
the record itself; (c) fewer single-point external contingencies (policy,
export-control, single-program, or single-fluid dependencies); (d) better
geographic portability. Example applications: D-02 over C-11/B-10 (same
concept, cheapest falsification); E-01 over C-01 (same concept, lower capital
and cleaner export posture); C-09 over D-05/E-05/A-07/B-09 (the merged
platform that absorbs the others); D-09 over C-10/A-08 (lowest-capital merged
variant).

## Coverage proof — all 126 IDs by shard with disposition

Disposition codes for not-selected candidates:

- `DUP-MERGED` — superseded by a selected merged/refined variant of the same concept
- `DUP-UNSEL` — near-duplicate of another record; the cluster's chosen representative is listed
- `CONTINGENT` — demand depends on an unproven contingency/gate that the record itself flags
- `ACCESS` — China-access / export-control / JV-licensing constraints dominate
- `INCUMBENT` — incumbent strength or commoditization risk dominates
- `NICHE` — market too small, lumpy, or single-buyer for this 24-slot shortlist
- `PHYSICS-OPT` — TRL 2–3 option purchase whose core claim is modeled-only
- `CAPEX-GATE` — heavy capital behind a blocked/uncertain category gate
- `WEAK-EV` — record self-flags stale, single-source, or inferential demand evidence
- `PROGRAM` — single government-program dependency

### Shard 1 — POOL_1.json (42 IDs)

| idea_id | Disposition |
|---|---|
| P3R2-A-01 | Not selected — DUP-MERGED: 800V rack protection cluster represented by selected P3R2-E-01 |
| P3R2-A-02 | **SELECTED — rank 19** |
| P3R2-A-03 | Not selected — CONTINGENT: record self-flags that EMT-model compliance may suffice (2027 gate kills seed); near-miss |
| P3R2-A-04 | Not selected — DUP-MERGED: quench protection cluster represented by selected P3R2-D-01 |
| P3R2-A-05 | **SELECTED — rank 17** |
| P3R2-A-06 | Not selected — DUP-MERGED: cryo I/O cluster represented by selected P3R2-E-04 |
| P3R2-A-07 | Not selected — DUP-MERGED: modulator cluster represented by selected P3R2-C-09 |
| P3R2-A-08 | Not selected — DUP-MERGED: UHDR dosimetry cluster represented by selected P3R2-D-09 |
| P3R2-A-09 | Not selected — CAPEX-GATE: $15-35M in-house sterilization cell with EtO regulatory driver flagged unsourced; theme absorbed by unselected D-08 |
| P3R2-A-10 | **SELECTED — rank 9** |
| P3R2-A-11 | Not selected — WEAK-EV: record self-flags thin technical base (two sources) and incumbent catch-up as the main risk |
| P3R2-A-12 | Not selected — DUP-MERGED: PCHE cluster represented by selected P3R2-C-08 |
| P3R2-A-13 | Not selected — DUP-MERGED: space PPU cluster represented by selected P3R2-E-10 |
| P3R2-A-14 | **SELECTED — rank 6** |
| P3R2-A-15 | Not selected — DUP-MERGED: thermal metrology cluster represented by selected P3R2-C-05 |
| P3R2-A-16 | Not selected — INCUMBENT: TIM giants can outspend and packagers may design around TIM1; kill-gated reliability delta unproven; near-miss |
| P3R2-A-17 | Not selected — DUP-MERGED: beam-combining cluster represented by selected P3R2-D-10 |
| P3R2-A-18 | Not selected — DUP-MERGED: laser-driver cluster represented by selected P3R2-C-13 |
| P3R2-A-19 | Not selected — DUP-MERGED: rectification cluster represented by selected P3R2-C-07 |
| P3R2-A-20 | Not selected — INCUMBENT: formation incumbents already ship recuperative products; wedge commoditizes before 2030 |
| P3R2-A-21 | Not selected — DUP-MERGED: MW charging cluster represented by selected P3R2-C-15 |
| P3R2-A-22 | Not selected — CONTINGENT: destruction-technology selection could tip to SCWO and verification methods unsettled; power-layer play C-14 selected instead |
| P3R2-B-01 | Not selected — DUP-MERGED: negative-pressure loop absorbed as primary variant of selected P3R2-C-04 |
| P3R2-B-02 | Not selected — DUP-MERGED: test-platform concept absorbed into selected P3R2-C-05 |
| P3R2-B-03 | Not selected — DUP-UNSEL + ACCESS: CN 800V inlet variant; cluster represented by P3R2-E-01; CN design-in access risk high |
| P3R2-B-04 | Not selected — ACCESS: CN protection stack needs CCC/GB JV lab and grid-layer access; cluster covered by A-02/E-14 |
| P3R2-B-05 | Not selected — ACCESS: record self-flags SEVERE export-control risk; cluster represented by P3R2-A-10 |
| P3R2-B-06 | Not selected — WEAK-EV: ESC demand trigger inferential (no named tender), record's own FIX condition |
| P3R2-B-07 | Not selected — DUP-MERGED: PCHE CN variant absorbed into selected P3R2-C-08 |
| P3R2-B-08 | Not selected — NICHE: record self-rates very narrow initial SAM, extra/optional seed |
| P3R2-B-09 | Not selected — DUP-MERGED: CN modulator variant absorbed into selected P3R2-C-09 |
| P3R2-B-10 | Not selected — DUP-MERGED: HTS QC cluster represented by selected P3R2-D-02 |
| P3R2-B-11 | Not selected — WEAK-EV: record self-rates optional pending CN cryo competitor mapping; cluster represented by P3R2-C-12 |
| P3R2-B-12 | Not selected — ACCESS + NICHE: CN-only licensing with lumpy approval-dependent (CEPC) demand |
| P3R2-B-13 | Not selected — DUP-MERGED: absorbed into selected P3R2-C-07; Sungrow kill-check flagged in-record |
| P3R2-B-14 | Not selected — CONTINGENT: record self-classifies as contingent option on standards non-convergence with pre-agreed fold into A-21/C-15 |
| P3R2-B-15 | Not selected — INCUMBENT: CN mid-market price-war risk; record demands differentiate-or-exit |
| P3R2-B-16 | Not selected — ACCESS: export-control scoping is the gating uncertainty plus China-only procurement; record confidence low-medium |
| P3R2-B-17 | Not selected — WEAK-EV: record self-flags CN demand as inferential, 'weakest link'; theme covered by selected P3R2-A-14 |
| P3R2-B-18 | Not selected — WEAK-EV: demand-bridge seed with no named CN buyer; flywheel theme also unselected as D-19 |
| P3R2-B-19 | Not selected — DUP-MERGED: absorbed into selected P3R2-C-13 |
| P3R2-B-20 | Not selected — WEAK-EV: record self-declares weakest-thesis discardable extra (2021-vintage data) |

### Shard 2 — POOL_2.json (42 IDs)

| idea_id | Disposition |
|---|---|
| P3R2-B-21 | Not selected — CONTINGENT: FTO-gated patent thicket, small ASP, record marks it a merge candidate |
| P3R2-B-22 | Not selected — WEAK-EV: record self-flags feature-not-product risk with license-out fallback |
| P3R2-C-01 | Not selected — DUP-UNSEL: same concept as selected P3R2-E-01 with added dual-entity complexity and higher capital ($8-20M) |
| P3R2-C-02 | Not selected — CONTINGENT: record codifies a fold-into-C-01 kill trigger if OCP/vendors spec an in-rack buffer by 2029 |
| P3R2-C-03 | Not selected — CAPEX-GATE: $25-60M behind a binding 2028 standards+procurement gate in a certification-blocked category |
| P3R2-C-04 | **SELECTED — rank 11** |
| P3R2-C-05 | **SELECTED — rank 2** |
| P3R2-C-06 | Not selected — DUP-UNSEL: TVW platform variant; cluster represented by P3R2-A-10 (vendor-neutral metrology wedge, lower capital than C-06's $12-30M head-on generator play) |
| P3R2-C-07 | **SELECTED — rank 10** |
| P3R2-C-08 | **SELECTED — rank 8** |
| P3R2-C-09 | **SELECTED — rank 4** |
| P3R2-C-10 | Not selected — DUP-UNSEL: UHDR dosimetry variant; cluster represented by P3R2-D-09 |
| P3R2-C-11 | Not selected — DUP-MERGED: acceptance-test systems absorbed into selected P3R2-D-02 |
| P3R2-C-12 | **SELECTED — rank 22** |
| P3R2-C-13 | **SELECTED — rank 24** |
| P3R2-C-14 | **SELECTED — rank 13** |
| P3R2-C-15 | **SELECTED — rank 18** |
| P3R2-C-16 | Not selected — DUP-MERGED: HIL compliance testing absorbed into selected P3R2-E-14 (CN license chapter) |
| P3R2-C-17 | Not selected — DUP-MERGED + ACCESS: quench cluster represented by P3R2-D-01; record self-flags poor export separability |
| P3R2-C-18 | Not selected — INCUMBENT: record self-declares highest commoditization risk in its batch (Vicor/Delta/Navitas field), discardable aggressive bet |
| P3R2-C-19 | Not selected — CONTINGENT: entirely levered to sCO2 commercialization pace; record holds it as an option behind machine-build signals |
| P3R2-C-20 | Not selected — DUP-MERGED: SSPA line folded into selected P3R2-C-09 per its own merge notes; gov-lab revenue lumpy |
| P3R2-C-21 | Not selected — INCUMBENT: record names Sungrow/Huawei-class as the hardest competitor set in batch; 2028 pilot gate unmet by design |
| P3R2-C-22 | **SELECTED — rank 15** |
| P3R2-D-01 | **SELECTED — rank 3** |
| P3R2-D-02 | **SELECTED — rank 5** |
| P3R2-D-03 | Not selected — DUP-MERGED: cryoplant skid absorbed into selected P3R2-C-12 |
| P3R2-D-04 | Not selected — CAPEX-GATE: $15-40M cryogenic feeder vs 'more copper' default and datacenter uptime-culture clash |
| P3R2-D-05 | Not selected — DUP-MERGED: open-interface Marx bricks absorbed into selected P3R2-C-09 |
| P3R2-D-06 | Not selected — PROGRAM: government-concentrated buyer base; record admits grants-not-products risk if next-gen Z slips |
| P3R2-D-07 | Not selected — CONTINGENT: retrofit-at-rebuild wedge with record's own 2029 license-or-fold decision point; near-miss |
| P3R2-D-08 | Not selected — CONTINGENT: record self-declares a working hypothesis with three load-bearing gated assumptions (EtO primary source, SSPA cost crossover, backlog persistence) |
| P3R2-D-09 | **SELECTED — rank 23** |
| P3R2-D-10 | **SELECTED — rank 14** |
| P3R2-D-11 | Not selected — PHYSICS-OPT: TRL 2, 5% CE is modeling-only; record itself frames it as an option purchase with acqui-license exit |
| P3R2-D-12 | Not selected — PHYSICS-OPT: EHD documented enthusiasm zone (no industrial deployment) plus hard fluid-intersection kill gate |
| P3R2-D-13 | Not selected — NICHE + PROGRAM: single-buyer-class defense LRU; conventional chillers suffice if lasers plateau at 150 kW; near-miss |
| P3R2-D-14 | Not selected — DUP-MERGED: 400C tier absorbed into selected P3R2-A-14 |
| P3R2-D-15 | Not selected — DUP-MERGED: PPU bricks absorbed into selected P3R2-E-10 |
| P3R2-D-16 | Not selected — PROGRAM: record holds it as option (studies only) behind FSP downselect/flight-contract checkpoint |
| P3R2-D-17 | Not selected — DUP-MERGED: cryo interconnect absorbed into selected P3R2-E-04 |
| P3R2-D-18 | Not selected — PROGRAM: single SBIR topic anchor; record's own FIX gate requires a second demand anchor |

### Shard 3 — POOL_3.json (42 IDs)

| idea_id | Disposition |
|---|---|
| P3R2-D-19 | Not selected — CONTINGENT: buffering niche must be measured, not asserted (record FIX); BESS substitution risk; near-miss |
| P3R2-D-20 | Not selected — CONTINGENT: demand hostage to liquid-metal architecture beating solid media (record's own kill gate) |
| P3R2-E-01 | **SELECTED — rank 1** |
| P3R2-E-02 | Not selected — DUP-MERGED: control layer with pre-agreed merge path into selected P3R2-C-04's loop stack; standalone OEM-appetite gate |
| P3R2-E-03 | Not selected — DUP-UNSEL: TVW retrofit variant; cluster represented by P3R2-A-10 |
| P3R2-E-04 | **SELECTED — rank 21** |
| P3R2-E-05 | Not selected — DUP-MERGED: modulator family absorbed into selected P3R2-C-09 |
| P3R2-E-06 | Not selected — INCUMBENT: record self-declares highest commoditization risk in its batch (CN recuperation-as-standard before 2030) |
| P3R2-E-07 | Not selected — DUP-MERGED: precursor-detection platform absorbed into selected P3R2-D-01 |
| P3R2-E-08 | Not selected — DUP-MERGED: PCHE line absorbed into selected P3R2-C-08 |
| P3R2-E-09 | Not selected — DUP-MERGED: packaging-first 300C platform absorbed into selected P3R2-A-14 |
| P3R2-E-10 | **SELECTED — rank 12** |
| P3R2-E-11 | Not selected — CONTINGENT: CPO volume ramp gated (LPO substitution monitor); Coherent as buyer-and-competitor problem |
| P3R2-E-12 | Not selected — DUP-UNSEL + PROGRAM: near-duplicate of D-18 with the same single-SBIR anchor |
| P3R2-E-13 | Not selected — DUP-UNSEL + PHYSICS-OPT: near-duplicate of D-11; CE modeled-only, single-customer concentration |
| P3R2-E-14 | **SELECTED — rank 7** |
| P3R2-F-01 | **SELECTED — rank 20** |
| P3R2-F-02 | **SELECTED — rank 16** |
| P3R2-F-03 | Not selected — INCUMBENT: record itself makes the Calnetix-class incumbent map a pre-promotion requirement the white-space claim must survive |
| P3R2-F-04 | Not selected — INCUMBENT: established merchant AMB vendors (SKF S2M/Calnetix/Waukesha); wedge must survive record's own teardown gate |
| P3R2-F-05 | Not selected — INCUMBENT: Dana/BAE/Danfoss/ZF teardown required; repower inference unevidenced per record |
| P3R2-F-06 | Not selected — CONTINGENT + INCUMBENT: merchant sensing exists only if third-party protection (E-14-class) wins; Hitachi/ABB optical-CT incumbency |
| P3R2-F-07 | Not selected — INCUMBENT: Staubli/Phoenix/Huber+Suhner map required; CN swap leg gated on procurement openness evidence |
| P3R2-F-08 | Not selected — CONTINGENT + CAPEX-GATE: gated on breaker adoption (L08-016 contradiction open); capital-intensive packaging |
| P3R2-F-09 | Not selected — NICHE: small TAM, conservative buyers; record itself questions whether primes buy reliability-critical parts merchant |
| P3R2-F-10 | Not selected — WEAK-EV: inline volumetric QC demand inferential (only the equipment channel documented); US leg de-weighted by record |
| P3R2-F-11 | Not selected — CONTINGENT: process-substitution play behind a binding 10,000-shot coil-life gate; laser welding is the real substitute |
| P3R2-F-12 | Not selected — ACCESS: CATL full-stack bundling risk; JV-only CN marine access |
| P3R2-F-13 | Not selected — ACCESS: foreign content in SOE mine-safety systems politically fragile; margin-thin licensing |
| P3R2-F-14 | Not selected — ACCESS: record calls the CN licensing lane an export-control and IP-leakage tightrope with built-in licensee kill risk |
| P3R2-F-15 | Not selected — CONTINGENT + ACCESS: audit-pressure trigger inferential; gap closable by rectifier vendors or stack OEMs; Sungrow kill signal |
| P3R2-F-16 | Not selected — INCUMBENT: commodity-floor risk (B-15 lesson cited in-record); metrology premium untested |
| P3R2-F-17 | Not selected — CONTINGENT: demand contingent on undated regulatory tightening; record prices it as an option purchase |
| P3R2-F-18 | Not selected — ACCESS + WEAK-EV: overlaps F-03 CN leg; single-source TAM; foreign IP in state-led program fragile |
| P3R2-F-19 | Not selected — WEAK-EV: direct pain evidence is inference from spec structure; crowded by 2032 per record; near-miss |
| P3R2-F-20 | Not selected — INCUMBENT: record downgrades the one-dominant-vendor thesis to judgment pending a broad competitor map (Spellman/AE/AMETEK/Matsusada et al.) |
| P3R2-F-21 | Not selected — DUP-MERGED + NICHE: record itself plans fold-in as entry SKU of selected P3R2-F-02 |
| P3R2-F-22 | Not selected — CAPEX-GATE + INCUMBENT: craft/capital-intensive manufacturing race against Comet; binding partner gate; F-01 merge pre-agreed |
| P3R2-F-23 | Not selected — CONTINGENT: anticipatory demand (developers buy only if lenders force it) behind a binding 2029 financier gate |
| P3R2-G-01 | Not selected — ACCESS + PROGRAM: CEPC-lumpy anchor (record itself cites the B-12 defect) with CN-only tender access |
| P3R2-G-02 | Not selected — WEAK-EV: component-level pain inferred, not documented (record's self-declared honest gap); JV copying risk priced |
| P3R2-G-03 | Not selected — CONTINGENT: third-party-acceptance willingness unproven (binding 2029 frame-agreement gates); near-miss |

**Coverage check:** Shard 1: 42 rows, 4 selected + 38 not selected. Shard 2:
42 rows, 14 selected + 28 not selected. Shard 3: 42 rows, 6 selected + 36 not
selected. Total 126 evaluated = 24 selected + 102 not selected. No duplicate
IDs, no missing IDs; every ID above appears exactly once and matches the
shards as stored.

## Selected 24 (rank order)

1. P3R2-E-01 — 800VDC rack power-path protection module
2. P3R2-C-05 — liquid-cooling thermal emulation/conformance metrology
3. P3R2-D-01 — HTS quench detection and protection subsystem
4. P3R2-C-09 — standardized solid-state pulsed-power platform
5. P3R2-D-02 — reel-to-reel REBCO tape acceptance metrology
6. P3R2-A-14 — 300C-class mixed-signal electronics platform
7. P3R2-E-14 — DC protection relay + neutral HIL qualification
8. P3R2-C-08 — thermal-shock-tolerant PCHE recuperators
9. P3R2-A-10 — vendor-neutral IEDF metrology + waveform bias control
10. P3R2-C-07 — low-ripple AFE rectification retrofits
11. P3R2-C-04 — PFAS-free pumped two-phase cooling loop
12. P3R2-E-10 — rad-tolerant GaN PPU platform
13. P3R2-C-14 — modular MW-class industrial plasma power
14. P3R2-D-10 — coherent-beam-combining phase-control engine
15. P3R2-C-22 — electrolyzer degradation/bankability test systems
16. P3R2-F-02 — superconducting-magnet electrical BOP platform
17. P3R2-A-05 — US merchant NEG-coating line
18. P3R2-C-15 — dual-standard megawatt charge/swap infrastructure
19. P3R2-A-02 — MVDC hybrid solid-state circuit breaker
20. P3R2-F-01 — solid-state microsecond impedance matching
21. P3R2-E-04 — high-density cryogenic interconnect loader
22. P3R2-C-12 — kW-class turbo-Brayton cryocoolers
23. P3R2-D-09 — UHDR/FLASH beam-current and dose metrology
24. P3R2-C-13 — precision GaN laser pump-driver modules

TOP10 = ranks 1–10 (see `TOP10.json`).

## Limitations

- **Record-only evidence.** All pain, market, competitor, and source-ID claims
  are taken from the candidate records themselves; the blind protocol forbids
  external verification, so any error in a record propagates into the scores.
  Where records self-flag stale, single-source, or inferential evidence, I
  treated that as a scoring input rather than re-verifying.
- **Duplicate-cluster judgment.** Cluster membership and "merged variant"
  identification are my reading of the records' own merge notes; a different
  reader could pick a different cluster representative (e.g., C-01 vs E-01,
  C-06 vs A-10). The disposition table makes each such choice explicit.
- **Ordinal, not cardinal.** Ranks are holistic ordinal judgments; adjacent
  ranks (e.g., 11–16) are close calls and should not be over-interpreted.
- **Non-circular adjacency scoring.** The founder/PhD-adjacency component
  deliberately measures only plan executability in a university setting as
  written in each record; it does not measure fit to any actual person, which
  is out of scope for this blind stage.
- **No web access** means 2026-vintage facts inside records (specs, orders,
  policies) were accepted as stated at their stated dates; several records
  themselves demand 2029 refreshes, which I echoed in uncertainties/falsifiers
  rather than resolving.
