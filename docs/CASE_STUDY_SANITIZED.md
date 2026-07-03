# Sanitized Case Study — AI-Assisted Product Workflow

This is a sanitized example. It does not describe a private project, customer, domain, repository, or business workflow.

---

## Context

A founder is building a software product with help from ChatGPT, Cursor, Codex, GitHub, CI, and pull requests.

The project is moving quickly, but the execution workflow becomes difficult to control.

---

## Symptoms

The founder notices that:

- decisions are spread across several long chats
- Cursor results are copied manually into ChatGPT
- GitHub issues do not contain enough execution context
- PRs exist, but product acceptance remains unclear
- CI passes, but the product owner is not sure the actual intent was satisfied
- partial foundation work is sometimes described as complete
- follow-up tasks start before previous gates are closed
- the founder becomes the routing layer between every tool

---

## Sara-style intervention

The project introduces:

1. **Project Instructions**
   - Define the collaboration rules.
   - Require state-first answers.
   - Ban silent scope changes.

2. **Live Current-State File**
   - One concise source for current state, gates, blockers, and next safe action.

3. **Work Packets**
   - Each task has an Intent Lock, Approved Envelope, Forbidden Downgrades, Acceptance Criteria, Human Gates, and Stop Conditions.

4. **Execution Result Files**
   - Cursor/Codex writes structured results back into the repo.
   - The founder no longer has to paste long tool outputs manually.

5. **Review Verdicts**
   - The assistant returns `DONE`, `PARTIAL`, `BLOCKED`, or `WRONG DIRECTION` with risks and next action.

6. **Chat Retirement**
   - Long chats are retired into compact handoffs and a new startup prompt.

---

## Result

The workflow becomes easier to inspect:

- less manual copy/paste
- clearer gates
- fewer false completion claims
- better continuity between chats
- clearer PR review expectations
- less dependency on memory
- more disciplined use of Cursor/Codex

---

## What this case study does not claim

It does not claim:

- full autonomy
- automatic correctness
- automatic code merge
- replacement of human review
- elimination of product judgment
- a finished SaaS or runtime

The improvement comes from better workflow control, not from magic automation.
