# RUN_BENCHMARK.ps1 - Launch the Ascend Benchmark Mission
#
# Usage (PowerShell, from inside this folder):
#   .\RUN_BENCHMARK.ps1                 # full-auto, session effort = MAX
#   .\RUN_BENCHMARK.ps1 -Mode guarded   # enforced guardrails, a few one-time prompts
#   .\RUN_BENCHMARK.ps1 -Resume         # continue an interrupted run from disk state
#
# If blocked:  powershell -ExecutionPolicy Bypass -File .\RUN_BENCHMARK.ps1

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
    Write-Host 'Run this script from the 02_Ascend_Benchmark_Mission_2026-07 folder.' -ForegroundColor Red
    exit 1
}

# --- Sync prior corpus from the sibling lab folder ---------------------------
$lab = Join-Path (Split-Path $PSScriptRoot -Parent) '01_Market_Learning_Lab_2026-07'
$dst = Join-Path $PSScriptRoot '00_PRIOR_CORPUS'
New-Item -ItemType Directory -Force -Path $dst | Out-Null
if (Test-Path $lab) {
    Write-Host "Syncing lab corpus from: $lab"
    $pairs = @(
        @{ src = '10_RESEARCH\RB_01_huawei_computing_business.md'; dst = 'RB_01_huawei_computing_business.md' },
        @{ src = '10_RESEARCH\RB_02_ascend_supply_chain_map.md';   dst = 'RB_02_ascend_supply_chain_map.md' },
        @{ src = '30_FINDINGS\WATCHLIST.csv';                      dst = 'WATCHLIST.csv' },
        @{ src = '90_SOURCES\sources.json';                        dst = 'lab_sources.json' }
    )
    foreach ($p in $pairs) {
        $s = Join-Path $lab $p.src
        if (Test-Path $s) { Copy-Item $s (Join-Path $dst $p.dst) -Force }
        else { Write-Host "  (missing, skipped: $($p.src))" -ForegroundColor DarkYellow }
    }
} else {
    Write-Host 'Lab folder not found next to this one - using the shipped copies in 00_PRIOR_CORPUS.' -ForegroundColor Yellow
}

# --- Effort policy: MAX for the session ---------------------------------------
$env:CLAUDE_CODE_EFFORT_LEVEL = 'max'

# --- Prompt --------------------------------------------------------------------
if ($Resume) {
    $prompt = 'Resume the Ascend Benchmark Mission: read CLAUDE.md and 05_STATE/MASTER_STATE.json, then continue from the first incomplete phase per 01_MISSION/MISSION_BRIEF.md. Do not ask me questions. Enforce PAPER-ONLY, the NUMBER TRUTH RULE, and the answer-key spoiler boundary. Run until the mission is COMPLETE.'
} else {
    $prompt = (Get-Content -Raw '.\KICKOFF_PROMPT.txt').Trim()
}

# --- Permission flags ------------------------------------------------------------
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

Write-Host ("Model: {0} | Session effort: MAX | Bulk workers pinned to sonnet | Dir: {1}" -f $Model, (Get-Location).Path)
Write-Host 'Budget note: orchestrator/red-team draw on the weekly Fable pool; workers on the all-models pool.'
Write-Host 'A full run takes hours across 1-2 session windows; if it stops (session/weekly limit, sleep, crash): re-run with -Resume.'
Write-Host 'AFTER the run: do NOT open 30_ or 40_ until you have written your own attempt (see README self-test protocol).'
Write-Host '--------------------------------------------------------------------------------'

& claude @permArgs --model $Model $prompt
