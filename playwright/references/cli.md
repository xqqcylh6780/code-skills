# Playwright CLI Reference

Use the wrapper for the current platform. Resolve `<skill-root>` from the directory containing this skill's `SKILL.md`.

## Windows PowerShell

```powershell
$pwcli = '<skill-root>\scripts\playwright_cli.ps1'
& $pwcli open 'https://example.com' --headed
& $pwcli snapshot
```

After the user approves an `npx` download for the current command:

```powershell
$env:PLAYWRIGHT_ALLOW_NPX_DOWNLOAD = '1'
& $pwcli --help
```

## POSIX shells

```bash
PWCLI="<skill-root>/scripts/playwright_cli.sh"
"$PWCLI" open https://example.com --headed
"$PWCLI" snapshot
```

After the user approves an `npx` download for the current command:

```bash
PLAYWRIGHT_ALLOW_NPX_DOWNLOAD=1 "$PWCLI" --help
```

## Core commands

```text
open URL [--headed]       Open a page
close                     Close the current browser session
snapshot                  Capture stable element references
click REF                 Click an element
dblclick REF              Double-click an element
type TEXT                 Type into the focused element
fill REF TEXT             Replace an input value
press KEY                 Press a keyboard key
hover REF                 Hover an element
select REF VALUE          Select an option
check REF                 Check a checkbox
uncheck REF               Clear a checkbox
upload PATH               Upload a file after authorization
resize WIDTH HEIGHT       Set the viewport
screenshot [REF]          Capture the viewport or element
pdf                       Save a PDF when supported
console [LEVEL]           Inspect console messages
network                   Inspect network activity
tracing-start             Begin tracing
tracing-stop              Finish tracing
```

## Navigation and tabs

```text
go-back
go-forward
reload
tab-list
tab-new [URL]
tab-close [INDEX]
tab-select INDEX
```

## Sessions

Use a named session to isolate projects or authentication states:

```powershell
$env:PLAYWRIGHT_CLI_SESSION = 'checkout'
& $pwcli open 'https://example.com/checkout'
```

```bash
PLAYWRIGHT_CLI_SESSION=checkout "$PWCLI" open https://example.com/checkout
```

Never persist storage state or session files containing credentials in source control.

