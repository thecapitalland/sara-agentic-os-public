# Sara Agentic OS — Operating Model v0

## Purpose

Sara Agentic OS is a lightweight operating model for AI-assisted project execution.

Its purpose is to reduce:

- copy/paste between tools
- stale chat context
- tool-hopping
- ambiguous completion claims
- uncontrolled scope drift
- the project owner acting as the human relay between ChatGPT, Cursor, Codex, GitHub, CI, PR review, handoff, and next actions

It is a workflow-control model, not a custom runtime or SaaS platform.

---

## Core entities

### 1. Project Instructions

Project-level rules that every assistant or execution agent must read before giving project advice or doing work.

They should define:

- product intent
- response style
- forbidden behaviors
- state-source rules
- review format
- execution gates

### 2. Live Current-State File

A concise file that represents the live state of the project.

Recommended path:

```text
docs/state/PROJECT_CURRENT_STATE.md
```

It should include:

- current state
- approved envelope
- open gates
- blockers
- latest meaningful changes
- next safe action

It should not become a full history archive.

### 3. Work Packet

A task-specific execution file.

Recommended path:

```text
docs/workflow/packets/<PACKET-NAME>.md
```

It should include:

- Intent Lock
- Approved Envelope
- Forbidden Downgrades
- Acceptance Criteria
- Human Gates
- Validation Required
- Output Required
- Branch/PR Rules
- What Not To Touch
- Stop Conditions

### 4. Execution Result File

A structured output written by Cursor, Codex, or another execution agent.

Recommended path:

```text
docs/workflow/reviews/<PACKET-NAME>-RESULT.md
```

It should include:

- summary
- touched files
- validation performed
- risks
- what was not done
- PR link, if applicable
- follow-up needed

### 5. Review Verdict

The reviewer must not accept vague completion claims.

Use this format:

```text
Verdict: DONE / PARTIAL / BLOCKED / WRONG DIRECTION
Reason:
Gate:
Risks:
Next action:
Human needed: yes/no
```

---

## Approved execution levels

### Level 0 — Issue + packet + manual execution instruction

Approved.

The GitHub issue tracks the lifecycle. The packet contains the execution details. The human or assistant tells Cursor/Codex to read the issue and packet.

### Level 1 — Execution result written back to repo/PR

Approved.

Cursor/Codex writes a short issue/PR comment and, for nontrivial work, a structured result file.

### Level 2 — CI validates but does not merge

Approved.

CI may validate formatting, tests, lint, migrations, docs, or project-specific gates.

Passing CI does not automatically mean the work is done.

### Level 3 — Label-based routing

Approved with loop-safety.

Labels can route status such as:

- `sara:cursor-ready`
- `sara:needs-review`
- `sara:blocked`
- `sara:accepted`

Labels are signals, not proof of completion.

### Level 4 — Guarded low-risk auto-actions

Approved narrowly.

Examples:

- documentation/status updates
- issue labeling
- review routing
- safe housekeeping
- branch cleanup after approved merge

Conditions:

- narrow scope
- reversible where possible
- logged
- loop-safe
- no hidden implementation scope expansion
- no meaningful code auto-merge by default

### Level 5 — Code auto-merge

Not generally approved.

Meaningful code merges should remain human-gated unless explicitly approved for a narrow, low-risk case.

---

## Required issue pattern

Keep issues short. Put detailed instructions in a packet file.

```md
## Source of truth

docs/workflow/packets/<PACKET-NAME>.md

## Execution agent

Cursor or Codex

## Branch

Use branch: <branch-name>

## Rules

- Read Project Instructions first.
- Read `docs/state/PROJECT_CURRENT_STATE.md` first.
- Execute only the approved envelope.
- Do not start the next sprint or packet.
- Commit and push changes to your task branch only.
- Open or update a PR when done.
- Write short result/status in this issue or PR comment.
- For nontrivial work, write structured output to `docs/workflow/reviews/<PACKET-NAME>-RESULT.md`.
- Link the PR here.
```

---

## Anti-patterns

Avoid:

- using chat memory as the source of truth
- long issue bodies that contain full execution instructions
- pasting long AI logs into PR comments
- accepting "done" without validation
- letting green CI override product intent
- starting the next task before the current gate is closed
- silently changing scope because the AI found something interesting
- creating automation before the manual workflow is stable
- auto-merging meaningful code without explicit approval

---

## Default review policy

A task is not done merely because:

- the AI says it is done
- files were changed
- tests passed
- a PR exists
- the UI looks plausible
- a foundation was created

A task is done only when:

- the acceptance criteria are satisfied
- validation evidence exists
- forbidden downgrades were avoided
- human gates are passed where required
- project state is updated when the change is meaningful

---

## Operating principle

Sara should reduce real workflow friction.

If a proposed feature increases coordination burden, creates a new platform to maintain, or turns the human into an even busier relay, it is probably going in the wrong direction.
