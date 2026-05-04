# fix_agent.py

import os
import re

BASE = "ai-projects/multi-agents-cicd-project"

print("🔧 Fix Agent Running...")

pom_file = f"{BASE}/pom.xml"

if os.path.exists(pom_file):

    with open(pom_file, "r") as f:
        content = f.read()

    # 🔥 replace ANY log4j version with safe version
    new_content = re.sub(
        r'<artifactId>log4j-core</artifactId>\s*<version>.*?</version>',
        '<artifactId>log4j-core</artifactId>\n      <version>2.17.2</version>',
        content
    )

    if new_content != content:
        with open(pom_file, "w") as f:
            f.write(new_content)

        print("✅ Fixed: log4j version upgraded to 2.17.2")

    else:
        print("ℹ️ No changes needed")
