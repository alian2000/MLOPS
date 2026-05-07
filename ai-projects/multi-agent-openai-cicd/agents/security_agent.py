import json

print("🔐 Security Agent analyzing pom.xml...")

with open("pom.xml", "r") as f:
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

with open("reports/security_report.json", "w") as f:
    json.dump(report, f, indent=4)

print(report)
