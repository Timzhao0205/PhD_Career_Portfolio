#requires -Version 5.1
[CmdletBinding()]
param(
    [switch]$AllowCompatiblePS51
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot

$Root = $PSScriptRoot
$Failures = New-Object System.Collections.Generic.List[string]

function Add-Failure {
    param([string]$Message)
    [void]$script:Failures.Add($Message)
    Write-Host ("FAIL: {0}" -f $Message) -ForegroundColor Red
}

function Write-Pass {
    param([string]$Message)
    Write-Host ("PASS: {0}" -f $Message) -ForegroundColor Green
}

function Read-Json {
    param([string]$Path, [string]$Label)
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        Add-Failure "Missing ${Label}: $Path"
        return $null
    }
    try {
        return ([System.IO.File]::ReadAllText($Path) | ConvertFrom-Json)
    } catch {
        Add-Failure "Invalid JSON in ${Label}: $($_.Exception.Message)"
        return $null
    }
}

function Get-UniqueCount {
    param([string[]]$Values)
    $seen = @{}
    foreach ($value in @($Values)) {
        $key = ([string]$value).Trim().ToLowerInvariant()
        if (-not [string]::IsNullOrWhiteSpace($key)) {
            $seen[$key] = $true
        }
    }
    return $seen.Count
}

function Test-Runtime {
    $edition = [string]$PSVersionTable.PSEdition
    $version = [string]$PSVersionTable.PSVersion
    $build = [string]$PSVersionTable.BuildVersion
    $clr = [string]$PSVersionTable.CLRVersion
    Write-Host (
        'Runtime: PSEdition={0}; PSVersion={1}; BuildVersion={2}; CLR={3}' -f
        $edition,$version,$build,$clr
    )
    $compatible = (
        $edition -eq 'Desktop' -and
        $PSVersionTable.PSVersion.Major -eq 5 -and
        $PSVersionTable.PSVersion.Minor -eq 1
    )
    $exact = (
        $compatible -and
        $version -eq '5.1.26100.8875' -and
        $build -eq '10.0.26100.8875' -and
        $clr -eq '4.0.30319.42000'
    )
    if (-not $compatible) {
        Add-Failure (
            'Use Windows PowerShell 5.1 Desktop, not PowerShell 7.'
        )
    } elseif (-not $exact -and -not $AllowCompatiblePS51) {
        Add-Failure (
            'Runtime differs from the memorized target. Use ' +
            '-AllowCompatiblePS51 only after intentionally reviewing the ' +
            'Windows change.'
        )
    } elseif ($exact) {
        Write-Pass 'Exact memorized PowerShell 5.1 runtime.'
    } else {
        Write-Pass 'Compatible PowerShell 5.1 accepted by explicit override.'
    }
}

function Test-Scripts {
    $scripts = @(
        'START.ps1','CHECK.ps1','PILOT.ps1','VALIDATE.ps1',
        'CHECKPOINT.ps1','COMPLETE.ps1',
        '.claude\hooks\EVENT_LOG.ps1',
        '.claude\hooks\SESSION_START.ps1',
        '.claude\hooks\STATUS.ps1',
        '.claude\hooks\STOP_GUARD.ps1'
    )
    foreach ($relative in $scripts) {
        $path = Join-Path $Root $relative
        if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
            Add-Failure "Missing active PowerShell script: $relative"
            continue
        }
        $tokens = $null
        $errors = $null
        [void][System.Management.Automation.Language.Parser]::ParseFile(
            $path,[ref]$tokens,[ref]$errors
        )
        if (@($errors).Count -gt 0) {
            $messages = @($errors | ForEach-Object {
                $_.Message
            }) -join '; '
            Add-Failure "PowerShell parse error in ${relative}: $messages"
        }
    }
    if ($Failures.Count -eq 0) {
        Write-Pass 'Every active script parses in the installed PS5.1 host.'
    }
}

function Test-JsonConfiguration {
    foreach ($relative in @(
        'ROUTE.json','POWERSHELL_TARGET.json',
        '.claude\settings.json','SOURCE_SHA256.json','PACKAGE_SHA256.json'
    )) {
        [void](Read-Json (Join-Path $Root $relative) $relative)
    }
    $route = Read-Json (Join-Path $Root 'ROUTE.json') 'route'
    if ($null -ne $route) {
        if ([string]$route.execution_surface -ne
            'claude_code_interactive') {
            Add-Failure 'ROUTE.json is not interactive.'
        }
        $main = $route.main_session
        if ([string]$main.model -ne 'fable' -or
            [string]$main.effort -ne 'xhigh' -or
            [string]$main.permission_mode -ne 'bypassPermissions') {
            Add-Failure 'Main route must be fable/xhigh/bypassPermissions.'
        }
        if ($null -ne $main.monetary_stop -or
            $null -ne $main.turn_limit -or
            $null -ne $main.time_limit) {
            Add-Failure 'Route contains an active stop limit.'
        }
        $stages = @($route.stages)
        if ($stages.Count -ne 8) {
            Add-Failure 'Route must contain exactly eight stages.'
        }
        $names = @($stages | ForEach-Object { [string]$_.name })
        if ((Get-UniqueCount $names) -ne 8) {
            Add-Failure 'Route stage names are not unique.'
        }
        foreach ($stage in $stages) {
            if ([string]$stage.main_final_model -ne 'fable' -or
                [string]$stage.effort -ne 'xhigh' -or
                -not [bool]$stage.pilot_required) {
                Add-Failure "Invalid model/effort/pilot route: $($stage.name)"
            }
            $prompt = Join-Path $Root ([string]$stage.prompt)
            if (-not (Test-Path -LiteralPath $prompt -PathType Leaf)) {
                Add-Failure "Missing stage prompt: $($stage.prompt)"
            }
        }
    }
}

function Test-NoStopFlags {
    $active = @(
        'START.ps1',
        '.claude\settings.json',
        '.claude\hooks\STOP_GUARD.ps1',
        'ROUTE.json'
    )
    $forbidden = @(
        '--max-budget-usd','--max-turns','--no-session-persistence'
    )
    foreach ($relative in $active) {
        $text = [System.IO.File]::ReadAllText((Join-Path $Root $relative))
        foreach ($token in $forbidden) {
            if ($text.IndexOf($token,
                [System.StringComparison]::OrdinalIgnoreCase) -ge 0) {
                Add-Failure (
                    "Active launch file $relative contains stop flag $token."
                )
            }
        }
    }
    $startText = [System.IO.File]::ReadAllText(
        (Join-Path $Root 'START.ps1')
    )
    if ($startText -notmatch '--permission-mode' -or
        $startText -notmatch 'bypassPermissions' -or
        $startText -notmatch '--effort' -or
        $startText -notmatch 'xhigh' -or
        $startText -notmatch '--model' -or
        $startText -notmatch 'fable') {
        Add-Failure 'START.ps1 does not pin full-permission Fable/xhigh.'
    }
    if ($Failures.Count -eq 0) {
        Write-Pass 'Interactive route has no package-defined stop limit.'
    }
}

function Test-SourceManifest {
    $manifestPath = Join-Path $Root 'SOURCE_SHA256.json'
    $manifest = @(Read-Json $manifestPath 'source manifest')
    if ($manifest.Count -ne 419) {
        Add-Failure (
            "SOURCE_SHA256.json must contain 419 entries; observed " +
            "$($manifest.Count)."
        )
        return
    }
    foreach ($entry in $manifest) {
        $relative = [string]$entry.path
        if ([System.IO.Path]::IsPathRooted($relative) -or
            $relative -match '(^|[\\/])\.\.([\\/]|$)') {
            Add-Failure "Unsafe source-manifest path: $relative"
            continue
        }
        $path = Join-Path (Join-Path $Root 'src\06') $relative
        if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
            Add-Failure "Missing frozen source file: $relative"
            continue
        }
        $actual = (Get-FileHash -LiteralPath $path `
            -Algorithm SHA256).Hash.ToUpperInvariant()
        if ($actual -ne ([string]$entry.sha256).ToUpperInvariant()) {
            Add-Failure "Frozen source hash mismatch: $relative"
        }
    }
    if ($Failures.Count -eq 0) {
        Write-Pass 'All 419 frozen source files match their SHA-256 hashes.'
    }
}

function Test-PackageManifest {
    $manifestPath = Join-Path $Root 'PACKAGE_SHA256.json'
    $manifest = @(Read-Json $manifestPath 'package manifest')
    if ($manifest.Count -lt 20) {
        Add-Failure 'PACKAGE_SHA256.json is unexpectedly short.'
        return
    }
    foreach ($entry in $manifest) {
        $relative = [string]$entry.path
        if ([System.IO.Path]::IsPathRooted($relative) -or
            $relative -match '(^|[\\/])\.\.([\\/]|$)') {
            Add-Failure "Unsafe package-manifest path: $relative"
            continue
        }
        $path = Join-Path $Root $relative
        if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
            Add-Failure "Missing package file: $relative"
            continue
        }
        $actual = (Get-FileHash -LiteralPath $path `
            -Algorithm SHA256).Hash.ToUpperInvariant()
        if ($actual -ne ([string]$entry.sha256).ToUpperInvariant()) {
            Add-Failure "Package hash mismatch: $relative"
        }
    }
    if ($Failures.Count -eq 0) {
        Write-Pass 'Active package files match PACKAGE_SHA256.json.'
    }
}

function Test-FrozenCounts {
    $rawFiles = @(
        'P3R2_A_us_pain.json','P3R2_B_china_pain.json',
        'P3R2_C_dual_us_cn.json','P3R2_D_wildcards.json',
        'P3R2_E_jptwkr_side.json','P3R2_F_cn_topup.json',
        'P3R2_G_cn_microwave.json'
    )
    $rawIds = @()
    foreach ($name in $rawFiles) {
        $path = Join-Path $Root "src\06\20_OPPORTUNITY_POOL\$name"
        $items = @(Read-Json $path "raw pool $name")
        foreach ($item in $items) {
            $rawIds += [string]$item.idea_id
        }
    }
    if ($rawIds.Count -ne 126 -or
        (Get-UniqueCount $rawIds) -ne 126) {
        Add-Failure 'Frozen raw pool is not 126 rows / 126 unique IDs.'
    }

    $longlist = Read-Json (Join-Path $Root `
        'src\06\30_SCREENING\LONGLIST.json') 'longlist'
    if ($null -ne $longlist) {
        $longIds = @($longlist.ideas | ForEach-Object {
            [string]$_.idea_id
        })
        if ($longIds.Count -ne 65 -or
            (Get-UniqueCount $longIds) -ne 65) {
            Add-Failure 'Frozen longlist is not 65 unique IDs.'
        }
        foreach ($id in $longIds) {
            if ($rawIds -cnotcontains $id) {
                Add-Failure "Longlist ID is absent from raw pool: $id"
            }
        }
    }

    $ledger = @(Read-Json (Join-Path $Root `
        'src\06\90_BIBLIOGRAPHY\sources.json') 'source ledger')
    $ledgerIds = @($ledger | ForEach-Object { [string]$_.id })
    $accepted = @($ledger | Where-Object {
        $_.accepted -eq $true
    }).Count
    if ($ledger.Count -ne 1289 -or
        (Get-UniqueCount $ledgerIds) -ne 1289 -or
        $accepted -ne 1182) {
        Add-Failure (
            'Frozen ledger is not 1,289 unique / 1,182 accepted.'
        )
    }

    $selection = Read-Json (Join-Path $Root `
        'src\06\30_SCREENING\P5_SELECTION.json') 'historical selection'
    if ($null -ne $selection) {
        if (@($selection.final_24).Count -ne 24 -or
            @($selection.top_10_deep_dives).Count -ne 10) {
            Add-Failure 'Historical completed baseline is not 24/10.'
        }
    }
    $deep = @(Get-ChildItem -LiteralPath (Join-Path $Root `
        'src\06\40_DEEP_DIVES') -File | Where-Object {
            $_.Name -like 'DD_*.md'
        })
    if ($deep.Count -ne 10) {
        Add-Failure 'Historical baseline does not contain ten deep dives.'
    }
    if ($Failures.Count -eq 0) {
        Write-Pass (
            'Completed baseline validated: 126 raw, 65 longlist, 1,289 ' +
            'sources, historical 24/10.'
        )
    }
}

function Test-Paths {
    if ($Root.Length -gt 120) {
        Add-Failure (
            "Package root length is $($Root.Length); extract to C:\AI\F06I."
        )
    }
    $longest = 0
    foreach ($item in @(Get-ChildItem -LiteralPath $Root -Recurse -Force)) {
        if ($item.FullName.Length -gt $longest) {
            $longest = $item.FullName.Length
        }
        if ($item.Name.Length -gt 100) {
            Add-Failure "Filename component exceeds 100 chars: $($item.Name)"
        }
    }
    if ($longest -gt 220 -or ($Root.Length + 110) -gt 238) {
        Add-Failure (
            "Windows path headroom is insufficient; longest path=$longest."
        )
    } elseif ($Failures.Count -eq 0) {
        Write-Pass "Windows path policy; longest current path=$longest."
    }
}

function Test-Overrides {
    foreach ($name in @(
        'CLAUDE_CODE_EFFORT_LEVEL','CLAUDE_CODE_SUBAGENT_MODEL',
        'ANTHROPIC_MODEL','ANTHROPIC_DEFAULT_FABLE_MODEL'
    )) {
        $value = [Environment]::GetEnvironmentVariable($name)
        if (-not [string]::IsNullOrWhiteSpace($value)) {
            Add-Failure "$name can override the pinned route."
        }
    }
    if ($Failures.Count -eq 0) {
        Write-Pass 'No environment variable can silently override the route.'
    }
}

Write-Host ''
Write-Host '==== PowerShell target ====' -ForegroundColor Cyan
Test-Runtime

Write-Host ''
Write-Host '==== Active package ====' -ForegroundColor Cyan
Test-Scripts
Test-JsonConfiguration
Test-NoStopFlags
Test-Overrides

Write-Host ''
Write-Host '==== Immutable inputs ====' -ForegroundColor Cyan
Test-SourceManifest
Test-PackageManifest
Test-FrozenCounts
Test-Paths

Write-Host ''
if ($Failures.Count -gt 0) {
    Write-Host (
        "PACKAGE VALIDATION FAILED ({0} issue(s))." -f $Failures.Count
    ) -ForegroundColor Red
    exit 1
}
Write-Host (
    'PACKAGE VALIDATION PASSED: exact PS5.1 target, active scripts, ' +
    'interactive route, hashes, counts, no stop limit, and path rules.'
) -ForegroundColor Green
exit 0
