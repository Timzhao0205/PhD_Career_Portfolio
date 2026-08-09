"""Create PACKAGE_SHA256.json for immutable active package files."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_TOP = {"src", "state", "logs", "outputs", "pilot", "quarantine"}
EXCLUDED_FILES = {"PACKAGE_SHA256.json"}


records: list[dict[str, object]] = []
for path in sorted(ROOT.rglob("*")):
    if not path.is_file():
        continue
    relative = path.relative_to(ROOT)
    if relative.parts[0] in EXCLUDED_TOP:
        continue
    if relative.as_posix() in EXCLUDED_FILES:
        continue
    data = path.read_bytes()
    records.append(
        {
            "path": relative.as_posix(),
            "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest().upper(),
        }
    )

(ROOT / "PACKAGE_SHA256.json").write_text(
    json.dumps(records, indent=2) + "\n",
    encoding="utf-8",
)

