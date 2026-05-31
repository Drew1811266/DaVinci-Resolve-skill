# Resolve Object Model

## Purpose

Give the agent a stable map of DaVinci Resolve project objects before it plans UI steps or scripts.

## Applies To

- Resolve versions: 20.x, 21.x, user installed version to verify
- Edition: Free and Studio, feature availability to verify
- OS: macOS, Windows, Linux
- Automation status: Partially scriptable; exact API must be checked in installed Developer documentation

## Core Model

```text
Resolve application
  -> Project Manager
    -> Project Library / database context
    -> Project
      -> Media Pool
        -> bins / folders
        -> media pool items
      -> Timelines
        -> tracks
        -> timeline items
        -> markers
        -> subtitle tracks
      -> Project settings
      -> Render settings
      -> Render queue
```

## Planning Rules

- Identify the active project before touching media, timelines, render settings, or project settings.
- Identify the target timeline before editing, subtitles, audio, color, Fusion, or render work.
- Treat Media Pool references and source files as different things; removing an item from a project is not the same as deleting a file from disk.
- Treat project settings, timeline settings, color management, relinking, and collaboration settings as high-risk state.
- Use scripting only when the API object and method are confirmed.

## Verification

- Project name matches the user request.
- Target timeline name, duration, frame rate, and track structure match expectations.
- Media Pool bins and items reflect the intended operation.
- Source files remain unchanged unless the user explicitly confirmed a file operation.

## Source References

- Source ID: bmd-product-overview-21
- Source ID: installed-developer-docs-user
- Last verified: 2026-05-31 for high-level product structure; installed API details remain user-version dependent
