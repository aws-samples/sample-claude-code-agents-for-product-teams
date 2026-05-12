#!/usr/bin/env bash
# Install the dashboard into a target project's ./artifacts/_dashboard/ directory.
#
# Usage: bash install.sh <target-project-path> [project-name]
#
# Assumes it's invoked from the handbook repo root so it can find
# AI-PDLC-linear-flow.md as the source of truth for data.js.

set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <target-project-path> [project-name]" >&2
  exit 2
fi

TARGET="$1"
PROJECT_NAME="${2:-$(basename "$TARGET")}"
STARTED_AT="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
HANDBOOK_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
MASTER_FLOW="$HANDBOOK_ROOT/AI-PDLC-linear-flow.md"

if [[ ! -f "$MASTER_FLOW" ]]; then
  echo "error: could not find $MASTER_FLOW — run install.sh from the handbook repo" >&2
  exit 1
fi

DASH_DIR="$TARGET/artifacts/_dashboard"
mkdir -p "$DASH_DIR"

cp "$SCRIPT_DIR/dashboard.html" "$DASH_DIR/dashboard.html"
cp "$SCRIPT_DIR/update_status.py" "$DASH_DIR/update_status.py"
chmod +x "$DASH_DIR/update_status.py"

python3 "$SCRIPT_DIR/generate_data.py" "$MASTER_FLOW" "$DASH_DIR/data.js"

if [[ ! -f "$DASH_DIR/status.js" ]]; then
  sed \
    -e "s|__PROJECT_NAME__|$PROJECT_NAME|g" \
    -e "s|__PROJECT_PATH__|$TARGET|g" \
    -e "s|__STARTED_AT__|$STARTED_AT|g" \
    "$SCRIPT_DIR/status.template.js" > "$DASH_DIR/status.js"
  echo "created $DASH_DIR/status.js"
else
  echo "preserving existing $DASH_DIR/status.js"
fi

echo ""
echo "Dashboard installed at: $DASH_DIR"
echo "Open in a browser: file://$DASH_DIR/dashboard.html"

# Auto-open in the default browser unless NO_OPEN=1 is set.
if [[ "${NO_OPEN:-}" != "1" ]]; then
  if command -v open >/dev/null 2>&1; then
    open "$DASH_DIR/dashboard.html"
  elif command -v xdg-open >/dev/null 2>&1; then
    xdg-open "$DASH_DIR/dashboard.html" >/dev/null 2>&1 &
  fi
fi
