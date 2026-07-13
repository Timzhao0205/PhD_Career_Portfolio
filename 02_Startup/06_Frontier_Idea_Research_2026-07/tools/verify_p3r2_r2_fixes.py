# Read-only verification of the P3R2 round-2 fix application. Run from project root.
import json
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

f = json.load(open("20_OPPORTUNITY_POOL/P3R2_F_cn_topup.json", encoding="utf-8"))
a = json.load(open("20_OPPORTUNITY_POOL/P3R2_A_us_pain.json", encoding="utf-8"))
F = {r["idea_id"]: r for r in f}

print("F verdicts:", dict(Counter(r["elegance_verdict"] for r in f)))
fix_notes = [r["idea_id"] for r in f if "fix_applied_notes" in r]
print("fix_applied_notes on:", len(fix_notes), fix_notes)
print("F-06 flags:", F["P3R2-F-06"]["primary_market"], F["P3R2-F-06"]["china_beachhead"])
print("F-18 dup:", F["P3R2-F-18"].get("duplicate_of"),
      "| F-21 dup:", F["P3R2-F-21"].get("duplicate_of"),
      "| F-08 dup:", F["P3R2-F-08"].get("duplicate_of"))
print("F-02 new ids present:",
      "L03-052" in F["P3R2-F-02"]["demand_source_ids"],
      "L07-009" in F["P3R2-F-02"]["technical_source_ids"])
a02 = [r for r in a if r["idea_id"] == "P3R2-A-02"][0]
print("A-02 merge_import_notes present:", "merge_import_notes" in a02,
      "| plan has F-08 workstream:", "die-characterization" in a02["precompany_plan_2026_2029"])
print("A-02 key order tail:", list(a02.keys())[-3:])

# quarantine check: prefilter-listed IDs must not appear in the F file
txt = open("20_OPPORTUNITY_POOL/P3R2_F_cn_topup.json", encoding="utf-8").read()
pre = json.load(open("05_STATE/INDIA_SOURCE_ORIGIN_PREFILTER.json", encoding="utf-8"))


def collect_ids(obj, acc):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in ("id", "source_id") and isinstance(v, str) and re.match(r"^L\d{2}-\d{3}$", v):
                acc.add(v)
            else:
                collect_ids(v, acc)
    elif isinstance(obj, list):
        for x in obj:
            collect_ids(x, acc)


qids = set()
collect_ids(pre, qids)
hits = sorted(i for i in qids if i in txt)
print("prefilter IDs found in F file:", hits if hits else "none")

md = open("20_OPPORTUNITY_POOL/P3R2_F_cn_topup.md", encoding="utf-8").read()
print("MD FIX annotations:", md.count("- **[FIX applied 2026-07-13 R2"))
print("MD PROMOTE annotations:", md.count("R2 - PROMOTE]"))
print("MD REJECT annotations:", md.count("R2 - REJECT]"))
print("MD MERGED annotations:", md.count("R2 - MERGED INTO"))
print("MD blockquote present:", "**Adjudication R2 applied 2026-07-13:**" in md)
print("MD F-06 header downgraded:", "(US-primary; CN license chapter only" in md)
amd = open("20_OPPORTUNITY_POOL/P3R2_A_us_pain.md", encoding="utf-8").read()
print("A MD import note present:", "- **[Merge-import 2026-07-13 R2]:**" in amd)
