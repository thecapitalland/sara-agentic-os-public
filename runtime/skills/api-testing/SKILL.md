---
name: api-testing
description: "Verify API contracts, auth, validation, errors, idempotency and integration behavior."
---

# api-testing

## Process

1. derive cases from contract and risk
2. test success and malformed/unauthorized/forbidden cases
3. verify status/body/schema and side effects
4. test idempotency/concurrency where relevant
5. capture request/response evidence without secrets
6. add regression coverage for confirmed defects

## Constraints

- do not hit production or third-party systems without authorization
- avoid brittle tests tied to irrelevant formatting

## Output

Produce the smallest durable artifact/evidence needed by the active work item. Separate facts, assumptions, findings, risks, and unresolved gates.
