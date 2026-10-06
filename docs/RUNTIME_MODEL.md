# Runtime Model

## Principle

Represent a capability with the lowest-overhead artifact that preserves quality and authority.

| Need | Artifact |
| --- | --- |
| independent judgment / separate review context | Agent |
| repeatable method/checklist | Skill |
| always-on invariant | Rule |
| external data/action interface | MCP |
| deterministic enforcement | CI/Hook |
| scheduled/event trigger | Automation |
| tone/style only | Persona |

## Public Agent baseline — 12

Core:
- product-lead
- product-design-lead
- software-architect
- frontend-engineer
- backend-integration-engineer
- quality-test-engineer
- independent-code-reviewer

Triggered:
- workflow-architect
- mobile-application-engineer
- security-architect
- appsec-code-auditor
- release-engineer

The Main Agent is the parent coordinator. There is no standing "manager swarm".

## Public Skill baseline — 16

- team-orchestrator
- repo-discovery
- delivery-planning
- incident-response
- prompt-engineering
- workflow-review
- workflow-design
- controlled-change
- workflow-validation
- test-evidence
- api-testing
- test-automation
- tool-evaluation
- mobile-application-delivery
- mobile-store-release
- app-store-optimization

## Routing discipline

1. Simple bounded work -> Main Agent directly.
2. Scope/value uncertainty -> Product Lead.
3. Architecture boundary -> Software Architect.
4. Complex workflow/state machine -> Workflow Architect.
5. Implementation -> relevant engineer.
6. Sensitive trust boundary -> Security Architect; code-level assurance as needed -> AppSec Auditor.
7. Material verification -> Quality Engineer and/or Independent Reviewer.
8. Packaging/deployment/rollback -> Release Engineer.

Do not call every role.

## Tool authority

Visible tools do not imply permission. Each write-capable task must define its write scope and protected actions.

## Runtime portability

The contracts are intentionally model/vendor-neutral. Adapters may translate them to Cursor, Codex, Claude-compatible environments, or future runtimes without changing the canonical responsibility model.
