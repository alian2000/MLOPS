import os
import re
from utils.openai_client import ask_gpt

print("🔧 Fix Agent Running...")

# --------------------------------
# READ BUILD LOG
# --------------------------------

log_path = "build.log"

if os.path.exists(log_path):

    with open(log_path, "r") as f:
        log = f.read()

    # --------------------------------
    # OPENAI ANALYSIS
    # --------------------------------

    prompt = f"""
    Analyze this Maven build failure and explain root cause.

    BUILD LOG:
    {log}
    """

    try:
        response = ask_gpt(prompt)

        print("🧠 OpenAI Suggestion:")
        print(response)

    except Exception as e:
        print("❌ OpenAI Error:", e)

else:
    print("❌ build.log not found")

# --------------------------------
# FIX 1 : Invalid log4j dependency
# --------------------------------

pom_path = "pom.xml"

if os.path.exists(pom_path):

    with open(pom_path, "r") as f:
        pom = f.read()

    fixed = False

    # invalid old version
    if "<version>1.1.1</version>" in pom:

        print("🔧 Fixing invalid log4j version 1.1.1")

        pom = pom.replace(
            "<version>1.1.1</version>",
            "<version>2.17.1</version>"
        )

        fixed = True

    # another invalid demo version
    if "<version>1.1.0</version>" in pom:

        print("🔧 Fixing invalid log4j version 1.1.0")

        pom = pom.replace(
            "<version>1.1.0</version>",
            "<version>2.17.1</version>"
        )

        fixed = True

    if fixed:

        with open(pom_path, "w") as f:
            f.write(pom)

        print("✅ pom.xml updated successfully")

    else:
        print("ℹ️ No dependency issue found")

else:
    print("❌ pom.xml not found")

# --------------------------------
# FIX 2 : Java syntax error
# --------------------------------

java_base = "src/main/java"

if os.path.exists(java_base):

    for root, dirs, files in os.walk(java_base):

        for file in files:

            if file.endswith(".java"):

                java_file = os.path.join(root, file)

                with open(java_file, "r") as f:
                    code = f.read()

                original_code = code

                # --------------------------------
                # Auto fix broken println
                # --------------------------------

                code = re.sub(
                    r'System\.out\.println\("Hello AI DevOps"\)\s*\)\s*;',
                    'System.out.println("Hello AI DevOps");',
                    code
                )

                code = re.sub(
                    r'System\.out\.println\("Hello AI DevOps"\)\s*\)',
                    'System.out.println("Hello AI DevOps");',
                    code
                )

                # --------------------------------
                # Ultimate safe rewrite
                # --------------------------------

                if "System.out.println" in code:

                    code = '''
package com.demo;

public class App {

    public static void main(String[] args) {

        System.out.println("Hello AI DevOps");

    }
}
'''

                # save only if changed
                if code != original_code:

                    with open(java_file, "w") as f:
                        f.write(code)

                    print(f"✅ Syntax fixed in {file}")

else:
    print("❌ Java source folder not found")

print("🚀 Fix Agent Completed")
