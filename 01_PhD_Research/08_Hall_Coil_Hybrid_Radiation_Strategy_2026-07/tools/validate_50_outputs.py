"""Validate stage-50 outputs (limitations, technology comparison, falsification).

Checks existence/nontriviality, exact CSV header, row counts, ID resolution
against the stage-10D ledger / evidence map / stage-30 risk register,
required per-item fields, honesty markers (unknown / not_applicable /
counterexamples), and cross-references between the two markdown outputs.
"""

import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
OUT = os.path.join(ROOT, "outputs")

LIM = os.path.join(OUT, "05_LIMITATIONS_AND_FAILURE_MODES.md")
CMP = os.path.join(OUT, "05_TECHNOLOGY_COMPARISON.csv")
FAL = os.path.join(OUT, "05_FALSIFICATION_TESTS.md")
LEDGER = os.path.join(OUT, "01_SOURCE_LEDGER.csv")
EVMAP = os.path.join(OUT, "01_EVIDENCE_MAP.csv")
RISKS = os.path.join(OUT, "03_RADIATION_RISK_REGISTER.csv")

EXPECTED_HEADER = (
    "technology,principle,dc_response,bandwidth,dynamic_range,field_range,"
    "temperature_limit,radiation_evidence,drift,calibration_traceability,"
    "vector_capability,size_and_placement,electronics,integration_burden,"
    "maturity,cost_category,best_fit,critical_limit,evidence_ids,confidence"
).split(",")

FM_FIELDS = [
    "**Cause", "**Symptom", "**Detectability", "**Consequence",
    "**Mitigation", "**Residual risk", "**Test",
]
FT_FIELDS = [
    "**Hypothesis at risk", "**Setup", "**Reference", "**Metric",
    "**Pass/fail threshold", "**Confounders", "**Decision", "**Evidence",
]

results = []


def check(name, ok, detail=""):
    results.append((name, ok, detail))
    print(f"{'PASS' if ok else 'FAIL'}: {name}" + (f" - {detail}" if detail else ""))


def main():
    # -- existence / nontriviality ------------------------------------------
    for p, floor in [(LIM, 15000), (CMP, 8000), (FAL, 12000)]:
        ok = os.path.isfile(p) and os.path.getsize(p) >= floor
        check(f"exists+nontrivial: {os.path.basename(p)}", ok,
              f"{os.path.getsize(p) if os.path.isfile(p) else 0} bytes (floor {floor})")

    lim = open(LIM, encoding="utf-8").read()
    fal = open(FAL, encoding="utf-8").read()

    # -- reference sets ------------------------------------------------------
    with open(LEDGER, encoding="utf-8") as f:
        source_ids = {r["source_id"] for r in csv.DictReader(f)}
    with open(EVMAP, encoding="utf-8") as f:
        claim_ids = {r["claim_id"] for r in csv.DictReader(f)}
    with open(RISKS, encoding="utf-8") as f:
        risk_ids = {r["risk_id"] for r in csv.DictReader(f)}
    check("reference files parsed", bool(source_ids and claim_ids and risk_ids),
          f"{len(source_ids)} sources, {len(claim_ids)} claims, {len(risk_ids)} risks")

    # -- CSV: header, rows, uniqueness --------------------------------------
    with open(CMP, encoding="utf-8", newline="") as f:
        rdr = csv.DictReader(f)
        header = rdr.fieldnames
        rows = list(rdr)
    check("CSV exact header", header == EXPECTED_HEADER, f"{len(header or [])} cols")
    check("CSV >= 10 technologies", len(rows) >= 10, f"{len(rows)} rows")
    techs = [r["technology"] for r in rows]
    check("CSV unique technologies", len(techs) == len(set(techs)))
    empty = [(r["technology"], k) for r in rows for k, v in r.items() if not (v or "").strip()]
    check("CSV no empty cells", not empty, str(empty[:4]))

    # -- CSV: evidence IDs resolve ------------------------------------------
    bad = []
    for r in rows:
        for tok in re.split(r"[;\s]+", r["evidence_ids"].strip()):
            if tok and tok not in source_ids and tok not in claim_ids:
                bad.append((r["technology"][:30], tok))
    check("CSV evidence_ids resolve", not bad, str(bad[:6]))

    # -- CSV: honesty markers and counterexamples ---------------------------
    blob = " ".join(v for r in rows for v in r.values()).lower()
    check("CSV uses 'unknown'", "unknown" in blob)
    check("CSV uses 'not_applicable'", "not_applicable" in blob)
    n_counter = sum(1 for r in rows if "COUNTEREXAMPLE" in r["best_fit"])
    check("CSV >= 3 simpler-sensor-wins counterexamples", n_counter >= 3, f"{n_counter}")

    # -- Limitations MD: >= 15 failure modes, all 7 fields each -------------
    fm_ids = re.findall(r"^### (FM-\d{2})", lim, re.M)
    check("MD >= 15 failure modes", len(fm_ids) >= 15, f"{len(fm_ids)} modes: {fm_ids[0]}..{fm_ids[-1]}")
    check("MD failure-mode IDs unique", len(fm_ids) == len(set(fm_ids)))
    sections = re.split(r"^### ", lim, flags=re.M)
    missing = []
    for sec in sections:
        m = re.match(r"(FM-\d{2})", sec)
        if not m:
            continue
        for fld in FM_FIELDS:
            if fld not in sec:
                missing.append((m.group(1), fld))
    check("MD every FM has cause/symptom/detectability/consequence/"
          "mitigation/residual/test", not missing, str(missing[:6]))

    # -- Limitations MD: required stage areas present -----------------------
    for kw in ["novelty", "narrowest defensible", "not novel",
               "counterexample", "uncertainty floor", "channel-count"]:
        check(f"MD covers '{kw}'", kw.lower() in lim.lower())

    # -- Falsification MD: tests, fields, ordering note ----------------------
    ft_ids = re.findall(r"^## (FT-\d{2})", fal, re.M)
    check("FT >= 8 tests", len(ft_ids) >= 8, f"{len(ft_ids)} tests")
    check("FT IDs unique+ordered", ft_ids == sorted(set(ft_ids)), str(ft_ids))
    missing = []
    for sec in re.split(r"^## ", fal, flags=re.M):
        m = re.match(r"(FT-\d{2})", sec)
        if not m:
            continue
        for fld in FT_FIELDS:
            if fld not in sec:
                missing.append((m.group(1), fld))
    check("FT every test has hypothesis/setup/reference/metric/threshold/"
          "confounders/decision/evidence", not missing, str(missing[:6]))
    n_radfree = len(re.findall(r"\| FT-\d{2} \|[^|]+\|[^|]+\| yes \|", fal))
    check("FT majority radiation-free with stop decisions", n_radfree >= 8,
          f"{n_radfree} radiation-free rows in summary table")

    # -- ID resolution in both MDs ------------------------------------------
    for name, text in [("limitations", lim), ("falsification", fal)]:
        bad = sorted({t for t in re.findall(r"\b([HRP]\d{3})\b", text)
                      if t not in source_ids})
        check(f"{name}: source IDs resolve", not bad, str(bad[:8]))
        bad = sorted({t for t in re.findall(r"\bC\d{2}\b", text)
                      if t not in claim_ids})
        check(f"{name}: claim IDs resolve", not bad, str(bad[:8]))
        bad = sorted({t for t in re.findall(r"\bRR-\d{2}\b", text)
                      if t not in risk_ids})
        check(f"{name}: risk IDs resolve", not bad, str(bad[:8]))

    # -- cross-references between the two MDs --------------------------------
    bad = sorted({t for t in re.findall(r"\bFT-\d{2}\b", lim) if t not in ft_ids})
    check("limitations cites only existing FT IDs", not bad, str(bad))
    bad = sorted({t for t in re.findall(r"\bFM-\d{2}\b", fal) if t not in fm_ids})
    check("falsification cites only existing FM IDs", not bad, str(bad))

    n_fail = sum(1 for _, ok, _ in results if not ok)
    print(f"\n{len(results) - n_fail}/{len(results)} PASS")
    sys.exit(1 if n_fail else 0)


if __name__ == "__main__":
    main()
