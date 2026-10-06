---
name: repo-discovery
description: "Establish repository reality before planning or editing."
---

# repo-discovery

## Process

1. identify root, branch, remote, status, active instructions and current work object
2. map relevant languages, packages, entry points and tests
3. locate project State/Gates/ADRs/config relevant to the task
4. search task symbols and dependencies before broad reading
5. separate observed facts from inferred architecture
6. produce a minimal repository map and open questions

## Constraints

- read before edit
- do not treat generated/cache/vendor directories as primary architecture
- do not infer missing business intent from code

## Output

Produce the smallest durable artifact/evidence needed by the active work item. Separate facts, assumptions, findings, risks, and unresolved gates.
