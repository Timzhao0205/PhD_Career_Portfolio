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

function Add-ValidationError([string]$Message) {
    $script:errors += $Message
    Write-Host ("FAIL: {0}" -f $Message) -ForegroundColor Red
}

function Assert-File([string]$Base,[string]$RelativePath) {
    $path = Join-Path $Base $RelativePath
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        Add-ValidationError "Missing file: $RelativePath"
        return
    }
    if ((Get-Item -LiteralPath $path).Length -eq 0 -and
        $RelativePath -notmatch 'CLAUDE_EVENT_LOG\.jsonl$') {
        Add-ValidationError "Empty file: $RelativePath"
    }
}

$rootRequired = @(
    'RUN_EVERYTHING.ps1','RUN_PHD_RESEARCH.ps1','README_START_HERE.md',
    'MODEL_ROUTING_TABLE.md','AGENTS.md','CHATGPT_WINDOWS_CONTINUE.md',
    'CHATGPT_WINDOWS_START_PROMPT.md','CLAUDE_ONLY_MIGRATION_2026-07-24.md',
    'RETRY_CLAUDE_AFTER_HANDOFF.md',
    'CLAUDE_RETRY_OVERRIDE_PATCH_2026-07-24.md',
    'FABLE_PRIMARY_POLICY_PATCH_2026-07-24.md',
    'VALIDATOR_PS51_HOTFIX_2026-07-24.md',
    'PACKAGE_TEST_REPORT_2026-07-24.md'
)
foreach ($file in $rootRequired) { Assert-File -Base $researchRoot -RelativePath $file }

$missionRequired = @(
    'README_START.md','MISSION.md','CLAUDE.md','AGENTS.md',
    'EXECUTION_PLAN.md','MODEL_POLICY.md','SOURCE_POLICY.md',
    'CHECKPOINT_PROTOCOL.md','PACKAGE_MANIFEST.md','PACKAGE_VALIDATION.md',
    'OFFICIAL_SETUP_REFERENCES.md','ENVIRONMENT_SETUP_MANIFEST.md',
    'RUN_PHD_RESEARCH.ps1','TEST_CLAUDE_MODELS.ps1',
    'INVOKE_CLAUDE_CHILD.ps1','VALIDATE_PACKAGE.ps1',
    'INPUT_CHECKSUMS.sha256','.claude\settings.json',
    'inputs\INPUT_NOTES.md','inputs\ORIGINAL_REQUEST.txt',
    'inputs\ORIGINAL_REQUEST_AND_SETUP.md',
    'inputs\Decision_Letter_IEEE_2026-07-23.pdf',
    'inputs\IEEE_submission_bundle_2026-07-02.pdf',
    'inputs\regular_lsens_original.zip',
    'inputs\07_HSX_august2025_results_original.zip',
    'prompts\_shared_system.md','prompts\00_inventory.md',
    'prompts\10a_literature_gan.md','prompts\10b_literature_fusion.md',
    'prompts\10c_literature_methods.md','prompts\10d_literature_merge.md',
    'prompts\20_direction.md','prompts\30_manuscript.md',
    'prompts\40_experiment.md','prompts\50_patent.md',
    'prompts\60_timeline.md','prompts\70_redteam.md',
    'prompts\80_synthesis.md',
    'state\PROJECT_STATE.md','state\WORKLOG.md',
    'state\MODEL_EFFORT_LOG.csv','state\SESSION_INDEX.csv',
    'state\OPERATION_LOG.csv','state\CLAUDE_EVENT_LOG.jsonl',
    'state\CHATGPT_HANDOFF_STATE.json','state\CHATGPT_HANDOFF.md',
    '_history\r0\README.md','_history\r0\RESET_MANIFEST.json'
)
foreach ($file in $missionRequired) {
    Assert-File -Base $missionRoot -RelativePath $file
}

$formerRuntimeFiles = @(
    ('CODEX' + '_MCP_CLIENT.ps1'),
    ('TEST_' + 'MCP_CONNECTION.ps1'),
    ('INVOKE_' + 'CODEX_EXEC_CHILD.ps1'),
    ('.mcp.' + 'codex.json'),
    ('state\runtime_' + 'mcp.json')
)
foreach ($file in $formerRuntimeFiles) {
    if (Test-Path -LiteralPath (Join-Path $missionRoot $file)) {
        Add-ValidationError "Removed runtime file is still present: $file"
    }
}
if (Test-Path -LiteralPath (
    Join-Path $researchRoot ('CODEX_' + 'RECOVERY_FIX_2026-07-24.md')
)) {
    Add-ValidationError 'Superseded recovery document is still present.'
}

$scripts = @(
    (Join-Path $researchRoot 'RUN_EVERYTHING.ps1'),
    (Join-Path $researchRoot 'RUN_PHD_RESEARCH.ps1'),
    (Join-Path $missionRoot 'RUN_PHD_RESEARCH.ps1'),
    (Join-Path $missionRoot 'TEST_CLAUDE_MODELS.ps1'),
    (Join-Path $missionRoot 'INVOKE_CLAUDE_CHILD.ps1'),
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
        Add-ValidationError ("PowerShell parse error in {0}: {1}" -f
            (Split-Path -Leaf $scriptPath),$parseError.Message)
    }
}

foreach ($jsonFile in @(
    '.claude\settings.json',
    'state\CHATGPT_HANDOFF_STATE.json'
)) {
    try {
        Get-Content -Raw -LiteralPath (Join-Path $missionRoot $jsonFile) |
            ConvertFrom-Json | Out-Null
    } catch {
        Add-ValidationError "Invalid JSON: $jsonFile"
    }
}

try {
    $settings = Get-Content -Raw -LiteralPath (
        Join-Path $missionRoot '.claude\settings.json'
    ) | ConvertFrom-Json
    if ([string]$settings.model -ne 'sonnet' -or
        [string]$settings.effortLevel -ne 'high') {
        Add-ValidationError 'Project defaults must be Sonnet/High.'
    }
} catch {}

try {
    $handoff = Get-Content -Raw -LiteralPath (
        Join-Path $missionRoot 'state\CHATGPT_HANDOFF_STATE.json'
    ) | ConvertFrom-Json
    if ([int]$handoff.schema_version -ne 2) {
        Add-ValidationError 'Handoff-state schema version is not 2.'
    }
    if ([bool]$handoff.flags.usage_limit_checked_by_runner -or
        [bool]$handoff.flags.inactivity_timeout_enabled) {
        Add-ValidationError 'Handoff flags incorrectly enable usage polling or inactivity timeout.'
    }
    if ([string]$handoff.chatgpt_windows.model -ne 'gpt-5.6-sol') {
        Add-ValidationError 'Handoff state does not map to GPT-5.6 Sol.'
    }
    if ([string]$handoff.model_policy_scope -ne 'fable_final_result_only' -or
        -not [bool]$handoff.flags.downgrade_tracking_fable_final_result_only -or
        -not [bool]$handoff.flags.fable_final_result_required -or
        -not [bool]$handoff.flags.auxiliary_model_adjustment_allowed) {
        Add-ValidationError 'Handoff state does not declare the Fable final-result policy.'
    }
    if (-not $handoff.PSObject.Properties['result_model']) {
        Add-ValidationError 'Handoff state does not record the current/final result model.'
    }
    if ([string]$handoff.workflow_status -eq 'READY_TO_START_FROM_BEGINNING') {
        if ([int]$handoff.progress.completed_count -ne 0 -or
            [string]$handoff.current_stage -ne '00_inventory' -or
            [string]$handoff.progress.next_incomplete_stage -ne '00_inventory' -or
            -not [bool]$handoff.flags.full_restart) {
            Add-ValidationError 'The declared full-restart state is not at stage 00 with 0/12 complete.'
        }
        $activeMarkers = @(Get-ChildItem -LiteralPath (
            Join-Path $missionRoot 'state\markers'
        ) -File | Where-Object { $_.Name -ne '.gitkeep' })
        $activeSessions = @(Get-ChildItem -LiteralPath (
            Join-Path $missionRoot 'state\sessions'
        ) -File | Where-Object { $_.Name -ne '.gitkeep' })
        if (@($activeMarkers).Count -ne 0 -or @($activeSessions).Count -ne 0) {
            Add-ValidationError 'The full-restart state still has an active marker or session.'
        }
    }
} catch {}

$checksumPath = Join-Path $missionRoot 'INPUT_CHECKSUMS.sha256'
if (Test-Path -LiteralPath $checksumPath -PathType Leaf) {
    foreach ($line in (Get-Content -LiteralPath $checksumPath)) {
        if ([string]::IsNullOrWhiteSpace($line)) { continue }
        if ($line -notmatch '^([0-9a-fA-F]{64})\s{2}(.+)$') {
            Add-ValidationError "Malformed checksum line: $line"
            continue
        }
        $expectedHash = $Matches[1].ToLowerInvariant()
        $relative = $Matches[2] -replace '/','\'
        $path = Join-Path $missionRoot $relative
        if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
            Add-ValidationError "Checksummed input missing: $relative"
            continue
        }
        $actualHash = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()
        if ($actualHash -ne $expectedHash) {
            Add-ValidationError "Checksum mismatch: $relative"
        }
    }
}

$manuscriptRoot = Join-Path $researchRoot '01_Publications\submitted\regular_lsens'
$hsxRoot = Join-Path $researchRoot '07_HSX_august2025_results'
if (-not (Test-Path -LiteralPath (
    Join-Path $manuscriptRoot 'regular_lsens.tex'
) -PathType Leaf)) {
    Add-ValidationError 'Extracted manuscript source is missing regular_lsens.tex.'
}
if (-not (Test-Path -LiteralPath $hsxRoot -PathType Container)) {
    Add-ValidationError 'Extracted HSX result folder is missing.'
} else {
    $hsxFiles = @(Get-ChildItem -LiteralPath $hsxRoot -Recurse -File)
    if (@($hsxFiles).Count -lt 230) {
        Add-ValidationError 'Extracted HSX result folder has fewer than 230 files.'
    }
}

$runnerPath = Join-Path $missionRoot 'RUN_PHD_RESEARCH.ps1'
$runnerText = Get-Content -Raw -LiteralPath $runnerPath
$rootEverythingText = Get-Content -Raw -LiteralPath (
    Join-Path $researchRoot 'RUN_EVERYTHING.ps1'
)
$rootDispatcherText = Get-Content -Raw -LiteralPath (
    Join-Path $researchRoot 'RUN_PHD_RESEARCH.ps1'
)
$childText = Get-Content -Raw -LiteralPath (
    Join-Path $missionRoot 'INVOKE_CLAUDE_CHILD.ps1'
)
$probeText = Get-Content -Raw -LiteralPath (
    Join-Path $missionRoot 'TEST_CLAUDE_MODELS.ps1'
)

$expectedRouting = [ordered]@{
    '00_inventory'=@('sonnet','high','High')
    '10a_literature_gan'=@('sonnet','xhigh','Extra High')
    '10b_literature_fusion'=@('sonnet','xhigh','Extra High')
    '10c_literature_methods'=@('sonnet','xhigh','Extra High')
    '10d_literature_merge'=@('fable','xhigh','Max')
    '20_direction'=@('fable','xhigh','Max')
    '30_manuscript'=@('fable','xhigh','Max')
    '40_experiment'=@('fable','xhigh','Max')
    '50_patent'=@('fable','xhigh','Max')
    '60_timeline'=@('sonnet','high','High')
    '70_redteam'=@('fable','xhigh','Max')
    '80_synthesis'=@('fable','xhigh','Max')
}
foreach ($stage in $expectedRouting.Keys) {
    $model = $expectedRouting[$stage][0]
    $effort = $expectedRouting[$stage][1]
    $handoffEffort = $expectedRouting[$stage][2]
    $pattern = "'" + [regex]::Escape($stage) +
        "'\s*=\s*@\{[\s\S]{0,500}?Model='" + [regex]::Escape($model) +
        "';\s*Effort='" + [regex]::Escape($effort) +
        "'[\s\S]{0,200}?ChatGptModel='gpt-5\.6-sol';\s*ChatGptEffort='" +
        [regex]::Escape($handoffEffort) + "'"
    if ($runnerText -notmatch $pattern) {
        Add-ValidationError "Incorrect model/effort mapping for stage $stage."
    }
}
if ([regex]::Matches($runnerText,"Model='fable';\s*Effort='xhigh'").Count -ne 7) {
    Add-ValidationError 'Expected exactly seven Fable/Extra High stages.'
}
if ([regex]::Matches($runnerText,"Model='sonnet';\s*Effort='xhigh'").Count -ne 3) {
    Add-ValidationError 'Expected exactly three Sonnet/Extra High stages.'
}
if ([regex]::Matches($runnerText,"Model='sonnet';\s*Effort='high'").Count -ne 2) {
    Add-ValidationError 'Expected exactly two Sonnet/High stages.'
}
if ($runnerText -notmatch "Resolve-ModelIntegrityAction[\s\S]{0,300}REGENERATE_AND_RETRY_REQUESTED_CLAUDE_MODEL" -or
    $runnerText -notmatch "SAVE_AND_HANDOFF_TO_CHATGPT_WINDOWS" -or
    $runnerText -notmatch 'EnforceModelIntegrity=\$enforceModelIntegrity' -or
    $runnerText -notmatch "ExpectedModel\s+-match\s+'\(\?i\)fable'" -or
    $runnerText -notmatch "PrimaryModelsText" -or
    $runnerText -notmatch "AuxiliaryModelsText" -or
    $runnerText -notmatch "TransientPrimaryModelsText" -or
    $runnerText -notmatch "ResultModel" -or
    $runnerText -notmatch "Cannot complete Fable-assigned stage") {
    Add-ValidationError 'Fable final-result first/second downgrade transition policy is missing.'
}
if ($runnerText -notmatch
    "ClarifiedRetry[\s\S]{0,120}cfg\.Model\s+-eq\s+'fable'[\s\S]{0,2000}'--safe-mode'") {
    Add-ValidationError 'The first Fable primary fallback does not select a fresh safe-mode retry.'
}
if ($runnerText -match 'CLAUDE_CODE_SUBAGENT_MODEL\s*=') {
    Add-ValidationError 'The runner still forces every auxiliary subagent onto the primary model.'
}
if ($runnerText -match
    'metadata\.Mismatch[\s\S]{0,160}Stop-ClaudeChildProcess') {
    Add-ValidationError 'The runner stops on a temporary Fable model adjustment instead of evaluating the final result model.'
}
foreach ($launcher in @(
    [pscustomobject]@{Name='RUN_EVERYTHING.ps1';Text=$rootEverythingText},
    [pscustomobject]@{Name='root RUN_PHD_RESEARCH.ps1';Text=$rootDispatcherText},
    [pscustomobject]@{Name='mission RUN_PHD_RESEARCH.ps1';Text=$runnerText}
)) {
    if ($launcher.Text -notmatch 'RetryClaudeAfterHandoff') {
        Add-ValidationError ("{0} does not expose the explicit Claude retry switch." -f
            $launcher.Name)
    }
}
if ($rootEverythingText -notmatch
    "runArguments\s*\+=\s*'-RetryClaudeAfterHandoff'") {
    Add-ValidationError 'RUN_EVERYTHING.ps1 does not forward the retry switch.'
}
if ($runnerText -notmatch 'function Save-HandoffHistory' -or
    $runnerText -notmatch 'USER_RETRY_AUTHORIZATION\.json' -or
    $runnerText -notmatch 'user_authorized_claude_retry' -or
    $runnerText -notmatch 'retry_cycle' -or
    $runnerText -notmatch 'cycle_attempt') {
    Add-ValidationError 'The explicit retry path does not preserve and label handoff history.'
}
if ($runnerText -notmatch
    "savedStatus\s+-eq\s+'CHATGPT_HANDOFF_REQUIRED'[\s\S]{0,2000}Save-HandoffHistory" -or
    $runnerText -notmatch
    "resumeSessionId\s*=\s*''[\s\S]{0,1000}CLAUDE_RETRY_AUTHORIZED") {
    Add-ValidationError 'The handoff override does not archive state and select a fresh Claude session.'
}
if ($runnerText -notmatch
    'while\s*\(-not\s+\$stageComplete\s+-and\s+\$cycleAttempt\s+-le\s+2\)') {
    Add-ValidationError 'The retry-cycle two-attempt bound is missing.'
}
if ($runnerText -notmatch 'state\\CHATGPT_HANDOFF_STATE\.json' -or
    $runnerText -notmatch 'state\\OPERATION_LOG\.csv' -or
    $runnerText -notmatch 'state\\CLAUDE_EVENT_LOG\.jsonl') {
    Add-ValidationError 'Continuous transition logging files are not wired into the runner.'
}
if ($runnerText -match 'ClaudeInactivityMinutes|CodexInactivityMinutes|Test-ClaudeUsageUnavailable|claude_inactive_timeout') {
    Add-ValidationError 'The runner still contains usage/inactivity watchdog behavior.'
}
if ($runnerText -match 'codex\s+exec|mcp-server|--mcp-config|--strict-mcp-config|codex_mcp') {
    Add-ValidationError 'The runner still contains an alternate-agent or MCP execution path.'
}
if ($runnerText -notmatch "'--disallowedTools','mcp__\*'") {
    Add-ValidationError 'Claude invocations do not deny user-scoped MCP tools.'
}
if ($probeText -match '--mcp-config|--strict-mcp-config|mcp-server') {
    Add-ValidationError 'Claude probes still load an MCP configuration.'
}
if ($probeText -notmatch "'--disallowedTools','mcp__\*'") {
    Add-ValidationError 'Claude probes do not deny user-scoped MCP tools.'
}
if ($childText -notmatch 'AutoFlush\s*=\s*\$true' -or
    $childText -notmatch 'CLAUDE_EVENT_LOG|EventLogFile') {
    Add-ValidationError 'The child process does not flush a per-event durable index.'
}
if ($childText -notmatch "model_policy_scope='fable_final_result_only'" -or
    $childText -notmatch 'primary_models=' -or
    $childText -notmatch 'auxiliary_models=' -or
    $childText -notmatch 'result_model_candidate=' -or
    $childText -notmatch 'fable_nonfinal_adjustment_flag=' -or
    $childText -notmatch "RequestedModel\s+-match\s+'\(\?i\)fable'") {
    Add-ValidationError 'The event logger does not distinguish temporary/auxiliary models from the Fable final result.'
}

$operationHeader = [string](Get-Content -LiteralPath (
    Join-Path $missionRoot 'state\OPERATION_LOG.csv'
) -First 1)
foreach ($requiredColumn in @(
    'progress','requested_model','requested_effort','reported_models',
    'downgrade_flag','usage_flag','inactivity_flag','checkpoint','next_action'
)) {
    if ($operationHeader -notmatch [regex]::Escape($requiredColumn)) {
        Add-ValidationError "OPERATION_LOG.csv is missing column $requiredColumn."
    }
}

if ($RequireComplete) {
    foreach ($stage in $expectedRouting.Keys) {
        if (-not (Test-Path -LiteralPath (
            Join-Path $missionRoot ("state\markers\{0}.done.json" -f $stage)
        ) -PathType Leaf)) {
            Add-ValidationError "Completion marker missing: $stage"
        }
    }
    foreach ($file in @(
        'outputs\FINAL_EXECUTIVE_STRATEGY.md',
        'outputs\FINAL_ACTION_PLAN.md',
        'outputs\FINAL_DELIVERABLE_INDEX.md',
        'outputs\FINAL_AUDIT.md'
    )) {
        Assert-File -Base $missionRoot -RelativePath $file
    }
}

if (@($errors).Count -gt 0) {
    Write-Host ''
    Write-Host ("PACKAGE VALIDATION FAILED ({0} issue(s))." -f @($errors).Count) -ForegroundColor Red
    exit 1
}

Write-Host 'PASS: package structure, JSON, checksums, Claude-only routing, continuous logs, Fable final-result enforcement, temporary/auxiliary-model allowance, explicit retry archive, and ChatGPT handoff validated.' -ForegroundColor Green
exit 0
