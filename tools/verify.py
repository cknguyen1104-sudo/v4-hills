"""Verify the approved V4 baseline; optionally validate WebAssembly with Node."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "baseline-sha256.json").read_text())
errors = []
for name, expected in manifest.items():
    path = root / name
    if not path.is_file():
        errors.append(f"Missing: {name}")
    elif hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        errors.append(f"Changed: {name}")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"PASS: {len(manifest)} approved V4 files match SHA-256 checksums.")
node = shutil.which("node")
if node:
    wasm = [str(root / name) for name in manifest if name.endswith(".wasm")]
    subprocess.run([node, "-e", "for (const f of process.argv.slice(1)) { if (!WebAssembly.validate(require('fs').readFileSync(f))) throw Error(f); console.log('PASS WASM: '+f); }", *wasm], check=True)
else:
    print("Node not installed; optional WASM validation skipped.")
