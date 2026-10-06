# Sara Runtime Baseline

This directory contains the public, vendor-neutral runtime contracts.

- `agents/` — independent-judgment roles.
- `skills/` — reusable procedures.
- `adapters/` — client-specific installation/render guidance.

The canonical roster is `sara/manifest.json`. Do not hard-code roster counts in additional policy files.

## Rule

A role is not automatically an Agent. Prefer a Skill for repeatable procedure and an Agent only when independent judgment/context materially helps.

Live installation is an explicit operator action. Repository presence does not imply installation.
