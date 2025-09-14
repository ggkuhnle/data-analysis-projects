#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <notebook1.ipynb> [notebook2.ipynb ... | dir]" >&2
  exit 1
fi

# Collect target files
files=()
for arg in "$@"; do
  if [[ -d "$arg" ]]; then
    while IFS= read -r -d '' f; do files+=("$f"); done < <(find "$arg" -type f -name '*.ipynb' -print0)
  elif [[ -f "$arg" ]]; then
    files+=("$arg")
  else
    echo "Skipping (not found): $arg" >&2
  fi
done

if [[ ${#files[@]} -eq 0 ]]; then
  echo "No .ipynb files to process." >&2
  exit 1
fi

for nb in "${files[@]}"; do
  python3 - "$nb" <<'PYCODE'
import json, sys, pathlib

p = pathlib.Path(sys.argv[1])
nb = json.loads(p.read_text(encoding="utf-8"))
changed = False

for cell in nb.get("cells", []):
    if cell.get("cell_type") != "markdown":
        continue
    src = cell.get("source", [])
    if isinstance(src, str):
        lines = src.splitlines(keepends=True)
    else:
        lines = list(src)

    # Find first non-empty line
    i = 0
    while i < len(lines) and lines[i].strip() == "":
        i += 1

    # Replace leading '---'
    if i < len(lines) and lines[i].strip() == "---":
        nl = "\n" if lines[i].endswith("\n") else ""
        lines[i] = "<hr />" + nl
        cell["source"] = lines
        changed = True

if changed:
    backup = p.with_suffix(p.suffix + ".bak")
    backup.write_text(json.dumps(nb, ensure_ascii=False, indent=2), encoding="utf-8")
    p.write_text(json.dumps(nb, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Patched: {p} (backup at {backup})")
else:
    print(f"No changes: {p}")
PYCODE
done

