# Render Delivery Workflow

## Purpose

Plan exports and render jobs while preventing overwrite, codec, subtitle, and range mistakes.

## Applies To

- Resolve versions: 20.x, 21.x, user installed version to verify
- Edition: Free and Studio, codec availability to verify
- OS: macOS, Windows, Linux
- Page: Deliver
- Automation status: Partially scriptable after render API confirmation

## Required Inputs

- Target timeline.
- Render range: entire timeline or in/out range.
- Format and codec.
- Resolution and frame rate.
- Output directory and filename.
- Audio settings.
- Subtitle mode: burn-in, embedded, sidecar, or none.
- Overwrite policy.

## Workflow

1. Confirm target project and timeline.
2. Collect render settings.
3. Check output path and filename collision.
4. Confirm codec and subtitle behavior against version, OS, and edition.
5. Add render job using UI guidance or confirmed scripting API.
6. Start render only after confirmation when long, batch, or overwrite-prone.

## Risk Escalators

- Overwriting existing output.
- Batch export.
- Starting render immediately.
- Changing project or timeline settings to satisfy delivery.

## Verification

- Render queue job settings match request.
- Output file exists after render.
- Duration, codec, resolution, frame rate, audio, and subtitles match expected values.

## Source References

- Source ID: bmd-product-overview-21
- Source ID: installed-developer-docs-user
- Last verified: 2026-05-31 for high-level workflow
