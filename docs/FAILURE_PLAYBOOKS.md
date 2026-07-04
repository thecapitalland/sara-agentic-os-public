# Failure Playbooks

Sara Agentic OS assumes tools can fail.

The goal is not to avoid every failure. The goal is to recover without losing state, hiding risk, or forcing the human owner to rebuild context manually.

---

## First 10 minutes recovery protocol

When something looks broken:

1. Stop new writes.
2. Identify the repository and environment.
3. Identify the last known good state or commit.
4. Read the current-state file.
5. Preserve commands, logs, screenshots, and exact error text.
6. Verify with read-only checks first.
7. Separate verified facts from assumptions.
8. Report the suspected issue, verified facts, unknowns, next safe action, and whether a human is needed.

---

## Incident severity levels

| Level | Meaning | Example | Response |
|---|---|---|---|
| P0 | Possible data loss or destructive environment damage | data appears missing, wrong target, unexpected destructive command | stop writes, read-only verification, incident note |
| P1 | Deploy or environment path broken | app down, deploy key failure, service restart failure | stop deploy, collect evidence, use fallback only with traceability |
| P2 | Source-of-truth conflict | GitHub and mirror disagree, wrong branch, stale handoff | GitHub controls; report sync gap |
| P3 | Low-risk docs/process issue | typo, stale wording, small docs clarification | use safe default and docs fast lane |

---

## Git failure playbook

### Symptoms

- wrong branch
- wrong remote
- stale local branch
- pull request from the wrong source
- changed files outside the approved envelope
- CI passes but the wrong files changed

### Recovery

1. Stop new work on the branch.
2. Record repo, branch, base, head SHA, and PR number.
3. List changed files.
4. Compare changed files to the packet.
5. If out of scope, mark the work `PARTIAL` or `WRONG DIRECTION`.
6. If the branch is contaminated, close it and create a clean branch.

---

## SSH / deploy-key failure playbook

### Symptoms

- `Permission denied (publickey)`
- server cannot fetch from GitHub
- key exists but is not selected
- test works as one user but fails as the deploy user

### Recovery

1. Test as the actual deploy user.
2. Record host, repo path, remote URL, key path, and exact error.
3. Test with explicit key selection when appropriate.
4. Do not deploy from GitHub until fetch or pull is deterministic.
5. If local fallback is used, record the branch, commit, status, diff, target, and reason.

---

## Local fallback playbook

GitHub should remain the live source of truth, but local fallback can be useful when server access to GitHub is temporarily broken.

Before using local state, record:

```text
repo path:
branch:
HEAD SHA:
git status --short:
git remote -v:
diff summary if uncommitted changes exist:
reason normal GitHub path cannot be used:
rollback path:
```

After fallback, reconcile the local state back to GitHub.

---

## Mirror / Drive failure playbook

A secondary mirror is useful for handoff and onboarding, but it should not override the repository source of truth.

If the mirror and GitHub disagree:

1. Use GitHub for operational decisions.
2. Mark the mirror stale.
3. Correct the mirror later.
4. Do not execute from mirror-only context unless explicitly approved.

---

## Chat connector failure playbook

Collaboration tools are context surfaces, not execution authority.

If a decision exists only in Slack, chat, or another connector:

1. Extract the decision.
2. Convert it into a GitHub issue, packet, state update, or review note.
3. Do not let the connector become the only source of execution scope.

---

## Data-state incident playbook

When data appears missing or inconsistent:

1. Stop.
2. Do not run destructive fixes.
3. Identify environment and data source.
4. Verify row counts or state read-only.
5. Compare app-facing and shell-facing configuration.
6. Preserve exact commands and logs.
7. Only restore or mutate data after source, target, backup, and rollback path are explicit.

---

## Post-incident note

Every meaningful incident should produce a short note:

```text
What appeared wrong:
Verified root cause:
Data impact:
Commands run:
What was not done:
Next prevention rule:
Human needed:
```
