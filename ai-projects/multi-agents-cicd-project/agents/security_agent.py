import json
import os

BASE = "ai-projects/multi-agents-cicd-project"

report = {"issues": []}

with open(f"{BASE}/build.log", "r", errors="ignore") as f:
    data = f.read().lower()

if "password" in data:
    report["issues"].append("Password found in logs")

# 🔥 DEMO ONLY FIRST TIME
flag_file = f"{BASE}/demo_triggered"

if not os.path.exists(flag_file):
    report["issues"].append("Demo security issue: hardcoded credential detected")
    
    with open(flag_file, "w") as f:
        f.write("done")

with open(f"{BASE}/reports/security.json", "w") as f:
    json.dump(report, f, indent=4)

if report["issues"]:
    exit(1)
