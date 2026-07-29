# SELF_CHECK — B20_align (PILOT SAMPLE — NOT FINAL)

Stage: `B20_align` | Mode: `PILOT` | Attempt: `1`
Named worker: `pap06-fable-xhigh` | Requested: Fable 5 / xhigh

Checklist against the task card and stage specification. PASS/FAIL with
disclosures; no failure is concealed.

1. **All 6 required files present and pilot-labeled.** PASS.
   ALIGNMENT.csv (leading `# PILOT SAMPLE — NOT FINAL` comment row),
   ALIGNMENT.md, IMPACT_MAP.md, SOURCES.csv (pilot-label comment row),
   RUN_META.md, SELF_CHECK.md — every file carries the banner. All written
   only inside `pilot/B20_align/attempt-1/`; nothing written elsewhere.
2. **Exactly six ideas, spanning all four alignment classes.** PASS.
   6 data rows in ALIGNMENT.csv. Overall classes (ALIGNMENT.md §3):
   STRONG P3R2-D-02; MEDIUM P3R2-D-01, P3R2-A-14; WEAK P3R2-C-13,
   P3R2-C-07; ADVERSE P3R2-D-10. At least one of each required class,
   including one clearly adverse (D-10, negative interference in both
   directions). Selection rationale recorded (ALIGNMENT.md §1) and spans
   triple-final members, a verified split decision, and a killed idea, and
   spans domains near (D-02, D-01) to far (D-10, C-07) from the PhD.
3. **Both directions analyzed per idea.** PASS. ALIGNMENT.csv carries
   separate `phd_to_startup` and `startup_to_phd` classifications with a
   shared mechanism cell; IMPACT_MAP.md §1 gives per-idea chains in both
   directions covering moat/credibility/data/tools/buyer access/validation/
   timing/constraints/opportunity cost (forward) and requirements/
   experiments/datasets/collaborators/publication risk/scope drift/
   conflicts/research value (reverse) where each is material.
4. **Idea records actually read before judging.** PASS with disclosure.
   Each of the six ideas' defining record was read this run (list in
   RUN_META). Disclosed: D04 and D06 read through mechanism-bearing
   sections only; old06 DD_P3R2_A_14.md not read (new06 D06 used as A-14's
   record); old06 D-02/D-01 deep dives skimmed for concept confirmation.
5. **Every material technical claim mapped to B15 evidence or stronger.**
   PASS. Evidence cells cite B15 rows (EV01/06/11/13/23/25/26/27/30/31/34/
   35) and only B15-adjudicated papers (P0008, P0017, P0033, P0038, P0046,
   P0050 — all opened/adjudicated by B15, none cited merely because B12
   found it); PhD-side facts cite B10 claims (Cxx); current-market facts
   cite A30-verified opened primaries (A30:D10-DIS-01..03,
   A30:C07-DIS-01..02) or sources opened this run (S-B20-01/02). Where a
   fact is corpus-record-only (TapeStar sensor count; REBCO ramp figures;
   SPARC/superhot schedules) it is explicitly labeled as such with
   refresh-sensitivity disclosed, not silently upgraded.
6. **Stable idea IDs verbatim.** PASS. `P3R2-D-02`, `P3R2-D-01`,
   `P3R2-A-14`, `P3R2-C-13`, `P3R2-D-10`, `P3R2-C-07` — exactly as in
   A30's COMPARE.json membership/rank tables and the corpora's own files.
7. **At least two with-Opt2/without-Opt2 counterfactuals.** PASS.
   IMPACT_MAP.md §2 (P3R2-D-02, full), §3 (P3R2-D-01, full), plus §4
   (P3R2-D-10 as a deliberate zero-delta control). Each distinguishes what
   changes causally from what merely correlates, and each names which Opt2
   element does the causal work.
8. **No causation from thematic similarity.** PASS. The rule is applied
   explicitly: C-13 (shared "GaN" vocabulary) and D-10 (shared
   "control/estimation" vocabulary) are classified weak/adverse because no
   mechanism survives; D-01's "fusion magnet" affinity is shown to be
   milieu correlation with a small causal core; D-02's strength is argued
   from a concrete mechanism (Hall array + traceable calibration), not
   from its fusion theme. ALIGNMENT.md §7 records that thematic proximity
   predicted alignment poorly in this sample.
9. **Schema exact.** PASS. ALIGNMENT.csv header is exactly
   `idea_id,idea_name,source_version,phd_to_startup,startup_to_phd,mechanism,evidence,dependency,time_horizon,conflict,confidence,falsifier,action`
   with one leading comment row and exactly 6 data rows (comma-containing
   fields quoted). SOURCES.csv header is exactly
   `claim_id,url,title,publisher,published_date,accessed_date,source_type,stage_file,confidence,limitation`
   with a pilot-label comment row, 2 opened-source rows, and two
   disclosure comment lines (failed opens; discovery-only searches).
10. **Web-source rule.** PASS. The two load-bearing current-market claims
    this pilot's own judgments lean on directly (the TapeStar incumbent
    class for D-02's mechanism; the merchant HTS magnet market for
    D-01/D-02 timing) were opened this run; remaining current-market facts
    are honestly attributed to A30's verified opened primaries or labeled
    corpus-dated. Search snippets were treated as discovery only.
11. **Internal consistency.** PASS. Direction classes, overall classes,
    mechanisms, dependencies, and counterfactuals are consistent across
    ALIGNMENT.csv, ALIGNMENT.md, and IMPACT_MAP.md (checked row by row);
    the C-07 weak/adverse and A-14 medium/weak boundary judgments are
    flagged identically in both files, with the rubric distinction
    (idea-specific interference vs generic opportunity cost) stated in
    ALIGNMENT.md §2.
12. **No fabrication.** PASS to the best of this worker's verification:
    no idea record, mechanism, market fact, measurement, citation, DOI, or
    model-identity claim was invented; every quoted figure traces to a
    named record; requested vs observed model/effort kept separate in
    RUN_META (observed effort NOT_EXPOSED; observed model recorded as
    self-declared only).
13. **Scope discipline.** PASS. No startup ranking, no portfolio decision,
    no venture-viability verdict beyond quoting corpus kill rules; support-
    stage founder-fit overstatements were corrected (new06 D01 §14, D04)
    rather than repeated. Immutable material untouched; A30's
    reconciliation consumed, not re-derived (per B00 handoff note).

**Known limitations (disclosed, not failures):** pilot sample is
deliberately non-representative; two records read partially; TapeStar
detailed specs unverified (protected datasheet); Opt2 mechanisms inherit
folder-08 pre-redteam status (C40) and the C50 provenance caveat; exact
run clock times not available to this worker.
