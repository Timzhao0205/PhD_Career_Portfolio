#requires -Version 5.1
[CmdletBinding()]
param(
    [switch]$RequireComplete
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot

$missionRoot = $PSScriptRoot
$researchRoot = Split-Path -Parent $missionRoot
$errors = @()

function Add-Error([string]$Message) {
    $script:errors += $Message
    Write-Host ("FAIL: {0}" -f $Message) -ForegroundColor Red
}

function Assert-File([string]$Base,[string]$Relative,[switch]$AllowEmpty) {
    $path = Join-Path $Base $Relative
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        Add-Error "Missing file: $Relative"
        return
    }
    if (-not $AllowEmpty -and (Get-Item -LiteralPath $path).Length -eq 0) {
        Add-Error "Empty file: $Relative"
    }
}

$rootFiles = @(
    'RUN_HYBRID_RADIATION_ANALYSIS.ps1',
    'README_HYBRID_RADIATION_ANALYSIS.md'
)
foreach ($file in $rootFiles) {
    Assert-File -Base $researchRoot -Relative $file
}

$missionFiles = @(
    'RUN_HYBRID_RADIATION_ANALYSIS.ps1',
    'INVOKE_CLAUDE_CHILD.ps1','TEST_CLAUDE_MODELS.ps1',
    'VALIDATE_PACKAGE.ps1','.claude\settings.json',
    'README_START.md','MISSION.md','AGENTS.md','CLAUDE.md',
    'EXECUTION_PLAN.md','MODEL_POLICY.md','SOURCE_POLICY.md',
    'CHECKPOINT_PROTOCOL.md','DECISION_FRAMEWORK.md',
    'LITERATURE_SEEDS.md','OFFICIAL_SETUP_REFERENCES.md',
    'PACKAGE_MANIFEST.md','PACKAGE_VALIDATION.md','RESUME_GUIDE.md',
    'prompts\_shared_system.md','prompts\00_inventory.md',
    'prompts\10a_literature_hybrid.md',
    'prompts\10b_literature_radiation.md',
    'prompts\10c_literature_applications.md',
    'prompts\10d_evidence_merge.md',
    'prompts\20_observability.md',
    'prompts\30_radiation_compensation.md',
    'prompts\40_applications_collaboration.md',
    'prompts\50_limitations_comparison.md',
    'prompts\60_research_program.md','prompts\70_redteam.md',
    'prompts\80_synthesis.md',
    'state\PROJECT_STATE.md','state\WORKLOG.md',
    'state\MODEL_EFFORT_LOG.csv','state\PERFORMANCE_LOG.csv',
    'state\SESSION_INDEX.csv','state\OPERATION_LOG.csv'
)
foreach ($file in $missionFiles) {
    Assert-File -Base $missionRoot -Relative $file
}
Assert-File -Base $missionRoot -Relative 'state\CLAUDE_EVENT_LOG.jsonl' `
    -AllowEmpty
Assert-File -Base $missionRoot -Relative 'logs\RUN_HISTORY.jsonl' -AllowEmpty

$scripts = @(
    (Join-Path $researchRoot 'RUN_HYBRID_RADIATION_ANALYSIS.ps1'),
    (Join-Path $missionRoot 'RUN_HYBRID_RADIATION_ANALYSIS.ps1'),
    (Join-Path $missionRoot 'INVOKE_CLAUDE_CHILD.ps1'),
    (Join-Path $missionRoot 'TEST_CLAUDE_MODELS.ps1'),
    (Join-Path $missionRoot 'VALIDATE_PACKAGE.ps1')
)
foreach ($scriptPath in $scripts) {
    if (-not (Test-Path -LiteralPath $scriptPath -PathType Leaf)) { continue }
    $tokens = $null
    $parseErrors = $null
    [System.Management.Automation.Language.Parser]::ParseFile(
        $scriptPath,[ref]$tokens,[ref]$parseErrors
    ) | Out-Null
    foreach ($parseError in @($parseErrors)) {
        Add-Error ("PowerShell parse error in {0}: {1}" -f
            (Split-Path -Leaf $scriptPath),$parseError.Message)
    }
}

try {
    $settings = Get-Content -Raw -LiteralPath (
        Join-Path $missionRoot '.claude\settings.json'
    ) | ConvertFrom-Json
    if ([string]$settings.model -ne 'sonnet' -or
        [string]$settings.effortLevel -ne 'high' -or
        -not [bool]$settings.disableClaudeAiConnectors) {
        Add-Error 'Project settings must be Sonnet/high with AI connectors disabled.'
    }
} catch {
    Add-Error 'Invalid .claude/settings.json.'
}

$runnerPath = Join-Path $missionRoot 'RUN_HYBRID_RADIATION_ANALYSIS.ps1'
$runner = if (Test-Path -LiteralPath $runnerPath) {
    Get-Content -Raw -LiteralPath $runnerPath
} else {
    ''
}

$routing = [ordered]@{
    '00_inventory'=@('sonnet','high')
    '10a_literature_hybrid'=@('sonnet','xhigh')
    '10b_literature_radiation'=@('sonnet','xhigh')
    '10c_literature_applications'=@('sonnet','high')
    '10d_evidence_merge'=@('fable','xhigh')
    '20_observability'=@('fable','xhigh')
    '30_radiation_compensation'=@('fable','xhigh')
    '40_applications_collaboration'=@('sonnet','xhigh')
    '50_limitations_comparison'=@('fable','xhigh')
    '60_research_program'=@('fable','xhigh')
    '70_redteam'=@('fable','xhigh')
    '80_synthesis'=@('fable','xhigh')
}
foreach ($stage in $routing.Keys) {
    $model = $routing[$stage][0]
    $effort = $routing[$stage][1]
    $pattern = "'" + [regex]::Escape($stage) +
        "'\s*=\s*@\{[\s\S]{0,500}?Model='" +
        [regex]::Escape($model) + "';\s*Effort='" +
        [regex]::Escape($effort) + "'"
    if ($runner -notmatch $pattern) {
        Add-Error "Incorrect or missing model route for $stage."
    }
}
if ([regex]::Matches(
    $runner,"Model='fable';\s*Effort='xhigh'"
).Count -ne 7) {
    Add-Error 'Exactly seven Fable/xhigh critical stages are required.'
}
if ($runner -notmatch '--permission-mode' -or
    $runner -notmatch 'bypassPermissions' -or
    $runner -notmatch '--safe-mode' -or
    $runner -notmatch 'MANUAL_CONTINUATION_REQUIRED') {
    Add-Error 'Runner lacks full-permission, safe retry, or manual-pause policy.'
}
if ($runner -notmatch 'PERFORMANCE_LOG\.csv' -or
    $runner -notmatch 'total_cost_usd' -or
    $runner -notmatch 'web_search_requests') {
    Add-Error 'Runner lacks required performance telemetry.'
}
if ($runner -match '(?i)\b(openai|codex)\s+exec\b') {
    Add-Error 'Runner contains an automatic alternate-provider invocation.'
}

$performanceHeader = (
    Get-Content -LiteralPath (
        Join-Path $missionRoot 'state\PERFORMANCE_LOG.csv'
    ) -First 1
).Trim()
$requiredPerformance = @(
    'timestamp','stage','attempt','requested_model','requested_effort',
    'duration_seconds','num_turns','input_tokens','output_tokens',
    'cache_read_input_tokens','cache_creation_input_tokens','total_cost_usd',
    'web_search_requests','web_fetch_requests','result_model','integrity',
    'verified_source_count','notes'
)
$actualPerformance = @($performanceHeader.Trim('"') -split '","')
if (($actualPerformance -join ',') -ne ($requiredPerformance -join ',')) {
    Add-Error 'PERFORMANCE_LOG.csv header is invalid.'
}

$priorLedger = Join-Path $researchRoot `
    '06\outputs\01_SOURCE_LEDGER.csv'
if (-not (Test-Path -LiteralPath $priorLedger -PathType Leaf)) {
    Add-Error 'Folder 06 source ledger is missing.'
} else {
    try {
        $priorRows = @(Import-Csv -LiteralPath $priorLedger)
        if (@($priorRows).Count -lt 100) {
            Add-Error 'Folder 06 source ledger is unexpectedly small.'
        }
    } catch {
        Add-Error 'Folder 06 source ledger cannot be parsed.'
    }
}
if (-not (Test-Path -LiteralPath (
    Join-Path $researchRoot '07_HSX_august2025_results'
) -PathType Container)) {
    Add-Error 'Folder 07 HSX context is missing.'
}

if ($RequireComplete) {
    $finalFiles = @(
        'outputs\FINAL_EXECUTIVE_DECISION.md',
        'outputs\FINAL_PLAIN_LANGUAGE_GUIDE.md',
        'outputs\FINAL_ACTION_PLAN.md',
        'outputs\FINAL_DELIVERABLE_INDEX.md',
        'outputs\FINAL_AUDIT.md',
        'outputs\01_SOURCE_LEDGER.csv',
        'outputs\01_NEW_SOURCE_AUDIT.csv'
    )
    foreach ($file in $finalFiles) {
        Assert-File -Base $missionRoot -Relative $file
    }
    $finalAudit = Join-Path $missionRoot 'outputs\FINAL_AUDIT.md'
    if (Test-Path -LiteralPath $finalAudit -PathType Leaf) {
        $last = (Get-Content -LiteralPath $finalAudit -Tail 1).Trim()
        if ($last -ne 'FINAL STATUS: PASS') {
            Add-Error "Final audit terminal line is '$last'."
        }
    }
    $finalLedger = Join-Path $missionRoot 'outputs\01_SOURCE_LEDGER.csv'
    if (Test-Path -LiteralPath $finalLedger -PathType Leaf) {
        try {
            $rows = @(Import-Csv -LiteralPath $finalLedger)
            $verified = @($rows | Where-Object {
                [string]$_.peer_review_status -eq 'verified_peer_reviewed'
            })
            if (@($verified).Count -lt 120) {
                Add-Error 'Final ledger has fewer than 120 verified peer-reviewed rows.'
            }
        } catch {
            Add-Error 'Final source ledger cannot be parsed.'
        }
    }
    $markers = Join-Path $missionRoot 'state\markers'
    if (-not (Test-Path -LiteralPath $markers -PathType Container) -or
        @(Get-ChildItem -LiteralPath $markers -Filter '*.done.json' -File).Count -lt 12) {
        Add-Error 'Fewer than twelve completion markers are present.'
    }
}

if (@($errors).Count -gt 0) {
    Write-Host ''
    Write-Host ("PACKAGE VALIDATION FAILED ({0} issue(s))." -f
        @($errors).Count) -ForegroundColor Red
    exit 1
}

Write-Host 'PASS: package structure, scripts, JSON, routing, full-permission mode, two-strike Fable policy, telemetry, and folder 06/07 context validated.' `
    -ForegroundColor Green
if ($RequireComplete) {
    Write-Host 'PASS: final artifacts, source total, markers, and terminal audit validated.' `
        -ForegroundColor Green
}
exit 0
