# Glossary

Common terms used in Sara Agentic OS.

---

## Project Instructions

Project-level rules that the assistant or execution agent must read before giving advice or doing work.

They usually define product intent, source-of-truth rules, gates, review format, and forbidden actions.

---

## Current-State File

A concise live file that describes the current project state.

Recommended path:

```text
docs/state/PROJECT_CURRENT_STATE.md
```

It should answer: where are we now, what is approved, what is blocked, what gates are open, and what is the next safe action.

---

## Work Packet

A task-specific execution document.

It should contain enough detail for an execution agent to work without relying on a long chat transcript.

Recommended path:

```text
docs/workflow/packets/<packet-name>.md
```

---

## Intent Lock

The part of a packet that says what the work is trying to preserve.

It protects product direction from being silently changed by implementation details.

---

## Approved Envelope

The exact scope that is allowed for the task.

The agent should not work outside this envelope without a new approval.

---

## Forbidden Downgrade

A change that might appear to simplify implementation but weakens product intent, quality, safety, or user value.

---

## Human Gate

A decision that must be made or accepted by a named human before the work can be considered complete.

Examples: product acceptance, meaningful code merge, deployment exposure, or sensitive logic changes.

---

## Execution Result File

A structured output file written by Cursor, Codex, or another execution agent.

Recommended path:

```text
docs/workflow/reviews/<packet-name>-RESULT.md
```

It should include summary, touched files, validation, risks, what was not done, and PR link if relevant.

---

## Review Verdict

The assistant or reviewer response after inspecting evidence.

Standard format:

```text
Verdict: DONE / PARTIAL / BLOCKED / WRONG DIRECTION
Reason:
Gate:
Risks:
Next action:
Human needed: yes/no
```

---

## Done Claim

A statement from an agent that work is done.

A done claim is not acceptance.

---

## Accepted Work

Work that has passed the packet criteria, validation, review verdict, and any required human gate.

---

## Issue Agent Conveyor

The workflow that moves work from GitHub issue to packet, agent lane, branch, PR, result file, review, and closeout.

---

## Agent Lane

A labeled execution lane assigned to one agent or one branch.

Example labels:

- `agent:cursor-a`
- `agent:cursor-b`
- `agent:codex-a`

---

## Sequential-Only

A safety mode where work should not be split across multiple agents.

Use this when tasks touch shared state, core logic, environment behavior, or human-gated decisions.

---

## Parallel-Safe

A mode where work may be split across lanes because ownership, non-scope, merge order, and stop conditions are clear.

---

## Source of Truth

The authoritative place for current operational state.

For repo/code projects, Sara recommends GitHub as the live source of truth.

---

## Mirror

A secondary copy used for handoff, onboarding, or continuity.

A mirror is not the live execution authority unless explicitly approved as a fallback.

---

## Chat Retirement

A compact handoff created when a long chat becomes slow, stale, or hard to continue.

Retirement files help continuity but should not replace the current-state file.
