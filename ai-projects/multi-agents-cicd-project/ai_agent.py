import json

BASE = "ai-projects/multi-agents-cicd-project"

decision = {"status": "APPROVED"}

with open(f"{BASE}/reports/project.json") as f:
    project = json.load(f)

with open(f"{BASE}/reports/security.json") as f:
    security = json.load(f)

if project["status"] == "FAILED" or security["issues"]:
    decision["status"] = "REJECTED"

with open(f"{BASE}/reports/ai.json", "w") as f:
    json.dump(decision, f, indent=4)

if decision["status"] == "REJECTED":
    exit(1)
