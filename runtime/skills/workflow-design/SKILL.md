---
name: workflow-design
description: "Design a testable workflow from an approved objective."
---

# workflow-design

## Process

1. define start/end states and invariants
2. enumerate transitions and owners
3. define durable handoff artifacts
4. design failure/retry/rollback paths
5. identify safe concurrency and serialization points
6. translate states into acceptance tests and observability

## Constraints

- keep state machine smaller than the problem allows
- avoid duplicate sources of truth

## Output

Produce the smallest durable artifact/evidence needed by the active work item. Separate facts, assumptions, findings, risks, and unresolved gates.
