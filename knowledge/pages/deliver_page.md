# Deliver Page

## Purpose

Support render setup, queue planning, output verification, and delivery safety.

## Applies To

- Resolve versions: 20.x, 21.x, user installed version to verify
- Edition: Free and Studio, codec and hardware support to verify
- OS: macOS, Windows, Linux
- Automation status: Partially scriptable; exact render API must be verified

## Typical User Intents

- Export a video.
- Add a render job.
- Batch render timelines.
- Export review copies with subtitles.
- Check render settings.

## UI-Capable Tasks

- Configure render presets and custom settings.
- Add jobs to the render queue.
- Start renders after confirmation.

## Scriptable Tasks

Potentially scriptable after API confirmation:

- Read or set render settings.
- Add jobs to render queue.
- Start render jobs.
- Inspect render queue state.

## Tasks Requiring Confirmation

- Overwriting existing outputs.
- Starting long or batch renders.
- Changing project or timeline settings for delivery.

## Safety Notes

- Adding a job and starting a render are separate actions.
- Batch exports should dry-run output paths first.

## Verification

- Render queue contains intended jobs.
- Output files match requested settings after render.
- No unintended overwrite occurred.

## Source References

- Source ID: bmd-product-overview-21
- Source ID: installed-developer-docs-user
- Last verified: 2026-05-31 for high-level page role
