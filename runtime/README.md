# Sara Runtime Baseline

This directory contains Sara's public, vendor-neutral runtime contracts.

- `agents/` — independent-judgment roles.
- `skills/` — reusable procedures.

The canonical roster is `sara/manifest.json`. Do not hard-code roster counts in additional policy files.

A role is not automatically an Agent. Prefer a Skill for repeatable procedure and an Agent only when independent judgment or separate review context materially helps.

Live installation is an explicit operator action. Repository presence does not imply installation.
