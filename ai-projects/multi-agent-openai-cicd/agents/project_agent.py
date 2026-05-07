import json

print("🤖 Project Agent analyzing build.log...")

with open("build.log", "r") as f:
    log = f.read()

report = {
    "status": "SUCCESS",
    "issues": []
}

if "COMPILATION ERROR" in log:
    report["status"] = "FAILED"
    report["issues"].append("Java compilation error")

if "';' expected" in log:
    report["issues"].append("Missing semicolon in Java code")

if "BUILD FAILURE" in log:
    report["status"] = "FAILED"

with open("reports/project.json", "w") as f:
    json.dump(report, f, indent=4)

print(report)
