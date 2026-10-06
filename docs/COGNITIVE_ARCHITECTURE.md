# Cognitive Architecture

This document captures the useful, testable ideas contributed by the Amir/NeuroMesh research branch without turning biological metaphors into authority.

## Guardrails

For every cognitive/bio-inspired mechanism distinguish:
1. external scientific/technical evidence;
2. engineering analogy;
3. implemented behavior;
4. proposed hypothesis;
5. measured result.

Do not add a module merely because a metaphor is attractive.

## Shared cognitive functions

A practical agentic system can treat these as shared functions:

- **Perception** — code, diffs, logs, tool outcomes, screenshots, repository structure.
- **Memory** — working, episodic, and carefully promoted durable facts.
- **Attention** — choose what deserves context/reasoning budget.
- **Value/Risk** — estimate confidence, consequence, novelty, quality.
- **Action** — edits, tools, commands, messages, deployment adapters.

Specialist Agents should consume these common functions rather than each inventing a private infrastructure stack.

## Shared workspace, not mega-agent

Target pattern:

```text
observations
   -> selective context/gating
   -> typed shared task state
      -> specialist capability
      -> actions
   -> outcomes/evidence
   -> learning candidates
```

A shared workspace means selective state exchange, not one omniscient LLM receiving every token.

## Experience Ledger

Before learning, record what happened:

```yaml
experience:
  task_id:
  repo_ref:
  commit:
  model_runtime:
  selected_context: []
  tools_used: []
  decisions: []
  actions: []
  outcomes: []
  validation: []
  tokens:
  latency:
  human_interventions:
```

## Outcome contract

Learning needs consequence evidence:

```yaml
outcome:
  task_id:
  tests_passed:
  accepted:
  uat_passed:
  merged:
  rolled_back:
  user_rejected:
  evidence_refs: []
```

## Learning discipline

Possible learning actions:
- no change;
- keep episodic evidence;
- promote a durable fact after verification;
- adjust retrieval/routing preference;
- decay/silence a weak path;
- create a Skill candidate;
- add a regression/evaluation fixture.

One successful run must not become universal law.

## Timescales

- fast: current task/context;
- medium: episodic memory, routing weights, Skills, evaluation data;
- slow: learned rankers/routers/adapters only after enough validated evidence.

The foundation/reasoning model remains replaceable.
