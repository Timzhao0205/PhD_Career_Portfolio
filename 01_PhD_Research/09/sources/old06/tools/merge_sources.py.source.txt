#!/usr/bin/env python3
"""Merge mission ledgers by canonical_key without manufacturing acceptance or metadata."""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "90_BIBLIOGRAPHY" / "sources.json"
SCAN_DIRS = ["10_SOURCE_ATLAS", "20_OPPORTUNITY_POOL", "30_SCREENING", "40_DEEP_DIVES", "50_GEOGRAPHY"]
LIST_FIELDS = ("lane_ids", "idea_ids", "geography")

def load_records(path):
    try: obj=json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception as e: raise RuntimeError(f"{path}: {e}")
    if isinstance(obj, dict) and isinstance(obj.get("sources"), list): obj=obj["sources"]
    if not isinstance(obj, list): return []
    return [x for x in obj if isinstance(x, dict) and x.get("canonical_key")]

def quality(s):
    status=(s.get("india_origin_audit") or {}).get("status")
    audit_rank={"verified_non_india_origin":3,"verified_multinational_allowed":3,
                "excluded_india_origin":2,"pending":1}.get(status,0)
    return (audit_rank, bool(s.get("accepted")), bool(s.get("fetched")), s.get("tier")=="T1",
            s.get("peer_review_status")=="verified", len(str(s.get("claim_supported", ""))))

def merge(a,b):
    best, other = (b,a) if quality(b)>quality(a) else (a,b)
    out=dict(other); out.update({k:v for k,v in best.items() if v not in (None,"",[])})
    for field in LIST_FIELDS:
        vals=[]
        for src in (a,b):
            v=src.get(field) or []
            if isinstance(v,str): v=[v]
            vals.extend(v)
        out[field]=sorted({str(x) for x in vals if str(x)})
    notes=[str(x.get("notes","")).strip() for x in (a,b) if str(x.get("notes","")).strip()]
    out["notes"]=" | ".join(dict.fromkeys(notes))
    return out

def main():
    paths=[]
    for d in SCAN_DIRS:
        paths.extend(p for p in (ROOT/d).rglob("*.json") if p.resolve()!=OUT.resolve())
    merged={}
    for path in sorted(paths):
        for rec in load_records(path):
            key=str(rec["canonical_key"]).strip().lower()
            if not key: continue
            merged[key]=merge(merged[key],rec) if key in merged else rec
    records=sorted(merged.values(), key=lambda s:(not bool(s.get("accepted")),str(s.get("id",""))))
    OUT.write_text(json.dumps(records,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"merged={len(records)} accepted={sum(x.get('accepted') is True for x in records)} output={OUT.relative_to(ROOT)}")
    return 0

if __name__ == "__main__": sys.exit(main())
