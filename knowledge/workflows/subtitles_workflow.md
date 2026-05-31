# Subtitles Workflow

## Purpose

Plan subtitle creation, import, export, and render behavior without confusing track subtitles, burned-in subtitles, embedded captions, and sidecar files.

## Applies To

- Resolve versions: 20.x, 21.x, user installed version to verify
- Edition: Free and Studio, subtitle feature availability to verify
- OS: macOS, Windows, Linux
- Pages: Edit, Deliver
- Automation status: Partial; exact subtitle API and render behavior must be verified

## Required Inputs

- Target timeline.
- Subtitle source: text, SRT, existing subtitle track, or generated captions.
- Language.
- Desired render behavior: burn-in, embedded, sidecar, or no render.
- Whether existing subtitle tracks may be replaced.

## Workflow

1. Confirm target timeline.
2. Identify subtitle source and format.
3. Confirm whether to create a new track or modify an existing one.
4. Verify timing visually.
5. Confirm render/export subtitle behavior before delivery.

## Risk Escalators

- Replacing existing subtitle tracks.
- Burning subtitles into final output.
- Batch-exporting multiple subtitle versions.
- Claiming newest subtitle APIs without installed documentation.

## Verification

- Subtitle track exists and aligns with dialogue.
- Exported or rendered subtitle mode matches the user request.
- Source subtitle files remain unchanged unless explicitly confirmed.

## Source References

- Source ID: bmd-product-overview-21
- Source ID: installed-developer-docs-user
- Last verified: 2026-05-31
