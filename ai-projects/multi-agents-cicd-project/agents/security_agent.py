import json
import os

BASE = "ai-projects/multi-agents-cicd-project"

report = {"issues": []}

with open(f"{BASE}/build.log", "r", errors="ignore") as f:
    data = f.read().lower()

if "password" in data:
    report["issues"].append("Password found in logs")

# 🔥 trigger only once
flag = f"{BASE}/demo_flag"

if not os.path.exists(flag):
    report["issues"].append("Demo security issue: hardcoded credential detected")
    
    with open(flag, "w") as f:
        f.write("done")

with open(f"{BASE}/reports/security.json", "w") as f:
    json.dump(report, f, indent=4)

if report["issues"]:
    exit(1)
