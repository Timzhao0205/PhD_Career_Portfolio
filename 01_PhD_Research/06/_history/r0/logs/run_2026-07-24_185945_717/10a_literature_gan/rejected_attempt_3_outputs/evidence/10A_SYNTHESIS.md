# Stage 10A synthesis — GaN/WBG/Hall-sensor evidence batch

Status: `evidence/10A_GAN_WBG_SOURCES.csv` contains **86 unique,
independently verified, `verified_peer_reviewed` rows** (`A0001`-`A0086`) —
above the 65-source aim and well above the 55-row floor.

## 0. Attempt-history note (read this before trusting anything below)

This is **global attempt 3** of this stage. Attempt 1 and attempt 2 both
self-reported `COMPLETE` with a 68-row ledger, but the launcher's own
model-integrity record (`state/OPERATION_LOG.csv`,
`state/CHATGPT_HANDOFF_STATE.json`) shows **both** attempts actually ran with
a mid-session downgrade to `claude-haiku-4-5-20251001` despite each
attempt's own transcript claiming a clean `claude-sonnet-5` run. Both
68-row CSVs were quarantined by the launcher and are **not** the basis for
anything below. This attempt treated both quarantined CSVs strictly as
unverified lead lists (used only to know what *had been claimed*, never to
accept a citation, author, venue, or DOI on trust) and independently
rebuilt the ledger from scratch: seed candidates were re-derived directly
from primary files (the manuscript's own bibliography and the project-04
review bibliography), and every one of the 86 rows below was verified this
session against a live Crossref API record (`api.crossref.org/works/<doi>`,
fetched via `curl`/Python `urllib`, not assumed). Full detail in
`state/PROJECT_STATE.md` and `state/WORKLOG.md`.

## 1. Search and verification method

1. **Seeds (14 rows, `A0001`-`A0014`):** re-derived directly from two
   primary files, not from either quarantined CSV:
   - The submitted manuscript's own bibliography
     (`01_Publications/submitted/regular_lsens/regular_lsens.tex`), refs
     5-12: six core AlGaN/GaN 2DEG Hall-device-physics references (Mishra
     2002 HEMT overview, Yuan 2023 harsh-environment GaN, Ambacher 1999 2DEG
     formation, Alpert 2019 geometry/sensitivity/offset, Alpert 2020
     high-temperature sensitivity, Lu 2006 high-temperature AlGaN/GaN Hall)
     plus two comparable-Hall-platform/radiation-context references (Quercia
     2022 and Bolshakova 2017, both on non-GaN Hall probes in fusion-reactor
     radiation environments). Ref 15 (a Stanford PhD dissertation) was
     excluded per `SOURCE_POLICY.md`'s "do not count theses/dissertations"
     rule.
   - The project-04 magnetic-sensor review bibliography
     (`04_Magnetic_Sensor_Review_Sensors2026/outputs/references.bib`): five
     further GaN/Hall-relevant entries (Crescentini 2022 Hall-current-sensor
     review, a 2012 JPCS AlGaN/GaN HEMT Hall paper, a 2019 CMOS Hall
     offset-cancellation paper, Munter 1990 — the foundational
     spinning-current paper — and a 2025 silicon 3-axis Hall sensor with
     offset cancellation). The Popović *Hall Effect Devices* monograph was
     excluded (peer review not independently established for a book, per
     policy); `Alpert2020gan2deg` deduplicated against the manuscript's own
     ref11 (identical DOI).
   - A 14th seed — **the stage's headline finding** — was independently
     located and verified directly by the lead researcher (not a subagent):
     Dowling, Alpert, Yalamarthy, Satterthwaite, Kumar, Kock, Ausserlechner,
     **Senesky**, *IEEE Sensors Letters*, 2019,
     `doi:10.1109/lsens.2019.2898157`. See Section 5.
2. **Six parallel Sonnet-5 lane subagents** (`Agent` tool, `model: sonnet`
   pinned per `MODEL_POLICY.md`'s family-integrity requirement, run in
   foreground so all six batches returned together), one per the stage
   prompt's required coverage sub-area: (A) AlGaN/GaN 2DEG & comparable
   III-V Hall platforms; (B) Hall geometry/sensitivity/offset/planar
   Hall/cross-axis; (C) spinning-current/offset-cancellation methods +
   further Senesky-group prior art; (D) noise/drift/linearity/
   bandwidth/parasitics/contacts/wire-bonds/packaging/calibration/TCS/
   repeatability; (E) GaN/SiC/WBG harsh-temperature/vacuum/radiation
   extreme-environment instrumentation; (F) prior GaN Hall-sensor
   performance reviews and novelty-relevant comparisons. Each subagent was
   required to independently verify every candidate via a live Crossref API
   fetch (or official publisher page) before reporting it, using its own
   Bash/WebSearch/WebFetch tool access, and to drop rather than fabricate
   anything unverifiable. Combined, the six lanes returned 104 candidate
   blocks.
3. **Deduplication:** all seed + lane candidates (118 raw blocks) were
   parsed programmatically and deduplicated by normalized (lowercased) DOI,
   yielding 98 unique verified records. Six DOIs were independently
   rediscovered by two different lanes each (e.g. the Ausserlechner
   three-terminal offset paper found by both the geometry lane and the
   spinning-current lane) — a soft cross-lane corroboration signal, not
   double-counted.
4. **Curation to avoid padding:** 12 of the 98 were removed as redundant
   within a narrow sub-theme (e.g. keeping the strongest 1-2 papers from an
   InSb-Hall-sensor cluster or a GaN-proton-irradiation cluster rather than
   every near-duplicate; full list and stated reason for each cut in
   `state/build_final_csv.py`), leaving **86**. Nothing was cut for being
   unverifiable — every cut candidate was itself independently
   Crossref-confirmed; the cuts were a deliberate quality/redundancy pass,
   not exclusion of doubtful sources (all doubtful/unverifiable candidates
   were dropped by the lane subagents before they were ever reported).
5. **Independent spot-check by the lead researcher:** 8 rows spanning all
   six lanes plus a seed (including the highest-stakes rows — the
   novelty-critical Marsic 2025 IEEE Access "Study of GaN Hall Effect
   Magnetic Sensors" paper, and the corrected-author JPCS 2012 entry) were
   independently re-fetched from live Crossref by the lead researcher
   directly (not via a subagent) and matched exactly against the CSV
   content. No discrepancy was found.
6. **Structural validation:** a Python `csv` pass
   (`state/validate_10a_csv.py`) confirmed: header byte-exact to
   `SOURCE_POLICY.md`'s 16-column schema; 86 rows; 0 duplicate
   `source_id`/`doi`/title; sequential IDs `A0001`-`A0086`; 0 blank required
   fields; all `peer_review_status` = `verified_peer_reviewed`; all
   `quality_tier` in `{A,B,C}`; all `access_level` in
   `{full_text,abstract_metadata,metadata_only}`; all `url` values are
   `https://doi.org/<doi>` with the DOI lowercase and matching exactly;
   all `year` values numeric and in range.

## 2. Venue and year distribution

- **86 rows across 50 distinct venues.** No single venue dominates; the
  top venues are *IEEE Sensors Journal* (9), *Sensors* (8, MDPI — all
  individually Crossref-confirmed peer-reviewed journal articles, tiered
  `C` in the rubric below to reflect a lower selectivity bar than
  discipline-leading journals), *Sensors and Actuators A: Physical* (6),
  *Journal of Applied Physics* (4), and *Solid-State Electronics* (4).
- **Year range: 1979-2025**, i.e. from the foundational Hall-geometry
  theory era through the most current (2025) AlGaN/GaN Hall-sensor
  publications. Decade distribution: 1970s: 1, 1980s: 3, 1990s: 6, 2000s:
  12, 2010s: 33, 2020s: 31. The heavy 2010s/2020s weighting (64 of 86 rows)
  reflects that AlGaN/GaN Hall sensing and spinning-current refinement are
  both active, growing research areas — directly relevant to the
  reviewer's novelty question (Section 5).
- **Quality tier** (rubric defined per-row in the ledger, summarized here):
  `A` (foundational/seminal papers or top-tier venues — e.g. Ambacher 1999,
  Mishra 2002, Munter 1990, the Versnel Hall-geometry trilogy, Lenz &
  Edelstein 2006, the Dowling 2019 headline finding): **16 rows**. `B`
  (solid peer-reviewed journal articles in established IEEE/AIP/IOP/
  Elsevier/Wiley/ECS venues): **48 rows**. `C` (peer-reviewed conference
  proceedings, workshop proceedings, or MDPI-family open-access journals —
  still independently Crossref-verified as peer-reviewed, but a lower
  selectivity bar than tier A/B): **22 rows**.
- **Source type:** 65 `journal_article`, 11 `review_article`, 10
  `conference_paper` (all conference entries independently confirmed as
  peer-reviewed proceedings — IEEE Sensors, IRPS, MEMS, PRIME, SBMicro,
  CSTIC, iSES, or the Hilton Head Solid-State Sensors Workshop, which uses
  Transducer Research Foundation peer review).
- **Access level:** 73 `metadata_only` (bibliographic Crossref record
  confirmed; abstract/body not read), 13 `abstract_metadata` (an abstract
  was actually retrieved and read this session), 0 `full_text`. See
  Section 6.

## 3. Performance/novelty comparison dimensions for a manuscript table

The ledger supports a cross-material-system Hall-sensor comparison table
along these dimensions, each anchored to specific `source_id`s:

| Dimension | GaN/AlGaN-family rows | Comparator-material rows |
|---|---|---|
| Current-related sensitivity (S_I) | `A0016` (AlGaN/GaN 2DEG current sensing, TED 2021), `A0006` (`ref10`, IEEE Sensors J 2019), `A0018` (Arkansas AlGaN/GaN micro-Hall, 2018), `A0021` (AlN/GaN, TED 2024, Senesky co-author) | `A0025` (GaAs/InGaAs/AlGaAs 2DEG quantum well), `A0023` (InGaAs/AlGaAs/GaAs nanotesla magnetometry), `A0079` (iSES 2022 direct GaN-vs-GaAs comparison) |
| Voltage-related sensitivity (S_V) | `A0006` | `A0036` (planar-Hall-device S_V geometry optimization) |
| Zero-field offset (raw, pre-cancellation) | `A0006`, `A0018` | `A0029` (CMOS vs. bipolar offset), `A0044` (planar Hall effect as an offset/cross-axis source) |
| Offset after spinning-current cancellation | `A0014`/Dowling 2019 (**the manuscript's own closest prior art**, see Section 5), `A0045` (Dowling 2020 JMEMS, residual-offset mechanism) | `A0052` (silicon, 2 MS/s randomized spinning, offset reduced 130→23 µT), `A0050` (Bilotti/Monreal/Vig 1997, classic dynamic quadrature offset cancellation) |
| Operating temperature range | `A0008` (`ref12`, Lu 2006, AlGaN/GaN), `A0017` (AlGaN/GaN-on-Si, 75-500 K), `A0021` | `A0085` (Sensors 2011 review, Si/GaAs/InSb/InAs), `A0071` (SiC, 500 °C), `A0074` (AlGaN/GaN ohmic-contact stability to 500 °C) |
| Bandwidth | *(gap — see Section 4)* | `A0052` (Si, 820 kHz notch-free), `A0056` (Acta IMEKO, analytical Hall-plate bandwidth-limit model) |
| Noise floor / detectivity | *(gap — see Section 4)* | `A0054` (Mosser 2017, nanotesla-range spinning-current noise), `A0058` (graphene, 700 nT·Hz⁻¹ᐟ² at room temperature) |
| Radiation tolerance | `A0067` (GaN/AlGaN/SiC radiation-damage review, 2023), `A0068` (GaN ionizing-radiation review, 2016), `A0069`/`A0070` (proton/heavy-ion damage on GaN HEMTs) | `A0001` (Quercia 2022, radiation-hard fusion Hall probes), `A0078` (WBG radiation-detection review) |
| Review-article backbone for a full table | `A0009` (Crescentini 2022, Hall-current-sensor review) | `A0080` (Lenz & Edelstein 2006), `A0081` (Ripka & Janosek 2010), `A0085` (Sensors 2011, extreme-temperature Hall-material review) |

This gives Stage 30/40 a ready-made, source-anchored starting point for the
AE-requested comparison table without new bench work.

## 4. Established results vs. unresolved questions

**Established (multiple independently verified sources converge):**
- Current-spinning offset cancellation on AlGaN/GaN 2DEG Hall plates is
  **not** a novel technique in the abstract — it was foundationally
  established on other materials by 1990 (`A0012`/Munter) and refined
  through 2022 (`A0052`, randomized spinning) — and has itself already been demonstrated
  specifically on AlGaN/GaN by the manuscript's own PI's group at least
  twice before the manuscript (`A0014` 2019, `A0045` 2020), plus a 2018
  workshop precursor (`A0047`).
- AlGaN/GaN Hall-sensor high-temperature operation is a well-established,
  actively growing literature (12+ independent groups represented across
  the ledger: Stanford/Senesky, Arkansas/Mantooth-Salamo, IISc
  Bengaluru/Muralidharan, Montpellier/CRHEA, and others), spanning 2006-2025.

**Unresolved / gaps — `NOT ESTABLISHED FROM SUPPLIED FILES OR THIS LEDGER`:**
- **No row in this ledger reports a bandwidth or noise-floor figure for an
  AlGaN/GaN Hall sensor specifically** (as opposed to silicon, graphene, or
  GaAs-family comparators). This directly bears on the unresolved 1 MHz
  vs. ~1-2 kHz bandwidth conflict already flagged in
  `outputs/00_CONFLICT_LEDGER.md` Conflict 3 — this ledger cannot resolve
  that conflict, only confirm that no published comparator closes it either.
- **No source in this ledger combines current-spinning AlGaN/GaN offset
  cancellation with in-vessel/plasma-facing deployment in a single paper.**
  The closest analogues split across two different rows: `A0014`/`A0045`
  (current-spinning AlGaN/GaN, bench-only) vs. `A0001`/`A0002` (in-vessel
  fusion-radiation Hall probes, non-GaN material). This is a genuine
  candidate novelty axis, flagged for Stage 20, not decided here.
- **No source independently confirms an absolute-field-calibration
  precedent for an in-vessel-deployed GaN Hall sensor with a
  conventional-probe comparison** — consistent with, not contradictory to,
  the Stage 00 finding that the supplied HSX data cannot itself close that
  gap either.

## 5. Implications for the submitted GaN Hall sensor (flagged as inference, not decision)

**This stage does not decide the PhD direction or publication route** — per
the stage prompt. The following is inference for Stage 20/30 to weigh, not
a conclusion reached here.

The headline, independently-verified finding is `A0014` — Dowling, Alpert,
Yalamarthy, Satterthwaite, Kumar, Kock, Ausserlechner, **Debbie G.
Senesky**, "Micro-Tesla Offset in Thermally Stable AlGaN/GaN 2DEG Hall
Plates Using Current Spinning," *IEEE Sensors Letters*, 2019,
`doi:10.1109/lsens.2019.2898157`. Verified directly by the lead researcher
via a live Crossref fetch this session (not carried over from either
quarantined attempt): Debbie G. Senesky — the mission subject's own PhD
advisor — is the senior/last author. This paper demonstrates four-phase
current-spinning offset cancellation on the **identical AlGaN/GaN 2DEG
material system**, in the **identical venue** (*IEEE Sensors Letters*), by
the **identical research group**, predating the submitted manuscript by
seven years. This independently corroborates Reviewer 2's novelty concern
(supplied fact `C010` in `outputs/00_CLAIM_BASELINE.csv`) using external,
verified literature evidence rather than the reviewer's own assertion
alone.

Two further ledger entries strengthen this picture and should be read
alongside it, not in isolation:
- `A0045` (Dowling et al., *J. Microelectromechanical Systems*, 2020) — the
  same author cluster's **direct follow-on** paper, explaining the
  residual-offset mechanism after spinning via infrared thermography.
- `A0047` (Dowling et al., Hilton Head Workshop, 2018) — an **earlier**
  paper by the same cluster investigating bias-condition effects on
  AlGaN/GaN 2DEG Hall plates, showing the spinning-current result was the
  culmination of a multi-year internal research line, not an isolated prior
  paper.

Taken together, these three rows indicate the specific combination of
"current spinning" + "AlGaN/GaN 2DEG" is prior art from within the same
lab, not merely the same field — a materially stronger novelty concern than
a same-field-different-lab prior-art citation would be. Any revision
strategy (Stage 30) will need to articulate a distinguishing contribution
precisely (e.g., in-vessel/plasma deployment, absolute calibration, a
different geometry, or a measurement-architecture contribution) rather than
the spinning-current-on-AlGaN/GaN mechanism itself, which this ledger shows
is already published by the same group.

## 6. Limitations caused by abstract/metadata-only access

- **0 of 86 rows are `full_text`.** 73 are `metadata_only` (Crossref
  bibliographic record confirmed: title/authors/year/venue/volume/issue/
  pages) and 13 are `abstract_metadata` (an abstract was actually retrieved
  and read). No row's body text, figures, or tables were read this session.
- Consequently, **any specific numeric value quoted in a `notes` or
  `claims_supported` cell should be re-confirmed against the primary
  source before verbatim use in a revised manuscript or comparison table.**
  Where a lane subagent could not itself verify a quantitative detail
  beyond a secondary-source description (e.g., a WebSearch snippet rather
  than a directly-read abstract), this is stated explicitly in that row's
  `notes` field rather than presented as confirmed — e.g. `A0053` and
  `A0054`'s notes both flag that their quoted quantitative offset/noise
  figures came from a secondary-source description, not an independently
  read primary record, and should be re-confirmed before citation.
- Several publisher landing pages (IEEE Xplore, ScienceDirect/Elsevier) were
  inaccessible to the fetching tools this session (access-gated or
  redirect-blocked); those rows are honestly marked `metadata_only` rather
  than `abstract_metadata`, even where a subagent located a secondary
  description of the content.
- This is consistent with, not contradictory to, the Stage 00 finding that
  full-text access to the submitted manuscript's own bundle
  (`inputs/IEEE_submission_bundle_2026-07-02.pdf`) was itself blocked
  (password-protected).

## 7. Row count

**86 unique, verified, `peer_review_status = verified_peer_reviewed` rows**
(`A0001`-`A0086`) in `evidence/10A_GAN_WBG_SOURCES.csv` — above the
65-source aim and the 55-row floor stated in the stage prompt. Structural
validation passed with 0 errors (`state/validate_10a_csv.py`); DOI/venue
identity independently re-confirmed by the lead researcher via live
Crossref fetch for an 8-row spanning spot-check with 0 discrepancies.

Per the stage prompt, this synthesis does **not** decide the PhD direction
or publication route — that is Stage 20's task, informed by but not
resolved in this document.
