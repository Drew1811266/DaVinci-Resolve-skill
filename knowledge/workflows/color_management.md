# Color Management Workflow

## Purpose

Plan color management decisions without silently changing the interpretation of an existing project.

## Applies To

- Resolve versions: 20.x, 21.x, user installed version to verify
- Edition: Free and Studio, feature availability to verify
- OS: macOS, Windows, Linux
- Page: Color
- Automation status: UI or hybrid recommended; project setting APIs require exact verification

## Required Inputs

- Source camera or file color space.
- Timeline color space.
- Output color space or delivery target.
- Whether the project already has grades.
- Whether the change should apply to a duplicate project or timeline.

## Workflow

1. Inspect current project color assumptions with user-provided context.
2. Identify source, timeline, and output color spaces.
3. Recommend backup or duplicate timeline/project before changes.
4. Apply changes only after explicit confirmation.
5. Review representative shots visually.

## Risk Escalators

- Changing project-wide color management.
- Applying technical LUTs in the wrong color space.
- Batch-updating clips with unknown source color spaces.

## Verification

- Representative clips look correct in the target display pipeline.
- Scopes and image review show no obvious clipping or transform mismatch.
- Existing grades are not unintentionally invalidated.

## Source References

- Source ID: bmd-product-overview-21
- Source ID: bmd-training-resolve-20
- Last verified: 2026-05-31
