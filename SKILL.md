---
name: davinci-resolve
description: Use when planning, scripting, guiding, or reviewing DaVinci Resolve workflows including media import, project/timeline management, editing, color, Fusion, Fairlight, subtitles, rendering, automation, troubleshooting, and safety checks across Free/Studio editions and macOS/Windows/Linux.
---

# DaVinci Resolve

## Overview

Help users complete DaVinci Resolve work safely by turning requests into explicit plans, scripts, UI instructions, verification steps, and rollback notes. Treat Resolve knowledge as versioned and source-bound; do not invent menus, shortcuts, API methods, codecs, paths, or edition-specific features.

## Operating Rules

1. Parse the task before choosing an execution mode.
2. Ask only the minimum missing questions needed for the task and risk level.
3. Verify version, Free/Studio edition, OS, project state, target timeline, input media, output path, and overwrite permission when relevant.
4. Require explicit confirmation before destructive or broad changes.
5. Prefer official or installed documentation for version-specific behavior.
6. Include verification steps for every operation plan.
7. Include rollback or recovery notes when a change may alter project state or files.
8. Keep platform-specific assumptions isolated; this skill must remain portable across AI agent platforms.

## Execution Modes

Choose one mode for each task:

| Mode | Use when |
| --- | --- |
| Instruction | The user needs guidance, automation is unavailable, or visual judgment matters. |
| Scripting | The task is repeatable, data-oriented, and supported by confirmed Resolve scripting APIs. |
| Hybrid | Scripts can prepare state but the user must visually confirm, refine, or approve in Resolve. |
| UI automation | The current AI platform exposes reliable app-control tools and the user permits UI control. |
| Pause/refuse | The task is unsafe, destructive without confirmation, illegal, impossible, or unsupported. |

## Safety Gates

Never delete, unlink, overwrite, relink, transcode, replace, render over, or batch-modify project/media/timeline data without explicit user confirmation.

Before destructive or broad operations:

1. Identify affected project objects, timelines, bins, clips, media paths, render files, or settings.
2. Recommend or create a backup when possible.
3. State the concrete risk.
4. Ask for confirmation.
5. Provide rollback or recovery guidance.

Never overwrite source camera media. Never assume render outputs may overwrite existing files. Never change project frame rate, timeline frame rate, color management, proxy/optimized media settings, collaboration settings, or source relinking without explicit confirmation.

## Task Workflow

For each user request:

1. Interpret the goal and affected Resolve domain.
2. Search `action_cards/` for a matching card and use its required inputs, safety gates, and verification list.
3. Identify missing context: Resolve version, edition, OS, open project, target timeline, media paths, output settings, backup state, and overwrite permission.
4. Assign risk: low, medium, high, or blocked.
5. Select an execution mode.
6. Produce steps, script, UI guidance, or a minimal clarifying question.
7. End with verification and rollback notes.

Use `references/scripting_policy.md` before generating Python or Lua. Use `references/action_card_schema.md` when adding or revising action cards. Use `sources/sources.yaml` and `sources/version_matrix.yaml` when grounding version- or edition-specific claims.

## Default User Response

Use this structure unless the user asks for a shorter answer:

```markdown
I understand your goal as: ...

Missing information:
- ...

Recommended mode: ...
Reason: ...

Preflight:
- ...

Steps:
1. ...

Verification:
- ...

Risks and rollback:
- ...
```

Omit sections that do not apply. For simple guidance tasks, answer directly but still avoid unverified claims.

## Scripting Rules

Generate executable Resolve automation only when required API objects and methods are confirmed by loaded skill knowledge or user-provided official documentation. If API support is uncertain, provide pseudocode plus a checklist of methods to verify in the installed Developer documentation.

Scripts must:

- Validate Resolve connection, project manager, project, media pool, timeline, and render queue objects before use.
- Separate configuration from execution logic.
- Print clear status messages.
- Fail safely.
- Avoid hardcoded user paths unless provided by the user.
- Avoid deletion or overwrite unless explicitly confirmed.
- Use dry-run behavior for broad or risky operations.

## Source Policy

Prefer knowledge in this order:

1. User-provided project facts.
2. Installed DaVinci Resolve Developer documentation.
3. Official Blackmagic Design documentation.
4. Official release notes and new-feature guides.
5. Official training materials.
6. Community references, clearly labeled as non-authoritative.

If a menu, shortcut, API, codec, license feature, or workflow varies by version, say what needs verification rather than guessing.

## Maintenance

- Keep `manifest.yaml` platform-neutral.
- Keep action cards concise and machine-readable.
- Add source records before adding version-specific facts.
- Add evaluation tasks for any new safety rule, API workflow, or action card.
- Run `scripts/validate_skill_assets.py` and the skill validator after edits.
