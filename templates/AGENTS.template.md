# AGENTS.md

This file defines execution rules for AI agents working in this repository.

---

## Required startup

Before doing project work, read:

1. Project Instructions, if available
2. `docs/state/PROJECT_CURRENT_STATE.md`
3. the relevant work packet in `docs/workflow/packets/`
4. this `AGENTS.md`

Do not rely on chat memory as the source of truth.

---

## Scope control

You must:

- execute only the approved envelope
- preserve the Intent Lock
- respect Forbidden Downgrades
- stop if the state file conflicts with the packet
- stop if the task requires secrets, credentials, or unapproved access
- stop if validation cannot be performed and no safe fallback exists

You must not:

- silently shrink scope
- silently expand scope
- call partial/foundation work done
- start the next task
- commit directly to main
- merge your own meaningful code changes
- modify unrelated files

---

## Branch and PR rules

- Work on the branch specified in the packet.
- If no branch is specified, stop and ask for the branch or create a clearly named task branch only if project rules allow it.
- Open or update a PR when work is complete.
- Keep PR comments short.
- Put detailed results in a review file.

---

## Result output

For nontrivial work, write a result file:

```text
docs/workflow/reviews/<PACKET-NAME>-RESULT.md
```

The result must include:

- summary
- touched files
- validation performed
- acceptance criteria status
- risks
- what was not done
- PR link, if applicable
- human gates required

---

## Validation

Run the validation required by the packet.

If validation cannot be run, do not claim DONE. Explain what was not validated and why.

---

## Completion policy

A task is not DONE merely because files changed or tests passed.

A task is DONE only when:

- acceptance criteria are satisfied
- validation evidence exists
- forbidden downgrades were avoided
- human gates are respected
- project state is updated if the change is meaningful

---

## Review verdict expected

The reviewer will judge output using:

```text
Verdict: DONE / PARTIAL / BLOCKED / WRONG DIRECTION
Reason:
Gate:
Risks:
Next action:
Human needed: yes/no
```
