param(
    [switch]$Todos, [switch]$Claude, [switch]$Codex, [switch]$Cursor,
    [switch]$OpenCode, [switch]$Agents, [switch]$Conferir, [string]$Destino
)
$ErrorActionPreference = "Stop"
$RepoDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$InstallArgs = @()
foreach ($Flag in @("Todos", "Claude", "Codex", "Cursor", "OpenCode", "Agents", "Conferir")) {
    if (Get-Variable -Name $Flag -ValueOnly) { $InstallArgs += "--$($Flag.ToLower())" }
}
if ($Destino) { $InstallArgs += @("--destino", $Destino) }
if (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3 (Join-Path $RepoDir "scripts/instalar.py") @InstallArgs
} else {
    & python (Join-Path $RepoDir "scripts/instalar.py") @InstallArgs
}
exit $LASTEXITCODE
