# Stage 00 — Scope Audit

Run: HSXIP-20260805T071311Z. Scope authority: `IP_SCOPE.md`, `CLAUDE.md`.
This audit is a fact/anomaly record, not a legal opinion and not an exhaustive
forensic source scrub (source-scrub depth is Stage 50's job).

## 1. Controlling publication

**Title (fact, from `IP_SCOPE.md` and confirmed in `regular_lsens.tex` line
370):** "AlGaN/GaN Hall-Effect Sensor for In-Situ Magnetic Field Monitoring of
the HSX Stellarator."

**Authors (fact, from `regular_lsens.tex` lines 381–388):** Yiming Zhao
(Stanford EE, corresponding, timzhao@stanford.edu), Wayne Goodman (UW-Madison
Nuclear Engineering & Engineering Physics, Senior IEEE Member), Thomas
Gallenberger (UW-Madison NEEP), Jasmine M. Cox (Stanford EE), Benedikt Geiger
(UW-Madison NEEP), Debbie G. Senesky (Stanford EE and Aero/Astro, corresponding
author, Senior IEEE Member). Venue: IEEE Sensors Letters ("Sensor
Applications" subject line). Acknowledgment cites DOE Contract
DE-AC02-76SF00515, SLAC FWP 101264, TomKat Center for Sustainable Energy
(Stanford), fabrication at Stanford Nanofabrication Facility (NNCI, NSF Award
ECCS-2026822). This is a fact directly relevant to Stage 50's
sponsor/coauthor/inventor questions.

## 2. Controlling artifacts and integrity

Three artifacts, as specified in `IP_SCOPE.md`:

| Artifact | Manifest SHA-256 | Recomputed SHA-256 | Match |
|---|---|---|---|
| `inputs/manuscript/source_original.zip` | a4748e8e962d33931f67db8b82f9c136b7b783ff27aa33babef56a6afec65a6e | a4748e8e962d33931f67db8b82f9c136b7b783ff27aa33babef56a6afec65a6e | Yes |
| `inputs/manuscript/submission.pdf` | fa1563a04a7fdc79c80c38d39db8f69d4af50291fe010e5808249cf457d0e48c | fa1563a04a7fdc79c80c38d39db8f69d4af50291fe010e5808249cf457d0e48c | Yes |
| `inputs/manuscript/source/regular_lsens/regular_lsens.tex` | fc34b033802de487bfdd39e9dc4eeb568fc3d4854b6734d196975ef9701c509e | fc34b033802de487bfdd39e9dc4eeb568fc3d4854b6734d196975ef9701c509e | Yes |

All three hashes independently recomputed by this stage and match
`inputs/HASHES.sha256` exactly. No integrity issue found. `submission.pdf` is
9 pages (matches the "nine-page submission bundle" description in
`IP_SCOPE.md`), 2,614,676 bytes, produced by Aspose.PDF for Java 25.6
(CreationDate 2026-07-02). Its embedded XMP Title/Author fields are blank
(verified with `pdfinfo`), so no template metadata leaked into the submission
PDF.

`source_original.zip` contains exactly 17 entries (2 directory entries + 15
files), consistent with the "17-entry source archive" description in
`IP_SCOPE.md`:

- `regular_lsens/`, `regular_lsens/figures/` (directories)
- `regular_lsens/figures/fig1.pdf`, `fig2.pdf`, `fig3.pdf`, `fig4.pdf`,
  `fig4-eps-converted-to.pdf`, `fig4.eps`, `fig5.pdf`(via eps-converted)
  — precisely: `fig4.eps`, `fig4-eps-converted-to.pdf`, `fig4.pdf`, `fig5.eps`,
  `fig5-eps-converted-to.pdf`
- `regular_lsens/graphical_abstract.pdf`
- `regular_lsens/IEEE_lsens.cls` (stock IEEE Sensors Letters class file,
  unmodified — header text matches the public Michael Shell IEEEtran-derived
  template verbatim)
- `regular_lsens/regular_lsens.tex` (identical bytes/hash to the extracted
  copy under `inputs/manuscript/source/`)
- `regular_lsens/regular_lsens.aux`, `regular_lsens.log`,
  `regular_lsens.synctex.gz`, `regular_lsens.pdf` — LaTeX build byproducts

No entries reference or resemble the excluded PhD/startup archives; no
nested archives, hidden files, or unrelated file types were found.

## 3. Included technical groups (as scoped by `IP_SCOPE.md`, confirmed present in the TeX body)

1. **Hall device and fabrication** — purchased NTT Advanced Technology
   AlGaN/GaN heterostructure wafer (3.7 µm buffer, 300 nm GaN, 1 nm AlN
   spacer, 22 nm Al0.28Ga0.72N barrier); fabrication at Stanford
   Nanofabrication Facility; mesa etch; Ti/Al/Mo/Au ohmic contacts annealed at
   850 °C/35 s; 7 nm Al2O3 passivation; vias; Ti/Au bond metal; 5 mm × 5 mm
   die; regular octagonal Hall plate, 200 µm inscribed diameter (§II-A).
2. **UHV/GDC module** — Al wire bonds to ceramic LCC (Spectrum Semiconductor
   Materials); EPO-TEK 353ND epoxy encapsulation; 150 °C vacuum bake, 1 hour;
   custom zirconia ceramic holder; stainless-steel standoff; insertion into
   HSX vessel; grounded graphite shield over the module to reduce arcing and
   epoxy degradation during GDC and plasma operation (§II-B).
3. **Bias and readout** — voltage-biased Hall plate (0.4 V bias vs. 0 V
   unbiased); Keysight DSOX1204G oscilloscope waveform generator for bias;
   INA849 instrumentation amp + two OPA814 stages; total gain 200 V/V;
   1 MHz bandwidth; external electronics via vacuum feedthroughs (§II-C).
4. **Deployment and validation method** — in-vessel deployment near the HSX
   plasma edge; 68 consecutive shots; biased-vs-unbiased and
   plasma-discharge-vs-coil-only comparisons (shots 63/65/68); temporal
   comparison of amplified sensor output against HSX diamagnetic-loop stored
   energy across high-energy (shot 21), late-breakdown (shot 18), and
   failed-breakdown (shot 19) cases, with a documented ~30 ms DAQ timing
   offset (§III).

All four groups match `IP_SCOPE.md` verbatim; no additional technical group
appears in the rendered text beyond these four.

## 4. Explicit future work (fact, §III/Conclusion, matches `IP_SCOPE.md`)

- No absolute magnetic-field calibration is demonstrated; V_off calibration
  and its temperature dependence are future work.
- Extended-duration deployment to evaluate offset stability — future work.
- Radiation and neutron irradiation characterization at a dedicated facility
  — future work.
- Lower-noise readout electronics for resolving smaller-amplitude MHD
  fluctuations — future work.
- The paper states temporal correlation, not interchangeable measurement,
  between local field and volumetric stored energy.

Per `CLAUDE.md` and `IP_SCOPE.md`, these future-work sentences are prior-art
context for later stages, not disclosed inventions of this manuscript.

## 5. Excluded concepts (not evaluated as manuscript IP, per `IP_SCOPE.md`)

Three-axis/vector Hall probes; Hall-plus-inductive-coil hybrid/mutual
calibration probes; radiation-compensation, current-spinning,
self-calibration, or sensitivity-recovery architectures not implemented in
this paper; TCAD/simulation publications, startup ideas, power
electronics/converters, future PhD directions, and other folder-06 concepts;
any new package design invented during later analysis stages (permissible
only as labeled future design-around ideas, never as disclosed inventions).
None of these appear as implemented, validated content in the rendered TeX
body — confirmed by full-text read of the manuscript's technical sections.

## 6. TeX comment and source-disclosure inspection

Full line-by-line review of all `%`-comment content in
`regular_lsens.tex` (619 lines). Findings:

- **No scope-violating content.** All comments are either (a) standard
  IEEEtran/IEEE_lsens template boilerplate (package-usage notes, legal
  notice, LPPL license text, editorial instructions — lines 2–325, 437–550)
  that also ships in the public IEEE_lsens class documentation, or (b)
  inert leftover template placeholders never rendered into the PDF.
- **Anomaly — unrendered alternate abstract (source-disclosure item, not a
  scope violation).** Lines 420–423 contain a commented-out ~180-word
  "full" abstract, superseded by the ~150-word abstract actually used
  (`\begin{abstract}[graphical_abstract]`, lines 427–429; labeled "150 words
  version" at line 425). The commented alternate wording is substantively
  the same content as the rendered abstract (slightly more verbose, e.g.
  explicitly states "voltage-biased at 0.4 V" and "differential amplifier
  chain" phrasing) and discloses no technical group, parameter, or result
  beyond what is already in the rendered paper body. Flagged only because it
  is extra text present in the TeX source that would ship inside an arXiv
  source tarball and is not visible in the PDF-rendered version — a Stage 50
  source-hygiene item, not an IP-scope item.
- **Anomaly — inert leftover hyperref template metadata.** Lines 303–306
  contain an unused `\hypersetup{pdftitle={Bare Demo of IEEE\_lsens.cls for
  IEEE Sensors Letters}, pdfauthor={Michael D. Shell}, ...}` block, carried
  over from the public Michael Shell demo template and never edited for this
  paper. The `hyperref` package itself is never loaded (its `\usepackage`
  line, 284/286, remains commented out), so this block is dead code with no
  effect on typesetting. Confirmed non-issue: `pdfinfo` on
  `submission.pdf` shows blank Title/Author metadata, so this placeholder
  text is not present in the actual submitted PDF. Recorded as a source
  hygiene anomaly only.
- **Anomaly — stale copyright-year placeholder.** Line 438,
  `\IEEEpubid{1949-307X \copyright\ 2023 IEEE...}`, is boilerplate publisher
  ID text carried from the template (year 2023) and is not a factual
  publication-year claim by the authors; it is a cosmetic template artifact,
  not a scope or disclosure issue.
- No `TODO`/`FIXME`/`XXX`/`\iffalse`/`\begin{comment}`/"confidential"/"do not
  submit" or similar author notes-to-self were found anywhere in the file
  (explicit regex sweep, case-insensitive, zero matches beyond this audit's
  own search).
- No named individuals, institutions, funding numbers, or technical detail
  appear in comments beyond what is stated in the rendered body and
  Acknowledgment section.

## 7. ZIP build-artifact source-disclosure hazard (fact)

`regular_lsens.log` and `regular_lsens.synctex.gz` (both inside
`source_original.zip`) embed the **local compile-machine absolute path**
`d:/timzhao/Downloads/regular_lsens/regular_lsens.tex` (and sibling TeX Live
install path `d:/texlive/2024/...`) in multiple lines. This discloses the
compiling user's local Windows username-adjacent folder structure
(`d:/timzhao/Downloads/...`) and machine layout. It is a **privacy/source-hygiene
hazard for an arXiv source upload**, not a technical/IP disclosure hazard — no
additional device, package, readout, or result information is present beyond
what the rendered PDF shows. `.log`, `.aux`, and `.synctex.gz` are non-standard,
unnecessary inclusions in a LaTeX source submission (arXiv only needs `.tex`,
`.cls`, and figure files) and should be stripped before any arXiv source
upload. This finding is handed to Stage 50 (`50_SOURCE_SCRUB.md`) for
disposition; Stage 00 does not recommend action, only records the fact.

`IEEE_lsens.cls` is the unmodified stock class file (byte content matches the
public Michael Shell IEEEtran-derived template header verbatim) — no injected
or hidden text.

No other ZIP entry (figures, `.pdf` build output) was found to contain text
content beyond what is rendered in `submission.pdf`; figures were inventoried
by name/size/timestamp only, per instruction not to analyze contents beyond
scope-relevant inspection.

## 8. Excluded large archives — absence confirmation

`inputs/context/excluded_archives.csv` records two archives as excluded by
disposition and never provided as working inputs to this run:

- `01_PhD_Research (2)(1).zip` (203,468,226 bytes) — excluded, "broader PhD
  and later concepts outside the named publication."
- `02_Startup(8).zip` (152,168,953 bytes) — excluded, "startup portfolio is
  outside the publication-only IP question."

**Confirmed absent from the working input tree.** A directory listing of
`inputs/` and `inputs/manuscript/` (the only artifact locations named in
`IP_SCOPE.md`) shows no such files anywhere in this package — only
`HASHES.sha256`, `context/excluded_archives.csv`, `prior_art_seeds.csv`, and
the three `manuscript/` artifacts audited above. This audit did not open,
list, or analyze the contents of either excluded archive, consistent with
`CLAUDE.md`'s instruction never to broaden the task merely because excluded
archives existed elsewhere. Their listing in `excluded_archives.csv` is
itself only a hash/size/disposition record, not their content.

## 9. Gate compliance (Stage 00, `schemas/OUTPUT_GATES.md`)

- [x] `00_SCOPE_AUDIT.md` exists and is nonempty (this file).
- [x] Lists all controlling artifacts (§2) with exact hash match confirmation.
- [x] Lists exact included technical groups (§3) and exclusions (§5), matching
      `IP_SCOPE.md` verbatim.
- [x] States input-integrity issues: none found for the three controlling
      artifacts (§2); build-artifact path-leak anomaly recorded (§7) as a
      hygiene item, not an integrity failure.
- [x] States that unrelated (PhD/startup) archives were absent/excluded
      without analyzing their contents (§8).
- [x] Identifies publication source-file disclosure hazards (§6, §7).
- [x] Excluded concepts (§5) are recorded only as exclusions, not evaluated as
      manuscript IP.
- [x] No claim of legal advice, exhaustive search, or FTO opinion made
      anywhere in this document.
- [x] All statements above are facts drawn directly from the named input
      files; no inference beyond direct observation is presented as fact.

**Overall Stage 00 result: PASS.** No integrity failure. No scope violation.
Two source-hygiene anomalies recorded (§6 unrendered alternate abstract,
§7 local-path leakage in `.log`/`.synctex.gz`) for Stage 50 disposition.
