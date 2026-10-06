# Context Engine

## Goal

Give the reasoning model the **smallest relevant evidence set** that preserves correctness.

The context layer is not memory authority and not project governance.

## Baseline path

Without any external context engine:

1. identify repository root and active work object;
2. search for task-relevant symbols/files;
3. read only necessary surrounding code and rules;
4. expand evidence when uncertainty remains;
5. record exact evidence references in material reviews.

This remains the portable fallback.

## Optional NeuroMesh integration

For large repositories, Sara supports the maintained upstream **NeuroMesh** project as an optional local MCP context provider.

Why it fits:
- local-first repository graph;
- structural symbol/call/import evidence;
- task-conditioned seed selection;
- bounded neighborhood expansion;
- reversible body folding;
- impact/trace/search tools;
- explicit coverage signals;
- model/vendor independence.

Sara does not vendor the old internal fork. Use the maintained upstream and retain its own license.

### Contract

Sara may ask a context provider for:
- task-relevant files/symbols;
- structural dependencies;
- call/import traces;
- impact radius;
- architecture summary;
- evidence coverage.

Sara must not treat provider output as:
- product intent;
- approval;
- canonical State/Gates;
- security exception;
- proof that a change is correct.

## Suggested interaction

```text
task/work item
  -> repo discovery
  -> neuromesh_get_context(task) when available/useful
  -> expand a fold only if needed
  -> trace/impact only when the task requires it
  -> edit/test
  -> record evidence/outcome
```

Do not call a context engine for tiny repositories or obvious one-file edits when normal search is cheaper.

## Context trust ladder

```text
raw observation
 -> candidate fact
 -> verified fact with source + timestamp
 -> explicit canonical decision/project state
```

Retrieval never silently performs the final promotion.

## Memory and learning

Start with durable Git/Issue/Result evidence. Add memory only when a measured retrieval/state problem remains.

Future learning should operate on an Experience/Outcome ledger, not on anecdotes. "No change" is a valid learning result.

See `docs/COGNITIVE_ARCHITECTURE.md`.
