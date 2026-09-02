[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]] $PlaywrightArguments
)

$ErrorActionPreference = 'Stop'

$playwrightCommand = Get-Command 'playwright-cli' -ErrorAction SilentlyContinue
if ($null -ne $playwrightCommand) {
    $command = $playwrightCommand.Source
    $prefixArguments = @()
}
else {
    $npxCommand = Get-Command 'npx' -ErrorAction SilentlyContinue
    if ($null -eq $npxCommand) {
        throw 'playwright-cli is not installed and npx is unavailable.'
    }
    if ($env:PLAYWRIGHT_ALLOW_NPX_DOWNLOAD -ne '1') {
        throw 'playwright-cli is not installed. Obtain user approval, then set PLAYWRIGHT_ALLOW_NPX_DOWNLOAD=1 to allow npx to download @playwright/cli.'
    }
    $command = $npxCommand.Source
    $prefixArguments = @('--yes', '--package', '@playwright/cli', 'playwright-cli')
}

$hasSession = $false
foreach ($argument in $PlaywrightArguments) {
    if ($argument -eq '--session' -or $argument.StartsWith('--session=')) {
        $hasSession = $true
        break
    }
}

$arguments = @($prefixArguments)
if (-not $hasSession -and -not [string]::IsNullOrWhiteSpace($env:PLAYWRIGHT_CLI_SESSION)) {
    $arguments += @('--session', $env:PLAYWRIGHT_CLI_SESSION)
}
$arguments += $PlaywrightArguments

& $command @arguments
exit $LASTEXITCODE

