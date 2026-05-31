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
    "applies_to",
    "source_refs",
    "automation",
    "risk",
    "confirmation",
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
RISK_LEVELS = {"low", "medium", "high", "blocked"}
SCRIPTABILITY = {"confirmed", "partial", "to_verify", "unsupported"}
CAPABILITY_STATUS = {"confirmed", "partial", "to_verify", "unsupported"}
EVAL_REQUIRED_KEYS = {"id", "input", "risk_level", "expected"}
NON_BYPASS_PHRASES = {"do not ask", "just overwrite", "skip backup", "别问了", "直接覆盖", "不用备份"}


def source_ids() -> set[str]:
    data = load_yaml(ROOT / "sources" / "sources.yaml")
    if not isinstance(data, dict):
        return set()
    return {
        item.get("id")
        for item in data.get("sources", [])
        if isinstance(item, dict) and isinstance(item.get("id"), str)
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
    known_sources = source_ids()
    cards = sorted((ROOT / "action_cards").glob("*.yaml"))
    if not cards:
        return ["action_cards/: no action cards found"]
    for path in cards:
        data = load_yaml(path)
        if not isinstance(data, dict):
            errors.append(f"{path.name}: card must be a mapping")
            continue
        card_id = data.get("id")
        if isinstance(card_id, str) and path.name != f"{card_id}.yaml":
            errors.append(f"{path.name}: filename must equal id + '.yaml'")
        missing = REQUIRED_CARD_KEYS - set(data)
        if missing:
            errors.append(f"{path.name}: missing keys: {', '.join(sorted(missing))}")
        risk = data.get("risk_level")
        if risk not in RISK_LEVELS:
            errors.append(f"{path.name}: invalid risk_level {risk!r}")
        applies_to = data.get("applies_to")
        if not isinstance(applies_to, dict):
            errors.append(f"{path.name}: applies_to must be a mapping")
        else:
            for key in ("resolve_versions", "editions", "operating_systems"):
                if not applies_to.get(key):
                    errors.append(f"{path.name}: applies_to.{key} must not be empty")
        refs = data.get("source_refs")
        if not isinstance(refs, list) or not refs:
            errors.append(f"{path.name}: source_refs must not be empty")
        else:
            for index, ref in enumerate(refs):
                if not isinstance(ref, dict):
                    errors.append(f"{path.name}: source_refs[{index}] must be a mapping")
                    continue
                ref_id = ref.get("source_id")
                if ref_id not in known_sources:
                    errors.append(f"{path.name}: unknown source_id {ref_id!r}")
                if not ref.get("evidence_type"):
                    errors.append(f"{path.name}: source_refs[{index}].evidence_type must not be empty")
                if not ref.get("last_verified"):
                    errors.append(f"{path.name}: source_refs[{index}].last_verified must not be empty")
        automation = data.get("automation")
        if not isinstance(automation, dict):
            errors.append(f"{path.name}: automation must be a mapping")
        else:
            scriptability = automation.get("scriptability")
            if scriptability not in SCRIPTABILITY:
                errors.append(f"{path.name}: invalid automation.scriptability {scriptability!r}")
            if "likely_scriptable" in str(automation):
                errors.append(f"{path.name}: automation must not use vague 'likely_scriptable' wording")
            for key in ("required_api_objects", "required_api_methods"):
                if not isinstance(automation.get(key), list):
                    errors.append(f"{path.name}: automation.{key} must be a list")
            for key in ("ui_required", "human_visual_review_required"):
                if not isinstance(automation.get(key), bool):
                    errors.append(f"{path.name}: automation.{key} must be boolean")
        dynamic_risk = data.get("risk")
        if not isinstance(dynamic_risk, dict):
            errors.append(f"{path.name}: risk must be a mapping")
        else:
            if dynamic_risk.get("base_risk") not in RISK_LEVELS:
                errors.append(f"{path.name}: invalid risk.base_risk {dynamic_risk.get('base_risk')!r}")
            if not isinstance(dynamic_risk.get("escalators"), list):
                errors.append(f"{path.name}: risk.escalators must be a list")
        confirmation = data.get("confirmation")
        if not isinstance(confirmation, dict):
            errors.append(f"{path.name}: confirmation must be a mapping")
        else:
            required_before = confirmation.get("required_before")
            cannot_bypass = set(confirmation.get("cannot_be_bypassed_by") or [])
            if risk == "high" and not required_before:
                errors.append(f"{path.name}: high-risk card must declare confirmation.required_before")
            if not NON_BYPASS_PHRASES.issubset(cannot_bypass):
                errors.append(f"{path.name}: confirmation.cannot_be_bypassed_by missing required safety phrases")
        if risk == "high":
            safety = data.get("safety")
            if not isinstance(safety, dict) or not safety.get("confirmation_required_before"):
                errors.append(f"{path.name}: high-risk card must have safety.confirmation_required_before")
        inputs_text = " ".join(str(item) for item in data.get("required_inputs", []) + data.get("optional_inputs", []))
        if any(token in inputs_text for token in ("source", "media_path")):
            if "source camera media" not in str(data).lower() and "source files remain unchanged" not in str(data).lower():
                errors.append(f"{path.name}: card touching file paths must protect source media")
        if not data.get("verification"):
            errors.append(f"{path.name}: verification must not be empty")
        if not data.get("rollback"):
            errors.append(f"{path.name}: rollback must not be empty")
    return errors


def validate_knowledge() -> list[str]:
    errors: list[str] = []
    for path in sorted((ROOT / "knowledge").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for heading in ("## Applies To", "## Source References"):
            if heading not in text:
                errors.append(f"{path.relative_to(ROOT)}: missing {heading}")
    return errors


def validate_api_capability_matrix() -> list[str]:
    errors: list[str] = []
    path = ROOT / "knowledge" / "scripting" / "api_capability_matrix.yaml"
    if not path.exists():
        return ["knowledge/scripting/api_capability_matrix.yaml: missing"]
    data = load_yaml(path)
    if not isinstance(data, dict) or not isinstance(data.get("capabilities"), list):
        return ["knowledge/scripting/api_capability_matrix.yaml: capabilities must be a list"]
    known_sources = source_ids()
    seen: set[str] = set()
    for item in data["capabilities"]:
        if not isinstance(item, dict):
            errors.append("api_capability_matrix.yaml: each capability must be a mapping")
            continue
        cap_id = item.get("id")
        if not isinstance(cap_id, str) or not cap_id:
            errors.append("api_capability_matrix.yaml: capability id must not be empty")
        elif cap_id in seen:
            errors.append(f"api_capability_matrix.yaml: duplicate capability id {cap_id!r}")
        else:
            seen.add(cap_id)
        status = item.get("status")
        if status not in CAPABILITY_STATUS:
            errors.append(f"{cap_id}: invalid status {status!r}")
        if item.get("source_id") not in known_sources:
            errors.append(f"{cap_id}: unknown source_id {item.get('source_id')!r}")
        if status == "confirmed" and not item.get("methods"):
            errors.append(f"{cap_id}: confirmed capability must list methods")
        if item.get("risk_level") not in RISK_LEVELS:
            errors.append(f"{cap_id}: invalid risk_level {item.get('risk_level')!r}")
    return errors


def validate_eval_cases() -> list[str]:
    errors: list[str] = []
    cases_dir = ROOT / "evals" / "cases"
    cases = sorted(cases_dir.glob("*.yaml"))
    if not cases:
        return ["evals/cases/: no eval cases found"]
    for path in cases:
        data = load_yaml(path)
        if not isinstance(data, dict):
            errors.append(f"{path.relative_to(ROOT)}: case must be a mapping")
            continue
        missing = EVAL_REQUIRED_KEYS - set(data)
        if missing:
            errors.append(f"{path.relative_to(ROOT)}: missing keys: {', '.join(sorted(missing))}")
        if path.stem != data.get("id"):
            errors.append(f"{path.relative_to(ROOT)}: filename stem must equal id")
        if data.get("risk_level") not in RISK_LEVELS:
            errors.append(f"{path.relative_to(ROOT)}: invalid risk_level {data.get('risk_level')!r}")
        expected = data.get("expected")
        if not isinstance(expected, dict):
            errors.append(f"{path.relative_to(ROOT)}: expected must be a mapping")
            continue
        if data.get("risk_level") == "high" and not expected.get("requires_confirmation"):
            errors.append(f"{path.relative_to(ROOT)}: high-risk case must require confirmation")
        for key in ("must_include", "must_not_include", "required_execution_modes"):
            if key in expected and not isinstance(expected[key], list):
                errors.append(f"{path.relative_to(ROOT)}: expected.{key} must be a list")
    return errors


def validate_adapter_contract() -> list[str]:
    path = ROOT / "adapters" / "generic-agent" / "runtime_contract.md"
    if not path.exists():
        return ["adapters/generic-agent/runtime_contract.md: missing"]
    text = path.read_text(encoding="utf-8")
    required = [
        "Unknown capabilities must be treated as `false`.",
        "can_execute_python",
        "can_access_local_resolve",
        "can_control_ui",
        "can_request_user_confirmation",
        "do not ask",
        "直接覆盖",
    ]
    return [f"{path.relative_to(ROOT)}: missing required text {item!r}" for item in required if item not in text]


def main() -> int:
    errors = (
        validate_yaml_files()
        + validate_action_cards()
        + validate_knowledge()
        + validate_api_capability_matrix()
        + validate_eval_cases()
        + validate_adapter_contract()
    )
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Skill assets validated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
