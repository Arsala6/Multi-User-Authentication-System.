# 🔐 Multi-User Authentication System (CLI)

## 📌 Project Overview
This project is a Command-Line Interface (CLI) based Multi-User Authentication System developed in Python.  
It allows multiple users to securely register, login, and manage their accounts using JSON-based data storage.

The system simulates a real-world login/signup system with proper validation, password security, and error handling.

---

## 🚀 Features

### 🔹 Core Features
- User Registration (Username, Email, Password)
- User Login (using Username or Email)
- Secure password storage using hashing (SHA-256)
- JSON-based data storage
- Input validation and error handling

---

### 🔹 Security Features
- Passwords are hashed before storing (no plain text)
- Duplicate username and email prevention
- Case-sensitive authentication
- Login attempt limit (maximum 3 tries)

---

### 🔹 Validation Rules
- Email must follow proper format (using regex)
- Password must:
  - Be at least 8 characters long
  - Contain at least one letter
  - Contain at least one number

---

### 🌟 Bonus Features
- Password Reset functionality
- Account Deletion
- Login attempt restriction (security feature)

---

## 🛠 Technologies Used
- Python
- JSON (for data storage)
- hashlib (for password hashing)
- re (for email validation)

---

## ▶️ How to Run

### 🔹 Step 1: Clone or Download Project
Download the project folder or clone from GitHub.

### 🔹 Step 2: Run the Program
```bash
python auth_system.py
👩‍💻 Author
Name: Arsala Baloch
Project: Multi-User Authentication System
