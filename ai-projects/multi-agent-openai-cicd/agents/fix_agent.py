import os
import re

print("🔧 Fixing pom.xml dependency issue...")

pom_path = "pom.xml"

if os.path.exists(pom_path):

    with open(pom_path, "r") as f:
        pom = f.read()

    print("📄 BEFORE FIX:")
    print(pom)

    # FORCE REPLACE INVALID LOG4J VERSION
    pom = pom.replace(
        "1.1.1",
        "2.17.1"
    )

    pom = pom.replace(
        "1.1.0",
        "2.17.1"
    )

    with open(pom_path, "w") as f:
        f.write(pom)

    print("✅ pom.xml UPDATED")

    # VERIFY UPDATED CONTENT
    with open(pom_path, "r") as f:
        verify = f.read()

    print("📄 AFTER FIX:")
    print(verify)

else:
    print("❌ pom.xml not found")
