# RUN_STRATEGY.ps1 - Launch Round 3 (C12+C10 Strategy, Competitors & Patent Whitespace)
#
# Usage (PowerShell, from inside this folder):
#   .\RUN_STRATEGY.ps1                 # full-auto, session effort = MAX
#   .\RUN_STRATEGY.ps1 -Mode guarded   # enforced guardrails, a few one-time prompts
#   .\RUN_STRATEGY.ps1 -Resume         # continue an interrupted run from disk state
#
# If blocked:  powershell -ExecutionPolicy Bypass -File .\RUN_STRATEGY.ps1

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
    Write-Host 'Run this script from the 03_C12_C10_Strategy_IP_2026-07 folder.' -ForegroundColor Red
    exit 1
}

# --- Sync prior corpus from the sibling Round-2 folder -----------------------
$r2 = Join-Path (Split-Path $PSScriptRoot -Parent) '02_Novel_Lanes_Research_2026-07'
$dst = Join-Path $PSScriptRoot '00_PRIOR_CORPUS'
New-Item -ItemType Directory -Force -Path (Join-Path $dst 'DEEPDIVES') | Out-Null
if (Test-Path $r2) {
    Write-Host "Syncing Round-2 outputs from: $r2"
    $pairs = @(
        '60_FINAL_SYNTHESIS\00_FINAL_SHOWDOWN.md',
        '60_FINAL_SYNTHESIS\01_ROADMAP_IMPLICATIONS.md',
        '60_FINAL_SYNTHESIS\INCUMBENTS.md',
        '50_POLICY_DELTA\POLICY_DELTA.md'
    )
    foreach ($p in $pairs) {
        $src = Join-Path $r2 $p
        if (Test-Path $src) { Copy-Item $src $dst -Force }
        else { Write-Host "  (missing, skipped: $p)" -ForegroundColor DarkYellow }
    }
    $dd = Join-Path $r2 '00_PRIOR_CORPUS\GEN3\DEEPDIVES'
    foreach ($n in @('DD_C12_hts_winding_machines.md','DD_C12_sources.json',
                     'DD_C10_magnet_power_converters.md','DD_C10_sources.json',
                     'DD_C11_hts_quench_protection.md','DD_C11_sources.json',
                     'DD_C33_hts_coil_qc_instruments.md','DD_C33_sources.json')) {
        $src = Join-Path $dd $n
        if (Test-Path $src) { Copy-Item $src (Join-Path $dst 'DEEPDIVES') -Force }
        else { Write-Host "  (missing, skipped: DEEPDIVES\$n)" -ForegroundColor DarkYellow }
    }
} else {
    Write-Host 'Round-2 folder not found next to this one - using the shipped copies in 00_PRIOR_CORPUS.' -ForegroundColor Yellow
}

# --- Effort policy: MAX for the session; patent-scout/auditor pinned high ----
$env:CLAUDE_CODE_EFFORT_LEVEL = 'max'

# --- Prompt ------------------------------------------------------------------
if ($Resume) {
    $prompt = 'Resume Round 3: read CLAUDE.md and 05_STATE/MASTER_STATE.json, then continue from the first incomplete phase per 01_MISSION/MISSION_BRIEF_V3.md. Do not ask me questions. Enforce the PATENT TRUTH RULE and the Stanford/UIUC wall. Run until the mission is COMPLETE.'
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

Write-Host ("Model: {0} | Session effort: MAX (patent-scout/auditor pinned high) | Dir: {1}" -f $Model, (Get-Location).Path)
Write-Host 'A full run takes hours; if it stops (weekly limit, sleep, crash): re-run with -Resume.'
Write-Host '--------------------------------------------------------------------------------'

& claude @permArgs --model $Model $prompt
