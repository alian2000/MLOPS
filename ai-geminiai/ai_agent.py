import os
import sys
import time
from google import genai
from google.genai import types

# 💡 Note: Jenkins will inject this environment variable for us
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_KEY:
    print("❌ ERROR: GEMINI_API_KEY environment variable is missing!")
    sys.exit(1)

# Initialize the official Google GenAI Client
client = genai.Client(api_key=GEMINI_KEY)

# ✅ NEW CORRECT PATHS
LOG_FILE = "build.log"
JAVA_FILE = "src/main/java/App.java"
POM_FILE = "pom.xml"


def read_file(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read()
    return ""


def write_file(path, content):
    with open(path, "w") as f:
        f.write(content)


def ask_ai(log, java_code, pom):
    print("\n🤖 Analyzing build failures using Google Gemini...\n")
    
    prompt = f"""You are a DevOps AI agent.

Build failed with this error:
{log}

Java Code:
{java_code}

POM File:
{pom}

Fix all issues:
- syntax errors
- outdated dependencies

Return ONLY updated Java code and pom.xml in this exact format:

---JAVA---
<fixed java code>

---POM---
<fixed pom.xml>
"""

    # Call Gemini 2.5 Flash with a temperature of 0 for strict, deterministic code fixes
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.0
        )
    )

    return response.text


def apply_fix(ai_output):
    if "---JAVA---" in ai_output and "---POM---" in ai_output:
        java_part = ai_output.split("---JAVA---")[1].split("---POM---")[0]
        pom_part = ai_output.split("---POM---")[1]

        write_file(JAVA_FILE, java_part.strip())
        write_file(POM_FILE, pom_part.strip())

        print("✅ Gemini Fix Applied Successfully")
        return True

    print("⚠️ Gemini response formatting was invalid")
    return False


def main():
    print("🤖 AI Self-Healing Agent Started...")

    log = read_file(LOG_FILE)
    if not log:
        print("❌ build.log not found or empty")
        return

    java_code = read_file(JAVA_FILE)
    pom = read_file(POM_FILE)

    ai_output = ask_ai(log, java_code, pom)

    print("\n🤖 Gemini Response:\n", ai_output)

    apply_fix(ai_output)


if __name__ == "__main__":
    main()
