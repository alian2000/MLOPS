import json
import os

SECURITY_FILE = "ai-projects/multi-agent-openai-cicd/reports/security.json"
PROJECT_FILE = "ai-projects/multi-agent-openai-cicd/reports/project.json"

def safe_load(file_path):
    if not os.path.exists(file_path):
        return {"status": "FAILED", "issues": ["Report missing"]}
    with open(file_path) as f:
        return json.load(f)

project = safe_load(PROJECT_FILE)
security = safe_load(SECURITY_FILE)

final = {
    "decision": "APPROVED",
    "reasons": []
}

if project.get("status") == "FAILED":
    final["decision"] = "REJECTED"
    final["reasons"] += project.get("issues", [])

if security.get("status") == "FAILED":
    final["decision"] = "REJECTED"
    final["reasons"] += security.get("issues", [])

with open("ai-projects/multi-agent-openai-cicd/reports/ai.json", "w") as f:
    json.dump(final, f, indent=4)

print("🧠 AI Decision:", final)
