import os
from utils.openai_client import ask_gpt

report_path = "reports/combined.txt"

if not os.path.exists(report_path):
    print("❌ combined.txt not found")
    exit(1)

report = open(report_path).read()

prompt = f"""
Based on this report decide:

APPROVE or REJECT build.

REPORT:
{report}
"""

decision = ask_gpt(prompt)

print("🧠 AI Decision:")
print(decision)

if "REJECT" in decision.upper():
    open("build_failed", "w").write("failed")
