import os
import re

BASE = "ai-projects/multi-agents-cicd-project"

print("🔧 Fix Agent Running...")

# -----------------------------
# 🔥 FIX 1: pom.xml dependency
# -----------------------------
pom_file = f"{BASE}/pom.xml"

if os.path.exists(pom_file):
    with open(pom_file, "r") as f:
        content = f.read()

    original = content

    # Fix ANY log4j version → safe version
    content = re.sub(
        r'(<artifactId>log4j-core</artifactId>\s*<version>)(.*?)(</version>)',
        r'\g<1>2.17.2\g<3>',
        content
    )

    if content != original:
        with open(pom_file, "w") as f:
            f.write(content)

        print("✅ Fixed: log4j dependency upgraded to 2.17.2")
    else:
        print("ℹ️ No pom.xml changes needed")

# -----------------------------
# 🔥 FIX 2: Java syntax error
# -----------------------------
java_file = f"{BASE}/src/main/java/com/demo/App.java"

if os.path.exists(java_file):
    with open(java_file, "r") as f:
        code = f.read()

    original = code

    # Fix missing semicolon (demo case)
    code = code.replace(
        'System.out.println("Hello AI DevOps"',
        'System.out.println("Hello AI DevOps");'
    )

    if code != original:
        with open(java_file, "w") as f:
            f.write(code)

        print("✅ Fixed: Java syntax error corrected")
    else:
        print("ℹ️ No Java changes needed")

print("🔧 Fix Agent completed")
