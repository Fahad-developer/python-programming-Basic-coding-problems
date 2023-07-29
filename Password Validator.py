"""
Problem: Password Validator

You have been tasked with creating a password validation function.
The function should take a password as input and perform the following checks:

1- The password must be at least 8 characters long and at most 20 characters long.
2- The password must contain at least one uppercase letter, one lowercase letter, and one digit.
3- The password may only contain the following special characters: !@#$%^&*()
4- The function should return True if the password is valid according to the above rules,
and False otherwise.
"""
# -------------#----------------#--------------------#-------------------#---------------------#
# Solution

# Creating a function and passing parameters threw it.
def password_validator(password, length, characters):
    # Printing a simple message.
    print("Analyzing Password.")
    # Checking if the length is less then 8.
    if length < 8:
        print("Invalid: Password should contain at least 8 characters.")
        return False
    # Checking if the length of password is greater then 20.
    elif length > 20:
        print("Invalid: Password should not exceed 20 characters.")
        return False
    # If both condition True the printing message.
    else:
        print("1- Good Password Length.")

        has_uppercase = False
        has_lowercase = False
        has_digit = False
        special_characters = False

        for char in password:
            if char.isupper():
                has_uppercase = True
            elif char.islower():
                has_lowercase = True
            elif char.isdigit():
                has_digit = True

        for char in password:
            if char in characters:
                special_characters = True

        if has_uppercase:
            print("2- Password Contains Uppercase.")
        else:
            print("Invalid: Password should contain at least one uppercase letter.")

        if has_lowercase:
            print("3- Password Contains Lowercase.")
        else:
            print("Invalid: Password should contain at least one lowercase letter.")

        if has_digit:
            print("4- Password Contains a Digit.")
        else:
            print("Invalid: Password should contain at least one digit.")

        if special_characters:
            print("5- Password Contains Special Characters.")
        else:
            print("Invalid: Password should contain at least one special character.")

        return has_uppercase and has_lowercase and has_digit and special_characters

# Creating a variable of str class.
characters = "!@#$%^&*()"

# Creating a variable and taking input.
password = input("Enter your password: ")
# Saving length of password variable in variable called length.
length = len(password)

print(password_validator(password, length, characters))


