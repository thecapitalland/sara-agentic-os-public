# Evidence & Assurance

Confidence is not evidence. Completion is a state transition backed by evidence.

## Exact candidate
Validation and review belong to an exact candidate identity. Material changes invalidate stale review evidence.

## Material completion
Include applicable acceptance criteria, deterministic validation, candidate identity, independent review, security review when triggered, human gates, rollback/recovery, durable Result, and State/Gates reconciliation.

## Independent review
The author is not the sole final reviewer of a material protected change.

## Publication discipline
For runtime publication:
1. pin canonical source version;
2. inventory target state;
3. create a reversible checkpoint;
4. publish only canonical artifacts;
5. inventory after state;
6. verify expected files/counts/hashes when applicable;
7. run native acceptance probes;
8. preserve residual failures;
9. keep rollback instructions.

Automated validation is evidence; it does not waive human authority.
