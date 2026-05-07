import json

with open("ai-projects/multi-agent-openai-cicd/reports/project.json") as f:
    project = json.load(f)

with open("ai-projects/multi-agent-openai-cicd/reports/security.json") as f:
    security = json.load(f)

final = {
    "decision": "APPROVED",
    "reasons": []
}

if project["status"] == "FAILED":
    final["decision"] = "REJECTED"
    final["reasons"].extend(project["issues"])

if security["status"] == "FAILED":
    final["decision"] = "REJECTED"
    final["reasons"].extend(security["issues"])

with open("ai-projects/multi-agent-openai-cicd/reports/ai.json", "w") as f:
    json.dump(final, f, indent=4)

print("🧠 AI Decision:")
print(final)
