import os
import json

print("🔧 Fix Agent Started...")

# ------------------------------------------------
# ABSOLUTE PROJECT ROOT
# ------------------------------------------------

PROJECT_ROOT = "/var/jenkins_home/workspace/AI-DevOps-Pipeline/ai-projects/multi-agent-openai-cicd"

REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports")

os.makedirs(REPORTS_DIR, exist_ok=True)

fix_report = {
    "fixes_applied": []
}

# ------------------------------------------------
# FIX POM.XML
# ------------------------------------------------

pom_file = os.path.join(PROJECT_ROOT, "pom.xml")

print(f"📄 Editing: {pom_file}")

if os.path.exists(pom_file):

    with open(pom_file, "r") as f:
        pom = f.read()

    if "1.1.1" in pom:

        pom = pom.replace("1.1.1", "2.17.1")

        with open(pom_file, "w") as f:
            f.write(pom)

        print("✅ log4j version updated")

        fix_report["fixes_applied"].append(
            "Updated log4j version"
        )

# ------------------------------------------------
# FIX JAVA FILE
# ------------------------------------------------

java_file = os.path.join(
    PROJECT_ROOT,
    "src/main/java/App.java"
)

print(f"📄 Editing: {java_file}")

if os.path.exists(java_file):

    fixed_code = '''
package com.demo;

public class App {

    public static void main(String[] args) {

        System.out.println("Hello AI DevOps");

    }

}
'''

    with open(java_file, "w") as f:
        f.write(fixed_code)

    print("✅ Java syntax fixed")

    fix_report["fixes_applied"].append(
        "Fixed Java syntax"
    )

else:

    print("❌ App.java not found")

# ------------------------------------------------
# SAVE REPORT
# ------------------------------------------------

report_path = os.path.join(
    REPORTS_DIR,
    "fix_report.json"
)

with open(report_path, "w") as f:
    json.dump(fix_report, f, indent=4)

print("✅ fix_report.json generated")

print("🎉 Fix Agent Completed")
