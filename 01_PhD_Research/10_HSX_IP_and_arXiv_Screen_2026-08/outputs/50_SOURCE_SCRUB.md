# Stage 50 — arXiv Source Scrub

Run: HSXIP-20260805T071311Z. Applies `docs/ARXIV_SCRUB.md` item by item to the
exact material in `inputs/manuscript/submission.pdf`, `inputs/manuscript/source_original.zip`,
and `inputs/manuscript/source/regular_lsens/regular_lsens.tex`. Builds on
`outputs/00_SCOPE_AUDIT.md` §§6-7 and independently re-verifies every finding
this session (ZIP re-extracted, `.log`/`.synctex.gz` re-inspected, `.tex`
re-read, `pdfinfo`/`pdftotext` re-run on `submission.pdf` and the ZIP's figure
PDFs). **This is a checklist and findings record, not an upload. This workflow
performed no upload, edit, recompile-for-submission, or external transmission
of any of this material.**

---

## 1. Exact material exposed by each artifact (fact)

| Artifact | What it is | What it exposes beyond the peer-reviewed paper text |
|---|---|---|
| `inputs/manuscript/submission.pdf` | 9-page journal-portal bundle: paper (pp.1-7 approx.), graphical abstract (p.8), cover letter (p.9) | The cover letter (p.9) and, to a lesser degree, the graphical abstract — **neither belongs in an arXiv upload** (§3) |
| `inputs/manuscript/source_original.zip` | 17-entry original LaTeX source archive (2 dirs + 15 files) | TeX source with inert comments; local compile-machine file paths inside `.log`/`.synctex.gz`; a redundant 4-page build PDF (`regular_lsens.pdf`) distinct from `submission.pdf` | 
| `regular_lsens.tex` | The paper's LaTeX source | One unrendered alternate abstract in a comment block; unused template placeholder metadata; a stale copyright-year placeholder |

## 2. IP and content (per `docs/ARXIV_SCRUB.md` §"IP and content")

### 2.1 "Confirm every potentially protectable element has been disclosed to
OTL or deliberately released with informed authorization."

**Not satisfied on the current record.** Per `outputs/50_ARXIV_RISK.md` §6,
C3 (the grounded graphite shield) is `conditional_hold`, not resolved with
OTL, and no OTL disclosure is confirmed to exist. This item is the reason for
the `HOLD_ARXIV_FOR_OTL` gate label and is not something a source-file edit
can fix — it is a process precondition, not a redaction task.

### 2.2 "Remove unsupported future inventions and confidential facility
details."

- **Future work (F36/F37, `regular_lsens.tex` L506):** absolute calibration,
  extended-duration deployment, radiation/neutron characterization, and
  lower-noise readout are stated as future work in one sentence each, in the
  rendered Conclusion. Per `IP_SCOPE.md`, these are not disclosed inventions
  and this workflow does not treat them as content to scrub — they are already
  the authors' own public framing of what is *not* done, not a specification
  of an unpublished invention. No action identified.
  Cited in
  the manuscript, not disclosed as a package detail — nothing to remove.
- **Confidential facility details:** no facility security, access-control, or
  non-technical operational detail (e.g., internal HSX scheduling, unpublished
  safety procedures) was found in the rendered text or TeX comments during
  this session's re-read. The only facility-specific technical content is the
  UHV/GDC packaging already addressed as C3's disclosure question in
  `50_ARXIV_RISK.md`, not a separate confidentiality issue.

### 2.3 "Verify figures contain no hidden layers, notes, internal labels, or
metadata."

Independently re-checked this session with `pdfinfo` on the ZIP's figure PDFs
and graphical abstract:

| File | Creator/Producer | Finding |
|---|---|---|
| `figures/fig1.pdf`, `fig2.pdf` | Inkscape 1.4.2 / cairo 1.16.0 | Standard vector-graphics export metadata only; no author/title/keyword fields populated |
| `figures/fig4.pdf` | Apache FOP 2.4.0-SNAPSHOT (PDFDocumentGraphics2D) | Standard converter metadata; likely an intermediate conversion artifact (see §2.5 on the `.eps`/`-eps-converted-to.pdf` pairs) |
| `graphical_abstract.pdf` | Inkscape 1.4.2 / cairo 1.16.0 | Same as fig1/fig2 |

No hidden layers, embedded notes, internal lab labels, or author-identifying
metadata were found in the fields inspected. **Not inspected:** vector-layer
content inside the PDF drawing streams (e.g., a hidden Inkscape layer toggled
off in the visible render) — a full hidden-layer audit would require opening
each figure in a vector editor and enumerating layers, which was not performed
this session (declared limitation, not a finding of absence).

### 2.4 "Review TeX comments for unpublished ideas, collaborator notes,
credentials, editable links, internal paths, and deleted text."

Full re-read of all `%`-comment content in `regular_lsens.tex` this session,
consistent with and re-confirming `outputs/00_SCOPE_AUDIT.md` §6:

- **Unrendered alternate abstract, L420-423 (source-hygiene item, independently
  re-read this session).** A commented-out ~180-word abstract sits directly
  above the ~150-word abstract actually used (L425-429, "150 words version").
  The alternate wording is more verbose (e.g., spells out "voltage-biased at
  0.4 V" and "differential amplifier chain" explicitly) but discloses no
  technical group, parameter, or result beyond the rendered paper body. It is
  flagged only because **it would ship inside an arXiv source tarball and
  would be visible to anyone who downloads the source**, even though it never
  appears in the rendered PDF — deleted/superseded text of exactly the kind
  `docs/ARXIV_SCRUB.md` asks to review. **No independent IP content — a
  presentation/hygiene item, not a disclosure hazard.**
- **Unused hyperref template metadata, L303-306.** An inert
  `\hypersetup{pdftitle={Bare Demo of IEEE\_lsens.cls for IEEE Sensors
  Letters}, pdfauthor={Michael D. Shell}, ...}` block, carried over from the
  public Michael Shell demo template. `hyperref` is never loaded (its
  `\usepackage` line at L284/286 stays commented out), so this block has zero
  effect on the compiled output — confirmed again this session: `pdfinfo` on
  `submission.pdf` shows blank Title/Author XMP fields. **Cosmetic; no
  disclosure risk; leaving it in the arXiv source would only be an
  authorship-attribution embarrassment (wrong name/title in dead code), not an
  IP or credential leak.**
- **Stale copyright-year placeholder, L438.** `\IEEEpubid{1949-307X
  \copyright\ 2023 IEEE...}` — boilerplate publisher-ID template text (year
  2023), not a factual claim by the authors. Cosmetic only.
- No `TODO`/`FIXME`/`XXX`/`\iffalse`/`\begin{comment}`, no "confidential" or
  "do not submit" markers, no named individuals/credentials/editable links
  beyond the published Acknowledgment and author-block content, re-confirmed
  by regex sweep this session (case-insensitive, zero additional matches
  beyond what Stage 00 already found).

### 2.5 "Include only files needed to compile the preprint. Do not upload the
journal submission bundle, cover letter, review correspondence, logs, `.aux`,
`.synctex.gz`, unrelated graphics, backups, or Git history."

Independently re-extracted `source_original.zip` this session (17 entries: 2
directories + 15 files) and classified each:

| Entry | Needed to compile the paper? | Action if an arXiv upload is ever prepared |
|---|---|---|
| `regular_lsens.tex` | Yes | Include |
| `IEEE_lsens.cls` | Yes (unmodified stock class file, confirmed byte-identical header to the public Michael Shell IEEEtran-derived template) | Include (or rely on arXiv's own copy if it stocks this class — verify at upload time, not assumed here) |
| `figures/fig1.pdf`, `fig2.pdf`, `fig3.pdf` | Yes | Include |
| `figures/fig4.eps`, `figures/fig4.pdf`, `figures/fig4-eps-converted-to.pdf` | Only **one** of these three is actually needed — see note below | Resolve duplication before upload (not resolved by this workflow) |
| `figures/fig5.eps`, `figures/fig5-eps-converted-to.pdf` | Only **one** of these two is needed | Resolve duplication before upload |
| `graphical_abstract.pdf` | Not part of the compiled paper body (used only in the journal portal's separate graphical-abstract slot); not referenced by `\includegraphics` in the paper's compiled sections read this session | **Exclude** unless the author deliberately wants it as a supplementary arXiv figure — a decision, not a default |
| `regular_lsens.aux` | No (build byproduct) | **Exclude** — matches `docs/ARXIV_SCRUB.md`'s explicit `.aux` prohibition |
| `regular_lsens.log` | No (build byproduct); **also contains the local-path leak, §2.6** | **Exclude** |
| `regular_lsens.synctex.gz` | No (editor-sync byproduct); **also contains the local-path leak, §2.6** | **Exclude** |
| `regular_lsens.pdf` | No — this is the ZIP's own **locally-compiled 4-page output PDF** (`pdfTeX-1.40.26`, independently confirmed by `pdfinfo` this session, distinct from the 9-page `submission.pdf` journal bundle). It is exactly the kind of "resulting output file" `docs/ARXIV_SCRUB.md` and arXiv's own rules (S007) prohibit including | **Exclude** |

**Note on the `.eps`/`.pdf` figure duplication (fact + compile-hygiene
inference):** `regular_lsens.tex` L490 and L499 `\includegraphics` the `.eps`
files directly (`fig4.eps`, `fig5.eps`), which implies a DVI/PS-based
toolchain or an `epstopdf`-mediated pdfLaTeX build; the matching
`*-eps-converted-to.pdf` files are auto-generated intermediates from that
conversion, confirmed present as separate ZIP entries with later timestamps
than their source `.eps` files. **This is a compilation-hygiene issue, not an
IP issue**: `docs/ARXIV_SCRUB.md` directs "compile in a clean directory" before
any upload specifically to catch problems like this — arXiv's own build
environment may not have `epstopdf`'s shell-escape enabled, which is a common
cause of silent arXiv compile failures when both an `.eps` and its
auto-converted `.pdf` are present inconsistently. **Not resolved here; flagged
as a pre-upload technical check, independent of the OTL question.**

**Submission bundle, cover letter, review correspondence:** `submission.pdf`
itself (the 9-page bundle including the cover letter, p.9) is **not** a
compile-source file and must never be part of an arXiv source or PDF upload.
The cover letter in particular (§3.2 of `outputs/50_ARXIV_RISK.md`; F49-F51 in
`outputs/10_DISCLOSURE_MAP.csv`) contains an unsupported comparative
sensitivity claim ("substantially higher sensitivity" vs. ITER/DEMO metal Hall
probes, F51, no supporting data anywhere in the three controlling artifacts)
and "first"-type novelty assertions (F49/F50) that do not appear in the
peer-reviewed body — **these must never reach arXiv in any form**, both
because they are outside the compiled paper and because, as unsupported
claims, they would raise their own credibility exposure if posted.

### 2.6 Local-path / privacy leak in build artifacts (fact, independently
re-verified this session)

Directly re-extracted and searched `regular_lsens.log` and
`regular_lsens.synctex.gz` from the freshly-extracted ZIP this session:

- `regular_lsens.log` contains, verbatim, `d:/timzhao/Downloads/regular_lsens/regular_lsens.tex`
  and sibling references to the local `d:/texlive/2024/...` TeX Live
  installation path (2+ occurrences, independently grepped this session).
- `regular_lsens.synctex.gz` (gzip-compressed binary), independently
  decompressed and text-scanned this session, contains the same local path
  repeated across multiple `Input:` records:
  `d:/timzhao/Downloads/regular_lsens/regular_lsens.tex`,
  `.../IEEE_lsens.cls`, `.../regular_lsens.aux`.

**Assessment (unchanged from Stage 00, independently reconfirmed): this is a
privacy/source-hygiene hazard — it discloses the compiling author's local
Windows folder structure and machine layout — not a technical/IP disclosure
hazard.** No additional device, package, readout, or result information is
present beyond what `submission.pdf` already shows. Both files are already
excluded from any hypothetical arXiv upload under §2.5's `.log`/`.synctex.gz`
prohibition, which independently resolves this leak as a side effect of normal
arXiv-compliant file selection — no separate redaction step is needed *if*
the exclusion in §2.5 is followed.

---

## 3. Rights and submission hygiene (per `docs/ARXIV_SCRUB.md` §"Rights and
submission hygiene")

### 3.1 "Confirm all coauthors approve the exact arXiv version."

**Not addressed by any artifact — open item, see `outputs/50_ARXIV_RISK.md`
§4.3.** The cover letter confirms all six coauthors approved the *journal*
submission ("has been approved by all coauthors," `submission.pdf` p.9); no
artifact shows coauthor approval of a *specific arXiv file set*, which is a
different, not-yet-taken step.

### 3.2 "Check IEEE's current preprint and copyright-notice requirements for
the paper's current submission/acceptance status."

Done this session — full findings in `outputs/50_ARXIV_RISK.md` §3. Summary:
IEEE's own policy (directly fetched, verified_full) permits arXiv posting
before, during, and after submission/acceptance without treating it as prior
publication, but requires the posted version to be updated to a DOI citation
or copyright-noticed accepted version once the paper is accepted. **This is an
IEEE-side clearance question, separate from the OTL/patent-timing question
that drives the gate label in `50_ARXIV_RISK.md` §6.**

### 3.3 "Select an arXiv license deliberately; it is irrevocable for that
version."

Not selected by this workflow (no upload performed). Per arXiv's own policy
(S006, https://info.arxiv.org/help/license/index.html, verified_full,
directly fetched in Stage 20 and consistent with this session's independent
review of the same page's summary in the ledger): "The license chosen is
irrevocable and cannot be changed." **Flag for the researcher:** this
irrevocability compounds the disclosure-timing risk in `50_ARXIV_RISK.md` §5 —
not only is the disclosure itself permanent, but the specific rights grant to
arXiv/the public is also permanent once selected, independent of what happens
with OTL or IEEE afterward. License choice should be made deliberately at
upload time, not defaulted.

### 3.4 "Ensure figure and class-file rights permit redistribution."

- `IEEE_lsens.cls`: confirmed unmodified stock class file (Stage 00, re-
  confirmed this session by header comparison) — a publicly distributed
  LaTeX class intended for author use in exactly this way; no redistribution
  concern identified.
- Figures (`fig1`-`fig5`, graphical abstract): all appear to be
  author-generated (Inkscape/cairo-produced vector graphics, fig4 via Apache
  FOP conversion) rather than third-party imagery — no external copyright
  attribution or license text was found in the TeX captions or figure
  metadata suggesting non-author-owned content. **Not independently verified
  against original data/instrument-screenshot provenance** (e.g., whether any
  panel is a screenshot of a third-party instrument's proprietary UI) — a
  declared limitation, not a finding of a problem.

### 3.5 "Use arXiv-compatible filenames and exact case matches."

Not evaluated in depth (no upload staging performed). Current filenames
(`regular_lsens.tex`, `IEEE_lsens.cls`, `fig1.pdf` etc.) contain no spaces or
unusual characters and appear arXiv-compatible on inspection; a full check
requires assembling the actual candidate upload set first, which this
workflow does not do.

### 3.6 "Compile in a clean directory, inspect the generated PDF page by page,
and scan the upload archive again before the final submit action."

**Not performed — explicitly out of scope for this workflow** (`CLAUDE.md`:
"Do not ... upload to arXiv, modify the manuscript"). Flagged here only as the
action item the researcher must still perform themselves, including resolving
the `.eps`/`.pdf` duplication noted in §2.5 before any compile attempt.

---

## 4. Journal/copyright/license cross-check summary

| Question | Finding | Source |
|---|---|---|
| Does an arXiv post conflict with the IEEE Sensors Letters submission? | No — IEEE explicitly permits arXiv posting before/during/after submission and does not treat it as prior publication | `50_ARXIV_RISK.md` §3.1, directly fetched IEEE Author Center policy, verified_full |
| What must happen to the arXiv copy if the paper is accepted? | Replace with full DOI citation or an accepted version bearing an IEEE copyright notice and DOI | Same source |
| Is the arXiv license choice reversible? | No — irrevocable per version | S006, verified_full |
| Does the manuscript's own IEEE copyright placeholder (`\IEEEpubid`, L438) affect anything? | No — dead template boilerplate (year 2023), not a live copyright claim; cosmetic only | §2.4 |
| Is there an independent OTL/patent-timing reason to hold, separate from IEEE/arXiv mechanics? | Yes — see `outputs/50_ARXIV_RISK.md` §§5-6 | Cross-reference |

---

## 5. Overall source-scrub verdict

**The ZIP is not upload-ready as-is**, independent of the OTL question:

1. Four build/output byproducts must be stripped: `regular_lsens.aux`,
   `regular_lsens.log`, `regular_lsens.synctex.gz`, `regular_lsens.pdf` —
   the last of these is a full alternate compiled PDF that has no place in a
   source upload.
2. The `.log`/`.synctex.gz` local-path leak is resolved automatically by
   item 1's exclusion; no separate redaction step is needed if the ZIP is
   rebuilt from only the compile-necessary files.
3. `graphical_abstract.pdf` should be a deliberate inclusion/exclusion
   decision, not a default carry-over from the journal bundle.
4. The `.eps`/`-eps-converted-to.pdf` figure duplication should be resolved
   by a clean recompile before upload (technical, not IP-related).
5. `submission.pdf` (with its cover letter, F49-F51 unsupported claims) must
   never be uploaded in whole or in part — only the paper content compiled
   from the scrubbed `.tex`/`.cls`/figure set belongs on arXiv.
6. Coauthor approval of the specific arXiv file set, and the OTL/PI
   authorization question in `outputs/50_ARXIV_RISK.md` §§4, 6, remain
   open and are the controlling reasons for the `HOLD_ARXIV_FOR_OTL` gate —
   items 1-4 above are necessary housekeeping regardless of that gate's
   outcome, but they do not by themselves resolve it.

No upload, edit, or recompilation was performed by this workflow. This
document is a checklist and findings record only.
