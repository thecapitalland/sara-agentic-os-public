# Work Packet — <PACKET NAME>

Packet ID:
Date:
Owner:
Execution agent:
Target branch:
Related issue:
Related PR:

---

## 1. Intent Lock

What is the real product/workflow intent behind this task?

- 

This intent must not be silently changed.

---

## 2. Approved Envelope

The execution agent is approved to do only the following:

- 
- 
- 

---

## 3. Forbidden Downgrades

The execution agent must not:

- silently reduce scope
- replace product intent with a weaker technical shortcut
- call foundation/partial work done
- change unrelated files
- start the next task
- alter auth/security/deployment/data models unless explicitly allowed

Project-specific forbidden downgrades:

- 
- 

---

## 4. Acceptance Criteria

The task is acceptable only if all criteria are met:

- [ ] 
- [ ] 
- [ ] 

---

## 5. Human Gates

The following require explicit human approval:

- [ ] Merge to main
- [ ] Production/staging deployment
- [ ] Auth/security changes
- [ ] Data migration/destructive operation
- [ ] Product scope change
- [ ] Other:

---

## 6. Validation Required

The execution agent must run or provide evidence for:

- [ ] Tests:
- [ ] Lint/typecheck:
- [ ] Build:
- [ ] Migration check:
- [ ] Manual verification:
- [ ] Screenshot/UAT evidence, if UI:

If validation cannot be run, explain why.

---

## 7. Output Required

The execution agent must provide:

- short issue/PR status comment
- list of touched files
- validation evidence
- known risks
- what was not done
- PR link, if applicable
- result file at:

```text
docs/workflow/reviews/<PACKET-NAME>-RESULT.md
```

---

## 8. Branch / PR Rules

- Work on branch:

```text
<branch-name>
```

- Do not commit directly to main.
- Open or update a PR when done.
- Keep PR description concise.
- Link this packet in the PR.
- Do not merge without the required human gate.

---

## 9. What Not To Touch

The execution agent must not modify:

- 
- 
- 

---

## 10. Stop Conditions

Stop and report BLOCKED if:

- required source files are missing
- project state conflicts with this packet
- acceptance criteria are impossible without scope change
- secrets/credentials are required
- write permissions are unavailable
- validation cannot be performed and no safe fallback exists
- the task requires a forbidden downgrade

---

## 11. Notes

Additional context:

- 
