# Project, Media, and Timeline Model

## Purpose

Define how project, media, and timeline concepts relate so the agent can avoid destructive ambiguity.

## Applies To

- Resolve versions: 20.x, 21.x, user installed version to verify
- Edition: Free and Studio, feature availability to verify
- OS: macOS, Windows, Linux
- Automation status: Partially scriptable; exact API must be checked in installed Developer documentation

## Concepts

- Project: The Resolve container for media pool, timelines, settings, grades, Fusion comps, Fairlight state, and render queue.
- Media Pool: Project-level references to source media. It does not imply source files were copied, moved, or transcoded.
- Bin: Media Pool organization container.
- Media Pool Item: A project reference to a piece of media or generated asset.
- Timeline: An ordered edit structure containing tracks and timeline items.
- Track: Video, audio, or subtitle lane in a timeline.
- Timeline Item: A clip instance on a timeline. It is not the same object as the source file.
- Render Queue: Project state describing pending or completed render jobs.

## Ambiguity Rules

- "Delete unused media" is ambiguous; clarify Media Pool removal versus disk deletion.
- "Import media" is ambiguous; clarify import only, import with bin creation, import image sequence, proxy generation, optimized media, or timeline creation.
- "Export timeline" is ambiguous; clarify render output, XML/AAF/EDL interchange, subtitle export, or project archive.
- "Fix offline media" is high risk; clarify relink paths and backup state before action.

## Safety Notes

- Never delete source files based on Media Pool state alone.
- Never change timeline frame rate without explicit confirmation.
- Never assume output files can overwrite older deliverables.

## Verification

- Compare project object names against user-provided names.
- Verify source file paths still exist.
- Verify timeline structure and render queue state after operations.

## Source References

- Source ID: bmd-product-overview-21
- Source ID: installed-developer-docs-user
- Last verified: 2026-05-31 for high-level model; installed API details remain user-version dependent
