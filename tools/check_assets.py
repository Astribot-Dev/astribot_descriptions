#!/usr/bin/env python3
"""Verify the complete model inventory and asset payloads from manifest.json."""
import hashlib
import json
import sys
from pathlib import Path, PurePosixPath


def check(root):
    root = root.resolve()
    manifest = json.loads((root / "manifest.json").read_text())
    if manifest.get("schema_version") != 1:
        raise ValueError("Unsupported asset manifest schema")
    allowed_roots = {"astribot_s1", "astribot_t1"}
    entries = manifest["files"]
    expected, errors = set(), []
    for entry in entries:
        raw = entry["path"]
        path = PurePosixPath(raw)
        if path.is_absolute() or ".." in path.parts or not path.parts:
            errors.append(f"Invalid manifest path: {raw}")
            continue
        if path.parts[0] not in allowed_roots or raw in expected:
            errors.append(f"Unexpected or duplicate manifest path: {raw}")
            continue
        expected.add(raw)
        target = root / path
        if target.is_symlink() or not target.resolve().is_relative_to(root):
            errors.append(f"Unsafe model path: {raw}")
            continue
        if not target.is_file():
            errors.append(f"Missing asset: {raw}")
            continue
        digest = hashlib.sha256()
        size = 0
        with target.open("rb") as handle:
            first = handle.read(1024 * 1024)
            if first.startswith(b"version https://git-lfs.github.com/spec/v1\n"):
                errors.append(f"LFS payload is missing: {raw}")
                continue
            while first:
                size += len(first)
                digest.update(first)
                first = handle.read(1024 * 1024)
        if size != entry["size"] or digest.hexdigest() != entry["sha256"]:
            errors.append(f"Asset content differs from manifest: {raw}")
        oid = entry.get("lfs_oid")
        if oid and oid != "sha256:" + entry["sha256"]:
            errors.append(f"LFS OID disagrees with asset digest: {raw}")
    actual = {p.relative_to(root).as_posix()
              for name in allowed_roots for p in (root / name).rglob("*")
              if p.is_file() or p.is_symlink()}
    for path in sorted(actual - expected):
        errors.append(f"Unlisted model asset: {path}")
    if not expected:
        errors.append("Manifest contains no model assets")
    return {"model_assets": len(expected), "errors": errors, "passed": not errors}


if __name__ == "__main__":
    try:
        result = check(Path(__file__).resolve().parents[1])
    except (KeyError, ValueError, OSError) as exc:
        result = {"passed": False, "errors": [str(exc)]}
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["passed"] else 1)
