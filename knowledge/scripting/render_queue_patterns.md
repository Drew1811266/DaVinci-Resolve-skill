# Render Queue Patterns

## Applies To

- Resolve versions: installed Scripting README last updated 2025-10-07; user installed version to verify
- Edition: Codec and hardware availability to verify
- OS: macOS, Windows, Linux
- Automation status: Confirmed APIs exist for queue inspection, settings, job creation, and render start

## Safe Pattern

1. Inspect current project and timeline.
2. Dry-run output path and filename collision checks.
3. Check format and codec availability.
4. Set render settings only after user confirms.
5. Add render job.
6. Start rendering only after explicit confirmation.

## High-Risk Operations

- Starting all queued render jobs.
- Overwriting existing files.
- Changing render mode, format, codec, or data levels without review.

## Source References

- Source ID: installed-developer-docs-user
- Last verified: 2026-05-31
