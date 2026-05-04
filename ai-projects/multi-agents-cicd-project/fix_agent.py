BASE = "ai-projects/multi-agents-cicd-project"

print("🔧 Fixing pom.xml...")

pom = f"{BASE}/pom.xml"

with open(pom, "r") as f:
    data = f.read()

if "2.14.1" in data:
    data = data.replace("2.14.1", "2.17.2")

    with open(pom, "w") as f:
        f.write(data)

    print("✅ Fixed vulnerable dependency")
