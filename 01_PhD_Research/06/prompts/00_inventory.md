# Stage 00 — authoritative inventory and requirements trace

Build the factual baseline before conducting literature research.

Inspect at minimum:

- every file under `inputs/`;
- `../01_Publications/submitted/regular_lsens/regular_lsens.tex` and its PDF;
- the extracted `../07_HSX_august2025_results/` tree, including file types,
  shot coverage, scripts, figures, and obvious metadata;
- `../02_HSX_Hall_Sensor_Readout/`;
- `../03_HSX_Vector_Probe_RSI2026/`;
- relevant prior review outputs in
  `../04_Magnetic_Sensor_Review_Sensors2026/`;
- the package/design work in `../05_HSX_ChatGPT_Windows_App/`;
- the parent root `CLAUDE.md` and folder index.

Do not run a broad literature search in this stage.

Create:

1. `outputs/00_INPUT_INVENTORY.md`
   - inventory by evidence group, not a noisy listing of every scope CSV;
   - authoritative path, date/identity, what it can establish, what it cannot
     establish, and any readability/format limitation;
   - manuscript section/figure/table map;
   - decision-letter editor/reviewer map;
   - HSX data/shot/script map;
   - prior-project outputs that may be reused only after verification.
2. `outputs/00_REQUIREMENTS_TRACE.csv`
   - exact header:
     `requirement_id,user_requirement,acceptance_test,planned_stage,planned_output,status,notes`
   - trace every numbered mission item, source minimum, model safeguard,
     one-command resume, low-cleanroom preference, two-year graduation goal,
     startup goal, manuscript options, and pre-publication IP screen.
3. `outputs/00_CONFLICT_LEDGER.md`
   - explicitly address the parent claim that the paper was “published in
     2023” versus the 23-Jul-2026 decline letter;
   - record every material contradiction or ambiguity without deciding by
     convenience;
   - name the controlling evidence or label the issue unresolved.
4. `outputs/00_CLAIM_BASELINE.csv`
   - exact header:
     `claim_id,claim,classification,evidence_path,evidence_locator,status,confidence,notes`
   - classifications: `supplied_fact`, `prior_project_claim`,
     `measured_value`, `inference`, `proposal`, `unknown`;
   - include all material claims currently made in the manuscript abstract,
     novelty/contribution text, calibration/bandwidth claims, shot-count
     claims, and core project trajectory.

Acceptance checks:

- Every uploaded evidence group is represented.
- Reviewer 1, Reviewer 2, the Associate Editor, and the decision outcome are
  separately represented.
- The known publication-status conflict is not buried or resolved without
  proof.
- No measured value is silently altered.
- The inventory states which raw files are sufficient for quantitative
  re-analysis and which are not.

Next stage: `10a_literature_gan`.
