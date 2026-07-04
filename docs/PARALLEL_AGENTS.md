# Parallel Agents Guide

Sara Agentic OS supports parallel AI-assisted execution only when the work is clearly partitioned.

This guide is for people using more than one Cursor/Codex-style assistant, branch, or pull request at the same time.

Parallel work can help, but unmanaged parallel agents create rework, merge conflicts, scope drift, and false completion claims.

---

## Core rule

Use parallel agents only when each lane has:

- one issue
- one work packet
- one branch
- one pull request
- declared ownership
- declared non-scope
- a result file or concise result comment
- an overlap stop condition

If this cannot be declared, run sequentially.

---

## Good use cases

Parallel work may be appropriate when tasks are independent, such as:

- two separate documentation pages
- isolated copy review and separate test planning
- two independent UI surfaces
- separate examples that do not share state files

---

## Sequential-only cases

Prefer sequential work when a task touches:

- shared project state
- product intent
- core formulas or business logic
- deployment or environment behavior
- shared templates or routes
- the same page or service as another task
- anything that requires a human gate

---

## Packet requirements

Each parallel packet should declare:

```text
Agent lane:
Branch:
Owned files or areas:
Forbidden files or areas:
Merge order:
Expected pull request:
Validation required:
Output required:
Stop condition:
```

---

## Merge order

Parallel work does not mean random merge order.

A packet should say whether the PR is:

- independent
- first in merge order
- second after another PR
- blocked until another PR lands

If a PR changes a shared surface, later PRs should refresh before review.

---

## Overlap stop condition

If an agent discovers it needs to touch another lane's owned area, it must stop and report:

```text
BLOCKED: parallel overlap
Issue:
Agent lane:
Owned area requested:
Reason:
Suggested next step:
```

---

## Result requirements

Each agent result should include:

- issue number
- lane label
- branch
- PR link
- touched files
- validation performed
- overlap check result
- risks
- what was not done
- reviewer request

---

## Labels are not proof

Labels are workflow signals, not correctness proof.

- `status:done-by-agent` means the agent claims work is ready for review.
- `status:review-needed` means a reviewer should inspect evidence.
- `status:accepted` should only be used after review and any required human gate.

---

## Practical warning

The goal is not to maximize the number of agents.

The goal is to reduce uncontrolled rework.

Start sequential. Add parallel lanes only when ownership, acceptance criteria, and review order are clear.
