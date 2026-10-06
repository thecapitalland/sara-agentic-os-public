# Migration & Lineage

Sara Agentic OS v1 is a consolidation, not a raw repository dump.

## Sara governance lineage

Retained:
- Git-first operational truth;
- Issue/spec execution envelope;
- State/Gates;
- branch/PR discipline;
- structured Result;
- exact closeout;
- parallel ownership and overlap stop rules;
- action-over-wait for already-authorized safe work.

Removed/avoided:
- duplicate constitutional prose in many files;
- project-specific private state;
- automation that can loop without bounded triggers;
- separate global Agent definitions inside project governance.

## Agentic Engineering System lineage

Retained:
- Agent vs Skill distinction;
- 12-Agent / 16-Skill baseline;
- Main Agent as parent coordinator;
- trigger-gated specialists;
- human/tool permission boundaries;
- independent review;
- manifest-driven roster;
- runtime adapter separation.

Corrected in the public design:
- one manifest owns stable roster/version facts;
- project State remains outside the global runtime catalog.

## Agentic Control Plane lineage

The former control-plane track is treated as historical implementation evidence, not a separate product.

Retained:
- source-to-runtime mapping;
- before/after inventory;
- reversible backup/restore;
- hash/count verification;
- native acceptance probes;
- independent review;
- explicit residual risks.

## Amir / NeuroMesh lineage

The private Amir branch shared its code ancestry with NeuroMesh and added cognitive/research design material.

Unified decision:
- do not vendor the old fork;
- integrate the maintained upstream NeuroMesh as an optional context provider;
- retain the useful cognitive architecture, experience-ledger, learning, and evidence-guardrail ideas in Sara-authored public documents;
- preserve upstream licensing/attribution.

## Why not copy everything

Raw merging would preserve conflicting authorities, stale histories, private evidence, machine-specific paths, and old runtime snapshots.

The unified public repo preserves **capabilities and verified patterns**, not every historical artifact.
