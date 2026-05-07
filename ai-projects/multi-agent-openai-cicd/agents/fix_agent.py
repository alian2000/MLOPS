import json
import os

print("🔧 Fix Agent Running...")

fixes = []

# -----------------------------
# FIX pom.xml
# -----------------------------

with open("pom.xml", "r") as f:
    pom = f.read()

updated = pom.replace("1.1.1", "2.17.1")
updated = updated.replace("1.1.0", "2.17.1")

with open("pom.xml", "w") as f:
    f.write(updated)

fixes.append("Updated log4j dependency")

print("✅ pom.xml fixed")

# -----------------------------
# FIX Java syntax
# -----------------------------

java_file = "src/main/java/com/demo/App.java"

fixed_java = '''package com.demo;

public class App {

    public static void main(String[] args) {

        System.out.println("Hello AI DevOps");

    }
}
'''

with open(java_file, "w") as f:
    f.write(fixed_java)

fixes.append("Fixed Java syntax error")

print("✅ Java syntax fixed")

# -----------------------------
# FINAL REPORT
# -----------------------------

report = {
    "status": "FIX_APPLIED",
    "fixes": fixes
}

with open("reports/fix_report.json", "w") as f:
    json.dump(report, f, indent=4)

print(report)
