from utils.openai_client import ask_gpt

report = open("reports/combined.txt").read()

prompt = f"""
Based on this report, decide:
APPROVE or REJECT build.

Explain shortly.

REPORT:
{report}
"""

decision = ask_gpt(prompt)

print("🧠 AI Decision:")
print(decision)

if "REJECT" in decision:
    open("build_failed", "w").write("fail")
