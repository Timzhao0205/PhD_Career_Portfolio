# Stage 30 - Literature review: sensor types (commercial + pioneering)

ultrathink

This is the intellectual core of Section 2. Read `docs/PROJECT_BRIEF.md`
(section 3 lists the families to cover), `refs_raw/00_seed.jsonl` (reuse these
anchors), and `outputs/00_target_journal_brief.md` if present.

Produce a sourced, annotated brief at `outputs/30_litreview_sensor_types.md`
covering EVERY family in the brief's taxonomy. This is not final prose - it is a
citation-carrying research brief the author will write from. For EACH family:

1. **Operating principle** - 2-4 sentences, physically correct.
2. **Performance envelope** - field range, resolution / noise floor (with units,
   e.g. pT/√Hz), bandwidth, and where relevant offset/《drift》, linearity,
   dynamic range. Every number cited; if you cannot source a number, say so
   rather than inventing one.
3. **Strengths** and **weaknesses / failure modes** - honest, specific.
4. **Commercial maturity** - mass-market / niche / lab-only, with representative
   devices or vendors (tag vendor sources `[VENDOR]`; they support device facts,
   not performance claims used as peer-reviewed evidence).
5. **Pioneering directions** - what recent peer-reviewed work is pushing (last
   ~5 years), e.g. wide-bandgap GaN Hall, sub-pT TMR for biomagnetics, NV
   ensembles, chip-scale OPM, magnetoelectric arrays.
6. **Key references** - 3-8 per family, peer-reviewed preferred. Log each to
   `refs_raw/30.jsonl` per the shared schema.

Cover at least: Hall (Si + GaN/2DEG, spinning-current), AMR, GMR (spin-valve),
TMR/MTJ, fluxgate, search-coil/induction, GMI, SQUID, OPM/SERF, NV-diamond,
magnetoelectric, MEMS/Lorentz, and fiber-optic / magneto-optic (at least briefly).
Note resonance magnetometers (proton/Overhauser, CPT) in a short paragraph.

Then build a **comparison table** (markdown) with columns: family | principle |
field range | resolution/noise | bandwidth | size/power | cost tier | maturity |
typical domains | key refs. Populate only with sourced values; use "n/r" (not
reported) rather than guessing.

Quality bar: this is where wrong numbers or invented citations do the most
damage. Prefer recent review articles and primary papers from IEEE, APS, AIP,
Nature, IOP, MDPI, Wiley/Springer. Use arXiv only to find work, then cite the
version of record. Aim for roughly 40-70 distinct, real sources across the
families. Finish by writing the file and its refs log.
