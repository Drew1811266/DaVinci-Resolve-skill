# Create Timeline Workflow

## Purpose

Create timelines from media or user-defined clip lists without damaging existing edits.

## Applies To

- Resolve versions: 20.x, 21.x, user installed version to verify
- Edition: Free and Studio, feature availability to verify
- OS: macOS, Windows, Linux
- Pages: Cut, Edit
- Automation status: Partially scriptable after timeline API confirmation

## Required Inputs

- Target project.
- Clip selection.
- Timeline name.
- Clip order rule.
- Frame rate, if it must differ from defaults.
- Resolution, if required.

## Workflow

1. Confirm active project and media selection.
2. Resolve clip ordering.
3. Check whether a timeline with the target name exists.
4. Confirm frame rate before creation.
5. Create timeline through UI guidance or confirmed scripting API.
6. Set current timeline only if requested.

## Risk Escalators

- Replacing an existing timeline.
- Changing frame rate.
- Batch-editing an existing timeline.

## Verification

- Timeline exists with expected name.
- Clip count, order, duration, frame rate, and resolution match the request.
- Existing timelines remain unchanged unless explicitly confirmed.

## Source References

- Source ID: bmd-product-overview-21
- Source ID: installed-developer-docs-user
- Last verified: 2026-05-31 for high-level workflow
