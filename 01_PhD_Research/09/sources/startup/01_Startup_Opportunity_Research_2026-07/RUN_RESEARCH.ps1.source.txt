# RUN_RESEARCH.ps1 - Launch the autonomous startup research mission in Claude Code
#
# Usage (from PowerShell, inside this folder):
#   .\RUN_RESEARCH.ps1                 # full-auto (zero prompts; uses --dangerously-skip-permissions)
#   .\RUN_RESEARCH.ps1 -Mode guarded   # near-zero prompts, safer (acceptEdits + project allow-list)
#   .\RUN_RESEARCH.ps1 -Resume         # continue an interrupted run (state files pick up where it left off)
#   .\RUN_RESEARCH.ps1 -Model fable    # override the model id if needed
#
# If script execution is blocked, run once:
#   powershell -ExecutionPolicy Bypass -File .\RUN_RESEARCH.ps1

param(
    [ValidateSet('full', 'guarded')]
    [string]$Mode = 'full',
    [switch]$Resume,
    [string]$Model = 'claude-fable-5'
)

$ErrorActionPreference = 'Stop'
Set-Location -Path $PSScriptRoot

# --- Preflight -------------------------------------------------------------
$claude = Get-Command claude -ErrorAction SilentlyContinue
if (-not $claude) {
    Write-Host 'Claude Code is not installed (or not on PATH).' -ForegroundColor Red
    Write-Host 'Install it, then re-run this script:' -ForegroundColor Yellow
    Write-Host '    irm https://claude.ai/install.ps1 | iex'
    Write-Host 'Then run  claude  once in any folder to log in with your Max account.'
    exit 1
}

if (-not (Test-Path '.\KICKOFF_PROMPT.txt')) {
    Write-Host 'KICKOFF_PROMPT.txt not found - run this script from the research folder.' -ForegroundColor Red
    exit 1
}

# --- Build the prompt -------------------------------------------------------
if ($Resume) {
    $prompt = 'Resume the autonomous research mission: read CLAUDE.md and 05_STATE/MASTER_STATE.json, then continue from the first incomplete phase per 01_MISSION/MISSION_BRIEF.md. Do not ask me questions. Run until the mission is COMPLETE.'
} else {
    $prompt = (Get-Content -Raw '.\KICKOFF_PROMPT.txt').Trim()
}

# --- Permission flags -------------------------------------------------------
if ($Mode -eq 'full') {
    $permArgs = @('--dangerously-skip-permissions')
    Write-Host ''
    Write-Host 'MODE: FULL AUTO - Claude Code will run with ALL permission checks disabled' -ForegroundColor Yellow
    Write-Host '(--dangerously-skip-permissions). It is instructed to stay inside this folder,'
    Write-Host 'but nothing technically stops a bypassed session from touching other files.'
    Write-Host 'Use -Mode guarded if you prefer enforced guardrails with occasional prompts.'
    Write-Host ''
} else {
    $permArgs = @('--permission-mode', 'acceptEdits')
    Write-Host ''
    Write-Host 'MODE: GUARDED - acceptEdits + the allow-list in .claude\settings.json.' -ForegroundColor Green
    Write-Host 'Expect at most a few one-time prompts (approve with "a"/"always allow").'
    Write-Host ''
}

# --- Launch -----------------------------------------------------------------
Write-Host ("Model: {0}   |   Working dir: {1}" -f $Model, (Get-Location).Path)
Write-Host 'Starting Claude Code... (leave this window open; a full run takes several hours)'
Write-Host 'If the run stops for any reason (rate limit, sleep, crash): re-run with -Resume'
Write-Host '--------------------------------------------------------------------------------'

# A fresh session is the most robust resume: state files carry everything.
& claude @permArgs --model $Model $prompt
