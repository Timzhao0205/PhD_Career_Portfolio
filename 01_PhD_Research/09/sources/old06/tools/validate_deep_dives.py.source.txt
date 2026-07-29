#!/usr/bin/env python3
"""Validate exact deep-dive coverage, length, and accepted-source quotas."""

from __future__ import annotations

import json
import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
PRIMARY = {
    "buyer_tender", "buyer_specification", "procurement_award", "company_filing",
    "earnings_transcript", "official_project_award", "direct_customer_documentation",
}
WORD = re.compile(r"\b[\w][\w'’-]*\b", re.UNICODE)
SOURCE_LINE = re.compile(r"<!--\s*SOURCE_IDS:\s*(.*?)\s*-->", re.S)


def main() -> int:
    errors: list[str] = []
    selection = json.loads((ROOT / "30_SCREENING" / "P5_SELECTION.json").read_text(encoding="utf-8-sig"))
    expected = set(selection["top_10_deep_dives"])
    ledger = {
        row["id"]: row
        for row in json.loads((ROOT / "90_BIBLIOGRAPHY" / "sources.json").read_text(encoding="utf-8-sig"))
        if row.get("accepted")
    }
    paths = sorted((ROOT / "40_DEEP_DIVES").glob("DD_*.md"))
    if len(paths) != 10:
        errors.append(f"deep-dive file count {len(paths)} != 10")
    seen: set[str] = set()
    for path in paths:
        text = path.read_text(encoding="utf-8-sig")
        matched = [iid for iid in expected if iid in text[:1000]]
        if len(matched) != 1:
            errors.append(f"{path.name}: expected exactly one top-10 idea ID, found {matched}")
            continue
        iid = matched[0]
        seen.add(iid)
        word_count = len(WORD.findall(re.sub(r"<!--.*?-->", "", text, flags=re.S)))
        if not 2500 <= word_count <= 4000:
            errors.append(f"{path.name}: word count {word_count} outside 2500-4000")
        marker = SOURCE_LINE.search(text)
        if not marker:
            errors.append(f"{path.name}: missing SOURCE_IDS marker")
            continue
        ids = list(dict.fromkeys(marker.group(1).split()))
        refs = [ledger[source_id] for source_id in ids if source_id in ledger]
        peer = sum(row.get("source_type") == "academic_peer_reviewed" for row in refs)
        primary = sum(row.get("demand_evidence_type") in PRIMARY for row in refs)
        if len(refs) < 20 or peer < 7 or primary < 5:
            errors.append(f"{path.name}: sources total={len(refs)} peer={peer} primary={primary}")
    if seen != expected:
        errors.append(f"top-10 coverage mismatch missing={sorted(expected-seen)} extra={sorted(seen-expected)}")
    if errors:
        print("DEEP-DIVE VALIDATION FAIL")
        for error in errors:
            print("-", error)
        return 1
    print("DEEP-DIVE VALIDATION PASS exact=10 words=2500-4000 sources>=20/7/5")
    return 0


if __name__ == "__main__":
    sys.exit(main())
