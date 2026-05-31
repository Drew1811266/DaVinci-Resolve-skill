"""Dry-run render output path collision checks.

This script does not connect to Resolve and does not add or start render jobs.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Dry-run Resolve render output paths.")
    parser.add_argument("--output-dir", required=True, help="Target render directory.")
    parser.add_argument("--name", required=True, help="Base output filename without extension.")
    parser.add_argument("--extension", required=True, help="Output extension, such as mp4 or mov.")
    parser.add_argument("--timeline", action="append", default=[], help="Timeline name. Repeat for batch renders.")
    args = parser.parse_args()

    output_dir = Path(args.output_dir).expanduser()
    extension = args.extension.lstrip(".")
    timelines = args.timeline or ["current_timeline"]
    print("DRY RUN: no Resolve render jobs will be added or started.")
    print(f"Output directory: {output_dir}")
    if not output_dir.exists():
        print("Directory does not exist and would need to be created or changed.")
    for timeline in timelines:
        filename = f"{args.name}-{timeline}.{extension}" if len(timelines) > 1 else f"{args.name}.{extension}"
        target = output_dir / filename
        status = "exists: overwrite confirmation required" if target.exists() else "available"
        print(f"- {timeline}: {target} [{status}]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
