# Operating Model v1

## Unit of material work

Material, mutating, cross-session, or cross-tool work uses:

```text
Objective -> Issue/spec -> isolated execution -> PR -> evidence/review -> Result -> reconciliation
```

Read-only questions and tiny local edits do not need synthetic ceremony.

## Phase 0 — Discovery

Challenge the premise. Decide whether to build, configure, buy, reuse, defer, or stop.

Output only when needed: `templates/OBJECTIVE_CONTRACT.template.yaml`.

## Phase 1 — Authorize

Create the durable work object and acceptance boundary.

Required for material mutation:
- repository/project identity;
- objective;
- scope/non-goals;
- risk/protected domains;
- expected evidence;
- stop conditions;
- human gates.

## Phase 2 — Compose context

Load the minimum useful evidence:
1. global Sara invariants;
2. objective/work object;
3. current project State/Gates;
4. relevant ADRs/rules;
5. repository evidence;
6. selected Skill references;
7. external docs only when needed.

Do not accumulate whole-project chat history.

## Phase 3 — Route capability

Use the Main Agent directly for simple work. Invoke a specialist only when separate judgment/context materially helps.

Examples:
- unresolved value/scope -> Product Lead;
- material system boundary -> Software Architect;
- complex stateful flow -> Workflow Architect;
- auth/trust boundary -> Security Architect;
- material implementation -> relevant engineer;
- verification -> Quality Engineer;
- independent material review -> Independent Reviewer;
- release/deploy -> Release Engineer.

## Phase 4 — Execute bounded work

Every execution lane needs:
- explicit objective;
- allowed write scope;
- forbidden scope;
- validation;
- output contract;
- stop conditions.

Parallelize only isolated surfaces. Shared schema/migration/state/config requires a named owner and merge order.

## Phase 5 — Verify

Prefer deterministic tests first. Add independent judgment where tests cannot prove the requirement.

Security is trigger-based and shift-left; it is not a ceremonial final Agent.

## Phase 6 — Human gates

Human approval is mandatory for protected actions listed in the manifest.

The existence of a credential or write-capable tool is not approval.

## Phase 7 — Result and reconciliation

A material Result records:
- exact commit/PR;
- files/surfaces changed;
- validation;
- findings;
- acceptance status;
- remaining risk;
- what was not done;
- next gate.

Completion requires agreement among applicable Issue/spec, PR, Result, State/Gates, release state, and human acceptance.

## Status vocabulary

Use:
- `READY`
- `ACTIVE`
- `BLOCKED`
- `REVIEW`
- `UAT`
- `RELEASE`
- `DONE`

Never use DONE for a partial or merely agent-claimed result.
