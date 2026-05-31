# Color Page

## Purpose

Support grading, LUT planning, color management checks, and visual review workflows.

## Applies To

- Resolve versions: 20.x, 21.x, user installed version to verify
- Edition: Free and Studio, feature availability to verify
- OS: macOS, Windows, Linux
- Automation status: Hybrid recommended; exact node or grade API support must be verified

## Typical User Intents

- Apply LUTs.
- Match shots.
- Create a look.
- Adjust exposure, contrast, saturation, or color balance.
- Change color management.

## UI-Capable Tasks

- Grade clips.
- Review scopes and image quality.
- Apply or disable LUTs.
- Adjust nodes and color management with user confirmation.

## Scriptable Tasks

Do not claim node graph mutation or grade automation unless installed Developer documentation confirms the exact API.

## Tasks Requiring Human Review

- Aesthetic looks, skin tone judgment, exposure choices, shot matching, and creative LUT strength.

## Safety Notes

- Changing color management is high risk.
- Apply LUTs to a test clip or duplicated timeline before broad application.

## Verification

- Grade applies only to intended clips.
- Image is evaluated in the intended color pipeline.
- No unintended clipping, saturation, or color-space mismatch is visible.

## Source References

- Source ID: bmd-product-overview-21
- Source ID: bmd-training-resolve-20
- Last verified: 2026-05-31 for high-level workflow context
