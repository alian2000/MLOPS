import json
import os

report = {
    "issues": []
}

# Scan build.log
with open("build.log", "r", errors="ignore") as f:
    data = f.read().lower()

if "password" in data:
    report["issues"].append("Password found in logs")

if "apikey" in data:
    report["issues"].append("API key found in logs")

# Scan Java files
for root, dirs, files in os.walk("src"):
    for file in files:
        if file.endswith(".java"):
            path = os.path.join(root, file)

            with open(path, "r", errors="ignore") as f:
                content = f.read()

                if "System.exit" in content:
                    report["issues"].append(f"{file}: System.exit used")

# Save report
with open("reports/security.json", "w") as f:
    json.dump(report, f, indent=4)

print("🔐 Security Agent Done:", report)

if report["issues"]:
    exit(1)
