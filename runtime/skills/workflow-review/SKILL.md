---
name: workflow-review
description: "Review a multi-step workflow for state integrity, ownership, failure recovery and unnecessary complexity."
---

# workflow-review

## Process

1. map states/actors/data/tool boundaries
2. check ambiguous ownership and hidden shared writes
3. inspect retries, idempotency, timeouts and compensation
4. identify human relay points and removable ceremony
5. compare against a simpler sequential/manual baseline
6. return findings and the smallest safe simplification

## Constraints

- do not recommend orchestration infrastructure without a measured need
- distinguish process problems from tool problems

## Output

Produce the smallest durable artifact/evidence needed by the active work item. Separate facts, assumptions, findings, risks, and unresolved gates.
