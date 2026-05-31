# Behavior Eval Runbook

## Purpose

Use machine-readable eval cases to check whether an agent response respects safety gates, version checks, language policy, and API hallucination limits.

## Case Format

Cases live in `evals/cases/*.yaml`. Each case includes:

- `id`
- `input`
- `risk_level`
- `expected.must_include`
- `expected.must_not_include`
- `expected.requires_confirmation`
- `expected.requires_version_check`
- `expected.forbidden_api_claims`
- `expected.required_execution_modes`

## Running Structural Checks

```bash
python3 scripts/run_behavior_evals.py
```

## Evaluating Responses

Provide a YAML or JSON mapping from case id to agent response:

```yaml
dangerous_delete: "..."
render_overwrite: "..."
```

Then run:

```bash
python3 scripts/run_behavior_evals.py --responses path/to/responses.yaml
```
