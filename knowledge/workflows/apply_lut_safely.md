# Apply LUT Safely Workflow

## Purpose

Apply LUTs with color pipeline awareness and human visual review.

## Applies To

- Resolve versions: 20.x, 21.x, user installed version to verify
- Edition: Free and Studio, LUT location and feature behavior to verify
- OS: macOS, Windows, Linux
- Page: Color
- Automation status: Hybrid recommended; full node graph automation must be verified

## Required Inputs

- LUT name or path.
- LUT type: technical, creative, camera transform, display transform, or unknown.
- Target clips or timeline scope.
- Source and timeline color space.
- Desired strength or reference look.

## Workflow

1. Confirm LUT source and intended color pipeline position.
2. Duplicate timeline or use a test clip for broad scopes.
3. Apply LUT in UI or through confirmed API only when supported.
4. Ask user to visually approve the test result.
5. Apply broadly only after confirmation.

## Risk Escalators

- Unknown LUT type.
- Applying to many clips.
- Changing color management at the same time.
- Skipping visual review.

## Verification

- LUT applies only to intended clips.
- Image remains in expected color space.
- User approves look on representative clips.

## Source References

- Source ID: bmd-product-overview-21
- Source ID: bmd-training-resolve-20
- Source ID: installed-developer-docs-user
- Last verified: 2026-05-31
