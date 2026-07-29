# RUN_RESEARCH.ps1 - Launch Round 2 (Novel Lanes & Final Showdown) in Claude Code
#
# Usage (PowerShell, from inside this folder):
#   .\RUN_RESEARCH.ps1                 # full-auto, session effort = MAX (your requested policy)
#   .\RUN_RESEARCH.ps1 -Mode guarded   # enforced guardrails, a few one-time prompts
#   .\RUN_RESEARCH.ps1 -Resume         # continue an interrupted run from disk state
#
# If blocked:  powershell -ExecutionPolicy Bypass -File .\RUN_RESEARCH.ps1

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
    Write-Host 'Install:  irm https://claude.ai/install.ps1 | iex   then run `claude` once to log in.'
    exit 1
}
if (-not (Test-Path '.\KICKOFF_PROMPT.txt')) {
    Write-Host 'Run this script from the 02_Novel_Lanes_Research_2026-07 folder.' -ForegroundColor Red
    exit 1
}

# --- Sync Round-1 finals into 00_PRIOR_CORPUS/GEN3 --------------------------
$gen3src = Join-Path (Split-Path $PSScriptRoot -Parent) '01_Startup_Opportunity_Research_2026-07'
$gen3dst = Join-Path $PSScriptRoot '00_PRIOR_CORPUS\GEN3'
New-Item -ItemType Directory -Force -Path $gen3dst | Out-Null
if (Test-Path $gen3src) {
    Write-Host "Syncing Round-1 outputs from: $gen3src"
    $pairs = @(
        @('60_PHASE6_SYNTHESIS\*.md',            ''),
        @('50_PHASE5_POLICY\POLICY_BRIEF.md',    ''),
        @('50_PHASE5_POLICY\policy_sources.json',''),
        @('90_BIBLIOGRAPHY\sources.json',        'gen3_sources.json'),
        @('20_PHASE2_CANDIDATES\candidates.json',''),
        @('20_PHASE2_CANDIDATES\CANDIDATES.md',  ''),
        @('30_PHASE3_SCORING\SCORING_MATRIX.csv',''),
        @('30_PHASE3_SCORING\SELECTION.md',      ''),
        @('70_SATURATION_CHECK\SATURATION_REPORT.md',  ''),
        @('70_SATURATION_CHECK\ADJUDICATION_ANNEX.md', '')
    )
    foreach ($p in $pairs) {
        $src = Join-Path $gen3src $p[0]
        if (Test-Path $src) {
            if ($p[1] -ne '') { Copy-Item $src (Join-Path $gen3dst $p[1]) -Force }
            else              { Copy-Item $src $gen3dst -Force }
        } else { Write-Host "  (missing, skipped: $($p[0]))" -ForegroundColor DarkYellow }
    }
    New-Item -ItemType Directory -Force -Path (Join-Path $gen3dst 'DEEPDIVES') | Out-Null
    Copy-Item (Join-Path $gen3src '40_PHASE4_DEEPDIVES\*') (Join-Path $gen3dst 'DEEPDIVES') -Force -ErrorAction SilentlyContinue
} else {
    Write-Host "Round-1 folder not found next to this one - using the GEN3 files already shipped in 00_PRIOR_CORPUS\GEN3." -ForegroundColor Yellow
}

# --- Effort policy: MAX for the session; scouts/auditor pinned high ---------
# Env var makes max persist for this session (per Claude Code docs); the two
# source-gathering agents are pinned to `effort: high` in .claude\agents\*.md.
$env:CLAUDE_CODE_EFFORT_LEVEL = 'max'

# --- Prompt ------------------------------------------------------------------
if ($Resume) {
    $prompt = 'Resume Round 2: read CLAUDE.md and 05_STATE/MASTER_STATE.json, then continue from the first incomplete phase per 01_MISSION/MISSION_BRIEF_V2.md. Do not ask me questions. Run until the mission is COMPLETE.'
} else {
    $prompt = (Get-Content -Raw '.\KICKOFF_PROMPT.txt').Trim()
}

# --- Permission flags ----------------------------------------------------------
if ($Mode -eq 'full') {
    $permArgs = @('--dangerously-skip-permissions')
    Write-Host ''
    Write-Host 'MODE: FULL AUTO (all permission checks disabled for this session).' -ForegroundColor Yellow
    Write-Host 'CLAUDE.md confines the mission to this folder by instruction, not OS enforcement.'
    Write-Host 'Use -Mode guarded for enforced guardrails with a few one-time prompts.'
} else {
    $permArgs = @('--permission-mode', 'acceptEdits')
    Write-Host ''
    Write-Host 'MODE: GUARDED (acceptEdits + .claude\settings.json allow-list).' -ForegroundColor Green
}

Write-Host ("Model: {0} | Session effort: MAX (scouts/auditor pinned high) | Dir: {1}" -f $Model, (Get-Location).Path)
Write-Host 'A full run takes hours; if it stops (weekly limit, sleep, crash): re-run with -Resume.'
Write-Host '--------------------------------------------------------------------------------'

& claude @permArgs --model $Model $prompt
