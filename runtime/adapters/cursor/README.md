# Cursor Adapter

## Mapping

- Sara Agent contract: `runtime/agents/<name>.md`
- Cursor user Agent: `%USERPROFILE%/.cursor/agents/<name>.md` on Windows or the equivalent home path.
- Sara Skill: `runtime/skills/<name>/SKILL.md`
- Cursor user Skill: `%USERPROFILE%/.cursor/skills/<name>/SKILL.md`

Project-specific rules remain project-local.

## Safe install discipline

1. validate this repository baseline;
2. inventory existing user-level Agents/Skills;
3. back up conflicting files;
4. copy only the manifest roster;
5. do not overwrite project-specific overrides automatically;
6. restart/reload the client as required;
7. run representative routing tasks;
8. record failures and rollback rather than forcing parity.

This public repository does not mutate Cursor settings, MCP configuration, credentials, or User Rules automatically.
