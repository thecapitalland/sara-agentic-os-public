# Roadmap

Sara Agentic OS is currently an operating model, not a product platform.

This roadmap is intentionally conservative. It describes public-facing maturity without overstating automation.

---

## Current status — Operating Model v0

Available now:

- core README and positioning
- Operating Model v0
- Adoption Guide
- sanitized case study
- project-state template
- work-packet template
- execution-result template
- chat-retirement template
- optional AGENTS template
- issue-to-agent conveyor guide
- parallel agents guide
- operational lessons
- failure playbooks
- presentation narrative

---

## v0.1 — Public documentation hardening

Goals:

- improve examples
- add clearer template instructions
- add a sample project walkthrough
- add more adoption/help issue templates
- improve glossary and terminology
- make the public README easier to scan
- collect external feedback

---

## v0.2 — Evidence and review patterns

Goals:

- improve review verdict examples
- add sample PR review workflows
- add examples of `PARTIAL`, `BLOCKED`, and `WRONG DIRECTION`
- define safer docs/status fast-lane examples
- document common anti-patterns from public feedback

---

## v0.3 — Optional helper checks

Possible additions:

- lightweight checklists for packet completeness
- GitHub issue template improvements
- documentation-only validation examples
- optional CI checks for docs structure

These should remain optional and should not become a hidden runtime or automation platform.

---

## Later — Narrow automation experiments

Potential future experiments:

- helper scripts for local validation
- optional GitHub Actions that check packet fields
- label consistency checks
- docs-only housekeeping checks
- branch cleanup after accepted merge

Any automation should be:

- narrow
- reversible where possible
- logged
- loop-safe
- not a replacement for review
- not a general code auto-merge path

---

## Not on the roadmap by default

Sara does not currently aim to become:

- a SaaS platform
- a custom agent runtime
- a GitHub App
- a dashboard-heavy tool
- a queue or background worker
- a marketplace
- a blockchain system
- an autonomous code-merging system

These would require separate design, safety review, and explicit approval.

---

## Public readiness checklist

Before actively promoting Sara beyond a quiet public repo, the project should have:

- clear README
- complete adoption guide
- sanitized case study
- issue conveyor guide
- failure playbooks
- glossary
- sample project walkthrough
- contribution guidelines
- no private project details
- no exaggerated automation claims
- a clear invitation for feedback and collaborators
