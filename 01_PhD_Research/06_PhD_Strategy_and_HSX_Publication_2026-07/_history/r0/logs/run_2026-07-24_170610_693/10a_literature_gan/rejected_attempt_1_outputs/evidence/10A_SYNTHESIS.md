# 10A — GaN/WBG/Hall-sensor evidence batch: synthesis

Stage `10a_literature_gan`. Companion ledger: `evidence/10A_GAN_WBG_SOURCES.csv`
(68 rows, provisional IDs `A0001`-`A0068`). This stage does not decide the PhD
direction or publication route (reserved for Stage 20); it only builds and
characterizes the GaN/WBG/Hall-sensor evidence lane.

## 1. Search and verification method

**Seeding.** Rather than starting a blind web search, this stage first mined
two existing, already-curated citation pools for GaN/WBG/Hall-sensor-relevant
candidates:

- The submitted manuscript's own 20-item bibliography
  (`../01_Publications/submitted/regular_lsens/regular_lsens.tex`, lines
  550-613). Nine of its twenty references are GaN/WBG/Hall-sensor-material
  relevant (`ref3`, `ref5`, `ref6`, `ref7`-`ref12`); the remainder are
  fusion/HSX-diagnostics references out of this stage's scope (reserved for
  Stage 10b).
- The prior lit-review pipeline's bibliography
  (`../04_Magnetic_Sensor_Review_Sensors2026/outputs/references.bib`, 122
  entries, general magnetic-sensing scope). Only 3 of its entries were
  GaN/Hall-specific and in-scope for this lane (Crescentini 2022, Koide/JPCS
  2012, Lim & Park 2019); the rest cover SQUID/NV-diamond/fluxgate/TMR/GMR/
  digital-twin topics outside this stage's coverage bullets and were not
  re-used here.

All 13 seed candidates were independently re-verified this stage (not simply
copied from either prior document) via direct Crossref DOI-record fetches
(`https://api.crossref.org/works/<DOI>`), confirming title, authors, venue,
and year before inclusion. One seed candidate surfaced during seeding
(Popović, *Hall Effect Devices*, IOP Publishing monograph, DOI
`10.1887/0750308559`) was **excluded**: Crossref confirms the DOI exists but
does not certify peer review for a monograph, and no independent evidence of
peer review was found, so per `SOURCE_POLICY.md` ("books... unless peer
review is independently established") it was left out rather than counted.

**Fan-out search.** Five parallel literature-search passes were then run, one
per remaining coverage sub-area named in the stage prompt: (A) AlGaN/GaN 2DEG
and comparable III-V Hall device physics; (B) Hall geometry, sensitivity,
offset, planar Hall effect, cross-axis response; (C) spinning-current/
current-reversal/offset-cancellation methods; (D) noise, drift, linearity,
bandwidth, parasitics, contacts, wire bonds, packaging, calibration,
temperature coefficients, repeatability; (E) GaN/SiC/WBG harsh-environment
instrumentation plus prior GaN Hall-sensor performance/review literature.
Each pass was required to verify every candidate against a Crossref DOI
record or official publisher landing page before reporting it, and to drop
(not guess or fabricate) anything that failed verification. Combined, the
five passes proposed 70 verified candidates; after removing cross-lane
duplicates (a paper independently rediscovered by more than one search pass)
and the pre-existing seed overlaps, 55 net-new sources remained, for a total
ledger of **68 unique, independently verified, peer-reviewed rows**
(13 seed + 55 net-new).

**Independent spot-check.** After compilation, 8 of the fan-out-sourced rows
(spanning all five lanes: `A0022`, `A0027`, `A0036`, `A0042`, `A0048`,
`A0053`, `A0058`, `A0068`) were re-verified directly against Crossref by this
session (not merely trusting the sub-search report). All 8 confirmed
correctly on title/authors/journal/year; two had minor volume/issue/page
discrepancies (`A0048` Niroula et al. and `A0068` Shetty et al., both
Crossref-confirmed and corrected in the final CSV). No fabricated or
unverifiable DOI was found in the spot-check sample.

**What "verified" means here.** For journal articles, verification is a
Crossref (or, in one case, official publisher landing page) bibliographic
record match. For peer-reviewed conference papers (IEEE Sensors 2004
proceedings, EuroSimE 2007, iSES 2022, IOP *J. Phys.: Conf. Ser.*),
verification confirms the paper appears in the named proceedings container
of an established peer-reviewing body (IEEE, IOP); it does not re-derive
each venue's individual review workflow from first principles. This is
stated explicitly, per `verification_basis`, rather than silently upgraded to
a stronger claim.

## 2. Venue and year distribution

68 rows total.

**By decade:** 1980s: 1 · 1990s: 6 · 2000s: 18 · 2010s: 21 · 2020s: 22.
The distribution is deliberately weighted toward recent work (43/68, 63%,
from 2010 onward) while retaining the foundational older papers the field's
techniques trace back to (Munter 1990 spinning-current; Popović & Hälg 1988
nonlinearity; Bilotti 1997 quadrature offset cancellation).

**By source type:** journal_article 54 · peer_reviewed_conference_paper 6 ·
review_article 8.

**By quality tier** (rubric below): A: 25 · B: 37 · C: 6.

**Top venues (>=2 rows):** *Sensors* (MDPI) 8 · *Sensors and Actuators A:
Physical* 8 · *IEEE Journal of Solid-State Circuits* 5 · *IEEE Sensors
Journal* 4 · *Applied Physics Letters* 3 · *Proceedings of IEEE Sensors 2004*
3 · *ECS J. Solid State Sci. Technol.* 2 · *Microsystems & Nanoengineering* 2
· *Nuclear Fusion* 2 · *Journal of Applied Physics* 2 · *IEEE Transactions on
Magnetics* 2. The remaining 26 venues each contribute 1 row, giving broad
institutional/venue diversity rather than concentration in a single journal.

**Quality-tier rubric** (documented here since this stage does not produce a
standalone `01_SOURCE_COVERAGE.md`; the final ledger stage should reconcile
or restate this rubric):
- **A** — Foundational, highly-cited, or directly-on-point primary literature
  in an established venue (e.g. IEEE JSSC, IEEE Sensors Journal, RSI, JAP,
  Nuclear Fusion), or Senesky-group/directly-connected prior art on the
  identical material system.
- **B** — Solid peer-reviewed journal article or peer-reviewed conference
  paper, relevant but more specialized, narrower in scope, a comparator
  platform, or a review/perspective article without independent primary data.
- **C** — Peer-reviewed but a smaller/regional/less-established venue,
  metadata-only verification with a more tangential relevance, or a paper
  included mainly for adjacent-methodology context rather than direct
  on-topic relevance.

## 3. Performance/novelty comparison dimensions for a manuscript table

Cross-referencing the sources tagged `novelty comparison` or
`performance table` in the ledger, a reviewer-facing comparison table (as the
Associate Editor requested — claim `C011`) could be built along these
columns, each traceable to specific `source_id`s:

| Dimension | Representative sources |
|---|---|
| Material system (AlGaN/GaN, InAlN/GaN, AlN/GaN, GaAs/InGaAs, InSb, SiC) | A0003, A0004, A0005, A0009, A0012, A0013, A0016, A0018, A0019, A0020, A0067, A0068 |
| Room-temperature current-/voltage-related sensitivity | A0003, A0005, A0006, A0033, A0034 |
| Offset (raw and after any cancellation) | A0005, A0006, A0022, A0026, A0034, A0041, A0042 |
| Operating temperature range / high-temperature stability | A0003, A0004, A0006, A0007, A0009, A0014, A0015, A0016, A0018, A0067 |
| Bandwidth / frequency response | A0033, A0045, A0068 |
| Offset-cancellation method used (if any) and residual offset achieved | A0022, A0035, A0036, A0037, A0038, A0039, A0040, A0041, A0042, A0043 |
| Repeatability across multiple fabricated devices | A0005, A0034, A0041, A0053 |
| Packaging / extreme-environment survivability | A0048, A0049, A0050, A0051, A0053 |

The single most important entry for this table is **`A0042`** (Dowling et
al., *IEEE Sensors Letters*, 2019, doi:10.1109/lsens.2019.2898157): a prior
Senesky-group (Tim's own PI) paper applying four-phase current spinning to
the **identical AlGaN/GaN 2DEG material system** as the submitted manuscript,
reporting offset reduced roughly 30x to a few microtesla with stable
sensitivity from -100 to 200 degC. This is supplied-evidence-grade prior art
that predates and is directly comparable to the submitted manuscript's
device. Reviewer 2's claim (`C010`) that "GaN 2DEG Hall devices for dynamic
field detection have been reported previously" is independently corroborated
by this source plus `A0003` (Lu et al. 2006), `A0004` (Koide et al. 2012),
`A0067` (Bouguen et al. 2009), and `A0005`/`A0006` (Alpert et al. 2019/2020,
also Senesky-group). This is stated as **inference from independently
verified literature**, not as a decision on manuscript strategy — that
synthesis is reserved for later stages.

## 4. Established results vs. unresolved questions

**Established by this literature (peer-reviewed, independently verified):**
- AlGaN/GaN 2DEG Hall sensing is a literature area with published prior art
  going back at least to 2002 (`A0016` SiC precedent) and 2006 (`A0003`,
  GaN-specific), continuing through 2025 (`A0011`, `A0043`).
- Spinning-current/current-reversal offset cancellation is a mature,
  extensively published technique (foundational 1990-2004: `A0035`, `A0022`,
  `A0036`; refined through 2014-2020: `A0040`, `A0041`) with a documented,
  quantified residual-offset floor for **voltage-biased** (as opposed to
  current-biased) Hall probes (`A0023`), which is directly relevant given the
  manuscript's own 0.4 V bias scheme.
- The same Senesky group has already published a current-spinning
  offset-cancellation result on the identical AlGaN/GaN 2DEG material system
  (`A0042`, 2019) and a geometry/offset/repeatability study across multiple
  fabricated AlGaN/GaN and InAlN/GaN devices (`A0005`, 2019 — the manuscript's
  own `ref10`).
- Hall-sensor materials for extreme radiation/temperature fusion environments
  (DEMO/ITER/JET-class) are an active, separate literature area (`A0055`,
  `A0056`, `A0057`, `A0053`) that already frames GaN/other WBG materials as
  candidates, without this manuscript's device having been evaluated in that
  specific literature.

**Unresolved / not established by this literature (flagged, not
guessed):**
- No source found in this batch reports absolute (Tesla-referenced) field
  calibration data for an in-vessel-deployed AlGaN/GaN 2DEG Hall sensor in an
  operating stellarator or tokamak alongside a conventional probe comparison
  — i.e., the literature does not contain a ready-made precedent that would
  substitute for the bench-top/B-dot calibration the reviewers requested for
  *this* device. This is consistent with, not contradictory to, the Stage 00
  finding that the supplied HSX data itself cannot close that same gap.
  Whether an appropriate B-dot/calibration comparison exists in the *fusion*
  diagnostics literature specifically (as opposed to the GaN/WBG lane
  covered here) is deferred to Stage 10b.
- No source in this batch reports wire-bond or ohmic-contact reliability data
  specific to the manuscript's exact LCC package + EPO-TEK 353ND epoxy +
  zirconia holder + UHV bake combination; the closest analogues (`A0048`
  ohmic contacts to 500 degC, `A0049`/`A0050` wire-bond reliability, `A0051`
  ceramic diffusion bonding) are all for different exact material/packaging
  combinations. Extrapolation from these to the manuscript's specific package
  is an inference, not an established result.
- The bandwidth-justification gap Reviewer 1 raised (why 1 MHz, device- or
  amplifier-limited?) has candidate analytical tools in this batch (`A0033`,
  `A0045`) but no source directly computes an expected bandwidth number for
  the manuscript's specific Hall-plate geometry and readout chain; applying
  those models to the manuscript's numbers would be new analysis, not a
  literature citation.

## 5. Implications for the submitted GaN Hall sensor (flagged as inference, not decision)

These are **inferences drawn from the verified literature**, offered as
input to later stages (Stage 20 direction decision; Stage 30 manuscript
strategy) — this stage does not itself decide direction or strategy:

- The existence of `A0042` (Senesky group, IEEE Sensors Letters, 2019,
  identical material system, current-spinning offset cancellation already
  demonstrated) means any revised manuscript or response letter addressing
  Reviewer 2's novelty concern will need to explicitly distinguish the
  submitted manuscript's contribution from this closely related prior
  in-group work, rather than treat GaN 2DEG Hall sensing itself as novel.
- Conversely, `A0042`/`A0005`/`A0006` are all **calibration/offset-focused**
  bench studies; none of them report **in-vessel, real-time, plasma-shot
  deployment** the way the submitted manuscript does. The literature in this
  batch does not contain a source that combines (a) AlGaN/GaN 2DEG Hall
  sensing, (b) offset-calibrated readout, and (c) live fusion-device
  deployment in one paper — each element individually has prior art, but not
  (from this lane's search) the specific combination. Whether that
  combination is sufficient novelty is a judgment call for Stage 20, not
  established or refuted by this evidence batch alone.
- The AE's request for "a comparison table against other GaN sensors"
  (`C011`) can be populated using this ledger's Section 3 dimensions today,
  without new experiments, using `A0003`, `A0004`, `A0005`, `A0006`, `A0009`,
  `A0013`, `A0067`, `A0068`, and `A0042`.

## 6. Limitations from abstract-only/metadata-only access

Of the 68 rows, 52 are `abstract_metadata` and 16 are `metadata_only`; **zero
are `full_text`**. No paper's full PDF or HTML body was read in this stage —
every verification was a Crossref bibliographic-record match (title,
authors, venue, year, and for some rows a Crossref-supplied abstract
summary) or, in one case, an official publisher landing page. This means:

- Quantitative values quoted in Section 3/4 of this synthesis (offset
  magnitudes, temperature ranges, sensitivity numbers) are drawn from
  abstract-level statements returned by the search-lane subagents and were
  **not independently re-derived from full-text figures/tables** by this
  session. They should be treated as reported-in-abstract claims, to be
  confirmed against full text before being quoted verbatim in any revised
  manuscript.
- Several IEEE Xplore and one Wiley full-text page actively blocked
  automated fetches (HTTP 418 / 402 responses) during the search passes;
  Crossref's DOI API was used as the fallback authoritative source in those
  cases, which confirms bibliographic existence and venue but not full-text
  content.
- 6 rows (Tier C) are flagged as weaker either because of a smaller/regional
  venue, single-author minimal metadata, or more tangential relevance —
  these are legitimate, verified peer-reviewed sources, but should be
  weighted accordingly in any downstream synthesis.

## 7. Row count

**68 valid, unique, independently-verified peer-reviewed rows** — above the
65-source target and well above the 55-row floor set by the stage prompt.
No candidate was padded in to hit the count: multiple candidates surfaced by
the search lanes (arXiv preprints, an IEEE DataPort dataset entry, and one
ohmic-contact paper that hit a Crossref rate limit during verification) were
explicitly dropped rather than included unverified; they are named in the
lane reports preserved in this stage's process but are not in the CSV.

## 8. Known duplicate/overlap note

`A0053` (Entler et al. 2021, ceramic-chromium Hall sensors) shares two
authors (Duran, Vyborny) with manuscript `ref3`/`A0055` (Ceran et al. 2019)
but is a distinct publication (different title, different DOI, different
year) — confirmed as a legitimate separate source, not a duplicate entry.
