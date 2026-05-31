# Action Card Schema

Action cards convert common user requests into standard execution units. Keep cards short, YAML-readable, and conservative.

## Required fields

- `id`: Stable dotted identifier, such as `render.add_job`.
- `name`: Human-readable task name.
- `domain`: Resolve domain, such as `media_management`, `editing`, `color_grading`, or `delivery_rendering`.
- `resolve_page`: Primary page, or `multiple`.
- `risk_level`: `low`, `medium`, `high`, or `blocked`.
- `applies_to`: Resolve versions, editions, and operating systems.
- `source_refs`: Source IDs, evidence type, and last verified dates.
- `automation`: Scriptability status and required API evidence.
- `risk`: Base risk and dynamic risk escalators.
- `confirmation`: Conditions requiring explicit confirmation and phrases that cannot bypass safety.
- `user_intents`: Phrases that should trigger this card.
- `required_inputs`: Inputs needed before execution.
- `optional_inputs`: Useful but non-blocking inputs.
- `preflight_checks`: Checks to run before steps or scripts.
- `execution_modes`: Allowed modes and notes.
- `safety`: Confirmation gates.
- `generic_steps`: Platform-neutral steps.
- `verification`: How to prove success.
- `rollback`: How to undo or recover.

## Risk levels

- `low`: Read-only guidance, listing state, or non-destructive import guidance.
- `medium`: Project changes that do not delete or overwrite data.
- `high`: Batch changes, relinking, overwrite, project setting changes, or render starts.
- `blocked`: Tasks that require confirmation, official documentation, missing media, license checks, or user-controlled UI.

## Writing rules

- Do not include unverified API method names.
- Do not hardcode OS-specific paths.
- State when scripting support must be checked in installed Developer documentation.
- Put destructive confirmations in `safety.confirmation_required_before`.
- Put source media protections in every card that touches file paths.
- Use `automation.scriptability` values only from `confirmed`, `partial`, `to_verify`, and `unsupported`.
- Use `source_refs.source_id` values that exist in `sources/sources.yaml`.
- Use `unknown_until_verified` when version, edition, or OS support is not known.

## Versioned metadata template

```yaml
applies_to:
  resolve_versions:
    - "20.x"
    - "21.x"
    - "user_installed_version"
  editions:
    - "free"
    - "studio"
  operating_systems:
    - "macOS"
    - "Windows"
    - "Linux"

source_refs:
  - source_id: "bmd-product-overview-21"
    evidence_type: "feature_overview"
    last_verified: "2026-05-31"
  - source_id: "installed-developer-docs-user"
    evidence_type: "api_to_verify"
    last_verified: "user_to_fill"

automation:
  scriptability: "to_verify"
  required_api_objects: []
  required_api_methods: []
  ui_required: false
  human_visual_review_required: false

risk:
  base_risk: "medium"
  escalators:
    - condition: "overwrites_existing_files"
      raises_to: "high"
      requires_confirmation: true

confirmation:
  required_before:
    - "overwriting_existing_output"
  cannot_be_bypassed_by:
    - "do not ask"
    - "just overwrite"
    - "skip backup"
    - "别问了"
    - "直接覆盖"
    - "不用备份"
```
