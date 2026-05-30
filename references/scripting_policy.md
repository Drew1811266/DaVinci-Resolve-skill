# Resolve Scripting Policy

Use this before generating DaVinci Resolve Python or Lua automation.

## Generate code only when

- The user wants automation or a repeatable workflow.
- The operation is suitable for scripting rather than visual judgment.
- Required API objects and methods are confirmed by installed Developer documentation, official docs, or user-provided authoritative excerpts.
- Required paths, project names, timeline names, and overwrite permissions are known.

## Do not generate executable code when

- Exact API support is uncertain.
- The task asks for subjective grading, beauty cleanup, creative Fusion design, or audio taste decisions without human review.
- The task deletes media, relinks media, changes project settings, starts broad renders, or overwrites files without explicit confirmation.

## Required script behavior

- Keep configuration variables at the top.
- Include a `DRY_RUN` option for broad or risky tasks.
- Check that Resolve is reachable.
- Check that project manager, current project, media pool, timeline, and render queue objects exist before using them.
- Print each planned change before performing it.
- Preserve source media.
- Avoid overwriting output files unless the user explicitly confirmed it.
- Catch exceptions and return actionable error messages.

## If API support is uncertain

Provide pseudocode and a verification list instead of made-up API calls:

```text
Verify in installed Developer documentation:
- Object that exposes the target feature
- Method for reading current project/timeline
- Method for applying the setting
- Return values and failure behavior
- Version or Studio limitations
```

## Minimal connection example

See `references/scripting/examples/connect_to_resolve.py`. It is a template for environment checking and safe failure, not proof that every downstream workflow is scriptable.
