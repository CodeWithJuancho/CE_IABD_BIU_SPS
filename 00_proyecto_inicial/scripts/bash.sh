#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
WORKSPACE_ROOT="$(cd "$PROJECT_ROOT/.." && pwd)"
DATE="$(date +"%m_%d_%y")"
PYTHON_BIN="$WORKSPACE_ROOT/.venv/bin/python"

if [ ! -x "$PYTHON_BIN" ]; then
  PYTHON_BIN="$(command -v python3 || echo python3)"
fi

echo "Fecha actual: $DATE"
cp "$PROJECT_ROOT/users/extracted/users.csv" "$PROJECT_ROOT/users/processed/${DATE}_processed_users.txt"

echo "Archivo copiado a: $PROJECT_ROOT/users/processed/${DATE}_processed_users.txt"
"$PYTHON_BIN" "$SCRIPT_DIR/python.py" "$PROJECT_ROOT"
