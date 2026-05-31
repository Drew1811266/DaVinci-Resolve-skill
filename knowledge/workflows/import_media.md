# Import Media Workflow

## Purpose

Plan safe media import without modifying source camera files.

## Applies To

- Resolve versions: 20.x, 21.x, user installed version to verify
- Edition: Free and Studio, codec support to verify
- OS: macOS, Windows, Linux
- Page: Media
- Automation status: Partially scriptable after import API confirmation

## Required Inputs

- Source path or folder.
- Target project.
- Target bin or bin creation rule.
- Recursive import preference.
- Image sequence handling preference.
- Whether proxy or optimized media generation is requested.

## Workflow

1. Confirm the active project.
2. Validate source path exists.
3. Clarify whether to import only, create bins, create a timeline, or generate proxies.
4. Check source media protection: do not move, delete, rename, or overwrite camera originals.
5. Import through UI guidance or confirmed scripting API.
6. Report imported, skipped, and failed items.

## Risk Escalators

- Generating proxies or optimized media.
- Moving or copying source files.
- Relinking offline media.
- Importing huge folder trees without dry-run.

## Verification

- Clips appear in the target bin.
- Source files remain unchanged.
- Offline and failed imports are reported.

## Source References

- Source ID: bmd-product-overview-21
- Source ID: installed-developer-docs-user
- Last verified: 2026-05-31 for high-level workflow
