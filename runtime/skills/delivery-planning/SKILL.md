---
name: delivery-planning
description: "Convert approved scope into dependency-ordered, implementation-ready work."
---

# delivery-planning

## Process

1. restate approved outcome, exclusions and unresolved gates
2. decompose by deliverable/dependency rather than job title
3. define objective, write scope, outputs, acceptance evidence and reviewer per task
4. identify safe parallel lanes and shared-state serialization
5. add only necessary architecture/security/release gates
6. define recovery/rollback for stateful or hard-to-reverse changes

## Constraints

- do not invent product requirements, dates or approvals
- prefer small independently reviewable slices
- planning is not permission to execute protected actions

## Output

Produce the smallest durable artifact/evidence needed by the active work item. Separate facts, assumptions, findings, risks, and unresolved gates.
