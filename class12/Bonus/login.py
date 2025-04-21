def login(username, password):
    users = {
        "user1": "password123",
        "user2": "mypassword",
        "admin": "adminpass"
    }
    if username in users and users[username] == password:
        return "Login successful!"
    else:
        return "Invalid username or password."
username = input("Enter username: ")
password = input("Enter password: ")
print(login(username, password))
