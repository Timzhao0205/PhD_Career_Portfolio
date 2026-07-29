#requires -Version 5.1
[CmdletBinding()]
param(
    [ValidateRange(30,600)]
    [int]$TimeoutSeconds = 180
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Continue'
Set-Location -LiteralPath $PSScriptRoot

$missionRoot = $PSScriptRoot
$childScript = Join-Path $missionRoot 'INVOKE_CLAUDE_CHILD.ps1'
$testRoot = Join-Path $missionRoot 'logs\claude_model_connection_test'
$receiptPath = Join-Path $missionRoot 'state\CLAUDE_MODEL_CONNECTION_TEST.json'
$modelLog = Join-Path $missionRoot 'state\MODEL_EFFORT_LOG.csv'
$operationLog = Join-Path $missionRoot 'state\OPERATION_LOG.csv'
$eventLog = Join-Path $missionRoot 'state\CLAUDE_EVENT_LOG.jsonl'

function Get-IsoTimestamp {
    return (Get-Date).ToString('o')
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

function Write-TestReceipt([object]$Value) {
    $temporary = "{0}.tmp.{1}" -f $receiptPath,$PID
    ($Value | ConvertTo-Json -Depth 12) |
        Set-Content -LiteralPath $temporary -Encoding UTF8
    Move-Item -LiteralPath $temporary -Destination $receiptPath -Force
}

function Stop-ProbeProcess {
    param([Parameter(Mandatory=$true)][System.Diagnostics.Process]$Process)
    if ($Process.HasExited) { return }
    if ($env:OS -eq 'Windows_NT' -and
        (Get-Command taskkill.exe -ErrorAction SilentlyContinue)) {
        & taskkill.exe /PID $Process.Id /T /F *> $null
    } else {
        try { $Process.Kill() } catch {}
    }
}

function Read-ProbeMetadata([string]$StreamFile) {
    $models = @()
    $initModel = ''
    $observed = ''
    if (Test-Path -LiteralPath $StreamFile -PathType Leaf) {
        foreach ($line in (Get-Content -LiteralPath $StreamFile -ErrorAction SilentlyContinue)) {
            if ([string]::IsNullOrWhiteSpace($line)) { continue }
            try { $event = $line | ConvertFrom-Json } catch { continue }
            if ($event.PSObject.Properties['model']) {
                $value = [string]$event.model
                if (-not [string]::IsNullOrWhiteSpace($value)) { $models += $value }
                if ($event.PSObject.Properties['type'] -and
                    [string]$event.type -eq 'system' -and
                    $event.PSObject.Properties['subtype'] -and
                    [string]$event.subtype -eq 'init') {
                    $initModel = $value
                }
            }
            if ($event.PSObject.Properties['message'] -and
                $null -ne $event.message -and
                $event.message.PSObject.Properties['model']) {
                $value = [string]$event.message.model
                if (-not [string]::IsNullOrWhiteSpace($value)) { $models += $value }
            }
            if ($event.PSObject.Properties['type'] -and
                [string]$event.type -eq 'result' -and
                $event.PSObject.Properties['result']) {
                $observed = [string]$event.result
            }
        }
    }
    return [pscustomobject]@{
        InitModel=$initModel
        Models=@($models | Select-Object -Unique)
        Observed=$observed.Trim()
    }
}

New-Item -ItemType Directory -Force -Path $testRoot | Out-Null
if (-not (Test-Path -LiteralPath $eventLog -PathType Leaf)) {
    New-Item -ItemType File -Path $eventLog | Out-Null
}
$probeDefinitions = @(
    [ordered]@{alias='sonnet';family='sonnet';expected='CLAUDE_SONNET_OK'},
    [ordered]@{alias='fable';family='fable';expected='CLAUDE_FABLE_OK'}
)
$results = @()
$failureMessages = @()

try {
    $versionOutput = & claude --version 2>&1
    $versionExitCode = $LASTEXITCODE
    $versionText = ($versionOutput | Out-String).Trim()
    if ($versionExitCode -ne 0) { throw 'Claude Code did not return a version.' }
    $authOutput = & claude auth status --text 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw 'Claude Code is not authenticated. Run claude auth login, then run RUN_EVERYTHING.ps1 again.'
    }

    foreach ($probe in $probeDefinitions) {
        $probeDirectory = Join-Path $testRoot ([string]$probe.alias)
        New-Item -ItemType Directory -Force -Path $probeDirectory | Out-Null
        $streamFile = Join-Path $probeDirectory 'stream.jsonl'
        $errorFile = Join-Path $probeDirectory 'stderr.txt'
        $promptFile = Join-Path $probeDirectory 'prompt.txt'
        $argumentsFile = Join-Path $probeDirectory 'claude_arguments.json'
        New-Item -ItemType File -Force -Path $streamFile,$errorFile | Out-Null

        @"
This is a minimal read-only connection and model-access probe.
Do not read files, use tools, browse, run commands, or write files.
Return exactly this token and nothing else:
$($probe.expected)
"@ | Set-Content -LiteralPath $promptFile -Encoding UTF8

        $claudeArguments = @(
            '-p',
            '--model',[string]$probe.alias,
            '--effort','low',
            '--max-turns','1',
            '--output-format','stream-json',
            '--verbose',
            '--permission-mode','plan',
            '--setting-sources','project',
            '--disallowedTools','mcp__*',
            '--no-chrome',
            '--no-session-persistence'
        )
        ConvertTo-Json -InputObject @($claudeArguments) -Depth 5 |
            Set-Content -LiteralPath $argumentsFile -Encoding UTF8

        $hostPath = (Get-Process -Id $PID).Path
        $childArguments = @(
            '-NoProfile','-NonInteractive','-ExecutionPolicy','Bypass',
            '-File',$childScript,
            '-PromptFile',$promptFile,
            '-ArgumentsFile',$argumentsFile,
            '-StreamFile',$streamFile,
            '-ErrorFile',$errorFile,
            '-EventLogFile',$eventLog,
            '-WorkingDirectory',$missionRoot,
            '-Stage',("connection_probe_{0}" -f $probe.alias),
            '-Attempt','1',
            '-RequestedModel',[string]$probe.alias,
            '-RequestedEffort','low'
        )
        $startInfo = New-Object System.Diagnostics.ProcessStartInfo
        $startInfo.FileName = $hostPath
        $startInfo.Arguments = (
            @($childArguments | ForEach-Object {
                Quote-ProcessArgument ([string]$_)
            }) -join ' '
        )
        $startInfo.WorkingDirectory = $missionRoot
        $startInfo.UseShellExecute = $false
        $startInfo.CreateNoWindow = $true
        $process = New-Object System.Diagnostics.Process
        $process.StartInfo = $startInfo
        $watch = [Diagnostics.Stopwatch]::StartNew()
        $exitCode = 1
        $timedOut = $false
        try {
            if (-not $process.Start()) {
                throw "Could not start the Claude $($probe.alias) probe."
            }
            while (-not $process.HasExited -and
                $watch.Elapsed.TotalSeconds -lt $TimeoutSeconds) {
                Start-Sleep -Milliseconds 500
                $process.Refresh()
            }
            if (-not $process.HasExited) {
                $timedOut = $true
                Stop-ProbeProcess -Process $process
            }
            try { $process.WaitForExit(5000) | Out-Null } catch {}
            if ($process.HasExited) { $exitCode = $process.ExitCode }
        } finally {
            $watch.Stop()
            if (-not $process.HasExited) { Stop-ProbeProcess -Process $process }
            try { $process.Dispose() } catch {}
        }

        $metadata = Read-ProbeMetadata -StreamFile $streamFile
        $reportedModels = @($metadata.Models)
        $versionPattern = "(?i){0}(?:-|_)?5(?:[-_.]|$)" -f (
            [regex]::Escape([string]$probe.family)
        )
        $versionVerified = $metadata.InitModel -match $versionPattern
        if (-not $versionVerified) {
            foreach ($reportedModel in $reportedModels) {
                if ([string]$reportedModel -match $versionPattern) {
                    $versionVerified = $true
                }
            }
        }
        $connected = (-not $timedOut) -and $exitCode -eq 0 -and
            $metadata.Observed -eq [string]$probe.expected -and
            $versionVerified
        $trackedFableDowngrade = (
            [string]$probe.family -eq 'fable' -and -not $versionVerified
        )
        $status = if ($connected) { 'PASS' } else { 'FAIL' }
        $result = [pscustomobject][ordered]@{
            alias=[string]$probe.alias
            expected_family=[string]$probe.family
            expected_major_version=5
            effort='low'
            status=$status
            exit_code=$exitCode
            timed_out=$timedOut
            init_model=$metadata.InitModel
            reported_models=$reportedModels
            expected_token=[string]$probe.expected
            observed_token=$metadata.Observed
            seconds=[math]::Round($watch.Elapsed.TotalSeconds,1)
            raw_stream=$streamFile
            stderr=$errorFile
        }
        $results += $result

        [pscustomobject]@{
            timestamp=Get-IsoTimestamp
            stage=("claude_{0}_connection_test" -f $probe.alias)
            route='claude_code_powershell'
            attempt=1
            requested_model=[string]$probe.alias
            requested_effort='low'
            reported_models=($reportedModels -join ';')
            status=if ($connected) { 'connected' } else { 'failed' }
            session_id=''
            seconds=$result.seconds
            validation=if ($connected) { [string]$probe.expected } else { 'probe_failed' }
            notes=("init_model={0};timed_out={1};policy_scope=fable_final_result_only" -f
                $metadata.InitModel,$timedOut)
        } | Export-Csv -LiteralPath $modelLog -NoTypeInformation -Append -Encoding UTF8

        [pscustomobject]@{
            timestamp=Get-IsoTimestamp
            stage=("connection_probe_{0}" -f $probe.alias)
            operation='connection_probe'
            progress=$status
            route='claude_code_powershell'
            attempt=1
            status=$status
            requested_model=[string]$probe.alias
            requested_effort='low'
            reported_models=($reportedModels -join ';')
            downgrade_flag=$trackedFableDowngrade
            downgrade_count=if ($trackedFableDowngrade) { 1 } else { 0 }
            usage_flag='NOT_CHECKED_BY_RUNNER'
            inactivity_flag='NOT_CHECKED_BY_RUNNER'
            session_id=''
            stream_file=$streamFile
            checkpoint=$receiptPath
            next_action=if ($connected) { 'Proceed' } else { 'Stage runner will verify again and never auto-route.' }
            notes=("observed={0};policy_scope=fable_final_result_only;temporary_and_auxiliary_models_allowed=true" -f
                $metadata.Observed)
        } | Export-Csv -LiteralPath $operationLog -NoTypeInformation -Append -Encoding UTF8

        if ($connected) {
            Write-Host (
                "PASS: Claude {0} is connected and reported a version-5 model ({1})." -f
                $probe.alias,$metadata.InitModel
            ) -ForegroundColor Green
        } else {
            $failureMessages += ("Claude {0} probe failed" -f $probe.alias)
            Write-Host ("FAIL: Claude {0} probe did not pass." -f $probe.alias) -ForegroundColor Red
        }
    }

    $overall = if (@($failureMessages).Count -eq 0) { 'PASS' } else { 'FAIL' }
    Write-TestReceipt -Value ([ordered]@{
        tested_at=(Get-IsoTimestamp)
        status=$overall
        claude_cli_version=$versionText
        authentication='connected'
        probes=@($results)
        errors=@($failureMessages)
    })
    if ($overall -eq 'PASS') { exit 0 }
    exit 1
} catch {
    $message = $_.Exception.Message
    Write-TestReceipt -Value ([ordered]@{
        tested_at=(Get-IsoTimestamp)
        status='FAIL'
        error=$message
        probes=@($results)
    })
    Write-Host ''
    Write-Host ("FAIL: {0}" -f $message) -ForegroundColor Red
    Write-Host 'The research runner will not invoke another provider.'
    exit 1
}
