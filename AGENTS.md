# Sara Agent Bootstrap

## Load order

For material work, load:
1. `sara/manifest.json`;
2. `docs/OPERATING_MODEL.md`;
3. current project State and Gates;
4. active Objective / Work Item;
5. the relevant Agent contract;
6. only the Skills needed for the task.

## Execution rule

Keep simple work direct.

For material work, invoke the smallest sufficient capability set. Do not simulate a meeting and do not invoke the whole roster.

## Durable work

```text
Objective -> Work Item -> bounded change -> validation/review -> Result -> State/Gates reconciliation
```

## Protected actions

Explicit human approval is required for protected actions defined in the manifest.

Available capability does not create authority.

## Completion

Never claim DONE/PASS solely from an agent statement or green validation.

Material completion requires the applicable acceptance evidence and gate state.
