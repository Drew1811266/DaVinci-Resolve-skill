"""List projects and folders in the current Project Manager folder.

Read-only script. It does not load, create, delete, or save projects.
"""

from __future__ import annotations

import sys

from _resolve_common import get_current_project


def main() -> int:
    try:
        _resolve, project_manager, project = get_current_project()
        current_folder = project_manager.GetCurrentFolder()
        folders = project_manager.GetFolderListInCurrentFolder() or []
        projects = project_manager.GetProjectListInCurrentFolder() or []
        print(f"Current folder: {current_folder}")
        print("Folders:")
        for name in folders:
            print(f"- {name}")
        print("Projects:")
        for name in projects:
            marker = " (current)" if project is not None and name == project.GetName() else ""
            print(f"- {name}{marker}")
        return 0
    except Exception as exc:
        print(f"Project listing failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
