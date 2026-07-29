"""Stage 70 cross-file audit: every S-ID cited anywhere in outputs/ must
resolve to the ledger; every output CSV must parse with a consistent
column count; relative links in outputs/*.md must resolve on disk."""
import csv
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "outputs"


def ledger_ids():
    with open(OUT / "01_SOURCE_LEDGER.csv", encoding="utf-8-sig", newline="") as f:
        return {r["source_id"] for r in csv.DictReader(f)}


def main() -> int:
    problems = []
    ids = ledger_ids()

    # 1) S-ID resolution across every outputs file (md + csv)
    cite_counts = Counter()
    for p in sorted(OUT.iterdir()):
        if p.suffix.lower() not in (".md", ".csv") or p.name.startswith("07_"):
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"\bS\d{4}\b", text):
            # skip DOI/PII contexts like 10.1016/S0924-4247(98)... or
            # article numbers like pfr.5.s2054 (preceded by '/' or '.',
            # or followed by '-' as in an ISSN-based PII)
            before = text[m.start() - 1] if m.start() > 0 else ""
            after = text[m.end()] if m.end() < len(text) else ""
            if before in "/." or after == "-":
                continue
            sid = m.group(0)
            # Documented false positive: row S0090's citation string
            # "Pustovitov, Plasma Fusion Res. 5, S2054 (2010)" contains
            # the journal's article number S2054, which is not a
            # citation ID (manually adjudicated at stage 70).
            if sid == "S2054" and p.name == "01_SOURCE_LEDGER.csv":
                continue
            cite_counts[sid] += 1
            if sid not in ids:
                problems.append(f"UNRESOLVED S-ID {sid} in {p.name}")
    print(f"distinct S-IDs cited across outputs: {len(cite_counts)}")
    uncited = sorted(ids - set(cite_counts))
    print(f"ledger rows never cited anywhere: {len(uncited)}")

    # 2) CSV structural parse for all output CSVs
    for p in sorted(OUT.glob("*.csv")):
        if p.name.startswith("07_"):
            continue
        with open(p, encoding="utf-8-sig", newline="") as f:
            rows = list(csv.reader(f))
        widths = Counter(len(r) for r in rows if any(c.strip() for c in r))
        if len(widths) != 1:
            problems.append(f"CSV RAGGED {p.name}: widths {dict(widths)}")
        print(f"{p.name}: {len(rows)-1} data rows, width {list(widths)}")

    # 3) relative links in outputs/*.md resolve
    link_pat = re.compile(r"\]\(((?!https?://|#|mailto:)[^)]+)\)")
    n_links = 0
    for p in sorted(OUT.glob("*.md")):
        if p.name.startswith("07_"):
            continue
        for m in link_pat.finditer(p.read_text(encoding="utf-8", errors="replace")):
            target = m.group(1).split("#")[0].strip()
            if not target:
                continue
            n_links += 1
            cand = (p.parent / target).resolve()
            if not cand.exists():
                problems.append(f"BROKEN LINK in {p.name}: {m.group(1)}")
    print(f"relative links checked: {n_links}")

    print()
    if problems:
        print("PROBLEMS FOUND:")
        for x in problems:
            print(" -", x)
        return 1
    print("CROSS-FILE AUDIT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
