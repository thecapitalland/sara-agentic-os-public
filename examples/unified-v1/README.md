# Unified v1 Sample Project

This sample shows the smallest durable Sara setup for a real repository task.

## Files

- `AGENTS.md` — local bootstrap.
- `docs/state/PROJECT_CURRENT_STATE.md` — current truth.
- `docs/state/GATES.md` — protected/open gates.
- `docs/work/objective.yaml` — why the work exists.
- `docs/work/work-item.yaml` — authorized execution envelope.
- `docs/work/RESULT.md` — final evidence and next state.

## Example flow

```text
objective
 -> Issue/spec
 -> work-item
 -> task branch
 -> implementation + focused tests
 -> independent review if material
 -> RESULT
 -> State/Gates update
```

The sample intentionally does not require all Sara Agents or NeuroMesh. Add them only if the project needs them.
