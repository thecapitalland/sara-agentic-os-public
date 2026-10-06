# Codex Adapter

Codex and Cursor do not use identical Agent file formats. The Sara responsibility model stays canonical; a Codex adapter may render it.

## Target surfaces

Typical user-level targets:

```text
~/.codex/AGENTS.md
~/.codex/agents/*.toml
~/.agents/skills/<name>/SKILL.md
```

## Adapter requirements

A renderer/installer must:
- pin the Sara source commit;
- derive the roster from `sara/manifest.json`;
- preserve responsibility and approval boundaries;
- record any runtime-specific wording adaptation;
- be deterministic and dry-run-first;
- never copy credentials/auth databases;
- inventory before/after state;
- support rollback;
- verify the runtime actually loads the rendered artifacts.

Do not maintain a second hand-edited canonical Agent catalog in TOML.

The former Agentic Control Plane proved the value of this publication discipline; v1 folds that discipline into the unified evidence model rather than reviving a separate repository.
