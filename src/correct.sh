#!/usr/bin/env bash
set -euo pipefail

# hop to repo root if available
if git rev-parse --show-toplevel >/dev/null 2>&1; then
  cd "$(git rev-parse --show-toplevel)"
fi

TARGET="notebooks"
[[ -d "$TARGET" ]] || TARGET="."   # fallback if notebooks/ isn't present

echo "Scanning under: $TARGET"
export PYTHONUNBUFFERED=1

find "$TARGET" -name "*.ipynb" -print0 | while IFS= read -r -d '' f; do
  python3 - "$f" <<'PY'
import json, sys, pathlib
p = pathlib.Path(sys.argv[1])
orig = p.read_text(encoding="utf-8")
nb = json.loads(orig)
changed = False

for cell in nb.get("cells", []):
    if not isinstance(cell.get("metadata"), dict):
        cell["metadata"] = {}
        changed = True
    tags = cell["metadata"].get("tags")
    if tags is None:
        cell["metadata"]["tags"] = []
        changed = True
    elif not isinstance(tags, list):
        cell["metadata"]["tags"] = [str(tags)]
        changed = True

if changed:
    p.with_suffix(p.suffix + ".bak").write_text(orig, encoding="utf-8")  # backup original
    p.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Fixed: {p}")
else:
    print(f"OK:    {p}")
PY
done
