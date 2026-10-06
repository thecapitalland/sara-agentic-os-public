# Architecture

Sara v2 separates authority, context, execution, and assurance into four planes.

## Governance & Delivery
Owns what work is authorized and where it is in its lifecycle.

```text
Intent -> Objective -> Work Item -> State/Gates -> Change -> Result -> Reconciled completion
```

## Context & Cognition
Owns what evidence should be brought into the current reasoning task: repository discovery, task-conditioned evidence, uncertainty, memory boundaries, Experience/Outcome records, and learning candidates.

Context never creates authority.

## Runtime & Capability
Owns how authorized work is routed to the smallest sufficient capability set: Main Coordinator, specialist Agents, reusable Skills, and action/write boundaries.

It does not own project State or product intent.

## Evidence & Assurance
Owns proof: deterministic validation, independent review, exact candidate identity, acceptance evidence, rollback, recovery, and residual-risk reporting.

## Control flow

```mermaid
sequenceDiagram
    participant O as Owner
    participant G as Governance
    participant C as Context
    participant R as Runtime
    participant A as Assurance

    O->>G: intent / outcome
    G->>G: objective + work boundary
    G->>C: request relevant evidence
    C-->>R: bounded task context
    G->>R: authority + gates
    R->>R: execute smallest sufficient capability set
    R->>A: candidate + evidence
    A-->>G: validation / review result
    G-->>O: accepted result or real decision gate
```

If two documents appear to own the same policy, the manifest and document registry decide.
