#!/usr/bin/env python3
"""Validate portable DaVinci Resolve skill assets."""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - depends on host environment
    print("PyYAML is required: python3 -m pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_CARD_KEYS = {
    "id",
    "name",
    "domain",
    "resolve_page",
    "risk_level",
    "user_intents",
    "required_inputs",
    "optional_inputs",
    "preflight_checks",
    "execution_modes",
    "safety",
    "generic_steps",
    "verification",
    "rollback",
}


def load_yaml(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def validate_yaml_files() -> list[str]:
    errors: list[str] = []
    for path in sorted(ROOT.rglob("*.yaml")):
        try:
            data = load_yaml(path)
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)}: YAML parse failed: {exc}")
            continue
        if data is None:
            errors.append(f"{path.relative_to(ROOT)}: YAML file is empty")
    return errors


def validate_action_cards() -> list[str]:
    errors: list[str] = []
    cards = sorted((ROOT / "action_cards").glob("*.yaml"))
    if not cards:
        return ["action_cards/: no action cards found"]
    for path in cards:
        data = load_yaml(path)
        if not isinstance(data, dict):
            errors.append(f"{path.name}: card must be a mapping")
            continue
        missing = REQUIRED_CARD_KEYS - set(data)
        if missing:
            errors.append(f"{path.name}: missing keys: {', '.join(sorted(missing))}")
        risk = data.get("risk_level")
        if risk not in {"low", "medium", "high", "blocked"}:
            errors.append(f"{path.name}: invalid risk_level {risk!r}")
        if not data.get("verification"):
            errors.append(f"{path.name}: verification must not be empty")
        if not data.get("rollback"):
            errors.append(f"{path.name}: rollback must not be empty")
    return errors


def main() -> int:
    errors = validate_yaml_files() + validate_action_cards()
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Skill assets validated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
