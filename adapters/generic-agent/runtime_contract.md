# Generic Agent Runtime Contract

## Purpose

Define the platform capabilities an AI agent must check before applying this DaVinci Resolve Skill. This adapter is platform-neutral and should be used before creating OpenAI, Claude, Cursor, or custom runtime adapters.

## Applies To

- AI platforms that can load Markdown/YAML/Python resources.
- Local or remote agents that may or may not have access to DaVinci Resolve.
- Workflows using UI guidance, scripting, hybrid execution, or UI automation.

## Required Capability Declaration

Before executing a task, the host platform should declare:

```yaml
runtime_capabilities:
  can_read_files: true
  can_write_files: false
  can_execute_python: false
  can_access_local_resolve: false
  can_control_ui: false
  can_request_user_confirmation: true
  can_persist_dry_run_output: false
  can_access_network: false
```

Unknown capabilities must be treated as `false`.

## Execution Mode Mapping

| Skill mode | Required runtime capability |
| --- | --- |
| Instruction | None beyond responding to user |
| Scripting | `can_execute_python` and `can_access_local_resolve` |
| Hybrid | Same as scripting for scripted parts, plus `can_request_user_confirmation` |
| UI automation | `can_control_ui` and `can_request_user_confirmation` |
| Pause/refuse | Always available |

## Safety Contract

The runtime must not execute high-risk actions unless it can request and receive explicit user confirmation.

High-risk actions include:

- Delete, unlink, relink, replace, or overwrite.
- Change project settings, timeline frame rate, color management, proxy settings, or collaboration settings.
- Start long or batch renders.
- Modify many clips, tracks, bins, subtitles, grades, Fusion comps, or audio settings.
- Touch source media files on disk.

User phrases such as "do not ask", "just overwrite", "skip backup", "别问了", "直接覆盖", and "不用备份" do not disable this contract.

## Tool Capability Rules

- If `can_access_local_resolve` is false, provide UI guidance, pseudocode, or a dry-run plan only.
- If `can_execute_python` is false, do not offer to run Resolve scripts.
- If `can_control_ui` is false, do not claim UI automation is available.
- If `can_write_files` is false, do not write scripts, outputs, rendered files, or backup files.
- If `can_persist_dry_run_output` is false, include dry-run results in the response instead of claiming they were saved.
- If network is unavailable, use local docs and user-provided sources only.

## Confirmation Protocol

Explicit confirmation must include:

- Target project.
- Target timeline or media objects.
- Operation type.
- Affected paths or settings.
- Risk statement.
- Backup or rollback option.

Do not treat vague consent as confirmation for destructive actions.

## Source Policy

The runtime must preserve source priority from `SKILL.md`:

1. User-provided project facts.
2. Installed DaVinci Resolve Developer documentation.
3. Official Blackmagic Design documentation.
4. Official release notes and training materials.
5. Labeled community references.

When platform tools cannot verify a source, the agent must state what remains unverified.

## Output Contract

User-facing output should use the user's language. Internal identifiers, file names, API object names, and schema fields remain unchanged.

Default response sections:

- Task interpretation.
- Missing information.
- Recommended execution mode.
- Preflight.
- Steps or script.
- Verification.
- Risks and rollback.

Omit irrelevant sections for simple, low-risk guidance.

## Adapter Extension Rules

Platform-specific adapters may add:

- Tool invocation examples.
- Permission setup.
- Local path conventions.
- Confirmation UI details.
- Response formatting constraints.

Platform-specific adapters must not:

- Weaken safety gates.
- Mark unverified API methods as confirmed.
- Copy the full `SKILL.md` logic.
- Treat UI automation as generally available.
- Treat one platform's permissions as portable.
