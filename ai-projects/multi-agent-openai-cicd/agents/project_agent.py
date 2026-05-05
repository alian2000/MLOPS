from utils.openai_client import ask_gpt

log = open("build.log").read()

prompt = f"""
Analyze this Maven build log.
Find:
- error type
- root cause

LOG:
{log}
"""

result = ask_gpt(prompt)

print("📊 Project Agent Report:")
print(result)
