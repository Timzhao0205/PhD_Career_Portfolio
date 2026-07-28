#!/usr/bin/env python3
"""Create deterministic, non-overlapping P2A batches from the current accepted ledger."""
import json, pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
data=json.loads((ROOT/"90_BIBLIOGRAPHY"/"sources.json").read_text(encoding="utf-8-sig"))
ids=sorted(s["id"] for s in data if s.get("accepted") is True)
size=70
batches=[{"batch_id":f"P2A-{i//size+1:02d}","source_ids":ids[i:i+size]} for i in range(0,len(ids),size)]
out={"accepted_records_to_audit":len(ids),"batch_size_max":size,"batches":batches,
     "completion_rule":"Every ID must end with verified_non_india_origin or verified_multinational_allowed, or be quarantined and independently replaced if a gate fails."}
(ROOT/"05_STATE"/"INDIA_SOURCE_ORIGIN_AUDIT_QUEUE.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"origin audit queue records={len(ids)} batches={len(batches)}")
