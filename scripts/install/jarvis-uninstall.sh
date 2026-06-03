#!/usr/bin/env bash
# Chottu-uninstall.sh — clean removal of Chottu from $HOME.
#
# Removes:
#   ~/.Chottu/
#   ~/.local/bin/Chottu
#   ~/.local/bin/Chottu-uninstall
#
# Does NOT remove: ollama, uv, or the Rust toolchain.

set -euo pipefail

Chottu_HOME="${Chottu_HOME:-$HOME/.Chottu}"

if [[ -f "$Chottu_HOME/.state/bg.pid" ]]; then
    pid=$(cat "$Chottu_HOME/.state/bg.pid" 2>/dev/null || echo "")
    if [[ -n "$pid" ]] && kill -0 "$pid" 2>/dev/null; then
        echo "Stopping background work (pid=$pid)..."
        kill "$pid" 2>/dev/null || true
    fi
fi

if command -v ollama >/dev/null 2>&1; then
    ollama stop >/dev/null 2>&1 || true
fi

if [[ -d "$Chottu_HOME" ]]; then
    rm -rf "$Chottu_HOME"
    echo "Removed $Chottu_HOME"
fi

for f in "$HOME/.local/bin/Chottu" "$HOME/.local/bin/Chottu-uninstall"; do
    if [[ -L "$f" ]] || [[ -f "$f" ]]; then
        rm -f "$f"
        echo "Removed $f"
    fi
done

cat <<EOF

Chottu removed.

Left intact (may be used by other tools):
  - Ollama       (uninstall: brew uninstall ollama  /  rm -f /usr/local/bin/ollama)
  - uv           (uninstall: rm -rf ~/.local/share/uv ~/.cargo/bin/uv)
  - Rust toolchain (uninstall: rustup self uninstall)
EOF
