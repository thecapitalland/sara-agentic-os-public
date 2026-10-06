# Sara Agentic OS

**A unified, Git-first operating system for governed AI-assisted engineering.**

Sara combines four concerns that are often scattered across separate tools and repositories:

1. **Governance & Delivery** — turn intent into durable, reviewable project work.
2. **Runtime & Capabilities** — route work to the smallest sufficient Agent/Skill set.
3. **Context & Cognition** — give models task-conditioned repository evidence instead of flooding context.
4. **Evidence & Assurance** — prove what happened, preserve exact candidate identity, and keep rollback/review boundaries explicit.

> Status: **Unified v1 candidate**. The architecture and public runtime baseline are usable, but live installation, automation, and production authority remain explicit operator decisions.

## Why this exists

AI-assisted projects usually break in the seams between systems:

- product intent lives in chat while code state lives in Git;
- agents duplicate roles or call an entire virtual company for a small task;
- large repositories flood models with irrelevant files;
- tools expose actions without defining authority;
- "done" is asserted without exact evidence;
- review, merge, release, memory, and handoff state drift apart;
- the human becomes the transport layer between ChatGPT, Cursor, Codex, GitHub, CI, and deployment.

Sara treats those as one system problem.

## Unified architecture

```text
Owner / Product Intent
        |
        v
+-------------------------------+
| GOVERNANCE & DELIVERY PLANE   |
| objective -> issue/spec       |
| state/gates -> branch/PR      |
| review -> result -> closeout  |
+---------------+---------------+
                |
                v
+-------------------------------+
| RUNTIME & CAPABILITY PLANE    |
| Main/orchestrator             |
| 12 trigger-gated Agents       |
| 16 reusable Skills            |
| tool/approval boundaries      |
+---------------+---------------+
                |
                v
+-------------------------------+
| CONTEXT & COGNITIVE PLANE     |
| repo discovery                |
| task-conditioned context      |
| optional NeuroMesh MCP        |
| experience/outcome contracts  |
+---------------+---------------+
                |
                v
+-------------------------------+
| EVIDENCE & ASSURANCE PLANE    |
| tests / QA / independent      |
| review / exact-head evidence  |
| publish / rollback discipline |
+-------------------------------+
```

The planes cooperate, but they do **not** redefine one another's authority.

## What each predecessor contributes

| Source | Retained strengths | Unified destination |
| --- | --- | --- |
| Sara governance work | Git-first lifecycle, State/Gates, Issue/spec/branch/PR/Result, fail-closed handoff, parallel ownership | Governance & Delivery Plane |
| Agentic Engineering System | 12-Agent / 16-Skill capability model, Agent-vs-Skill discipline, routing, approval/tool boundaries, runtime adapters | Runtime & Capability Plane |
| Agentic Control Plane | publish pins, before/after inventory, exact hashes, independent verification, rollback/evidence discipline | Evidence & Assurance Plane |
| Amir / NeuroMesh research | structural context graph, bounded retrieval/folding, MCP integration, cognitive/experience/learning design | Context & Cognitive Plane |

The archived control-plane track is **not** a separate runtime anymore. Its useful rules are absorbed here.

## Canonical source map

For this repository:

```text
sara/manifest.json                         -> machine-readable authority map
AGENTS.md                                  -> thin bootstrap/router
docs/OPERATING_MODEL_V1.md                 -> project/work lifecycle
runtime/agents/                            -> public Agent contracts
runtime/skills/                            -> public Skill procedures
docs/CONTEXT_ENGINE.md                     -> context-provider contract
docs/EVIDENCE_ASSURANCE.md                 -> verification/publish/rollback
templates/                                 -> project adoption artifacts
```

Historical v0 documents remain useful background, but they are not authoritative when they conflict with v1.

## Default work flow

```text
Intent
  -> Objective Contract
  -> Issue + accepted work artifact
  -> bounded execution
  -> branch + PR
  -> deterministic validation
  -> independent review when material
  -> human gate when protected
  -> Result + State/Gates reconciliation
```

Simple, low-risk work may skip unnecessary ceremony. Material or protected work may not skip required authority/evidence gates.

## Runtime model

Sara does not equate a job title with an Agent.

- **Agent/Subagent** — independent judgment or separate review context.
- **Skill** — repeatable method/checklist/procedure.
- **Rule** — short invariant or project constraint.
- **MCP** — external data/action interface.
- **Hook/CI** — deterministic enforcement.
- **Automation** — trigger; never authority by itself.

The public baseline contains **12 Agents and 16 Skills**. The Main Agent remains the parent coordinator; do not invoke the whole roster.

See [Runtime Model](docs/RUNTIME_MODEL.md).

## Context engine

Sara is model-agnostic and context-provider-agnostic. The default baseline is repository discovery plus selective file reading.

For large repositories, Sara supports **NeuroMesh** as an optional local MCP context engine. NeuroMesh can build a structural graph, route to task-relevant symbols/files, skeletonize unused bodies, and expose expansion/impact/trace tools without making NeuroMesh the project source of truth.

Sara intentionally does **not** vendor the old internal NeuroMesh fork. Use the maintained upstream implementation and keep Sara's integration contract here.

See [Context Engine](docs/CONTEXT_ENGINE.md).

## Public baseline

- 12 public Agent contracts.
- 16 reusable Skills.
- project objective/work/outcome templates.
- State/Gates/result lifecycle.
- Cursor and Codex adapter guidance.
- optional NeuroMesh MCP integration.
- exact-head review and rollback rules.
- validation script and read-only CI.

## Safety

Availability of a model, tool, token, credential, plugin, MCP, shell, or write permission does **not** create authority.

Explicit human approval remains required for production deployment, destructive operations, privileged/security-sensitive changes, credential/secret changes, material data migration, billing/external commitments, or changes to the governance/runtime baseline itself.

## Start here

1. [Unified Architecture](docs/ARCHITECTURE.md)
2. [Operating Model v1](docs/OPERATING_MODEL_V1.md)
3. [Runtime Model](docs/RUNTIME_MODEL.md)
4. [Context Engine](docs/CONTEXT_ENGINE.md)
5. [Evidence & Assurance](docs/EVIDENCE_ASSURANCE.md)
6. [Cognitive Architecture](docs/COGNITIVE_ARCHITECTURE.md)
7. [Migration & Lineage](docs/MIGRATION_AND_LINEAGE.md)
8. [Adoption Guide](docs/ADOPTION_GUIDE.md)

## Validation

```bash
python scripts/validate_baseline.py
```

The public CI is intentionally read-only. It validates structure; it does not merge, deploy, publish secrets, or invoke AI agents.

## Licensing

Sara-authored documentation, templates, Agent contracts, Skill contracts, and configuration examples remain under **CC BY-NC 4.0** unless a file says otherwise.

Third-party software such as NeuroMesh remains under its own upstream license. Sara integrates it; this repository does not relicense it. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
