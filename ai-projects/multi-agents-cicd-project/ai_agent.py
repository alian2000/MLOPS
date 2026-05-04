import json
import os

BASE = "ai-projects/multi-agents-cicd-project"

decision = {
    "status": "APPROVED",
    "reason": []
}

project_file = f"{BASE}/reports/project.json"
security_file = f"{BASE}/reports/security.json"

# 🔍 Read Project Agent Report
if os.path.exists(project_file):
    with open(project_file) as f:
        project = json.load(f)

    if project.get("status") == "FAILED":
        decision["status"] = "REJECTED"
        decision["reason"].extend(project.get("errors", []))
else:
    decision["status"] = "REJECTED"
    decision["reason"].append("Project report missing")

# 🔐 Read Security Agent Report
if os.path.exists(security_file):
    with open(security_file) as f:
        security = json.load(f)

    if security.get("issues"):
        decision["status"] = "REJECTED"
        decision["reason"].extend(security.get("issues", []))
else:
    decision["status"] = "REJECTED"
    decision["reason"].append("Security report missing")

# 🧠 Save Decision
with open(f"{BASE}/reports/ai.json", "w") as f:
    json.dump(decision, f, indent=4)

print("🧠 AI Decision:", decision)

# ❌ Reject = exit code 1 (Jenkins trigger)
if decision["status"] == "REJECTED":
    exit(1)
