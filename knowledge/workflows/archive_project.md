# Archive Project Workflow

## Purpose

Create a recoverable backup or archive before risky work.

## Applies To

- Resolve versions: 20.x, 21.x, user installed version to verify
- Edition: Free and Studio, archive feature availability to verify
- OS: macOS, Windows, Linux
- Pages: Project Manager, Media
- Automation status: UI or hybrid recommended unless API is confirmed

## Required Inputs

- Project name.
- Backup or archive destination.
- Whether media should be included.
- Whether cache, proxies, or optimized media should be included.
- Overwrite policy for existing backup files.

## Workflow

1. Confirm correct project is open.
2. Decide backup scope: project-only backup or archive with media.
3. Validate destination and free disk space.
4. Create backup through verified UI workflow or confirmed API.
5. Verify backup can be found and, when practical, restored or opened.

## Risk Escalators

- Excluding media when the user expects a full archive.
- Overwriting previous backups.
- Archiving huge media trees without checking destination space.

## Verification

- Backup or archive exists at expected path.
- File timestamp matches operation.
- Restore path is understood before risky follow-up work begins.

## Source References

- Source ID: bmd-product-overview-21
- Source ID: installed-developer-docs-user
- Last verified: 2026-05-31 for high-level workflow
