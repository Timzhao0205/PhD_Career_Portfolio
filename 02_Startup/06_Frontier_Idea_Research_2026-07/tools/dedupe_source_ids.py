#!/usr/bin/env python3
"""Collapse historical source-ID collisions to one authoritative row per ID."""

from __future__ import annotations

import collections
import json
import pathlib
import shutil


ROOT = pathlib.Path(__file__).resolve().parents[1]
PATH = ROOT / "90_BIBLIOGRAPHY" / "sources.json"
BACKUP = ROOT / "98_RUN_LOGS" / "P8_PRE_SOURCE_ID_DEDUPE_sources.json"


def richness(row: dict) -> tuple[int, int, int, int]:
    audit = row.get("india_origin_audit") or {}
    return (
        int(bool(row.get("fetched"))),
        int(bool(audit.get("status"))),
        int(bool(row.get("claim_supported"))),
        len(str(row.get("locator") or "")),
    )


def main() -> int:
    ledger = json.loads(PATH.read_text(encoding="utf-8-sig"))
    groups: dict[str, list[dict]] = collections.defaultdict(list)
    order: list[str] = []
    for row in ledger:
        source_id = row["id"]
        if source_id not in groups:
            order.append(source_id)
        groups[source_id].append(row)
    output: list[dict] = []
    collisions: list[dict] = []
    for source_id in order:
        group = groups[source_id]
        accepted = [row for row in group if row.get("accepted") is True]
        if len(accepted) > 1:
            raise SystemExit(f"multiple accepted rows share ID {source_id}")
        chosen = accepted[0] if accepted else max(group, key=richness)
        output.append(chosen)
        if len(group) > 1:
            collisions.append({
                "source_id": source_id,
                "rows_before": len(group),
                "chosen_accepted": bool(chosen.get("accepted")),
                "chosen_canonical_key": chosen.get("canonical_key"),
                "discarded": [
                    {
                        "accepted": bool(row.get("accepted")),
                        "canonical_key": row.get("canonical_key"),
                        "title": row.get("title"),
                    }
                    for row in group if row is not chosen
                ],
            })
    if not BACKUP.exists():
        shutil.copy2(PATH, BACKUP)
    PATH.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report = {
        "artifact": "P8_SOURCE_ID_DEDUPE",
        "status": "complete",
        "rows_before": len(ledger),
        "rows_after": len(output),
        "duplicate_ids_collapsed": len(collisions),
        "extra_rows_removed": len(ledger) - len(output),
        "policy": "Choose the sole accepted row when present; otherwise retain the richest fetched/audited rejected record. No ID had multiple accepted rows.",
        "collisions": collisions,
    }
    (ROOT / "99_AUDIT" / "P8_SOURCE_ID_DEDUPE.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ROOT / "99_AUDIT" / "P8_SOURCE_ID_DEDUPE.md").write_text(
        "# P8 source-ID deduplication\n\n"
        f"Collapsed {len(collisions)} historical duplicate IDs and removed {len(ledger)-len(output)} extra rows. "
        "Every duplicate group had at most one accepted record, so the authoritative accepted row was retained; "
        "groups containing only rejected records retained the richest fetched/audited row. The pre-repair ledger is preserved in `98_RUN_LOGS/P8_PRE_SOURCE_ID_DEDUPE_sources.json`.\n",
        encoding="utf-8",
    )
    print(f"source ID dedupe complete rows={len(ledger)}->{len(output)} duplicate_ids={len(collisions)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
