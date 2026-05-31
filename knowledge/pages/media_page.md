# Media Page

## Purpose

Organize, inspect, import, and manage media references before editing.

## Applies To

- Resolve versions: 20.x, 21.x, user installed version to verify
- Edition: Free and Studio, codec and collaboration features to verify
- OS: macOS, Windows, Linux
- Automation status: Partially scriptable; import API details must be verified

## Typical User Intents

- Import a folder of footage.
- Create bins.
- Inspect clip metadata.
- Relink offline media.
- Prepare media before timeline creation.

## UI-Capable Tasks

- Import media through the UI.
- Create and organize bins.
- Inspect metadata and clip properties.
- Relink media after user confirms paths.

## Scriptable Tasks

Potentially scriptable after installed Developer documentation confirms methods:

- Read current project and media pool state.
- Import media references.
- Create bins.
- List media pool items.

## Tasks Requiring Confirmation

- Relinking media.
- Deleting media pool items.
- Deleting source files from disk.
- Generating proxies or optimized media.

## Safety Notes

- Importing should not move, delete, or overwrite source camera media.
- Removing from Media Pool must be distinguished from deleting on disk.

## Verification

- Clips appear in the intended bin.
- Source media paths remain unchanged.
- Offline status and metadata match expectations.

## Source References

- Source ID: bmd-product-overview-21
- Source ID: installed-developer-docs-user
- Last verified: 2026-05-31 for high-level page role
