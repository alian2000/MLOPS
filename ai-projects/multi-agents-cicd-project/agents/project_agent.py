import json
import os

BASE = "ai-projects/multi-agents-cicd-project"

report = {
    "status": "SUCCESS",
    "errors": []
}

log_file = f"{BASE}/build.log"

if not os.path.exists(log_file):
    report["status"] = "FAILED"
    report["errors"].append("build.log not found")

else:
    with open(log_file, "r", errors="ignore") as f:
        log = f.read()

    if "BUILD FAILURE" in log:
        report["status"] = "FAILED"
        report["errors"].append("Build failure")

    if "Could not resolve dependencies" in log:
        report["status"] = "FAILED"
        report["errors"].append("Dependency resolution failed")

    if "COMPILATION ERROR" in log:
        report["status"] = "FAILED"
        report["errors"].append("Compilation error")

# save report
os.makedirs(f"{BASE}/reports", exist_ok=True)

with open(f"{BASE}/reports/project.json", "w") as f:
    json.dump(report, f, indent=4)

print("🤖 Project Agent Report:", report)

if report["status"] == "FAILED":
    exit(1)
