# agents/security_agent.py

import json

BASE = "ai-projects/multi-agents-cicd-project"

report = {"issues": []}

with open(f"{BASE}/pom.xml") as f:
    data = f.read()

# 🔥 detect vulnerable OR invalid
if "log4j-core" in data:

    if "2.14.1" in data:
        report["issues"].append("Vulnerable log4j version detected")

    if "1.1.1" in data:
        report["issues"].append("Invalid log4j version (not found in Maven repo)")

with open(f"{BASE}/reports/security.json", "w") as f:
    json.dump(report, f, indent=4)

print("🔐 Security Report:", report)

if report["issues"]:
    exit(1)
