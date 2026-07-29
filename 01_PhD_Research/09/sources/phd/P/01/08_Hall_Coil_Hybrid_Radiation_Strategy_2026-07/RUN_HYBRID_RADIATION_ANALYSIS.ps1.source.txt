#requires -Version 5.1
<#
Claude-only, checkpointed runner for the Hall + inductive-coil hybrid,
radiation-compensation, applications, and limitations analysis.

Normal run and automatic resume:
  powershell -ExecutionPolicy Bypass -File .\RUN_HYBRID_RADIATION_ANALYSIS.ps1 -Resume

Explicitly start a new Claude retry cycle after a saved manual checkpoint:
  powershell -ExecutionPolicy Bypass -File .\RUN_HYBRID_RADIATION_ANALYSIS.ps1 -Resume -RetryClaudeAfterHandoff

This runner never invokes another AI provider. It does not poll Claude usage
and it does not stop a quiet process. The user may stop PowerShell manually;
the live stream, event index, attempt state, performance metrics, and manual
continuation snapshot are flushed inside the project as work proceeds.
#>
[CmdletBinding()]
param(
    [switch]$Resume,
    [switch]$DryRun,
    [switch]$SelfTest,
    [string[]]$OnlyStage,
    [string]$FromStage,
    [string[]]$ForceStage,
    [switch]$RetryClaudeAfterHandoff,
    [ValidateSet('full','guarded')]
    [string]$Mode = 'full'
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot

$MissionRoot = $PSScriptRoot
$ResearchRoot = Split-Path -Parent $MissionRoot
$MinClaudeVersion = [version]'2.1.219'
$RunStamp = Get-Date -Format 'yyyy-MM-dd_HHmmss_fff'
$RunRoot = Join-Path $MissionRoot ("logs\run_{0}" -f $RunStamp)
$HistoryPath = Join-Path $MissionRoot 'logs\RUN_HISTORY.jsonl'
$ModelLogPath = Join-Path $MissionRoot 'state\MODEL_EFFORT_LOG.csv'
$PerformanceLogPath = Join-Path $MissionRoot 'state\PERFORMANCE_LOG.csv'
$SessionIndexPath = Join-Path $MissionRoot 'state\SESSION_INDEX.csv'
$OperationLogPath = Join-Path $MissionRoot 'state\OPERATION_LOG.csv'
$EventLogPath = Join-Path $MissionRoot 'state\CLAUDE_EVENT_LOG.jsonl'
$HandoffJsonPath = Join-Path $MissionRoot 'state\CHATGPT_HANDOFF_STATE.json'
$HandoffMarkdownPath = Join-Path $MissionRoot 'state\CHATGPT_HANDOFF.md'
$GeneratedPromptRoot = Join-Path $MissionRoot 'state\generated_prompts'
$HandoffHistoryRoot = Join-Path $MissionRoot 'state\handoff_history'
$SharedPromptPath = Join-Path $MissionRoot 'prompts\_shared_system.md'
$ClaudeChildPath = Join-Path $MissionRoot 'INVOKE_CLAUDE_CHILD.ps1'
$script:CurrentStage = ''
$script:CurrentAttempt = 0
$script:CurrentRetryCycle = 0
$script:CurrentCycleAttempt = 1
$script:CurrentHandoffHistory = ''
$script:CurrentStream = ''
$utf8 = New-Object System.Text.UTF8Encoding $false
$OutputEncoding = $utf8
try { [Console]::OutputEncoding = $utf8 } catch {}

$Stages = [ordered]@{
    '00_inventory' = @{
        Prompt='prompts\00_inventory.md'; Model='sonnet'; Effort='high'; MaxTurns=70; Next='10a_literature_hybrid'
        Expected=@(
            'outputs\00_INPUT_INVENTORY.md',
            'outputs\00_REQUIREMENTS_TRACE.csv',
            'outputs\00_CONFLICT_LEDGER.md'
        )
    }
    '10a_literature_hybrid' = @{
        Prompt='prompts\10a_literature_hybrid.md'; Model='sonnet'; Effort='xhigh'; MaxTurns=145; Next='10b_literature_radiation'
        Expected=@('evidence\10A_HYBRID_SOURCES.csv','evidence\10A_HYBRID_SYNTHESIS.md')
    }
    '10b_literature_radiation' = @{
        Prompt='prompts\10b_literature_radiation.md'; Model='sonnet'; Effort='xhigh'; MaxTurns=155; Next='10c_literature_applications'
        Expected=@('evidence\10B_RADIATION_SOURCES.csv','evidence\10B_RADIATION_SYNTHESIS.md')
    }
    '10c_literature_applications' = @{
        Prompt='prompts\10c_literature_applications.md'; Model='sonnet'; Effort='high'; MaxTurns=135; Next='10d_evidence_merge'
        Expected=@('evidence\10C_APPLICATION_SOURCES.csv','evidence\10C_APPLICATION_SYNTHESIS.md')
    }
    '10d_evidence_merge' = @{
        Prompt='prompts\10d_evidence_merge.md'; Model='fable'; Effort='xhigh'; MaxTurns=155; Next='20_observability'
        Expected=@(
            'outputs\01_SOURCE_LEDGER.csv',
            'outputs\01_HYBRID_LITERATURE_REVIEW.md',
            'outputs\01_RADIATION_LITERATURE_REVIEW.md',
            'outputs\01_APPLICATIONS_ALTERNATIVES_REVIEW.md',
            'outputs\01_EVIDENCE_MAP.csv',
            'outputs\01_SOURCE_COVERAGE.md',
            'outputs\01_NEW_SOURCE_AUDIT.csv'
        )
    }
    '20_observability' = @{
        Prompt='prompts\20_observability.md'; Model='fable'; Effort='xhigh'; MaxTurns=125; Next='30_radiation_compensation'
        Expected=@(
            'outputs\02_OBSERVABILITY_AND_IDENTIFIABILITY.md',
            'outputs\02_MUTUAL_CALIBRATION_FEASIBILITY.md',
            'outputs\02_ESTIMATOR_REQUIREMENTS.csv'
        )
    }
    '30_radiation_compensation' = @{
        Prompt='prompts\30_radiation_compensation.md'; Model='fable'; Effort='xhigh'; MaxTurns=135; Next='40_applications_collaboration'
        Expected=@(
            'outputs\03_RADIATION_COMPENSATION_ARCHITECTURE.md',
            'outputs\03_SIMULATION_AND_VALIDATION_PLAN.md',
            'outputs\03_RADIATION_RISK_REGISTER.csv'
        )
    }
    '40_applications_collaboration' = @{
        Prompt='prompts\40_applications_collaboration.md'; Model='sonnet'; Effort='xhigh'; MaxTurns=125; Next='50_limitations_comparison'
        Expected=@(
            'outputs\04_APPLICATION_SCORECARD.csv',
            'outputs\04_COLLABORATION_STRATEGY.md',
            'outputs\04_COLLABORATOR_CANDIDATES.csv'
        )
    }
    '50_limitations_comparison' = @{
        Prompt='prompts\50_limitations_comparison.md'; Model='fable'; Effort='xhigh'; MaxTurns=125; Next='60_research_program'
        Expected=@(
            'outputs\05_LIMITATIONS_AND_FAILURE_MODES.md',
            'outputs\05_TECHNOLOGY_COMPARISON.csv',
            'outputs\05_FALSIFICATION_TESTS.md'
        )
    }
    '60_research_program' = @{
        Prompt='prompts\60_research_program.md'; Model='fable'; Effort='xhigh'; MaxTurns=125; Next='70_redteam'
        Expected=@(
            'outputs\06_INTEGRATED_RESEARCH_PROGRAM.md',
            'outputs\06_DECISION_GATES_AND_ROADMAP.md',
            'outputs\06_ADVISOR_MEETING_BRIEF.md'
        )
    }
    '70_redteam' = @{
        Prompt='prompts\70_redteam.md'; Model='fable'; Effort='xhigh'; MaxTurns=130; Next='80_synthesis'
        Expected=@(
            'outputs\07_RED_TEAM_FINDINGS.md',
            'outputs\07_SOURCE_AUDIT.csv',
            'outputs\07_CORRECTION_LOG.md'
        )
    }
    '80_synthesis' = @{
        Prompt='prompts\80_synthesis.md'; Model='fable'; Effort='xhigh'; MaxTurns=110; Next='none'
        Expected=@(
            'outputs\FINAL_EXECUTIVE_DECISION.md',
            'outputs\FINAL_PLAIN_LANGUAGE_GUIDE.md',
            'outputs\FINAL_ACTION_PLAN.md',
            'outputs\FINAL_DELIVERABLE_INDEX.md',
            'outputs\FINAL_AUDIT.md'
        )
    }
}

$RequiredLedgerHeader = @(
    'source_id','citation','title','authors','year','venue','doi','url',
    'source_type','peer_review_status','quality_tier','topic_tags',
    'claims_supported','verification_basis','access_level','notes'
)

function Get-IsoTimestamp {
    return (Get-Date).ToString('o')
}

function Write-Section([string]$Text) {
    Write-Host ''
    Write-Host ("==== {0} ====" -f $Text) -ForegroundColor Cyan
}

function Write-JsonAtomic {
    param([Parameter(Mandatory=$true)][string]$Path,
          [Parameter(Mandatory=$true)][object]$Value)
    $parent = Split-Path -Parent $Path
    if (-not (Test-Path -LiteralPath $parent -PathType Container)) {
        New-Item -ItemType Directory -Force -Path $parent | Out-Null
    }
    $temp = "{0}.tmp.{1}" -f $Path,$PID
    ($Value | ConvertTo-Json -Depth 15) | Set-Content -LiteralPath $temp -Encoding UTF8
    Move-Item -LiteralPath $temp -Destination $Path -Force
}

function Initialize-StateFiles {
    foreach ($directory in @(
        (Join-Path $MissionRoot 'logs'),
        (Join-Path $MissionRoot 'state\attempts'),
        (Join-Path $MissionRoot 'state\markers'),
        (Join-Path $MissionRoot 'state\sessions'),
        (Join-Path $MissionRoot 'state\checkpoints'),
        $GeneratedPromptRoot,
        $HandoffHistoryRoot
    )) {
        New-Item -ItemType Directory -Force -Path $directory | Out-Null
    }
    if (-not (Test-Path -LiteralPath $ModelLogPath -PathType Leaf)) {
        '"timestamp","stage","route","attempt","requested_model","requested_effort","reported_models","status","session_id","seconds","validation","notes"' |
            Set-Content -LiteralPath $ModelLogPath -Encoding UTF8
    }
    if (-not (Test-Path -LiteralPath $PerformanceLogPath -PathType Leaf)) {
        '"timestamp","stage","attempt","requested_model","requested_effort","duration_seconds","num_turns","input_tokens","output_tokens","cache_read_input_tokens","cache_creation_input_tokens","total_cost_usd","web_search_requests","web_fetch_requests","result_model","integrity","verified_source_count","notes"' |
            Set-Content -LiteralPath $PerformanceLogPath -Encoding UTF8
    }
    if (-not (Test-Path -LiteralPath $SessionIndexPath -PathType Leaf)) {
        '"timestamp","stage","route","attempt","session_id","stream_file","status"' |
            Set-Content -LiteralPath $SessionIndexPath -Encoding UTF8
    }
    if (-not (Test-Path -LiteralPath $OperationLogPath -PathType Leaf)) {
        '"timestamp","stage","operation","progress","route","attempt","status","requested_model","requested_effort","reported_models","downgrade_flag","downgrade_count","usage_flag","inactivity_flag","session_id","stream_file","checkpoint","next_action","notes"' |
            Set-Content -LiteralPath $OperationLogPath -Encoding UTF8
    }
    if (-not (Test-Path -LiteralPath $EventLogPath -PathType Leaf)) {
        New-Item -ItemType File -Path $EventLogPath | Out-Null
    }
    if (-not (Test-Path -LiteralPath $HistoryPath -PathType Leaf)) {
        New-Item -ItemType File -Path $HistoryPath | Out-Null
    }
}

function Add-HistoryRecord {
    param([hashtable]$Record)
    $Record['timestamp'] = Get-IsoTimestamp
    ($Record | ConvertTo-Json -Depth 12 -Compress) |
        Add-Content -LiteralPath $HistoryPath -Encoding UTF8
}

function Add-CsvRecord {
    param([string]$Path,[object]$Record)
    $Record | Export-Csv -LiteralPath $Path -NoTypeInformation -Append -Encoding UTF8
}

function Add-OperationRecord {
    param(
        [string]$Stage='',
        [string]$Operation='',
        [string]$Progress='',
        [string]$Route='claude_code_powershell',
        [int]$Attempt=0,
        [string]$Status='',
        [string]$RequestedModel='',
        [string]$RequestedEffort='',
        [string]$ReportedModels='',
        [bool]$DowngradeFlag=$false,
        [int]$DowngradeCount=0,
        [string]$SessionId='',
        [string]$StreamFile='',
        [string]$Checkpoint='',
        [string]$NextAction='',
        [string]$Notes=''
    )
    if ([string]::IsNullOrWhiteSpace($Progress)) { $Progress = $Status }
    Add-CsvRecord -Path $OperationLogPath -Record ([pscustomobject]@{
        timestamp=Get-IsoTimestamp
        stage=$Stage
        operation=$Operation
        progress=$Progress
        route=$Route
        attempt=$Attempt
        status=$Status
        requested_model=$RequestedModel
        requested_effort=$RequestedEffort
        reported_models=$ReportedModels
        downgrade_flag=$DowngradeFlag
        downgrade_count=$DowngradeCount
        usage_flag='NOT_CHECKED_BY_RUNNER'
        inactivity_flag='NOT_CHECKED_BY_RUNNER'
        session_id=$SessionId
        stream_file=$StreamFile
        checkpoint=$Checkpoint
        next_action=$NextAction
        notes=$Notes
    })
}

function Get-StageMarkerPath([string]$Stage) {
    return (Join-Path $MissionRoot ("state\markers\{0}.done.json" -f $Stage))
}

function Get-AttemptStatePath([string]$Stage) {
    return (Join-Path $MissionRoot ("state\attempts\{0}.json" -f $Stage))
}

function Get-SessionStatePath([string]$Stage) {
    return (Join-Path $MissionRoot ("state\sessions\{0}.session_id" -f $Stage))
}

function Read-AttemptState([string]$Stage) {
    $path = Get-AttemptStatePath $Stage
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { return $null }
    try { return (Get-Content -Raw -LiteralPath $path | ConvertFrom-Json) }
    catch { return $null }
}

function Set-AttemptState {
    param(
        [string]$Stage,
        [int]$Attempt,
        [string]$Status,
        [string]$StreamFile='',
        [string]$SessionId='',
        [string]$ReportedModels='',
        [string]$PrimaryModels='',
        [string]$AuxiliaryModels='',
        [string]$ResultModel='',
        [bool]$SecurityFallbackFlag=$false,
        [int]$DowngradeCount=0,
        [string]$PromptFile='',
        [string]$Note='',
        [int]$RetryCycle=0,
        [int]$CycleAttempt=1,
        [string]$HandoffHistory=''
    )
    $cfg = $Stages[$Stage]
    $value = [ordered]@{
        schema_version=2
        stage=$Stage
        route='claude_code_powershell'
        attempt=$Attempt
        retry_cycle=$RetryCycle
        cycle_attempt=$CycleAttempt
        status=$Status
        requested_model=[string]$cfg.Model
        requested_effort=[string]$cfg.Effort
        reported_models=$ReportedModels
        primary_models=$PrimaryModels
        auxiliary_models=$AuxiliaryModels
        result_model=$ResultModel
        model_policy_scope='fable_final_result_only'
        security_fallback_flag=$SecurityFallbackFlag
        downgrade_count=$DowngradeCount
        stream_file=$StreamFile
        session_id=$SessionId
        generated_prompt=$PromptFile
        handoff_history=$HandoffHistory
        manual_review_hint=[ordered]@{
            requested_claude_model=[string]$cfg.Model
            requested_claude_effort=[string]$cfg.Effort
            do_not_auto_route_to_another_provider=$true
        }
        note=$Note
        updated_at=Get-IsoTimestamp
    }
    Write-JsonAtomic -Path (Get-AttemptStatePath $Stage) -Value $value
}

function Get-NextIncompleteStage {
    foreach ($name in @($Stages.Keys)) {
        if (-not (Test-Path -LiteralPath (Get-StageMarkerPath $name) -PathType Leaf)) {
            return [string]$name
        }
    }
    return ''
}

function Get-Progress {
    $completed = @()
    foreach ($name in @($Stages.Keys)) {
        if (Test-Path -LiteralPath (Get-StageMarkerPath $name) -PathType Leaf) {
            $completed += [string]$name
        }
    }
    [object[]]$allNames = @($Stages.Keys)
    return [ordered]@{
        completed_count=@($completed).Count
        total_count=$allNames.Count
        completed_stages=@($completed)
        next_incomplete_stage=(Get-NextIncompleteStage)
    }
}

function Write-HandoffState {
    param(
        [string]$Status,
        [string]$Stage='',
        [int]$Attempt=0,
        [string]$Reason='',
        [string]$StreamFile='',
        [string]$SessionId='',
        [string]$ReportedModels='',
        [string]$PrimaryModels='',
        [string]$AuxiliaryModels='',
        [string]$ResultModel='',
        [bool]$SecurityFallbackFlag=$false,
        [int]$DowngradeCount=0,
        [string]$GeneratedPrompt='',
        [string]$NextAction='',
        [int]$RetryCycle=0,
        [int]$CycleAttempt=1,
        [string]$HandoffHistory=''
    )
    if ([string]::IsNullOrWhiteSpace($Stage)) {
        $Stage = Get-NextIncompleteStage
    }
    $model = ''
    $effort = ''
    $expected = @()
    if (-not [string]::IsNullOrWhiteSpace($Stage) -and $Stages.Contains($Stage)) {
        $cfg = $Stages[$Stage]
        $model = [string]$cfg.Model
        $effort = [string]$cfg.Effort
        $expected = @($cfg.Expected)
    }
    $progress = Get-Progress
    $activeRoute = if ($Status -eq 'MANUAL_CONTINUATION_REQUIRED') {
        'manual_continuation_pending'
    } else {
        'claude_code_powershell'
    }
    $state = [ordered]@{
        schema_version=2
        updated_at=Get-IsoTimestamp
        workflow_status=$Status
        reason=$Reason
        current_stage=$Stage
        stage_attempt=$Attempt
        retry_cycle=$RetryCycle
        cycle_attempt=$CycleAttempt
        active_route=$activeRoute
        requested_claude_model=$model
        requested_claude_effort=$effort
        reported_models=$ReportedModels
        primary_models=$PrimaryModels
        auxiliary_models=$AuxiliaryModels
        result_model=$ResultModel
        model_policy_scope='fable_final_result_only'
        security_fallback_flag=$SecurityFallbackFlag
        downgrade_count=$DowngradeCount
        flags=[ordered]@{
            downgrade_detected=($DowngradeCount -gt 0)
            first_model_retry_used=($DowngradeCount -gt 0)
            downgrade_tracking_fable_final_result_only=$true
            fable_final_result_required=$true
            auxiliary_model_adjustment_allowed=$true
            manual_continuation_required=($Status -eq 'MANUAL_CONTINUATION_REQUIRED')
            alternate_provider_handoff_required=$false
            usage_limit_checked_by_runner=$false
            inactivity_timeout_enabled=$false
            manual_stop_supported=$true
            user_authorized_claude_retry=($RetryCycle -gt 0)
            previous_handoff_archived=(-not [string]::IsNullOrWhiteSpace($HandoffHistory))
            external_agent_runtime_enabled=$false
            connector_runtime_enabled=$false
        }
        progress=$progress
        current_stage_expected_outputs=$expected
        durable_files=[ordered]@{
            attempt_state=("state\attempts\{0}.json" -f $Stage)
            completion_markers='state\markers'
            raw_claude_stream=$StreamFile
            claude_event_index='state\CLAUDE_EVENT_LOG.jsonl'
            operation_log='state\OPERATION_LOG.csv'
            model_effort_log='state\MODEL_EFFORT_LOG.csv'
            session_index='state\SESSION_INDEX.csv'
            generated_prompt=$GeneratedPrompt
            handoff_history=$HandoffHistory
            human_snapshot='state\CHATGPT_HANDOFF.md'
        }
        manual_continuation=[ordered]@{
            requested_claude_model=$model
            requested_claude_effort=$effort
            do_not_auto_route_to_another_provider=$true
            instructions='AGENTS.md'
            continuation_guide='RESUME_GUIDE.md'
        }
        session_id=$SessionId
        next_action=$NextAction
    }
    Write-JsonAtomic -Path $HandoffJsonPath -Value $state

    $markdown = @"
# Manual continuation snapshot

- Updated: $($state.updated_at)
- Workflow status: $Status
- Reason: $Reason
- Current stage: $Stage
- Claude attempt: $Attempt
- User-authorized retry cycle: $RetryCycle
- Attempt within current cycle: $CycleAttempt
- Requested Claude model / effort: $model / $effort
- Reported models: $ReportedModels
- Primary models: $PrimaryModels
- Auxiliary models: $AuxiliaryModels
- Current/final result model: $ResultModel
- Model policy: Fable 5 must produce each Fable-assigned final result;
  temporary and auxiliary model adjustments are allowed
- Security/content fallback notice observed: $SecurityFallbackFlag
- Downgrade count: $DowngradeCount
- Completed stages: $($progress.completed_count) / $($progress.total_count)
- Raw live stream: $StreamFile
- Generated effective prompt: $GeneratedPrompt
- Previous handoff archive: $HandoffHistory
- Requested Claude model / effort: $model / $effort
- Automatic alternate-provider routing: disabled

## Continue

$NextAction

Do not silently route to another provider. Review this snapshot and
state/CHATGPT_HANDOFF_STATE.json. After deciding how to proceed, either repair
the named prerequisite or explicitly authorize a fresh Claude-only cycle with
-RetryClaudeAfterHandoff.
"@
    $markdown | Set-Content -LiteralPath $HandoffMarkdownPath -Encoding UTF8
}

function Get-IntegerProperty {
    param(
        [Parameter(Mandatory=$true)][object]$InputObject,
        [Parameter(Mandatory=$true)][string]$Name,
        [int]$Default=0
    )
    $property = $InputObject.PSObject.Properties[$Name]
    if ($null -eq $property -or $null -eq $property.Value) {
        return $Default
    }
    try { return [int]$property.Value }
    catch { return $Default }
}

function Get-StringProperty {
    param(
        [Parameter(Mandatory=$true)][object]$InputObject,
        [Parameter(Mandatory=$true)][string]$Name,
        [string]$Default=''
    )
    $property = $InputObject.PSObject.Properties[$Name]
    if ($null -eq $property -or $null -eq $property.Value) {
        return $Default
    }
    return [string]$property.Value
}

function Get-DoubleProperty {
    param(
        [Parameter(Mandatory=$true)][object]$InputObject,
        [Parameter(Mandatory=$true)][string]$Name,
        [double]$Default=0
    )
    $property = $InputObject.PSObject.Properties[$Name]
    if ($null -eq $property -or $null -eq $property.Value) {
        return $Default
    }
    try { return [double]$property.Value }
    catch { return $Default }
}

function Save-HandoffHistory {
    param(
        [Parameter(Mandatory=$true)][string]$Stage,
        [Parameter(Mandatory=$true)][object]$AttemptState,
        [Parameter(Mandatory=$true)][int]$RetryCycle
    )
    $historyName = "retry_{0}_cycle_{1}_{2}" -f $RunStamp,$RetryCycle,$Stage
    $historyRelative = "state\handoff_history\{0}" -f $historyName
    $historyDirectory = Join-Path $MissionRoot $historyRelative
    New-Item -ItemType Directory -Force -Path $historyDirectory | Out-Null

    $copied = @()
    $copies = @(
        [pscustomobject]@{
            Source=(Get-AttemptStatePath $Stage)
            Name='attempt_state_before_retry.json'
        },
        [pscustomobject]@{
            Source=$HandoffJsonPath
            Name='CHATGPT_HANDOFF_STATE_before_retry.json'
        },
        [pscustomobject]@{
            Source=$HandoffMarkdownPath
            Name='CHATGPT_HANDOFF_before_retry.md'
        },
        [pscustomobject]@{
            Source=(Get-SessionStatePath $Stage)
            Name='session_id_before_retry.txt'
        }
    )
    foreach ($item in $copies) {
        if (Test-Path -LiteralPath $item.Source -PathType Leaf) {
            Copy-Item -LiteralPath $item.Source -Destination (
                Join-Path $historyDirectory $item.Name
            )
            $copied += $item.Name
        }
    }

    $savedPrompt = [string]$AttemptState.generated_prompt
    $promptSource = $savedPrompt
    if (-not (Test-Path -LiteralPath $promptSource -PathType Leaf) -and
        -not [string]::IsNullOrWhiteSpace($savedPrompt)) {
        $promptSource = Join-Path $GeneratedPromptRoot (
            Split-Path -Leaf $savedPrompt
        )
    }
    if (-not [string]::IsNullOrWhiteSpace($promptSource) -and
        (Test-Path -LiteralPath $promptSource -PathType Leaf)) {
        Copy-Item -LiteralPath $promptSource -Destination (
            Join-Path $historyDirectory 'generated_prompt_before_retry.md'
        )
        $copied += 'generated_prompt_before_retry.md'
    }

    $checkpoint = Get-ChildItem -LiteralPath (
        Join-Path $MissionRoot 'state\checkpoints'
    ) -File -Filter ("CP_{0}_*.md" -f $Stage) |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1
    if ($null -ne $checkpoint) {
        Copy-Item -LiteralPath $checkpoint.FullName -Destination (
            Join-Path $historyDirectory 'latest_checkpoint_before_retry.md'
        )
        $copied += 'latest_checkpoint_before_retry.md'
    }

    $authorization = [ordered]@{
        schema_version=1
        authorized_at=Get-IsoTimestamp
        authorization='USER_EXPLICITLY_REQUESTED_ANOTHER_CLAUDE_CODE_RUN'
        stage=$Stage
        new_retry_cycle=$RetryCycle
        previous_status=[string]$AttemptState.status
        previous_global_attempt=(Get-IntegerProperty -InputObject $AttemptState -Name 'attempt' -Default 0)
        previous_retry_cycle=(Get-IntegerProperty -InputObject $AttemptState -Name 'retry_cycle' -Default 0)
        previous_cycle_attempt=(Get-IntegerProperty -InputObject $AttemptState -Name 'cycle_attempt' -Default 2)
        previous_reason=[string]$AttemptState.note
        previous_reported_models=[string]$AttemptState.reported_models
        previous_session_id=[string]$AttemptState.session_id
        previous_stream_file=[string]$AttemptState.stream_file
        preserved_files=@($copied)
        new_session_required=$true
        next_action='Start the same stage in a fresh Claude session using durable files. Do not resume the rejected session.'
    }
    Write-JsonAtomic -Path (
        Join-Path $historyDirectory 'USER_RETRY_AUTHORIZATION.json'
    ) -Value $authorization
    Add-HistoryRecord @{
        event='user_authorized_claude_retry'
        stage=$Stage
        retry_cycle=$RetryCycle
        previous_attempt=$authorization.previous_global_attempt
        previous_reason=$authorization.previous_reason
        archive=$historyRelative
    }
    return $historyRelative
}

function Convert-JsonLine([string]$Line) {
    if ([string]::IsNullOrWhiteSpace($Line)) { return $null }
    try { return ($Line | ConvertFrom-Json) } catch { return $null }
}

function Get-SessionIdFromStream([string]$StreamFile) {
    if (-not (Test-Path -LiteralPath $StreamFile -PathType Leaf)) { return '' }
    foreach ($line in (Get-Content -LiteralPath $StreamFile -ErrorAction SilentlyContinue)) {
        $event = Convert-JsonLine $line
        if ($null -ne $event -and $event.PSObject.Properties['session_id']) {
            $sid = [string]$event.session_id
            if (-not [string]::IsNullOrWhiteSpace($sid)) { return $sid }
        }
    }
    return ''
}

function Get-LatestSessionId([string]$Stage) {
    $attemptState = Read-AttemptState $Stage
    if ($null -ne $attemptState) {
        if ($attemptState.PSObject.Properties['session_id']) {
            $saved = [string]$attemptState.session_id
            if (-not [string]::IsNullOrWhiteSpace($saved)) { return $saved }
        }
        if ($attemptState.PSObject.Properties['stream_file']) {
            $fromStream = Get-SessionIdFromStream ([string]$attemptState.stream_file)
            if (-not [string]::IsNullOrWhiteSpace($fromStream)) { return $fromStream }
        }
    }
    $path = Get-SessionStatePath $Stage
    if (Test-Path -LiteralPath $path -PathType Leaf) {
        $saved = ([string](Get-Content -Raw -LiteralPath $path)).Trim()
        if (-not [string]::IsNullOrWhiteSpace($saved)) { return $saved }
    }
    return ''
}

function Get-ClaudeStreamMetadata {
    param(
        [string]$StreamFile,
        [string]$ErrorFile,
        [string]$ExpectedModel
    )
    $models = @()
    $primaryModels = @()
    $initModel = ''
    $lastAssistantPrimaryModel = ''
    $securityFallbackFlag = $false
    $lastResultEvent = $null
    if (Test-Path -LiteralPath $StreamFile -PathType Leaf) {
        foreach ($line in (Get-Content -LiteralPath $StreamFile -ErrorAction SilentlyContinue)) {
            $event = Convert-JsonLine $line
            if ($null -eq $event) { continue }
            if ($event.PSObject.Properties['model']) {
                $value = [string]$event.model
                if (-not [string]::IsNullOrWhiteSpace($value)) { $models += $value }
                if ($event.PSObject.Properties['type'] -and
                    [string]$event.type -eq 'system' -and
                    $event.PSObject.Properties['subtype'] -and
                    [string]$event.subtype -eq 'init') {
                    $initModel = $value
                    if (-not [string]::IsNullOrWhiteSpace($value)) {
                        $primaryModels += $value
                    }
                }
            }
            if ($event.PSObject.Properties['message'] -and
                $null -ne $event.message -and
                $event.message.PSObject.Properties['model']) {
                $value = [string]$event.message.model
                if (-not [string]::IsNullOrWhiteSpace($value)) { $models += $value }
                $isSubagentEvent = $false
                if ($event.PSObject.Properties['parent_tool_use_id']) {
                    $isSubagentEvent = -not [string]::IsNullOrWhiteSpace(
                        [string]$event.parent_tool_use_id
                    )
                }
                if (-not $isSubagentEvent -and
                    -not [string]::IsNullOrWhiteSpace($value)) {
                    $primaryModels += $value
                    $lastAssistantPrimaryModel = $value
                }
            }
            foreach ($usageName in @('modelUsage','model_usage')) {
                $usageProperty = $event.PSObject.Properties[$usageName]
                if ($null -ne $usageProperty -and $null -ne $usageProperty.Value) {
                    foreach ($property in $usageProperty.Value.PSObject.Properties) {
                        if (-not [string]::IsNullOrWhiteSpace([string]$property.Name)) {
                            $models += [string]$property.Name
                        }
                    }
                }
            }
            if ($event.PSObject.Properties['type'] -and
                [string]$event.type -in @('system','result') -and
                $line -match '(?i)(safety|classifier|flagged|content[- ]based).{0,240}(fallback|re-run|switch)|(?:fallback|re-run|switch).{0,240}(opus|safety|classifier|flagged)') {
                $securityFallbackFlag = $true
            }
            if ($event.PSObject.Properties['type'] -and
                [string]$event.type -eq 'result') {
                $lastResultEvent = $event
            }
        }
    }
    $uniqueModels = @($models | Select-Object -Unique)
    $uniquePrimaryModels = @($primaryModels | Select-Object -Unique)
    $auxiliaryModels = @($uniqueModels | Where-Object {
        $uniquePrimaryModels -notcontains [string]$_
    })
    $expectedPattern = [regex]::Escape(([string]$ExpectedModel).ToLowerInvariant())
    $expectedSeen = $false
    $mismatch = $false
    $enforceModelIntegrity = ([string]$ExpectedModel -match '(?i)fable')
    $resultModel = $lastAssistantPrimaryModel
    if (-not [string]::IsNullOrWhiteSpace($resultModel)) {
        if ($resultModel -match ("(?i){0}" -f $expectedPattern)) {
            $expectedSeen = $true
        } elseif ($enforceModelIntegrity -and
            $resultModel -match '(?i)(fable|opus|sonnet|haiku)') {
            $mismatch = $true
        }
    }
    $errorText = ''
    if (Test-Path -LiteralPath $ErrorFile -PathType Leaf) {
        $errorText = [string](Get-Content -Raw -LiteralPath $ErrorFile -ErrorAction SilentlyContinue)
    }
    if ($errorText -match '(?i)(safety|classifier|flagged|content[- ]based).{0,240}(fallback|re-run|switch)|(?:fallback|re-run|switch).{0,240}(opus|safety|classifier|flagged)') {
        $securityFallbackFlag = $true
    }
    $transientPrimaryModels = @($uniquePrimaryModels | Where-Object {
        [string]$_ -ne $resultModel
    })
    $numTurns = 0
    $inputTokens = 0
    $outputTokens = 0
    $cacheReadInputTokens = 0
    $cacheCreationInputTokens = 0
    $totalCostUsd = 0
    $webSearchRequests = 0
    $webFetchRequests = 0
    if ($null -ne $lastResultEvent) {
        $numTurns = Get-IntegerProperty -InputObject $lastResultEvent `
            -Name 'num_turns' -Default 0
        $totalCostUsd = Get-DoubleProperty -InputObject $lastResultEvent `
            -Name 'total_cost_usd' -Default 0
        $usageProperty = $lastResultEvent.PSObject.Properties['usage']
        if ($null -ne $usageProperty -and $null -ne $usageProperty.Value) {
            $usage = $usageProperty.Value
            $inputTokens = Get-IntegerProperty -InputObject $usage `
                -Name 'input_tokens' -Default 0
            $outputTokens = Get-IntegerProperty -InputObject $usage `
                -Name 'output_tokens' -Default 0
            $cacheReadInputTokens = Get-IntegerProperty -InputObject $usage `
                -Name 'cache_read_input_tokens' -Default 0
            $cacheCreationInputTokens = Get-IntegerProperty -InputObject $usage `
                -Name 'cache_creation_input_tokens' -Default 0
            $serverToolProperty = $usage.PSObject.Properties['server_tool_use']
            if ($null -ne $serverToolProperty -and
                $null -ne $serverToolProperty.Value) {
                $serverToolUse = $serverToolProperty.Value
                $webSearchRequests = Get-IntegerProperty `
                    -InputObject $serverToolUse -Name 'web_search_requests' -Default 0
                $webFetchRequests = Get-IntegerProperty `
                    -InputObject $serverToolUse -Name 'web_fetch_requests' -Default 0
            }
        }
    }
    return [pscustomobject]@{
        InitModel=$initModel
        Models=$uniqueModels
        ModelsText=($uniqueModels -join ';')
        PrimaryModels=$uniquePrimaryModels
        PrimaryModelsText=($uniquePrimaryModels -join ';')
        AuxiliaryModels=$auxiliaryModels
        AuxiliaryModelsText=($auxiliaryModels -join ';')
        TransientPrimaryModels=$transientPrimaryModels
        TransientPrimaryModelsText=($transientPrimaryModels -join ';')
        ResultModel=$resultModel
        ExpectedSeen=$expectedSeen
        Mismatch=$mismatch
        EnforceModelIntegrity=$enforceModelIntegrity
        SecurityFallbackFlag=$securityFallbackFlag
        ErrorText=$errorText
        NumTurns=$numTurns
        InputTokens=$inputTokens
        OutputTokens=$outputTokens
        CacheReadInputTokens=$cacheReadInputTokens
        CacheCreationInputTokens=$cacheCreationInputTokens
        TotalCostUsd=$totalCostUsd
        WebSearchRequests=$webSearchRequests
        WebFetchRequests=$webFetchRequests
    }
}

function Quote-ProcessArgument([string]$Value) {
    if ($null -eq $Value -or $Value.Length -eq 0) { return '""' }
    if ($Value -notmatch '[\s"]') { return $Value }
    $builder = New-Object System.Text.StringBuilder
    [void]$builder.Append('"')
    $slashes = 0
    foreach ($character in $Value.ToCharArray()) {
        if ($character -eq '\') {
            $slashes++
            continue
        }
        if ($character -eq '"') {
            [void]$builder.Append(('\' * (($slashes * 2) + 1)))
            [void]$builder.Append('"')
            $slashes = 0
            continue
        }
        if ($slashes -gt 0) {
            [void]$builder.Append(('\' * $slashes))
            $slashes = 0
        }
        [void]$builder.Append($character)
    }
    if ($slashes -gt 0) { [void]$builder.Append(('\' * ($slashes * 2))) }
    [void]$builder.Append('"')
    return $builder.ToString()
}

function Stop-ClaudeChildProcess {
    param([Parameter(Mandatory=$true)][System.Diagnostics.Process]$Process)
    if ($Process.HasExited) { return }
    if ($env:OS -eq 'Windows_NT' -and (Get-Command taskkill.exe -ErrorAction SilentlyContinue)) {
        & taskkill.exe /PID $Process.Id /T /F *> $null
    } else {
        try { $Process.Kill() } catch {}
    }
}

function Resolve-ModelIntegrityAction([int]$CycleAttempt) {
    if ($CycleAttempt -le 1) { return 'REGENERATE_AND_RETRY_REQUESTED_CLAUDE_MODEL' }
    return 'SAVE_AND_PAUSE_FOR_MANUAL_CONTINUATION'
}

function Invoke-ClaudeAttempt {
    param(
        [string]$Stage,
        [int]$Attempt,
        [int]$RetryCycle=0,
        [int]$CycleAttempt=1,
        [string]$ResumeSessionId='',
        [switch]$ClarifiedRetry,
        [string]$HandoffHistory=''
    )
    $cfg = $Stages[$Stage]
    $script:CurrentStage = $Stage
    $script:CurrentAttempt = $Attempt
    $script:CurrentRetryCycle = $RetryCycle
    $script:CurrentCycleAttempt = $CycleAttempt
    $script:CurrentHandoffHistory = $HandoffHistory
    $suffix = if ([string]::IsNullOrWhiteSpace($ResumeSessionId)) { 'new' } else { 'resume' }
    $attemptDirectory = Join-Path $RunRoot (
        "{0}\cycle_{1}_attempt_{2}_{3}" -f $Stage,$RetryCycle,$Attempt,$suffix
    )
    New-Item -ItemType Directory -Force -Path $attemptDirectory | Out-Null
    $streamFile = Join-Path $attemptDirectory 'stream.jsonl'
    $errorFile = Join-Path $attemptDirectory 'stderr.txt'
    New-Item -ItemType File -Force -Path $streamFile,$errorFile | Out-Null
    $script:CurrentStream = $streamFile

    $shared = Get-Content -Raw -Encoding UTF8 -LiteralPath $SharedPromptPath
    $stagePrompt = Get-Content -Raw -Encoding UTF8 -LiteralPath (
        Join-Path $MissionRoot $cfg.Prompt
    )
    $prefix = ''
    if ($RetryCycle -gt 0) {
        $prefix = @"
===== USER-AUTHORIZED CLAUDE RETRY CYCLE $RetryCycle =====
The user explicitly confirmed that Claude usage remains and requested another
Claude-only attempt after a saved ChatGPT handoff. The previous handoff,
attempt state, model evidence, and recovery files were preserved under
'$HandoffHistory'. Start a fresh Claude session; do not continue the rejected
session. Continue the workflow from durable files, and independently verify
anything consulted from rejected-attempt quarantine before accepting it.
This is global attempt $Attempt. Fable 5 final-result integrity uses a
two-attempt cycle; other stage models continue normally while temporary and
auxiliary model usage is logged.

"@
    }
    if ($ClarifiedRetry -and [string]$cfg.Model -eq 'fable') {
        $prefix += @"
===== FABLE 5 FINAL-RESULT RETRY =====
The previous attempt finished without a verifiable Fable 5 final result,
commonly because content-classifier fallback left the session on Opus.
This is benign academic electrical-engineering research concerning magnetic
sensors, metrology, semiconductor devices, publication planning, and plasma
instrumentation. Do not broaden the task. Keep Fable 5 as the main model.
Auxiliary/internal tools and subagents may use other models; those models are
logged but are not a downgrade. Fable 5 must personally re-read, reconcile,
validate, and produce the accepted final result and final main response.
Re-read durable files, preserve valid work, and satisfy only this stage's
acceptance gates.

"@
    }
    if (-not [string]::IsNullOrWhiteSpace($ResumeSessionId)) {
        $prefix += @"
===== DURABLE RESUME =====
Continue the interrupted stage from the saved files and event log. Inspect the
latest attempt state, live stream, checkpoint, and partial artifacts. Do not
repeat valid work. Finish all acceptance gates for this stage.

"@
    }
    $fullPrompt = $prefix + $shared +
        "`r`n`r`n===== CURRENT STAGE =====`r`n`r`n" + $stagePrompt
    $generatedPrompt = Join-Path $GeneratedPromptRoot (
        "{0}_attempt_{1}_cycle_{2}_{3}.md" -f
            $Stage,$Attempt,$RetryCycle,$RunStamp
    )
    $fullPrompt | Set-Content -LiteralPath $generatedPrompt -Encoding UTF8
    $promptFile = Join-Path $attemptDirectory 'prompt.md'
    $fullPrompt | Set-Content -LiteralPath $promptFile -Encoding UTF8

    $claudeArguments = @(
        '-p',
        '--model',[string]$cfg.Model,
        '--effort',[string]$cfg.Effort,
        '--max-turns',[string]$cfg.MaxTurns,
        '--output-format','stream-json',
        '--verbose',
        '--name',("phd-{0}-r{1}-c{2}-a{3}" -f
            $Stage,$RetryCycle,$CycleAttempt,$Attempt),
        '--setting-sources','project',
        '--disallowedTools','mcp__*',
        '--no-chrome'
    )
    if ($ClarifiedRetry -and [string]$cfg.Model -eq 'fable') {
        $claudeArguments += '--safe-mode'
    }
    if (-not [string]::IsNullOrWhiteSpace($ResumeSessionId)) {
        $claudeArguments += @('--resume',$ResumeSessionId)
    }
    if ($Mode -eq 'full') {
        $claudeArguments += @('--permission-mode','bypassPermissions')
    } else {
        $claudeArguments += @(
            '--permission-mode','acceptEdits',
            '--allowedTools','Read','Write','Edit','Glob','Grep','WebSearch',
            'WebFetch','PowerShell','Bash','TodoWrite','Task'
        )
    }
    $argumentsFile = Join-Path $attemptDirectory 'claude_arguments.json'
    ConvertTo-Json -InputObject @($claudeArguments) -Depth 5 |
        Set-Content -LiteralPath $argumentsFile -Encoding UTF8

    $startingDowngradeCount = if ([string]$cfg.Model -eq 'fable') {
        $CycleAttempt - 1
    } else {
        0
    }
    Set-AttemptState -Stage $Stage -Attempt $Attempt -Status 'CLAUDE_IN_PROGRESS' `
        -StreamFile $streamFile -SessionId $ResumeSessionId `
        -DowngradeCount $startingDowngradeCount -PromptFile $generatedPrompt `
        -Note 'Live Claude attempt started' -RetryCycle $RetryCycle `
        -CycleAttempt $CycleAttempt -HandoffHistory $HandoffHistory
    Add-OperationRecord -Stage $Stage -Operation 'attempt_started' -Attempt $Attempt `
        -Status 'CLAUDE_IN_PROGRESS' -RequestedModel ([string]$cfg.Model) `
        -RequestedEffort ([string]$cfg.Effort) -StreamFile $streamFile `
        -DowngradeCount $startingDowngradeCount -Checkpoint $HandoffJsonPath `
        -NextAction 'Continue Claude stage; manual stop is allowed because every event is flushed.' `
        -Notes ("retry_cycle={0};cycle_attempt={1};history={2}" -f
            $RetryCycle,$CycleAttempt,$HandoffHistory)
    Write-HandoffState -Status 'CLAUDE_IN_PROGRESS' -Stage $Stage -Attempt $Attempt `
        -StreamFile $streamFile -SessionId $ResumeSessionId `
        -DowngradeCount $startingDowngradeCount -GeneratedPrompt $generatedPrompt `
        -NextAction 'Claude is active. If PowerShell is stopped manually, rerun the same one-command launcher; it resumes from durable files.' `
        -RetryCycle $RetryCycle -CycleAttempt $CycleAttempt `
        -HandoffHistory $HandoffHistory

    $hostPath = (Get-Process -Id $PID).Path
    $childArguments = @(
        '-NoProfile',
        '-NonInteractive',
        '-ExecutionPolicy','Bypass',
        '-File',$ClaudeChildPath,
        '-PromptFile',$promptFile,
        '-ArgumentsFile',$argumentsFile,
        '-StreamFile',$streamFile,
        '-ErrorFile',$errorFile,
        '-EventLogFile',$EventLogPath,
        '-WorkingDirectory',$MissionRoot,
        '-Stage',$Stage,
        '-Attempt',[string]$Attempt,
        '-RequestedModel',[string]$cfg.Model,
        '-RequestedEffort',[string]$cfg.Effort
    )
    $startInfo = New-Object System.Diagnostics.ProcessStartInfo
    $startInfo.FileName = $hostPath
    $startInfo.Arguments = (
        @($childArguments | ForEach-Object { Quote-ProcessArgument ([string]$_) }) -join ' '
    )
    $startInfo.WorkingDirectory = $MissionRoot
    $startInfo.UseShellExecute = $false
    $startInfo.CreateNoWindow = $true

    $oldPowerShell = $env:CLAUDE_CODE_USE_POWERSHELL_TOOL
    $env:CLAUDE_CODE_USE_POWERSHELL_TOOL = '1'

    $process = New-Object System.Diagnostics.Process
    $process.StartInfo = $startInfo
    $watch = [Diagnostics.Stopwatch]::StartNew()
    [long]$lastLength = -1
    $metadata = $null
    try {
        if (-not $process.Start()) { throw 'Could not start Claude Code.' }
        while (-not $process.HasExited) {
            Start-Sleep -Milliseconds 750
            $process.Refresh()
            [long]$length = 0
            if (Test-Path -LiteralPath $streamFile -PathType Leaf) {
                $length = (Get-Item -LiteralPath $streamFile).Length
            }
            if ($length -ne $lastLength) {
                $lastLength = $length
                $metadata = Get-ClaudeStreamMetadata -StreamFile $streamFile `
                    -ErrorFile $errorFile -ExpectedModel ([string]$cfg.Model)
                Write-HandoffState -Status 'CLAUDE_IN_PROGRESS' -Stage $Stage `
                    -Attempt $Attempt -StreamFile $streamFile `
                    -SessionId (Get-SessionIdFromStream $streamFile) `
                    -ReportedModels $metadata.ModelsText `
                    -PrimaryModels $metadata.PrimaryModelsText `
                    -AuxiliaryModels $metadata.AuxiliaryModelsText `
                    -ResultModel $metadata.ResultModel `
                    -SecurityFallbackFlag $metadata.SecurityFallbackFlag `
                    -DowngradeCount $startingDowngradeCount -GeneratedPrompt $generatedPrompt `
                    -NextAction 'Claude is active; the raw event stream and event index are current.' `
                    -RetryCycle $RetryCycle -CycleAttempt $CycleAttempt `
                    -HandoffHistory $HandoffHistory
            }
        }
        try { $process.WaitForExit(5000) | Out-Null } catch {}
        $exitCode = if ($process.HasExited) { $process.ExitCode } else { 1 }
    } finally {
        $watch.Stop()
        if (-not $process.HasExited) { Stop-ClaudeChildProcess -Process $process }
        try { $process.Dispose() } catch {}
        if ($null -eq $oldPowerShell) {
            Remove-Item Env:CLAUDE_CODE_USE_POWERSHELL_TOOL -ErrorAction SilentlyContinue
        } else {
            $env:CLAUDE_CODE_USE_POWERSHELL_TOOL = $oldPowerShell
        }
    }
    $metadata = Get-ClaudeStreamMetadata -StreamFile $streamFile `
        -ErrorFile $errorFile -ExpectedModel ([string]$cfg.Model)
    $sessionId = Get-SessionIdFromStream $streamFile
    if ($metadata.EnforceModelIntegrity -and $metadata.Mismatch) {
        $integrity = 'model_mismatch'
    } elseif ($exitCode -ne 0) {
        $integrity = 'runtime_failure'
    } elseif ($metadata.EnforceModelIntegrity -and
        -not $metadata.ExpectedSeen) {
        $integrity = 'model_unverified'
    } else {
        $integrity = 'ok'
    }
    return [pscustomobject]@{
        Stage=$Stage
        Attempt=$Attempt
        RetryCycle=$RetryCycle
        CycleAttempt=$CycleAttempt
        ExitCode=$exitCode
        SessionId=$sessionId
        StreamFile=$streamFile
        ErrorFile=$errorFile
        GeneratedPrompt=$generatedPrompt
        Seconds=[math]::Round($watch.Elapsed.TotalSeconds,1)
        Integrity=$integrity
        ModelsText=$metadata.ModelsText
        PrimaryModelsText=$metadata.PrimaryModelsText
        AuxiliaryModelsText=$metadata.AuxiliaryModelsText
        TransientPrimaryModelsText=$metadata.TransientPrimaryModelsText
        ResultModel=$metadata.ResultModel
        InitModel=$metadata.InitModel
        SecurityFallbackFlag=$metadata.SecurityFallbackFlag
        ErrorText=$metadata.ErrorText
        NumTurns=$metadata.NumTurns
        InputTokens=$metadata.InputTokens
        OutputTokens=$metadata.OutputTokens
        CacheReadInputTokens=$metadata.CacheReadInputTokens
        CacheCreationInputTokens=$metadata.CacheCreationInputTokens
        TotalCostUsd=$metadata.TotalCostUsd
        WebSearchRequests=$metadata.WebSearchRequests
        WebFetchRequests=$metadata.WebFetchRequests
    }
}

function Save-SessionIndex {
    param([string]$Stage,[int]$Attempt,[string]$SessionId,
          [string]$StreamFile,[string]$Status)
    if (-not [string]::IsNullOrWhiteSpace($SessionId)) {
        $SessionId | Set-Content -LiteralPath (Get-SessionStatePath $Stage) -Encoding ASCII
    }
    Add-CsvRecord -Path $SessionIndexPath -Record ([pscustomobject]@{
        timestamp=Get-IsoTimestamp
        stage=$Stage
        route='claude_code_powershell'
        attempt=$Attempt
        session_id=$SessionId
        stream_file=$StreamFile
        status=$Status
    })
}

function Write-ModelRecord {
    param([string]$Stage,[int]$Attempt,[string]$RequestedModel,
          [string]$RequestedEffort,[string]$ReportedModels,[string]$Status,
          [string]$SessionId,[double]$Seconds,[string]$Validation,[string]$Notes)
    Add-CsvRecord -Path $ModelLogPath -Record ([pscustomobject]@{
        timestamp=Get-IsoTimestamp
        stage=$Stage
        route='claude_code_powershell'
        attempt=$Attempt
        requested_model=$RequestedModel
        requested_effort=$RequestedEffort
        reported_models=$ReportedModels
        status=$Status
        session_id=$SessionId
        seconds=$Seconds
        validation=$Validation
        notes=$Notes
    })
}

function Get-CurrentVerifiedSourceCount {
    $ledgerPath = Join-Path $MissionRoot 'outputs\01_SOURCE_LEDGER.csv'
    if (-not (Test-Path -LiteralPath $ledgerPath -PathType Leaf)) { return 0 }
    try {
        return @(
            Import-Csv -LiteralPath $ledgerPath | Where-Object {
                [string]$_.peer_review_status -eq 'verified_peer_reviewed'
            }
        ).Count
    } catch {
        return 0
    }
}

function Write-PerformanceRecord {
    param(
        [Parameter(Mandatory=$true)][object]$Result,
        [Parameter(Mandatory=$true)][object]$Config,
        [string]$Notes=''
    )
    Add-CsvRecord -Path $PerformanceLogPath -Record ([pscustomobject]@{
        timestamp=Get-IsoTimestamp
        stage=[string]$Result.Stage
        attempt=[int]$Result.Attempt
        requested_model=[string]$Config.Model
        requested_effort=[string]$Config.Effort
        duration_seconds=[double]$Result.Seconds
        num_turns=[int]$Result.NumTurns
        input_tokens=[int]$Result.InputTokens
        output_tokens=[int]$Result.OutputTokens
        cache_read_input_tokens=[int]$Result.CacheReadInputTokens
        cache_creation_input_tokens=[int]$Result.CacheCreationInputTokens
        total_cost_usd=[double]$Result.TotalCostUsd
        web_search_requests=[int]$Result.WebSearchRequests
        web_fetch_requests=[int]$Result.WebFetchRequests
        result_model=[string]$Result.ResultModel
        integrity=[string]$Result.Integrity
        verified_source_count=(Get-CurrentVerifiedSourceCount)
        notes=$Notes
    })
}

function Move-RejectedStageOutputs {
    param([string]$Stage,[int]$Attempt,[string]$Reason,
          [int]$RetryCycle=0,[int]$CycleAttempt=1)
    $destinationRoot = Join-Path $RunRoot (
        "{0}\rejected_attempt_{1}_outputs" -f $Stage,$Attempt
    )
    $moved = @()
    foreach ($relative in @($Stages[$Stage].Expected)) {
        $source = Join-Path $MissionRoot $relative
        if (-not (Test-Path -LiteralPath $source -PathType Leaf)) { continue }
        $destination = Join-Path $destinationRoot $relative
        New-Item -ItemType Directory -Force -Path (Split-Path -Parent $destination) |
            Out-Null
        Move-Item -LiteralPath $source -Destination $destination -Force
        $moved += $relative
    }
    $manifest = [ordered]@{
        stage=$Stage
        attempt=$Attempt
        retry_cycle=$RetryCycle
        cycle_attempt=$CycleAttempt
        reason=$Reason
        moved_files=@($moved)
        destination=$destinationRoot
        timestamp=Get-IsoTimestamp
    }
    Write-JsonAtomic -Path (Join-Path $destinationRoot 'QUARANTINE_MANIFEST.json') `
        -Value $manifest
    Add-HistoryRecord @{
        event='rejected_outputs_quarantined'
        stage=$Stage
        attempt=$Attempt
        retry_cycle=$RetryCycle
        cycle_attempt=$CycleAttempt
        reason=$Reason
        files=@($moved)
        destination=$destinationRoot
    }
    return $destinationRoot
}

function Test-CsvBatch {
    param([string]$Path,[int]$Minimum)
    try { $rows = @(Import-Csv -LiteralPath $Path) }
    catch { return [pscustomobject]@{Ok=$false;Message="CSV parse failed: $Path"} }
    if (@($rows).Count -eq 0) {
        return [pscustomobject]@{Ok=$false;Message="CSV is empty: $Path"}
    }
    $header = @($rows[0].PSObject.Properties.Name)
    if (($header -join ',') -ne ($RequiredLedgerHeader -join ',')) {
        return [pscustomobject]@{Ok=$false;Message="Ledger header is invalid: $Path"}
    }
    $verified = @($rows | Where-Object {
        [string]$_.peer_review_status -eq 'verified_peer_reviewed'
    })
    if (@($verified).Count -lt $Minimum) {
        return [pscustomobject]@{
            Ok=$false
            Message=("Verified peer-reviewed rows {0} < {1}: {2}" -f
                @($verified).Count,$Minimum,$Path)
        }
    }
    $ids = @($rows | ForEach-Object { [string]$_.source_id })
    if (@($ids | Where-Object { [string]::IsNullOrWhiteSpace($_) }).Count -gt 0) {
        return [pscustomobject]@{Ok=$false;Message="Blank source_id: $Path"}
    }
    if (@($ids | Select-Object -Unique).Count -ne @($ids).Count) {
        return [pscustomobject]@{Ok=$false;Message="Duplicate source_id: $Path"}
    }
    $normalizedDois = @(
        $rows | ForEach-Object {
            $value = ([string]$_.doi).Trim().ToLowerInvariant()
            $value = $value -replace '^https?://(dx\.)?doi\.org/',''
            if (-not [string]::IsNullOrWhiteSpace($value)) { $value }
        }
    )
    if (@($normalizedDois | Select-Object -Unique).Count -ne
        @($normalizedDois).Count) {
        return [pscustomobject]@{
            Ok=$false
            Message="Duplicate normalized DOI: $Path"
        }
    }
    $normalizedTitles = @(
        $rows | ForEach-Object {
            $value = (
                ([string]$_.title).ToLowerInvariant() -replace '[^a-z0-9]+',' '
            ).Trim()
            if (-not [string]::IsNullOrWhiteSpace($value)) { $value }
        }
    )
    if (@($normalizedTitles | Select-Object -Unique).Count -ne
        @($normalizedTitles).Count) {
        return [pscustomobject]@{
            Ok=$false
            Message="Duplicate normalized title: $Path"
        }
    }
    $invalidVerified = @(
        $verified | Where-Object {
            ([string]$_.source_type) -match
                '(?i)(preprint|arxiv|patent|standard|thesis|webpage|blog|book)' -or
            ([string]$_.quality_tier) -notin @('A','B','C') -or
            ([string]$_.access_level) -notin
                @('full_text','abstract_metadata','metadata_only') -or
            [string]::IsNullOrWhiteSpace([string]$_.title) -or
            [string]::IsNullOrWhiteSpace([string]$_.citation) -or
            [string]::IsNullOrWhiteSpace([string]$_.venue) -or
            [string]::IsNullOrWhiteSpace([string]$_.verification_basis) -or
            [string]::IsNullOrWhiteSpace([string]$_.topic_tags) -or
            [string]::IsNullOrWhiteSpace([string]$_.claims_supported) -or
            ([string]$_.year) -notmatch '^\d{4}$' -or
            (
                [string]::IsNullOrWhiteSpace([string]$_.doi) -and
                [string]::IsNullOrWhiteSpace([string]$_.url)
            )
        }
    )
    if (@($invalidVerified).Count -gt 0) {
        return [pscustomobject]@{
            Ok=$false
            Message=("{0} verified rows have an invalid type, tier, access level, identity, year, or required field: {1}" -f
                @($invalidVerified).Count,$Path)
        }
    }
    return [pscustomobject]@{
        Ok=$true
        Message=("{0} total rows; {1} verified peer-reviewed; metadata and uniqueness gates passed" -f
            @($rows).Count,@($verified).Count)
    }
}

function Test-FinalLedger([string]$Path) {
    $basic = Test-CsvBatch -Path $Path -Minimum 120
    if (-not $basic.Ok) { return $basic }
    $rows = @(Import-Csv -LiteralPath $Path)
    $verified = @($rows | Where-Object {
        [string]$_.peer_review_status -eq 'verified_peer_reviewed'
    })
    $topicRequirements = [ordered]@{
        hybrid_coil=@('(hybrid|inductive|coil|integrator|sensor fusion|kalman|rogowski|mirnov)',25)
        radiation=@('(radiation|irradiation|neutron|gamma|proton|displacement damage|transmutation|tid)',30)
        applications_alternatives=@('(tokamak|stellarator|z-pinch|magneto-inertial|motor|superconduct|fluxgate|sqUID|magnetoresist|fiber optic|nv center)',25)
        calibration_methods=@('(calibrat|observab|identif|uncertainty|estimat|fault|drift|compensat)',20)
    }
    foreach ($topic in $topicRequirements.Keys) {
        $pattern = [string]$topicRequirements[$topic][0]
        $minimum = [int]$topicRequirements[$topic][1]
        $count = @($verified | Where-Object {
            [string]$_.topic_tags -match $pattern
        }).Count
        if ($count -lt $minimum) {
            return [pscustomobject]@{
                Ok=$false
                Message=("Topic quota {0}: {1} < {2}" -f $topic,$count,$minimum)
            }
        }
    }

    $priorPath = Join-Path (Split-Path -Parent $MissionRoot) `
        '06\outputs\01_SOURCE_LEDGER.csv'
    if (Test-Path -LiteralPath $priorPath -PathType Leaf) {
        $priorRows = @(Import-Csv -LiteralPath $priorPath)
        $priorKeys = @{}
        foreach ($prior in $priorRows) {
            $doi = ([string]$prior.doi).Trim().ToLowerInvariant() `
                -replace '^https?://(dx\.)?doi\.org/',''
            $title = (([string]$prior.title).ToLowerInvariant() `
                -replace '[^a-z0-9]+',' ').Trim()
            if (-not [string]::IsNullOrWhiteSpace($doi)) {
                $priorKeys["doi:$doi"] = $true
            }
            if (-not [string]::IsNullOrWhiteSpace($title)) {
                $priorKeys["title:$title"] = $true
            }
        }
        $newCount = 0
        foreach ($row in $verified) {
            $doi = ([string]$row.doi).Trim().ToLowerInvariant() `
                -replace '^https?://(dx\.)?doi\.org/',''
            $title = (([string]$row.title).ToLowerInvariant() `
                -replace '[^a-z0-9]+',' ').Trim()
            $seen = (
                (-not [string]::IsNullOrWhiteSpace($doi) -and
                    $priorKeys.ContainsKey("doi:$doi")) -or
                (-not [string]::IsNullOrWhiteSpace($title) -and
                    $priorKeys.ContainsKey("title:$title"))
            )
            if (-not $seen) { $newCount++ }
        }
        if ($newCount -lt 75) {
            return [pscustomobject]@{
                Ok=$false
                Message=("Only {0} verified sources are new relative to folder 06; require 75" -f
                    $newCount)
            }
        }
    }
    return [pscustomobject]@{
        Ok=$true
        Message=("{0} total rows; 120-source, topic-quota, new-source, metadata, type, access, identity, and uniqueness gates passed" -f
            @($rows).Count)
    }
}

function Test-StageOutputs([string]$Stage) {
    $missing = @()
    foreach ($relative in @($Stages[$Stage].Expected)) {
        $path = Join-Path $MissionRoot $relative
        if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
            $missing += $relative
        } elseif ((Get-Item -LiteralPath $path).Length -lt 40) {
            $missing += ("{0} (empty/too small)" -f $relative)
        }
    }
    if (@($missing).Count -gt 0) {
        return [pscustomobject]@{
            Ok=$false
            Message=("Missing or empty: " + ($missing -join '; '))
        }
    }
    switch ($Stage) {
        '10a_literature_hybrid' {
            return (Test-CsvBatch -Path (Join-Path $MissionRoot 'evidence\10A_HYBRID_SOURCES.csv') -Minimum 40)
        }
        '10b_literature_radiation' {
            return (Test-CsvBatch -Path (Join-Path $MissionRoot 'evidence\10B_RADIATION_SOURCES.csv') -Minimum 45)
        }
        '10c_literature_applications' {
            return (Test-CsvBatch -Path (Join-Path $MissionRoot 'evidence\10C_APPLICATION_SOURCES.csv') -Minimum 40)
        }
        '10d_evidence_merge' {
            return (Test-FinalLedger -Path (Join-Path $MissionRoot 'outputs\01_SOURCE_LEDGER.csv'))
        }
        '70_redteam' {
            try {
                $audit = @(Import-Csv -LiteralPath (Join-Path $MissionRoot 'outputs\07_SOURCE_AUDIT.csv'))
            } catch {
                return [pscustomobject]@{Ok=$false;Message='Source-audit CSV parse failed'}
            }
            if (@($audit).Count -lt 30) {
                return [pscustomobject]@{Ok=$false;Message='Source audit contains fewer than 30 rows'}
            }
        }
        '80_synthesis' {
            $last = (Get-Content -LiteralPath (
                Join-Path $MissionRoot 'outputs\FINAL_AUDIT.md'
            ) -Tail 1).Trim()
            if ($last -ne 'FINAL STATUS: PASS') {
                return [pscustomobject]@{
                    Ok=$false
                    Message=("FINAL_AUDIT.md ends with '{0}'" -f $last)
                }
            }
            $ledger = Test-FinalLedger -Path (
                Join-Path $MissionRoot 'outputs\01_SOURCE_LEDGER.csv'
            )
            if (-not $ledger.Ok) { return $ledger }
        }
    }
    return [pscustomobject]@{
        Ok=$true
        Message='Required files exist and stage-specific checks passed'
    }
}

function Save-CompletionMarker {
    param([string]$Stage,[int]$Attempt,[string]$Model,[string]$Effort,
          [string]$SessionId,[string]$Validation,[int]$RetryCycle=0,
          [int]$CycleAttempt=1,[string]$HandoffHistory='',
          [string]$PrimaryModels='',[string]$AuxiliaryModels='',
          [string]$ResultModel='',
          [bool]$SecurityFallbackFlag=$false,[int]$DowngradeCount=0)
    $hashes = @()
    foreach ($relative in @($Stages[$Stage].Expected)) {
        $hash = Get-FileHash -LiteralPath (Join-Path $MissionRoot $relative) `
            -Algorithm SHA256
        $hashes += [ordered]@{
            path=$relative
            sha256=$hash.Hash.ToLowerInvariant()
        }
    }
    $requiredFinalModel = [string]$Stages[$Stage].Model
    if ($requiredFinalModel -eq 'fable' -and
        $ResultModel -notmatch '(?i)fable') {
        throw "Cannot complete Fable-assigned stage $Stage without a Fable final result model."
    }
    $markerModel = if ([string]::IsNullOrWhiteSpace($ResultModel)) {
        $Model
    } else {
        $ResultModel
    }
    $marker = [ordered]@{
        stage=$Stage
        status='complete'
        completed_at=Get-IsoTimestamp
        route='claude_code_powershell'
        attempt=$Attempt
        retry_cycle=$RetryCycle
        cycle_attempt=$CycleAttempt
        model=$markerModel
        reported_models=$Model
        primary_models=$PrimaryModels
        auxiliary_models=$AuxiliaryModels
        result_model=$ResultModel
        model_policy_scope='fable_final_result_only'
        security_fallback_flag=$SecurityFallbackFlag
        effort=$Effort
        session_id=$SessionId
        validation=$Validation
        outputs=$hashes
    }
    Write-JsonAtomic -Path (Get-StageMarkerPath $Stage) -Value $marker
    Set-AttemptState -Stage $Stage -Attempt $Attempt -Status 'COMPLETE' `
        -SessionId $SessionId -ReportedModels $Model `
        -PrimaryModels $PrimaryModels -AuxiliaryModels $AuxiliaryModels `
        -ResultModel $ResultModel `
        -SecurityFallbackFlag $SecurityFallbackFlag `
        -DowngradeCount $DowngradeCount -Note $Validation `
        -RetryCycle $RetryCycle -CycleAttempt $CycleAttempt `
        -HandoffHistory $HandoffHistory
}

function Resolve-SelectedStages {
    [object[]]$all = @($Stages.Keys)
    if ($null -ne $OnlyStage -and @($OnlyStage).Count -gt 0) {
        $selected = @()
        foreach ($token in $OnlyStage) {
            $matches = @($all | Where-Object {
                [string]$_ -eq $token -or [string]$_ -like "$token*"
            })
            if (@($matches).Count -eq 0) {
                throw "OnlyStage token '$token' matched no stage."
            }
            foreach ($match in $matches) {
                if ($selected -notcontains $match) { $selected += $match }
            }
        }
        return @($selected)
    }
    if (-not [string]::IsNullOrWhiteSpace($FromStage)) {
        $matches = @($all | Where-Object {
            [string]$_ -eq $FromStage -or [string]$_ -like "$FromStage*"
        })
        if (@($matches).Count -eq 0) {
            throw "FromStage '$FromStage' matched no stage."
        }
        $start = [array]::IndexOf($all,$matches[0])
        return @($all[$start..($all.Count - 1)])
    }
    return @($all)
}

function Test-Forced([string]$Stage) {
    if ($null -eq $ForceStage) { return $false }
    foreach ($token in @($ForceStage)) {
        if ($Stage -eq $token -or $Stage -like "$token*") { return $true }
    }
    return $false
}

function Test-PackageBaseline {
    $required = @(
        'README_START.md','MISSION.md','CLAUDE.md','AGENTS.md',
        'EXECUTION_PLAN.md','MODEL_POLICY.md','SOURCE_POLICY.md',
        'CHECKPOINT_PROTOCOL.md','PACKAGE_MANIFEST.md','PACKAGE_VALIDATION.md',
        'VALIDATE_PACKAGE.ps1','OFFICIAL_SETUP_REFERENCES.md',
        'LITERATURE_SEEDS.md','DECISION_FRAMEWORK.md',
        'TEST_CLAUDE_MODELS.ps1','INVOKE_CLAUDE_CHILD.ps1',
        'RUN_HYBRID_RADIATION_ANALYSIS.ps1',
        'prompts\_shared_system.md','prompts\00_inventory.md',
        'prompts\10a_literature_hybrid.md',
        'prompts\10b_literature_radiation.md',
        'prompts\10c_literature_applications.md',
        'prompts\10d_evidence_merge.md','prompts\20_observability.md',
        'prompts\30_radiation_compensation.md',
        'prompts\40_applications_collaboration.md',
        'prompts\50_limitations_comparison.md',
        'prompts\60_research_program.md','prompts\70_redteam.md',
        'prompts\80_synthesis.md'
    )
    foreach ($relative in $required) {
        if (-not (Test-Path -LiteralPath (Join-Path $MissionRoot $relative) -PathType Leaf)) {
            throw "Package baseline is incomplete; missing $relative"
        }
    }
    if (-not (Test-Path -LiteralPath (
        Join-Path $ResearchRoot '06\outputs\01_SOURCE_LEDGER.csv'
    ) -PathType Leaf)) {
        throw 'Folder 06 source ledger is missing.'
    }
    if (-not (Test-Path -LiteralPath (
        Join-Path $ResearchRoot '07_HSX_august2025_results'
    ) -PathType Container)) {
        throw 'Extracted HSX result folder is missing.'
    }
}

function Invoke-Preflight {
    Write-Section 'Preflight'
    $hostPath = (Get-Process -Id $PID).Path
    $validationArguments = @(
        '-NoProfile','-NonInteractive','-ExecutionPolicy','Bypass',
        '-File',(Join-Path $MissionRoot 'VALIDATE_PACKAGE.ps1')
    )
    & $hostPath @validationArguments
    if ($LASTEXITCODE -ne 0) { throw 'Package validation did not pass.' }
    Test-PackageBaseline
    Write-Host 'PASS: package structure, PowerShell, model policy, folder 06 evidence, and HSX context validated.' -ForegroundColor Green
    if ($DryRun) { return }

    $claudeCommand = Get-Command claude -ErrorAction SilentlyContinue
    if ($null -eq $claudeCommand) {
        throw 'Claude Code is not on PATH. Install or restore Claude Code; the manual continuation snapshot preserves the exact restart point.'
    }
    $oldPreference = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    try {
        $versionText = (& claude --version 2>&1 | Out-String).Trim()
        if ($LASTEXITCODE -ne 0 -or $versionText -notmatch '(\d+\.\d+\.\d+)') {
            throw 'Claude Code did not return a usable version.'
        }
        $version = [version]$Matches[1]
        if ($version -lt $MinClaudeVersion) {
            throw "Claude Code $version is older than required version $MinClaudeVersion."
        }
        $authText = (& claude auth status --text 2>&1 | Out-String)
        if ($LASTEXITCODE -ne 0) {
            throw 'Claude Code is not authenticated.'
        }
    } finally {
        $ErrorActionPreference = $oldPreference
    }
    Write-Host ("Claude Code: {0}" -f $versionText)
    Write-Host 'Claude authentication: OK' -ForegroundColor Green
    Write-Host 'Usage is not polled and quiet processes are not timed out. Stop PowerShell manually if needed; durable event logs are continuously flushed.'
}

function Invoke-PolicySelfTest {
    Write-Section 'Policy self-test'
    if ((Resolve-ModelIntegrityAction 1) -ne 'REGENERATE_AND_RETRY_REQUESTED_CLAUDE_MODEL') {
        throw 'First-downgrade transition is incorrect.'
    }
    if ((Resolve-ModelIntegrityAction 2) -ne 'SAVE_AND_PAUSE_FOR_MANUAL_CONTINUATION') {
        throw 'Second-downgrade transition is incorrect.'
    }
    foreach ($name in @($Stages.Keys)) {
        $cfg = $Stages[$name]
        if ([string]$cfg.Model -notin @('sonnet','fable')) {
            throw "Stage $name is not Claude-only."
        }
    }
    $selfTestRoot = Join-Path $RunRoot 'model_policy'
    New-Item -ItemType Directory -Force -Path $selfTestRoot | Out-Null
    $emptyError = Join-Path $selfTestRoot 'stderr.txt'
    New-Item -ItemType File -Force -Path $emptyError | Out-Null

    $sonnetAuxiliary = Join-Path $selfTestRoot 'sonnet_with_haiku_aux.jsonl'
    @(
        '{"type":"system","subtype":"init","model":"claude-sonnet-5"}',
        '{"type":"assistant","message":{"model":"claude-sonnet-5","content":[]}}',
        '{"type":"result","modelUsage":{"claude-sonnet-5":{},"claude-haiku-4-5-20251001":{"webSearchRequests":1}}}'
    ) | Set-Content -LiteralPath $sonnetAuxiliary -Encoding UTF8
    $sonnetMetadata = Get-ClaudeStreamMetadata -StreamFile $sonnetAuxiliary `
        -ErrorFile $emptyError -ExpectedModel 'sonnet'
    if ($sonnetMetadata.EnforceModelIntegrity -or $sonnetMetadata.Mismatch -or
        $sonnetMetadata.AuxiliaryModelsText -notmatch '(?i)haiku') {
        throw 'Sonnet plus auxiliary Haiku must be logged without downgrade enforcement.'
    }

    $fableAuxiliary = Join-Path $selfTestRoot 'fable_with_opus_aux.jsonl'
    @(
        '{"type":"system","subtype":"init","model":"claude-fable-5"}',
        '{"type":"assistant","message":{"model":"claude-fable-5","content":[]}}',
        '{"type":"result","modelUsage":{"claude-fable-5":{},"claude-opus-5":{}}}'
    ) | Set-Content -LiteralPath $fableAuxiliary -Encoding UTF8
    $fableAuxMetadata = Get-ClaudeStreamMetadata -StreamFile $fableAuxiliary `
        -ErrorFile $emptyError -ExpectedModel 'fable'
    if (-not $fableAuxMetadata.EnforceModelIntegrity -or
        $fableAuxMetadata.Mismatch -or
        $fableAuxMetadata.AuxiliaryModelsText -notmatch '(?i)opus') {
        throw 'Auxiliary Opus usage must not count as a Fable final-result failure.'
    }

    $fableTemporary = Join-Path $selfTestRoot 'fable_temporary_opus_then_fable.jsonl'
    @(
        '{"type":"system","subtype":"init","model":"claude-fable-5"}',
        '{"type":"assistant","message":{"model":"claude-opus-5","content":[]}}',
        '{"type":"assistant","message":{"model":"claude-fable-5","content":[]}}'
    ) | Set-Content -LiteralPath $fableTemporary -Encoding UTF8
    $fableTemporaryMetadata = Get-ClaudeStreamMetadata -StreamFile $fableTemporary `
        -ErrorFile $emptyError -ExpectedModel 'fable'
    if ($fableTemporaryMetadata.Mismatch -or
        $fableTemporaryMetadata.ResultModel -notmatch '(?i)fable' -or
        $fableTemporaryMetadata.TransientPrimaryModelsText -notmatch '(?i)opus') {
        throw 'A temporary Opus adjustment followed by a Fable final result must be allowed.'
    }

    $fableFallback = Join-Path $selfTestRoot 'fable_primary_fallback.jsonl'
    @(
        '{"type":"system","subtype":"init","model":"claude-fable-5"}',
        '{"type":"system","subtype":"model_fallback","notice":"Safety classifier flagged the request; re-run using Opus fallback."}',
        '{"type":"assistant","message":{"model":"claude-opus-5","content":[]}}'
    ) | Set-Content -LiteralPath $fableFallback -Encoding UTF8
    $fableFallbackMetadata = Get-ClaudeStreamMetadata -StreamFile $fableFallback `
        -ErrorFile $emptyError -ExpectedModel 'fable'
    if (-not $fableFallbackMetadata.Mismatch -or
        $fableFallbackMetadata.ResultModel -notmatch '(?i)opus' -or
        $fableFallbackMetadata.PrimaryModelsText -notmatch '(?i)opus' -or
        -not $fableFallbackMetadata.SecurityFallbackFlag) {
        throw 'A Fable main-session fallback to Opus must trigger downgrade tracking.'
    }

    Write-Host 'PASS: only a non-Fable final result on a Fable-assigned stage enforces downgrade transitions.' -ForegroundColor Green
    Write-Host 'PASS: temporary and auxiliary model adjustments are logged and allowed.' -ForegroundColor Green
    Write-Host 'PASS: Fable must produce the accepted result; first failure retries in safe mode and second pauses at a durable manual checkpoint.' -ForegroundColor Green
    Write-Host 'PASS: all 12 stages are Claude-only; manual continuation never auto-routes to another provider.' -ForegroundColor Green
}

try {
    Initialize-StateFiles
    New-Item -ItemType Directory -Force -Path $RunRoot | Out-Null
    if ($SelfTest) {
        Invoke-PolicySelfTest
        exit 0
    }
    Invoke-Preflight
    $selectedStages = @(Resolve-SelectedStages)

    Write-Section 'Execution plan'
    foreach ($stage in @($Stages.Keys)) {
        $cfg = $Stages[$stage]
        $selected = $selectedStages -contains $stage
        $done = Test-Path -LiteralPath (Get-StageMarkerPath $stage) -PathType Leaf
        $forced = Test-Forced $stage
        $action = if (-not $selected) { 'not selected' }
                  elseif ($done -and -not $forced) { 'skip: complete' }
                  elseif ($forced) { 'RUN: forced' }
                  else { 'RUN' }
        Write-Host ("{0,-32} claude={1}/{2} {3}" -f
            $stage,$cfg.Model,$cfg.Effort,$action)
    }
    $pendingStage = Get-NextIncompleteStage
    $pendingState = if ([string]::IsNullOrWhiteSpace($pendingStage)) {
        $null
    } else {
        Read-AttemptState $pendingStage
    }
    $pendingHandoff = (
        $null -ne $pendingState -and
        [string]$pendingState.status -eq 'MANUAL_CONTINUATION_REQUIRED'
    )
    if (-not $pendingHandoff) {
        Write-HandoffState -Status 'READY_IF_NEEDED' `
            -NextAction 'Run Claude with RUN_HYBRID_RADIATION_ANALYSIS.ps1; the same command resumes after interruption.'
    } elseif ($RetryClaudeAfterHandoff) {
        Write-Host 'Explicit Claude retry authorization detected; the existing handoff snapshot will be archived before it is changed.' -ForegroundColor Yellow
    } else {
        Write-Host 'Existing ChatGPT handoff snapshot preserved. Use -RetryClaudeAfterHandoff only when you explicitly want a fresh Claude retry cycle.' -ForegroundColor Yellow
    }
    if ($DryRun) {
        Add-OperationRecord -Operation 'dry_run_completed' -Status 'PASS' `
            -Checkpoint $HandoffJsonPath -NextAction 'Run the same command without -DryRun.'
        Write-Host ''
        Write-Host 'Dry run complete; no model was invoked and no research output was changed.' -ForegroundColor Yellow
        exit 0
    }

    $stopForHandoff = $false
    foreach ($stage in @($Stages.Keys)) {
        if ($selectedStages -notcontains $stage) { continue }
        $script:CurrentStage = $stage
        $cfg = $Stages[$stage]
        $markerPath = Get-StageMarkerPath $stage
        $forced = Test-Forced $stage
        if ((Test-Path -LiteralPath $markerPath -PathType Leaf) -and -not $forced) {
            continue
        }
        if ($forced -and (Test-Path -LiteralPath $markerPath -PathType Leaf)) {
            Move-Item -LiteralPath $markerPath -Destination (
                "{0}.superseded.{1}" -f $markerPath,$RunStamp
            ) -Force
        }

        Write-Section $stage
        $attempt = 1
        $retryCycle = 0
        $cycleAttempt = 1
        $handoffHistory = ''
        $script:CurrentRetryCycle = $retryCycle
        $script:CurrentCycleAttempt = $cycleAttempt
        $script:CurrentHandoffHistory = $handoffHistory
        $resumeSessionId = ''
        $attemptState = Read-AttemptState $stage
        if ($Resume -and $null -ne $attemptState) {
            $savedStatus = [string]$attemptState.status
            $retryCycle = Get-IntegerProperty -InputObject $attemptState `
                -Name 'retry_cycle' -Default 0
            $savedAttemptNumber = Get-IntegerProperty -InputObject $attemptState `
                -Name 'attempt' -Default 1
            $defaultCycleAttempt = if ($savedAttemptNumber -gt 1) { 2 } else { 1 }
            $cycleAttempt = Get-IntegerProperty -InputObject $attemptState `
                -Name 'cycle_attempt' -Default $defaultCycleAttempt
            $handoffHistory = Get-StringProperty -InputObject $attemptState `
                -Name 'handoff_history' -Default ''
            if ($savedStatus -eq 'MANUAL_CONTINUATION_REQUIRED') {
                if (-not $RetryClaudeAfterHandoff) {
                    Write-HandoffState -Status 'MANUAL_CONTINUATION_REQUIRED' -Stage $stage `
                        -Attempt ([int]$attemptState.attempt) -Reason ([string]$attemptState.note) `
                        -StreamFile ([string]$attemptState.stream_file) `
                        -SessionId ([string]$attemptState.session_id) `
                        -ReportedModels ([string]$attemptState.reported_models) `
                        -DowngradeCount ([int]$attemptState.downgrade_count) `
                        -GeneratedPrompt ([string]$attemptState.generated_prompt) `
                        -NextAction 'Review the saved checkpoint. Rerun with -RetryClaudeAfterHandoff only after explicitly authorizing a fresh Claude-only cycle.' `
                        -RetryCycle $retryCycle -CycleAttempt $cycleAttempt `
                        -HandoffHistory $handoffHistory
                    Write-Warning 'This stage is paused at a durable manual checkpoint. Claude was not restarted because no explicit retry switch was supplied.'
                    $stopForHandoff = $true
                    break
                }

                $retryCycle += 1
                $handoffHistory = Save-HandoffHistory -Stage $stage `
                    -AttemptState $attemptState -RetryCycle $retryCycle
                $previousAttempt = Get-IntegerProperty -InputObject $attemptState `
                    -Name 'attempt' -Default 0
                $attempt = $previousAttempt + 1
                $cycleAttempt = 1
                $resumeSessionId = ''
                $script:CurrentRetryCycle = $retryCycle
                $script:CurrentCycleAttempt = $cycleAttempt
                $script:CurrentHandoffHistory = $handoffHistory
                Set-AttemptState -Stage $stage -Attempt $attempt `
                    -Status 'CLAUDE_RETRY_AUTHORIZED' -DowngradeCount 0 `
                    -Note 'USER_CONFIRMED_CLAUDE_USAGE_AVAILABLE' `
                    -RetryCycle $retryCycle -CycleAttempt $cycleAttempt `
                    -HandoffHistory $handoffHistory
                Write-HandoffState -Status 'CLAUDE_RETRY_AUTHORIZED' -Stage $stage `
                    -Attempt $attempt -Reason 'USER_CONFIRMED_CLAUDE_USAGE_AVAILABLE' `
                    -DowngradeCount 0 `
                    -NextAction 'Start a fresh Claude session for the current stage from durable files; do not resume the rejected session.' `
                    -RetryCycle $retryCycle -CycleAttempt $cycleAttempt `
                    -HandoffHistory $handoffHistory
                Add-OperationRecord -Stage $stage `
                    -Operation 'user_authorized_claude_retry' `
                    -Attempt $attempt -Status 'CLAUDE_RETRY_AUTHORIZED' `
                    -RequestedModel ([string]$cfg.Model) `
                    -RequestedEffort ([string]$cfg.Effort) `
                    -DowngradeCount 0 -Checkpoint $handoffHistory `
                    -NextAction 'Start a fresh Claude session for this stage.' `
                    -Notes ("retry_cycle={0};previous_attempt={1};new_session=true" -f
                        $retryCycle,$previousAttempt)
                Write-Section 'User-authorized Claude retry'
                Write-Host ("Archived the prior handoff at {0}" -f $handoffHistory) -ForegroundColor Green
                Write-Host ("Starting retry cycle {0}, global attempt {1}, in a fresh Claude session." -f
                    $retryCycle,$attempt) -ForegroundColor Yellow
            }
            if ($savedStatus -eq 'MODEL_RETRY_PENDING') {
                $attempt = Get-IntegerProperty -InputObject $attemptState `
                    -Name 'attempt' -Default 2
                $cycleAttempt = Get-IntegerProperty -InputObject $attemptState `
                    -Name 'cycle_attempt' -Default 2
            } elseif ($savedStatus -ne 'COMPLETE') {
                if ($savedStatus -ne 'MANUAL_CONTINUATION_REQUIRED') {
                    $attempt = Get-IntegerProperty -InputObject $attemptState `
                        -Name 'attempt' -Default 1
                    $resumeSessionId = Get-LatestSessionId $stage
                    if (-not [string]::IsNullOrWhiteSpace($resumeSessionId)) {
                        Write-Host ("Resuming Claude session {0}" -f $resumeSessionId) -ForegroundColor Yellow
                    } else {
                        Write-Warning 'No session ID was available; durable files will be continued in a fresh Claude session.'
                    }
                }
            }
        }

        $stageComplete = $false
        while (-not $stageComplete -and $cycleAttempt -le 2) {
            $clarified = (
                $cycleAttempt -eq 2 -and [string]$cfg.Model -eq 'fable'
            )
            $result = Invoke-ClaudeAttempt -Stage $stage -Attempt $attempt `
                -RetryCycle $retryCycle -CycleAttempt $cycleAttempt `
                -ResumeSessionId $resumeSessionId -ClarifiedRetry:$clarified `
                -HandoffHistory $handoffHistory
            $resumeSessionId = ''
            $trackedDowngrade = (
                [string]$cfg.Model -eq 'fable' -and
                $result.Integrity -in @('model_mismatch','model_unverified')
            )
            $downgradeCount = if ($trackedDowngrade) {
                $cycleAttempt
            } elseif ([string]$cfg.Model -eq 'fable') {
                $cycleAttempt - 1
            } else {
                0
            }
            $integrityNextAction = if ($trackedDowngrade) {
                Resolve-ModelIntegrityAction $cycleAttempt
            } elseif ($result.Integrity -eq 'ok') {
                'VALIDATE_STAGE_OUTPUTS'
            } else {
                'SAVE_FOR_MANUAL_CONTINUATION'
            }
            $modelEvidenceNote = (
                "primary_models={0};transient_primary_models={1};auxiliary_models={2};result_model={3};policy_scope=fable_final_result_only;security_fallback_flag={4}" -f
                $result.PrimaryModelsText,$result.TransientPrimaryModelsText,
                $result.AuxiliaryModelsText,$result.ResultModel,
                $result.SecurityFallbackFlag
            )
            Save-SessionIndex -Stage $stage -Attempt $attempt `
                -SessionId $result.SessionId -StreamFile $result.StreamFile `
                -Status $result.Integrity
            Write-ModelRecord -Stage $stage -Attempt $attempt `
                -RequestedModel ([string]$cfg.Model) `
                -RequestedEffort ([string]$cfg.Effort) `
                -ReportedModels $result.ModelsText -Status $result.Integrity `
                -SessionId $result.SessionId -Seconds $result.Seconds `
                -Validation 'not_yet_run' `
                -Notes ("{0};retry_cycle={1};cycle_attempt={2};{3}" -f
                    $result.ErrorText,$retryCycle,$cycleAttempt,$modelEvidenceNote)
            Write-PerformanceRecord -Result $result -Config $cfg `
                -Notes ("retry_cycle={0};cycle_attempt={1};security_fallback_flag={2}" -f
                    $retryCycle,$cycleAttempt,$result.SecurityFallbackFlag)
            Add-OperationRecord -Stage $stage -Operation 'attempt_finished' `
                -Attempt $attempt -Status $result.Integrity `
                -RequestedModel ([string]$cfg.Model) `
                -RequestedEffort ([string]$cfg.Effort) `
                -ReportedModels $result.ModelsText `
                -DowngradeFlag $trackedDowngrade `
                -DowngradeCount $downgradeCount -SessionId $result.SessionId `
                -StreamFile $result.StreamFile -Checkpoint $HandoffJsonPath `
                -NextAction $integrityNextAction `
                -Notes ("exit_code={0};retry_cycle={1};cycle_attempt={2};{3}" -f
                    $result.ExitCode,$retryCycle,$cycleAttempt,$modelEvidenceNote)
            Add-HistoryRecord @{
                event='attempt_finished'
                stage=$stage
                attempt=$attempt
                retry_cycle=$retryCycle
                cycle_attempt=$cycleAttempt
                exit_code=$result.ExitCode
                integrity=$result.Integrity
                models=$result.ModelsText
                primary_models=$result.PrimaryModelsText
                transient_primary_models=$result.TransientPrimaryModelsText
                auxiliary_models=$result.AuxiliaryModelsText
                result_model=$result.ResultModel
                model_policy_scope='fable_final_result_only'
                security_fallback_flag=$result.SecurityFallbackFlag
                session_id=$result.SessionId
                stream_file=$result.StreamFile
            }

            if ($trackedDowngrade) {
                $quarantine = Move-RejectedStageOutputs -Stage $stage -Attempt $attempt `
                    -Reason $result.Integrity -RetryCycle $retryCycle `
                    -CycleAttempt $cycleAttempt
                if ((Resolve-ModelIntegrityAction $cycleAttempt) -eq
                    'REGENERATE_AND_RETRY_REQUESTED_CLAUDE_MODEL') {
                    $nextAttempt = $attempt + 1
                    Set-AttemptState -Stage $stage -Attempt $nextAttempt `
                        -Status 'MODEL_RETRY_PENDING' -ReportedModels $result.ModelsText `
                        -PrimaryModels $result.PrimaryModelsText `
                        -AuxiliaryModels $result.AuxiliaryModelsText `
                        -ResultModel $result.ResultModel `
                        -SecurityFallbackFlag $result.SecurityFallbackFlag `
                        -DowngradeCount 1 -PromptFile $result.GeneratedPrompt `
                        -Note 'First non-Fable or unverifiable final result on a Fable-assigned stage checkpointed; a regenerated Fable 5 safe-mode retry is pending.' `
                        -RetryCycle $retryCycle -CycleAttempt 2 `
                        -HandoffHistory $handoffHistory
                    Write-HandoffState -Status 'CLAUDE_RETRY_PENDING' -Stage $stage `
                        -Attempt $nextAttempt -Reason 'FIRST_FABLE_FINAL_RESULT_FAILURE' `
                        -StreamFile $result.StreamFile -SessionId $result.SessionId `
                        -ReportedModels $result.ModelsText `
                        -PrimaryModels $result.PrimaryModelsText `
                        -AuxiliaryModels $result.AuxiliaryModelsText `
                        -ResultModel $result.ResultModel `
                        -SecurityFallbackFlag $result.SecurityFallbackFlag `
                        -DowngradeCount 1 `
                        -GeneratedPrompt $result.GeneratedPrompt `
                        -NextAction 'The first Fable-assigned attempt without a Fable final result was saved and quarantined. A clarified fresh Fable 5 session will retry once in safe mode.' `
                        -RetryCycle $retryCycle -CycleAttempt 2 `
                        -HandoffHistory $handoffHistory
                    Add-OperationRecord -Stage $stage -Operation 'first_downgrade_pause' `
                        -Attempt $attempt -Status 'MODEL_RETRY_PENDING' `
                        -RequestedModel ([string]$cfg.Model) `
                        -RequestedEffort ([string]$cfg.Effort) `
                        -ReportedModels $result.ModelsText -DowngradeFlag $true `
                        -DowngradeCount 1 -StreamFile $result.StreamFile `
                        -Checkpoint $HandoffJsonPath `
                        -NextAction 'Regenerate the prompt and retry the requested Claude model once.' `
                        -Notes ("Quarantined at {0};retry_cycle={1};next_global_attempt={2};{3}" -f
                            $quarantine,$retryCycle,$nextAttempt,$modelEvidenceNote)
                    Write-Section 'Fable 5 final-result pause and regenerated retry'
                    Write-Warning 'First Fable-assigned attempt without a verifiable Fable final result saved. Rebuilding the effective prompt and retrying Fable 5 once in a fresh safe-mode session.'
                    $attempt = $nextAttempt
                    $cycleAttempt = 2
                    continue
                }

                $reason = 'SECOND_FABLE_FINAL_RESULT_FAILURE'
                Set-AttemptState -Stage $stage -Attempt $attempt `
                    -Status 'MANUAL_CONTINUATION_REQUIRED' -StreamFile $result.StreamFile `
                    -SessionId $result.SessionId -ReportedModels $result.ModelsText `
                    -PrimaryModels $result.PrimaryModelsText `
                    -AuxiliaryModels $result.AuxiliaryModelsText `
                    -ResultModel $result.ResultModel `
                    -SecurityFallbackFlag $result.SecurityFallbackFlag `
                    -DowngradeCount 2 -PromptFile $result.GeneratedPrompt `
                    -Note $reason -RetryCycle $retryCycle `
                    -CycleAttempt $cycleAttempt -HandoffHistory $handoffHistory
                Write-HandoffState -Status 'MANUAL_CONTINUATION_REQUIRED' -Stage $stage `
                    -Attempt $attempt -Reason $reason -StreamFile $result.StreamFile `
                    -SessionId $result.SessionId -ReportedModels $result.ModelsText `
                    -PrimaryModels $result.PrimaryModelsText `
                    -AuxiliaryModels $result.AuxiliaryModelsText `
                    -ResultModel $result.ResultModel `
                    -SecurityFallbackFlag $result.SecurityFallbackFlag `
                    -DowngradeCount 2 -GeneratedPrompt $result.GeneratedPrompt `
                    -NextAction 'Stop Claude and review the saved evidence. If you later explicitly authorize another Claude-only cycle, rerun with -RetryClaudeAfterHandoff.' `
                    -RetryCycle $retryCycle -CycleAttempt $cycleAttempt `
                    -HandoffHistory $handoffHistory
                Add-OperationRecord -Stage $stage -Operation 'second_downgrade_handoff' `
                    -Attempt $attempt -Status 'MANUAL_CONTINUATION_REQUIRED' `
                    -RequestedModel ([string]$cfg.Model) `
                    -RequestedEffort ([string]$cfg.Effort) `
                    -ReportedModels $result.ModelsText -DowngradeFlag $true `
                    -DowngradeCount 2 -SessionId $result.SessionId `
                    -StreamFile $result.StreamFile -Checkpoint $HandoffJsonPath `
                    -NextAction 'Pause for manual review; do not silently substitute another model or provider.' `
                    -Notes ("Quarantined at {0};retry_cycle={1};cycle_attempt={2};{3}" -f
                        $quarantine,$retryCycle,$cycleAttempt,$modelEvidenceNote)
                $stopForHandoff = $true
                break
            }

            if ($result.Integrity -ne 'ok') {
                $reason = 'CLAUDE_RUNTIME_FAILURE_OR_MANUAL_STOP'
                Set-AttemptState -Stage $stage -Attempt $attempt `
                    -Status 'MANUAL_CONTINUATION_REQUIRED' -StreamFile $result.StreamFile `
                    -SessionId $result.SessionId -ReportedModels $result.ModelsText `
                    -PrimaryModels $result.PrimaryModelsText `
                    -AuxiliaryModels $result.AuxiliaryModelsText `
                    -ResultModel $result.ResultModel `
                    -SecurityFallbackFlag $result.SecurityFallbackFlag `
                    -DowngradeCount $downgradeCount `
                    -PromptFile $result.GeneratedPrompt -Note $reason `
                    -RetryCycle $retryCycle -CycleAttempt $cycleAttempt `
                    -HandoffHistory $handoffHistory
                Write-HandoffState -Status 'MANUAL_CONTINUATION_REQUIRED' -Stage $stage `
                    -Attempt $attempt -Reason $reason -StreamFile $result.StreamFile `
                    -SessionId $result.SessionId -ReportedModels $result.ModelsText `
                    -PrimaryModels $result.PrimaryModelsText `
                    -AuxiliaryModels $result.AuxiliaryModelsText `
                    -ResultModel $result.ResultModel `
                    -SecurityFallbackFlag $result.SecurityFallbackFlag `
                    -DowngradeCount $downgradeCount `
                    -GeneratedPrompt $result.GeneratedPrompt `
                    -NextAction 'Repair the named runtime issue or explicitly start a fresh Claude retry with -RetryClaudeAfterHandoff.' `
                    -RetryCycle $retryCycle -CycleAttempt $cycleAttempt `
                    -HandoffHistory $handoffHistory
                Add-OperationRecord -Stage $stage -Operation 'runtime_failure_handoff' `
                    -Attempt $attempt -Status 'MANUAL_CONTINUATION_REQUIRED' `
                    -RequestedModel ([string]$cfg.Model) `
                    -RequestedEffort ([string]$cfg.Effort) `
                    -ReportedModels $result.ModelsText `
                    -DowngradeCount $downgradeCount `
                    -SessionId $result.SessionId `
                    -StreamFile $result.StreamFile -Checkpoint $HandoffJsonPath `
                    -NextAction 'Repair the runtime issue or explicitly authorize a fresh Claude retry.' `
                    -Notes ("{0};retry_cycle={1};cycle_attempt={2};{3}" -f
                        $result.ErrorText,$retryCycle,$cycleAttempt,$modelEvidenceNote)
                $stopForHandoff = $true
                break
            }

            $validation = Test-StageOutputs $stage
            if (-not $validation.Ok) {
                Set-AttemptState -Stage $stage -Attempt $attempt `
                    -Status 'MANUAL_CONTINUATION_REQUIRED' -StreamFile $result.StreamFile `
                    -SessionId $result.SessionId -ReportedModels $result.ModelsText `
                    -PrimaryModels $result.PrimaryModelsText `
                    -AuxiliaryModels $result.AuxiliaryModelsText `
                    -ResultModel $result.ResultModel `
                    -SecurityFallbackFlag $result.SecurityFallbackFlag `
                    -DowngradeCount $downgradeCount `
                    -PromptFile $result.GeneratedPrompt `
                    -Note ("STAGE_VALIDATION_FAILED: {0}" -f $validation.Message) `
                    -RetryCycle $retryCycle -CycleAttempt $cycleAttempt `
                    -HandoffHistory $handoffHistory
                Write-HandoffState -Status 'MANUAL_CONTINUATION_REQUIRED' -Stage $stage `
                    -Attempt $attempt -Reason 'STAGE_VALIDATION_FAILED' `
                    -StreamFile $result.StreamFile -SessionId $result.SessionId `
                    -ReportedModels $result.ModelsText `
                    -PrimaryModels $result.PrimaryModelsText `
                    -AuxiliaryModels $result.AuxiliaryModelsText `
                    -ResultModel $result.ResultModel `
                    -SecurityFallbackFlag $result.SecurityFallbackFlag `
                    -DowngradeCount $downgradeCount `
                    -GeneratedPrompt $result.GeneratedPrompt `
                    -NextAction 'Repair only the failed acceptance gate, revalidate, and continue; or explicitly start a fresh Claude retry with -RetryClaudeAfterHandoff.' `
                    -RetryCycle $retryCycle -CycleAttempt $cycleAttempt `
                    -HandoffHistory $handoffHistory
                Write-ModelRecord -Stage $stage -Attempt $attempt `
                    -RequestedModel ([string]$cfg.Model) `
                    -RequestedEffort ([string]$cfg.Effort) `
                    -ReportedModels $result.ModelsText -Status 'validation_failed' `
                    -SessionId $result.SessionId -Seconds 0 `
                    -Validation $validation.Message `
                    -Notes ("Manual continuation checkpoint prepared;{0}" -f
                        $modelEvidenceNote)
                Add-OperationRecord -Stage $stage -Operation 'validation_failed_handoff' `
                    -Attempt $attempt -Status 'MANUAL_CONTINUATION_REQUIRED' `
                    -RequestedModel ([string]$cfg.Model) `
                    -RequestedEffort ([string]$cfg.Effort) `
                    -ReportedModels $result.ModelsText `
                    -DowngradeCount $downgradeCount `
                    -SessionId $result.SessionId `
                    -StreamFile $result.StreamFile -Checkpoint $HandoffJsonPath `
                    -NextAction 'Repair the failed gate, then rerun the validator and launcher.' `
                    -Notes ("{0};retry_cycle={1};cycle_attempt={2};{3}" -f
                        $validation.Message,$retryCycle,$cycleAttempt,$modelEvidenceNote)
                $stopForHandoff = $true
                break
            }

            Save-CompletionMarker -Stage $stage -Attempt $attempt `
                -Model $result.ModelsText -Effort ([string]$cfg.Effort) `
                -SessionId $result.SessionId -Validation $validation.Message `
                -RetryCycle $retryCycle -CycleAttempt $cycleAttempt `
                -HandoffHistory $handoffHistory `
                -PrimaryModels $result.PrimaryModelsText `
                -AuxiliaryModels $result.AuxiliaryModelsText `
                -ResultModel $result.ResultModel `
                -SecurityFallbackFlag $result.SecurityFallbackFlag `
                -DowngradeCount $downgradeCount
            Add-OperationRecord -Stage $stage -Operation 'stage_completed' `
                -Attempt $attempt -Status 'COMPLETE' `
                -RequestedModel ([string]$cfg.Model) `
                -RequestedEffort ([string]$cfg.Effort) `
                -ReportedModels $result.ModelsText `
                -DowngradeCount $downgradeCount `
                -SessionId $result.SessionId `
                -StreamFile $result.StreamFile -Checkpoint (Get-StageMarkerPath $stage) `
                -NextAction ("Proceed to {0}" -f $cfg.Next) `
                -Notes ("{0};retry_cycle={1};cycle_attempt={2};history={3};{4}" -f
                    $validation.Message,$retryCycle,$cycleAttempt,$handoffHistory,
                    $modelEvidenceNote)
            Write-HandoffState -Status 'READY_IF_NEEDED' `
                -NextAction ("Stage {0} is complete. Continue with {1}." -f $stage,$cfg.Next)
            Write-Host ("PASS: {0}" -f $validation.Message) -ForegroundColor Green
            $stageComplete = $true
        }
        if ($stopForHandoff -or -not $stageComplete) { break }
    }

    if ($stopForHandoff) {
        Write-Section 'Saved for manual continuation'
        Write-Host 'Claude was not routed to another provider. All current state is inside this folder.' -ForegroundColor Yellow
        Write-Host 'Review state\CHATGPT_HANDOFF.md. The same command resumes ordinary interruptions; an explicit -RetryClaudeAfterHandoff is required after a protected pause.' -ForegroundColor Yellow
        exit 2
    }

    $allComplete = [string]::IsNullOrWhiteSpace((Get-NextIncompleteStage))
    Write-Section 'Run summary'
    if ($allComplete) {
        Write-HandoffState -Status 'MISSION_COMPLETE' `
            -NextAction 'Review outputs\FINAL_EXECUTIVE_DECISION.md and outputs\FINAL_ACTION_PLAN.md.'
        Add-OperationRecord -Operation 'mission_completed' -Status 'COMPLETE' `
            -Checkpoint $HandoffJsonPath -NextAction 'Review final outputs.'
        Write-Host 'MISSION COMPLETE — all stage markers are present.' -ForegroundColor Green
    } else {
        Write-HandoffState -Status 'READY_IF_NEEDED' `
            -NextAction 'Selected stages completed; run the same command to continue remaining stages.'
        Write-Host 'Selected stages completed. Additional stages remain.' -ForegroundColor Yellow
    }
    exit 0
} catch {
    $message = $_.Exception.Message
    Write-Host ''
    Write-Host ("FATAL: {0}" -f $message) -ForegroundColor Red
    try {
        Add-HistoryRecord @{
            event='fatal'
            message=$message
            stage=$script:CurrentStage
            attempt=$script:CurrentAttempt
            retry_cycle=$script:CurrentRetryCycle
            cycle_attempt=$script:CurrentCycleAttempt
            handoff_history=$script:CurrentHandoffHistory
        }
        Add-OperationRecord -Stage $script:CurrentStage -Operation 'launcher_fatal' `
            -Attempt $script:CurrentAttempt -Status 'MANUAL_CONTINUATION_REQUIRED' `
            -StreamFile $script:CurrentStream -Checkpoint $HandoffJsonPath `
            -NextAction 'Repair the named prerequisite, then rerun the same launcher.' `
            -Notes ("{0};retry_cycle={1};cycle_attempt={2};history={3}" -f
                $message,$script:CurrentRetryCycle,
                $script:CurrentCycleAttempt,$script:CurrentHandoffHistory)
        Write-HandoffState -Status 'MANUAL_CONTINUATION_REQUIRED' `
            -Stage $script:CurrentStage -Attempt $script:CurrentAttempt `
            -Reason 'LAUNCHER_FATAL' -StreamFile $script:CurrentStream `
            -NextAction 'Continue from durable files after repairing the displayed prerequisite, or explicitly retry Claude with -RetryClaudeAfterHandoff.' `
            -RetryCycle $script:CurrentRetryCycle `
            -CycleAttempt $script:CurrentCycleAttempt `
            -HandoffHistory $script:CurrentHandoffHistory
    } catch {}
    Write-Host 'The current folder remains the recovery source. See state\CHATGPT_HANDOFF.md.' -ForegroundColor Yellow
    exit 1
}
