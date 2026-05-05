import json
import os
import re

BASE = "ai-projects/multi-agents-cicd-project"

report = {
    "status": "SUCCESS",
    "errors": []
}

log_file = f"{BASE}/build.log"

print("🤖 Project Agent analyzing build.log...")

if not os.path.exists(log_file):
    report["status"] = "FAILED"
    report["errors"].append("build.log not found")

else:
    with open(log_file, "r", errors="ignore") as f:
        log = f.read()

    # 🔥 Extract actual compilation error line
    if "COMPILATION ERROR" in log:
        report["status"] = "FAILED"

        matches = re.findall(r"\[ERROR\].*", log)
        if matches:
            report["errors"].append(matches[0])  # 👈 actual error
        else:
            report["errors"].append("Compilation error detected")

# save report
os.makedirs(f"{BASE}/reports", exist_ok=True)

with open(f"{BASE}/reports/project.json", "w") as f:
    json.dump(report, f, indent=4)

print("🤖 Project Agent Report:", report)

if report["status"] == "FAILED":
    exit(1)
