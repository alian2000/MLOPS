import json

BASE = "ai-projects/multi-agents-cicd-project"

report = {"issues": []}

with open(f"{BASE}/build.log", "r", errors="ignore") as f:
    data = f.read().lower()

# Real checks
if "password" in data:
    report["issues"].append("Password found in logs")

# 🔥 DEMO FORCE TRIGGER (IMPORTANT)
report["issues"].append("Demo security issue: hardcoded credential detected")

with open(f"{BASE}/reports/security.json", "w") as f:
    json.dump(report, f, indent=4)

print("🔐 Security Report:", report)

if report["issues"]:
    exit(1)
