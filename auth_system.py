import json
import os
import hashlib
import re

DATA_FILE = "users.json"

# ------------------ FILE HANDLING ------------------
def load_users():
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                return json.load(f)
    except:
        print("Error loading file")
    return []

def save_users(users):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(users, f, indent=4)
    except:
        print("Error saving file")

# ------------------ VALIDATION ------------------
def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validate_password(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isalpha() for char in password):
        return False
    return True

# ------------------ HASHING ------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ------------------ REGISTER ------------------
def register():
    users = load_users()

    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    # Check duplicates
    for user in users:
        if user["username"] == username:
            print("❌ Username already exists")
            return
        if user["email"] == email:
            print("❌ Email already exists")
            return

    if not validate_email(email):
        print("❌ Invalid email format")
        return

    if not validate_password(password):
        print("❌ Weak password (min 8 chars, include letters & numbers)")
        return

    hashed = hash_password(password)

    users.append({
        "username": username,
        "email": email,
        "password": hashed
    })

    save_users(users)
    print("✅ Registration successful")

# ------------------ LOGIN ------------------
def login():
    users = load_users()

    identifier = input("Enter username or email: ")
    password = input("Enter password: ")

    hashed = hash_password(password)

    attempts = 3

    while attempts > 0:
        for user in users:
            if (user["username"] == identifier or user["email"] == identifier) and user["password"] == hashed:
                print("✅ Login successful")
                return

        attempts -= 1
        if attempts == 0:
            print("❌ Too many failed attempts")
            return

        print(f"❌ Incorrect credentials. Attempts left: {attempts}")
        password = input("Re-enter password: ")
        hashed = hash_password(password)

# ------------------ RESET PASSWORD ------------------
def reset_password():
    users = load_users()
    email = input("Enter your email: ")

    for user in users:
        if user["email"] == email:
            new_pass = input("Enter new password: ")

            if not validate_password(new_pass):
                print("❌ Weak password")
                return

            user["password"] = hash_password(new_pass)
            save_users(users)
            print("✅ Password updated")
            return

    print("❌ Email not found")

# ------------------ DELETE ACCOUNT ------------------
def delete_account():
    users = load_users()
    username = input("Enter username to delete: ")

    new_users = [u for u in users if u["username"] != username]

    if len(new_users) == len(users):
        print("❌ User not found")
    else:
        save_users(new_users)
        print("🗑 Account deleted")

# ------------------ MENU ------------------
def main():
    while True:
        print("\n🔐 AUTHENTICATION SYSTEM")
        print("1. Register")
        print("2. Login")
        print("3. Reset Password")
        print("4. Delete Account")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            reset_password()
        elif choice == "4":
            delete_account()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

# ------------------ RUN ------------------
if __name__ == "__main__":
    main()