#!/usr/bin/env python3
"""Normalize two accepted P5 round-two journal records to the ledger enum."""

from __future__ import annotations

import json
import pathlib


root = pathlib.Path(__file__).resolve().parents[1]
path = root / "90_BIBLIOGRAPHY" / "sources.json"
ledger = json.loads(path.read_text(encoding="utf-8-sig"))
target = {"P5R2-CN-S04", "P5R2-CN-S14"}
seen: set[str] = set()
for row in ledger:
    if row.get("id") in target:
        if row.get("source_type") != "academic_peer_reviewed" or not row.get("peer_review_evidence_url"):
            raise SystemExit(f"record is not a verified journal source: {row.get('id')}")
        row["peer_review_status"] = "verified"
        seen.add(row["id"])
if seen != target:
    raise SystemExit(f"missing target records: {sorted(target - seen)}")
path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("normalized peer-review status: " + ", ".join(sorted(seen)))
