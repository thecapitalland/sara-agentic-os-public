---
name: incident-response
description: "Handle active runtime/production incidents through containment, evidence, recovery and follow-up."
---

# incident-response

## Process

1. establish impact, affected environment and exact timeline
2. preserve evidence and stop unsafe change churn
3. choose the smallest reversible containment
4. validate service recovery separately from root-cause confidence
5. record residual risk and monitoring
6. create follow-up corrective work outside the hot path

## Constraints

- do not hide failed attempts
- avoid destructive cleanup before evidence capture
- production actions remain within explicit incident authority

## Output

Produce the smallest durable artifact/evidence needed by the active work item. Separate facts, assumptions, findings, risks, and unresolved gates.
