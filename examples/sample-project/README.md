# Sample Project Walkthrough

This folder shows a minimal Sara-style workflow for a fictional project.

It is intentionally small and sanitized.

---

## Files

```text
examples/sample-project/
├── README.md
├── AGENTS.md
└── docs/
    ├── state/
    │   └── PROJECT_CURRENT_STATE.md
    └── workflow/
        ├── packets/
        │   └── sample-work-packet.md
        └── reviews/
            └── sample-result.md
```

---

## Flow

1. The current-state file defines where the project is now.
2. The work packet defines the task envelope.
3. The execution agent reads the packet and works only inside scope.
4. The agent writes a result file.
5. The reviewer returns a verdict.

---

## What this example demonstrates

- state-first workflow
- issue/packet separation
- explicit non-scope
- structured execution result
- review verdict discipline

It does not demonstrate automation, deployment, or code auto-merge.
