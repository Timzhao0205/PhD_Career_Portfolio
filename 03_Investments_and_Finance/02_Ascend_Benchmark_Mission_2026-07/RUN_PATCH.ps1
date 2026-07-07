# RUN_PATCH.ps1 - Launch the Accuracy Patch (+5 names, Fable critical review of all)
#
# Usage (PowerShell, from inside the 02_Ascend_Benchmark_Mission_2026-07 folder):
#   .\RUN_PATCH.ps1                 # full-auto
#   .\RUN_PATCH.ps1 -Mode guarded   # enforced guardrails
#   .\RUN_PATCH.ps1 -Resume         # continue an interrupted patch from disk state
#
# If blocked:  powershell -ExecutionPolicy Bypass -File .\RUN_PATCH.ps1

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
    exit 1
}
if (-not (Test-Path '.\KICKOFF_PATCH.txt')) {
    Write-Host 'Run this script from the 02_Ascend_Benchmark_Mission_2026-07 folder (patch files merged in).' -ForegroundColor Red
    exit 1
}
if (-not (Test-Path '.\05_STATE\MASTER_STATE.json')) {
    Write-Host 'v1 mission state not found - the patch amends a COMPLETE v1 run.' -ForegroundColor Red
    exit 1
}
$state = Get-Content -Raw '.\05_STATE\MASTER_STATE.json' | ConvertFrom-Json
if ($state.mission -ne 'COMPLETE') {
    Write-Host ("v1 mission is '{0}', not COMPLETE - finish or resume v1 first (RUN_BENCHMARK.ps1 -Resume)." -f $state.mission) -ForegroundColor Red
    exit 1
}

# --- Effort policy ------------------------------------------------------------
$env:CLAUDE_CODE_EFFORT_LEVEL = 'max'

# --- Prompt --------------------------------------------------------------------
if ($Resume) {
    $prompt = 'Resume the Accuracy Patch: read CLAUDE.md, 01_MISSION/PATCH_BRIEF.md and 05_STATE/PATCH_STATE.json, then continue from the first incomplete patch phase, honoring the F4 fallback priority order. Do not ask me questions. Enforce PAPER-ONLY, the NUMBER TRUTH RULE, the spoiler boundary, and the FABLE-FRUGALITY rules. Run until PATCH_STATE.json reads patch COMPLETE.'
} else {
    $prompt = (Get-Content -Raw '.\KICKOFF_PATCH.txt').Trim()
}

# --- Permission flags ------------------------------------------------------------
if ($Mode -eq 'full') {
    $permArgs = @('--dangerously-skip-permissions')
    Write-Host ''
    Write-Host 'MODE: FULL AUTO (all permission checks disabled for this session).' -ForegroundColor Yellow
} else {
    $permArgs = @('--permission-mode', 'acceptEdits')
    Write-Host ''
    Write-Host 'MODE: GUARDED (acceptEdits + .claude\settings.json allow-list).' -ForegroundColor Green
}

Write-Host ("Model: {0} | Effort: MAX | Fable = judgment (reviews/red-team/synthesis), Sonnet = gathering | Dir: {1}" -f $Model, (Get-Location).Path)
Write-Host 'Batched SAFE-STOP checkpoints every 4 reviews; if a session/weekly cap hits: re-run with -Resume.'
Write-Host 'Spoiler boundary unchanged: do not open 30_/40_ mid-run if you have not done the blind attempt.'
Write-Host '--------------------------------------------------------------------------------'

& claude @permArgs --model $Model $prompt
