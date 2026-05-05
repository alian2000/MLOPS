# -----------------------------
# 🔥 FIX 2: Java syntax error (SMART FIX)
# -----------------------------
java_base = f"{BASE}/src/main/java"

fixed = False

for root, dirs, files in os.walk(java_base):
    for file in files:
        if file.endswith(".java"):
            java_file = os.path.join(root, file)

            with open(java_file, "r") as f:
                code = f.read()

            original = code

            # 🔥 Case 1: extra ')' after semicolon
            code = code.replace(
                'System.out.println("Hello AI DevOps");)',
                'System.out.println("Hello AI DevOps");'
            )

            # 🔥 Case 2: missing semicolon
            code = code.replace(
                'System.out.println("Hello AI DevOps")',
                'System.out.println("Hello AI DevOps");'
            )

            if code != original:
                with open(java_file, "w") as f:
                    f.write(code)

                print(f"✅ Fixed Java syntax in: {java_file}")
                fixed = True

if not fixed:
    print("ℹ️ No Java fixes applied")
