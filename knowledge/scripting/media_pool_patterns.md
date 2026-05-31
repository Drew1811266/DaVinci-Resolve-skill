# Media Pool Patterns

## Applies To

- Resolve versions: installed Scripting README last updated 2025-10-07; user installed version to verify
- Edition: Free and Studio behavior to verify
- OS: macOS, Windows, Linux
- Automation status: Confirmed APIs exist for inspection and media import

## Safe Pattern

1. Inspect project and Media Pool.
2. Validate source paths.
3. Dry-run imported path list.
4. Confirm target folder or bin.
5. Import only after source media protection is clear.

## High-Risk Operations

- Relinking clips.
- Unlinking clips.
- Deleting clips or folders.
- Replacing clips.
- Linking proxy or full-resolution media.

## Source References

- Source ID: installed-developer-docs-user
- Last verified: 2026-05-31
