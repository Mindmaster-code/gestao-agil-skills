param(
    [switch]$Todos,
    [switch]$Claude,
    [switch]$Codex,
    [switch]$Cursor,
    [switch]$OpenCode,
    [switch]$Agents,
    [string]$Destino
)

$ErrorActionPreference = "Stop"
$RepoDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$SkillsDir = Join-Path $RepoDir "skills"
$Timestamp = (Get-Date).ToUniversalTime().ToString("yyyyMMdd-HHmmss-fff")
$Targets = New-Object System.Collections.Generic.List[string]

if ($Todos -or $Claude) {
    $Targets.Add((Join-Path $HOME ".claude\skills"))
}
if ($Todos -or $Codex) {
    $CodexRoot = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
    $Targets.Add((Join-Path $CodexRoot "skills"))
}
if ($Todos -or $Cursor) {
    $Targets.Add((Join-Path $HOME ".cursor\skills"))
}
if ($Todos -or $OpenCode) {
    $Targets.Add((Join-Path $HOME ".config\opencode\skills"))
}
if ($Todos -or $Agents) {
    $Targets.Add((Join-Path $HOME ".agents\skills"))
}
if ($Destino) {
    $Targets.Add($Destino)
}

if ($Targets.Count -eq 0) {
    Write-Error "Escolha -Todos, um ambiente específico ou -Destino."
}

foreach ($Target in ($Targets | Select-Object -Unique)) {
    New-Item -ItemType Directory -Force -Path $Target | Out-Null
    $Backup = Join-Path $Target ".ga2-backup\$Timestamp"

    foreach ($Source in Get-ChildItem -Path $SkillsDir -Directory -Filter "ga2-*") {
        $Destination = Join-Path $Target $Source.Name
        if (Test-Path $Destination) {
            New-Item -ItemType Directory -Force -Path $Backup | Out-Null
            Move-Item -Path $Destination -Destination (Join-Path $Backup $Source.Name)
        }
        Copy-Item -Path $Source.FullName -Destination $Destination -Recurse
    }

    Write-Output "Instaladas 30 skills em $Target"
}
