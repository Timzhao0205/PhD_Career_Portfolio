#!/usr/bin/env python3
"""Strict P7 structural validation beyond the legacy mission validator."""

from __future__ import annotations

import csv
import json
import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
BANNED = re.compile(r"\b(?:India|Indian|Singapore)\b", re.I)
LABELS = [
    "Buyer and painful job", "Product", "Cool frontier vision", "Extreme edge",
    "Current demand proof", "Niche size by bottom-up arithmetic", "Competition",
    "Technical path", "Decisive experiment and budget", "V1 capital and time",
    "Risks and kill criteria", "US route", "China route", "Optional side routes",
    "Expansion", "Score and confidence", "Citations", "Founder fit",
]


def main() -> int:
    errors: list[str] = []
    selection = json.loads((ROOT / "30_SCREENING" / "P5_SELECTION.json").read_text(encoding="utf-8-sig"))
    expected = [row["idea_id"] for row in selection["final_24"]]
    csv_path = ROOT / "60_FINAL_PORTFOLIO" / "02_COMPARISON_MATRIX.csv"
    try:
        with csv_path.open(encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
        ids = [row["idea_id"] for row in rows]
        if ids != expected:
            errors.append("comparison CSV IDs/order do not match frozen selection")
        if len(rows) != 24:
            errors.append(f"comparison CSV row count {len(rows)} != 24")
    except Exception as exc:
        errors.append(f"comparison CSV unreadable: {exc}")

    card_path = ROOT / "60_FINAL_PORTFOLIO" / "01_IDEA_CARDS.md"
    if card_path.exists():
        content = card_path.read_text(encoding="utf-8-sig")
        chunks = re.split(r"(?m)^## \d+\. ", content)[1:]
        if len(chunks) != 24:
            errors.append(f"idea card count {len(chunks)} != 24")
        for chunk in chunks:
            iid = next((value for value in expected if value in chunk[:1000]), "<unknown>")
            for label in LABELS:
                if f"**{label}" not in chunk:
                    errors.append(f"{iid}: missing card field {label}")
            founder = chunk.rfind("**Founder fit")
            if founder >= 0 and any(chunk.rfind(f"**{label}") > founder for label in LABELS[:-1]):
                errors.append(f"{iid}: founder fit is not last")
    else:
        errors.append("missing idea cards")

    roadmap = ROOT / "60_FINAL_PORTFOLIO" / "04_VALIDATION_ROADMAP_2026_2030.md"
    if roadmap.exists():
        value = roadmap.read_text(encoding="utf-8-sig")
        for year in range(2026, 2035):
            if str(year) not in value:
                errors.append(f"roadmap missing year {year}")
    else:
        errors.append("missing roadmap")

    geo = ROOT / "50_GEOGRAPHY" / "GEOGRAPHY_BRIEF.md"
    if geo.exists():
        value = geo.read_text(encoding="utf-8-sig")
        if value.lower().count("united states") < 3 or value.lower().count("china") < 3:
            errors.append("geography brief lacks full primary treatment of both countries")
    else:
        errors.append("missing geography brief")

    for rel in (
        "50_GEOGRAPHY/GEOGRAPHY_BRIEF.md",
        "60_FINAL_PORTFOLIO/00_EXECUTIVE_PORTFOLIO.md",
        "60_FINAL_PORTFOLIO/01_IDEA_CARDS.md",
        "60_FINAL_PORTFOLIO/02_COMPARISON_MATRIX.csv",
        "60_FINAL_PORTFOLIO/03_FRONTIER_MAP.md",
        "60_FINAL_PORTFOLIO/04_VALIDATION_ROADMAP_2026_2030.md",
    ):
        path = ROOT / rel
        if path.exists() and BANNED.search(path.read_text(encoding="utf-8-sig")):
            errors.append(f"{rel}: excluded-market reference")
    if errors:
        print("FINAL PORTFOLIO VALIDATION FAIL")
        for error in errors:
            print("-", error)
        return 1
    print("FINAL PORTFOLIO VALIDATION PASS exact24 full cards roadmap2026-2034 geography dual-primary")
    return 0


if __name__ == "__main__":
    sys.exit(main())
