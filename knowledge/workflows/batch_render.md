# Batch Render Workflow

## Purpose

Plan batch rendering across timelines or versions with dry-run output collision checks.

## Applies To

- Resolve versions: 20.x, 21.x, user installed version to verify
- Edition: Free and Studio, codec and hardware support to verify
- OS: macOS, Windows, Linux
- Page: Deliver
- Automation status: Scriptable after render settings and queue APIs are confirmed

## Required Inputs

- Timeline list.
- Output directory.
- Naming pattern.
- Format and codec.
- Subtitle behavior.
- Whether rendering should start automatically.
- Overwrite policy.

## Workflow

1. List target timelines.
2. Build output paths from naming pattern.
3. Run dry-run collision checks.
4. Confirm overwrites, if any.
5. Add render jobs using confirmed API or UI guidance.
6. Start rendering only after explicit confirmation.

## Risk Escalators

- Batch scope.
- Existing output collisions.
- Starting render immediately.
- Mixed subtitle or audio versions.

## Verification

- Every requested timeline maps to one intended output path.
- Render queue contains expected jobs.
- Outputs exist after render and match requested settings.
- No unintended overwrite occurred.

## Source References

- Source ID: bmd-product-overview-21
- Source ID: installed-developer-docs-user
- Last verified: 2026-05-31
