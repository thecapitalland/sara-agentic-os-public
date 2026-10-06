# Unified Architecture

## Optimization target

Sara optimizes for **accepted outcomes** with less human relay, rework, context waste, and governance ambiguity.

It does not optimize for agent count, automation count, model prestige, or maximum autonomy.

## Four planes

### 1. Governance & Delivery Plane

Owns the durable lifecycle of work:

```text
Intent -> Objective Contract -> Issue/spec -> State/Gates
       -> bounded execution -> branch/PR -> Result -> closeout
```

This plane decides **what work is authorized and what state it is in**. It does not define how every specialist is implemented.

### 2. Runtime & Capability Plane

Owns the reusable execution capability:

- Main Agent as parent coordinator.
- 12 independent-judgment Agent contracts.
- 16 reusable procedural Skills.
- runtime/tool permission boundaries.
- Cursor/Codex adapter rules.

This plane decides **which capability should act**. It does not own project product state.

### 3. Context & Cognitive Plane

Owns how evidence is assembled for a task:

- repository discovery;
- task-conditioned context;
- provenance/freshness;
- optional structural context engine;
- experience/outcome records;
- future memory/learning candidates.

A context provider may improve retrieval, but it never becomes product or governance authority.

### 4. Evidence & Assurance Plane

Owns proof:

- deterministic validation where possible;
- independent review for material protected work;
- exact commit/head/environment identity;
- before/after inventory for runtime publication;
- rollback evidence;
- PASS/PARTIAL/BLOCKED semantics.

## Control flow

```text
OWNER / PRODUCT INTENT
        |
        v
Objective Contract
        |
   human gate when needed
        |
        v
Work Ledger (Issue/spec + State/Gates)
        |
        +------ context request ------+
        |                             v
        |                    Context/Cognitive Plane
        |                    repo / optional NeuroMesh
        |                             |
        v                             |
Runtime/Capability Router <-----------+
        |
        v
bounded Agent/Skill execution
        |
        v
tests / evidence / review
        |
        v
Result + exact candidate
        |
        +--> remediation
        |
        +--> human UAT / production gate when applicable
        |
        v
reconciled completion
```

## Anti-duplication rules

1. Runtime Agents do not redefine project State/Gates.
2. Project governance does not maintain a competing global Agent roster.
3. Context/memory never silently promotes itself to canonical truth.
4. CI/tests provide evidence; they do not create business authority.
5. Models and tools are replaceable implementation choices, not constitutional roles.
6. Historical evidence does not become current policy merely because it remains in Git.

## Smallest sufficient path

The default path for a small change is deliberately short:

```text
task -> direct execution -> focused validation -> review if material -> done
```

Use the full lifecycle only when durability, risk, parallelism, or cross-tool handoff justifies it.
