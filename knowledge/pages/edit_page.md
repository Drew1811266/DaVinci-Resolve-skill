# Edit Page

## Purpose

Support timeline editing, track organization, subtitles, markers, and interchange planning.

## Applies To

- Resolve versions: 20.x, 21.x, user installed version to verify
- Edition: Free and Studio, feature availability to verify
- OS: macOS, Windows, Linux
- Automation status: Partially scriptable through confirmed timeline APIs

## Typical User Intents

- Create or modify timelines.
- Add clips, markers, or subtitles.
- Export XML or other interchange.
- Prepare edits for render.

## UI-Capable Tasks

- Arrange and trim clips.
- Add tracks, markers, and subtitles.
- Export timelines through verified UI paths.

## Scriptable Tasks

Potentially scriptable after API confirmation:

- Create timelines.
- List timelines.
- Set current timeline.
- Add or inspect timeline items.
- Export timeline interchange.

## Tasks Requiring Confirmation

- Replacing an existing timeline.
- Changing timeline frame rate.
- Deleting timeline items in bulk.

## Safety Notes

- Timeline frame rate changes are high risk.
- Automated edits should target a duplicate timeline unless the user confirms otherwise.

## Verification

- Timeline name, duration, frame rate, resolution, tracks, and item count match expectations.

## Source References

- Source ID: bmd-product-overview-21
- Source ID: installed-developer-docs-user
- Last verified: 2026-05-31 for high-level page role
