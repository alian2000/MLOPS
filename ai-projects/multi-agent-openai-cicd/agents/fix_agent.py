import os
import json

print("🔧 Fix Agent Started...")

PROJECT_ROOT = "/var/jenkins_home/workspace/AI-DevOps-Pipeline/ai-projects/multi-agent-openai-cicd"

REPORTS_DIR = f"{PROJECT_ROOT}/reports"

os.makedirs(REPORTS_DIR, exist_ok=True)

fix_report = {
    "fixes_applied": []
}

# ------------------------------------------------
# FIX POM.XML
# ------------------------------------------------

pom_path = f"{PROJECT_ROOT}/pom.xml"

if os.path.exists(pom_path):

    with open(pom_path, "r") as f:
        pom = f.read()

    pom = pom.replace("1.1.1", "2.17.1")

    with open(pom_path, "w") as f:
        f.write(pom)

    print("✅ pom.xml fixed")

    fix_report["fixes_applied"].append(
        "Updated log4j version"
    )

# ------------------------------------------------
# FIX APP.JAVA
# ------------------------------------------------

java_path = f"{PROJECT_ROOT}/src/main/java/App.java"

fixed_java = '''
public class App {

    public static void main(String[] args) {

        System.out.println("Hello AI DevOps");

    }

}
'''

with open(java_path, "w") as f:
    f.write(fixed_java)

print("✅ App.java fixed")

fix_report["fixes_applied"].append(
    "Fixed Java syntax error"
)

# ------------------------------------------------
# SAVE REPORT
# ------------------------------------------------

report_path = f"{REPORTS_DIR}/fix_report.json"

with open(report_path, "w") as f:
    json.dump(fix_report, f, indent=4)

print("✅ fix_report.json created")

print("🎉 Fix Agent Completed")
