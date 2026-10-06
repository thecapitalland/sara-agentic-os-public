# Evidence & Assurance

This plane absorbs the most useful discipline from the former deployment/control-plane track.

## Completion is evidence-backed

Material completion requires:
- exact source/candidate identity;
- acceptance criteria;
- deterministic validation where possible;
- independent review when required;
- protected human gates when applicable;
- durable Result;
- reconciliation of open/blocked related work.

## Exact-head rule

Review and validation belong to a specific commit/PR head. A later material push invalidates stale review evidence.

## Runtime publication rule

When publishing user-level Agents/Skills to a live runtime:

1. identify canonical source commit;
2. inventory current target state;
3. back up or create a reversible restore point;
4. render/install from canonical source only;
5. inventory after state;
6. verify expected files/hashes/counts;
7. run native acceptance probes;
8. independently review material baseline changes;
9. preserve residual risks rather than rewriting them as PASS;
10. keep rollback instructions.

## Before/after evidence

For a runtime install, record at minimum:
- source commit;
- target paths;
- artifact count;
- relevant hashes;
- runtime/client version;
- validation command/result;
- known residual failures;
- rollback location/method.

Do not commit credentials, auth databases, tokens, or unrelated user configuration.

## Independent review

The implementer must not be the sole final reviewer of a material protected change.

Independent review should verify:
- scope;
- authority;
- evidence integrity;
- correctness/security risks;
- skipped lanes/gates;
- false DONE/PASS claims.

## Rollback

Stateful or production-facing changes need an explicit rollback/recovery design before authorization. Rollback should be safely exercised or independently verified where practical.

## CI boundary

CI is evidence. CI does not:
- make product decisions;
- waive human approval;
- accept security risk;
- authorize production;
- prove UAT.
