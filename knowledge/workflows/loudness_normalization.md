# Loudness Normalization Workflow

## Purpose

Plan loudness normalization while preserving editorial intent and avoiding destructive audio changes.

## Applies To

- Resolve versions: 20.x, 21.x, user installed version to verify
- Edition: Free and Studio, audio feature availability to verify
- OS: macOS, Windows, Linux
- Page: Fairlight
- Automation status: UI or hybrid recommended; exact audio APIs must be verified

## Required Inputs

- Target timeline.
- Delivery loudness target.
- True peak limit, if required.
- Track, bus, or full mix scope.
- Whether timeline duplication is allowed.

## Workflow

1. Confirm target standard and scope.
2. Duplicate timeline or preserve backup for broad changes.
3. Measure current loudness with confirmed tools.
4. Apply normalization or processing workflow with human listening review.
5. Re-measure and verify no clipping or intelligibility loss.

## Risk Escalators

- Batch-modifying clip gain.
- Changing track or bus processing.
- Applying presets without listening review.
- Delivering to a strict broadcast target.

## Verification

- Integrated loudness and true peak match target.
- Dialogue remains intelligible.
- No unintended tracks were changed.

## Source References

- Source ID: bmd-product-overview-21
- Source ID: bmd-training-resolve-20
- Source ID: installed-developer-docs-user
- Last verified: 2026-05-31
