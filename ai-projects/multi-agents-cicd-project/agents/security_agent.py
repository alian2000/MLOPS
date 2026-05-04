import json

BASE = "ai-projects/multi-agents-cicd-project"

report = {"issues": []}

with open(f"{BASE}/build.log", "r", errors="ignore") as f:
    data = f.read().lower()

if "password" in data:
    report["issues"].append("Password found in logs")

with open(f"{BASE}/reports/security.json", "w") as f:
    json.dump(report, f, indent=4)

if report["issues"]:
    exit(1)
