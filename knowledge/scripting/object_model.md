# Scripting Object Model

## Applies To

- Resolve versions: installed Scripting README last updated 2025-10-07; user installed version to verify
- Edition: Scripting README is for DaVinci Resolve Studio; verify Free edition behavior before relying on automation
- OS: macOS, Windows, Linux
- Automation status: Confirmed for listed low-risk inspection methods in `api_capability_matrix.yaml`

## Purpose

Map confirmed scripting objects to safe operating boundaries.

## Confirmed Starting Path

```text
DaVinciResolveScript.scriptapp("Resolve")
  -> Resolve
    -> GetProjectManager()
      -> ProjectManager
        -> GetCurrentProject()
          -> Project
            -> GetMediaPool()
            -> GetTimelineCount()
            -> GetTimelineByIndex(index)
            -> GetCurrentTimeline()
            -> GetRenderJobList()
```

## Mutation Boundaries

- Read-only inspection can use confirmed low-risk capabilities.
- Import, timeline creation, render settings, and render job creation are medium risk even when APIs are confirmed.
- Delete, relink, overwrite, render start, project settings, timeline settings, and color management are high risk and require explicit confirmation.

## Source References

- Source ID: installed-developer-docs-user
- Last verified: 2026-05-31
