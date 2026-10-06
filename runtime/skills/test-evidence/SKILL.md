---
name: test-evidence
description: "Capture verification evidence so another reviewer can reproduce or audit the claim."
---

# test-evidence

## Process

1. record exact commit/build/environment
2. record command or test method
3. capture concise result and relevant artifacts
4. separate pass/fail/blocked/skipped
5. link evidence to acceptance criteria
6. preserve known failures and limitations

## Constraints

- do not paste secrets or huge raw logs
- do not convert skipped/unavailable checks into PASS

## Output

Produce the smallest durable artifact/evidence needed by the active work item. Separate facts, assumptions, findings, risks, and unresolved gates.
