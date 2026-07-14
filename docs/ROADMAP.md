# Roadmap

Sara Agentic OS is currently an operating model, not a shipped runtime platform.

This roadmap is intentionally conservative. It separates the usable public baseline from candidate orchestration work and does not overstate automation.

---

## Current status — Operating Model v0

Available now:

- core README and positioning
- Operating Model v0
- Adoption Guide
- sanitized case study
- project-state template
- work-packet template
- execution-result template
- chat-retirement template
- optional AGENTS template
- issue-to-agent conveyor guide
- parallel agents guide
- operational lessons
- failure playbooks
- presentation narrative

Operating Model v0 remains the current usable baseline even while Sara v2 is explored.

---

## v0.1 — Public documentation hardening

Goals:

- improve examples
- add clearer template instructions
- add a sample project walkthrough
- add more adoption/help issue templates
- improve glossary and terminology
- make the public README easier to scan
- collect external feedback

---

## v0.2 — Evidence and review patterns

Goals:

- improve review verdict examples
- add sample PR review workflows
- add examples of `PARTIAL`, `BLOCKED`, and `WRONG DIRECTION`
- define safer docs/status fast-lane examples
- document common anti-patterns from public feedback

---

## v0.3 — Optional helper checks

Possible additions:

- lightweight checklists for packet completeness
- GitHub Issue template improvements
- documentation-only validation examples
- optional CI checks for docs structure

These should remain optional and should not become a hidden runtime or automation platform.

---

## Sara v2 candidate — Bounded execution orchestration

Sara v2 is a candidate architecture direction, not a released runtime.

The objective is to reduce the founder or product owner's role as the human relay between planning, execution agents, independent review, remediation, CI, merge, reconciliation, and closeout.

Read the public candidate overview:

- [Sara v2 Candidate — Bounded Execution Orchestration](SARA_V2_BOUNDED_ORCHESTRATION.md)

### Candidate maturity path

1. **O0 — Manual relay**
2. **O1 — GitHub artifact handoff**
3. **O2 — Read-only shadow orchestration**
4. **O3 — Bounded native single-session orchestration**
5. **O4 — Persistent local runner**
6. **O5 — Independent external review adapter**
7. **O6 — Multi-Issue milestone conveyor**

### Required order

```text
protocol and safety model
-> shadow evidence
-> single-Issue pilot
-> persistent local runner
-> independent reviewer adapter
-> milestone conveyor
```

A later level must not be activated simply because tools are available. It requires evidence from the preceding level.

### Candidate principles

Any future bounded orchestration should be:

- optional;
- local-first initially;
- GitHub-backed;
- least-privilege;
- explicit about project overlays and human gates;
- deterministic for state, locks, retries, budgets, timeouts, and permissions;
- auditable and recoverable;
- unable to expand scope on its own;
- unable to let an implementing agent approve its own work.

### Not shipped today

The public repository does not currently ship:

- a persistent agent runtime;
- a scheduler or durable queue;
- a background Issue-claiming worker;
- a GitHub App that launches coding agents;
- a multi-vendor orchestration service;
- autonomous code merge or production deployment.

---

## Narrow automation experiments

Potential future experiments inside the v0 or early-v2 boundary:

- helper scripts for local validation
- optional GitHub Actions that check packet fields
- label consistency checks
- docs-only housekeeping checks
- branch cleanup after accepted merge
- read-only shadow evaluation of routing and stop/continue decisions

Any automation should be:

- narrow
- reversible where possible
- logged
- loop-safe
- not a replacement for review
- not a general code auto-merge path

---

## Not on the roadmap by default

Sara does not currently aim to become:

- a large SaaS platform
- an unrestricted auto-coding system
- a dashboard-heavy tool
- a marketplace
- a blockchain system
- an autonomous production deployment system
- a general code auto-merging service

These would require separate design, safety review, evidence, and explicit approval.

---

## Public readiness checklist

Before actively promoting Sara beyond a quiet public repo, the project should have:

- clear README
- complete adoption guide
- sanitized case study
- Issue conveyor guide
- failure playbooks
- glossary
- sample project walkthrough
- contribution guidelines
- no private project details
- no exaggerated automation claims
- a clear invitation for feedback and collaborators
- clear separation between shipped baseline and candidate roadmap
