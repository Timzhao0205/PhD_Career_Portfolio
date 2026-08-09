# HSX IP/arXiv review — native Claude Code package

This is a self-contained, publication-only research package. It launches the
native Claude Code interface from Windows PowerShell, requests Claude Fable 5 at
xhigh effort for the parent and critical judgment stages, assigns Sonnet 5 to
cost-efficient support stages, and saves checkpoints after every stage.

It does **not** inherit state, outputs, source counts, or errors from any earlier
package. The large PhD and startup archives are intentionally excluded because
the task is limited to technologies actually disclosed in this manuscript.

## Recommended setup

1. Extract this folder to a short local path, preferably `C:\HSX_IP` or
   `D:\HSX_IP`. Do not run it from inside the ZIP.
2. Open **Windows PowerShell** in that extracted folder.
3. If native Claude Code is not installed, run once:

   ```powershell
   irm https://claude.ai/install.ps1 | iex
   ```

4. If you have never signed in, run `claude` once and complete authentication.
5. Begin or resume with the same single command:

   ```powershell
   powershell -NoProfile -ExecutionPolicy Bypass -File .\START.ps1
   ```

`START.ps1` performs a deterministic preflight, opens the interactive Claude
Code interface, and uses a named session. On later runs it resumes from
`state/STATE.json` and the latest checkpoint.

## Permission warning

The command uses `--dangerously-skip-permissions` because full read/write access
was requested. Native Windows does not sandbox this mode. The project rules tell
Claude to work only in this folder, but the operating-system permission is
broader. Use a dedicated folder and do not place credentials or unrelated
sensitive files beside it. Claude Code may display its own one-time confirmation
the first time bypass mode is used; a project cannot suppress that safeguard.

## Model integrity

- Parent/orchestrator: Fable 5 / xhigh.
- Critical IP, UHV/GDC, red-team, and final stages: Fable 5 / xhigh.
- Structured extraction and source-heavy stages: Sonnet 5 at medium to xhigh.
- Automatic model switching on a safety flag is disabled.
- A first Fable flag is quarantined and retried once with a narrower benign
  prompt; a second pauses with a durable checkpoint.
- No provider or model substitution is silently accepted.

See `MODEL_PLAN.md` for the full table. Actual model, effort, duration, turns,
tokens, web activity, and cost are logged only when Claude Code exposes them;
unknown values are recorded as `not_exposed` rather than guessed.

## Intended outputs

The main decision documents will appear under `outputs`:

- `70_FINAL_OTL_BRIEF.md`
- `70_EXEC_SUMMARY.md`
- `70_MODEL_REPORT.md`
- `50_ARXIV_RISK.md`
- `40_UHV_PACKAGE_VERDICT.md`

The workflow performs research and drafts only. It does not file a patent,
contact Stanford OTL or counsel, modify the submitted manuscript, or upload to
arXiv.

## If interrupted

Run the same command again. Do not delete `state`, `outputs`, or `.claude`.
Consult `RESUME.md` only if the workflow explicitly writes `state/PAUSE.md`.
