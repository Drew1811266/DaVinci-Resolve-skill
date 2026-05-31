#!/usr/bin/env python3
"""Run lightweight behavior assertions for DaVinci Resolve skill eval cases."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("PyYAML is required: python3 -m pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)


ROOT = Path(__file__).resolve().parents[1]
CASES_DIR = ROOT / "evals" / "cases"
RISK_LEVELS = {"low", "medium", "high", "blocked"}


def load_yaml_or_json(path: Path) -> object:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    return yaml.safe_load(text)


def load_cases() -> list[dict]:
    cases: list[dict] = []
    for path in sorted(CASES_DIR.glob("*.yaml")):
        data = load_yaml_or_json(path)
        if not isinstance(data, dict):
            raise ValueError(f"{path}: case must be a mapping")
        data["_path"] = str(path.relative_to(ROOT))
        cases.append(data)
    return cases


def validate_case(case: dict) -> list[str]:
    errors: list[str] = []
    label = case.get("id", case.get("_path", "<unknown>"))
    for key in ("id", "input", "risk_level", "expected"):
        if key not in case:
            errors.append(f"{label}: missing {key}")
    if case.get("risk_level") not in RISK_LEVELS:
        errors.append(f"{label}: invalid risk_level {case.get('risk_level')!r}")
    expected = case.get("expected")
    if not isinstance(expected, dict):
        errors.append(f"{label}: expected must be a mapping")
        return errors
    for key in ("must_include", "must_not_include", "required_execution_modes"):
        value = expected.get(key, [])
        if not isinstance(value, list):
            errors.append(f"{label}: expected.{key} must be a list")
    for key in ("requires_confirmation", "requires_version_check"):
        value = expected.get(key, False)
        if not isinstance(value, bool):
            errors.append(f"{label}: expected.{key} must be boolean")
    if case.get("risk_level") == "high" and not expected.get("requires_confirmation"):
        errors.append(f"{label}: high-risk case must require confirmation")
    return errors


def evaluate_response(case: dict, response: str) -> list[str]:
    errors: list[str] = []
    expected = case["expected"]
    label = case["id"]
    response_lower = response.lower()
    for text in expected.get("must_include", []):
        if text.lower() not in response_lower:
            errors.append(f"{label}: response missing required text {text!r}")
    for text in expected.get("must_not_include", []):
        if text.lower() in response_lower:
            errors.append(f"{label}: response includes forbidden text {text!r}")
    for text in expected.get("forbidden_api_claims", []) or []:
        if text.lower() in response_lower:
            errors.append(f"{label}: response appears to claim forbidden API {text!r}")
    if expected.get("requires_confirmation") and not any(
        token in response for token in ("确认", "explicit confirmation", "明确确认", "请确认")
    ):
        errors.append(f"{label}: response does not appear to request confirmation")
    if expected.get("requires_version_check") and not any(
        token in response for token in ("版本", "version", "Resolve version")
    ):
        errors.append(f"{label}: response does not appear to request/check version")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate and optionally score behavior eval responses.")
    parser.add_argument("--responses", help="YAML/JSON mapping from case id to agent response.")
    args = parser.parse_args()

    errors: list[str] = []
    cases = load_cases()
    if not cases:
        errors.append("No eval cases found.")
    for case in cases:
        errors.extend(validate_case(case))

    if args.responses:
        response_map = load_yaml_or_json(Path(args.responses))
        if not isinstance(response_map, dict):
            errors.append("--responses file must contain a mapping from case id to response")
        else:
            for case in cases:
                response = response_map.get(case.get("id"))
                if response is None:
                    errors.append(f"{case.get('id')}: missing response")
                elif not isinstance(response, str):
                    errors.append(f"{case.get('id')}: response must be a string")
                else:
                    errors.extend(evaluate_response(case, response))

    if errors:
        print("Behavior eval failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Behavior eval cases validated: {len(cases)}")
    if args.responses:
        print("Responses passed lightweight assertions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
