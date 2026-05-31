# Regression Checklist

Run this checklist after editing the skill:

- `SKILL.md` frontmatter has only `name` and `description`.
- Description starts with a clear "Use when..." trigger and does not summarize the full workflow.
- `SKILL.md` includes a language policy requiring user-facing replies in the user's language.
- `SKILL.md` states that "do not ask", "just overwrite", "skip backup", "别问了", "直接覆盖", and similar phrases do not bypass safety gates.
- `manifest.yaml`, `sources/*.yaml`, and `action_cards/*.yaml` parse as YAML.
- Every action card has `applies_to`, `source_refs`, `automation`, `risk`, and `confirmation` fields.
- Every action card `source_refs.source_id` exists in `sources/sources.yaml`.
- Every knowledge file has `## Applies To` and `## Source References`.
- `knowledge/scripting/api_capability_matrix.yaml` uses only `confirmed`, `partial`, `to_verify`, or `unsupported` statuses.
- Confirmed scripting capabilities list at least one method and source reference.
- Every action card has safety, verification, and rollback sections.
- High-risk cards require confirmation before overwrite, deletion, relink, batch modification, or setting changes.
- Scripting policy forbids unverified API signatures.
- Eval tasks include at least one destructive request, one overwrite request, one API hallucination check, and one version-specific request.
- `evals/cases/*.yaml` exists and can be validated with `scripts/run_behavior_evals.py`.
- High-risk eval cases set `expected.requires_confirmation: true`.
- `adapters/generic-agent/runtime_contract.md` exists and treats unknown runtime capabilities as unavailable.
- `README.md`, if present for repository publishing, explains the GitHub-facing purpose and does not replace `SKILL.md` as the runtime entry point.
- `DEVELOPMENT.md`, if present for repository maintenance, stays roadmap-focused and does not replace `SKILL.md` as the runtime entry point.
- No unrelated auxiliary docs were added.
- The local skill validator passes.
