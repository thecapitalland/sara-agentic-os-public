# Runtime Model

Use the lowest-overhead representation that preserves required capability and assurance.

| Need | Representation |
|---|---|
| independent judgment or separate review context | Agent |
| repeatable procedure | Skill |
| always-on invariant | Rule |
| external data/action boundary | Interface Adapter |
| deterministic enforcement | Validation |
| trigger | Automation |
| communication style | Persona |

A job title does not automatically become an Agent.

## Main Coordinator
Handles simple work directly, loads only relevant context, invokes only needed specialists, preserves boundaries, and never treats the roster as a virtual meeting.

## Routing
- simple bounded task → direct execution;
- unresolved value/scope → product judgment;
- material system boundary → architecture judgment;
- complex stateful flow → workflow architecture;
- implementation → relevant engineering capability;
- sensitive trust boundary → security architecture;
- code-level sensitive review → application security audit;
- material verification → quality and/or independent review;
- packaging, rollout, recovery → release capability.

Tool visibility never implies authorization.

Runtime contracts are model-neutral and client-neutral. A client-specific representation is an adapter, not a second source of truth.
