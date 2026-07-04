# Sara Agentic OS

**A practical operating model for AI-assisted project execution.**

Sara Agentic OS is not a custom agent runtime, SaaS product, dashboard, marketplace, blockchain system, or auto-coding bot.

It is a lightweight governance and workflow-control model for people who work across tools like ChatGPT, Cursor, Codex, GitHub, CI, pull requests, project handoffs, and review loops — and do not want to become the human relay between them.

> Current status: **Operating Model v0** — practical, experimental, template-based, and intentionally lightweight.

---

## The problem

AI-assisted development can move fast, but the workflow often becomes messy:

- important decisions are buried in long chats
- Cursor/Codex results are pasted manually between tools
- GitHub issues, PRs, CI, and chat context drift apart
- partial work gets called "done"
- prompts silently expand or shrink scope
- the founder/product owner becomes the routing layer between all tools

Sara exists to reduce that friction.

---

## What Sara is

Sara Agentic OS is an operating model for controlling AI-assisted project work through:

- live project state files
- project instructions
- work packets
- explicit intent locks
- approved execution envelopes
- forbidden downgrades
- human gates
- structured Cursor/Codex result files
- GitHub issue / branch / PR discipline
- issue-to-agent conveyor rules
- assistant review verdicts
- chat retirement and handoff protocols
- optional repository-level instruction templates for AI-assisted tools

The goal is not to make AI "fully autonomous". The goal is to make AI-assisted execution **less chaotic, less stale, less manual, and easier to verify**.

---

## What Sara is not

Sara is not:

- a SaaS platform
- a custom agent runtime
- a GitHub App
- a dashboard-heavy product
- a queue/service worker
- an autonomous code merger
- a blockchain/smart-contract system
- a set of shipped agents
- a replacement for product judgment
- a guarantee that AI output is correct

Meaningful product and code decisions should still pass through explicit human gates.

---

## Core workflow

```text
Product intent / owner decision
        ↓
Project Instructions + Live Current State
        ↓
GitHub Issue + Work Packet
        ↓
Cursor / Codex task branch
        ↓
Pull Request + Result Review File
        ↓
Assistant verdict
        ↓
Human gate
        ↓
Merge / closeout / state update
```

---

## Approved levels

| Level | Name | Status | Notes |
|---|---|---:|---|
| 0 | Issue + packet + manual Cursor/Codex instruction | Approved | Safe baseline |
| 1 | Cursor/Codex writes structured result back to repo/PR | Approved | Reduces manual copy/paste |
| 2 | CI validates but does not merge | Approved | Green CI is evidence, not final proof |
| 3 | Label-based review routing | Approved with loop-safety | Labels are signals, not completion proof |
| 4 | Guarded low-risk auto-actions | Approved narrowly | Docs/status/labels/housekeeping only |
| 5 | Code auto-merge | Not generally approved | Requires explicit narrow approval |

---

## Start here

- [Operating Model v0](docs/OPERATING_MODEL_V0.md)
- [Adoption Guide](docs/ADOPTION_GUIDE.md)
- [Issue Agent Conveyor](docs/ISSUE_AGENT_CONVEYOR.md)
- [Parallel Agents Guide](docs/PARALLEL_AGENTS.md)
- [Failure Playbooks](docs/FAILURE_PLAYBOOKS.md)
- [Operational Lessons](docs/OPERATIONAL_LESSONS.md)
- [Glossary](docs/GLOSSARY.md)
- [Roadmap](docs/ROADMAP.md)
- [Presentation Narrative](docs/PRESENTATION.md)
- [Collaboration Invitation](docs/COLLABORATION.md)
- [Sanitized Case Study](docs/CASE_STUDY_SANITIZED.md)
- [Sample Project Walkthrough](examples/sample-project/README.md)

---

## Repository structure

```text
.
├── README.md
├── CONTRIBUTING.md
├── LICENSE.md
├── SECURITY.md
├── docs/
│   ├── OPERATING_MODEL_V0.md
│   ├── ADOPTION_GUIDE.md
│   ├── ISSUE_AGENT_CONVEYOR.md
│   ├── PARALLEL_AGENTS.md
│   ├── FAILURE_PLAYBOOKS.md
│   ├── OPERATIONAL_LESSONS.md
│   ├── GLOSSARY.md
│   ├── ROADMAP.md
│   ├── PRESENTATION.md
│   ├── COLLABORATION.md
│   └── CASE_STUDY_SANITIZED.md
├── examples/
│   └── sample-project/
├── templates/
│   ├── PROJECT_CURRENT_STATE.template.md
│   ├── WORK_PACKET.template.md
│   ├── EXECUTION_RESULT.template.md
│   ├── CHAT_RETIREMENT.template.md
│   └── AGENTS.template.md        # optional instruction template, not shipped agents
└── .github/
    ├── pull_request_template.md
    └── ISSUE_TEMPLATE/
        ├── question.yml
        ├── improvement.yml
        └── adoption-help.yml
```

---

## Quick start

1. Copy `templates/PROJECT_CURRENT_STATE.template.md` into your project as:

   ```text
   docs/state/PROJECT_CURRENT_STATE.md
   ```

2. Optional: if you use Cursor, Codex, or similar AI-assisted execution tools, copy `templates/AGENTS.template.md` into your repo as:

   ```text
   AGENTS.md
   ```

   This file is only an instruction template. It does not create agents, run agents, or add automation.

3. Before each task, create a work packet from:

   ```text
   templates/WORK_PACKET.template.md
   ```

4. Ask Cursor/Codex to read:

   - Project Instructions
   - `docs/state/PROJECT_CURRENT_STATE.md`
   - the relevant work packet
   - `AGENTS.md`, if your project uses it

5. Require Cursor/Codex to write a structured result using:

   ```text
   templates/EXECUTION_RESULT.template.md
   ```

6. Review the result with a strict verdict:

   ```text
   Verdict: DONE / PARTIAL / BLOCKED / WRONG DIRECTION
   Reason:
   Gate:
   Risks:
   Next action:
   Human needed: yes/no
   ```

---

## Design principles

- Do not rely on chat memory as the source of truth.
- Do not silently shrink or expand scope.
- Do not call partial/foundation work done.
- Separate product intent from execution prompts.
- Keep issues short; put execution details in packet files.
- Keep current-state files concise and current, not historical archives.
- Use CI as evidence, not as final product acceptance.
- Keep meaningful code merges human-gated unless narrowly approved.
- When friction appears, diagnose the workflow problem before writing another prompt.

---

## Who this is for

Sara may help you if you are:

- a founder using AI coding tools across multiple projects
- a product owner trying to keep AI execution aligned with intent
- a developer using ChatGPT/Cursor/Codex/GitHub together
- a small team that needs lightweight execution governance without building a full platform
- someone tired of manually copying long AI outputs between tools

Sara is probably overkill if your project is small, single-session, or does not need repeatable execution control.

---

## Collaboration

Sara is early and practical.

Useful help can come from many directions:

- workflow critique
- AI-assisted development experience
- GitHub/Cursor/Codex patterns
- issue and PR review discipline
- examples and templates
- case studies that can be shared safely
- technical writing
- product judgment
- community feedback

Read [Collaboration Invitation](docs/COLLABORATION.md) for suggested ways to help.

---

## Questions and help

If you have a question, open a GitHub Issue using the **Question / Adoption Help** template.

If you want help applying this model to a real project workflow, use the **Adoption Help** issue template and keep examples general and sanitized.

If you want to improve the model, open an Issue first or submit a Pull Request with a clear explanation of the problem and proposed change.

---

## Contributing

Contributions are welcome, especially:

- clearer templates
- better anti-loop rules
- better review verdict formats
- better examples
- safer GitHub/Cursor/Codex workflow patterns
- practical case studies without sensitive information

Please read `CONTRIBUTING.md` before opening a PR.

---

## License

This repository is published under **CC BY-NC 4.0** for documentation and templates unless otherwise stated.

You may read, adapt, and share the material with attribution for non-commercial use.

For commercial use, please contact the repository owner.

---

## Maintainer note

Sara Agentic OS is intentionally small. If a proposed change turns it into a large platform, custom runtime, dashboard, or uncontrolled automation system, it should be treated as a separate product decision — not a silent expansion of this operating model.
