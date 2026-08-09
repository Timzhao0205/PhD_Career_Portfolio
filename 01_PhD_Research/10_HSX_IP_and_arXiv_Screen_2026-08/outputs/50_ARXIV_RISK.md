# Stage 50 — arXiv/OTL Disclosure-Risk Gate

Run: HSXIP-20260805T071311Z. Scope authority: `IP_SCOPE.md`, `CLAUDE.md`,
`schemas/OUTPUT_GATES.md` (§50 gate), `docs/ARXIV_SCRUB.md`, `docs/OTL_QUESTIONS.md`.
Inputs: `outputs/00_SCOPE_AUDIT.md` §§6-7, `outputs/30_IP_SCREEN.md` (dispositions,
§3 record-tension note), `outputs/40_UHV_PACKAGE_VERDICT.md` + `40_EVIDENCE_GAPS.md`
(C3 status, G1-G11), `outputs/20_PRIOR_ART.csv` rows S001-S003/S006-S007, and the
three controlling manuscript artifacts, independently re-inspected this session
(TeX line cites below; ZIP entries independently extracted and hashed-in-place
this session; `submission.pdf` p.9 independently re-extracted this session).

**What this document is and is not.** This is a disclosure-timing and process
risk assessment to support an arXiv/OTL decision. **It is not legal advice, not
a patentability or novelty opinion, and not an FTO opinion.** It does not tell
the researcher what the law requires of their specific facts — it identifies
which facts are known, which are unknown, and which official sources govern the
question, so the researcher can take those facts to Stanford OTL and/or IEEE.
No upload, submission, or external communication was performed by this workflow.

---

## 1. Disclosure timeline

### 1.1 Known dates (fact, from file metadata and document text, independently
re-verified this session)

| Date (local, as recorded) | Event | Evidence |
|---|---|---|
| 2026-06-11 | `figures/fig2.pdf`, `figures/fig3.pdf`, `figures/fig4.eps` created; `IEEE_lsens.cls` (stock template) copied into the working folder | ZIP entry timestamps, independently extracted and listed this session |
| 2026-06-15 | `figures/fig5.eps` created | ZIP entry timestamp |
| 2026-06-18 | `graphical_abstract.pdf` created | ZIP entry timestamp |
| 2026-06-26 | `figures/fig1.pdf` created | ZIP entry timestamp |
| 2026-07-02 14:03:50 (author's local clock, UTC-07:00) | Final edit of `regular_lsens.tex` before compilation | ZIP entry timestamp |
| 2026-07-02 14:04:10 (same clock) | Local LaTeX compile producing `regular_lsens.aux/.log/.pdf/.synctex.gz` (4-page paper-only PDF, `pdfTeX-1.40.26`, independently confirmed by `pdfinfo` this session) | ZIP entry timestamps; `pdfinfo` re-run this session |
| 2026-07-02 | `submission.pdf` created (9 pages: paper + graphical abstract + cover letter), Producer `Aspose.PDF for Java 25.6` — consistent with a journal-portal-generated bundle, not an author-authored PDF | `outputs/00_SCOPE_AUDIT.md` §2 (hash-verified); independently re-confirmed via `pdfinfo` this session |
| 2026-07-02 (same document) | Cover letter, addressed "Dear Professor Andrei Shkel" (IEEE Sensors Letters), states verbatim: *"This manuscript has not been posted on any preprint repository. It is original, is not under consideration elsewhere, and has been approved by all coauthors."* | `submission.pdf` p.9, independently re-extracted this session (`pdftotext`) |
| 2026-08-05 (today) | This Stage-50 review is run | Run timestamp |

**Fact:** as of the 2026-07-02 submission, the authors affirmatively represented
to IEEE Sensors Letters that no preprint posting (arXiv or otherwise) had
occurred. **Fact:** no artifact in this package post-dates 2026-07-02, so this
package contains no evidence of any subsequent posting, acceptance, or
publication event.

### 1.2 Unknown / not established by the supplied artifacts

- **Peer-review status today (2026-08-05).** Whether IEEE Sensors Letters has
  since accepted, requested revisions, or rejected the manuscript is not
  stated anywhere in the inputs. This matters because IEEE's own posting rules
  (§4 below) attach different obligations at "submitted," "accepted," and
  "published" stages.
- **Date of the underlying deployment.** The manuscript reports shot numbers
  (18, 19, 21, 63, 65, 68) but no calendar dates for the 68-shot campaign or
  for when the packaged module (including the shield) was first built,
  installed, or GDC-exposed.
- **Earliest disclosure of the shield/module to anyone without a
  confidentiality duty** (`IP_SCOPE.md`; Stage 40's G10) — e.g., an HSX
  operations review, a conference talk or poster, a thesis chapter, a lab
  webpage, or an internal facility report predating the manuscript. Nothing in
  the three controlling artifacts confirms or rules this out. **This is the
  single biggest open unknown for the disclosure-timing question**, because it
  could mean the shield concept is already public through a channel this
  workflow was never given access to evaluate (out of `IP_SCOPE.md`'s
  controlling-artifact boundary), or it could mean the manuscript/journal
  submission is the first disclosure of any kind.
- **Conception date and identity of who conceived the shield** (Stage 40 G2) —
  unresolved; controls both novelty-timing and inventorship.
- Whether any Stanford invention disclosure has already been filed with OTL for
  any element of this work — not stated, not assumed.

### 1.3 What is and is not "public disclosure" so far (fact, sourced;
framing, not legal advice)

- **The 2026-07-02 journal submission, by itself, is ordinarily treated as a
  confidential peer-review submission, not a public disclosure** — IEEE
  reviewers operate under confidentiality norms, and the cover letter itself
  represents that no preprint has been posted. This package makes no
  independent finding about IEEE Sensors Letters' specific reviewer-pool
  confidentiality practice; it notes the general norm and that no contrary
  evidence appears in the artifacts.
- **A prospective arXiv posting would be different in kind, not degree**: per
  arXiv's own policy (S006, https://info.arxiv.org/help/license/index.html,
  verified_full, directly fetched), arXiv "keeps a permanent record of every
  article and version posted, ... viewed and downloaded freely by anyone," and
  "the license chosen is irrevocable and cannot be changed." An arXiv post is
  immediate, permanent, and unrestricted-audience — the paradigm case of a
  public disclosure, distinct from a confidential journal-review submission.
- **Stanford OTL's own framing (S001, https://otl.stanford.edu/researchers/submit-invention-otl,
  verified_abstract — direct fetch returned HTTP 403 both in Stage 20 and again
  when re-attempted this session; verified via consistent cached quotation)**
  lists "preprints, posters, theses, and abstract publications" as forms of
  public disclosure and states OTL "will not file patent applications if the
  invention has been publicly disclosed prior to filing." Stanford "strongly
  encourages inventors to confidentially disclose ... before a public
  disclosure."

---

## 2. U.S. grace period vs. foreign absolute novelty — separated, not legal advice

This section states what the governing frameworks say in general terms, with
primary sources, so the researcher can bring the right facts to OTL/counsel.
**It does not apply these frameworks to reach a conclusion about this specific
manuscript's patentability**, and it does not resolve which countries or
which claim scope would matter.

### 2.1 United States — AIA 35 U.S.C. 102(b)(1) grace period

Directly fetched, quoted verbatim, from MPEP 2153/2153.01(a)
(https://www.uspto.gov/web/offices/pac/mpep/s2153.html, official USPTO source,
accessed 2026-08-05, verified_full):

> "a disclosure which would otherwise qualify as prior art under AIA 35 U.S.C.
> 102(a)(1) is excepted as prior art if the disclosure is made: (1) one year or
> less before the effective filing date of the claimed invention; and (2) by
> the inventor or a joint inventor or by another who obtained the subject
> matter disclosed directly or indirectly from the inventor or a joint
> inventor."

**Fact, general rule:** the U.S. gives up to one year after a first
inventor-originated public disclosure within which a U.S. application may still
be filed without that disclosure counting as prior art against it.

**A specific nuance directly relevant to this manuscript's authorship
structure (fact, same MPEP source):** the exception's availability depends on
whether the disclosure is "readily apparent" as inventor-originated by
comparing the publication's author list to the eventual application's
inventor list:

> if "the application names as joint inventors A, B, and C, and the
> publication names as authors A and B" ... "it is apparent that the
> disclosure is a grace period inventor disclosure, and the publication is not
> prior art" — but if "the application names as joint inventors A and B, and
> the publication names as authors A, B and C," it "would not be readily
> apparent from the publication that it is an inventor-originated disclosure
> and the publication would be treated as prior art" absent additional
> evidence.

**Inference, flagged as an open question, not a conclusion:** this manuscript
lists six authors (Zhao, Goodman, Gallenberger, Cox, Geiger, Senesky). If a
future U.S. filing's inventor list for the shield/module (C3) turned out to be
narrower than all six authors — which is exactly the open question in §5 below
and in Stage 40's G2/G11 — the publication's author list could be *larger*
than the inventor list, which is the scenario the MPEP flags as requiring
"additional evidence" to invoke the grace-period exception. This is a concrete
reason the authorship-vs-inventorship question (§5) is not academic: it can
affect whether even a timely U.S. filing is automatically protected by the
grace period, or whether it needs supporting declarations. **This is not a
prediction that the exception would fail here — only that the authorship
question is evidentially material and worth raising with OTL/counsel now.**

**Also relevant, general knowledge, no new source needed:** the one-year grace
period runs from the *earliest* qualifying inventor-originated public
disclosure — if an earlier disclosure exists (§1.2, unresolved), the clock may
already be running from that date, not from any later arXiv posting.

### 2.2 Foreign jurisdictions — absolute (strict) novelty

Directly relevant Stanford OTL guidance (S002,
https://otl.stanford.edu/patent, verified_abstract; direct fetch again
returned HTTP 403 this session, verified via consistent cached quotation
matching the Stage 20 ledger record):

> foreign "strict novelty" jurisdictions bar patenting if the invention was
> "known publicly or disclosed in a publication even one day before" filing,
> and "publication" is interpreted "much more broadly than in the typical
> research community."

**Fact, general rule:** many major non-U.S. jurisdictions (commonly cited
examples include the European Patent Office and much of Asia) have **no
inventor grace period** for most disclosures — a public disclosure of any kind,
by anyone, even one day before a filing, can be novelty-destroying there,
regardless of U.S. grace-period status. **This project does not enumerate
which specific countries would matter for this invention or verify any single
country's current statute; that determination is OTL/counsel's task, not
this workflow's.**

**Consequence for this manuscript (inference, calibrated):** because arXiv
posting is immediate, permanent, and globally accessible (§1.3), posting to
arXiv would start the foreign absolute-novelty clock (effectively ending
patent eligibility in strict-novelty countries as of the posting date) even in
scenarios where the U.S. grace period would still be available. **This is the
core reason the U.S. grace period does not make an arXiv posting "safe" from
an IP standpoint — it only preserves one jurisdiction's option, and only if the
authorship/inventorship and timing facts line up (§2.1).**

### 2.3 Explicit non-legal-advice statement

Nothing above is a legal conclusion about this manuscript. §§2.1-2.2 report
what USPTO's and Stanford OTL's own published materials say in general terms.
Whether, when, and where a filing would be timely — and whether any disclosure
already occurred through a channel outside this workflow's controlling
artifacts (§1.2) — are questions for Stanford OTL and/or patent counsel with
the actual, complete disclosure history.

---

## 3. IEEE preprint and copyright policy — verified this session

### 3.1 arXiv posting relative to IEEE submission status (fact, directly
fetched and quoted)

From IEEE's official Author Center post-publication policy page
(https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/post-publication-policies/,
accessed 2026-08-05, verified_full, directly fetched this session):

> "Authors who have submitted or plan to submit their articles to IEEE may
> retain their posted preprints in the following locations: arXiv.org,
> TechRxiv.org, or any not-for-profit preprint server approved by the
> Publication Services and Products Board (PSPB)" and "IEEE does not consider
> this to be a form of prior publication."

From IEEE's companion "Article Sharing and Posting Policies" document
(https://journals.ieeeauthorcenter.ieee.org/wp-content/uploads/sites/7/IEEE-Article-Sharing-and-Posting-Policies.pdf,
official IEEE document, PDF directly retrieved and text-extracted this
session, verified_full):

> "PRIOR TO SUBMISSION TO AN IEEE PUBLICATION (PREPRINT) ... Authors may share
> or post their preprints ... On the author's personal website or their
> employer's website" [and, per the "submitted/accepted" and "accepted"
> sections that follow] "... On TechRxiv or ArXiv ... Upon acceptance,
> previously posted versions must be replaced by a full citation with DOI or
> the accepted version with DOI."

**Fact, synthesized:** IEEE, as a venue-side matter, does **not** treat an
arXiv posting made before or during submission as prior publication that would
disqualify the manuscript from IEEE Sensors Letters, and explicitly permits
arXiv as an approved posting location through submission, acceptance, and
after acceptance (with a copyright-notice/DOI update obligation triggered at
acceptance). **This means the IEEE venue relationship is not, by itself, a
reason to withhold an arXiv posting** — the risk this document is concerned
with is the OTL/patent-timing risk in §§1-2, not an IEEE editorial or
copyright-clearance risk.

### 3.2 Copyright-notice mechanics if/when accepted (fact, same sources)

- Before any IEEE copyright form is signed, IEEE's own author-facing guidance
  (consistent secondary confirmation, `IEEE Sensors Letters` "Information for
  Authors" page, https://ieee-sensorsletters.org/information-for-authors/,
  fetched this session) states IEEE "owns the copyright to the technical
  contributions it publishes" upon acceptance, and authors must submit a
  completed IEEE Copyright Form.
- Per §3.1's directly-fetched primary source, **upon acceptance** any
  previously posted arXiv version must be updated to either (a) a full
  citation with DOI, or (b) the accepted version bearing an IEEE copyright
  notice and DOI.
- **Action for the researcher, not performed by this workflow:** if an arXiv
  post is made now (pre-acceptance) and the paper is later accepted, the
  arXiv record will need a follow-up update at acceptance and again at
  publication — a housekeeping obligation independent of the IP question.

### 3.3 What this section does not establish

This section verifies **IEEE's own** posting/copyright rules. It says nothing
about Stanford OTL's disclosure-timing concerns (§§1-2) or about foreign
novelty (§2.2) — an arXiv posting can be simultaneously "fine" under IEEE
policy and "risky" for OTL filing options. These are separate questions, kept
separate throughout this document per project instructions.

---

## 4. Sponsor, PI, coauthor, inter-institutional, and inventorship questions
(mapped to manuscript fact; answers not assumed)

All items below restate `docs/OTL_QUESTIONS.md` against this manuscript's
specific, independently re-verified facts. **None are answered here** — they
are the concrete list to bring to the PI and OTL.

### 4.1 Sponsors of record (fact, `regular_lsens.tex` L514, Acknowledgment,
independently re-read this session)

> "The work of the authors was supported by the U.S. Department of Energy
> under Contract No. DE-AC02-76SF00515, SLAC FWP 101264, and by the TomKat
> Center for Sustainable Energy at Stanford University. Fabrication work was
> performed at the Stanford Nanofabrication Facility, a member of the National
> Nanotechnology Coordinated Infrastructure (NNCI), supported by the National
> Science Foundation under Award ECCS-2026822."

- DOE Contract DE-AC02-76SF00515 (SLAC operating contract) and SLAC FWP 101264
  — federal funding agreement question: does Bayh-Dole reporting apply to any
  element of this work? Per Stanford OTL's own process page (S003,
  https://otl.stanford.edu/researchers/otls-process, verified_abstract):
  Stanford must report inventions to federal sponsors under Bayh-Dole "whether
  or not those inventions are considered patentable." **This reporting
  obligation is triggered by federal funding nexus, not by a screen's
  patentability conclusion — it applies to C3 regardless of Stage 30/40's
  screen-out/hold labels**, and is a question for OTL/sponsored-research
  administration, not something this workflow resolves.
- NSF Award ECCS-2026822 (SNF/NNCI) — funded the *fabrication facility* (Group
  1, C1 — screened out at Stage 30); question for OTL: does NSF facility
  funding reach downstream packaging/deployment work (C3) performed with
  facility-fabricated die, or only the fabrication step itself?
- TomKat Center for Sustainable Energy (Stanford) — non-government sponsor;
  S003 notes non-government sponsors "may also have intellectual property
  clauses" — unknown here whether TomKat's specific agreement has IP terms;
  a document this workflow does not have access to.
- **UW-Madison / HSX facility funding is not named in the manuscript's own
  Acknowledgment paragraph**, even though three of six authors (Goodman,
  Gallenberger, Geiger) are UW-Madison-affiliated and HSX is a DOE-supported
  UW-Madison facility (fact, author affiliations at `regular_lsens.tex`
  L381-388). **This is a gap worth flagging to OTL directly**: whatever DOE
  contract(s), UW-Madison institutional agreements, or facility-use terms
  govern HSX operation are not disclosed in the paper and were not supplied to
  this workflow; they may impose their own sponsor-reporting or IP terms
  independent of the Stanford-side Acknowledgment.

### 4.2 PI authorization (question, not resolved here)

Per S003: "the PI's authorization is required even if the PI is not an
inventor." **Open question:** who is the PI of record for this work's
governing award(s) (DOE contract, SLAC FWP, TomKat grant), and has that person
been asked whether they authorize (a) an OTL disclosure, and/or (b) an arXiv
posting, before either occurs? Not addressed by any artifact in this package.

### 4.3 Coauthor approval of the exact arXiv version (per
`docs/ARXIV_SCRUB.md`)

**Open question, not addressed by any artifact:** have all six authors
(Zhao, Goodman, Gallenberger, Cox, Geiger, Senesky) reviewed and approved the
*specific* file set proposed for an arXiv upload (as distinct from approving
the journal submission, which the cover letter already states they did)? The
checklist in `docs/ARXIV_SCRUB.md` requires this as a precondition independent
of the IP question.

### 4.4 Inventorship — distinct from authorship (fact-based framing, S002)

Per S002 (https://otl.stanford.edu/patent, verified_abstract): inventorship is
defined by "who conceives of an original and non-obvious idea" as reflected in
eventual claims, "not by authorship or institutional role." Applied to this
manuscript's only surviving candidate (C3, the grounded graphite shield):

- **Who conceived the shield, its geometry, grounding route, and placement,
  and when?** (`IP_SCOPE.md`; Stage 40 G2) — unresolved by any controlling
  artifact; `10_DISCLOSURE_MAP.csv` F44 confirms no per-element inventorship
  or conception statement appears anywhere in the TeX, PDF body, cover letter,
  or graphical abstract.
- **Did UW-Madison HSX personnel (Goodman, Gallenberger, Geiger) contribute
  the shield, flange, holder, or GDC-handling solution, or the experimental
  deployment method?** (Stage 40 G11) — unresolved. If yes, this both changes
  the inventor list (with the §2.1 authorship/inventorship-mismatch
  consequence for any U.S. filing) and brings UW-Madison's institutional
  IP/sponsor terms into the decision, which this workflow has no access to
  and cannot evaluate.
- **Was the shield standard HSX/GDC facility engineering, adapted from an
  existing probe, or newly developed for this module?** (Stage 40 G9) — if
  standard facility practice, this both weakens C3's novelty/obviousness
  posture (Stage 40 §2) *and* raises an inventorship/ownership question
  independent of patentability: routine facility engineering conceived by HSX
  staff before this manuscript could mean the relevant conception predates
  and sits outside this manuscript's author group entirely.

### 4.5 Inter-institutional ownership

Stanford and UW-Madison are separate institutions, each with its own
technology-transfer office and, potentially, its own sponsor obligations.
**Open question, explicitly for OTL and not resolved here:** if UW-Madison
personnel are found to be co-inventors of any C3 element (§4.4), does an
inter-institutional ownership/co-filing agreement need to be negotiated before
any filing decision, and does that change the timing pressure around an arXiv
posting (i.e., does more time need to be reserved for a two-institution
process)? Stanford OTL's own process page (S003) describes only the
single-institution disclosure process; nothing in the supplied sources
addresses UW-Madison's parallel process or an existing Stanford/UW-Madison
umbrella agreement, if one exists.

---

## 5. The C3-specific disclosure-timing question (the load-bearing analysis)

This synthesizes Stage 30 §4 and Stage 40 §1/§10 with §§1-4 above. **C3 (the
UHV/GDC module, load-bearing element = grounded graphite shield, F16) is the
only candidate carried into this stage; C1, C2, C4, C5 were screened out at
Stage 30 and are not re-opened here** (`30_IP_SCREEN.md` §7).

**The split that matters (fact, `regular_lsens.tex` L465, independently
re-read this session):** the shield's *entire* public textual disclosure is
one sentence: *"To reduce the risk of arcing and epoxy degradation during
glow discharge cleaning (GDC) and plasma operations, a grounded graphite
shield was installed over the packaged sensor module."* This concept-level
sentence is present in **both** the already-submitted journal manuscript
**and** would be present, unchanged, in any arXiv posting of the same paper.
The implementation detail that could support a distinguishing, reproducible
claim — geometry, apertures, clearances, grounding route, dimensions,
comparative/failure data (F40-F42) — **is in neither artifact**; it exists (if
it exists at all) only in inventor-held records this workflow has not seen.

**Consequence 1 — arXiv adds no *new* technical disclosure beyond the journal
submission.** Because the concept sentence is already identical in both, an
arXiv posting does not disclose any additional shield detail that a
competitor or examiner could not already learn from the manuscript once it is
public by any route (including eventual IEEE publication).

**Consequence 2 — arXiv changes *when* and *how irrevocably* that same
sentence becomes public, and this is the actual risk.** §1.3 established that
the 2026-07-02 journal submission is, on the available evidence, not yet a
public disclosure (confidential peer review; cover letter represents no prior
posting). An arXiv posting would be an immediate, permanent, globally-visible
public disclosure of the same concept-level sentence (§1.3, §2.2), starting
the U.S. grace-period clock (§2.1, with the authorship-mismatch caveat) and
foreclosing filing in strict-novelty foreign jurisdictions as of the posting
date (§2.2) — **before** the minimum evidence bundle that Stage 40 identified
as necessary to know whether C3 is even worth OTL's time has been gathered
(Stage 40 §10 / `40_EVIDENCE_GAPS.md` §4: G1 failure/comparison records, G2
conception records, G3 drawings/grounding route, at minimum).

**Consequence 3 — the same clock starts regardless of arXiv, once IEEE
publishes.** If/when IEEE Sensors Letters accepts and publishes the paper, the
same one-sentence disclosure becomes public through that channel with or
without an arXiv posting. **This means the arXiv-specific decision is about
*acceleration and irrevocability*, not about whether the concept will
eventually become public at all** — on the current evidence, some public
disclosure of the shield concept is already in motion via the journal
pipeline, and this package cannot determine its current stage (§1.2). An arXiv
post would be the *faster, more certain, and more immediately verifiable* of
the two triggers, which is exactly what makes it the more useful point at
which to insert an OTL checkpoint before the trigger fires irreversibly.

**Consequence 4 — record tension noted for completeness, not a hold basis on
its own.** Stage 30 §3 flagged that the introduction's premise that
conventional Hall platforms "cannot be deployed near the plasma edge" (L451)
sits in tension with verified in-vessel InSb/GaAs deployments (S015/S016/N016).
This is at most an accuracy nuance the authors may wish to consider before
any future revision; per Stage 30, it is never a required manuscript
modification by this workflow and is **not** part of the reasoning for the
gate decision below, which turns entirely on the C3 disclosure-timing/evidence
question.

---

## 6. Gate decision

### `HOLD_ARXIV_FOR_OTL`

**Basis (all four must be true simultaneously; all four are true on the
current record):**
1. C3 remains `conditional_hold`, not `screen_out`, at both Stage 30 and
   Stage 40 — it is still an open candidate, not a resolved non-issue.
2. The shield's concept-level disclosure (F16) is not yet confirmed public
   (§1.3) — the journal submission is presumptively confidential, and no
   earlier public disclosure is confirmed (though also not ruled out — §1.2
   G10 is the controlling unknown).
3. An arXiv posting would be an immediate, irrevocable, and (per §2.2)
   novelty-affecting public disclosure of that same concept-level content, in
   a jurisdiction-general and U.S.-authorship-sensitive way (§2.1), before the
   Stage 40 minimum evidence bundle has been gathered or an OTL/PI decision
   has been made.
4. The sponsor/PI/inter-institutional/inventorship questions in §4 are
   unresolved and independently require PI authorization and, per S003,
   Bayh-Dole-driven reporting to federal sponsors regardless of the
   patentability screen's outcome.

### Conditions that would release the hold (any one is sufficient)

- **(a) OTL completes intake and clears posting.** The PI submits the draft
  intake (`outputs/50_OTL_INTAKE.md`) to Stanford OTL (and, if UW-Madison
  inventorship is confirmed under §4.4, to UW-Madison's technology-transfer
  office), OTL reviews it, and either (i) declines to pursue a filing and
  affirmatively clears the authors to post, or (ii) files a provisional
  application, after which posting the same content is no longer
  novelty-destroying for that filing.
- **(b) An informed PI/author decision to proceed without OTL filing.**
  Nothing in this workflow or `IP_SCOPE.md` gives this package authority to
  compel an OTL filing — Stage 30/40's own calibrated expectation (absent the
  minimum evidence bundle) is that no publication-specific filing case is
  likely to survive Stage 60/70 scrutiny. If the PI, with the sponsor/
  inventorship questions in §4 and the evidence gaps in Stage 40 §10 in hand,
  makes an informed decision that OTL review is unnecessary or that the value
  is not worth the delay, that decision — documented — releases the hold. This
  package cannot make that call for the researcher.
- **(c) Confirmation the concept is already public through an earlier,
  independent channel (§1.2 G10).** If a documented earlier public disclosure
  (poster, talk, prior report) is found to already cover the shield concept at
  or beyond the manuscript's level of detail, the marginal risk of an arXiv
  posting is much reduced (though the U.S. grace-period clock would then be
  running from that earlier date, not from any future arXiv date — a fact for
  OTL/counsel to assess, not this workflow).

### Expected OTL turnaround (verified, not assumed)

Directly fetched, Stanford Office of Research primary source
(https://doresearch.stanford.edu/how-to/disclose-invention, accessed
2026-08-05, verified_full):

> "Shortly after the Invention Disclosure is submitted, an OTL licensing
> manager will contact the inventor(s) to discuss the invention and its
> commercial potential." The same page states, on disclosure timing generally:
> "To preserve patent rights, inventors should disclose inventions before
> publications ... or presentations describing the invention are publicly
> available."

**No specific number of business days for initial contact or full evaluation
is published on any Stanford OTL page this workflow could access** (direct
fetches of `otl.stanford.edu` pages returned HTTP 403 in this session and in
Stage 20; the only quantified OTL timeframe found anywhere in this research —
a 2-3 month *marketing* period after a licensing decision, from a general web
search, not independently fetched from a primary page — describes a much
later stage of OTL's process and is not carried as a verified figure here).
**Action for the researcher:** ask OTL directly, at the moment of submitting
`outputs/50_OTL_INTAKE.md`, what their current initial-response timeline is;
do not assume a number.

### Scope of the hold

This hold applies to **posting this manuscript (or any version substantively
disclosing the same C3 concept) to arXiv or any other public preprint
server**. It does not instruct the researcher on the already-completed IEEE
Sensors Letters submission (outside this workflow's control per `CLAUDE.md`)
and does not extend to C1/C2/C4/C5, which carry no hold (Stage 30 §7:
`screen_out`).

---

## 7. Gate compliance

- Disclosure timeline with knowns and the largest unknown stated: §1.
- U.S. grace period and foreign absolute novelty separated, sourced, and
  explicitly not resolved as legal advice: §2.
- Sponsor/coauthor/inventor/PI/inter-institutional questions mapped to
  specific manuscript facts, none assumed answered: §4.
- IEEE preprint/copyright guidance independently verified this session with
  primary-source quotations: §3.
- C3-specific disclosure-timing analysis connecting all of the above to the
  single surviving candidate: §5.
- Binary recommendation with explicit, falsifiable release conditions: §6.
- No upload, submission, edit to the manuscript, or external communication was
  performed. No claim of legal advice, exhaustive search, or FTO opinion
  appears anywhere in this document.

## 8. Files produced

- `outputs/50_ARXIV_RISK.md` (this file)
- `outputs/50_SOURCE_SCRUB.md`
- `outputs/50_OTL_INTAKE.md`
