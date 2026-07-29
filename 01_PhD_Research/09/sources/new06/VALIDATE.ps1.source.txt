#requires -Version 5.1
[CmdletBinding()]
param(
    [ValidateSet(
        '10_refresh','20_p4','30_redteam','40_select',
        '45_packs','50_deep','60_synth','70_audit'
    )]
    [string]$Stage,
    [switch]$Pilot,
    [switch]$All,
    [switch]$Quiet,
    [string]$BasePath
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot

$Root = $PSScriptRoot
$Failures = New-Object System.Collections.Generic.List[string]
$Stages = @(
    '10_refresh','20_p4','30_redteam','40_select',
    '45_packs','50_deep','60_synth','70_audit'
)

function Add-Failure {
    param([string]$Message)
    [void]$script:Failures.Add($Message)
    if (-not $Quiet) {
        Write-Host ("FAIL: {0}" -f $Message) -ForegroundColor Red
    }
}

function Write-Pass {
    param([string]$Message)
    if (-not $Quiet) {
        Write-Host ("PASS: {0}" -f $Message) -ForegroundColor Green
    }
}

function Read-JsonFile {
    param([string]$Path, [string]$Label)
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        Add-Failure "Missing ${Label}: $Path"
        return $null
    }
    try {
        $text = [System.IO.File]::ReadAllText($Path)
        if ([string]::IsNullOrWhiteSpace($text)) {
            Add-Failure "Empty ${Label}: $Path"
            return $null
        }
        return ($text | ConvertFrom-Json)
    } catch {
        Add-Failure "Invalid JSON in ${Label}: $Path - $($_.Exception.Message)"
        return $null
    }
}

function Get-Value {
    param($Object, [string]$Name, $Default)
    if ($null -eq $Object) {
        return $Default
    }
    $property = $Object.PSObject.Properties[$Name]
    if ($null -eq $property -or $null -eq $property.Value) {
        return $Default
    }
    return $property.Value
}

function Get-ArrayValue {
    param($Object, [string]$Name)
    $value = Get-Value -Object $Object -Name $Name -Default $null
    if ($null -eq $value) {
        return @()
    }
    return @($value)
}

function Require-File {
    param([string]$Directory, [string]$Name, [string]$Label)
    $path = Join-Path $Directory $Name
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        Add-Failure "Missing ${Label}: $path"
        return $null
    }
    $item = Get-Item -LiteralPath $path
    if ($item.Length -eq 0) {
        Add-Failure "Empty ${Label}: $path"
        return $null
    }
    return $path
}

function Test-RequiredProperties {
    param($Object, [string[]]$Names, [string]$Context)
    if ($null -eq $Object) {
        Add-Failure "$Context is null."
        return
    }
    foreach ($name in $Names) {
        if ($null -eq $Object.PSObject.Properties[$name]) {
            Add-Failure "$Context is missing property '$name'."
        }
    }
}

function Get-Ids {
    param([object[]]$Items, [string]$Property)
    $ids = @()
    foreach ($item in @($Items)) {
        $ids += [string](Get-Value -Object $item -Name $Property -Default '')
    }
    return @($ids)
}

function Test-UniqueIds {
    param(
        [string[]]$Ids,
        [int]$Expected,
        [string]$Context
    )
    if (@($Ids).Count -ne $Expected) {
        Add-Failure (
            "$Context must contain $Expected IDs; observed $(@($Ids).Count)."
        )
    }
    $seen = @{}
    foreach ($raw in @($Ids)) {
        $id = [string]$raw
        if ([string]::IsNullOrWhiteSpace($id)) {
            Add-Failure "$Context contains an empty ID."
            continue
        }
        $key = $id.Trim().ToLowerInvariant()
        if ($seen.ContainsKey($key)) {
            Add-Failure "$Context contains duplicate ID '$id'."
        } else {
            $seen[$key] = $true
        }
    }
}

function Test-ExactIdSet {
    param(
        [string[]]$Observed,
        [string[]]$Expected,
        [string]$Context
    )
    $left = @($Observed | ForEach-Object {
        ([string]$_).Trim().ToLowerInvariant()
    } | Sort-Object -Unique)
    $right = @($Expected | ForEach-Object {
        ([string]$_).Trim().ToLowerInvariant()
    } | Sort-Object -Unique)
    if (($left -join '|') -ne ($right -join '|')) {
        Add-Failure "$Context does not match the required ID set."
    }
}

function Test-ExactIdOrder {
    param(
        [string[]]$Observed,
        [string[]]$Expected,
        [string]$Context
    )
    $left = @($Observed | ForEach-Object {
        ([string]$_).Trim().ToLowerInvariant()
    })
    $right = @($Expected | ForEach-Object {
        ([string]$_).Trim().ToLowerInvariant()
    })
    if (($left -join '|') -ne ($right -join '|')) {
        Add-Failure "$Context does not preserve the required order."
    }
}

function Test-Subset {
    param(
        [string[]]$Subset,
        [string[]]$Superset,
        [string]$Context
    )
    $allowed = @{}
    foreach ($id in @($Superset)) {
        $allowed[([string]$id).Trim().ToLowerInvariant()] = $true
    }
    foreach ($id in @($Subset)) {
        $key = ([string]$id).Trim().ToLowerInvariant()
        if (-not $allowed.ContainsKey($key)) {
            Add-Failure "$Context contains non-member ID '$id'."
        }
    }
}

function Test-BooleanProperty {
    param($Object, [string]$Name, [string]$Context)
    $property = $Object.PSObject.Properties[$Name]
    if ($null -eq $property -or
        -not ($property.Value -is [System.Boolean])) {
        Add-Failure "$Context property '$name' must be a JSON Boolean."
    }
}

function Test-ResultFile {
    param([string]$Directory, [string]$ExpectedStage)
    $path = Require-File -Directory $Directory -Name 'RESULT.json' `
        -Label "$ExpectedStage result"
    if ($null -eq $path) {
        return
    }
    $result = Read-JsonFile -Path $path -Label "$ExpectedStage result"
    if ($null -eq $result) {
        return
    }
    if ([string](Get-Value $result 'stage' '') -ne $ExpectedStage) {
        Add-Failure "$ExpectedStage RESULT.json has the wrong stage."
    }
    if ([string](Get-Value $result 'status' '') -ne 'COMPLETE') {
        Add-Failure "$ExpectedStage RESULT.json status is not COMPLETE."
    }
}

function Get-FrozenLonglistIds {
    $path = Join-Path $Root 'src\06\30_SCREENING\LONGLIST.json'
    $data = Read-JsonFile -Path $path -Label 'frozen longlist'
    if ($null -eq $data) {
        return @()
    }
    return @(Get-Ids -Items @(Get-ArrayValue $data 'ideas') `
        -Property 'idea_id')
}

function Get-StageDirectory {
    param([string]$StageName, [switch]$IsPilot)
    $base = $Root
    if (-not [string]::IsNullOrWhiteSpace($BasePath)) {
        $base = [System.IO.Path]::GetFullPath($BasePath)
    }
    if ($IsPilot) {
        return (Join-Path (Join-Path $base 'pilot') $StageName)
    }
    return (Join-Path (Join-Path $base 'outputs') $StageName)
}

function Read-StageJson {
    param([string]$StageName, [string]$FileName)
    $directory = Get-StageDirectory -StageName $StageName
    return Read-JsonFile -Path (Join-Path $directory $FileName) `
        -Label "$StageName $FileName"
}

function Test-PilotStage {
    param([string]$StageName)
    $directory = Get-StageDirectory -StageName $StageName -IsPilot
    $jsonPath = Require-File -Directory $directory -Name 'PILOT.json' `
        -Label "$StageName pilot JSON"
    [void](Require-File -Directory $directory -Name 'PILOT.md' `
        -Label "$StageName pilot report")
    if ($null -eq $jsonPath) {
        return
    }
    $data = Read-JsonFile -Path $jsonPath -Label "$StageName pilot"
    if ($null -eq $data) {
        return
    }
    Test-RequiredProperties -Object $data -Names @(
        'stage','status','sample_ids','paths_tested',
        'checks','errors','lessons'
    ) -Context "$StageName pilot"
    if ([string](Get-Value $data 'stage' '') -ne $StageName) {
        Add-Failure "$StageName pilot stage field is incorrect."
    }
    if ([string](Get-Value $data 'status' '') -ne 'PASS') {
        Add-Failure "$StageName pilot status is not PASS."
    }
    if (@(Get-ArrayValue $data 'sample_ids').Count -lt 1) {
        Add-Failure "$StageName pilot has no sample IDs."
    }
    if (@(Get-ArrayValue $data 'paths_tested').Count -lt 1) {
        Add-Failure "$StageName pilot has no tested paths."
    }
    if (@(Get-ArrayValue $data 'errors').Count -ne 0) {
        Add-Failure "$StageName pilot reports errors."
    }
    $checks = Get-Value $data 'checks' $null
    if ($null -eq $checks -or
        @($checks.PSObject.Properties).Count -lt 1) {
        Add-Failure "$StageName pilot has no recorded checks."
    }
}

function Test-10Refresh {
    $directory = Get-StageDirectory -StageName '10_refresh'
    $refreshPath = Require-File $directory 'REFRESH.json' 'refresh data'
    $sourcesPath = Require-File $directory 'SOURCES.json' 'refresh sources'
    [void](Require-File $directory 'REFRESH.md' 'refresh report')
    if ($null -ne $refreshPath) {
        $data = Read-JsonFile $refreshPath 'refresh data'
        if ($null -ne $data) {
            $items = @(Get-ArrayValue $data 'items')
            $ids = @(Get-Ids $items 'idea_id')
            Test-UniqueIds $ids 65 '10_refresh items'
            Test-ExactIdSet $ids (Get-FrozenLonglistIds) `
                '10_refresh longlist coverage'
            $allowed = @(
                'updated','no_material_change','insufficient'
            )
            foreach ($item in $items) {
                Test-RequiredProperties $item @(
                    'idea_id','refresh_status','checked_claims',
                    'new_source_ids','stale_claims','confidence'
                ) "10_refresh item"
                $status = [string](Get-Value $item 'refresh_status' '')
                if ($allowed -notcontains $status) {
                    Add-Failure (
                        "10_refresh invalid refresh_status '$status'."
                    )
                }
                if (@(Get-ArrayValue $item 'checked_claims').Count -lt 1) {
                    Add-Failure (
                        "10_refresh item $([string](Get-Value $item 'idea_id' '')) " +
                        'has no checked claim.'
                    )
                }
            }
        }
    }
    if ($null -ne $sourcesPath) {
        $sources = @(Read-JsonFile $sourcesPath 'refresh sources')
        $ids = @(Get-Ids $sources 'id')
        Test-UniqueIds $ids $sources.Count '10_refresh sources'
    }
    Test-ResultFile $directory '10_refresh'
}

function Test-20P4 {
    $directory = Get-StageDirectory -StageName '20_p4'
    $scoresPath = Require-File $directory 'SCORES.json' 'P4 scores'
    $survivorsPath = Require-File $directory 'SURVIVORS.json' 'P4 survivors'
    [void](Require-File $directory 'P4_REPORT.md' 'P4 report')
    $criterionNames = @(
        'demonstrated_demand','frontier_vision','high_end_niche',
        'competition_whitespace','reachable_validation_budget',
        'technical_elegance','ten_x_edge','us_china_leverage',
        'launch_2030_fit','expansion_economics','founder_skill_transfer'
    )
    if ($null -ne $scoresPath) {
        $data = Read-JsonFile $scoresPath 'P4 scores'
        if ($null -ne $data) {
            $ideas = @(Get-ArrayValue $data 'ideas')
            $ids = @(Get-Ids $ideas 'idea_id')
            Test-UniqueIds $ids 65 '20_p4 scores'
            Test-ExactIdSet $ids (Get-FrozenLonglistIds) `
                '20_p4 longlist coverage'
            foreach ($idea in $ideas) {
                Test-RequiredProperties $idea @(
                    'idea_id','hard_gates','criteria','total_100',
                    'confidence','fatal_uncertainties','disposition'
                ) '20_p4 score'
                $gates = Get-Value $idea 'hard_gates' $null
                foreach ($gateName in @('G1','G2','G3','G4','G5','G6','G7')) {
                    $gate = Get-Value $gates $gateName $null
                    Test-RequiredProperties $gate @(
                        'pass','rationale','source_ids'
                    ) "20_p4 $gateName"
                    if ($null -ne $gate) {
                        Test-BooleanProperty $gate 'pass' "20_p4 $gateName"
                    }
                }
                $criteria = Get-Value $idea 'criteria' $null
                $sum = 0.0
                foreach ($name in $criterionNames) {
                    $criterion = Get-Value $criteria $name $null
                    Test-RequiredProperties $criterion @(
                        'score_0_5','weighted_points','rationale','source_ids'
                    ) "20_p4 criterion $name"
                    if ($null -ne $criterion) {
                        $score = [double](Get-Value $criterion `
                            'score_0_5' -1)
                        if ($score -lt 0 -or $score -gt 5) {
                            Add-Failure (
                                "20_p4 criterion $name score is outside 0-5."
                            )
                        }
                        $sum += [double](Get-Value $criterion `
                            'weighted_points' 0)
                    }
                }
                $total = [double](Get-Value $idea 'total_100' -1)
                if ([Math]::Abs($sum - $total) -gt 0.25) {
                    Add-Failure (
                        "20_p4 weighted points do not equal total for " +
                        [string](Get-Value $idea 'idea_id' '') + '.'
                    )
                }
            }
        }
    }
    if ($null -ne $survivorsPath) {
        $data = Read-JsonFile $survivorsPath 'P4 survivors'
        if ($null -ne $data) {
            $ideas = @(Get-ArrayValue $data 'ideas')
            $ids = @(Get-Ids $ideas 'idea_id')
            Test-UniqueIds $ids 30 '20_p4 survivors'
            Test-Subset $ids (Get-FrozenLonglistIds) `
                '20_p4 survivors'
            foreach ($idea in $ideas) {
                Test-RequiredProperties $idea @(
                    'idea_id','p4_rank','total_100','gate_status','p5_focus'
                ) '20_p4 survivor'
            }
        }
    }
    Test-ResultFile $directory '20_p4'
}

function Test-30Redteam {
    $directory = Get-StageDirectory -StageName '30_redteam'
    $path = Require-File $directory 'REDTEAM.json' 'red-team data'
    [void](Require-File $directory 'REDTEAM.md' 'red-team report')
    if ($null -ne $path) {
        $data = Read-JsonFile $path 'red-team data'
        if ($null -ne $data) {
            $ideas = @(Get-ArrayValue $data 'ideas')
            $ids = @(Get-Ids $ideas 'idea_id')
            Test-UniqueIds $ids 30 '30_redteam ideas'
            $survivorData = Read-StageJson '20_p4' 'SURVIVORS.json'
            if ($null -ne $survivorData) {
                $expected = Get-Ids @(Get-ArrayValue $survivorData 'ideas') `
                    'idea_id'
                Test-ExactIdSet $ids $expected '30_redteam survivor coverage'
            }
            foreach ($idea in $ideas) {
                Test-RequiredProperties $idea @(
                    'idea_id','decision','failure_modes',
                    'strongest_counterargument','demand_separability',
                    'competition_test','technical_kill_test',
                    'commercial_kill_test','geography_findings',
                    'source_defects','repair_requirements','residual_risk',
                    'confidence','source_ids'
                ) '30_redteam review'
                $decision = [string](Get-Value $idea 'decision' '')
                if (@('survive','repair','reject') -notcontains $decision) {
                    Add-Failure "30_redteam invalid decision '$decision'."
                }
            }
        }
    }
    Test-ResultFile $directory '30_redteam'
}

function Test-CheckObject {
    param($Checks, [string]$Context, [int]$Minimum)
    if ($null -eq $Checks) {
        Add-Failure "$Context is missing."
        return
    }
    $properties = @($Checks.PSObject.Properties)
    if ($properties.Count -lt $Minimum) {
        Add-Failure (
            "$Context must contain at least $Minimum checks; observed " +
            "$($properties.Count)."
        )
    }
    foreach ($property in $properties) {
        $value = $property.Value
        if ($value -is [System.Boolean]) {
            if (-not [bool]$value) {
                Add-Failure "$Context check '$($property.Name)' failed."
            }
        } else {
            $pass = Get-Value $value 'pass' $null
            if (-not ($pass -is [System.Boolean]) -or -not [bool]$pass) {
                Add-Failure (
                    "$Context check '$($property.Name)' lacks pass:true."
                )
            }
        }
    }
}

function Test-40Select {
    $directory = Get-StageDirectory -StageName '40_select'
    $path = Require-File $directory 'SELECTION.json' 'selection data'
    $checksPath = Require-File $directory 'PORTFOLIO_CHECKS.json' `
        'portfolio checks'
    [void](Require-File $directory 'SELECTION.md' 'selection report')
    if ($null -ne $path) {
        $data = Read-JsonFile $path 'selection data'
        if ($null -ne $data) {
            $items = @(Get-ArrayValue $data 'final_24')
            $ids = @(Get-Ids $items 'idea_id')
            $top = @(Get-ArrayValue $data 'top_10_deep_dives' |
                ForEach-Object { [string]$_ })
            Test-UniqueIds $ids 24 '40_select final 24'
            Test-UniqueIds $top 10 '40_select top 10'
            Test-Subset $top $ids '40_select top 10'
            $survivorData = Read-StageJson '20_p4' 'SURVIVORS.json'
            if ($null -ne $survivorData) {
                Test-Subset $ids (Get-Ids @(
                    Get-ArrayValue $survivorData 'ideas'
                ) 'idea_id') '40_select final 24'
            }
            $ranks = @()
            $allowedMarkets = @(
                'US','China','Japan','Taiwan','South Korea'
            )
            foreach ($item in $items) {
                Test-RequiredProperties $item @(
                    'idea_id','rank','concept','primary_lane','is_hts',
                    'product_role_class','customer_class',
                    'first_experiment_budget_usd','us_beachhead',
                    'china_beachhead','dual_market','side_market_primary',
                    'markets','g7_pass','experiment_by_2028',
                    'engagement_by_2029','score_total','why_now',
                    'key_kill','source_ids'
                ) '40_select item'
                foreach ($name in @(
                    'is_hts','us_beachhead','china_beachhead','dual_market',
                    'side_market_primary','g7_pass','experiment_by_2028',
                    'engagement_by_2029'
                )) {
                    Test-BooleanProperty $item $name '40_select item'
                }
                $ranks += [int](Get-Value $item 'rank' 0)
                $us = [bool](Get-Value $item 'us_beachhead' $false)
                $cn = [bool](Get-Value $item 'china_beachhead' $false)
                $dual = [bool](Get-Value $item 'dual_market' $false)
                if ($dual -ne ($us -and $cn)) {
                    Add-Failure (
                        "40_select dual_market mismatch for " +
                        [string](Get-Value $item 'idea_id' '') + '.'
                    )
                }
                foreach ($market in @(Get-ArrayValue $item 'markets')) {
                    if ($allowedMarkets -notcontains [string]$market) {
                        Add-Failure "40_select disallowed market '$market'."
                    }
                }
            }
            if ((@($ranks | Sort-Object) -join ',') -ne
                ((1..24) -join ',')) {
                Add-Failure '40_select ranks must be exactly 1 through 24.'
            }
        }
    }
    if ($null -ne $checksPath) {
        $data = Read-JsonFile $checksPath 'portfolio checks'
        if ($null -ne $data) {
            $checks = Get-Value $data 'checks' $data
            Test-CheckObject $checks '40_select portfolio checks' 1
        }
    }
    Test-ResultFile $directory '40_select'
}

function Test-45Packs {
    $directory = Get-StageDirectory -StageName '45_packs'
    $sourcesPath = Require-File $directory 'SOURCES.json' 'pack sources'
    $packsPath = Require-File $directory 'PACKS.json' 'source packs'
    [void](Require-File $directory 'PACKS.md' 'source-pack report')
    $sourceIds = @()
    if ($null -ne $sourcesPath) {
        $sources = @(Read-JsonFile $sourcesPath 'pack sources')
        $sourceIds = @(Get-Ids $sources 'id')
        Test-UniqueIds $sourceIds $sources.Count '45_packs source ledger'
        foreach ($source in $sources) {
            Test-RequiredProperties $source @(
                'id','title','url','publisher','published_at','accessed_at',
                'source_type','peer_reviewed','primary_demand','geography',
                'claim_supported','locator','access_level','accepted',
                'india_origin_status','non_indian_affiliation_evidence'
            ) '45_packs source'
            foreach ($name in @('peer_reviewed','primary_demand','accepted')) {
                Test-BooleanProperty $source $name '45_packs source'
            }
            if (-not [bool](Get-Value $source 'accepted' $false)) {
                Add-Failure (
                    "45_packs contains non-accepted source " +
                    [string](Get-Value $source 'id' '') + '.'
                )
            }
            $origin = [string](Get-Value $source `
                'india_origin_status' '')
            if ([string]::IsNullOrWhiteSpace($origin) -or
                $origin -match '(?i)unknown|unverified' -or
                $origin -match '^(?i:india_origin|verified_india_origin)$') {
                Add-Failure (
                    "45_packs has ineligible/unknown origin '$origin'."
                )
            }
        }
    }
    if ($null -ne $packsPath) {
        $data = Read-JsonFile $packsPath 'source packs'
        if ($null -ne $data) {
            $ideas = @(Get-ArrayValue $data 'ideas')
            $ids = @(Get-Ids $ideas 'idea_id')
            Test-UniqueIds $ids 10 '45_packs ideas'
            $selection = Read-StageJson '40_select' 'SELECTION.json'
            if ($null -ne $selection) {
                $top = @(Get-ArrayValue $selection 'top_10_deep_dives' |
                    ForEach-Object { [string]$_ })
                Test-ExactIdSet $ids $top '45_packs top-10 coverage'
            }
            foreach ($idea in $ideas) {
                Test-RequiredProperties $idea @(
                    'idea_id','source_ids','peer_reviewed_source_ids',
                    'primary_demand_source_ids','claim_source_map',
                    'coverage_gaps','quality_notes'
                ) '45_packs idea'
                $all = @(Get-ArrayValue $idea 'source_ids' |
                    ForEach-Object { [string]$_ })
                $peer = @(Get-ArrayValue $idea 'peer_reviewed_source_ids' |
                    ForEach-Object { [string]$_ })
                $demand = @(Get-ArrayValue $idea 'primary_demand_source_ids' |
                    ForEach-Object { [string]$_ })
                if (@($all | Sort-Object -Unique).Count -lt 20) {
                    Add-Failure (
                        "45_packs idea $([string](Get-Value $idea 'idea_id' '')) " +
                        'has fewer than 20 sources.'
                    )
                }
                if (@($peer | Sort-Object -Unique).Count -lt 7) {
                    Add-Failure '45_packs idea has fewer than 7 peer sources.'
                }
                if (@($demand | Sort-Object -Unique).Count -lt 5) {
                    Add-Failure (
                        '45_packs idea has fewer than 5 primary-demand sources.'
                    )
                }
                Test-Subset $all $sourceIds '45_packs source references'
                Test-Subset $peer $all '45_packs peer references'
                Test-Subset $demand $all '45_packs demand references'
            }
        }
    }
    Test-ResultFile $directory '45_packs'
}

function Get-WordCount {
    param([string]$Path)
    $text = [System.IO.File]::ReadAllText($Path)
    return [regex]::Matches(
        $text,
        "[\p{L}\p{N}][\p{L}\p{N}'/-]*"
    ).Count
}

function Test-SafeBaseName {
    param([string]$Name, [string]$Context)
    if ([string]::IsNullOrWhiteSpace($Name) -or
        [System.IO.Path]::IsPathRooted($Name) -or
        [System.IO.Path]::GetFileName($Name) -ne $Name -or
        $Name.Length -gt 80 -or
        $Name.IndexOfAny([System.IO.Path]::GetInvalidFileNameChars()) -ge 0) {
        Add-Failure "$Context is not a short Windows-safe base filename: $Name"
        return $false
    }
    return $true
}

function Test-50Deep {
    $directory = Get-StageDirectory -StageName '50_deep'
    $deepDir = Join-Path $directory 'DEEP'
    if (-not (Test-Path -LiteralPath $deepDir -PathType Container)) {
        Add-Failure "Missing deep-dive directory: $deepDir"
    }
    $indexPath = Require-File $directory 'INDEX.json' 'deep-dive index'
    [void](Require-File $directory 'GEOGRAPHY.md' 'geography report')
    $addPath = Require-File $directory 'ADD_SOURCES.json' 'added sources'
    $allowedSourceIds = @()
    $packSources = Read-StageJson '45_packs' 'SOURCES.json'
    if ($null -ne $packSources) {
        $allowedSourceIds += @(Get-Ids @($packSources) 'id')
    }
    if ($null -ne $addPath) {
        $added = @(Read-JsonFile $addPath 'added sources')
        $addedIds = @(Get-Ids $added 'id')
        Test-UniqueIds $addedIds $added.Count '50_deep added sources'
        $allowedSourceIds += $addedIds
    }
    $files = @()
    if (Test-Path -LiteralPath $deepDir -PathType Container) {
        $files = @(Get-ChildItem -LiteralPath $deepDir -File |
            Where-Object { $_.Extension -eq '.md' })
        if ($files.Count -ne 10) {
            Add-Failure (
                "50_deep must contain 10 Markdown reports; observed " +
                "$($files.Count)."
            )
        }
    }
    if ($null -ne $indexPath) {
        $data = Read-JsonFile $indexPath 'deep-dive index'
        if ($null -ne $data) {
            $ideas = @(Get-ArrayValue $data 'ideas')
            $ids = @(Get-Ids $ideas 'idea_id')
            Test-UniqueIds $ids 10 '50_deep index'
            $selection = Read-StageJson '40_select' 'SELECTION.json'
            if ($null -ne $selection) {
                $top = @(Get-ArrayValue $selection 'top_10_deep_dives' |
                    ForEach-Object { [string]$_ })
                Test-ExactIdSet $ids $top '50_deep top-10 coverage'
            }
            foreach ($idea in $ideas) {
                Test-RequiredProperties $idea @(
                    'idea_id','file','word_count','source_ids',
                    'peer_reviewed_source_ids','primary_demand_source_ids'
                ) '50_deep index item'
                $file = [string](Get-Value $idea 'file' '')
                if (Test-SafeBaseName $file '50_deep filename') {
                    $path = Join-Path $deepDir $file
                    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
                        Add-Failure "50_deep indexed file is missing: $path"
                    } else {
                        $actual = Get-WordCount $path
                        $recorded = [int](Get-Value $idea 'word_count' 0)
                        if ($actual -lt 2500 -or $actual -gt 4000) {
                            Add-Failure (
                                "50_deep $file word count $actual is outside " +
                                '2500-4000.'
                            )
                        }
                        if ([Math]::Abs($actual - $recorded) -gt 5) {
                            Add-Failure (
                                "50_deep $file recorded word_count differs " +
                                "from observed $actual."
                            )
                        }
                    }
                }
                $allIds = @(Get-ArrayValue $idea 'source_ids' |
                    ForEach-Object { [string]$_ })
                $peerIds = @(Get-ArrayValue $idea `
                    'peer_reviewed_source_ids' |
                    ForEach-Object { [string]$_ })
                $demandIds = @(Get-ArrayValue $idea `
                    'primary_demand_source_ids' |
                    ForEach-Object { [string]$_ })
                if (@($allIds | Sort-Object -Unique).Count -lt 20) {
                    Add-Failure '50_deep report has fewer than 20 sources.'
                }
                if (@($peerIds | Sort-Object -Unique).Count -lt 7) {
                    Add-Failure '50_deep report has fewer than 7 peer sources.'
                }
                if (@($demandIds | Sort-Object -Unique).Count -lt 5) {
                    Add-Failure (
                        '50_deep report has fewer than 5 demand sources.'
                    )
                }
                Test-Subset $allIds $allowedSourceIds `
                    '50_deep source references'
                Test-Subset $peerIds $allIds `
                    '50_deep peer references'
                Test-Subset $demandIds $allIds `
                    '50_deep demand references'
            }
        }
    }
    Test-ResultFile $directory '50_deep'
}

function Get-SelectionIds {
    $selection = Read-StageJson '40_select' 'SELECTION.json'
    if ($null -eq $selection) {
        return [ordered]@{ final = @(); top = @() }
    }
    return [ordered]@{
        final = @(Get-Ids @(Get-ArrayValue $selection 'final_24') 'idea_id')
        top = @(Get-ArrayValue $selection 'top_10_deep_dives' |
            ForEach-Object { [string]$_ })
    }
}

function Test-60Synth {
    $directory = Get-StageDirectory -StageName '60_synth'
    $portfolioPath = Require-File $directory 'PORTFOLIO.json' `
        'synthesis portfolio'
    foreach ($name in @(
        '00_EXECUTIVE.md','01_IDEA_CARDS.md','02_MATRIX.csv',
        '02_MATRIX.md','03_MAP.md','04_ROADMAP.md','05_MODEL_REPORT.md'
    )) {
        [void](Require-File $directory $name "synthesis $name")
    }
    if ($null -ne $portfolioPath) {
        $data = Read-JsonFile $portfolioPath 'synthesis portfolio'
        if ($null -ne $data) {
            $items = @(Get-ArrayValue $data 'items')
            $ids = @(Get-Ids $items 'idea_id')
            $top = @(Get-ArrayValue $data 'top_10_deep_dives' |
                ForEach-Object { [string]$_ })
            Test-UniqueIds $ids 24 '60_synth portfolio'
            Test-UniqueIds $top 10 '60_synth top 10'
            $expected = Get-SelectionIds
            Test-ExactIdSet $ids $expected.final `
                '60_synth final-24 consistency'
            Test-ExactIdSet $top $expected.top `
                '60_synth top-10 consistency'
            Test-ExactIdOrder $ids $expected.final `
                '60_synth final-24 order'
            Test-ExactIdOrder $top $expected.top `
                '60_synth top-10 order'
        }
    }
    $csvPath = Join-Path $directory '02_MATRIX.csv'
    if (Test-Path -LiteralPath $csvPath -PathType Leaf) {
        try {
            $rows = @(Import-Csv -LiteralPath $csvPath)
            if ($rows.Count -ne 24) {
                Add-Failure (
                    "60_synth CSV must contain 24 data rows; observed " +
                    "$($rows.Count)."
                )
            }
        } catch {
            Add-Failure "60_synth CSV is invalid: $($_.Exception.Message)"
        }
    }
    Test-ResultFile $directory '60_synth'
}

function Test-70Audit {
    $directory = Get-StageDirectory -StageName '70_audit'
    $auditPath = Require-File $directory 'AUDIT.json' 'audit data'
    [void](Require-File $directory 'AUDIT.md' 'audit report')
    [void](Require-File $directory 'CHANGELOG.md' 'audit changelog')
    $finalDir = Join-Path $directory 'FINAL'
    foreach ($name in @(
        'GEOGRAPHY.md','SELECTION.json','SOURCES.json'
    )) {
        [void](Require-File $finalDir $name "final $name")
    }
    $portfolioDir = Join-Path $finalDir 'PORTFOLIO'
    foreach ($name in @(
        'PORTFOLIO.json','00_EXECUTIVE.md','01_IDEA_CARDS.md',
        '02_MATRIX.csv','02_MATRIX.md','03_MAP.md','04_ROADMAP.md',
        '05_MODEL_REPORT.md'
    )) {
        [void](Require-File $portfolioDir $name "final portfolio $name")
    }
    $deepDir = Join-Path $finalDir 'DEEP'
    if (-not (Test-Path -LiteralPath $deepDir -PathType Container)) {
        Add-Failure "Missing final deep-dive directory: $deepDir"
    } else {
        $deepFiles = @(Get-ChildItem -LiteralPath $deepDir -File |
            Where-Object { $_.Extension -eq '.md' })
        if ($deepFiles.Count -ne 10) {
            Add-Failure (
                "70_audit FINAL/DEEP must contain 10 reports; observed " +
                "$($deepFiles.Count)."
            )
        }
        foreach ($deepFile in $deepFiles) {
            $count = Get-WordCount $deepFile.FullName
            if ($count -lt 2500 -or $count -gt 4000) {
                Add-Failure (
                    "70_audit final deep dive $($deepFile.Name) has " +
                    "$count words, outside 2500-4000."
                )
            }
        }
    }
    if ($null -ne $auditPath) {
        $audit = Read-JsonFile $auditPath 'audit data'
        if ($null -ne $audit) {
            Test-RequiredProperties $audit @(
                'verdict','checks','repairs','unresolved_critical',
                'unresolved_major','unresolved_minor','final_24_count',
                'deep_dive_count','source_count'
            ) '70_audit audit'
            if ([string](Get-Value $audit 'verdict' '') -ne 'PASS') {
                Add-Failure '70_audit verdict is not PASS.'
            }
            if (@(Get-ArrayValue $audit 'unresolved_critical').Count -ne 0) {
                Add-Failure '70_audit has unresolved critical issues.'
            }
            if (@(Get-ArrayValue $audit 'unresolved_major').Count -ne 0) {
                Add-Failure '70_audit has unresolved major issues.'
            }
            if ([int](Get-Value $audit 'final_24_count' 0) -ne 24) {
                Add-Failure '70_audit final_24_count is not 24.'
            }
            if ([int](Get-Value $audit 'deep_dive_count' 0) -ne 10) {
                Add-Failure '70_audit deep_dive_count is not 10.'
            }
            Test-CheckObject (Get-Value $audit 'checks' $null) `
                '70_audit checks' 10
        }
    }
    $selectionPath = Join-Path $finalDir 'SELECTION.json'
    $finalSelectionIds = @()
    $finalTopIds = @()
    if (Test-Path -LiteralPath $selectionPath -PathType Leaf) {
        $selection = Read-JsonFile $selectionPath 'final selection'
        if ($null -ne $selection) {
            $final = @(Get-ArrayValue $selection 'final_24')
            $top = @(Get-ArrayValue $selection 'top_10_deep_dives')
            $finalSelectionIds = @(Get-Ids $final 'idea_id')
            $finalTopIds = @($top | ForEach-Object { [string]$_ })
            Test-UniqueIds $finalSelectionIds 24 `
                '70_audit final selection'
            Test-UniqueIds $finalTopIds 10 `
                '70_audit final top 10'
        }
    }
    $finalPortfolioPath = Join-Path $portfolioDir 'PORTFOLIO.json'
    if (Test-Path -LiteralPath $finalPortfolioPath -PathType Leaf) {
        $portfolio = Read-JsonFile $finalPortfolioPath 'final portfolio'
        if ($null -ne $portfolio) {
            $portfolioIds = @(Get-Ids @(
                Get-ArrayValue $portfolio 'items'
            ) 'idea_id')
            $portfolioTop = @(Get-ArrayValue $portfolio `
                'top_10_deep_dives' | ForEach-Object { [string]$_ })
            Test-UniqueIds $portfolioIds 24 '70_audit final portfolio'
            Test-UniqueIds $portfolioTop 10 '70_audit portfolio top 10'
            if ($finalSelectionIds.Count -gt 0) {
                Test-ExactIdSet $portfolioIds $finalSelectionIds `
                    '70_audit portfolio/selection final 24'
                Test-ExactIdSet $portfolioTop $finalTopIds `
                    '70_audit portfolio/selection top 10'
                Test-ExactIdOrder $portfolioIds $finalSelectionIds `
                    '70_audit portfolio/selection final-24 order'
                Test-ExactIdOrder $portfolioTop $finalTopIds `
                    '70_audit portfolio/selection top-10 order'
            }
        }
    }
    $finalCsv = Join-Path $portfolioDir '02_MATRIX.csv'
    if (Test-Path -LiteralPath $finalCsv -PathType Leaf) {
        try {
            if (@(Import-Csv -LiteralPath $finalCsv).Count -ne 24) {
                Add-Failure '70_audit final matrix does not have 24 rows.'
            }
        } catch {
            Add-Failure "70_audit final matrix is invalid CSV."
        }
    }
    $sourcesPath = Join-Path $finalDir 'SOURCES.json'
    if (Test-Path -LiteralPath $sourcesPath -PathType Leaf) {
        $sources = @(Read-JsonFile $sourcesPath 'final sources')
        Test-UniqueIds (Get-Ids $sources 'id') $sources.Count `
            '70_audit final sources'
    }
    Test-ResultFile $directory '70_audit'
}

function Test-ActualStage {
    param([string]$StageName)
    switch ($StageName) {
        '10_refresh' { Test-10Refresh }
        '20_p4' { Test-20P4 }
        '30_redteam' { Test-30Redteam }
        '40_select' { Test-40Select }
        '45_packs' { Test-45Packs }
        '50_deep' { Test-50Deep }
        '60_synth' { Test-60Synth }
        '70_audit' { Test-70Audit }
    }
}

function Test-Checkpoint {
    param([string]$StageName)
    if (-not [string]::IsNullOrWhiteSpace($BasePath)) {
        return
    }
    $path = Join-Path $Root "state\stages\$StageName.json"
    $marker = Read-JsonFile $path "$StageName checkpoint"
    if ($null -eq $marker) {
        return
    }
    if ([string](Get-Value $marker 'stage' '') -ne $StageName -or
        [string](Get-Value $marker 'status' '') -ne 'COMPLETE') {
        Add-Failure "$StageName checkpoint identity/status is invalid."
    }
    $model = [string](Get-Value $marker 'model_observed' '')
    $effort = [string](Get-Value $marker 'effort_observed' '')
    if ($model -notmatch '(?i)fable' -or $model -notmatch '5') {
        Add-Failure "$StageName checkpoint is not verified as Fable 5."
    }
    if (@('xhigh','not_exposed') -notcontains $effort -or
        [string](Get-Value $marker 'effort_requested' '') -ne 'xhigh') {
        Add-Failure (
            "$StageName checkpoint effort evidence conflicts with requested " +
            'xhigh.'
        )
    }
    $files = @(Get-ArrayValue $marker 'output_files')
    if ($files.Count -lt 1) {
        Add-Failure "$StageName checkpoint has no output hashes."
    }
    foreach ($file in $files) {
        $relative = [string](Get-Value $file 'path' '')
        $expected = [string](Get-Value $file 'sha256' '')
        if ([string]::IsNullOrWhiteSpace($relative) -or
            [System.IO.Path]::IsPathRooted($relative) -or
            $relative -match '(^|[\\/])\.\.([\\/]|$)') {
            Add-Failure "$StageName checkpoint has an unsafe path."
            continue
        }
        $full = Join-Path $Root $relative
        if (-not (Test-Path -LiteralPath $full -PathType Leaf)) {
            Add-Failure "$StageName checkpoint file is missing: $relative"
            continue
        }
        $actual = (Get-FileHash -Algorithm SHA256 `
            -LiteralPath $full).Hash.ToUpperInvariant()
        if ($actual -ne $expected.ToUpperInvariant()) {
            Add-Failure "$StageName checkpoint hash mismatch: $relative"
        }
    }
    $pilotMarker = Join-Path $Root "pilot\$StageName\PILOT_COMPLETE.json"
    if (-not (Test-Path -LiteralPath $pilotMarker -PathType Leaf)) {
        Add-Failure "$StageName pilot checkpoint is missing."
    }
}

function Test-Telemetry {
    if (-not [string]::IsNullOrWhiteSpace($BasePath)) {
        return
    }
    foreach ($pauseName in @(
        'MODEL_RETRY.json','MODEL_PAUSE.json','PAUSE.json'
    )) {
        $pause = Join-Path $Root "state\$pauseName"
        if (Test-Path -LiteralPath $pause -PathType Leaf) {
            Add-Failure "Protected pause exists: state\$pauseName"
        }
    }
    $path = Join-Path $Root 'logs\status.jsonl'
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        Add-Failure 'Missing logs\status.jsonl model/effort telemetry.'
        return
    }
    $last = $null
    foreach ($line in [System.IO.File]::ReadAllLines($path)) {
        if ([string]::IsNullOrWhiteSpace($line)) {
            continue
        }
        try {
            $last = $line | ConvertFrom-Json
        } catch {
            Add-Failure 'logs\status.jsonl contains invalid JSON.'
        }
    }
    if ($null -eq $last) {
        Add-Failure 'logs\status.jsonl has no telemetry records.'
        return
    }
    $model = [string](Get-Value $last 'model_id' '')
    $effort = [string](Get-Value $last 'effort' '')
    if ($model -notmatch '(?i)fable' -or $model -notmatch '5') {
        Add-Failure 'Latest status model is not verifiably Fable 5.'
    }
    if (@('xhigh','not_exposed') -notcontains $effort) {
        Add-Failure 'Latest status effort explicitly conflicts with xhigh.'
    }
}

if (-not $All -and [string]::IsNullOrWhiteSpace($Stage)) {
    Add-Failure 'Specify -Stage <name> or -All.'
} elseif ($All) {
    foreach ($name in $Stages) {
        Test-PilotStage $name
        Test-ActualStage $name
        Test-Checkpoint $name
    }
    Test-Telemetry
} elseif ($Pilot) {
    Test-PilotStage $Stage
} else {
    Test-ActualStage $Stage
}

if ($Failures.Count -gt 0) {
    if (-not $Quiet) {
        Write-Host (
            "VALIDATION FAILED ({0} issue(s))." -f $Failures.Count
        ) -ForegroundColor Red
    }
    exit 1
}

if ($All) {
    Write-Pass 'All pilots, stages, checkpoints, telemetry, and final release.'
} elseif ($Pilot) {
    Write-Pass "$Stage pilot."
} else {
    Write-Pass "$Stage outputs."
}
exit 0
