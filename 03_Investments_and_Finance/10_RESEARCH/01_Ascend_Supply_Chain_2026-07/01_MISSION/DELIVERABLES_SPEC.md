# DELIVERABLES_SPEC

Dossier bar: a company gets a full dossier only if exposure_evidence would score >=3
(i.e., at least [REPORTED]-citing-filings). Concept-list names get a 5-line triage
note in 10_CHAIN_MAP instead, with what evidence WOULD promote them.

Required files at completion:
- 10_CHAIN_MAP/CHAIN_MAP_V1.md + per-tier sources JSON; BOM-per-rack model (may be a
  markdown table; no spreadsheet needed).
- 20_COMPANY_DOSSIERS/D_<ticker>_<name>.md + D_<ticker>_sources.json (template).
- 30_SCORING/SCORING_MATRIX.csv (filled) + SELECTION.md.
- 40_REDTEAM/RT_<ticker>.md for every selected name.
- 50_THESES/T_<ticker>_<name>.md for survivors, each with: thesis in <=3 sentences,
  variant perception (what I believe that the market doesn't, with evidence), scenario
  table (bear/base/bull with rough value math), pre-registered kill criteria (>=3,
  observable, dated), correlation statement, compliance table (COMPLIANCE_GATE section 4).
- 99_AUDIT/FINAL_AUDIT.md: traceability check, tier compliance stats, tag-change log.
- Append-only updates to ../../20_FINDINGS/ (WATCHLIST rows, LEDGER entries) - never
  set status 'actionable'.

Length discipline: dossiers <=2,500 words; theses <=1,200 words. Precision > volume.
