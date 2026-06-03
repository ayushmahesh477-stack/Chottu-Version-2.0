#!/usr/bin/env bash
# Chottu-wrapper.sh — symlinked to ~/.local/bin/Chottu.
# Activates the managed venv and execs the real Chottu CLI.

Chottu_HOME="${Chottu_HOME:-$HOME/.Chottu}"
VENV="$Chottu_HOME/.venv"

if [[ ! -d "$VENV" ]]; then
    echo "Chottu: venv not found at $VENV" >&2
    echo "Re-run the installer: curl -fsSL https://Chottu.github.io/Chottu/install.sh | bash" >&2
    exit 1
fi

exec "$VENV/bin/Chottu" "$@"
