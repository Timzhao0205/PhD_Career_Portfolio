#requires -Version 5.1
[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)][string]$PromptFile,
    [Parameter(Mandatory=$true)][string]$ArgumentsFile,
    [Parameter(Mandatory=$true)][string]$StreamFile,
    [Parameter(Mandatory=$true)][string]$ErrorFile,
    [Parameter(Mandatory=$true)][string]$EventLogFile,
    [Parameter(Mandatory=$true)][string]$WorkingDirectory,
    [Parameter(Mandatory=$true)][string]$Stage,
    [Parameter(Mandatory=$true)][int]$Attempt,
    [Parameter(Mandatory=$true)][string]$RequestedModel,
    [Parameter(Mandatory=$true)][string]$RequestedEffort
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Continue'
$utf8 = New-Object System.Text.UTF8Encoding $false
$streamWriter = $null
$eventWriter = $null

function Get-EventSummary {
    param([object]$Event)
    $parts = @()
    if ($null -ne $Event -and $Event.PSObject.Properties['type']) {
        $parts += [string]$Event.type
    }
    if ($null -ne $Event -and $Event.PSObject.Properties['subtype']) {
        $parts += [string]$Event.subtype
    }
    if ($null -ne $Event -and $Event.PSObject.Properties['message'] -and
        $null -ne $Event.message -and
        $Event.message.PSObject.Properties['content']) {
        foreach ($content in @($Event.message.content)) {
            if ($null -eq $content) { continue }
            if ($content.PSObject.Properties['type'] -and
                [string]$content.type -eq 'tool_use') {
                $toolName = ''
                if ($content.PSObject.Properties['name']) {
                    $toolName = [string]$content.name
                }
                $parts += ("tool:{0}" -f $toolName)
            }
        }
    }
    $summary = ($parts -join '/')
    if ($summary.Length -gt 500) { $summary = $summary.Substring(0,500) }
    return $summary
}

function Get-EventModelMetadata {
    param(
        [object]$Event,
        [string]$RequestedModel
    )
    $models = @()
    $primaryModels = @()
    if ($null -eq $Event) {
        return [pscustomobject]@{
            Models=@()
            PrimaryModels=@()
            AuxiliaryModels=@()
            ResultModelCandidate=''
            FableNonfinalAdjustment=$false
        }
    }
    if ($Event.PSObject.Properties['model']) {
        $value = [string]$Event.model
        if (-not [string]::IsNullOrWhiteSpace($value)) { $models += $value }
        if ($Event.PSObject.Properties['type'] -and
            [string]$Event.type -eq 'system' -and
            $Event.PSObject.Properties['subtype'] -and
            [string]$Event.subtype -eq 'init' -and
            -not [string]::IsNullOrWhiteSpace($value)) {
            $primaryModels += $value
        }
    }
    if ($Event.PSObject.Properties['message'] -and
        $null -ne $Event.message -and
        $Event.message.PSObject.Properties['model']) {
        $value = [string]$Event.message.model
        if (-not [string]::IsNullOrWhiteSpace($value)) { $models += $value }
        $isSubagentEvent = $false
        if ($Event.PSObject.Properties['parent_tool_use_id']) {
            $isSubagentEvent = -not [string]::IsNullOrWhiteSpace(
                [string]$Event.parent_tool_use_id
            )
        }
        if (-not $isSubagentEvent -and
            -not [string]::IsNullOrWhiteSpace($value)) {
            $primaryModels += $value
        }
    }
    foreach ($usageName in @('modelUsage','model_usage')) {
        $usageProperty = $Event.PSObject.Properties[$usageName]
        if ($null -ne $usageProperty -and $null -ne $usageProperty.Value) {
            foreach ($property in $usageProperty.Value.PSObject.Properties) {
                if (-not [string]::IsNullOrWhiteSpace([string]$property.Name)) {
                    $models += [string]$property.Name
                }
            }
        }
    }
    $uniqueModels = @($models | Select-Object -Unique)
    $uniquePrimaryModels = @($primaryModels | Select-Object -Unique)
    $auxiliaryModels = @($uniqueModels | Where-Object {
        $uniquePrimaryModels -notcontains [string]$_
    })
    $resultModelCandidate = ''
    if (@($uniquePrimaryModels).Count -gt 0) {
        $resultModelCandidate = [string]$uniquePrimaryModels[-1]
    }
    $fableNonfinalAdjustment = (
        [string]$RequestedModel -match '(?i)fable' -and
        $resultModelCandidate -match '(?i)(opus|sonnet|haiku)'
    )
    return [pscustomobject]@{
        Models=$uniqueModels
        PrimaryModels=$uniquePrimaryModels
        AuxiliaryModels=$auxiliaryModels
        ResultModelCandidate=$resultModelCandidate
        FableNonfinalAdjustment=$fableNonfinalAdjustment
    }
}

try {
    $prompt = Get-Content -Raw -LiteralPath $PromptFile
    $decoded = Get-Content -Raw -LiteralPath $ArgumentsFile | ConvertFrom-Json
    $claudeArguments = @($decoded | ForEach-Object { [string]$_ })
    Set-Location -LiteralPath $WorkingDirectory

    $streamWriter = [System.IO.StreamWriter]::new(
        $StreamFile,$true,$utf8
    )
    $streamWriter.AutoFlush = $true
    $eventWriter = [System.IO.StreamWriter]::new(
        $EventLogFile,$true,$utf8
    )
    $eventWriter.AutoFlush = $true

    $prompt | & claude @claudeArguments 2> $ErrorFile | ForEach-Object {
        $line = [string]$_
        $streamWriter.WriteLine($line)
        $event = $null
        try { $event = $line | ConvertFrom-Json } catch {}
        $modelMetadata = Get-EventModelMetadata -Event $event `
            -RequestedModel $RequestedModel
        $models = @($modelMetadata.Models)
        $primaryModels = @($modelMetadata.PrimaryModels)
        $auxiliaryModels = @($modelMetadata.AuxiliaryModels)
        $fableNonfinalAdjustment = [bool]$modelMetadata.FableNonfinalAdjustment
        $sessionId = ''
        if ($null -ne $event -and $event.PSObject.Properties['session_id']) {
            $sessionId = [string]$event.session_id
        }
        $eventType = ''
        $eventSubtype = ''
        if ($null -ne $event -and $event.PSObject.Properties['type']) {
            $eventType = [string]$event.type
        }
        if ($null -ne $event -and $event.PSObject.Properties['subtype']) {
            $eventSubtype = [string]$event.subtype
        }
        $securityFallbackFlag = $false
        if ($eventType -in @('system','result') -and
            $line -match '(?i)(safety|classifier|flagged|content[- ]based).{0,240}(fallback|re-run|switch)|(?:fallback|re-run|switch).{0,240}(opus|safety|classifier|flagged)') {
            $securityFallbackFlag = $true
        }
        $eventSummary = Get-EventSummary -Event $event
        $indexEntry = [ordered]@{
            timestamp=(Get-Date).ToString('o')
            stage=$Stage
            operation=$eventSummary
            progress=$eventSummary
            route='claude_code_powershell'
            attempt=$Attempt
            status='STREAM_EVENT_FLUSHED'
            requested_model=$RequestedModel
            requested_effort=$RequestedEffort
            reported_models=($models -join ';')
            primary_models=($primaryModels -join ';')
            auxiliary_models=($auxiliaryModels -join ';')
            result_model_candidate=[string]$modelMetadata.ResultModelCandidate
            model_policy_scope='fable_final_result_only'
            downgrade_flag=$false
            fable_nonfinal_adjustment_flag=$fableNonfinalAdjustment
            security_fallback_flag=$securityFallbackFlag
            usage_flag='NOT_CHECKED_BY_RUNNER'
            inactivity_flag='NOT_CHECKED_BY_RUNNER'
            session_id=$sessionId
            event_type=$eventType
            event_subtype=$eventSubtype
            raw_stream=$StreamFile
        }
        $eventWriter.WriteLine(
            ($indexEntry | ConvertTo-Json -Depth 8 -Compress)
        )
        Write-Output $line
    }
    exit $LASTEXITCODE
} catch {
    ($_ | Out-String) | Add-Content -LiteralPath $ErrorFile -Encoding UTF8
    exit 1
} finally {
    if ($null -ne $streamWriter) { try { $streamWriter.Dispose() } catch {} }
    if ($null -ne $eventWriter) { try { $eventWriter.Dispose() } catch {} }
}
