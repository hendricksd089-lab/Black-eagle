import hashlib
import os
import secrets

users = {}

PASSWORD_MIN_LENGTH = 8
HASH_ITERATIONS = 600_000
generic_failure = "Error: Invalid username or password."

def hash_password(password: str, salt: bytes | None = None) -> tuple[bytes, bytes]:
    """Hashes a password using PBKDF2-SHA256 with a secure salt."""
    if salt is None:
        salt = secrets.token_bytes(16)

    pwd_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        HASH_ITERATIONS,
    )
    return pwd_hash, salt

def validate_input(username: str, password: str) -> bool:
    """Validates registration and login constraints."""
    if not username.strip() or not password.strip():
        print("Error: Username and password cannot be empty.")
        return False

    if len(password) < PASSWORD_MIN_LENGTH:
        print(f"Error: Password must be at least {PASSWORD_MIN_LENGTH} characters long.")
        return False

    return True

def register():
    print("\n---User Registration ---")
    username = input("Enter username: ").strip()
    password = input("Enter password: ")

    if not validate_input(username, password):
        return

    if username in users:
        print("Error: Username already exists.")
        return

    pwd_hash, salt = hash_password(password)
    users[username] = {
        "hash": pwd_hash,
        "salt": salt,
    }
    print("User registered successfully.!")

def login():
    print("\n---User Login ---")
    username = input("Enter username: ").strip()
    password = input("Enter password: ")

    if not username or not password:
        print(generic_failure)
        return

    if username not in users:
        print(generic_failure)
        return

    stored_data = users[username]
    stored_hash = stored_data["hash"]
    stored_salt = stored_data["salt"]

    input_hash, _ = hash_password(password, stored_salt)

    if secrets.compare_digest(input_hash, stored_hash):
        print("Login successful!")
    else:
        print(generic_failure)


if __name__ == "__main__":
    while True:
        choice = input("\n1. Register\n2. Login\n3. Exit\nChoose an option: ")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")
            
            
          
            