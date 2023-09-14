"""
Problem: User Authentication

Write a Python program that simulates a basic user authentication system. The program should:

Maintain a dictionary of usernames and passwords (you can hardcode this for simplicity).
Prompt the user to enter their username and password.
Check if the entered username and password match any in the dictionary.
Display a success message if the credentials are correct or an error message if they are incorrect.

"""

# Solution.

user_credentials = {
    "user1" : "password 123",
    "user2" : "password",
    "user3" : "password password"
}

username = input("Enter your user name: ")

password = input("Enter your password: ")

if username in user_credentials and user_credentials[username] == password:
    print("Authentication Succesfull you are logged in.")
else:
    print("Authentication failed! please check your username or password and try again later.")