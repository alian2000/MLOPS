import os
import json
from openai import OpenAI

# ------------------------------------------------
# CONFIG
# ------------------------------------------------

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

BASE_PATH = os.getcwd()

LOG_FILE = f"{BASE_PATH}/build.log"

JAVA_FILE = f"{BASE_PATH}/src/main/java/App.java"

POM_FILE = f"{BASE_PATH}/pom.xml"

REPORT_DIR = f"{BASE_PATH}/reports"

# ------------------------------------------------
# READ FILE
# ------------------------------------------------

def read_file(path):

    if os.path.exists(path):

        with open(path, "r") as f:
            return f.read()

    return ""

# ------------------------------------------------
# WRITE FILE
# ------------------------------------------------

def write_file(path, content):

    with open(path, "w") as f:
        f.write(content)

# ------------------------------------------------
# ASK OPENAI
# ------------------------------------------------

def ask_openai(log, java_code, pom):

    prompt = f"""
You are an autonomous DevOps AI Agent.

A Maven build failed.

Fix ALL issues automatically.

Possible issues:
- Java syntax error
- Invalid dependency
- Compilation error
- Maven failure

BUILD LOG:
{log}

JAVA FILE:
{java_code}

POM.XML:
{pom}

IMPORTANT:
Return ONLY this format.

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

# ------------------------------------------------
# APPLY FIX
# ------------------------------------------------

def apply_fix(ai_output):

    if "---JAVA---" not in ai_output:

        print("❌ Invalid AI response")
        return False

    if "---POM---" not in ai_output:

        print("❌ Invalid AI response")
        return False

    try:

        java_code = ai_output.split(
            "---JAVA---"
        )[1].split(
            "---POM---"
        )[0]

        pom_code = ai_output.split(
            "---POM---"
        )[1]

        print("📄 Updating App.java")

        write_file(JAVA_FILE, java_code.strip())

        print("📄 Updating pom.xml")

        write_file(POM_FILE, pom_code.strip())

        return True

    except Exception as e:

        print(f"❌ Error applying fix: {e}")

        return False

# ------------------------------------------------
# REPORT
# ------------------------------------------------

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

# ------------------------------------------------
# MAIN
# ------------------------------------------------

def main():

    print("🤖 Fix Agent Started...")

    log = read_file(LOG_FILE)

    if not log:

        print("❌ build.log missing")
        return

    java_code = read_file(JAVA_FILE)

    pom = read_file(POM_FILE)

    print("🧠 Asking OpenAI for fixes...")

    ai_output = ask_openai(log, java_code, pom)

    print("\n🤖 AI RESPONSE:\n")

    print(ai_output)

    fixed = apply_fix(ai_output)

    if fixed:

        print("✅ AI Fix Applied")

        generate_report()

        print("🎉 Self-Healing Completed")

    else:

        print("❌ Fix failed")


if __name__ == "__main__":
    main()
