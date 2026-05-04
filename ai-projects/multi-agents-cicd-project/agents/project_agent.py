import json

log_file = "build.log"

report = {
    "status": "SUCCESS",
    "errors": [],
    "warnings": []
}

with open(log_file, "r", errors="ignore") as f:
    for line in f:
        line = line.strip()

        if "BUILD FAILURE" in line:
            report["status"] = "FAILED"
            report["errors"].append(line)

        elif "[ERROR]" in line:
            report["errors"].append(line)

        elif "[WARNING]" in line:
            report["warnings"].append(line)

# Save report
with open("reports/project.json", "w") as f:
    json.dump(report, f, indent=4)

print("🤖 Project Agent Done:", report)

if report["status"] == "FAILED":
    exit(1)
