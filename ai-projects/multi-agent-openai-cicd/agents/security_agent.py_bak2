import json
import os

print("🤖 Project Agent analyzing build.log...")

LOG_PATH = "build.log"
REPORT_PATH = "ai-projects/multi-agent-openai-cicd/reports/project.json"

report = {
    "status": "SUCCESS",
    "error_type": None,
    "issues": [],
    "root_cause": [],
    "impact": [],
    "fix_suggestions": []
}

# -------------------------------
# READ BUILD LOG SAFELY
# -------------------------------

if not os.path.exists(LOG_PATH):
    report["status"] = "FAILED"
    report["error_type"] = "FILE_NOT_FOUND"
    report["issues"].append("build.log not found")
else:
    with open(LOG_PATH, "r") as f:
        log = f.read()

    # -------------------------------
    # COMPILATION ERROR DETECTION
    # -------------------------------
    if "COMPILATION ERROR" in log:
        report["status"] = "FAILED"
        report["error_type"] = "COMPILATION_ERROR"

        report["issues"].append("Java compilation error detected")

        report["root_cause"].append(
            "Source code has syntax or structural Java errors preventing compilation"
        )

        report["impact"].append(
            "Build failure prevents deployment and stops CI/CD pipeline"
        )

        report["fix_suggestions"].append(
            "Check Java syntax errors, missing imports, or incorrect method signatures"
        )

    # -------------------------------
    # SEMICOLON ERROR
    # -------------------------------
    if "';' expected" in log:
        report["status"] = "FAILED"
        report["error_type"] = "SYNTAX_ERROR"

        report["issues"].append("Missing semicolon in Java code")

        report["root_cause"].append(
            "Java compiler expects ';' at end of statement but found missing token"
        )

        report["impact"].append(
            "Compilation stops at syntax parsing stage"
        )

        report["fix_suggestions"].append(
            "Check line number mentioned in log and add missing semicolon ';'"
        )

    # -------------------------------
    # MAVEN BUILD FAILURE
    # -------------------------------
    if "BUILD FAILURE" in log:
        report["status"] = "FAILED"
        report["error_type"] = "MAVEN_BUILD_FAILURE"

        report["issues"].append("Maven build failed")

        report["root_cause"].append(
            "Maven lifecycle failed due to compilation or dependency issues"
        )

        report["impact"].append(
            "Artifact is not generated, deployment blocked"
        )

        report["fix_suggestions"].append(
            "Run 'mvn clean install -X' for debug logs and fix dependency or compile errors"
        )

# -------------------------------
# SAVE REPORT
# -------------------------------

os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)

with open(REPORT_PATH, "w") as f:
    json.dump(report, f, indent=4)

# -------------------------------
# OUTPUT
# -------------------------------

print("\n🤖 PROJECT ANALYSIS REPORT:")
print(json.dumps(report, indent=4))
