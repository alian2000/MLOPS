import os
import sys
import time
from google import genai
from google.genai import types

# 🎨 Jenkins ANSI Color Palette Configurations
class Colors:
    PURPLE    = '\033[1;35m'  # Bold Magenta/Purple for GEMINI branding
    TEAL      = '\033[1;36m'   # Fixed typo (removed extra 'm') -> Clean Cyan/Teal
    GREEN     = '\033[1;32m'  # Success indicator
    RED       = '\033[1;31m'  # Failure/Error indicator
    YELLOW    = '\033[1;33m'  # Warning indicator
    BOLD      = '\033[1m'     # Bold white
    RESET     = '\033[0m'     # Reset color back to default

# 🔐 Extract the credential injected by the Jenkins environment
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_KEY:
    print(f"{Colors.RED}❌ ERROR: GEMINI_API_KEY environment variable is missing!{Colors.RESET}")
    sys.exit(1)

# Initialize the official Google GenAI Client
client = genai.Client(api_key=GEMINI_KEY)

# 📂 Corrected Relative Paths
LOG_FILE = "build.log"
JAVA_FILE = "src/main/java/App.java"
POM_FILE = "pom.xml"


def read_file(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read()
    return ""


def write_file(path, content):
    with open(path, "w") as f:
        f.write(content)


def ask_ai(log, java_code, pom):
    print(f"\n{Colors.PURPLE}╔════════════════════════════════════════════════════════════╗")
    print(f"║ 🤖  Initializing Generative Self-Healing Engine via GEMINI ║")
    print(f"╚════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    prompt = f"""You are a DevOps AI agent.

Build failed with this error:
{log}

Java Code:
{java_code}

POM File:
{pom}

Fix all issues:
- syntax errors
- outdated dependencies

Return ONLY updated Java code and pom.xml in this exact format:

---JAVA---
<fixed java code>

---POM---
<fixed pom.xml>
"""

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.0
        )
    )

    return response.text


def print_boxed_output(title, text_content):
    """Wraps text inside a clean, dynamic ASCII border box"""
    lines = text_content.strip().split('\n')
    box_width = max(max(len(line) for line in lines), 60)
    
    print(f"{Colors.TEAL}╔═ {Colors.PURPLE}{Colors.BOLD}{title}{Colors.TEAL} " + "═" * (box_width - len(title) - 2) + "╗")
    for line in lines:
        padding = " " * (box_width - len(line))
        print(f"║ {Colors.RESET}{line}{Colors.TEAL}{padding} ║")
    print(f"╚" + "═" * (box_width + 2) + f"╝{Colors.RESET}")


def print_comparison_panel(filename, original, fixed):
    """Prints a clear Before vs Replaced With comparison dashboard"""
    print(f"{Colors.BOLD}🔍 Code modifications detected in: {Colors.PURPLE}{filename}{Colors.RESET}")
    print(f"{Colors.RED}❌ BEFORE (Broken Code):{Colors.RESET}")
    print(f"{Colors.RED}------------------------------------------------------------{Colors.RESET}")
    print(original.strip())
    print(f"{Colors.RED}------------------------------------------------------------{Colors.RESET}")
    print(f"{Colors.GREEN}👉 REPLACED WITH (Gemini Clean Code):{Colors.RESET}")
    print(f"{Colors.GREEN}------------------------------------------------------------{Colors.RESET}")
    print(fixed.strip())
    print(f"{Colors.GREEN}------------------------------------------------------------{Colors.RESET}\n")


def apply_fix(original_java, original_pom, ai_output):
    if "---JAVA---" in ai_output and "---POM---" in ai_output:
        java_part = ai_output.split("---JAVA---")[1].split("---POM---")[0].strip()
        pom_part = ai_output.split("---POM---")[1].strip()

        # 📊 Print the comparison panel showing what changed before overwriting the files
        print(f"\n{Colors.PURPLE}✨ [GEMINI SELF-HEALING DIFFERENCE ANALYSIS] ✨{Colors.RESET}\n")
        
        if original_java.strip() != java_part:
            print_comparison_panel("src/main/java/App.java", original_java, java_part)
            
        if original_pom.strip() != pom_part:
            print_comparison_panel("pom.xml", original_pom, pom_part)

        # Write fixed files to node disk storage
        write_file(JAVA_FILE, java_part)
        write_file(POM_FILE, pom_part)

        print(f"\n{Colors.PURPLE}✨ [GEMINI FINAL REPOSITORY SNAPSHOTS] ✨{Colors.RESET}\n")
        print_boxed_output("FIXED JAVA REPOSITORY CODE", java_part)
        print("\n")
        print_boxed_output("FIXED MAVEN DEPENDENCY POM", pom_part)

        print(f"\n{Colors.GREEN}✅ {Colors.PURPLE}{Colors.BOLD}GEMINI{Colors.GREEN} Code Correction Layer Applied Successfully!{Colors.RESET}")
        return True

    print(f"\n{Colors.YELLOW}⚠️ {Colors.PURPLE}{Colors.BOLD}GEMINI{Colors.YELLOW} response formatting was invalid or empty.{Colors.RESET}")
    return False


def main():
    print(f"{Colors.BOLD}🤖 AI Self-Healing Agent Booting Up...{Colors.RESET}")

    log = read_file(LOG_FILE)
    if not log:
        print(f"{Colors.RED}❌ build.log not found or empty{Colors.RESET}")
        return

    # Capture original file states before changes are made
    original_java = read_file(JAVA_FILE)
    original_pom = read_file(POM_FILE)

    ai_output = ask_ai(log, original_java, original_pom)
    apply_fix(original_java, original_pom, ai_output)


if __name__ == "__main__":
    main()
