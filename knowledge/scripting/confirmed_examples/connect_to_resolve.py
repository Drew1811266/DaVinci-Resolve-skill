"""Connect to Resolve and print read-only application/project state."""

from __future__ import annotations

import sys

from _resolve_common import get_current_project, project_name


def main() -> int:
    try:
        resolve, _project_manager, project = get_current_project()
        product = resolve.GetProductName()
        version = resolve.GetVersionString()
        page = resolve.GetCurrentPage()
        print(f"Product: {product}")
        print(f"Version: {version}")
        print(f"Current page: {page}")
        print(f"Current project: {project_name(project)}")
        return 0
    except Exception as exc:
        print(f"Resolve connection check failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
