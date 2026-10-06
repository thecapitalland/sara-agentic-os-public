# Adoption Guide — Unified v1

Sara can be adopted incrementally. Do not install every artifact just because it exists.

## Level A — Governance only

Use this when you already have a capable coding assistant and mainly need durable project state.

Copy into your project:

```text
AGENTS.md
docs/state/PROJECT_CURRENT_STATE.md
docs/state/GATES.md
```

Use Sara templates for objective/work/result artifacts.

Best for:
- small teams;
- founder-led projects;
- mixed ChatGPT/Cursor/Codex workflows;
- projects suffering from stale context or false DONE claims.

## Level B — Governance + Runtime contracts

Add the Agent/Skill baseline when repeated work benefits from explicit independent roles.

Start with only:
- `team-orchestrator`
- `repo-discovery`
- `delivery-planning`
- one or two implementation roles;
- `quality-test-engineer`;
- `independent-code-reviewer`.

Promote security/release/mobile specialists only when triggered by real work.

## Level C — Optional context engine

If repository search/context cost becomes a measured problem, integrate NeuroMesh or another provider through the context contract.

Do not make it mandatory before measuring the baseline.

## Level D — Runtime packaging

Only after the contracts prove useful, use a deterministic client adapter/install process. Keep installation reversible and separate from authoring.

## Minimal project structure

```text
project/
├── AGENTS.md
├── docs/
│   ├── state/
│   │   ├── PROJECT_CURRENT_STATE.md
│   │   └── GATES.md
│   └── work/
│       ├── objective.yaml
│       ├── work-item.yaml
│       └── result.md
└── .cursor/ or client-specific project rules when needed
```

## First task

1. Write the real objective, including non-goals.
2. Decide whether the task is small enough for direct work.
3. For material work, create an Issue/spec and work item.
4. Discover repository reality.
5. Route the smallest sufficient capability set.
6. Execute on an isolated branch.
7. Run focused validation.
8. Use independent review when material/protected.
9. Record the Result.
10. Reconcile project State/Gates.

## Avoid

- copying all 12 Agents into a project when user-level runtime already provides them;
- treating a Skill as a manager Agent;
- creating a project database before GitHub/State files become insufficient;
- enabling automation before the manual lifecycle is reliable;
- turning a context engine into project authority;
- letting a strong model bypass approval/evidence rules.

## Client adapters

See:
- `runtime/adapters/cursor/README.md`
- `runtime/adapters/codex/README.md`

## Validation

From the Sara repository:

```bash
python scripts/validate_baseline.py
```
