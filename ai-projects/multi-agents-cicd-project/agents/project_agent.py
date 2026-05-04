import json

BASE = "ai-projects/multi-agents-cicd-project"

report = {"status": "SUCCESS", "errors": []}

with open(f"{BASE}/build.log", "r", errors="ignore") as f:
    for line in f:
        if "BUILD FAILURE" in line:
            report["status"] = "FAILED"
            report["errors"].append("Build failure")

with open(f"{BASE}/reports/project.json", "w") as f:
    json.dump(report, f)

if report["status"] == "FAILED":
    exit(1)
