"""Minimal DaVinci Resolve scripting connection template.

This template checks common import paths and fails safely. It does not perform
project mutations.
"""

from __future__ import annotations

import importlib
import os
import sys
from pathlib import Path
from typing import Any


def add_common_resolve_module_paths() -> None:
    """Add likely Resolve scripting module locations without assuming one works."""
    candidates = [
        os.environ.get("RESOLVE_SCRIPT_API"),
        "/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules",
        "C:/ProgramData/Blackmagic Design/DaVinci Resolve/Support/Developer/Scripting/Modules",
        "/opt/resolve/Developer/Scripting/Modules",
    ]
    for value in candidates:
        if value and Path(value).exists() and value not in sys.path:
            sys.path.append(value)


def get_resolve() -> Any:
    """Return a Resolve object or raise a clear error."""
    add_common_resolve_module_paths()
    try:
        module = importlib.import_module("DaVinciResolveScript")
    except ImportError as exc:
        raise RuntimeError(
            "Could not import DaVinciResolveScript. Confirm Resolve is installed "
            "and check Help > Documentation > Developer for the scripting path."
        ) from exc

    resolve = module.scriptapp("Resolve")
    if resolve is None:
        raise RuntimeError("Could not connect to Resolve. Start DaVinci Resolve and try again.")
    return resolve


def main() -> int:
    try:
        resolve = get_resolve()
        project_manager = resolve.GetProjectManager()
        if project_manager is None:
            raise RuntimeError("Connected to Resolve but could not access Project Manager.")
        project = project_manager.GetCurrentProject()
        if project is None:
            print("Connected to Resolve. No project is currently open.")
            return 0
        print(f"Connected to Resolve project: {project.GetName()}")
        return 0
    except Exception as exc:
        print(f"Resolve scripting preflight failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
