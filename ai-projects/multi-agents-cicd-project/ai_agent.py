import json

BASE = "ai-projects/multi-agents-cicd-project"

decision = {
    "status": "APPROVED",
    "reason": []
}

with open(f"{BASE}/reports/project.json") as f:
    project = json.load(f)

with open(f"{BASE}/reports/security.json") as f:
    security = json.load(f)

# Logic
if project["status"] == "FAILED":
    decision["status"] = "REJECTED"
    decision["reason"].append("Build failure detected")

if security["issues"]:
    decision["status"] = "REJECTED"
    decision["reason"].extend(security["issues"])

with open(f"{BASE}/reports/ai.json", "w") as f:
    json.dump(decision, f, indent=4)

print("🧠 AI Decision:", decision)

if decision["status"] == "REJECTED":
    exit(1)
