# SEARCH_PROTOCOL — PILOT SAMPLE — NOT FINAL

Stage: `B12_lit_search` | Mode: `PILOT` | Attempt: `1`
Named worker: `pap06-sonnet-high` | Requested model/effort: Sonnet 5 / high

This document is a **PILOT SAMPLE — NOT FINAL**. It records the protocol
actually executed to exercise the complete search -> verification ->
correction/retraction screening -> de-duplication path on exactly eight
retained publications (two per topic stream), not a full-run corpus.

## 0. Pilot-scope statement

This run does not attempt the full-run corpus target (60-100 unique
publications, >=48 accepted_core, >=8 accepted_core per stream). It
exercises every method step — discovery search, publisher-landing-page
verification, peer-review-status determination, correction/retraction
check, de-duplication, and exclusion logging — on a deliberately small,
bounded sample of exactly 8 retained publications (2 per topic stream,
all 8 accepted_core in this run). Genuine negative and access-failure
searches are logged, not hidden. Nothing below constitutes a startup
ranking, novelty claim, or final synthesis; those are reserved for
`B15_lit_synth` (Fable/xhigh).

## 1. Research questions (framed from B10, not accepting its inferences)

B10's `PHD_CORE.md`/`OPT2.md` describe (as the corpus's own claims, not
facts this pilot adopts) a GaN Hall-effect sensor deployed at HSX, a
proposed Hall+coil hybrid diagnostic (mutual calibration, bandwidth
fusion, radiation compensation), open HTS quench/current-redistribution
questions referenced as comparison context, and power-conversion/current
sensing techniques used in the sensor readout chain. This pilot frames
four neutral research questions from that context, without accepting any
B10 claim (novelty, feasibility, or numeric result) as true:

1. `hall_metrology` — What does peer-reviewed literature report on
   Hall/GaN Hall-sensor calibration, traceability, uncertainty, drift,
   temperature and radiation effects, bandwidth, and noise?
2. `hybrid_diagnostics` — What does peer-reviewed literature report on
   combining Hall and inductive-coil sensing (data/sensor fusion,
   bandwidth fusion, inverse reconstruction, diagnostic validation)?
3. `hts_quench_current` — What does peer-reviewed literature report on
   HTS current redistribution, quench detection/protection, and
   no-insulation coil behavior?
4. `power_conversion` — What does peer-reviewed literature report on
   WBG (SiC/GaN) power conversion, gate drive, and current sensing?

## 2. Databases / sites used

- WebSearch (general web search tool) as the discovery layer.
- WebFetch used to open the actual publisher landing page or DOI
  resolver target (doi.org) for every candidate considered for
  acceptance — never a search snippet alone.
- Publisher platforms reached this run: IOPscience (IOP Publishing),
  Copernicus (JSSS), MDPI (via doi.org resolver and, where blocked, its
  PubMed Central open-access mirror), SpringerLink (attempted, blocked by
  an authentication wall both times), AIP Publishing (attempted, blocked
  by HTTP 403), Wiley/IET (attempted, blocked by HTTP 402), ScienceDirect
  (attempted, blocked by HTTP 403), IEEE Xplore (attempted, no
  retrievable content returned), USPTO patent full-text (discovery only,
  never accepted), ResearchGate/academia.edu/arXiv/PubMed (discovery
  aids only, never treated as the verification source).

## 3. Query families

Ten discovery queries were run, at least two per topic stream, covering
calibration/traceability, hybrid sensor fusion, quench/current
redistribution, and WBG power-conversion themes; see `SEARCH_LOG.csv`
for the exact query strings, platform, result counts, and outcomes.
Query families intentionally included both broad discovery terms and
narrower doi/title-targeted follow-up searches used to locate a
publisher-verifiable version of a candidate first found only via a
secondary mirror (ResearchGate, academia.edu, PubMed).

## 4. Date / language boundaries

- Language: English only (no non-English sources were retained or
  excluded in this pilot; none were encountered).
- Date boundary: no hard cutoff was applied for the pilot; retained
  papers span 2016-2026, intentionally mixing one seminal (2016) and
  several recent (2020-2026) items per the full-run diversity principle,
  applied here at pilot scale. All web activity occurred on 2026-07-28
  (the session date); no papers dated after that access date were
  retained.

## 5. Inclusion / exclusion rules

**Include as `accepted_core`:** verified peer-reviewed journal research
or review article, with its publisher landing page (or DOI-resolver
target, including an open-access repository mirror such as PMC when the
publisher's own page could not be opened) directly opened by WebFetch
this session, DOI confirmed, and no unresolved correction/expression-of-
concern/retraction found on that record.

**Include as `accepted_supplement`:** peer-reviewed conference paper
with the specific venue's peer-review process independently verified.
(None were used in this pilot's final 8 — all 8 retained items met the
higher `accepted_core` bar — but the method supports this category and
the pilot logged conference/near-miss candidates it chose not to use;
see `EXCLUSIONS.csv` E11.)

**Exclude:** patents, preprints, theses, vendor/marketing pages, magazine
articles, non-peer-reviewed reports, items whose venue or peer-review
status could not be confirmed, and items whose publisher landing page
could not be opened (paywall, authentication wall, or access error) —
these are marked `unresolved`/excluded and are never promoted to
`accepted_core` on the strength of a DOI, publisher brand, or
professional-looking PDF alone.

## 6. Duplicate handling

De-duplication proceeds by normalized DOI first, then by normalized
title/year, per `workflow/stages/B12_lit_search.md`. In this pilot,
duplicate *mentions* of the same underlying record (e.g., a paper
surfaced via both its ResearchGate "Request PDF" mirror and its
publisher page in different queries, or a published version and its
arXiv preprint) were merged into a single unique record before
individual screening. Eight such duplicate-mention instances were
identified and merged across the pilot's 19 individually adjudicated
records (see `FLOW.json` for the reconciled count).

## 7. Screening sequence

1. WebSearch discovery query run and result list read (title/venue
   level).
2. Obvious non-literature results (patent full text, vendor/marketing
   pages, conference-council/navigation pages) screened out at this
   stage without an individual full-text fetch (3 such records were
   individually logged in `EXCLUSIONS.csv` as representative examples;
   others of this kind were encountered but not individually logged,
   consistent with pilot scope).
3. Remaining candidates: WebFetch attempted on the publisher landing
   page or DOI-resolver target.
   - Success + peer review confirmed + no correction/retraction found
     -> candidate for `accepted_core` (or `accepted_supplement` for a
     verified peer-reviewed conference venue).
   - Access failure (paywall HTTP 402, forbidden HTTP 403, auth-wall
     redirect, or empty content) -> logged as an exclusion with the
     specific technical reason; never silently treated as verified.
4. Stream quota check: because this pilot retains exactly 2 accepted
   items per stream, one fully verified, peer-reviewed, non-corrected
   candidate (E07) was still not retained once its stream's quota of 2
   was already filled by other verified items — logged honestly as a
   quota exclusion, not a quality exclusion.
5. Retained items assigned stable IDs `P0001`-`P0008` in the order they
   were successfully verified.

## 8. Evidence hierarchy

Per `LIT_POLICY.md`/`SOURCE_POLICY.md`: verified peer-reviewed journal
research/review articles > verified peer-reviewed conference papers
(supplement only) > preprints/theses/patents/vendor/magazine material
(discovery/context only, never accepted-core or accepted-supplement). A
DOI, publisher brand, or professional PDF appearance is never itself
proof of peer review; each retained item's peer-review status is
verified from the landing page's own review-process statement (e.g.,
JSSS's published "Review statement" naming the editor and "two anonymous
referees"; IOP journals' displayed received/revised/accepted dates and
review-type disclosure) or independent knowledge of the venue's
peer-review process (e.g., Nuclear Fusion, Superconductor Science and
Technology, Micromachines are all established peer-reviewed journals),
stated per item in `PAPER_LEDGER.csv` notes.

## 9. Correction / retraction screening

For every retained item, the opened publisher landing page was checked
for a correction, expression-of-concern, or retraction banner/notice.
None were found on any of the 8 retained items' landing pages (or, for
P0005/P0006, on the PMC mirror record used because the MDPI publisher
page itself returned HTTP 403 in this session). This pilot did not
separately query Crossref or Retraction Watch for a second independent
check; that is recorded as a limitation in `RUN_META.md`, not concealed.

## 10. Timestamp convention

No system clock/precise time was exposed to this agent. All
`SEARCH_LOG.csv` and ledger timestamps use the session date `2026-07-28`
with `NOT_EXPOSED` in place of a time-of-day, and queries are ordered by
their execution sequence (`query_id` Q01-Q10) rather than by invented
clock times.

## 11. Limitations

- Several publisher platforms actively blocked this session's WebFetch
  tool (SpringerLink via an IdP authentication redirect; AIP Publishing,
  ScienceDirect, Wiley/IET, and direct MDPI pages via HTTP 402/403).
  Candidates behind those walls were not accepted and are logged as
  exclusions with the specific technical reason, not silently dropped or
  guessed at.
- For the two Micromachines (MDPI) items retained, direct verification
  used the article's PubMed Central open-access mirror after the MDPI
  publisher page itself returned HTTP 403 on repeated attempts; this is
  disclosed per item rather than presented as an unqualified publisher-
  page verification.
- This is a support-stage pilot: it makes no startup-ranking, novelty,
  or synthesis judgment. It does not claim a formal systematic review or
  meta-analysis (PRISMA 2020's full checklist/protocol-registration
  requirements were not executed) — this is PRISMA-*inspired* reporting
  only, per `LIT_POLICY.md`.
- Absence of a correction/retraction notice on a landing page is
  evidence of "none found," not proof that no such notice exists
  anywhere (e.g., a delayed or off-page notice cannot be ruled out from
  a single access).
- The pilot's exactly-8-paper cap means several fully verified,
  peer-reviewed candidates (e.g., E07) were deliberately not retained
  once their stream's quota was filled; this reflects the pilot's
  bounded scope, not a quality judgment against those items.
