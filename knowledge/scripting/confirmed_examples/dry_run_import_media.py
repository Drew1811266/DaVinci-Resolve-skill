"""Dry-run a media import plan.

This script validates paths and prints what would be imported. It never calls
MediaPool.ImportMedia and never modifies source files or Resolve project state.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def collect_paths(source: Path, recursive: bool) -> list[Path]:
    if source.is_file():
        return [source]
    pattern = "**/*" if recursive else "*"
    return sorted(path for path in source.glob(pattern) if path.is_file() and not path.name.startswith("."))


def main() -> int:
    parser = argparse.ArgumentParser(description="Dry-run Resolve media import paths.")
    parser.add_argument("source", help="Source file or folder to inspect.")
    parser.add_argument("--recursive", action="store_true", help="Include nested files.")
    args = parser.parse_args()

    source = Path(args.source).expanduser()
    if not source.exists():
        print(f"Source does not exist: {source}", file=sys.stderr)
        return 1
    paths = collect_paths(source, args.recursive)
    print("DRY RUN: no Resolve project changes will be made.")
    print(f"Source: {source}")
    print(f"Files that would be offered for import: {len(paths)}")
    for path in paths[:100]:
        print(f"- {path}")
    if len(paths) > 100:
        print(f"... {len(paths) - 100} more files omitted")
    print("Source files remain unchanged.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
