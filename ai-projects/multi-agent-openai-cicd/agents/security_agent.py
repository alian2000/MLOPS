from utils.openai_client import ask_gpt

pom = open("pom.xml").read()

prompt = f"""
Check this pom.xml for:
- vulnerable dependencies
- invalid versions

Return issues clearly.

POM:
{pom}
"""

result = ask_gpt(prompt)

print("🔐 Security Report:")
print(result)
