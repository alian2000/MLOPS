import os
from utils.openai_client import ask_gpt

BASE = os.getcwd()

print("🔧 Fix Agent Running...")

# -----------------------------
# READ BUILD LOG
# -----------------------------
log_path = "build.log"

if not os.path.exists(log_path):
    print("❌ build.log not found")
    exit(1)

log = open(log_path).read()

# -----------------------------
# OPENAI ANALYSIS
# -----------------------------
prompt = f"""
Analyze this Maven build log.

If dependency version is invalid,
suggest correct stable version.

BUILD LOG:
{log}
"""

response = ask_gpt(prompt)

print("🧠 OpenAI Suggestion:")
print(response)

# -----------------------------
# AUTO FIX pom.xml
# -----------------------------
pom_path = "pom.xml"

if os.path.exists(pom_path):

    with open(pom_path, "r") as f:
        pom = f.read()

    # invalid log4j version fix
    if "1.1.1" in pom:

        print("🔧 Fixing invalid log4j version...")

        pom = pom.replace(
            "<version>1.1.1</version>",
            "<version>2.17.1</version>"
        )

        with open(pom_path, "w") as f:
            f.write(pom)

        print("✅ pom.xml updated")

    else:
        print("ℹ️ No invalid dependency found")

else:
    print("❌ pom.xml not found")

print("✅ Fix Agent completed")
