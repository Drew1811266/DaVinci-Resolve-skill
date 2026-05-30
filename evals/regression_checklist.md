# Regression Checklist

Run this checklist after editing the skill:

- `SKILL.md` frontmatter has only `name` and `description`.
- Description starts with a clear "Use when..." trigger and does not summarize the full workflow.
- `manifest.yaml`, `sources/*.yaml`, and `action_cards/*.yaml` parse as YAML.
- Every action card has safety, verification, and rollback sections.
- High-risk cards require confirmation before overwrite, deletion, relink, batch modification, or setting changes.
- Scripting policy forbids unverified API signatures.
- Eval tasks include at least one destructive request, one overwrite request, one API hallucination check, and one version-specific request.
- `README.md`, if present for repository publishing, explains the GitHub-facing purpose and does not replace `SKILL.md` as the runtime entry point.
- No unrelated auxiliary docs were added.
- The local skill validator passes.
