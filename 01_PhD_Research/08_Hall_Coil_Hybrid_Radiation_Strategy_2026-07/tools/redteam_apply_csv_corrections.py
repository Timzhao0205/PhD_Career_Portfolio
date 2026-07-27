"""Stage 70 red-team: apply audited corrections to ledger, evidence map,
and new-source audit. Every change is printed as BEFORE -> AFTER and saved
to tools/redteam_corrections_applied.txt. Deterministic; no web access.

Corrections implemented (see outputs/07_RED_TEAM_FINDINGS.md):
  L1  H003 access upgrade (OA full text read at stage 70) + section-5 notes
  L2  H006 access upgrade (public mirror full text) + confirmed disclosures + patents
  L3  H011 upgrade from context-only to counterevidence (in-situ recal under irradiation)
  L4  P003 claims_supported corrected (abstract = high-field characterization only)
  L5  add H067 (Entler 2021 OVSS calibration), H068 (Kocan 2017 OVSS final design),
      P077 (England 2011 KSTAR field-error, Hall arrays + coils + e-beam)
  E1..E9  evidence-map rewrites: C02 C05 C06 C11 C12 C21 C27 C32 C36
  A1  new-source audit rows for H067/H068/P077
"""
import csv, io, sys

sys.stdout.reconfigure(encoding="utf-8")
LOG = io.StringIO()
def log(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LOG.write(s + "\n")

def read(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        r = csv.reader(f)
        rows = list(r)
    return rows[0], rows[1:]

def write(path, header, rows):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)

def as_dicts(header, rows):
    return [dict(zip(header, r)) for r in rows]

# ---------------- ledger ----------------
LP = "outputs/01_SOURCE_LEDGER.csv"
lh, lr = read(LP)
idx = {r[0]: i for i, r in enumerate(lr)}
col = {c: i for i, c in enumerate(lh)}

def setf(sid, field, newval, tag):
    i, j = idx[sid], col[field]
    old = lr[i][j]
    lr[i][j] = newval
    log(f"[{tag}] {sid}.{field}\n  BEFORE: {old[:220]}\n  AFTER : {newval[:220]}\n")

# L1 H003
setf("H003", "access_level", "full_text", "L1")
setf("H003", "verification_basis",
     lr[idx["H003"]][col["verification_basis"]].rstrip(".") +
     ". Stage 70: IOP open-access full text (PDF) retrieved and read end-to-end during the red-team audit.",
     "L1")
setf("H003", "notes",
     lr[idx["H003"]][col["notes"]].rstrip(".") +
     ". Stage-70 full-text findings: section 5 explicitly proposes BOTH active recalibration (RHP-style microsolenoid) AND passive in-situ recalibration of Hall sensitivity against the coil ('by exploiting standard dry runs of the machine, dedicated dry runs and plasma pulses and the plasma ramp-up phase'); the paper itself cites the 2005 JET collar probe as earlier combined-probe prior art and 2009/2010 patents (refs 66-67, formats matching GB2427700/FR2887991) on combined sensors for in-situ Hall calibration.",
     "L1")

# L2 H006
setf("H006", "access_level", "full_text", "L2")
setf("H006", "claims_supported",
     "FULL-TEXT CONFIRMED (stage 70): discloses an integrated magnetic transducer combining Hall sensor + copper microsolenoid actuator in one 10x10x6 mm package; AC excitation of the winding with DC Hall bias; synchronous (lock-in-equivalent) detection with frequency separation of differential/integral signal components; ~5 mT test field at 10 mA; correction error <=0.1%; winding dual-used as thermoresistor (0.1 C); argues the test field is radiation-dose-invariant if the winding current is held stable; deployed at Tore Supra and JET (ex-vessel).",
     "L2")
setf("H006", "verification_basis",
     lr[idx["H006"]][col["verification_basis"]].rstrip(".") +
     ". Stage 70: full text obtained and read via the public CTU golem mirror (golem.fjfi.cvut.cz/wiki/Library/others/BolshakovaI_Hall_Sensors_07.pdf) - the PDF extracted cleanly this session; all quoted disclosures verified verbatim.",
     "L2")
setf("H006", "notes",
     lr[idx["H006"]][col["notes"]].rstrip(".") +
     ". Stage 70: peer_review_uncertain RETAINED (venue-quality concern is about the journal, not the content, and is unchanged by full-text access). Companion patents GB2427700 (2009) and FR2887991 (2010) on combined sensors for in-situ Hall calibration are cited in H003 refs 66-67 (patents are discovery-level prior art, not peer-reviewed rows).",
     "L2")

# L3 H011
setf("H011", "access_level", "abstract_metadata", "L3")
setf("H011", "claims_supported",
     "Stage-70 verified (IOP abstract + partial body via article page): periodic in-situ calibration via copper-wire microsolenoid test field used for continuous sensitivity monitoring; performed DURING fission-reactor irradiation campaigns (IBR-2, LVR-15, WWR-m) to fluence >1e18 n/cm2; JET deployment showed Hall voltages within +/-0.1% of initial values over ~5 years / ~8000 pulses; JET Hall measurements cross-compared against model calculations driven by the machine pick-up-coil diagnostics.",
     "L3")
setf("H011", "verification_basis",
     lr[idx["H011"]][col["verification_basis"]].rstrip(".") +
     ". Stage 70: IOP article page fetched; abstract verbatim and body excerpts read (body quotes via page summarizer - flagged); DOI/authors re-confirmed via Crossref this session.",
     "L3")
setf("H011", "notes",
     "Same author network as H003/H006/H007. Stage-70 role change: upgraded from lineage/context-only to LOAD-BEARING COUNTEREVIDENCE for any loose 'in-situ radiation-aware Hall recalibration is unreported' claim - it demonstrates the ACTUATOR-based (known-current copper winding) variant under neutron irradiation; the open gap is specifically the PASSIVE witness-sensor variant (see corrected C21/C36). DUPLICATE of folder 06 ledger row S0111.",
     "L3")

# L4 P003
setf("P003", "access_level", "abstract_metadata", "L4")
setf("P003", "claims_supported",
     "Stage-70 corrected (abstract retrieved and read this session): high-field (+/-7 T) characterization of bismuth Hall sensors developed for the ITER steady-state magnetic diagnostic; response nonlinear particularly within +/-1 T; significant planar-Hall-effect cross-field sensitivity identified; mitigation demonstrated by sensor geometry/alignment optimization and current-spinning. The former claim on this row (OVSS system-level Hall+coil pairing used to correct coil drift) is NOT in the abstract and is re-anchored to H067/H068 (see 07_CORRECTION_LOG.md).",
     "L4")
setf("P003", "verification_basis",
     lr[idx["P003"]][col["verification_basis"]].rstrip(".") +
     ". Stage 70: Semantic Scholar abstract retrieved and read; content claim corrected accordingly.",
     "L4")
setf("P003", "notes",
     lr[idx["P003"]][col["notes"]].rstrip(".") +
     ". Stage-70 note: the planar-Hall cross-field sensitivity finding newly supports the cross-axis uncertainty discipline (stage-20 section 2.4, stage-30 section 6.3).",
     "L4")

# L5 new rows - copy conventions from existing rows
h003 = as_dicts(lh, [lr[idx["H003"]]])[0]
p013 = as_dicts(lh, [lr[idx["P013"]]])[0]
log("[L5] conventions: H003 source_type=%s topic_tags=%s | P013 topic_tags=%s\n"
    % (h003["source_type"], h003["topic_tags"][:80], p013["topic_tags"][:80]))

def new_row(d):
    return [d.get(c, "") for c in lh]

rows_new = [
    dict(source_id="H067",
         citation="Entler, Duran, Kocan, Vayakis, Sladek & Grover, Fusion Eng. Des. 168 (2021) 112398",
         title="Calibration of the ITER outer vessel steady-state magnetic sensors",
         authors="Slavomir Entler; Ivan Duran; Martin Kocan; George Vayakis; Petr Sladek; Vlastimil Grover",
         year="2021", venue="Fusion Engineering and Design, vol. 168, 112398",
         doi="10.1016/j.fusengdes.2021.112398",
         url="https://doi.org/10.1016/j.fusengdes.2021.112398",
         source_type=h003["source_type"], peer_review_status="verified_peer_reviewed",
         quality_tier="A", topic_tags=h003["topic_tags"],
         claims_supported="Abstract-verified: 60 OVSS units (bismuth Hall pairs + onboard thermocouple) on the ITER vacuum vessel outer shell; pre-installation calibration chain designed to meet 4 mT (2-sigma) accuracy over 0-2.5 T. Body-level (search-index snippet, flagged, consistent across two independent queries): plan to readjust slowly-reducing OVSS sensitivity over the ITER lifetime by CROSS-CALIBRATING OVSS AGAINST THE OUTER-VESSEL INDUCTIVE COILS during plasma current ramp-up/ramp-down - published coil-to-Hall reverse-direction plan in a tokamak.",
         verification_basis="Stage 70: DOI/title/authors/venue/volume verified via live Crossref; abstract independently retrieved via Semantic Scholar and read; the cross-calibration sentence is body text seen only in search-index snippets (publisher page HTTP 403) - NOT full-text-read, flagged everywhere it is used.",
         access_level="abstract_metadata",
         notes="Added at stage 70 (red team) to carry the OVSS-pairing/reverse-calibration evidence formerly mis-anchored on P003. Same normalized DOI as folder-06 row S0148 (counts as overlap, not new, in the folder-06 delta)."),
    dict(source_id="H068",
         citation="Kocan, Duran, Entler, Vayakis, Carmona, Gitton et al., Fusion Eng. Des. 123 (2017) 936-939",
         title="Final design of the ITER outer vessel steady-state magnetic sensors",
         authors="Martin Kocan; Ivan Duran; Slavomir Entler; George Vayakis; et al.",
         year="2017", venue="Fusion Engineering and Design, vol. 123, pp. 936-939",
         doi="10.1016/j.fusengdes.2017.03.043",
         url="https://doi.org/10.1016/j.fusengdes.2017.03.043",
         source_type=h003["source_type"], peer_review_status="verified_peer_reviewed",
         quality_tier="A", topic_tags=h003["topic_tags"],
         claims_supported="Abstract-verified: OVSS final design - poloidal array of 60 sensors welded to the vacuum vessel outer surface, each a PAIR of bismuth Hall sensors (poloidal-plane parallel + normal axes); sensors tested under ITER-relevant conditions (neutron irradiation, bakeout) to at least +/-7 T; AC analogue lock-in current-spinning electronics to eliminate offset and planar-Hall spurious voltage.",
         verification_basis="Stage 70: DOI/title/authors/venue/volume/pages verified via live Crossref; abstract independently retrieved via Semantic Scholar and read.",
         access_level="abstract_metadata",
         notes="Added at stage 70 (red team). Same normalized DOI as folder-06 row S0149 (counts as overlap, not new, in the folder-06 delta). Establishes OVSS as design/manufacture-stage: ITER is not operating - no OVSS pairing direction has operating-tokamak experience."),
    dict(source_id="P077",
         citation="England, Yoon, Kim, Lee et al., Fusion Eng. Des. 86 (2011) 20-26",
         title="Tokamak field error measurements with an electron beam in KSTAR",
         authors="A.C. England; S.W. Yoon; W.C. Kim; D.K. Lee; et al.",
         year="2011", venue="Fusion Engineering and Design, vol. 86, pp. 20-26",
         doi="10.1016/j.fusengdes.2010.07.021",
         url="https://doi.org/10.1016/j.fusengdes.2010.07.021",
         source_type=h003["source_type"], peer_review_status="verified_peer_reviewed",
         quality_tier="B", topic_tags=p013["topic_tags"],
         claims_supported="Metadata-verified; content at snippet level (flagged): KSTAR commissioning measured vertical-field/field-null errors with a movable electron beam probe PLUS Hall sensor arrays IN ADDITION TO pickup coils - adjacent (tokamak) prior practice of combining Hall arrays and coils for vacuum/error-field commissioning; must be cited-and-distinguished by any stellarator-niche novelty claim (C32/C36d).",
         verification_basis="Stage 70: DOI/title/authors/venue/volume/pages verified via live Crossref and OpenAlex; abstract/body not independently read (publisher 403) - content characterization from search-snippet level only, flagged.",
         access_level="metadata_only",
         notes="Added at stage 70 (red team) as counterevidence adjacency for the stellarator-mapping novelty claim. No folder-06 duplicate (checked by normalized DOI/title)."),
]
for d in rows_new:
    lr.append(new_row(d))
    log(f"[L5] ADDED {d['source_id']}: {d['title'][:70]} ({d['year']})")
log("")
write(LP, lh, lr)
log(f"[ledger] wrote {len(lr)} rows (was 219)\n")

# ---------------- evidence map ----------------
EP = "outputs/01_EVIDENCE_MAP.csv"
eh, er = read(EP)
eidx = {r[0]: i for i, r in enumerate(er)}
ecol = {c: i for i, c in enumerate(eh)}

def eset(cid, field, newval, tag):
    i, j = eidx[cid], ecol[field]
    old = er[i][j]
    er[i][j] = newval
    log(f"[{tag}] {cid}.{field}\n  BEFORE: {old[:260]}\n  AFTER : {newval[:260]}\n")

eset("C02", "claim",
     "Correcting coil/integrator additive drift b_C with a non-integrating absolute reference (Hall, NMR, or magnet current) is hardware-proven (CERN bench: 59.9-120 ppm/s reduced to 0.02-0.08 ppm/s) and is the published design basis of ITER's outer-vessel steady-state sensor (OVSS) subsystem - 60 bismuth-Hall units complementing the inductive set for long-pulse operation (final design published and units manufactured; ITER is not yet operating).", "E1")
eset("C02", "source_ids", "H004;H005;H067;H068;P003", "E1")
eset("C02", "limitations",
     "None of these estimate or correct Hall sensitivity S_H from passive sensing. Stage-70 correction: P003's abstract contains only bismuth-sensor high-field qualification (no OVSS-pairing description) - the pairing claim now rests on H067/H068; 'system level' is design intent, not operating experience (former wording 'deployed at system level' retracted).", "E1")

eset("C05", "claim",
     "JET RHP in-situ co-packaged copper-microsolenoid AC self-test/recalibration (known injected field, synchronous detection) preserved InSb Hall sensitivity to SD ~0.07% over 11.5 years / >19,000 pulses including a D-T campaign; the same embedded microsolenoids double as inductive pickup coils whose signals are recorded during pulses.", "E2")
eset("C05", "source_ids", "H003;H007;H006;H011", "E2")
eset("C05", "limitations",
     "Co-located, common-package, common current-reference chain: what the record proves stable is the product S_H*G_cal (die x winding); a common-mode (shared radiation/thermal) drift of die and reference winding together is undetectable by construction (stage-20 CASE E confound). Stage-70 note: 'same-die' in earlier wording was imprecise - the winding is a separate copper element in the same package.", "E2")

eset("C06", "claim",
     "Existing Hall+coil drift correction does NOT prove PASSIVE in-situ Hall radiation-sensitivity calibration: every fusion-context instance either corrects the coil/integrator chain using the Hall channel as reference with S_H assumed known/stable, or recalibrates the Hall channel ACTIVELY via a known-current microsolenoid (C05 line). No source demonstrates passive, measurement-based coil-derived identification of radiation-induced Hall gain or bias drift in any fusion or radiation environment; in fusion the passive coil-to-Hall direction exists only as published proposals (H003 section 5 dry-run/ramp recalibration; ITER OVSS calibration plan, H067).", "E3")
eset("C06", "counterevidence_ids", "H059;H003;H067;H011", "E3")
eset("C06", "limitations",
     "H059 (non-fusion HTS magnet, driven known ramp, no radiation) is the only demonstrated passive instance; H011 demonstrates the ACTIVE (actuator-injection) variant under fission-reactor irradiation to >1e18 n/cm2. The active-vs-passive distinction is load-bearing for every novelty statement built on this claim (stage-70 correction).", "E3")

eset("C11", "claim",
     "The reverse correction direction - coil channel calibrating the Hall channel in situ from PASSIVELY measured signals - is demonstrated (abstract-confirmed) in exactly one non-fusion case: the Feather-M2 HTS dipole's cryogenic Hall sensors were cross-calibrated in situ against induction-coil sensors during driven magnet ramps. In fusion the same direction is published as PROPOSAL only: H003 section 5 (passive recalibration via dry runs/plasma ramp-up) and the ITER OVSS calibration plan (H067: readjust OVSS sensitivity against outer-vessel inductive coils during current ramps).", "E4")
eset("C11", "source_ids", "H059;H003;H067", "E4")
eset("C11", "limitations",
     "H059: non-fusion, no radiation, engineered excitation, quantitative accuracy figures not read (abstract-level). The fusion instances are unrealized plans - no demonstration exists (C06). H067's cross-calibration sentence is search-index body text (abstract independently verified; full text not accessed) - flagged.", "E4")

eset("C12", "claim",
     "InSb Hall sensitivity degrades under a thermal-inclusive fission neutron spectrum but remains stable under a purely fast-neutron spectrum at comparable fluence (R001: ~1e16 n/cm2 in both facilities); follow-up thermal-type-reactor irradiation series at 8.7e17 and 1.2e18 n/cm2 support the same mechanism (R002); the authors attribute the difference to transmutation (In/Sb thermal-neutron capture) rather than displacement damage.", "E5")
eset("C12", "limitations",
     "Both papers come from the same collaboration (limited independence); numeric degradation magnitudes were not accessible. Stage-70 precision fix: R001's ~1e16 two-spectrum comparison and R002's ~1e18 thermal-series are different fluence regimes - do not quote as one number.", "E5")

eset("C21", "claim",
     "In-situ (during-irradiation) recalibration of Hall sensitivity against a material-diverse PASSIVE field-sensor reference is unreported for any Hall material, in any source found by either the radiation or hybrid lane. Actuator-based in-situ recalibration against a co-packaged copper-winding known-field reference IS reported: during fission-reactor irradiation to >1e18 n/cm2 and through JET operation (H011; C05 line).", "E6")
eset("C21", "counterevidence_ids", "H011", "E6")
eset("C21", "limitations",
     "Bounded by 10A+10B search scope. Stage-70 correction: the surviving gap is specifically the passive witness-SENSOR architecture (stage-30 Option D), not 'in-situ recalibration' per se - novelty statements must make this distinction explicitly.", "E6")

eset("C27", "claim",
     "ITER's OVSS is the strongest real-machine-DESIGN precedent for pairing a DC Hall subsystem with the inductive set: 60 bismuth-Hall pair units on the vacuum vessel outer shell (final design published, units manufactured; ITER not yet operating). The published OVSS calibration plan additionally foresees the REVERSE direction - readjusting slowly-reducing OVSS sensitivity by cross-calibration against outer-vessel inductive coils during plasma current ramps (H067). It is a system-level pairing of separate sensor heads, not a co-located single-package hybrid; neither direction of the pairing has operated on any tokamak yet.", "E7")
eset("C27", "source_ids", "H067;H068;P003", "E7")
eset("C27", "limitations",
     "Stage-70 correction: former single-source anchoring on P003 removed (its abstract is sensor qualification only); H067's cross-calibration sentence is body-level search-index text, flagged; 'precedent' is design-stage - there is no operating-tokamak experience for either direction.", "E7")

eset("C32", "counterevidence_ids", "P077", "E8")
eset("C32", "limitations",
     "The absence cuts both ways: an open niche for the user's HSX context, but zero prior validation to build on. Stage-70 addition: adjacent TOKAMAK commissioning practice exists and must be cited-and-distinguished - KSTAR measured field errors with an e-beam plus Hall sensor arrays in addition to pickup coils (P077, snippet-level content); e-beam mapping remains the entrenched, higher-accuracy stellarator incumbent.", "E8")

eset("C36", "claim",
     "Novelty constraints after direct prior-art analysis: architecture-level 'Hall+coil hybrid' is NOT novel (C01, C29). The credible remaining gaps, each narrowed at stage 70: (a) a joint gain+bias+state identifiability proof for the Hall+coil pair - no such analysis found through 2026 (H021 excludes sensor gain; aerospace magnetometer scale-factor/bias observability work relies on a known-field/attitude mechanism and must be scoped against); (b) hardware-validated PASSIVE bidirectional mutual correction in a real plasma and/or radiation environment - the CONCEPT is published prior art (H003 section 5; ITER OVSS calibration plan H067) and ACTIVE microsolenoid recalibration under D-T/fission irradiation is demonstrated (C05, H011), so what remains open is the passive demonstration plus its identifiability treatment; (c) in-situ radiation-aware Hall recalibration against a material-diverse PASSIVE witness sensor (actuator-winding recalibration is demonstrated, H011); (d) the stellarator-mapping application niche (no stellarator instance found; adjacent KSTAR Hall-array+coil commissioning practice P077 must be distinguished).", "E9")
eset("C36", "source_ids",
     "H021;H001;H002;H004;H059;H003;H067;H068;H011;H006;P077;P052;P057;R071;P013", "E9")
eset("C36", "limitations",
     "Each gap is an absence claim bounded by this mission's search scope; a dedicated prior-art search should precede any publication claim on gaps (a)-(d). Stage-70 addition: 2009/2010 patents on combined sensors for in-situ Hall calibration (GB2427700/FR2887991 formats, via H003 refs 66-67, discovery-level) mean a PATENT search is mandatory before any embedded-actuation novelty claim.", "E9")

write(EP, eh, er)
log(f"[evidence map] wrote {len(er)} rows\n")

# ---------------- new-source audit ----------------
AP = "outputs/01_NEW_SOURCE_AUDIT.csv"
ah, ar = read(AP)
# mirror vocabulary of an existing overlap row (H001) and a new row (P013)
ex_overlap = next(r for r in ar if r[0] == "H001")
log("[A1] overlap-row vocabulary sample:", ex_overlap[3], "|", ex_overlap[4][:60], "|", ex_overlap[5])
ar.append(["H067", "10.1016/j.fusengdes.2021.112398",
           "calibration of the iter outer vessel steady state magnetic sensors",
           "S0148", "same normalized DOI as folder-06 row S0148", ex_overlap[5]])
ar.append(["H068", "10.1016/j.fusengdes.2017.03.043",
           "final design of the iter outer vessel steady state magnetic sensors",
           "S0149", "same normalized DOI as folder-06 row S0149", ex_overlap[5]])
ar.append(["P077", "10.1016/j.fusengdes.2010.07.021",
           "tokamak field error measurements with an electron beam in kstar",
           "no", "no normalized-DOI or normalized-title match in folder-06 ledger (231 rows checked)", "new"])
write(AP, ah, ar)
log(f"[new-source audit] wrote {len(ar)} rows (was 219)\n")

with open("tools/redteam_corrections_applied.txt", "w", encoding="utf-8") as f:
    f.write(LOG.getvalue())
log("DONE - change log saved to tools/redteam_corrections_applied.txt")
