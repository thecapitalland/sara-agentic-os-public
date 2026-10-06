# Roadmap

## Current — Unified v1 candidate

Delivered in this candidate:
- one authority map;
- governance/delivery plane;
- public 12-Agent / 16-Skill runtime contracts;
- context-engine contract;
- optional NeuroMesh integration;
- evidence/assurance rules;
- adoption templates;
- baseline validation.

## Gate A — Public review

Before declaring v1 stable:
- validate no private paths/secrets/project-specific material;
- review Agent/Skill duplication and trigger precision;
- verify license/third-party notices;
- test adoption on at least one clean sample project;
- verify Cursor/Codex adapter docs against current clients.

## Gate B — Safe runtime packaging

Only if real adoption needs it:
- deterministic render/install package;
- dry-run by default;
- explicit apply;
- before/after inventory;
- rollback;
- no credential mutation.

## Gate C — Context provider benchmark

Benchmark:
- baseline repository search;
- NeuroMesh-assisted context;
- quality/recall;
- latency;
- token/context volume;
- human intervention/rework.

Keep NeuroMesh optional unless measured value justifies the dependency.

## Gate D — Experience/Learning pilot

Start with the Experience/Outcome schema and offline analysis. Do not create autonomous memory mutation or self-promoting policies until evidence demonstrates a real problem and a safe evaluation path.

## Explicit non-goals

- agent swarm for its own sake;
- mandatory centralized orchestration service;
- replacing GitHub with a custom project database before needed;
- global autonomous memory as a prerequisite;
- production auto-deploy by default;
- self-approval of material changes.
