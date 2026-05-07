import os
import json

print("🔧 Fix Agent Started...")

# ------------------------------------------------
# PROJECT ROOT
# ------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT = os.path.abspath(
    os.path.join(BASE_DIR, "..")
)

# ------------------------------------------------
# REPORTS DIRECTORY
# ------------------------------------------------
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports")

os.makedirs(REPORTS_DIR, exist_ok=True)

# ------------------------------------------------
# FIX REPORT
# ------------------------------------------------
fix_report = {
    "fixes_applied": []
}

# ------------------------------------------------
# FIX 1 → INVALID LOG4J VERSION
# ------------------------------------------------
pom_file = os.path.join(PROJECT_ROOT, "pom.xml")

if os.path.exists(pom_file):

    with open(pom_file, "r") as f:
        pom = f.read()

    if "1.1.1" in pom:

        print("🔧 Fixing log4j version...")

        pom = pom.replace("1.1.1", "2.17.1")

        with open(pom_file, "w") as f:
            f.write(pom)

        print("✅ Fixed log4j version")

        fix_report["fixes_applied"].append(
            "Updated log4j version from 1.1.1 to 2.17.1"
        )

# ------------------------------------------------
# FIX 2 → JAVA SYNTAX ERROR
# ------------------------------------------------

java_file = os.path.join(
    PROJECT_ROOT,
    "src/main/java/App.java"
)

# fallback path
if not os.path.exists(java_file):

    java_file = os.path.join(
        PROJECT_ROOT,
        "src/main/java/com/demo/App.java"
    )

if os.path.exists(java_file):

    with open(java_file, "r") as f:
        code = f.read()

    syntax_issue = False

    # detect broken patterns
    if ');)' in code:
        syntax_issue = True

    if '"))' in code:
        syntax_issue = True

    if 'System.out.println("Hello AI DevOps")' in code:
        syntax_issue = True

    if syntax_issue:

        print("🔧 Fixing Java syntax issue...")

        fixed_code = """
package com.demo;

public class App {

    public static void main(String[] args) {

        System.out.println("Hello AI DevOps");

    }

}
"""

        with open(java_file, "w") as f:
            f.write(fixed_code)

        print("✅ Java syntax fixed")

        fix_report["fixes_applied"].append(
            "Fixed Java compilation syntax issue"
        )

# ------------------------------------------------
# SAVE JSON REPORT
# ------------------------------------------------

report_file = os.path.join(
    REPORTS_DIR,
    "fix_report.json"
)

with open(report_file, "w") as f:
    json.dump(fix_report, f, indent=4)

print("✅ Fix report generated")

print("🎉 Fix Agent Completed")
