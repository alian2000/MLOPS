import json
import os
import time

BASE_DIR = os.path.abspath(os.getcwd())

SECURITY_FILE = os.path.join(BASE_DIR, "reports/security.json")
PROJECT_FILE = os.path.join(BASE_DIR, "reports/project.json")
OUTPUT_FILE = os.path.join(BASE_DIR, "reports/ai.json")


def wait_for_file(path, timeout=5):
    for _ in range(timeout * 2):
        if os.path.exists(path):
            return True
        time.sleep(0.5)
    return False


def safe_load(file_path):
    if not wait_for_file(file_path):
        return {"status": "FAILED", "issues": ["Report missing: " + file_path]}
    with open(file_path) as f:
        return json.load(f)


project = safe_load(PROJECT_FILE)
security = safe_load(SECURITY_FILE)

final = {
    "decision": "APPROVED",
    "reasons": []
}

if project.get("status") == "FAILED":
    final["decision"] = "REJECTED"
    final["reasons"] += project.get("issues", [])

if security.get("status") == "FAILED":
    final["decision"] = "REJECTED"
    final["reasons"] += security.get("issues", [])

os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

with open(OUTPUT_FILE, "w") as f:
    json.dump(final, f, indent=4)

print("🧠 AI Decision:", final)
