import json

decision = {
    "final_status": "APPROVED",
    "reasons": []
}

# Load reports
with open("reports/project.json") as f:
    project = json.load(f)

with open("reports/security.json") as f:
    security = json.load(f)

# Decision logic
if project["status"] == "FAILED":
    decision["final_status"] = "REJECTED"
    decision["reasons"].append("Build failed")

if security["issues"]:
    decision["final_status"] = "REJECTED"
    decision["reasons"].extend(security["issues"])

# Save
with open("reports/ai.json", "w") as f:
    json.dump(decision, f, indent=4)

print("🧠 FINAL AI DECISION:", decision)

if decision["final_status"] == "REJECTED":
    exit(1)
