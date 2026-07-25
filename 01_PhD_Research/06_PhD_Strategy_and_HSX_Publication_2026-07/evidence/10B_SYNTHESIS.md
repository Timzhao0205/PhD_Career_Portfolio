# Stage 10B — fusion/plasma magnetic-diagnostics evidence batch: synthesis

Source: [`evidence/10B_FUSION_DIAGNOSTICS_SOURCES.csv`](10B_FUSION_DIAGNOSTICS_SOURCES.csv) (89
rows, `B0001`-`B0089`). This is one of three parallel literature lanes (10a/10b/10c) that feed
the merged, deduplicated `outputs/01_SOURCE_LEDGER.csv` at stage `10d_literature_merge`. IDs in
this file are provisional (`B####`) and will be renumbered `S####` at the merge stage per
`SOURCE_POLICY.md`. This stage does not decide PhD direction, manuscript route, or publication
strategy (reserved for stages `20_direction` / `30_manuscript`).

## 1. Search and verification method

**External evidence.** Seven parallel auxiliary-model (Sonnet, general-purpose agent) research
lanes were run in parallel, one per required coverage area: (1) Mirnov coils / B-dot probes,
(2) flux loops / diamagnetic loops, (3) integrator drift and long-pulse/steady-state
limitations, (4) fusion-context direct (Hall-probe) sensing precedent, (5) stellarator/HSX-
specific diagnostics and quasi-helical-symmetry theory, (6) magnetic equilibrium reconstruction
and vacuum-field/error-field validation, and (7) calibration/uncertainty methodology and
in-vessel packaging. Each lane used `WebSearch` to find candidates and verified every counted
paper via the Crossref API (`api.crossref.org/works/<doi>`), a PubMed/PMC record, or a direct
publisher DOI-landing-page fetch — never a search-engine snippet alone for existence/peer-review
status. Combined raw yield across the seven lanes was 104 candidate rows.

This main session then:

1. Deduplicated by normalized DOI across all seven lanes, removing 13 duplicate occurrences
   (the same paper independently surfaced by more than one lane — e.g. Chlechowitz et al. 2015's
   HSX magnetic-diagnostic-optimization paper was found by three separate lanes; Spuig et al.
   2015's WEST-integrator paper by three lanes).
2. Excluded one verified peer-reviewed candidate (Amodeo, Arpaia & Buzio 2019, *Sensors*, a CERN
   particle-accelerator flux-transducer drift-correction paper) as off-topic for a
   fusion/plasma-diagnostics batch — it is generic measurement-science drift physics, not a
   fusion or plasma paper — rather than padding the count, matching Stage 10A's precedent of
   excluding an off-topic peer-reviewed candidate (a GMR biosensor paper) instead of counting it.
3. Personally re-verified 10 DOIs directly via the Crossref API (not merely re-reading a lane's
   claim), spread across different lanes, publishers, and eras (1971-2026): `B0001` (Mirnov 1971,
   the foundational paper), `B0005`, `B0006`, `B0060` (Garcia et al. 2025, the "first
   quasi-helically-symmetric" claim source), `B0064` (Chlechowitz et al. 2015, the core HSX
   magnetic-diagnostic paper), `B0069` (Pedersen et al. 2016, Nature Communications), `B0075`
   (Stevenson et al. 2014, the closest direct Hall-probe-in-a-torsatron precedent), `B0051`
   (Duran et al. 2017, ITER bismuth Hall sensor), and `B0014` (Spuig et al. 2015, WEST
   integrators — used to resolve a page-number discrepancy between lanes: one lane reported pp.
   505-508 and two others reported pp. 966-969 for the identical DOI; the Crossref record
   confirms 966-969 is correct). All 10 spot checks matched the reporting lane's claimed
   title/authors/venue/year/DOI exactly.
4. Flagged one cross-lane overlap with Stage 10A rather than silently dropping it: `B0089`... no
   — `B0054` (Kovarik, Ceran, Bolshakova, Holyaka & Erashok 2006, CASTOR safety-factor Hall-probe
   paper) is the identical DOI already present in Stage 10A's ledger as `A0070` (found there via
   the GaN/WBG lane's fusion-comparator search). Per `SOURCE_POLICY.md`, each lane's ledger is
   provisional and cross-lane deduplication is the explicit job of stage `10d_literature_merge`;
   this row is kept here (it is genuinely on-topic for this lane too) with a note flagging the
   overlap for the merge stage.

No DOI in the ledger was guessed. Every row's `doi` field is a bare, Crossref-registered DOI;
`url` is the corresponding `https://doi.org/...` resolver link.

**Inference (this stage).** As in Stage 10A, most full-text publisher pages (ScienceDirect,
AIP Publishing, some IEEE/Springer records) blocked automated fetches with HTTP 402/403 — a
structural access limitation, not a shortcut taken by the lanes. Where this occurred, the row's
`access_level` honestly reflects that only the bibliographic identity (Crossref metadata), not
the content, was independently confirmed. IOPscience (Nuclear Fusion, Plasma Physics and
Controlled Fusion) and PubMed/PMC records were the most consistently fetchable full abstract
sources this session.

## 2. Diagnostic taxonomy and comparison dimensions

The 89 rows organize into seven diagnostic/topic families matching the stage's required coverage:

| Family | Rows | Representative sources |
|---|---:|---|
| Mirnov coil / B-dot probe (inductive, local dB/dt) | 15 | `B0001` (foundational, 1971), `B0005`, `B0006`, `B0012` |
| Flux loop / diamagnetic loop (inductive, global/integral) | 13 | `B0016`-`B0018`, `B0064` (HSX's own) |
| Integrator drift / long-pulse limitation | 12 | `B0029`, `B0034`, `B0036`, `B0037` |
| Fusion-context direct/Hall-probe sensing (non-GaN) | 14 | `B0041`-`B0054` |
| Stellarator/HSX-specific + quasi-helical-symmetry theory | 12 | `B0055`-`B0066` |
| Equilibrium reconstruction / vacuum-field / error-field | 13 | `B0067`-`B0079` |
| Calibration / uncertainty / in-vessel packaging | 10 | `B0080`-`B0089` |

Venue concentration (89 rows, 12 distinct venues): *Review of Scientific Instruments* (22),
*Fusion Engineering and Design* (21), *Nuclear Fusion* (16), *Plasma Physics and Controlled
Fusion* (8), *Fusion Science and Technology* (3), plus single-digit counts across *Sensors*,
*Physics of Plasmas*, *IEEE Transactions on Plasma Science*, *AIP Advances*, *Journal of Nuclear
Materials*, *Physics Letters A*, and *Nature Communications*. Year range 1971-2026 (mean ~2013),
reflecting both foundational (Mirnov 1971; Nuhrenberg & Zille 1988; Boozer 1995; Lao et al. 1985,
1990) and current (2024-2026: `B0043`, `B0049`, `B0053`, `B0060`, `B0077`-`B0079`) literature.
Source type: 86 `journal_article`, 3 `review_article` (`B0038`, `B0052`, `B0057`); quality tier:
58 `A`, 30 `B`, 1 `C` (`B0059`, a 2-page IEEE status note). Access level: 45
`abstract_metadata`, 43 `metadata_only`, 1 `full_text` (`B0047`, an open-access MDPI/PMC paper).

**Comparison dimensions this batch supports, with numbers traced to `source_id`:**

| Dimension | Inductive (Mirnov/flux-loop/diamagnetic) | Non-inductive (Hall-probe, this batch's fusion precedent) |
|---|---|---|
| Fundamental measurement | dB/dt, requires time integration | Direct B (DC-capable) |
| Bandwidth | ~10 kHz-50 MHz (B-dot, `B0006`); Mirnov arrays to hundreds of kHz | Reported fusion Hall probes: JET system operated as the DC/steady-state half of a hybrid architecture (`B0041`); no single-axis bandwidth figure found in this batch for a fusion Hall probe alone |
| Long-pulse/steady-state limitation | Integrator drift explicitly quantified: <8 mV/1000 s at 20 ms time constant (EAST, `B0034`); 10 mV/10 s at RC=0.5 ms (HL-2A, `B0037`); "small offset...significant drift for long pulse" (KSTAR, `B0036`) | None (by design) — this is the argument's core; ITER's own steady-state sensor choice is Hall-effect specifically because it avoids integration (`B0044`, `B0045`) |
| Radiation tolerance (device-physics level) | Mineral-insulated-cable RIEMF/TIEMF drift under irradiation (`B0039`, `B0089`) | InSb stable to 2e18 cm^-2 (`B0041`); bismuth to 1e23 n/m^2 (`B0045`); antimony to 1.4e20 cm^-2 with only 2.3% sensitivity shift (`B0043`); metal (gold) film to 1e24 n/m^2 (per Stage 10A `A0066`, not re-derived here) |
| Calibration accuracy achieved | Rogowski: 2-sigma <=0.5-1.0% of range (`B0024`); EAST pickup-coil system uncertainty budget itemized but not reduced to one number (`B0084`) | ITER OVSS: field-fitting error 1.2 mT over -12 to +12 T (`B0046`); calibration campaign contributes ~2.5 mT of a 4 mT (2-sigma) total-accuracy requirement, described as "at the limit of technical feasibility" (`B0080`) |
| In-vessel packaging precedent | 300+-sensor W7-X suite (`B0063`); JET coil fault/redesign history (`B0012`) | Ceramic (LTCC) co-fired packaging for ITER (`B0082`); paired-sensor redundancy design norm (`B0081`) |
| HSX's own existing suite | 10-turn diamagnetic loop + Rogowski coils + two poloidal belts of 3-axis pickup coils, feeding V3FIT reconstruction (`B0064`) | **No GaN/AlGaN Hall sensor found in this batch integrated into that suite** |

## 3. What direct Hall sensing can and cannot add beyond established diagnostics

**Can add (supported by this batch):**

- **DC/steady-state capability without integrator drift.** Every long-pulse/steady-state
  machine surveyed (W7-X, EAST, KSTAR, HL-2A, WEST/Tore Supra) has published dedicated papers
  whose entire purpose is suppressing integrator drift in inductive sensors (`B0029`, `B0030`,
  `B0032`-`B0037`) — a problem a DC-biased Hall sensor does not have by construction. This is
  the strongest, most literature-supported "can add" claim.
- **A real, chosen engineering path at the field's flagship facility.** ITER's own steady-state
  magnetic-diagnostic set uses Hall sensors specifically to fill the gap inductive coils cannot
  (`B0044`, `B0045`), and JET already runs Hall probes long-term in a hybrid coil+Hall
  architecture (`B0041`) — this is not a hypothetical benefit; it is the field's actual design
  choice for the DC-measurement gap.
- **Compact, flexible placement.** Multiple Mirnov-array papers document real constraints from
  coil spacing/placement (unevenly spaced arrays requiring dedicated sparse-recovery signal
  processing at JET, `B0008`; spatial-aliasing analysis at KTX, `B0007`) that a small solid-state
  point sensor sidesteps.

**Cannot add / not supported by this batch (evidence gaps, stated plainly):**

- **No peer-reviewed paper in this batch reports a GaN or AlGaN Hall sensor deployed in any
  tokamak or stellarator.** Every fusion-context direct-sensing precedent found (`B0041`-`B0054`)
  uses InSb, bismuth, antimony, gold, or an unspecified commercial Hall IC — never GaN. This
  matches and reinforces Stage 10A's independent finding (`evidence/10A_SYNTHESIS.md` §4).
- **No evidence a Hall sensor alone displaces Mirnov/flux-loop diagnostics for the measurements
  those diagnostics are actually good at** (MHD mode-number/frequency identification, fast
  transient stored-energy changes such as ELMs, `B0005`, `B0026`). The literature's own answer is
  *hybrid* sensor fusion (coil for bandwidth, Hall for DC accuracy), demonstrated algorithmically
  at KSTAR (`B0049`) and COMPASS-U/JET (`B0053`), and architecturally at JET (`B0041`) — not
  Hall-only replacement.
- **No GaN-specific fusion radiation/vacuum/thermal qualification data exists** in this batch
  (consistent with Stage 10A's finding that GaN radiation tolerance evidence is device-physics-
  level only, not fusion-Hall-sensor-specific). The closest comparators — bismuth, antimony, gold
  — have multi-year, multi-fluence qualification campaigns (`B0042`, `B0043`, `B0045`) that a GaN
  fusion Hall sensor does not yet have a published counterpart to.
- **No single-axis bandwidth or noise-floor figure for a fusion-deployed Hall probe was found in
  this batch**, so a like-for-like Hall-vs-Mirnov bandwidth comparison cannot be made purely from
  this lane's evidence (Stage 10A's `A0011`/`A0016` device-physics noise-floor numbers are the
  closest available, but those are bench measurements, not in-vessel fusion measurements).

## 4. Strongest and weakest novelty claims for the supplied HSX work

**Strongest claim this batch supports:** *first application of a GaN/AlGaN semiconductor Hall
sensor to in-vessel magnetic diagnostics on any magnetic-confinement-fusion device.* Every
fusion-context Hall-probe precedent this batch found — CASTOR (`B0048`, `B0054`), JET (`B0041`,
`B0042`), ITER design/final-design/testing work (`B0044`-`B0046`, `B0050`, `B0051`, `B0080`,
`B0081`), and the DEMO materials-outlook review (`B0052`) — uses InSb, bismuth, antimony, gold,
or an unspecified commercial IC, never GaN. This is an absence-of-evidence finding (a search
result, not proof no such work exists anywhere), and it is the same conclusion Stage 10A reached
independently from the GaN/WBG-focused lane, which strengthens rather than weakens it.

**A second, narrower and highly specific strong claim:** the manuscript's own facility framing
("HSX is the first quasi-helically symmetric stellarator") has a directly citable, peer-reviewed
2025 source — but with a precise wording difference worth correcting. Garcia et al. 2025 (`B0060`)
states verbatim: *"HSX is the first and only stellarator experiment optimized for quasi-helical
symmetry (QHS)"* — i.e. "first...experiment optimized for QHS," not literally "first
quasi-helically-symmetric stellarator." The original 1995 HSX design paper (`B0058`) itself uses
only "unique," never "first." **Recommendation (for stage `30_manuscript`, not decided here):**
cite `B0060` for the facility-priority claim and match its precise phrasing, rather than the
looser paraphrase, to avoid an easily-checked overclaim a reviewer could flag.

**Weakest claim / most exposed gap:** *novelty via "current-spinning offset cancellation" or
"calibration" alone.* Both Stage 10A (`A0005`, `A0033`-`A0038`) and this batch's calibration
literature show the field already has mature, quantitative Hall-sensor calibration methodology
(`B0046`, `B0080`, `B0084`) and current-spinning is decades-old prior art. If the manuscript or
its revision leans its novelty argument on "we calibrated a Hall sensor" or "we used current
spinning" rather than "we did so *inside a stellarator, in the specific GaN material system*,"
this batch's evidence base does not support that as new. This directly corroborates Reviewer 2's
decline rationale (per `outputs/00_CLAIM_BASELINE.csv` C008: "insufficient citation of prior GaN
Hall-device literature") from the fusion-diagnostics side of the literature, independent of the
GaN-device-physics side Stage 10A already covered.

**A related, second-order weak point:** the AEIC's explicit request (`outputs/00_CLAIM_BASELINE.csv`
C010) for a conventional-probe (B-dot/Mirnov) comparison is achievable — this batch supplies
extensive B-dot/Mirnov bandwidth, drift, and design literature (`B0002`, `B0006`-`B0009`) — but
**no comparison data currently exists in the supplied HSX materials** (per Stage 00's inventory);
this is an experiment/analysis gap, not a literature gap, and is explicitly out of scope for this
evidence-gathering stage (deferred to stage `40_experiment`).

## 5. Quantitative validation practices expected in fusion instrumentation

This batch establishes a clear expected standard, useful as a rubric for evaluating the supplied
manuscript and for planning the next HSX campaign (both deferred to later stages):

1. **An explicit, itemized uncertainty budget**, not a single number — e.g. EAST's breakdown by
   sensor-area error, integrator/acquisition error, cable attenuation, and vacuum-shot
   cross-checks (`B0084`); ITER Rogowski worst-case-plus-statistical error modeling (`B0024`).
2. **Calibration against a physical standard or independent method**, not just internal
   consistency — e.g. CTH's Hall-array calibration against Biot-Savart vacuum-field modeling
   (`B0075`, the closest direct methodological analogue to validating an HSX Hall sensor); W7-X's
   electron-beam flux-surface mapping validating the vacuum field to 1 part in 100,000 (`B0069`).
3. **Reported accuracy against a stated target**, framed relative to the measurement's intended
   use — ITER's 4 mT (2-sigma) requirement over 0-2.5 T with the calibration's own contribution
   quantified (`B0080`); DIII-D's ~1 mm vertical-position control accuracy (`B0076`).
4. **Environmental qualification reported as a program, not a single test** — neutron fluence,
   temperature cycling, *and* field range tested together and reported with the resulting
   sensitivity/drift change (`B0043`, `B0045`, `B0085`), not a single bench measurement at room
   temperature.
5. **Long-term/multi-pulse operational stability data, not just an initial calibration** — JET's
   18-sensor, 19,000-pulse, 11-year calibration-stability record at +/-0.07% (`B0041`) is the
   clearest example of this expectation at the high end.

By this rubric, the submitted manuscript's own single-module, uncalibrated, single-campaign
(per `outputs/00_CLAIM_BASELINE.csv` C001, C005, C007) status is well short of the field's
established validation norm — consistent with, and reinforcing, the AEIC's and both reviewers'
stated concerns (C008-C010). This is a factual gap-comparison, not a publication-route decision;
that decision belongs to stage `30_manuscript`.

## 6. HSX-specific evidence gaps

1. **No peer-reviewed paper in this batch (or Stage 10A) reports a GaN/AlGaN Hall sensor
   operated inside HSX or any other stellarator/tokamak.** Confirmed independently by two
   separate search lanes across two stages.
2. **No peer-reviewed HSX-specific Hall-sensor calibration, uncertainty, or conventional-probe
   (B-dot/Mirnov) comparison study was found.** HSX's own existing magnetic-diagnostic literature
   (`B0064`) covers its diamagnetic-loop/Rogowski/pickup-coil suite and V3FIT reconstruction, but
   contains no Hall-effect sensor content.
3. **The manuscript's "first quasi-helically symmetric stellarator" claim needs a citation
   correction, not a retraction** — `B0060` supports a closely related but more precisely worded
   claim ("first experiment optimized for QHS"); `B0056` (Garren & Boozer 1991) further notes
   exact quasi-helical symmetry cannot exist, only be approximated, which is a substantive nuance
   the manuscript's phrasing should not paper over.
4. **No literature in this batch quantifies what spatial/vector coverage advantage a 2-3 axis
   HSX vector probe (project 03) would have over HSX's existing pickup-coil belts** — the closest
   analogue is `B0064`'s finding that adding 80 well-placed magnetic sensors reduced HSX's
   equilibrium-solution ambiguity ~7-fold, which stage `40_experiment` may find useful as a
   sensor-placement-value precedent, but no source in this batch performs that comparison for a
   Hall-type sensor specifically.
5. **No source in this batch or Stage 10A establishes what "success" looks like quantitatively
   for a first-generation, single-axis GaN Hall sensor in a stellarator** (e.g., what
   accuracy/bandwidth/drift a reviewer or the field would consider a meaningful first
   demonstration) — the closest available quantitative bars come from non-GaN, more mature
   ITER/JET programs (§5 above), which may not be a fair target for a first-generation academic
   device; this calibration-target question is explicitly deferred to stage `40_experiment`.

## 7. Row count

**89 valid, unique, verified peer-reviewed rows** (`B0001`-`B0089`), all
`peer_review_status = verified_peer_reviewed`, all deduplicated by normalized DOI (0 duplicate
DOIs, 0 duplicate `source_id` values — verified programmatically: 89 rows, 16 columns, no empty
required fields, all `quality_tier`/`access_level`/`source_type` values within the allowed
enums). This exceeds both the stage floor (55) and the stage target (65). One additional
verified peer-reviewed candidate found during search (a CERN particle-accelerator flux-transducer
drift-correction paper) was deliberately excluded as off-topic for a fusion/plasma-diagnostics
batch rather than counted toward this total; 13 duplicate cross-lane occurrences of already-
counted DOIs were removed rather than double-counted. One row (`B0054`) is flagged as sharing a
DOI with Stage 10A's `A0070` — a legitimate cross-lane overlap left for stage `10d`'s merge to
resolve, not an error in this ledger.
