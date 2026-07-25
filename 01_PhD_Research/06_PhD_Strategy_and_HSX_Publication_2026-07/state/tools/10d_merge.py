"""Stage 10D: merge the three lane CSVs into outputs/01_SOURCE_LEDGER.csv.

Deterministic merge:
- lane order 10A -> 10B -> 10C, original row order preserved;
- drop B0041 (dup of A0068) and B0054 (dup of A0070), merging their info;
- apply Crossref-resolved metadata corrections from the 10D verification pass;
- assign stable IDs S0001..S0231;
- append per-row provenance and 10D re-verification notes.
"""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FILES = [
    ROOT / "evidence" / "10A_GAN_WBG_SOURCES.csv",
    ROOT / "evidence" / "10B_FUSION_DIAGNOSTICS_SOURCES.csv",
    ROOT / "evidence" / "10C_METHODS_SOURCES.csv",
]
OUT = ROOT / "outputs" / "01_SOURCE_LEDGER.csv"
MAP_OUT = ROOT / "state" / "tools" / "10d_id_map.csv"

HEADER = (
    "source_id,citation,title,authors,year,venue,doi,url,source_type,"
    "peer_review_status,quality_tier,topic_tags,claims_supported,"
    "verification_basis,access_level,notes"
).split(",")

DROP = {"B0041", "B0054"}

# DOIs personally re-verified by Fable 5 at stage 10D via the Crossref API.
REVERIFIED = {
    "10.1109/ises54909.2022.00071", "10.1063/1.2201339", "10.1063/1.115110",
    "10.3390/ma17051147", "10.1088/1741-4326/aa7867",
    "10.1088/1741-4326/ac8aad", "10.1007/s10582-006-0185-4",
    "10.1088/1361-6587/ae6c59", "10.1063/1.5038871",
    "10.1016/j.fusengdes.2019.03.201", "10.1016/j.fusengdes.2025.115180",
    "10.1088/1361-6587/adb179", "10.1088/0029-5515/55/11/113012",
    "10.1063/1.4894209", "10.1111/1467-9868.00294", "10.1109/TIM.2007.908635",
    "10.1063/1.5039356", "10.1088/1741-4326/ab555f",
    "10.1038/s41586-021-04301-9", "10.1088/1741-4326/acc852",
    "10.1038/s41598-023-42991-5", "10.1088/1741-4326/ae2937",
    "10.1088/1741-4326/ae34c6", "10.21014/actaimeko.v13i4.1762",
    "10.1016/j.asoc.2026.115267", "10.1007/s00542-013-2029-z",
    "10.1080/10420150.2024.2378424", "10.1088/1741-4326/adaed0",
    "10.1049/cds2.12067", "10.1007/s11214-025-01170-w",
    "10.1017/s0022377825100962", "10.1088/1361-6587/ae1870",
}
REVERIFY_NOTE = (
    "; independently re-verified at stage 10D by the merge session via the "
    "Crossref API (title/authors/venue/volume/year match)"
)

rows = []
by_id = {}
for f in FILES:
    with open(f, encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            rows.append(row)
            by_id[row["source_id"]] = row


def merge_tags(a, b):
    seen, out = set(), []
    for t in (a.split(";") + b.split(";")):
        t = t.strip()
        k = t.lower()
        if t and k not in seen:
            seen.add(k)
            out.append(t)
    return ";".join(out)


# --- merge duplicate-pair info into the kept 10A rows ---
a68, b41 = by_id["A0068"], by_id["B0041"]
a68["topic_tags"] = merge_tags(a68["topic_tags"], b41["topic_tags"])
a68["notes"] += (
    " [10D merge] Found independently by three lanes: 10A (A0068), 10B "
    "(B0041, which additionally framed the hybrid coil+Hall architecture as "
    "the field's own answer to long-pulse drift), and a 10C lane (excluded "
    "there as a cross-stage duplicate). Kept once here; the triple "
    "independent discovery marks it as one of the most load-bearing "
    "precedents in the whole ledger."
)

a70, b54 = by_id["A0070"], by_id["B0054"]
a70["topic_tags"] = merge_tags(a70["topic_tags"], b54["topic_tags"])
a70["notes"] += (
    " [10D merge] Found independently by three lanes: 10A (A0070), 10B "
    "(B0054), and a 10C lane (excluded there as a cross-stage duplicate). "
    "Author rendering resolved at 10D against the Crossref record, which "
    "returns 'K. Kovarik; I. Duran (Crossref diacritic form Curan/Duran); "
    "I. Bolshakova (Crossref typo form Boshakova); R. Holyaka; V. Erashok' "
    "-- the ASCII forms Kovarik/Duran/Bolshakova used here are the "
    "standard transliterations of this well-documented Czech/Ukrainian "
    "author group (same lineage as the JET/ITER Hall-probe rows)."
)

# --- Crossref-resolved corrections from the 10D verification pass ---
b52 = by_id["B0052"]
b52["authors"] = b52["authors"].replace("Ivan Ceran", "Ivan Duran")
b52["citation"] = b52["citation"].replace("Ceran et al.", "Duran et al.")
b52["notes"] += (
    " [10D correction] Lead author fixed from the lane's 'Ivan Ceran' to "
    "Ivan Duran per the Crossref record (Ivan Ďuran) fetched at 10D."
)

b53 = by_id["B0053"]
b53["authors"] = b53["authors"].replace("Ivan Curan", "Ivan Duran")
b53["citation"] = "Ivanek et al., Fusion Eng. Des. 217, 115180 (2025)"
b53["notes"] += (
    " [10D correction] Second author fixed from the lane's 'Ivan Curan' to "
    "Ivan Duran and volume enriched to 217 per the Crossref record (Matěj "
    "Ivánek; Ivan Ďuran; ...) fetched at 10D."
)

c62 = by_id["C0062"]
c62["authors"] = c62["authors"].replace("Marco Coesson", "Marco Coisson")
c62["citation"] = c62["citation"].replace("Coesson,", "Coisson,")
c62["notes"] += (
    " [10D correction] First author fixed from the lane's 'Coesson' to "
    "Coisson per the Crossref record (Marco Coïsson) fetched at 10D."
)

b43 = by_id["B0043"]
b43["citation"] = "Duran et al., Plasma Phys. Control. Fusion 68(6) (2026)"
b43["notes"] += (
    " [10D enrichment] Volume/issue 68(6) added per the Crossref record "
    "fetched at 10D."
)

c48 = by_id["C0048"]
c48["citation"] = "Subbotin et al., Nucl. Fusion 66(2) (2026)"
c48["notes"] += (
    " [10D enrichment] Volume/issue 66(2) added per the Crossref record "
    "fetched at 10D."
)

b25 = by_id["B0025"]
b25["citation"] = "Inoue et al., Nucl. Fusion 65(3) (2025)"
b25["notes"] += (
    " [10D enrichment] Volume/issue 65(3) added per the Crossref record "
    "fetched at 10D."
)

# --- venue normalization (same journal, different lane renderings) ---
VENUE_NORM = {
    "Sensors (MDPI)": "Sensors",
    "Materials (Basel)": "Materials",
}
for row in rows:
    if row["venue"] in VENUE_NORM:
        row["venue"] = VENUE_NORM[row["venue"]]

# --- assign final IDs and write ---
out_rows, id_map = [], []
n = 0
for row in rows:
    old = row["source_id"]
    if old in DROP:
        dup_of = "A0068" if old == "B0041" else "A0070"
        id_map.append({"old_id": old, "new_id": "", "kept_as": dup_of,
                       "doi": row["doi"]})
        continue
    n += 1
    new_id = f"S{n:04d}"
    id_map.append({"old_id": old, "new_id": new_id, "kept_as": new_id,
                   "doi": row["doi"]})
    new_row = {k: row[k] for k in HEADER}
    new_row["source_id"] = new_id
    prov = f"Provenance: {old}"
    if old == "A0068":
        prov += " (also B0041)"
    elif old == "A0070":
        prov += " (also B0054)"
    if row["doi"].strip().lower() in {d.lower() for d in REVERIFIED}:
        new_row["verification_basis"] = new_row["verification_basis"].rstrip(".") + REVERIFY_NOTE
    sep = "" if new_row["notes"].endswith((" ", "")) and not new_row["notes"] else " "
    new_row["notes"] = (new_row["notes"] + sep + "[" + prov + "]").strip()
    out_rows.append(new_row)

with open(OUT, "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=HEADER, quoting=csv.QUOTE_MINIMAL)
    w.writeheader()
    w.writerows(out_rows)

with open(MAP_OUT, "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["old_id", "new_id", "kept_as", "doi"])
    w.writeheader()
    w.writerows(id_map)

print(f"Wrote {len(out_rows)} rows to {OUT}")
print(f"ID map ({len(id_map)} entries) at {MAP_OUT}")
print(f"Last ID: {out_rows[-1]['source_id']}")
