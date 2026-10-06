#!/usr/bin/env python3
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

try:
    manifest = json.loads((ROOT / "sara" / "manifest.json").read_text(encoding="utf-8"))
except Exception as exc:
    print(f"FAIL: cannot read manifest: {exc}")
    sys.exit(1)

required = [
    "README.md","LICENSE","CHANGELOG.md","AGENTS.md",
    "docs/ARCHITECTURE.md","docs/OPERATING_MODEL.md","docs/RUNTIME_MODEL.md",
    "docs/CONTEXT_ENGINE.md","docs/COGNITIVE_ARCHITECTURE.md",
    "docs/EVIDENCE_ASSURANCE.md","docs/ADOPTION_GUIDE.md",
    "docs/DOCUMENT_REGISTRY.md","docs/ROADMAP.md",
]
for rel in required:
    if not (ROOT / rel).is_file():
        errors.append(f"missing required file: {rel}")

if manifest.get("version") != "2.0.0":
    errors.append("manifest version must be 2.0.0")
if manifest.get("license") != "MIT":
    errors.append("manifest license must be MIT")

agents = manifest.get("agents", [])
skills = manifest.get("skills", [])
if len(agents) != 12 or len(set(agents)) != 12:
    errors.append(f"expected 12 unique agents, got {len(agents)}")
if len(skills) != 16 or len(set(skills)) != 16:
    errors.append(f"expected 16 unique skills, got {len(skills)}")

for name in agents:
    if not (ROOT / "runtime" / "agents" / f"{name}.md").is_file():
        errors.append(f"missing agent: {name}")
for name in skills:
    if not (ROOT / "runtime" / "skills" / name / "SKILL.md").is_file():
        errors.append(f"missing skill: {name}")

if errors:
    print("SARA V2 VALIDATION: FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("SARA V2 VALIDATION: PASS")
print("version=2.0.0")
print(f"agents={len(agents)}")
print(f"skills={len(skills)}")
print("license=MIT")
