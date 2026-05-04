import json

BASE = "ai-projects/multi-agents-cicd-project"

report = {"issues": []}

with open(f"{BASE}/pom.xml") as f:
    data = f.read()

if "2.14.1" in data:
    report["issues"].append("Vulnerable log4j version detected")

with open(f"{BASE}/reports/security.json", "w") as f:
    json.dump(report, f)

if report["issues"]:
    exit(1)
