<#
  RUN.ps1 - one command to run the HSX readout + packaging review autonomously on Fable 5.
  Windows PowerShell. You are already logged into Claude Code.
  NOTE: keep this file ASCII-only. Windows PowerShell 5.1 reads no-BOM scripts as ANSI, so
  smart dashes / curly quotes break parsing. Plain - and " only.

  USAGE (from this folder):
      .\RUN.ps1                 # default: zero-prompt autonomous run on Fable 5
      .\RUN.ps1 -Resume         # continue from 05_STATE/MASTER_STATE.json
      .\RUN.ps1 -Mode guarded   # enforce the .claude allow-list (a few one-time 'a'=always approvals)

  If PowerShell blocks the script:
      powershell -ExecutionPolicy Bypass -File .\RUN.ps1
#>

param(
  [ValidateSet('full','guarded')] [string]$Mode = 'full',
  [switch]$Resume
)

$ErrorActionPreference = 'Stop'
Set-Location -Path $PSScriptRoot

# --- sanity checks ---
if (-not (Get-Command claude -ErrorAction SilentlyContinue)) {
  Write-Error "Claude Code CLI 'claude' not found on PATH. Install it and log in, then re-run."
}
if (-not (Test-Path .\KICKOFF_PROMPT.txt)) {
  Write-Error "KICKOFF_PROMPT.txt missing - run this from the pack root folder."
}

# --- optional: CAD tools for ST8 visuals (harmless if already present) ---
if (-not (Get-Command openscad -ErrorAction SilentlyContinue)) {
  Write-Host "[setup] OpenSCAD not found; attempting winget install (for ST8 renders)..." -ForegroundColor Yellow
  try {
    winget install --id OpenSCAD.OpenSCAD -e --silent --accept-source-agreements --accept-package-agreements
  } catch {
    Write-Host "[setup] OpenSCAD install skipped; the run will pip-install build123d or fall back to SVG diagrams." -ForegroundColor Yellow
  }
}

# --- build the initial message ---
if ($Resume) {
  $prompt = "Resume this run. Read CLAUDE.md and 05_STATE/MASTER_STATE.json, then continue from the first subtask not marked complete. Keep logging model/effort and progress."
} else {
  $prompt = Get-Content -Raw .\KICKOFF_PROMPT.txt
}

# --- permission flag ---
$permArgs = @()
if ($Mode -eq 'full') {
  $permArgs += '--dangerously-skip-permissions'
  Write-Host "[mode] full - zero prompts. This disables permission checks for the session; CLAUDE.md confines writes to this folder by instruction. Use -Mode guarded for enforced guardrails." -ForegroundColor Cyan
} else {
  Write-Host "[mode] guarded - the .claude allow-list is enforced. Press 'a' (always allow) on the first few prompts, then it runs hands-free." -ForegroundColor Cyan
}

Write-Host "[run] launching Claude Code on Fable 5 in $PSScriptRoot ..." -ForegroundColor Green
Write-Host "      Watch progress in 05_STATE\PROGRESS_LOG.md and the numbered output folders. Keep this window open." -ForegroundColor Green

# --- launch: orchestrator on Fable 5, seeded with the kickoff (or resume) ---
claude --model claude-fable-5 @permArgs $prompt

Write-Host ""
Write-Host "[done] session ended. If it stopped early (rate limit / sleep / closed window), run:  .\RUN.ps1 -Resume" -ForegroundColor Green
Write-Host "       Deliverables are under folders 10_ through 90_ ; sign-off items in 90_SYNTHESIS\DECISION_GATES.md" -ForegroundColor Green
