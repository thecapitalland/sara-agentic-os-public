# Sara v2 Candidate — Bounded Execution Orchestration

**Status:** candidate roadmap; no runtime is shipped by this repository.

## Why this direction exists

The current Sara operating model reduces workflow chaos through project state, Issues, work packets, branches, PRs, CI evidence, review verdicts, and explicit human gates.

A remaining problem is that the founder or product owner may still become the human relay between planning, coding agents, reviewers, remediation, CI, and closeout.

Sara v2 explores an optional bounded orchestration layer to reduce that relay work without replacing product judgment, human authority, GitHub evidence, or project-specific safety rules.

## Current baseline

The usable public baseline remains **Operating Model v0**.

It supports:

- Issue and work-packet execution;
- structured Cursor/Codex results;
- CI as evidence;
- label-assisted routing;
- parallel-agent ownership rules;
- strict review and human gates;
- manual and semi-automated operation.

This repository does not currently ship:

- an agent runtime;
- a scheduler or durable queue;
- a background worker;
- a GitHub App that launches coding agents;
- an autonomous code-merging service;
- a production deployment system.

## Candidate maturity path

### O0 — Manual relay

A human moves instructions and results between tools.

### O1 — Artifact handoff

Agents write structured results to GitHub. Review happens from Issues, PRs, diffs, CI, and result artifacts rather than chat copy/paste.

### O2 — Shadow orchestration

A read-only coordinator observes one real workflow and predicts:

- the next safe action;
- stop versus continue;
- reviewer routing;
- whether a human decision is genuinely required.

It does not change repository state.

### O3 — Native single-session orchestration

One root coordinator manages a bounded executor and independent read-only reviewers for one approved Issue.

### O4 — Persistent local runner

A small local runner may add:

- deterministic state transitions;
- worktree isolation;
- retry and timeout limits;
- budget controls;
- resume and crash recovery;
- structured audit events.

### O5 — Independent external review

Implementation and review may use different tools or models through structured, read-only review contracts.

### O6 — Multi-Issue milestone conveyor

A dependency-aware controller may coordinate serial and parallel Issues with explicit file ownership, merge order, integration review, and final human gates.

## Core safety model

### Deterministic controls

Code or explicit workflow rules should own:

- readiness and dependency checks;
- branch and worktree ownership;
- allowed state transitions;
- retries, timeouts, and budgets;
- exact commit and CI identity;
- permission boundaries;
- recovery and audit state.

### AI judgment

AI agents may perform:

- implementation;
- code and architecture review;
- security reasoning;
- intent comparison;
- finding classification;
- ambiguity detection and escalation recommendations.

AI agents should not replace the durable state store, scheduler, lock manager, or permission engine.

## Human boundary

The goal is not to remove the owner or product lead. The goal is to stop using them as the message bus.

A bounded system should normally handle:

- in-scope fixes;
- focused test failures;
- valid review findings;
- routine CI observation;
- documentation and closeout gaps;
- normal model or reviewer routing.

A human decision remains appropriate for:

- scope expansion;
- major product trade-offs;
- security or data authority expansion;
- destructive or production actions;
- final user or product acceptance gates;
- changes to vision and priority.

## Proof-before-runtime rule

The proposed order is:

```text
protocol and safety model
-> read-only shadow observation
-> bounded single-Issue orchestration
-> persistent local runner
-> independent reviewer adapter
-> multi-Issue milestone conveyor
```

A later step should not be activated merely because tools exist. It should require evidence from the preceding step.

## Non-goals

Sara v2 is not a default plan to become:

- a large SaaS platform;
- an unrestricted auto-coding system;
- a dashboard-heavy control center;
- a marketplace;
- an autonomous production deployer;
- a general code auto-merge service;
- a replacement for product judgment.

## Public status

This document describes a candidate direction. It is not a claim that the runtime exists, is production-ready, or is generally available.
