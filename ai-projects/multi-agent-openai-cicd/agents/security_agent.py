import json

print("🔐 Security Agent analyzing pom.xml...")

with open("ai-projects/multi-agent-openai-cicd/pom.xml", "r") as f:
    pom = f.read()

report = {
    "status": "SUCCESS",
    "issues": []
}

if "1.1.1" in pom:
    report["status"] = "FAILED"
    report["issues"].append("Invalid log4j version detected")

if "1.1.0" in pom:
    report["status"] = "FAILED"
    report["issues"].append("Old vulnerable log4j version")

with open("ai-projects/multi-agent-openai-cicd/reports/security.json", "w") as f:
    json.dump(report, f, indent=4)

print(report)
