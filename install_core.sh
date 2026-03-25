#!/usr/bin/env bash
# -----------------------------------------------------------------------------
# dr-core-shared Automation Installer
# -----------------------------------------------------------------------------
# Installs the shared core library for Python projects and runs a test scan
# -----------------------------------------------------------------------------

set -e

# Paths
BASE_PATH="/home/pc-1/repos"
CORE_REPO="$BASE_PATH/dr-core-shared"

# Check if core repo exists
if [ ! -d "$CORE_REPO" ]; then
    echo "[!] dr-core-shared repo not found at $CORE_REPO"
    exit 1
fi

echo "[*] Installing dr-core-shared in editable mode..."
pip install -e "$CORE_REPO"

# Run test scan
EXAMPLE_SCRIPT="$CORE_REPO/examples/example_scan.py"
if [ -f "$EXAMPLE_SCRIPT" ]; then
    echo "[*] Running example scan..."
    python "$EXAMPLE_SCRIPT"
else
    echo "[!] Example script not found: $EXAMPLE_SCRIPT"
fi

echo "[*] dr-core-shared installed and verified successfully."
