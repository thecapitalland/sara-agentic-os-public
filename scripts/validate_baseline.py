#!/usr/bin/env python3
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
manifest_path = ROOT / "sara" / "manifest.json"

errors = []

try:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
except Exception as exc:
    print(f"FAIL: cannot read manifest: {exc}")
    sys.exit(1)

required_docs = [
    "AGENTS.md",
    "docs/ARCHITECTURE.md",
    "docs/OPERATING_MODEL_V1.md",
    "docs/RUNTIME_MODEL.md",
    "docs/CONTEXT_ENGINE.md",
    "docs/EVIDENCE_ASSURANCE.md",
    "docs/COGNITIVE_ARCHITECTURE.md",
    "docs/MIGRATION_AND_LINEAGE.md",
    "docs/DOCUMENT_REGISTRY.md",
    "THIRD_PARTY_NOTICES.md",
]
for rel in required_docs:
    if not (ROOT / rel).is_file():
        errors.append(f"missing required file: {rel}")

agents = manifest.get("agents", [])
skills = manifest.get("skills", [])

if len(agents) != 12 or len(set(agents)) != 12:
    errors.append(f"expected 12 unique agents, got {len(agents)}")
if len(skills) != 16 or len(set(skills)) != 16:
    errors.append(f"expected 16 unique skills, got {len(skills)}")

for name in agents:
    path = ROOT / "runtime" / "agents" / f"{name}.md"
    if not path.is_file():
        errors.append(f"missing agent contract: {path.relative_to(ROOT)}")

for name in skills:
    path = ROOT / "runtime" / "skills" / name / "SKILL.md"
    if not path.is_file():
        errors.append(f"missing skill contract: {path.relative_to(ROOT)}")

if errors:
    print("BASELINE VALIDATION: FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("BASELINE VALIDATION: PASS")
print(f"version={manifest.get('version')}")
print(f"agents={len(agents)}")
print(f"skills={len(skills)}")
