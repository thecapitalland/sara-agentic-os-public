# Adoption Guide

## Level 1 — Governance only
Start with Project Current State, Gates, Objective Contract, Work Item, and Execution Result.

## Level 2 — Runtime contracts
Add only Agent and Skill contracts that repeatedly improve execution. A practical start is orchestration, repository discovery, planning, one implementation Agent, quality, and independent review.

## Level 3 — Context optimization
If repository context becomes a measured bottleneck, plug a provider into the generic context contract. Keep it optional until quality, latency, or context cost justifies it.

## Level 4 — Deterministic packaging
Only after the contracts prove useful: render/install from the canonical manifest, dry-run first, inventory before/after, preserve rollback, and verify the runtime actually loads the artifacts.

## Minimal structure
```text
project/
├── AGENTS.md
└── docs/
    ├── state/
    │   ├── PROJECT_CURRENT_STATE.md
    │   └── GATES.md
    └── work/
        ├── objective.yaml
        ├── work-item.yaml
        └── RESULT.md
```

Avoid invoking the whole roster, duplicating global contracts, adding infrastructure before need, enabling automation before the manual lifecycle is reliable, or allowing stronger reasoning to bypass approval/evidence.
