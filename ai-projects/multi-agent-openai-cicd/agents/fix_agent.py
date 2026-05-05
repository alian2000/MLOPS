from utils.openai_client import ask_gpt

log = open("build.log").read()

prompt = f"""
Fix the issue from this build log.

Return:
1. corrected code
2. file name

LOG:
{log}
"""

fix = ask_gpt(prompt)

print("🔧 Fix Suggestion:")
print(fix)

# simple demo write (you can improve parsing)
with open("AUTO_FIX.txt", "w") as f:
    f.write(fix)
