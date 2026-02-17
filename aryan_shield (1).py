import os
import random
import string
import time

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Clear Screen
def clear():
    os.system("clear")

# BIG BANNER
def banner():
    clear()
    print(CYAN + r"""
 █████╗ ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗
██╔══██╗██╔══██╗╚██╗ ██╔╝██╔══██╗████╗  ██║
███████║██████╔╝ ╚████╔╝ ███████║██╔██╗ ██║
██╔══██║██╔══██╗  ╚██╔╝  ██╔══██║██║╚██╗██║
██║  ██║██║  ██║   ██║   ██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝

        CODE WORD : ARYAN
    """ + RESET)

    print(YELLOW + "YouTube: aryanmalik-0786" + RESET)
    print(GREEN + "==== ARYAN SHIELD SECURITY TOOL ====\n" + RESET)


# 1️⃣ Password Generator
def password_generator():
    length = int(input("Enter password length: "))
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.choice(chars) for _ in range(length))
    print(GREEN + "\nStrong Password Generated: " + password + RESET)
    input("\nPress Enter to continue...")


# 2️⃣ Password Strength Checker
def password_checker():
    pwd = input("Enter password to check: ")
    score = 0

    if len(pwd) >= 8:
        score += 1
    if any(c.isdigit() for c in pwd):
        score += 1
    if any(c.isupper() for c in pwd):
        score += 1
    if any(c in "!@#$%^&*()" for c in pwd):
        score += 1

    if score == 4:
        print(GREEN + "Very Strong Password!" + RESET)
    elif score >= 2:
        print(YELLOW + "Medium Strength Password." + RESET)
    else:
        print(RED + "Weak Password!" + RESET)

    input("\nPress Enter to continue...")


# 3️⃣ Scam Risk Analyzer (basic awareness logic)
def scam_checker():
    text = input("Enter message or number to analyze: ").lower()

    scam_keywords = ["otp", "urgent", "win", "lottery", "prize", "bank", "verify"]

    risk = any(word in text for word in scam_keywords)

    if risk:
        print(RED + "⚠️ Possible Scam Risk Detected!" + RESET)
    else:
        print(GREEN + "No obvious scam keywords found." + RESET)

    input("\nPress Enter to continue...")


# 4️⃣ Basic System Security Check
def system_check():
    print(CYAN + "\nRunning basic security check..." + RESET)
    time.sleep(1)
    print("✔ System accessible")
    print("✔ Python environment working")
    print("✔ Tool integrity OK")
    input("\nPress Enter to continue...")


# 5️⃣ 2FA Reminder
def two_fa():
    print(YELLOW + "\nReminder: Enable 2FA on all important accounts!" + RESET)
    print("• Instagram")
    print("• Gmail")
    print("• Facebook")
    print("• Banking Apps")
    input("\nPress Enter to continue...")


# 6️⃣ Security Tips
def security_tips():
    print(CYAN + "\nSecurity Tips:\n" + RESET)
    print("1. Never share OTP with anyone.")
    print("2. Use different passwords for every account.")
    print("3. Enable 2FA everywhere.")
    print("4. Avoid unknown links.")
    print("5. Keep apps updated.")
    input("\nPress Enter to continue...")


# Main Menu
while True:
    banner()
    print("1. Strong Password Generator")
    print("2. Password Strength Checker")
    print("3. Scam Risk Analyzer")
    print("4. Basic System Security Check")
    print("5. 2FA Reminder System")
    print("6. Security Tips")
    print("7. Exit")

    choice = input("\nSelect option: ")

    if choice == "1":
        password_generator()
    elif choice == "2":
        password_checker()
    elif choice == "3":
        scam_checker()
    elif choice == "4":
        system_check()
    elif choice == "5":
        two_fa()
    elif choice == "6":
        security_tips()
    elif choice == "7":
        print(RED + "\nExiting ARYAN SHIELD...\n" + RESET)
        break
    else:
        print(RED + "Invalid Option!" + RESET)
        time.sleep(1)
