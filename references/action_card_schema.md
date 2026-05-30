# Action Card Schema

Action cards convert common user requests into standard execution units. Keep cards short, YAML-readable, and conservative.

## Required fields

- `id`: Stable dotted identifier, such as `render.add_job`.
- `name`: Human-readable task name.
- `domain`: Resolve domain, such as `media_management`, `editing`, `color_grading`, or `delivery_rendering`.
- `resolve_page`: Primary page, or `multiple`.
- `risk_level`: `low`, `medium`, `high`, or `blocked`.
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
