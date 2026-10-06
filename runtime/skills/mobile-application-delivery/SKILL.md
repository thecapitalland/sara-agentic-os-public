---
name: mobile-application-delivery
description: "Deliver mobile features with lifecycle, offline, permissions, device testing and platform constraints."
---

# mobile-application-delivery

## Process

1. confirm platform(s), app architecture and backend contracts
2. define lifecycle/offline/persistence behavior
3. handle permissions and device capabilities explicitly
4. test representative devices/emulators and failure states
5. coordinate packaging/signing boundaries with release workflow
6. record store/runtime constraints

## Constraints

- do not hide backend contract changes inside client code
- store release remains separately gated

## Output

Produce the smallest durable artifact/evidence needed by the active work item. Separate facts, assumptions, findings, risks, and unresolved gates.
