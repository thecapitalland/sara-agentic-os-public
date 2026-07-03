# Adoption Guide

This guide explains how to apply Sara Agentic OS to a real project without turning it into a heavy platform.

---

## Step 1 — Decide whether you actually need it

Use Sara if your project has recurring AI-assisted execution with multiple tools, branches, PRs, reviews, or handoffs.

Do not use Sara if the task is simple, one-off, or does not need repeatable control.

---

## Step 2 — Create the minimum project structure

Recommended structure:

```text
docs/
├── state/
│   └── PROJECT_CURRENT_STATE.md
└── workflow/
    ├── packets/
    ├── reviews/
    └── retirements/
AGENTS.md
```

Copy the templates from this repository:

```text
templates/PROJECT_CURRENT_STATE.template.md
templates/WORK_PACKET.template.md
templates/EXECUTION_RESULT.template.md
templates/CHAT_RETIREMENT.template.md
templates/AGENTS.template.md
```

---

## Step 3 — Write Project Instructions

Your Project Instructions should tell ChatGPT or another assistant:

- what the product is
- what the product is not
- what state sources to read first
- what gates are open or closed
- how to judge Cursor/Codex output
- what not to generate without approval

Example startup rule:

```text
Before answering project questions, read Project Instructions and the latest live current-state source first. Do not rely on memory. Do not silently shrink or expand scope. Do not call partial/foundation work done.
```

---

## Step 4 — Keep the current-state file short

The current-state file should answer:

- Where are we now?
- What is approved?
- What is blocked?
- What gates are open?
- What is the next safe action?
- Is a human decision needed?

It should not become a full chat transcript or history dump.

---

## Step 5 — Use packets for execution detail

Do not put large task instructions inside a GitHub issue.

Instead:

1. Create a short issue.
2. Put detailed execution instructions in a packet file.
3. Tell Cursor/Codex to read the packet.
4. Require a result file when done.

---

## Step 6 — Require structured result output

For nontrivial work, the execution agent should write a result file containing:

- summary
- touched files
- validation performed
- what was not done
- risks
- PR link
- next action

This reduces manual copy/paste and avoids long chat logs.

---

## Step 7 — Review with a strict verdict

Use:

```text
Verdict: DONE / PARTIAL / BLOCKED / WRONG DIRECTION
Reason:
Gate:
Risks:
Next action:
Human needed: yes/no
```

Never accept vague statements like:

- "implemented"
- "should work"
- "foundation is ready"
- "tests pass"

without matching them against the acceptance criteria.

---

## Step 8 — Retire long chats

When a chat becomes long, slow, or stale, retire it.

A retirement handoff should include:

- current state
- decisions made
- open gates
- locked product intent
- next safe action
- what not to repeat
- startup prompt for the next chat

Do not keep every historical handoff as active context. Keep one current-state file as the live source.

---

## Step 9 — Add automation slowly

Start manual.

Only add automation after the manual workflow is stable.

Suggested progression:

1. Manual issue + packet
2. Cursor/Codex result file
3. CI validation
4. Label-based review routing
5. Narrow low-risk auto-actions
6. Code auto-merge only with explicit narrow approval

---

## Step 10 — Keep product judgment human-gated

Sara can organize execution, but it should not replace product judgment.

A human should still decide:

- product direction
- acceptance of meaningful work
- code merge gates
- security-sensitive changes
- deployment/staging exposure
- scope changes
- anything irreversible or high-risk
