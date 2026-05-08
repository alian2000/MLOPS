import json
import os

print("🤖 Project Agent analyzing build.log...")

# -------------------------------
# SAFE PATH HANDLING
# -------------------------------
LOG_FILE = "build.log"
REPORT_DIR = "ai-projects/multi-agent-openai-cicd/reports"
REPORT_FILE = os.path.join(REPORT_DIR, "project.json")

# -------------------------------
# CHECK BUILD LOG EXISTS
# -------------------------------
if not os.path.exists(LOG_FILE):
    print("❌ build.log missing")
    exit(1)

with open(LOG_FILE, "r") as f:
    log = f.read()

# -------------------------------
# REPORT STRUCTURE
# -------------------------------
report = {
    "status": "SUCCESS",
    "issues": [],
    "severity": "LOW"
}

# -------------------------------
# ERROR DETECTION (IMPROVED)
# -------------------------------

if "COMPILATION ERROR" in log:
    report["status"] = "FAILED"
    report["severity"] = "HIGH"
    report["issues"].append("Java compilation error detected in Maven build")

if "';' expected" in log:
    report["status"] = "FAILED"
    report["severity"] = "MEDIUM"
    report["issues"].append("Syntax error: missing semicolon in Java code")

if "BUILD FAILURE" in log:
    report["status"] = "FAILED"
    report["severity"] = "HIGH"
    report["issues"].append("Maven build failure detected")

if "ERROR" in log and "COMPILATION ERROR" not in log:
    report["issues"].append("Generic build error found in logs")

# -------------------------------
# ENSURE REPORT DIRECTORY EXISTS
# -------------------------------
os.makedirs(REPORT_DIR, exist_ok=True)

# -------------------------------
# WRITE REPORT
# -------------------------------
with open(REPORT_FILE, "w") as f:
    json.dump(report, f, indent=4)

print("📊 Project Analysis Report Generated:")
print(json.dumps(report, indent=4))
