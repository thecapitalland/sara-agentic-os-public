---
name: mobile-store-release
description: "Prepare mobile store packaging, signing, metadata, rollout and rollback/hold strategy."
---

# mobile-store-release

## Process

1. identify exact release commit/version/build number
2. verify signing and secret boundaries without exposing secrets
3. run release build and required store checks
4. prepare metadata/compliance declarations from approved facts
5. define staged rollout/monitoring/stop criteria
6. record submitted artifact identity and outcome

## Constraints

- submission/production rollout requires explicit authority
- do not fabricate compliance/privacy declarations

## Output

Produce the smallest durable artifact/evidence needed by the active work item. Separate facts, assumptions, findings, risks, and unresolved gates.
