import os
from utils.openai_client import ask_gpt

print("🔧 Fix Agent Running...")

# --------------------------------
# FIX 1 : pom.xml dependency
# --------------------------------

pom_path = "pom.xml"

if os.path.exists(pom_path):

    with open(pom_path, "r") as f:
        pom = f.read()

    if "<version>1.1.1</version>" in pom:

        print("🔧 Fixing invalid log4j version...")

        pom = pom.replace(
            "<version>1.1.1</version>",
            "<version>2.17.1</version>"
        )

        with open(pom_path, "w") as f:
            f.write(pom)

        print("✅ pom.xml fixed")

# --------------------------------
# FIX 2 : Java syntax error
# --------------------------------

java_base = "src/main/java"

for root, dirs, files in os.walk(java_base):

    for file in files:

        if file.endswith(".java"):

            java_file = os.path.join(root, file)

            with open(java_file, "r") as f:
                code = f.read()

            # detect wrong syntax
            if 'System.out.println("Hello AI DevOps");)' in code:

                print(f"🔧 Fixing syntax in {file}")

                fixed = code.replace(
                    'System.out.println("Hello AI DevOps");)',
                    'System.out.println("Hello AI DevOps");'
                )

                with open(java_file, "w") as f:
                    f.write(fixed)

                print(f"✅ Syntax fixed in {file}")

print("✅ Fix Agent Completed")
