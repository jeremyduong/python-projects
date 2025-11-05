#Password Strength Checker

password = input("Enter a password: ")

if len(password) < 8:
    print("❌ Too short! Must be at least 8 characters.")
elif password.isdigit() or password.isalpha():
    print("⚠️ Try mixing letters and numbers for a stronger password.")
elif password.islower() or password.isupper():
    print("⚠️ Try mixing uppercase and lowercase letters.")
else:
    print("✅ Strong password!")
    