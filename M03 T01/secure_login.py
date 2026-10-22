import hashlib
import hmac
import secrets
users = {}


def hash_password(password):
    salt = secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac("sha256", password, salt, 600_000)
    return salt.hex() + "$" + digest.hex()


def verify_password(password, stored_hash):
    try:
        salt_hex, digest_hex = stored_hash.split("$", 1)
        salt = bytes.fromhex(salt_hex)
        expected = bytes.fromhex(digest_hex)
    except (AttributeError, ValueError):
        return False

    actual = hashlib.pbkdf2_hmac("sha256", password, salt, 600_000)
    return hmac.compare_digest(actual, expected)


def register():
    while True:
        username = input("Enter username: ").strip()
        if not username:
            print("Username cannot be empty. Please try again.")
            continue
        if username in users:
            print("Username already exists. Please choose another.")
            continue
        break

    while True:
        password = input("Enter password (minimum 6 characters): ")
        if len(password) < 6:
            print("Password must be at least 6 characters long.")
            continue
        break

    users[username] = hash_password(password.encode("utf-8"))
    print("User registered!")


def login():
    username = input("Username: ").strip()
    password = input("Password: ").encode("utf-8")

    if not username or not password:
        print("Invalid credentials.")
        return

    stored_hash = users.get(username)
    if stored_hash and verify_password(password, stored_hash):
        print("Login successful!")
    else:
        print("Invalid credentials.")


def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Select an option: ").strip()
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
            
                    
