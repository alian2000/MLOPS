import os
import re

print("🔧 Checking pom.xml...")

BASE_DIR = os.getcwd()

pom_path = os.path.join(BASE_DIR, "pom.xml")

print("📂 Current Path:", BASE_DIR)
print("📂 pom.xml:", pom_path)

if os.path.exists(pom_path):

    print("✅ pom.xml found")

    with open(pom_path, "r") as f:
        pom = f.read()

    print("📄 Existing pom.xml:")
    print(pom)

    updated_pom = pom.replace(
        "<version>1.1.1</version>",
        "<version>2.17.1</version>"
    )

    updated_pom = updated_pom.replace(
        "<version>1.1.0</version>",
        "<version>2.17.1</version>"
    )

    if pom != updated_pom:

        with open(pom_path, "w") as f:
            f.write(updated_pom)

        print("✅ log4j version updated successfully")

        # VERIFY AGAIN
        with open(pom_path, "r") as f:
            verify = f.read()

        print("📄 Updated pom.xml:")
        print(verify)

    else:

        print("⚠️ No dependency replacement happened")

else:

    print("❌ pom.xml NOT found")
