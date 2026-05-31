# Render Pipeline Basics

## Purpose

Define render planning concepts before the agent creates render jobs or guides Deliver page work.

## Applies To

- Resolve versions: 20.x, 21.x, user installed version to verify
- Edition: Free and Studio, codec and hardware feature availability to verify
- OS: macOS, Windows, Linux
- Page: Deliver
- Automation status: Partially scriptable; exact API must be checked in installed Developer documentation

## Core Concepts

- Render settings define format, codec, resolution, frame rate, audio, subtitles, data levels, color tags, filename, and destination.
- Render range can be entire timeline or a selected in/out range.
- Output can be a single file or individual clips, depending on workflow.
- A render job can be queued without being started.
- Starting a render can consume significant machine resources and may overwrite files if configured to do so.

## Planning Rules

- Clarify timeline, range, format, codec, resolution, frame rate, output path, filename, audio, subtitles, and overwrite policy.
- Treat codec support as OS, edition, and hardware dependent.
- Use dry-run output path collision checks for batch renders.
- Ask before starting long or batch renders.

## Verification

- Render job appears in the queue with expected settings.
- Output file exists after render.
- Duration, codec, resolution, frame rate, audio channels, and subtitle behavior match the request.
- No unintended overwrite occurred.

## Source References

- Source ID: bmd-product-overview-21
- Source ID: installed-developer-docs-user
- Last verified: 2026-05-31 for high-level workflow context; installed API details remain user-version dependent
