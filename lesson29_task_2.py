users = {}

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users:
        print("User already exists")
    else:
        hashed_password = hash(password)
        users[username] = hashed_password
        print("User registered successfully")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username not in users:
        print("User does not exist")
    else:
        hashed_password = hash(password)
        if hashed_password == users[username]:
            print("User logged in successfully")
        else:
            print("Incorrect password")

def main():
    while True:
        print(f"What do you want to do:\n1. Register\n2. Login\n3. Exit")
        choice = input("Make your choice, please: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Incorrect value")
        print(users)

if __name__ == "__main__":
    main()





