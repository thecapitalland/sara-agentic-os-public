# AGENTS.md — Sara Agentic OS Bootstrap

This file is the thin bootstrap for agents working with the public Sara distribution.

## Load order

For material work, read:

1. `sara/manifest.json`
2. `docs/OPERATING_MODEL_V1.md`
3. applicable project `PROJECT_CURRENT_STATE.md` and `GATES.md`
4. the active Issue/objective/work artifact
5. the applicable Agent contract under `runtime/agents/`
6. only the Skills actually needed under `runtime/skills/`

## Authority

Project/operator instructions control product intent. Sara supplies reusable governance and runtime defaults; a project may become stricter but must not silently weaken a named human gate or independent-review requirement.

## Execution rule

Handle simple, bounded, low-risk work directly. For material work, use the smallest necessary set of specialist Agents/Skills. Do not simulate a meeting and do not invoke the whole team.

## Durable work

For repository mutation or cross-tool handoff, use:

`Objective -> Issue/spec -> branch/ownership -> PR -> validation/review -> Result -> State/Gates reconciliation`

Chat is convenience context, not the sole source of truth.

## Protected actions

Human approval is required before production deployment, destructive/privileged actions, secret/credential changes, security-risk acceptance, material data migration, external financial/message commitments, or baseline governance/runtime changes.

## Completion

Never claim DONE/PASS/READY solely from an agent statement or green CI. Material completion requires the applicable acceptance evidence and review/gate state.
