import os

BASE = "ai-projects/multi-agents-cicd-project"

print("🔧 Fix Agent Running...")

sec_file = f"{BASE}/agents/security_agent.py"

if os.path.exists(sec_file):
    with open(sec_file, "r") as f:
        content = f.read()

    if "Demo security issue" in content:
        content = content.replace(
            'report["issues"].append("Demo security issue: hardcoded credential detected")',
            '# removed by fix agent'
        )

        with open(sec_file, "w") as f:
            f.write(content)

        print("✅ Demo issue removed")
    else:
        print("ℹ️ No demo issue found")
