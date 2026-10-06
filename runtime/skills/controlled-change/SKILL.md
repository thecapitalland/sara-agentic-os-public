---
name: controlled-change
description: "Apply bounded changes with preflight, ownership, verification and rollback discipline."
---

# controlled-change

## Process

1. confirm exact target and current state
2. identify write scope and protected surfaces
3. create a reversible checkpoint when needed
4. make the smallest coherent change
5. run focused validation
6. record exact result and rollback/recovery path

## Constraints

- no destructive reset/cleanup of unknown work
- no silent scope expansion
- no production/stateful mutation without required gate

## Output

Produce the smallest durable artifact/evidence needed by the active work item. Separate facts, assumptions, findings, risks, and unresolved gates.
