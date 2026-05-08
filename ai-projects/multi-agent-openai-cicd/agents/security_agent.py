import os
import json

print("🔐 Security Agent analyzing pom.xml...")

# -------------------------------
# PROJECT ROOT SAFE HANDLING
# -------------------------------
PROJECT_ROOT = os.path.abspath(os.getcwd())

POM_FILE = os.path.join(PROJECT_ROOT, "pom.xml")
REPORT_DIR = os.path.join(PROJECT_ROOT, "reports")
REPORT_FILE = os.path.join(REPORT_DIR, "security.json")

# -------------------------------
# DEBUG (IMPORTANT)
# -------------------------------
print("📂 PROJECT ROOT:", PROJECT_ROOT)
print("📄 POM FILE:", POM_FILE)

# -------------------------------
# CHECK FILE EXISTS
# -------------------------------
if not os.path.exists(POM_FILE):
    print("❌ pom.xml not found at:", POM_FILE)
    exit(1)

with open(POM_FILE, "r") as f:
    pom = f.read()

# -------------------------------
# REPORT STRUCTURE
# -------------------------------
report = {
    "status": "SUCCESS",
    "issues": [],
    "severity": "LOW",
    "cve_risk": []
}

# -------------------------------
# SECURITY CHECKS (IMPROVED)
# -------------------------------

if "1.1.1" in pom:
    report["status"] = "FAILED"
    report["severity"] = "HIGH"
    report["issues"].append("Invalid Log4j version detected (1.1.1)")
    report["cve_risk"].append("Potential CVE risk: Log4j vulnerable version pattern detected")

if "1.1.0" in pom:
    report["status"] = "FAILED"
    report["severity"] = "CRITICAL"
    report["issues"].append("Old vulnerable Log4j version detected (1.1.0)")
    report["cve_risk"].append("High risk of known Log4j CVE exploitation")

# -------------------------------
# ENSURE REPORT DIR EXISTS
# -------------------------------
os.makedirs(REPORT_DIR, exist_ok=True)

# -------------------------------
# WRITE REPORT
# -------------------------------
with open(REPORT_FILE, "w") as f:
    json.dump(report, f, indent=4)

print("📊 Security Analysis Completed:")
print(json.dumps(report, indent=4))
