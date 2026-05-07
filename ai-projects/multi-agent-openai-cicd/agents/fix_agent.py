import os
import json
from openai import OpenAI

# -----------------------------------
# CONFIG
# -----------------------------------

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

BASE_PATH = "ai-devops-maven"

LOG_FILE = f"{BASE_PATH}/build.log"
JAVA_FILE = f"{BASE_PATH}/src/main/java/App.java"
POM_FILE = f"{BASE_PATH}/pom.xml"

REPORT_DIR = "reports"

# -----------------------------------
# HELPERS
# -----------------------------------

def read_file(path):

    if os.path.exists(path):

        with open(path, "r") as f:
            return f.read()

    return ""


def write_file(path, content):

    with open(path, "w") as f:
        f.write(content)


# -----------------------------------
# ASK OPENAI
# -----------------------------------

def ask_ai(log, java_code, pom):

    prompt = f"""
You are an autonomous DevOps AI Agent.

A Maven build failed.

Analyze the logs carefully and FIX ALL ISSUES.

Possible issues:
- Java syntax errors
- Invalid dependencies
- Maven build failures
- Compilation errors

BUILD LOG:
{log}

JAVA FILE:
{java_code}

POM.XML:
{pom}

IMPORTANT:
1. Return COMPLETE updated Java code
2. Return COMPLETE updated pom.xml
3. Do NOT explain anything
4. Return ONLY in this format

---JAVA---
<complete fixed java code>

---POM---
<complete fixed pom.xml>
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


# -----------------------------------
# APPLY FIX
# -----------------------------------

def apply_fix(ai_output):

    if "---JAVA---" not in ai_output or "---POM---" not in ai_output:

        print("❌ Invalid AI response format")
        return False

    try:

        java_part = ai_output.split("---JAVA---")[1].split("---POM---")[0]

        pom_part = ai_output.split("---POM---")[1]

        print("📄 Updating App.java...")
        write_file(JAVA_FILE, java_part.strip())

        print("📄 Updating pom.xml...")
        write_file(POM_FILE, pom_part.strip())

        return True

    except Exception as e:

        print(f"❌ Failed applying fix: {e}")
        return False


# -----------------------------------
# GENERATE REPORT
# -----------------------------------

def generate_report():

    os.makedirs(REPORT_DIR, exist_ok=True)

    report = {
        "status": "fixed",
        "updated_files": [
            JAVA_FILE,
            POM_FILE
        ]
    }

    with open(f"{REPORT_DIR}/fix_report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("✅ fix_report.json generated")


# -----------------------------------
# GITHUB PUSH
# -----------------------------------

def push_changes():

    print("📤 Pushing AI fixes to GitHub...")

    os.system('''
    git config user.email "jenkins@ai.com"

    git config user.name "AI Fix Agent"

    git checkout main || true

    git add .

    git commit -m "[AI] Auto Fix Applied" || true

    git push origin HEAD:main --force
    ''')

    print("✅ GitHub updated")


# -----------------------------------
# MAIN
# -----------------------------------

def main():

    print("🤖 AI Agent Started...")

    log = read_file(LOG_FILE)

    if not log:

        print("❌ build.log missing")
        return

    java_code = read_file(JAVA_FILE)

    pom = read_file(POM_FILE)

    print("🧠 Asking OpenAI for fixes...")

    ai_output = ask_ai(log, java_code, pom)

    print("\n🤖 AI RESPONSE:\n")
    print(ai_output)

    fixed = apply_fix(ai_output)

    if fixed:

        print("✅ AI Fix Applied")

        generate_report()

        push_changes()

        print("🎉 AI Self-Healing Completed")

    else:

        print("❌ AI Fix Failed")


if __name__ == "__main__":
    main()
