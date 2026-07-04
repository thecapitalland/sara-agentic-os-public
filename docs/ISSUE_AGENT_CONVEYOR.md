# Issue Agent Conveyor

Sara Agentic OS uses an issue-to-agent conveyor to move work from intention to execution without pretending that AI work is magically autonomous.

The conveyor is a lightweight workflow pattern for teams and founders using GitHub Issues, work packets, Cursor/Codex-style coding agents, pull requests, CI, and human review.

It is not a queue service, scheduler, GitHub App, background worker, or autonomous agent runtime.

---

## Why this exists

AI-assisted work often fails because the handoff between tools is informal:

- the issue is too vague
- the prompt is too broad
- the agent starts before scope is approved
- labels are treated as proof of completion
- partial work is called done
- the human owner becomes the router between every tool

The conveyor makes the workflow inspectable.

---

## Core idea

Each meaningful task should move through this path:

```text
idea / product decision
        ↓
GitHub issue
        ↓
work packet
        ↓
agent lane
        ↓
branch + PR
        ↓
result file / PR comment
        ↓
assistant review verdict
        ↓
human gate if required
        ↓
accepted / changes requested / blocked
```

---

## Standard labels

Projects may rename labels, but the meaning should not be weakened.

### Readiness labels

- `sara:not-ready` — planning/discovery only. Do not execute.
- `sara:ready-for-agent` — packet exists and the issue can be picked up.
- `sara:do-not-run` — agents must not execute this issue.

### Agent lane labels

- `agent:cursor-a`
- `agent:cursor-b`
- `agent:cursor-c`
- `agent:codex-a`

Use at most one active execution lane per issue unless a packet explicitly defines safe sub-agent partitioning.

### Status labels

- `status:queued` — ready but not started.
- `status:in-progress` — assigned agent has started.
- `status:done-by-agent` — agent claims work is ready for review.
- `status:review-needed` — assistant/human review is needed.
- `status:changes-requested` — revision is required.
- `status:blocked` — work cannot safely continue.
- `status:accepted` — accepted after review and gates.

### Safety labels

- `sara:parallel-safe` — packet declares file ownership and merge order.
- `sara:sequential-only` — do not run in parallel.
- `sara:human-gate-required` — a named human gate is required before acceptance.

---

## Safe label transition

```text
sara:not-ready
        ↓
packet created and reviewed
        ↓
sara:ready-for-agent + status:queued + one agent lane
        ↓
status:in-progress
        ↓
PR + result file/comment
        ↓
status:done-by-agent + status:review-needed
        ↓
assistant review
        ↓
status:changes-requested / status:blocked / status:accepted
```

---

## Forbidden transitions

Do not:

- move from `status:done-by-agent` directly to completed without review
- use a label as proof that the work is correct
- mark an issue ready without a packet
- let an agent claim an issue that is still `sara:not-ready`
- run two agents on shared files without declared ownership or merge order
- let follow-up scope start automatically after one issue finishes

---

## Minimum issue body

```md
## Source of truth

docs/workflow/packets/<PACKET-NAME>.md

## Status

planning / queued / in-progress / review-needed / accepted

## Gate

<gate name or human gate>

## Agent lane

<agent label or sequential-only>

## Rules

- Read the packet and current-state file first.
- Execute only the approved envelope.
- Do not start the next packet.
- Open or update a PR.
- Write a result file or concise result comment.
```

---

## What the agent must output

For nontrivial work, the agent should write a structured result that includes:

- issue number
- branch
- PR link
- touched files
- validation performed
- risks
- what was not done
- acceptance criteria status
- blocker or review request

---

## Review verdict

The reviewer should answer with:

```text
Verdict: DONE / PARTIAL / BLOCKED / WRONG DIRECTION
Reason:
Gate:
Risks:
Next action:
Human needed: yes/no
```

`DONE` means accepted after evidence and gates, not merely that an agent said it was done.
