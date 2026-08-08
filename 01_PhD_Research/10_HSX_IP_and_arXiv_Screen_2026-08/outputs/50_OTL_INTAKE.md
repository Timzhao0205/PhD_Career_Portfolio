# Stage 50 — Draft OTL Intake (for researcher review and submission)

Run: HSXIP-20260805T071311Z.

**This is a draft prepared for the inventors/PI to review, edit, and submit
themselves through Stanford's own Researcher Portal (and, if §7 below applies,
through UW-Madison's technology-transfer office).** Per `CLAUDE.md`, this
workflow does not send email, submit an OTL disclosure, file a patent, or
communicate externally in any form. Nothing in this document has been
transmitted to OTL, UW-Madison, or anyone else. It is scoped **only** to C3 —
the UHV/GDC module and its grounded graphite shield — the single candidate
that survived Stage 30's screen and Stage 40's deep-dive
(`outputs/30_IP_SCREEN.md` §7; `outputs/40_UHV_PACKAGE_VERDICT.md` §0). C1
(Hall device/fabrication), C2 (fusion/stellarator use), C4 (readout chain),
and C5 (deployment/validation method) were screened out and are **not**
proposed for OTL submission by this draft (Stage 30 §7); they are omitted
below except where they matter to sponsor/inventorship context.

---

## 1. Candidate summary (what to tell OTL, stated candidly)

**Working title:** Grounded graphite shield for GDC/plasma-arc protection of
an epoxy-encapsulated in-vessel Hall-effect sensor package.

**One-paragraph description (research framing, not a legal claim):** An
AlGaN/GaN Hall-effect die, wire-bonded to a ceramic leadless chip carrier,
epoxy-encapsulated (EPO-TEK 353ND) and vacuum-baked, mounted on a zirconia
holder and stainless standoff for insertion into the HSX stellarator vessel,
is covered by an electrically grounded graphite shield. The shield's stated
purpose is to reduce arcing and epoxy degradation during glow discharge
cleaning (GDC) and plasma operation. The module operated through 68
consecutive HSX shots.

**Candid statement of what is conventional (do not oversell this to OTL):**
Per `outputs/40_UHV_PACKAGE_VERDICT.md` §2, six of the module's seven
elements — the ceramic carrier, aluminum wire bonds, the epoxy, the bake
schedule (which exactly matches the vendor's standard cure recommendation),
the zirconia holder, and the standoff/flange hardware — are individually
conventional, manufacturer-directed, or industry-standard choices, none cited
or claimed as new by the authors themselves. **The entire potentially
protectable content is concentrated in one element: the grounded graphite
shield** (F16), and even that element's public disclosure is a single sentence
(`regular_lsens.tex` L465) with no drawings, dimensions, grounding-route
detail, or comparative data (F40-F42).

**Candid statement of the obviousness posture (do not undersell this either):**
Per `outputs/40_UHV_PACKAGE_VERDICT.md` §0 and §4.3, this stage's own
verification found that (a) GDC arcing was a documented hazard by 1979
(V40-A, PPPL/OSTI primary source), (b) grounded-vs-floating electrical
behavior of objects in GDC was documented by the same 1979 source, and (c)
Wendelstein 7-X grounds part of its in-vessel Mirnov coil assembly to prevent
DC charging (N017). Every link in a predictable-combination (obviousness)
argument is currently supported by a verified source, and no documented
unexpected result or teaching-away evidence has been found. **On the public
record alone, this candidate faces a high obviousness risk and thin
enablement.** OTL should be told this directly, not have it discovered later.

---

## 2. Evidence gaps — the concrete ask (from `outputs/40_EVIDENCE_GAPS.md` §4,
restated here as the literal request to bring to the PI/OTL conversation)

| # | Ask | Why it matters | Direction if answered |
|---|---|---|---|
| G1 | Any documented no-shield failure, arcing incident, or epoxy-degradation event; any with/without-shield comparison, photos, or shot logs | The only realistic path to an unexpected-result/non-obviousness argument | Strengthens if found; leaves obviousness risk high if absent |
| G2 | Conception records — lab notebooks, e-mails, CAD/drawings with dates and named originators; where conceived (Stanford vs. UW-Madison HSX staff vs. joint) | Controls inventorship and which institution's OTL leads | Either direction — see §7 |
| G3 | Shield geometry, thickness, apertures, clearances, fastening, and grounding route/resistance-to-ground | Cures the enablement gap; without it, no distinguishing claim is draftable | Strengthens if documented |
| G4 | Any design calculation tying shield conductivity/thickness to arc suppression *and* magnetic-field transmission bandwidth (the skin-depth trade-off at the readout's 1 MHz band, `40_UHV_PACKAGE_VERDICT.md` §4.4) | The single most technically credible latent delta identified in this review — an engineered, non-arbitrary parameter choice, if it exists | Strengthens if found; nothing to evaluate if absent |
| G5 | GDC exposure logs for this module: cycle count, cumulative hours, discharge current density, post-campaign inspection of shield and epoxy | Determines whether the shield's protective function was ever actually tested by real exposure, or is an untested precaution | Strengthens if exposure + intact epoxy documented; **weakens sharply** if the module was not actually GDC-exposed |
| G6 | HSX's UHV acceptance criterion and any RGA/leak/base-pressure qualification records behind the 150°C/1-hour bake | Improves the record's completeness; will not by itself rescue the bake as an independent candidate (it already matches the vendor's standard cure) | Minor either way |
| G7 | Facility documentation (any fusion lab) prescribing that in-vessel diagnostics be *floated/isolated* during GDC specifically for protection | The only lead for a teaching-away argument; tested this review against a 1979 PPPL primary source and currently **unsupported** | Would strengthen only if found; currently weakens |
| G8 | Whether Wendelstein 7-X's graphite wall-protection panels themselves (not just the Mirnov coil center tap, which is confirmed grounded) are electrically grounded — the 2013 companion paper (ScienceDirect PII S0920379613005279) is paywalled and unresolved | The single cheapest external fact that could still flip the novelty picture toward screen-out if the panels are grounded | Weakens toward screen-out if confirmed |
| G9 | Whether the shield was standard HSX/GDC facility engineering, adapted from an existing probe, or newly developed for this module | Directly answers the routine-practice question the publication cannot answer alone | Weakens to screen-out if pre-existing facility practice |
| G10 | Earliest disclosure of the shield/module to anyone without a confidentiality duty (talks, posters, HSX ops reviews, theses, facility reports) predating the 2026-07-02 submission | Controls the disclosure-timing analysis in `outputs/50_ARXIV_RISK.md` §1 — the single biggest open unknown in this entire review | Either direction |
| G11 | A statement from Goodman/Gallenberger/Geiger (UW-Madison) on their contribution to the package/shield/deployment | Controls inventorship and which sponsor terms (DOE/UW facility vs. Stanford/DOE/SLAC/NSF) apply | Either direction |

**Flip thresholds, stated candidly (from `outputs/40_EVIDENCE_GAPS.md` §2):**
G1 + G2 + G3 together would be the minimum needed to present C3 to OTL as a
substantive (still narrow) candidate rather than a screen-out. Any one of
G5 (no real GDC exposure), G8 (W7-X panels confirmed grounded), or G9
(pre-existing facility practice) would independently move the recommendation
toward screen-out. If none of G1-G11 can be answered, the current posture
(conditional hold, high obviousness risk, thin enablement) stands, and per
`outputs/40_UHV_PACKAGE_VERDICT.md` §0 the calibrated expectation is that no
publication-specific filing case would survive further scrutiny.

---

## 3. Sponsor questions (for the intake form's funding-source fields)

Restated from `outputs/50_ARXIV_RISK.md` §4.1 — answer these on the OTL
disclosure form as accurately as possible; do not guess:

- DOE Contract DE-AC02-76SF00515 and SLAC FWP 101264 (Acknowledgment,
  `regular_lsens.tex` L514) — confirm whether these specifically funded the
  packaging/shield work (C3) or only fabrication/other aspects (C1).
- NSF Award ECCS-2026822 (SNF/NNCI) — funded the fabrication facility; confirm
  whether its terms reach the downstream packaging work.
- TomKat Center for Sustainable Energy (Stanford) — confirm whether this
  award carries its own IP clause (S003 notes non-government sponsors "may
  also have intellectual property clauses"; this workflow has not seen the
  actual award terms).
- **UW-Madison / HSX facility funding is not named in the manuscript's
  Acknowledgment**, despite three UW-Madison-affiliated authors and HSX being
  a DOE-supported UW-Madison facility. Identify and disclose whatever DOE
  contract(s) or UW-Madison institutional terms govern HSX operation and
  whether they impose independent reporting obligations.
- Per Stanford OTL's own process page (S003,
  https://otl.stanford.edu/researchers/otls-process): Bayh-Dole reporting to
  federal sponsors applies "whether or not those inventions are considered
  patentable" — **this means the disclosure/reporting question is separate
  from, and does not wait on, the patentability screen above.** Disclose
  regardless of how thin the technical candidate looks.

---

## 4. PI authorization

Per S003: "the PI's authorization is required even if the PI is not an
inventor." Identify the PI of record for the governing award(s) and confirm
they have reviewed this candidate summary and evidence-gap list before
submission to OTL. Not confirmed by any artifact available to this workflow.

---

## 5. Coauthor list (fact, for the intake form's author/potential-inventor
fields — authorship is not inventorship, see §6)

Yiming Zhao (Stanford EE, corresponding), Wayne Goodman (UW-Madison NEEP,
Senior IEEE Member), Thomas Gallenberger (UW-Madison NEEP), Jasmine M. Cox
(Stanford EE), Benedikt Geiger (UW-Madison NEEP), Debbie G. Senesky (Stanford
EE and Aero/Astro, corresponding author, Senior IEEE Member).
(`regular_lsens.tex` L381-388.)

---

## 6. Inventorship questions (do not assume the author list is the inventor
list)

Per Stanford OTL's own guidance (S002, https://otl.stanford.edu/patent):
inventorship follows "who conceives of an original and non-obvious idea," not
authorship or institutional role. For C3 specifically:

- Who conceived the grounded graphite shield, its geometry, grounding route,
  and placement, and when? (= G2 above)
- Did any UW-Madison HSX personnel contribute this element, the holder,
  flange, or GDC-handling approach? (= G11 above)
- Was the shield adapted from an existing HSX probe or facility practice, in
  which case conception may sit with facility engineering staff not listed as
  paper authors at all? (= G9 above)
- **A specific downstream consequence worth flagging to OTL directly**
  (`outputs/50_ARXIV_RISK.md` §2.1): if the eventual inventor list for any C3
  filing is narrower than this manuscript's six-author list, USPTO's own
  grace-period guidance (MPEP 2153.01(a)) treats a publication with *more*
  authors than the application's inventors as not "readily apparent" as an
  inventor-originated disclosure — potentially requiring additional evidence
  to invoke the one-year grace-period exception for a U.S. filing. This is a
  reason to resolve inventorship before relying on the grace period, not a
  prediction that the exception would fail.

---

## 7. Inter-institutional question

If UW-Madison personnel are confirmed as co-inventors of any C3 element,
identify whether a Stanford/UW-Madison inter-institutional ownership or
co-filing process already exists (e.g., an umbrella research agreement) or
would need to be initiated, and how much additional time that adds relative
to the disclosure-timing pressure in `outputs/50_ARXIV_RISK.md` §5. This
workflow found no Stanford/UW-Madison umbrella IP agreement referenced in any
supplied artifact and did not search for one (out of scope; a question for
Stanford OTL and UW-Madison's technology-transfer office directly).

---

## 8. Journal/disclosure-timing context to include on the form

Summarize for OTL (full analysis in `outputs/50_ARXIV_RISK.md` §§1-2, not
repeated here in full):

- Manuscript submitted to IEEE Sensors Letters on/around 2026-07-02 (Aspose
  PDF portal-bundle creation date); cover letter represents "has not been
  posted on any preprint repository" as of that date.
- Current peer-review status (submitted / revising / accepted / published) as
  of today (2026-08-05) is **not known to this workflow** — the PI/authors
  should state it on the form.
- No arXiv posting has occurred (per the same cover-letter representation and
  the absence of any later artifact in this package).
- Earliest disclosure of the shield/module to anyone without a
  confidentiality duty is unresolved (G10) — state whatever is actually known
  (talks, posters, HSX ops reviews) on the form; do not leave it blank if
  something is known.

---

## 9. What this draft is not

- It is not a filed disclosure. It is not legal advice. It does not conclude
  that C3 is patentable, novel, or non-obvious — Stage 30/40's own calibrated
  finding is the opposite on the public record alone (high obviousness risk,
  thin enablement), and this draft says so plainly in §1 so OTL is not
  presented an inflated case.
- It does not resolve any of the sponsor, PI, inventorship, or
  inter-institutional questions above — those are exactly what the OTL
  conversation is for.
- It does not replace Stanford's own Invention and Technology Disclosure Form
  (S003) — the PI/inventors should transfer the relevant facts above into that
  form themselves via the OTL Researcher Portal, adding whatever inventor-held
  evidence (G1-G11) they can supply.

## 10. Files produced

- `outputs/50_OTL_INTAKE.md` (this file)
- `outputs/50_ARXIV_RISK.md`
- `outputs/50_SOURCE_SCRUB.md`
