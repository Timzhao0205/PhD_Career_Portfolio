# PhD_Career_Portfolio

Yiming "Tim" Zhao — Stanford EE PhD (Senesky group). Three tracks, kept
separate on purpose.

| Folder | What lives there | Index |
|---|---|---|
| `01_PhD_Research/` | GaN Hall-effect magnetic sensing for fusion diagnostics in the HSX stellarator: the experimental line, its publications, and the analysis packages built around it. | `01_PhD_Research_Folder_Info.md` |
| `02_Startup/` | Venture research — five rounds of searching for a company to found around 2029–2030 — plus two hands-on technical projects spun out of it. | `02_Startup_Folder_Info.md` |
| `03_Investments_and_Finance/` | Market learning lab and equity benchmarking missions. | — |

## Conventions

Two-digit prefixes order folders at every level, and the same numbering runs
inside each project: `01_` mission, `05_`/`80_` durable state, `90_` sources,
`98_` run metrics, `99_` audit.

Most numbered folders are self-contained Claude Code packages with their own
binding `CLAUDE.md`, a `00_README_START_HERE.md`, and `.claude/agents/`. Launch
`claude` from the package folder, not from here, so its rules and agents load.

Markdown is the source of truth everywhere. `.html` files are generated mirrors
— regenerate rather than edit them.

## Two things worth knowing about

- **`02_Startup/00_SOURCE_DATABASE/`** — every source any startup round ever
  gathered, 3,432 of them, merged into one queryable database with full
  provenance. Search it before starting new research.
- **Snapshot folders.** Two run packages vendored full copies of research that
  already lives elsewhere in this repository. Those copies were removed and
  replaced by a manifest and a `rehydrate.py` that rebuilds them on demand:
  `01_PhD_Research/09_PAP06_Career_Portfolio_Synthesis_2026-07/sources/` and
  `02_Startup/07_Frontier_Ideas_Interactive_2026-07/src/06/`. Each has a README.

`REORGANIZATION_2026-08.md` records the 2026-08-08 cleanup that produced the
current layout.
