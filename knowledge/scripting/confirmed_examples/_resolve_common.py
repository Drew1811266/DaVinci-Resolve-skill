"""Shared helpers for conservative Resolve scripting examples."""

from __future__ import annotations

import importlib
import os
import sys
from pathlib import Path
from typing import Any


def add_module_paths() -> None:
    candidates = [
        os.environ.get("RESOLVE_SCRIPT_API")
        and str(Path(os.environ["RESOLVE_SCRIPT_API"]) / "Modules"),
        "/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules",
        "C:/ProgramData/Blackmagic Design/DaVinci Resolve/Support/Developer/Scripting/Modules",
        "/opt/resolve/Developer/Scripting/Modules",
    ]
    for value in candidates:
        if value and Path(value).exists() and value not in sys.path:
            sys.path.append(value)


def get_resolve() -> Any:
    add_module_paths()
    try:
        module = importlib.import_module("DaVinciResolveScript")
    except ImportError as exc:
        raise RuntimeError("Could not import DaVinciResolveScript. Check installed Developer/Scripting paths.") from exc
    resolve = module.scriptapp("Resolve")
    if resolve is None:
        raise RuntimeError("Could not connect to Resolve. Start DaVinci Resolve and try again.")
    return resolve


def get_current_project() -> tuple[Any, Any, Any]:
    resolve = get_resolve()
    project_manager = resolve.GetProjectManager()
    if project_manager is None:
        raise RuntimeError("Connected to Resolve but ProjectManager is unavailable.")
    project = project_manager.GetCurrentProject()
    return resolve, project_manager, project


def project_name(project: Any) -> str:
    return project.GetName() if project is not None else "<no project open>"
