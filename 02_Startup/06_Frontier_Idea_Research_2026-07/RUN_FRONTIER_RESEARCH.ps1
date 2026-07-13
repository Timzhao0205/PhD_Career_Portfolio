param(
    [switch]$Resume,
    [string]$CriticalModel = 'claude-fable-5',
    [string]$ScoutModel = 'claude-sonnet-5',
    [ValidateSet('high','xhigh')][string]$CriticalEffort = 'xhigh',
    [double]$MaxBudgetUSD = 0,
    [switch]$SkipModelProbe
)

$ErrorActionPreference = 'Stop'
Set-Location -Path $PSScriptRoot
$root = (Get-Location).Path

if ($CriticalModel -notmatch '^[A-Za-z0-9._-]+$' -or $ScoutModel -notmatch '^[A-Za-z0-9._-]+$') {
    throw 'Model names may contain only letters, digits, dot, underscore, and hyphen.'
}

if (-not (Get-Command claude -ErrorAction SilentlyContinue)) {
    Write-Host 'Claude Code is not installed or not on PATH.' -ForegroundColor Red
    Write-Host 'Install: irm https://claude.ai/install.ps1 | iex; then run claude once to log in.'
    exit 1
}

$required = @('CLAUDE.md','KICKOFF_PROMPT.txt','01_MISSION/MISSION_BRIEF.md','tools/validate_mission.py','.claude/agents/india-origin-auditor.md','.claude/agents/idea-elegance-judge.md')
foreach ($path in $required) {
    if (-not (Test-Path $path)) { throw "Missing required package file: $path" }
}

New-Item -ItemType Directory -Force -Path '.\98_RUN_LOGS' | Out-Null
$stamp = Get-Date -Format 'yyyyMMdd_HHmmss'
$transcript = ".\98_RUN_LOGS\claude_$stamp.jsonl"
$launcherLog = '.\98_RUN_LOGS\LAUNCHER_LOG.md'
$modelLog = '.\98_RUN_LOGS\MODEL_ROUTING_LOG.jsonl'
$version = (& claude --version 2>&1 | Out-String).Trim()

function Add-RouteLog([string]$phase,[string]$task,[string]$requested,[string]$effort,[string]$reason,[bool]$downgrade,[string]$status) {
    $record = [ordered]@{
        timestamp=(Get-Date).ToUniversalTime().ToString('o'); phase=$phase; task=$task
        requested_model=$requested; actual_model=$requested; effort=$effort; reason=$reason
        downgrade=$downgrade; status=$status; source='launcher'
    } | ConvertTo-Json -Compress
    Add-Content -Encoding utf8 -Path $modelLog -Value $record
}

$sourceAgentFiles = @(
    '.claude/agents/lane-scout.md', '.claude/agents/source-verifier.md',
    '.claude/agents/demand-competitor-analyst.md', '.claude/agents/source-auditor.md',
    '.claude/agents/geography-analyst.md', '.claude/agents/india-origin-auditor.md'
)
foreach ($agentFile in $sourceAgentFiles) {
    $body = Get-Content -Raw $agentFile
    $body = $body -replace '(?m)^model: .*$', "model: $ScoutModel"
    Set-Content -Encoding utf8 -Path $agentFile -Value $body
}

$criticalOverride = ($CriticalModel -ne 'claude-fable-5') -or ($CriticalEffort -ne 'xhigh')
$scoutOverride = $ScoutModel -ne 'claude-sonnet-5'
$scoutDowngrade = $ScoutModel -notin @('claude-sonnet-5','claude-fable-5')
Add-RouteLog 'launch' 'orchestrator' $CriticalModel $CriticalEffort 'Critical reasoning and synthesis' $criticalOverride 'configured'
Add-RouteLog 'launch' 'source-agents' $ScoutModel 'high/medium' 'High-volume discovery and verification' $scoutDowngrade 'configured'

@"

## $((Get-Date).ToString('o'))
- Claude Code: $version
- Root: $root
- Resume: $Resume
- Critical: $CriticalModel / $CriticalEffort
- Scout: $ScoutModel / high-medium
- Critical override from Fable 5: $criticalOverride
- Scout override from Sonnet 5: $scoutOverride
- Transcript: $transcript
"@ | Add-Content -Encoding utf8 -Path $launcherLog

if (-not $SkipModelProbe) {
    foreach ($probe in @(@($CriticalModel,$CriticalEffort,'critical'), @($ScoutModel,'low','scout'))) {
        Write-Host "Probing $($probe[2]) model $($probe[0])..."
        $reply = & claude -p --model $probe[0] --effort $probe[1] --max-turns 1 'Reply with exactly MODEL_OK.' 2>&1 | Out-String
        if ($LASTEXITCODE -ne 0 -or $reply -notmatch 'MODEL_OK') {
            Add-RouteLog 'launch' "probe-$($probe[2])" $probe[0] $probe[1] 'Availability probe' $false 'failed'
            throw "Model probe failed for $($probe[0]). No fallback was attempted. Output: $reply"
        }
        Add-RouteLog 'launch' "probe-$($probe[2])" $probe[0] $probe[1] 'Availability probe' $false 'passed'
    }
}

$env:FRONTIER_CRITICAL_MODEL = $CriticalModel
$env:FRONTIER_SCOUT_MODEL = $ScoutModel
$env:FRONTIER_CRITICAL_EFFORT = $CriticalEffort
$env:CLAUDE_CODE_EFFORT_LEVEL = $CriticalEffort
$env:CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS = '0'
$env:CLAUDE_CODE_RETRY_WATCHDOG = '1'

if ($Resume) {
    $prompt = 'Resume the frontier mission. Read CLAUDE.md, 01_MISSION/MISSION_BRIEF.md, 05_STATE/PRE_P3_INDIA_SOURCE_AUDIT_DIRECTIVE.md, 05_STATE/INDIA_SOURCE_ORIGIN_AUDIT_QUEUE.json, 05_STATE/2030_COMPANY_LAUNCH_PATCH_2026-07-12.md, 05_STATE/P3_US_CHINA_WEIGHTING_PATCH_2026-07-12.md, and 05_STATE/MASTER_STATE.json. P2A blocks P3: complete all 12 origin-audit batches, quarantine India-origin sources, allow mixed academic papers only with a verified non-Indian co-author affiliation, independently confirm derivative claims, repair ATLAS, search eligible replacements if any gate fails, and require machine plus Fable 5/xhigh P2A PASS. Then regenerate >=80 P3R2 seeds using Fable 5/xhigh, US/China dominant and JP/TW/KR optional. Company launch is 2030: every seed needs current TRL, 2026-2029 pre-company preparation, a named 2030-2034 demand trigger, expected 2030 competition, window-risk analysis, and a readiness kill date; reject windows that close before 2030 or mature after 2034. Run the independent Fable 5/xhigh elegance judge. Reuse durable technical sources but refresh mutable market/policy/price/competitor evidence. Preserve SEEDS_A-D only as drafts, log routing, ask no questions, and run until COMPLETE and PASS.'
} else {
    $prompt = (Get-Content -Raw '.\KICKOFF_PROMPT.txt').Trim()
}

$args = @(
    '-p', '--model', $CriticalModel, '--effort', $CriticalEffort,
    '--permission-mode', 'dontAsk', '--output-format', 'stream-json', '--verbose',
    '--name', 'frontier-idea-research', $prompt
)
if ($MaxBudgetUSD -gt 0) { $args = $args[0..($args.Count-2)] + @('--max-budget-usd', $MaxBudgetUSD.ToString([Globalization.CultureInfo]::InvariantCulture), $prompt) }

Write-Host "Starting autonomous run: $CriticalModel/$CriticalEffort" -ForegroundColor Green
Write-Host "Raw transcript: $transcript"
Write-Host 'If interrupted, run .\RUN_FRONTIER_RESEARCH.ps1 -Resume'

& claude @args 2>&1 | Tee-Object -FilePath $transcript
$exitCode = $LASTEXITCODE
@"
- Exit: $exitCode at $((Get-Date).ToString('o'))
"@ | Add-Content -Encoding utf8 -Path $launcherLog

if ($exitCode -ne 0) {
    Write-Host "Claude exited with code $exitCode. Resume after addressing the logged error." -ForegroundColor Yellow
    exit $exitCode
}

& python .\tools\validate_mission.py
if ($LASTEXITCODE -ne 0) {
    Write-Host 'Claude stopped, but the mission validator is not yet PASS. Run with -Resume.' -ForegroundColor Yellow
    exit 2
}
Write-Host 'Mission validator PASS. Open 60_FINAL_PORTFOLIO\00_EXECUTIVE_PORTFOLIO.md' -ForegroundColor Green
