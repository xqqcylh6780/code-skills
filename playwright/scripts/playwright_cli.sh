#!/usr/bin/env bash
set -euo pipefail

has_session_flag="false"
for arg in "$@"; do
  case "$arg" in
    --session|--session=*)
      has_session_flag="true"
      break
      ;;
  esac
done

if command -v playwright-cli >/dev/null 2>&1; then
  cmd=(playwright-cli)
else
  if ! command -v npx >/dev/null 2>&1; then
    echo "Error: playwright-cli is not installed and npx is unavailable." >&2
    exit 1
  fi
  if [[ "${PLAYWRIGHT_ALLOW_NPX_DOWNLOAD:-0}" != "1" ]]; then
    echo "Error: playwright-cli is not installed. Obtain user approval, then set PLAYWRIGHT_ALLOW_NPX_DOWNLOAD=1 to allow npx to download @playwright/cli." >&2
    exit 2
  fi
  cmd=(npx --yes --package @playwright/cli playwright-cli)
fi

if [[ "${has_session_flag}" != "true" && -n "${PLAYWRIGHT_CLI_SESSION:-}" ]]; then
  cmd+=(--session "${PLAYWRIGHT_CLI_SESSION}")
fi
cmd+=("$@")

exec "${cmd[@]}"

