---
name: prompt-engineering
description: "Design bounded prompts/instructions that preserve authority, context, outputs and stop conditions."
---

# prompt-engineering

## Process

1. state outcome and source-of-truth references
2. include only relevant context and constraints
3. define allowed/forbidden scope and tools
4. define expected artifact/evidence
5. define stop/escalation conditions
6. remove persona/verbosity that does not improve task success

## Constraints

- prompt text does not create authority
- do not bury critical constraints in prose
- prefer repository artifacts over giant chat prompts

## Output

Produce the smallest durable artifact/evidence needed by the active work item. Separate facts, assumptions, findings, risks, and unresolved gates.
