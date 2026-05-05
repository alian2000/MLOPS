import os
import re

BASE = "ai-projects/multi-agents-cicd-project"

print("🔧 Fix Agent Running...")

# -----------------------------
# 🔥 FIX 1: pom.xml
# -----------------------------
pom_file = f"{BASE}/pom.xml"

if os.path.exists(pom_file):
    with open(pom_file, "r") as f:
        content = f.read()

    new_content = re.sub(
        r'(<artifactId>log4j-core</artifactId>\s*<version>)(.*?)(</version>)',
        r'\g<1>2.17.2\g<3>',
        content
    )

    if new_content != content:
        with open(pom_file, "w") as f:
            f.write(new_content)
        print("✅ Fixed: log4j version")
    else:
        print("ℹ️ No pom.xml changes needed")

# -----------------------------
# 🔥 FIX 2: Java syntax error (AUTO DETECT FILE)
# -----------------------------
java_base = f"{BASE}/src/main/java"

fixed = False

for root, dirs, files in os.walk(java_base):
    for file in files:
        if file.endswith(".java"):
            java_file = os.path.join(root, file)

            with open(java_file, "r") as f:
                code = f.read()

            # detect missing semicolon
            if 'System.out.println("Hello AI DevOps"' in code:
                print(f"🔍 Found issue in: {java_file}")

                code = code.replace(
                    'System.out.println("Hello AI DevOps"',
                    'System.out.println("Hello AI DevOps");'
                )

                with open(java_file, "w") as f:
                    f.write(code)

                print(f"✅ Fixed: Java syntax in {file}")
                fixed = True

if not fixed:
    print("ℹ️ No Java fixes applied")

print("🔧 Fix Agent completed")
