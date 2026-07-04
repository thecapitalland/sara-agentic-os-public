# Operational Lessons

Sara Agentic OS was shaped by practical friction in AI-assisted project work.

This document captures reusable lessons without exposing private project details.

---

## 1. Chat memory is not a source of truth

Long chats become stale, slow, and hard to verify.

A project needs a live state file that says:

- where the project is now
- what is approved
- what is blocked
- what gates are open
- what the next safe action is
- whether a human decision is needed

---

## 2. `Done` is not accepted

An AI assistant or coding agent may say something is done.

That is a claim, not an acceptance decision.

Acceptance requires evidence:

- issue and packet match
- touched files are within scope
- validation was performed
- result file or PR comment exists
- review verdict is explicit
- human gate is passed when required

---

## 3. Issues should stay short

A GitHub issue should not become a giant prompt or chat transcript.

The issue should point to a work packet.

The packet carries the execution detail.

---

## 4. Work packets reduce prompt drift

A work packet should define:

- intent lock
- approved envelope
- forbidden downgrades
- acceptance criteria
- human gates
- validation required
- output required
- branch and PR rules
- what not to touch
- stop conditions

This makes it harder for the agent to silently expand or shrink scope.

---

## 5. Docs-only work can move faster

Docs/process changes are different from product code changes.

A docs-only fast lane is reasonable when the change is:

- narrow
- reversible
- not changing runtime behavior
- not changing data
- not granting a hidden high-risk capability

This does not mean code auto-merge is safe by default.

---

## 6. Data incidents require read-only verification first

When data appears missing or inconsistent, the first response should not be a fix.

The first response should be:

1. stop new writes
2. identify environment
3. identify the data source
4. compare app-facing and shell-facing state
5. preserve commands and logs
6. verify read-only before changing anything

---

## 7. Tool failures need playbooks

Git, SSH, Drive mirrors, chat connectors, CI, and staging environments can fail in different ways.

A good workflow does not assume every tool is always healthy.

It records:

- what tool failed
- what evidence exists
- what source is authoritative
- what fallback is allowed
- what must be reconciled later

---

## 8. Local fallback is allowed only when traceable

GitHub should remain the live source of truth.

A local working copy can be used as a fallback only when the branch, commit, status, and diff are known.

Any local-only fallback should be reconciled back to GitHub when connectivity returns.

---

## 9. Parallel agents are not free speed

Multiple agents can move faster only when the work is partitioned.

Without ownership, stop conditions, and merge order, parallel agents create rework.

---

## 10. The human owner should not become the router

The workflow should reduce the need for the founder or product owner to paste long outputs between tools.

Execution agents should write results back to durable artifacts.

Review should happen from GitHub evidence, not from manually copied chat fragments.

---

## What Sara is trying to improve

Sara does not make AI output automatically correct.

Sara improves the workflow around AI-assisted execution so that work is easier to inspect, review, recover, and continue.
