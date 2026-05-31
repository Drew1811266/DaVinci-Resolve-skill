# Python Scripting Patterns

## Applies To

- Resolve versions: installed Scripting README last updated 2025-10-07; user installed version to verify
- Edition: Verify Free/Studio scripting behavior in the user's environment
- OS: macOS, Windows, Linux
- Automation status: Confirmed for connection and read-only inspection patterns in `api_capability_matrix.yaml`

## Safe Pattern

1. Keep configuration at the top.
2. Connect to Resolve.
3. Validate each object before use.
4. Print a dry-run summary before mutation.
5. Require explicit confirmation outside the script for high-risk actions.
6. Catch exceptions and return actionable errors.

## Do Not

- Hardcode user-specific media paths unless the user provided them.
- Delete, relink, replace, render over, or batch-modify without confirmation.
- Call methods not listed as confirmed or provided by the user's official docs.

## Source References

- Source ID: installed-developer-docs-user
- Last verified: 2026-05-31
