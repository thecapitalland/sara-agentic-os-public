---
name: test-automation
description: "Automate stable, high-value regression checks without turning every behavior into a brittle test."
---

# test-automation

## Process

1. select repeated/high-risk behavior worth automation
2. choose the lowest stable test layer
3. make fixtures deterministic and isolated
4. avoid external dependencies when a local substitute proves the contract
5. integrate with CI without mutation authority
6. track flakiness as a defect

## Constraints

- do not automate unstable requirements
- do not use retries to hide deterministic failures

## Output

Produce the smallest durable artifact/evidence needed by the active work item. Separate facts, assumptions, findings, risks, and unresolved gates.
