---
name: workflow-validation
description: "Validate that a workflow behaves according to states, gates, handoffs and failure contracts."
---

# workflow-validation

## Process

1. derive scenarios from allowed/forbidden transitions
2. test happy path and material negative paths
3. verify gate bypass is rejected
4. verify retries/idempotency/overlap behavior
5. check durable artifacts and state reconciliation
6. record evidence per scenario

## Constraints

- labels/status text alone are not proof
- do not test only the final state

## Output

Produce the smallest durable artifact/evidence needed by the active work item. Separate facts, assumptions, findings, risks, and unresolved gates.
