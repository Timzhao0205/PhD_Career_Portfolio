# Stage 60 - Standards + business/investor potential

think hard

Read `docs/PROJECT_BRIEF.md` (section 6), `refs_raw/00_seed.jsonl`, and prior
outputs if present. This section serves a business+investor audience, so it must
be accurate about standards and disciplined about separating sourced facts from
framing/estimates.

Produce `outputs/60_standards_and_business.md` in two parts.

## Part A - Standards & qualification landscape
Explain, with citations, the standards that gate magnetic-sensor products in each
setting, and what each one requires at a level useful to a non-specialist
decision-maker:
- **Automotive / functional safety**: ISO 26262 (ASIL, SEooC, redundancy &
  diagnostics for position/current sensors), its IEC 61508 parent, ISO/PAS 21448
  (SOTIF), ISO/SAE 21434 (cybersecurity), and where ML complicates certification
  (link to Stage 50; cite the ISO 26262-vs-ML analyses).
- **Industrial**: IEC 61508, IEC 62443 (OT security), and relevant EMC / sensor
  interface standards.
- **Medical**: IEC 60601, ISO 13485, ISO 14971, and the FDA/CE regulatory framing
  for magnetic biosensing / MEG devices.
- **Metrology / traceability**: calibration to NIST/PTB magnetic references,
  field standards, and uncertainty budgeting.
Cite the standards bodies directly (ISO/IEC/IEEE/NIST pages) and any
peer-reviewed analyses. Note emerging AI-assurance standards (e.g. ISO/IEC work
on AI, automotive ML safety) where relevant, clearly labeled as emerging.

## Part B - Potential (business & investor read)
- **TRL ladder per sensor family** - a defensible maturity read (tie to Stage 30);
  label your TRL assignments as an assessment, not a cited fact.
- **Market framing** - cite reputable market/industry analyses for magnetic
  sensor market size/《growth》and key segments; state figures as reported and
  attribute them; DO NOT invent numbers. If only paywalled press summaries exist,
  report the summarized figure with its source and a caution.
- **Competitive / IP signals** - major suppliers and any notable patent/《M&A》
  trends you can source; keep it factual.
- **Risk & de-risking checklist** - qualification burden, supply chain,
  temperature/《radiation》robustness, calibration transfer, standardization gaps
  for ML-enabled sensing - what an investor should probe.

Include a table: standard | domain | what it governs | why it matters to a
buyer/investor. Log every source to `refs_raw/60.jsonl`; tag market-research and
vendor sources appropriately (`[VENDOR]` / market-report), and keep peer-reviewed
vs grey-literature clearly separated. Finish by writing the file and its refs log.
