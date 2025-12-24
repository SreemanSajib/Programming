
import hashlib
import os

FILE = "credentials.txt"

def md5_hex(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()

def load_users():
    users = []
    if not os.path.exists(FILE):
        return users
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            u, h = s.split(";", 1)
            users.append((u, h))
    return users

def save_users(users):
    with open(FILE, "w", encoding="utf-8") as f:
        for u, h in users:
            f.write(f"{u};{h}\n")

def register_user():
    username = input("Insert username: ")
    password = input("Insert password: ")
    users = load_users()
    users.append((username, md5_hex(password)))
    save_users(users)
    print("User registration completed!")

def authenticate():
    username = input("Insert username: ")
    password = input("Insert password: ")
    users = load_users()
    hashed = md5_hex(password)
    for idx, (u, h) in enumerate(users):
        if u == username and h == hashed:
            return idx, u
    return None, None

def user_menu(user_id, username):
    while True:
        print("\nUser menu:")
        print("1 - View profile")
        print("2 - Change password")
        print("0 - Logout")
        choice = input("Your choice: ")

        if choice == "1":
            print(f"Profile ID {user_id} - {username}")

        elif choice == "2":
            new_pw = input("Insert new password: ")
            users = load_users()
            users[user_id] = (username, md5_hex(new_pw))
            save_users(users)
            print("Password changed!")

        elif choice == "0":
            print("Logging out...")
            break

def main():
    print("Program starting.")

    while True:
        print("\nOptions:")
        print("1 - Login")
        print("2 - Register")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            user_id, username = authenticate()
            if username is None:
                print("Authentication failed!")
            else:
                print("Authentication successful!")
                user_menu(user_id, username)

        elif choice == "2":
            register_user()

        elif choice == "0":
            print("Exiting program.")
            break

    print("\nProgram ending.")

if __name__ == "__main__":
    main()
