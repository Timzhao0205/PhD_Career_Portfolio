"""Stage 10D: verify every [S####](https://doi.org/...) link in the review
matches the ledger's DOI for that ID, and that every bare [S####] exists."""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEDGER = ROOT / "outputs" / "01_SOURCE_LEDGER.csv"
REVIEW = ROOT / "outputs" / "01_LITERATURE_REVIEW.md"

with open(LEDGER, encoding="utf-8", newline="") as fh:
    ledger = {r["source_id"]: r for r in csv.DictReader(fh)}

text = REVIEW.read_text(encoding="utf-8")

linked = re.findall(r"\[(S\d{4})\]\((https://doi\.org/[^)]+)\)", text)
bare = re.findall(r"\[(S\d{4})\](?!\()", text)

fails = []
from urllib.parse import unquote

for sid, url in linked:
    if sid not in ledger:
        fails.append(f"{sid}: not in ledger")
        continue
    if unquote(url.strip().lower()) != ledger[sid]["url"].strip().lower():
        fails.append(f"{sid}: review={url} ledger={ledger[sid]['url']}")
for sid in bare:
    if sid not in ledger:
        fails.append(f"bare {sid}: not in ledger")

cited = {s for s, _ in linked} | set(bare)
print(f"linked citations: {len(linked)} ({len({s for s,_ in linked})} unique)")
print(f"bare citations: {len(bare)}")
print(f"unique sources cited: {len(cited)} / {len(ledger)}")
if fails:
    print("CITATION CHECK: FAIL")
    for f in fails:
        print("  ", f)
else:
    print("CITATION CHECK: PASS (every link matches the ledger DOI)")

# sanity: spot-print a few ID->title pairs used heavily in the review
for sid in ["S0068", "S0070", "S0128", "S0132", "S0143", "S0148", "S0181",
            "S0189", "S0219", "S0226"]:
    print(f"  {sid}: {ledger[sid]['title'][:70]}")
