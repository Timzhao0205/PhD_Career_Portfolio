# SEARCH_PROTOCOL — B12_lit_search FULL run

Stage: `B12_lit_search` | Mode: `FULL` | Attempt: `1`
Named worker: `pap06-sonnet-high` | Requested model/effort: Sonnet 5 / high

This document records the protocol actually executed for the full-run
corpus. It extends `pilot/B12_lit_search/attempt-1/SEARCH_PROTOCOL.md`
(exercised on 8 publications) to a 60-100-publication corpus, reusing the
same method (discovery search -> publisher-landing-page or authoritative
open-access-mirror verification -> peer-review-status determination ->
correction/retraction check -> de-duplication) and the same P0001-P0008
retained items with stable IDs and metadata unchanged. Nothing below
constitutes a startup ranking, novelty claim, or final synthesis; those
are reserved for `B15_lit_synth` (Fable/xhigh).

## 1. Research questions (framed from B10, not accepting its inferences)

Unchanged from the pilot. Framed from `outputs/B10_phd/attempt-1/PHD_CORE.md`
and `OPT2.md` as context only — no B10 claim (novelty, feasibility, or
numeric result) is adopted as true by this stage:

1. `hall_metrology` — What does peer-reviewed literature report on
   Hall/GaN Hall-sensor calibration, traceability, uncertainty, drift,
   temperature and radiation effects, bandwidth, and noise?
2. `hybrid_diagnostics` — What does peer-reviewed literature report on
   combining Hall and inductive-coil sensing (data/sensor fusion,
   bandwidth fusion, inverse reconstruction, sensor placement, current
   imaging, diagnostic validation)?
3. `hts_quench_current` — What does peer-reviewed literature report on
   HTS current redistribution, quench detection/protection, no-insulation
   coil behavior, and cryogen-free/measurement-actuation limits?
4. `power_conversion` — What does peer-reviewed literature report on
   specialized converters/supplies, WBG (SiC/GaN) devices, gate drive,
   magnetics, EMI/EMC, thermal/control/protection, HIL, qualification,
   reliability, and current sensing?

## 2. Databases / sites used

- WebSearch (general web search tool) as the discovery layer, including
  targeted `"pmc.ncbi.nlm.nih.gov"` site-scoped queries once PubMed
  Central was established as a reliable open-access mirror host this
  session (see Section 4).
- WebFetch used to open the actual publisher landing page, DOI-resolver
  target, or PMC mirror page for every candidate considered for
  acceptance — never a search snippet alone.
- Publisher platforms successfully opened this run: IOPscience (IOP
  Publishing — Nuclear Fusion, Superconductor Science and Technology,
  Semiconductor Science and Technology, Journal of Physics: Condensed
  Matter, Physica Scripta, Plasma Physics and Controlled Fusion), and
  PubMed Central (`pmc.ncbi.nlm.nih.gov`) as an authoritative open-access
  mirror for MDPI (Sensors, Micromachines, Materials), Nature-family
  (Nature Communications, Scientific Reports), Springer (SpringerPlus,
  Annals of Biomedical Engineering), AIP (Applied Physics Letters), and
  IEEE (Transactions on Applied Superconductivity, as NIH-funded
  author-manuscript records) journal articles.
- Publisher platforms actively blocking this session's WebFetch tool:
  `mdpi.com` direct pages (HTTP 403, consistent with the pilot), AIP
  Publishing `pubs.aip.org` direct pages for AIP Advances (HTTP 403),
  `link.aps.org` / Physical Review Applied (HTTP 403), `nature.com`
  direct pages (redirected to an `idp.nature.com` authentication wall,
  HTTP 303), SpringerLink (auth-wall pattern carried from the pilot,
  not re-tested this run), Wiley/IET (blocked pattern carried from the
  pilot), ScienceDirect (HTTP 403, carried pattern). IEEE Xplore direct
  pages (`ieeexplore.ieee.org`) were not attempted this run given the
  pilot's established no-retrievable-content failure pattern; IEEE
  content was instead reached, where available, through PMC
  author-manuscript mirrors.
- USPTO patent full-text, ResearchGate, academia.edu, arXiv, PubMed
  abstract pages, and OSTI.gov remained discovery aids only, never
  treated as the verification source.

## 3. Query families

Sixty-two discovery queries were run in total (`Q01`-`Q10` carried
unchanged from the accepted pilot; `Q11`-`Q62` new to this full run — see
`SEARCH_LOG.csv` for every exact query string, platform, result count,
and per-query outcome). Query families covered, per stream: calibration/
traceability/uncertainty/radiation/temperature/noise/bandwidth terms
(`hall_metrology`); sensor-fusion, inverse-reconstruction, current-imaging,
and diagnostic-validation terms (`hybrid_diagnostics`); no-insulation,
quench-detection, current-redistribution, and contact-resistance terms
(`hts_quench_current`); gate-drive, WBG device, magnetics, EMI, HIL, and
current-sensing terms (`power_conversion`). Once PMC was established as
a reliable open-access mirror host for otherwise-blocked publishers
(MDPI, Nature, Springer, AIP, IEEE), a second wave of `"pmc.ncbi.nlm.nih.gov"`
site-scoped queries (`Q35`-`Q62`) was run per stream to locate additional
publisher-verifiable candidates efficiently. Negative queries (no new
item accepted) are logged honestly in `SEARCH_LOG.csv`, not hidden
(e.g. `Q50`, `Q51`, `Q55`, `Q57`, `Q60`).

## 4. Date / language boundaries

- Language: English only; no non-English sources were retained. One
  candidate item published in a Japanese cryogenics-society bulletin
  (Teion Kogaku) was in English but excluded on peer-review-status
  grounds, not language (`E20`).
- Date boundary: no hard cutoff was applied; retained papers span
  1996-2026, deliberately mixing seminal older work (oldest: 1996,
  `hall_metrology`) with recent work, satisfying both the seminal-work
  and the >=16-accepted-core-from-2020-2026 (with >=2 per stream)
  requirements — see `FLOW.json` notes for the exact recount. All web
  activity occurred on 2026-07-28 (the session date); no paper dated
  after that access date was retained.

## 5. Inclusion / exclusion rules

Unchanged from the pilot (see `pilot/.../SEARCH_PROTOCOL.md` Section 5
for the full statement). Summary:

- **`accepted_core`:** verified peer-reviewed journal research or review
  article, with its publisher landing page — or an authoritative
  open-access mirror (PubMed Central) when the publisher domain blocked
  WebFetch access this session, disclosed per row in `access_status`/
  `notes` — directly opened, DOI confirmed, and no unresolved correction/
  expression-of-concern/retraction found on that record.
- **`accepted_supplement`:** peer-reviewed conference paper with the
  specific venue's peer-review process independently verified. None were
  retained this run: several conference-adjacent candidates were
  encountered (e.g. Journal of Physics: Conference Series items, `Q17`)
  but their venue-specific peer-review process was not independently
  confirmed to the standard this stage requires, so none were promoted
  to `accepted_supplement` rather than accepted on brand appearance
  alone.
- **`unresolved`:** none this run — every candidate that reached
  full-text verification was either accepted or excluded with a stated
  reason; no candidate was left in an ambiguous accepted/excluded state.
- **Exclude:** patents, preprints, theses, vendor/marketing pages,
  magazine articles, non-peer-reviewed reports, items whose venue or
  peer-review status could not be confirmed, items whose landing page
  could not be opened (paywall/authentication wall/access error), and
  items judged out of the accepted-core content-type scope (e.g. a
  peer-reviewed data-descriptor article, `E19`) — never promoted on the
  strength of a DOI, publisher brand, or professional-looking PDF alone.

## 6. Duplicate handling

De-duplication proceeds by normalized DOI first, then by normalized
title/year, per `workflow/stages/B12_lit_search.md`. Every new paper_id
(`P0009`-`P0062`) was checked against every existing `doi` value in
`PAPER_LEDGER.csv` before being added, so the ledger contains no
duplicate DOI. Six additional duplicate-mention instances (the same
underlying paper independently re-surfaced by more than one query) were
identified and merged into a single record this run — see `SEARCH_LOG.csv`
notes for `Q05`/`Q06`, `Q35`/`Q37`, `Q44`, `Q45` (two instances), and
`Q41`/`Q46` — and are reflected in `FLOW.json`'s `duplicates_removed`.
One cross-run exception is disclosed rather than silently resolved:
`EXCLUSIONS.csv` row `E10` (pilot-era, blocked HTTP 403) and
`PAPER_LEDGER.csv` row `P0031` refer to the same underlying paper
(`10.3390/s24186071`), located this run via a PubMed Central mirror not
previously found; both rows are retained for audit continuity, with
`E10` annotated as superseded.

## 7. Screening sequence

1. WebSearch discovery query run and result list read (title/venue
   level).
2. Obvious non-literature results (patent full text, vendor/marketing
   pages, journal special-issue index pages) screened out at this stage
   without an individual full-text fetch; only clearly representative
   instances are individually logged in `EXCLUSIONS.csv` (`E03`, `E04`,
   `E05`, carried from the pilot), consistent with the pilot's stated
   "representative, not exhaustive" convention.
3. Remaining candidates: WebFetch attempted on the publisher landing
   page, DOI-resolver target, or PMC mirror.
   - Success + peer review confirmed (via received/accepted dates,
     named academic editor, or an explicit review-statement/peer-review-
     information notice on the opened page) + no correction/retraction
     found -> `accepted_core`.
   - Success but content-type/scope mismatch (e.g. data descriptor) ->
     excluded with the specific reason (`E19`).
   - Success but peer-review process of the specific venue not
     independently confirmable from the opened record -> excluded as
     unresolved peer-review status (`E20`), never promoted on hosting
     appearance alone.
   - Access failure (HTTP 402/403, IdP authentication-wall redirect, or
     empty content) -> logged as an exclusion with the specific
     technical reason; never silently treated as verified. Where a PMC
     mirror could be located for the same DOI, that mirror was used
     instead and the direct-publisher block is disclosed in `notes`
     rather than causing exclusion.
4. Stream-balance check: searches continued per stream until each
   stream held a comfortable margin above the 8-accepted-core minimum
   (final per-stream accepted_core: `hall_metrology` 13,
   `hybrid_diagnostics` 14, `hts_quench_current` 17, `power_conversion`
   18) and the corpus as a whole reached the natural quality range
   within 60-100 (62 retained) without continuing to pad once sufficient
   high-quality, independently verified candidates were exhausted from
   the accessible platforms.
5. Retained items assigned stable IDs `P0009`-`P0062`, grouped by topic
   stream in the order each item was successfully verified within that
   stream's search sequence (continuing the pilot's `P0001`-`P0008`
   numbering; `P0001`-`P0008` themselves are unchanged from the pilot).

## 8. Evidence hierarchy

Unchanged from the pilot (see pilot Section 8). Verified peer-reviewed
journal research/review articles > verified peer-reviewed conference
papers (supplement only, none retained this run) >
preprints/theses/patents/vendor/magazine material (discovery/context
only). Peer-review status is read from each opened record's own
review-process statement (received/revised/accepted dates, named
academic editor, explicit review-statement, or "Peer review information"
notice), or from independent knowledge of an established peer-reviewed
venue (e.g. Nuclear Fusion, Superconductor Science and Technology, IEEE
Transactions on Applied Superconductivity, Nature Communications,
Scientific Reports, Sensors, Micromachines, Materials) — never inferred
from DOI, publisher brand, or PDF appearance alone. IEEE TAS items
accessed via NIH PMC author-manuscript mirrors are disclosed per row as
such, with metadata taken from the PMC citation record for the published
version.

## 9. Correction / retraction screening

For every one of the 62 retained items, the opened publisher landing
page or PMC mirror record was checked for a correction, expression-of-
concern, or retraction banner/notice. One correction (not a retraction)
was found — on `P0012` (Nature Communications 11:4163, corrected per
Nat Commun 12:554, 18 Jan 2021) — and is disclosed in that row's
`correction_status`; the item is retained as `accepted_core` per
`LIT_POLICY.md` (a correction is not a retraction and does not itself
disqualify a publication). No retraction or expression-of-concern notice
was found on any of the 62 retained items. As in the pilot, this run did
not separately query Crossref or Retraction Watch for a second
independent check beyond the opened record itself; that remains a
disclosed limitation (see `RUN_META.md`).

## 10. Timestamp convention

Unchanged from the pilot. No system clock/precise time was exposed to
this agent. All `SEARCH_LOG.csv` and ledger timestamps use the session
date `2026-07-28` with `NOT_EXPOSED` in place of a time-of-day; queries
are ordered by their execution sequence (`query_id` `Q01`-`Q62`) rather
than by invented clock times.

## 11. Limitations

- Several major publisher platforms actively blocked this session's
  WebFetch tool for direct access (`mdpi.com`, `pubs.aip.org` for AIP
  Advances specifically, `link.aps.org`, `nature.com`, and the
  pilot-established SpringerLink/Wiley-IET/ScienceDirect pattern, not
  re-tested this run). Where a PubMed Central mirror existed for the
  same DOI, it was used instead and disclosed per row; where no mirror
  was found (MDPI Electronics and Energies journals in particular are
  not consistently PMC-indexed), the candidate was excluded rather than
  accepted on faith (`E14`, `E16`, `E17`, `E18`).
  IEEE Xplore direct access was not re-attempted this run given the
  pilot's established failure pattern; IEEE Transactions on Applied
  Superconductivity items were instead reached via NIH PMC
  author-manuscript mirrors, disclosed per row.
- No independent second correction/retraction check (e.g. a separate
  Crossref or Retraction Watch query) was run beyond reading each opened
  record itself; recorded as a method limitation, not concealed.
- This is a support-stage full run: it makes no startup-ranking,
  novelty, or synthesis judgment. It does not claim a formal systematic
  review or meta-analysis (PRISMA 2020's full checklist/protocol-
  registration requirements were not executed) — this is PRISMA-
  *inspired* reporting only, per `LIT_POLICY.md`.
- Absence of a correction/retraction notice on an opened record is
  evidence of "none found," not proof that no such notice exists
  anywhere.
- `identified`/`duplicates_removed` in `FLOW.json` rely on explicitly
  documented re-surfacing instances noted during screening; this is a
  conservative, auditable count, not a claim of exhaustive detection of
  every silent duplicate across 62 broad discovery queries.
- No conference paper was retained as `accepted_supplement` this run:
  candidates were encountered but their specific venue's peer-review
  process was not independently confirmed to the standard this stage
  requires, so the corpus's 62 retained items are all `accepted_core`
  journal research or review articles.
