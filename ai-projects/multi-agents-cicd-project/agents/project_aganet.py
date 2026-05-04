# agents/project_agent.py

import json

BASE = "ai-projects/multi-agents-cicd-project"

report = {"status": "SUCCESS", "errors": []}

with open(f"{BASE}/build.log", "r", errors="ignore") as f:
    log = f.read()

if "BUILD FAILURE" in log:
    report["status"] = "FAILED"
    report["errors"].append("Build failure detected")

if "Could not resolve dependencies" in log:
    report["status"] = "FAILED"
    report["errors"].append("Dependency resolution failed")

with open(f"{BASE}/reports/project.json", "w") as f:
    json.dump(report, f, indent=4)

print("🤖 Project Report:", report)

if report["status"] == "FAILED":
    exit(1)
