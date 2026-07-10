# Stage 70 — Bibliography Verification & Formatting Report

Source: `refs_raw/00_seed.jsonl` (16), `refs_raw/00.jsonl` (5), `refs_raw/30.jsonl` (40),
`refs_raw/40.jsonl` (24), `refs_raw/50.jsonl` (24), `refs_raw/60.jsonl` (15) — 124 raw lines,
123 distinct keys, 2 duplicate sources merged → **122 unique references**.

Outputs: `outputs/references.bib`, `outputs/reference_registry.csv`, this report.

## Totals by status

| Status | Count |
|---|---|
| Peer-reviewed journal | 80 |
| Vendor-grey (datasheets, product/press pages) | 16 |
| Standard (ISO/IEC/SAE/CISPR/national-metrology) | 13 |
| Preprint (arXiv, no version of record found) | 4 |
| Market-report-grey | 2 |
| Edited book chapter | 2 |
| Peer-reviewed conference | 2 |
| Conference, marked non-peer-reviewed by source (AIAA) | 2 |
| Book (monograph) | 1 |
| **Total** | **122** |

Non-journal, non-standard total (preprint + vendor-grey + market-report-grey +
non-peer-reviewed conference): **24 / 122 (~20%)**.

## Duplicates merged

1. **`TMRsubpT2025APL`** — identical key appeared in both `00_seed.jsonl` (line 10:
   blank authors, blank DOI) and `30.jsonl` (line 12: authors "Nakano; et al.",
   DOI `10.1063/5.0263879`, note "Seed key enriched this run: DOI and first
   author verified via Crossref"). Kept the richer `30.jsonl` version. Re-verified
   independently: `https://doi.org/10.1063/5.0263879` redirects to
   `pubs.aip.org/apl/.../Tunnel-magnetoresistance-sensors-with-sub-pT`, URL slug
   matches the title, confirming *Applied Physics Letters* vol. 126, art. 160503
   (2025).
2. **`GVRmagsensormarket`** (in `40.jsonl`) and **`GrandView2025magmarket`** (in
   `60.jsonl`) — same URL (`grandviewresearch.com/industry-analysis/magnetic-sensors-market`),
   same publisher, re-scraped at different times (2024-vintage estimate vs.
   2025-vintage report). Merged into one entry under the key
   `GrandView2025magmarket`, keeping the more specific 2025 figures (USD 3.03B in
   2024 → USD 4.39B by 2030, 6.4% CAGR, Hall sensors ~29% share) as primary.
   `sections_used` on the merged row records both `applications` and
   `standards/business` since the same market-size figure is usable in either
   section.
3. **No other duplicates found.** Checked all 124 raw lines for repeated DOIs
   (none found beyond the TMR case above) and for title/topic overlap between
   plausibly similar-sounding entries (e.g. Ripka's two separate fluxgate/general
   review papers, several distinct "digital twin" papers, the Grand View vs.
   Market Research Future market reports which cover different market scopes —
   general magnetic sensors vs. automotive-only) — all confirmed to be genuinely
   distinct works, not duplicates.

## DOI verification performed

Per the prioritization rule, most of the entries on the task's example
"candidate" list (Popovic2004hallbook, Munter1990spinning, Crescentini2022hallcurrent,
Treutler2001automotive, Zheng2019mrroadmap, Egelhoff2009picoteslaMTJ,
Ripka2003fluxgateadv, Ge2016overhauser, Tumanski2007inductioncoil,
Roux2008themisSCM, Coillot2010dualband, Phan2008gmiprogress,
Dolabdjian2016gmichapter, Uchiyama2020picoteslaMI, Fagaly2006squidRSI,
Clarke2018squidfocus, Kominis2003subfemtotesla, Shah2007microfabvapor,
Boto2018wearableMEG, Kitching2018chipscaleatomic, NVsub10pT2024prapplied)
turned out, on actually loading their JSONL records, to **already have a
populated DOI field** — confirming the task's own warning not to trust that
list from memory. These were left as-is (not re-fetched individually; two of
them, Lenz2006magsensors and Kominis2003subfemtotesla, were spot-checked below
as stand-ins for the broader "high-confidence" population).

Entries that genuinely had a **blank DOI** and needed active verification:

- **`Tumanski2013modern`** (journal, *Przeglad Elektrotechniczny*, 2013) — ran a
  Crossref bibliographic search and a title+author query; both returned only
  other Tumanski works (his 2007 induction-coil review, a 2001 monograph, and
  unrelated Przeglad Elektrotechniczny articles by other authors). No Crossref
  record exists for this exact title/venue/year. Przeglad Elektrotechniczny is a
  Polish engineering trade journal with sparse Crossref/DOI coverage historically.
  **DOI left blank**, per the no-fabrication rule.
- **`NVcurrentPPM2023`** (arXiv:2304.07998) — fetched the arXiv abstract page:
  no `journal-ref` field, only an arXiv-issued DataCite DOI
  (`10.48550/arXiv.2304.07998`), which is **not** a journal DOI and was not
  inserted. No peer-reviewed version of record found; remains preprint-only.
- **`Salay2018ISO26262ML`** (arXiv:1709.02435) — same check; no journal-ref.
  The seed data's venue field speculated "SAE Technical Paper (verify)"; no SAE
  publication could be confirmed, so the venue was corrected to plain "arXiv"
  rather than retaining an unconfirmed SAE citation. No version of record found.
- **`PGTLNet2024preprint`** (arXiv:2401.09631) — no journal-ref; page notes
  acceptance at the NeurIPS 2023 "ML and the Physical Sciences" **workshop**
  (non-archival, not a formal proceedings entry). No peer-reviewed version of
  record found.
- **`SLCAMma2026preprint`** (arXiv:2604.19946) — page exists, submitted 21 Apr
  2026; no journal-ref, no version of record found (expected given how recent
  it is).
- **`Gnadt2022magnavcal`** and **`Glaessgen2012dtparadigm`** — both AIAA
  conference papers (already had DOIs `10.2514/6.2022-1760` and
  `10.2514/6.2012-1818`). Confirmed both DOIs resolve via `doi.org` redirect to
  `arc.aiaa.org` matching records. Source data explicitly flags
  `peer_reviewed:false` for both; retained that flag rather than override it,
  since AIAA SciTech/SDM papers of this type undergo abstract-level review, not
  full journal peer review.

Spot-checks on already-populated, high-confidence DOIs (per the instruction not
to re-verify everything): `Lenz2006magsensors` (10.1109/JSEN.2006.874493,
resolves to ieeexplore.ieee.org) and `Kominis2003subfemtotesla`
(10.1038/nature01484, resolves to nature.com/articles/nature01484) — both
confirmed resolvable and consistent with source metadata.

## Flagged: everything not peer-reviewed-journal/standard

### Preprints (4) — no version of record found for any
| Key | How used | Substitute needed? |
|---|---|---|
| NVcurrentPPM2023 | Discovery example of an integrated NV current sensor (ppm-scale) in the applications section | No confirmed peer-reviewed VoR found; note remains a preprint-sourced claim — flag for author's own knowledge of any 2024–26 follow-up publication before submission |
| Salay2018ISO26262ML | ISO 26262 / ML-safety gap analysis in standards section | No VoR found; consider citing a more recent peer-reviewed ISO 26262 + ML safety paper if the author knows one, otherwise keep with preprint caveat |
| PGTLNet2024preprint | Physics-informed aeromagnetic compensation example in future-methods section | Workshop-only (NeurIPS ML4PS), non-archival; no VoR — used for discovery/illustration only, as instructed |
| SLCAMma2026preprint | Magnetometer-array SLAM example in future-methods section | Too recent (Apr 2026) for a VoR to plausibly exist yet; discovery-only per source's own low-confidence flag |

### Conference papers marked non-peer-reviewed by source (2)
| Key | How used | Substitute needed? |
|---|---|---|
| Gnadt2022magnavcal | ML-enhanced magnetic calibration for airborne navigation, future-methods section | DOI resolves and record is legitimate; no substitute needed — cited for a specific case study, not general authority |
| Glaessgen2012dtparadigm | Origin/priority citation for the "digital twin" concept, future-methods section | No substitute needed — this is the historically correct origin citation regardless of peer-review tier |

### Vendor-grey (16) — product pages, datasheets, press releases; all clearly usable only as illustrative/market-context material, not as technical evidence
GEMOverhauserVendor, AllegroTMRcurrentVendor, InfineonCurrentSensorVendor,
LEMbatterycurrentVendor, MDTangleVendor, AllegroABSVendor, MDTencoderVendor,
STeCompassVendor, Allegro2023crocus, TDK2016micronas, RicohMEG2024clearance,
plus the 5 MDPI publisher-policy pages (MDPI2026SensorsIfA,
MDPI2026SensorsPublguid, MDPI2024RefGuideV10, MDPI2026AIAuthorship,
MDPI2026SensorsAPC) — the latter five are house-keeping citations for journal
formatting requirements, not content claims, so no substitute is applicable or
needed. The 11 product/press items are appropriately used only for
illustrative vendor examples and industry-history anecdotes in the
applications/standards-business sections; no peer-reviewed substitute exists
for this kind of information by nature (product specs, M&A history, regulatory
clearance announcements).

### Market-report-grey (2)
| Key | How used | Substitute needed? |
|---|---|---|
| GrandView2025magmarket (merged) | Market-size figures for the business/potential section | No — market-size numbers are inherently commercial-analyst territory; already labeled as estimate |
| MRFRautomotivemarket | Automotive-segment market sizing, applications/business section | Same as above |

### Book/monograph (1)
`Popovic2004hallbook` — standard Hall-sensor-physics reference text; correctly
has no DOI-substitute issue (DOI present).

## Metadata that could not be fully confirmed

- **`Tumanski2013modern`** — DOI could not be found/confirmed (see above); all
  other fields (title, author, year, venue, volume, pages) retained from the
  original source record since they were internally consistent and the paper's
  existence is corroborated by a Semantic Scholar record (URL retained), even
  though that page could not be re-rendered via fetch for a second independent
  check.
- **`Jauch2026mlquantmag`** — source note states "title/venue Crossref-verified;
  full text not retrieved," confidence left at the source's own "low" rating;
  not independently re-verified this run given the deep-verification budget was
  allocated to blank-DOI entries.
- Several entries (`Fluxgate2021Sensors`, `MagSensorsReview2021ERX`,
  `JEET2019lownoisehall`, `SerialMTJ2020sensors`, `SiHall3axis2025msn`,
  `SERFhybridcell2024msn`, `NVmicrowave2023prapplied`, `NVsub10pT2024prapplied`,
  `Spintronic2024npj`, `QuartzME2022symmetry`) carry **blank author fields** in
  the original source data (the automated collection step evidently didn't
  extract an author list for these, even though DOIs were captured). Author
  fields were left blank/"Anon." in outputs rather than guessed; flagged here so
  the author can fill them in from the DOI landing pages before submission if
  full author lists are wanted in-text.
- `TDK2016micronas` — the citation key implies 2016 but the source record's
  `year` field is 2015; retained the source's year value rather than silently
  "correcting" it, per the house rule against inventing/correcting values
  without confirmation.

## Notes on classification choices
- AIAA conference papers (`Gnadt2022magnavcal`, `Glaessgen2012dtparadigm`) don't
  cleanly fit the requested five-way taxonomy; classified as "conference,
  marked non-peer-reviewed by source" rather than silently promoted to
  "peer-reviewed conference," honoring the explicit `peer_reviewed:false` flag
  already present in the raw data.
- `Popovic2004hallbook` is a single-author monograph, not an edited-volume
  chapter, so it was given its own "book (monograph)" bucket distinct from
  `Zhou2022TMRchapter` and `Dolabdjian2016gmichapter`, which are genuine chapters
  in edited/multi-author volumes.
