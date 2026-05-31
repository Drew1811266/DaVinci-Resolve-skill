# Color Pipeline Basics

## Purpose

Help the agent treat color tasks as versioned, project-specific, and visually reviewed workflows.

## Applies To

- Resolve versions: 20.x, 21.x, user installed version to verify
- Edition: Free and Studio, feature availability to verify
- OS: macOS, Windows, Linux
- Page: Color
- Automation status: Hybrid recommended; exact scripting support must be verified

## Core Concepts

- Color management defines how source, timeline, and output color spaces are interpreted.
- A LUT can be technical, creative, camera-specific, display-oriented, or user-provided.
- A node graph is a grading structure; node order can change results.
- A look should be reviewed on representative shots before broad application.

## Planning Rules

- Ask for source color space, timeline color space, output color space, LUT type, and target scope when relevant.
- Do not apply a LUT broadly without a test clip or duplicated timeline.
- Do not change project color management without explicit confirmation.
- Prefer Hybrid or UI guidance for aesthetic decisions.

## Verification

- Confirm the LUT or grade affects only intended clips.
- Confirm highlights, shadows, saturation, and skin tones are not visibly broken.
- Confirm the grade is evaluated in the intended color pipeline.

## Source References

- Source ID: bmd-product-overview-21
- Source ID: bmd-training-resolve-20
- Last verified: 2026-05-31 for high-level workflow context
