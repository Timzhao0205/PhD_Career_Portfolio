from pathlib import Path
import csv
import sys
import zipfile
from lxml import etree
from docx import Document

ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / "outputs" / "Magnetic_Sensor_Review_Two_Version_Compilation.docx"
REG = ROOT / "outputs" / "reference_registry.csv"
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

errors = []
with zipfile.ZipFile(DOCX) as z:
    bad = z.testzip()
    if bad:
        errors.append(f"Corrupt ZIP member: {bad}")
    document_xml = etree.fromstring(z.read("word/document.xml"))
    styles_xml = etree.fromstring(z.read("word/styles.xml"))
    numbering_xml = etree.fromstring(z.read("word/numbering.xml"))

doc = Document(DOCX)
text = "\n".join(p.text for p in doc.paragraphs)
for table in doc.tables:
    for row in table.rows:
        text += "\n" + " | ".join(c.text for c in row.cells)

for token in ("turn0", "turn1", "codex-file-citation", "{{", "}}"):
    if token in text:
        errors.append(f"Internal/placeholder token present: {token}")

with REG.open(encoding="utf-8-sig", newline="") as fh:
    refs = list(csv.DictReader(fh))
missing_keys = [r["key"] for r in refs if r["key"] not in text]
if missing_keys:
    errors.append(f"Registry keys absent from appendix: {missing_keys[:10]} (total {len(missing_keys)})")

sects = document_xml.xpath("//w:sectPr", namespaces=NS)
for idx, sect in enumerate(sects, 1):
    pg_sz = sect.find("w:pgSz", NS)
    pg_mar = sect.find("w:pgMar", NS)
    if pg_sz is None or pg_sz.get(f"{{{NS['w']}}}w") != "12240" or pg_sz.get(f"{{{NS['w']}}}h") != "15840":
        errors.append(f"Section {idx}: page size is not US Letter portrait")
    if pg_mar is None:
        errors.append(f"Section {idx}: missing page margins")
    else:
        for side in ("top", "right", "bottom", "left"):
            if pg_mar.get(f"{{{NS['w']}}}{side}") != "1440":
                errors.append(f"Section {idx}: {side} margin mismatch")

styles = {s.get(f"{{{NS['w']}}}styleId"): s for s in styles_xml.xpath("//w:style", namespaces=NS)}
for style_id in ("Normal", "Heading1", "Heading2", "Heading3", "Evidence"):
    if style_id not in styles:
        errors.append(f"Missing required style: {style_id}")

tables = document_xml.xpath("//w:tbl", namespaces=NS)
for idx, table in enumerate(tables, 1):
    tbl_w = table.find("w:tblPr/w:tblW", NS)
    tbl_ind = table.find("w:tblPr/w:tblInd", NS)
    grid = table.findall("w:tblGrid/w:gridCol", NS)
    widths = [int(x.get(f"{{{NS['w']}}}w")) for x in grid]
    if tbl_w is None or int(tbl_w.get(f"{{{NS['w']}}}w")) != sum(widths):
        errors.append(f"Table {idx}: tblW/grid mismatch")
    if tbl_ind is None or tbl_ind.get(f"{{{NS['w']}}}w") != "120":
        errors.append(f"Table {idx}: tblInd mismatch")
    for r, row in enumerate(table.findall("w:tr", NS), 1):
        cells = row.findall("w:tc", NS)
        if len(cells) != len(widths):
            errors.append(f"Table {idx} row {r}: cell/grid count mismatch")
            continue
        cell_widths = []
        for cell in cells:
            tcw = cell.find("w:tcPr/w:tcW", NS)
            cell_widths.append(int(tcw.get(f"{{{NS['w']}}}w")) if tcw is not None else -1)
        if cell_widths != widths:
            errors.append(f"Table {idx} row {r}: tcW/grid mismatch")
        height = row.find("w:trPr/w:trHeight", NS)
        if height is not None and height.get(f"{{{NS['w']}}}hRule") == "exact":
            errors.append(f"Table {idx} row {r}: fixed exact height")

num_texts = numbering_xml.xpath("//w:lvlText/@w:val", namespaces=NS)
if "•" not in num_texts:
    errors.append("Custom real bullet numbering definition missing")

print(f"paragraphs={len(doc.paragraphs)} tables={len(doc.tables)} references={len(refs)} sections={len(doc.sections)}")
print(f"headings={sum(1 for p in doc.paragraphs if p.style.name.startswith('Heading'))}")
if errors:
    print("AUDIT FAILED")
    for error in errors:
        print("-", error)
    sys.exit(1)
print("AUDIT PASSED")
