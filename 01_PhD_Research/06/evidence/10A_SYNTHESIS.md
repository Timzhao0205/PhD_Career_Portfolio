# Stage 10A — GaN/WBG/Hall-sensor evidence batch: synthesis

Source: [`evidence/10A_GAN_WBG_SOURCES.csv`](10A_GAN_WBG_SOURCES.csv) (70
rows, `A0001`-`A0070`). This is one of three parallel literature lanes
(10a/10b/10c) that feed the merged, deduplicated `outputs/01_SOURCE_LEDGER.csv`
at stage `10d_literature_merge`.
IDs in this file are provisional (`A####`) and will be renumbered `S####` at
the merge stage per `SOURCE_POLICY.md`. This stage does not decide PhD
direction or publication route (reserved for stage `20_direction`).

## 1. Search and verification method

**External evidence.** Six parallel auxiliary-model (Sonnet, general-purpose
agent) research lanes were run in parallel, one per required coverage area:
(1) AlGaN/GaN 2DEG and comparable III-V Hall devices, (2) Hall geometry/
sensitivity/offset/planar Hall/cross-axis, (3) spinning-current/offset-
cancellation methods, (4) noise/drift/linearity/bandwidth/packaging/
calibration/temperature coefficient, (5) GaN/SiC/WBG harsh-environment
devices, (6) prior GaN Hall-sensor reviews and fusion/tokamak Hall-probe
novelty comparators. Each lane used `WebSearch` to find candidates and
`WebFetch` on publisher pages, DOI resolvers, or PubMed Central mirrors to
confirm peer-review status, or the Crossref API (`api.crossref.org/works/
<doi>`) when publisher pages blocked automated fetches (IEEE Xplore, AIP
Publishing, ScienceDirect, and Wiley returned HTTP 402/403 or blank
JavaScript-rendered pages to nearly all direct fetch attempts in this
session — a structural access limitation, not a shortcut taken by the
lanes). Every row records its own `verification_basis`.

Combined raw yield across the six lanes was 88 candidate rows. This main
session then:

1. Deduplicated by normalized DOI, yielding 70 unique candidates.
2. Personally re-verified 8 DOIs directly (not just re-reading the lane's
   claim), spread across different lanes and publishers: `A0004`, `A0012`,
   `A0016`, `A0033`, `A0045`, `A0060`, `A0068`, `A0070`. All 8 matched the
   reporting lane's claimed title, authors, venue, and DOI. One metadata
   inconsistency was found (`A0070`: Crossref itself returns two different
   author-name transliterations across queries for the same DOI/title/
   volume/pages — most likely a diacritic-encoding artifact in the source
   journal's metadata, not evidence of two different papers or a fabricated
   citation) and is flagged in that row's `notes`.
3. Excluded one candidate (a peer-reviewed GMR/magnetoresistive biosensor
   paper found by lane 3) as off-topic for a Hall-effect-focused batch,
   rather than padding the count, per the stage instruction.
4. Assigned merged `topic_tags`/`claims_supported` where a source was
   independently found by more than one lane (e.g. `A0004`, `A0005`,
   `A0006`, `A0010`, `A0012` recurred across 2-3 lanes).

No DOI in the ledger was guessed. Every row's `doi` field is a bare,
Crossref-registered DOI; `url` is the corresponding `https://doi.org/...`
resolver link.

**Inference (this stage).** Because most full-text publisher pages were
inaccessible, the batch leans on Crossref bibliographic metadata (title/
author/venue/volume/issue/page/date — an authoritative registration record,
not a secondary summary) for confirming a source *exists and is peer-
reviewed*, while `access_level` honestly tracks how much of the *content*
(not just the bibliographic identity) was actually read. See §6.

## 2. Venue and year distribution

70 rows span 39 distinct venues and years 1974-2026 (52 years). No single
venue dominates; the top venues are legacy Hall-sensor-physics journals
plus modern open-access outlets used heavily by the GaN Hall-sensor
sub-field itself:

| Venue | Count |
|---|---:|
| Sensors and Actuators A: Physical | 9 |
| Sensors (MDPI) | 8 |
| IEEE Sensors Journal | 7 |
| Applied Physics Letters | 4 |
| Solid-State Electronics | 2 |
| Nuclear Fusion | 2 |
| IEEE Journal of Solid-State Circuits | 2 |
| Fusion Engineering and Design | 2 |
| IEEE Transactions on Magnetics | 2 |
| (29 further venues) | 1 each |

Year distribution (5-year bins):

| Period | Count |
|---|---:|
| 1974-1990 | 3 |
| 1991-1995 | 3 |
| 1996-2000 | 5 |
| 2001-2005 | 5 |
| 2006-2010 | 9 |
| 2011-2015 | 12 |
| 2016-2020 | 15 |
| 2021-2026 | 18 |

Source type: 54 `journal_article`, 12 `review_article`, 4 `conference_paper`
(all conference entries are verified peer-reviewed proceedings — JPCS, IEEE
Sensors 2004, ASICON 2007, IEEE iSES 2022). Quality tier: 40 `A`, 27 `B`,
3 `C`. Access level: 31 `abstract_metadata`, 29 `metadata_only`, 10
`full_text` (see §6 for what this limits).

## 3. Performance/novelty comparison dimensions for a manuscript table

**Supplied fact (from
[`outputs/00_CONFLICT_LEDGER.md`](../outputs/00_CONFLICT_LEDGER.md) /
[`00_CLAIM_BASELINE.csv`](../outputs/00_CLAIM_BASELINE.csv), not re-derived
here).** The submitted manuscript's own sensor is
voltage-biased and uncalibrated, per Stage 00's baseline; project 02's
current-spinning calibrated successor is a bench/emulator-stage design
target, not an achieved calibration (`C6`).

**External evidence — quantitative anchors found this session** (each
number traceable to its `source_id`; only `full_text`- or
`abstract_metadata`-tagged rows are cited numerically, per §6):

| Dimension | GaN/AlGaN Hall (this field) | Non-GaN comparators found |
|---|---|---|
| Current-scaled sensitivity | 55-94.6 V/A/T RT (`A0001` 77; `A0004` 68.9; `A0006` mean 60.2; `A0016` 94.6; `A0017` 55) | GaAs 2DEG up to ~4300 V/A/T at RT dropping to ~2500 V/A/T at high temp (`A0009`); GaAs-InGaAs-AlGaAs IC 533 uV/uT / down to 177 nT detection (`A0014`); InAs/AlSb 2DEG ~570 V/A/T (`A0011`) |
| Temperature stability of sensitivity | GaN current-scaled sensitivity varies only ~10-13% from RT to 576 C (`A0006`); GaN ~40-50 V/A/T with little variation 300-500 K (`A0009`) vs. GaAs dropping ~40% over the same range (`A0009`) | GaAs voltage-scaled degrades sharply with temperature (`A0006`, `A0009`) |
| Temperature coefficient | 103 ppm/C to 300 C (`A0017`); <745 ppm/K, 403-500 K (`A0016`) | — |
| Offset after current spinning | GaN: ~3.4 +/- 2 uT residual, -100 to 200 C (`A0005`); Si CMOS randomized spinning: 130+/-22 uT -> 23+/-22 uT at 820 kHz BW (`A0039`) | Si vertical Hall ~90% offset reduction via contact redesign (`A0052`); Si CMOS digital Hall +/-2 mT sensitivity, 4 mT hysteresis, -40 to 120 C (`A0053`) |
| Noise floor | GaN: 44.3 uV pk-pk / 15.7 uV RMS (`A0016`) | InAs/AlSb 0.25 uT/sqrt(Hz) at 3 kHz, 0.027 uT/sqrt(Hz) gate-suppressed (`A0011`); ferromagnetic-AHE (not ordinary Hall) 50 nT/sqrt(Hz) at 1 kHz (`A0045`, flagged as a different physical mechanism) |
| Calibration methodology/uncertainty | Not found GaN-specific | General traceable Hall-probe calibration: +/-(7 mT + 13%), 5-term uncertainty budget (`A0051`) |
| In-vessel fusion Hall-probe precedent (any material) | **None found this session using GaN or any semiconductor 2DEG Hall sensor inside a stellarator or tokamak** | Metal (Au-film) Hall, DEMO-scale, tolerant to 1e24 n/m^2, <1% sensitivity change (`A0066`); antimony Hall, DEMO/ITER steady-state design (`A0067`); InSb Hall, JET, 11+ years/19,000+ pulses, +/-0.07% calibration stability (`A0068`); Hall probe, EAST toroidal field (material unconfirmed) (`A0069`); Hall probe, CASTOR safety-factor measurement (`A0070`) |
| Radiation tolerance (device-physics level, not this mission's experimental scope) | GaN HEMT tolerance to 1e13 cm^-2 at 380 keV protons (`A0002`); GaN/SiC radiation-damage mechanism reviews (`A0054`, `A0055`, `A0058`) | SiC Schottky diode radiation resistance under D-T fusion neutrons (`A0063`); SiC IBIC fusion detectors (`A0064`) |

**Recommendation (this stage, for later manuscript/direction stages to use
or reject).** A manuscript comparison table built from this batch should
present GaN's advantage as *temperature-stable current-scaled sensitivity
across a wide range* rather than *highest raw sensitivity* (GaAs/InAs 2DEG
platforms are more sensitive at room temperature but degrade faster with
temperature per `A0006`/`A0009`/`A0011`/`A0014`). The strongest, most
defensible novelty claim supported by this batch is: **first application of
a GaN/AlGaN 2DEG Hall sensor specifically to in-vessel stellarator (or any
magnetic-confinement-fusion device) magnetic diagnostics** — every fusion
in-vessel Hall-probe precedent found (`A0066`-`A0070`) uses a non-GaN
material system. This is a proposed framing, not a decided direction;
stage `20_direction` and `30_manuscript` must independently weigh it
against the calibration-gap and offset-characterization prior art in §4.

## 4. Established results versus unresolved questions

**Established (peer-reviewed, this batch):**

- Current-spinning/chopper offset cancellation is decades-old, general Hall-
  sensor prior art (`A0033`-`A0038`, `A0041`-`A0043`, foundational Munter
  1990/1991 `A0033`/`A0034`), and has already been demonstrated
  specifically on AlGaN/GaN 2DEG Hall plates by the Senesky group
  (`A0005`, published in the same venue, *IEEE Sensors Letters*, as the
  submitted manuscript).
- Geometry-driven sensitivity/offset trade-offs (current-related vs.
  voltage-related sensitivity) are characterized for AlGaN/GaN and
  InAlN/GaN specifically (`A0004`, `A0006`, `A0016`).
- GaN Hall sensitivity is markedly more temperature-stable than GaAs/InSb
  incumbents in the current-biased mode (`A0006`, `A0009`).
- Hall-effect in-vessel magnetic diagnostics is an established ~20-year
  practice in tokamaks (CASTOR 2006, EAST 2009, JET through 2021, DEMO
  design studies through 2019-2022: `A0066`-`A0070`), using metal,
  antimony, or InSb sensing elements — never (in this search) GaN.
- GaN and SiC device-level radiation tolerance is an active, separately
  reviewed literature (`A0002`, `A0054`, `A0055`, `A0058`), distinct from
  any GaN Hall-sensor-specific radiation test.

**Unresolved / not found in this batch (evidence gaps, to carry into later
stages, not filled by inference):**

- No peer-reviewed paper was found reporting a GaN or AlGaN Hall sensor
  operated inside a stellarator or tokamak. This batch cannot confirm
  whether such work exists outside what this search surfaced — only that
  none was found and verified.
- No GaN-Hall-sensor-specific traceable calibration methodology or
  uncertainty budget was found (`A0051` is a general Hall-probe calibration
  methodology, not GaN-specific).
- No unified single source was found presenting a GaN-vs-Si-vs-GaAs-vs-InSb
  Hall sensor performance comparison table across sensitivity, offset,
  noise, and temperature range in one place; `A0065` is the closest review
  found and explicitly lacks a GaN row (flagged in its own `notes`).
- No GaN-Hall-sensor-specific radiation or neutron-fluence test was found;
  radiation-tolerance evidence for GaN is at the general HEMT/device level
  (`A0002`), not the Hall-sensor-in-a-fusion-neutron-field level that
  exists for SiC diodes (`A0063`) and non-GaN Hall probes (`A0066`,
  `A0068`).

## 5. Implications for the submitted GaN Hall sensor (framed as inference/
   recommendation, not a decided direction)

**Inference.** If a reviewer raises a novelty objection against the
submitted manuscript on the grounds that "GaN Hall sensor offset/geometry
characterization already exists," that objection is well supported by this
batch (`A0004`, `A0005`, `A0006`, `A0012`, `A0016` — several from the same
PI's own lab lineage, which a reviewer could interpret either as
"established competence" or as "not new," depending on framing). Conversely,
if the manuscript's or a revision's novelty claim is narrowed to
*first-in-a-stellarator (or first-in-fusion) application of a GaN Hall
sensor*, this batch found no peer-reviewed counter-example — that narrower
claim currently holds up against the literature searched.

**Recommendation (for stage `30_manuscript` to accept, adjust, or reject,
not decided here).** Any revision should (a) explicitly cite the prior
current-spinning/offset-cancellation GaN literature (`A0004`-`A0006`,
`A0012`) rather than implying the technique is novel to this group's next
paper, and (b) lean the novelty argument on the fusion/stellarator
application gap identified in §3-4, which this batch's search did not find
a counter-example to.

**Unresolved gate.** Whether this framing is legally/scientifically
sufficient novelty for the target venue(s) is a stage `20_direction` /
`30_manuscript` decision, not decided by this evidence-gathering stage.

## 6. Limitations caused by abstract-only or metadata-only access

29 of 70 rows (41%) are `metadata_only` — only the bibliographic record
(title/authors/venue/volume/pages/DOI) was independently confirmed; no
abstract or body text was read this session for these rows. 31 of 70 (44%)
are `abstract_metadata` — abstract-level content was read or reliably
reconstructed from a search snippet quoting the abstract, but the full
paper was not read. Only 10 of 70 (14%) are `full_text` — the paper's
methods/results were actually read beyond the abstract (`A0016`, `A0039`,
`A0040`, `A0045`, `A0051`, `A0052`, `A0053`, `A0065`, `A0066`, `A0068`).

**Practical consequence for later stages:** any quantitative number quoted
from a `metadata_only` row in this ledger (e.g. `A0007`, `A0008`, `A0018`,
`A0027`-`A0030`, `A0033`(partial), `A0034`-`A0036`, `A0042`, `A0044`,
`A0046`-`A0050`, `A0055`, `A0057`, `A0061`, `A0062`, `A0064`, `A0069`) is
either not present in this ledger's `notes` field at all, or was sourced
from a search-engine snippet rather than the primary text and should be
re-confirmed against the primary source before being placed in a
manuscript table with a specific numeric claim attributed to it. The 10
`full_text` rows and the subset of `abstract_metadata` rows with explicit
numbers in their `notes` field (see the comparison table in §3) are the
higher-confidence numeric sources for a manuscript-ready comparison table.
This access limitation is a structural result of IEEE Xplore, AIP
Publishing, ScienceDirect, and Wiley blocking automated fetches in this
session, not a shortcut taken by the search.

## 7. Row count

**70 valid, unique, verified peer-reviewed rows** (`A0001`-`A0070`), all
`peer_review_status = verified_peer_reviewed`, all deduplicated by
normalized DOI (0 duplicate DOIs, 0 duplicate `source_id` values — verified
programmatically against the CSV). This exceeds both the stage floor (55)
and the stage target (65). One additional peer-reviewed candidate found
during search (a GMR/magnetoresistive biosensor paper) was deliberately
excluded as off-topic rather than counted toward this total.
