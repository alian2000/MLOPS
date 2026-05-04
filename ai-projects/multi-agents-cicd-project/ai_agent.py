import json

BASE = "ai-projects/multi-agents-cicd-project"

decision = {"status": "APPROVED"}

project = json.load(open(f"{BASE}/reports/project.json"))
security = json.load(open(f"{BASE}/reports/security.json"))

if project["status"] == "FAILED" or security["issues"]:
    decision["status"] = "REJECTED"

json.dump(decision, open(f"{BASE}/reports/ai.json", "w"))

if decision["status"] == "REJECTED":
    exit(1)
