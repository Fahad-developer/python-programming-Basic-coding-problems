"""
Problem: ATM Pin Verification

You are building an ATM system, and you need to implement the PIN verification process.
The ATM users have 4-digit PINs. Your task is to write a Python function that takes a
user's entered PIN and verifies its validity according to the following rules:

The PIN must be exactly 4 digits long.
The PIN can only contain digits (0-9).
"""
# -------------#---------------#-----------------#--------------------#----------------------------#
# Solution

def verification(pin, length):
    if length == 4:
        print("Pin is 4 digit long.")
    else:
        print("Invalid pin, must be 4 digits long.")
    if pin.isdigit():
        print("Pin contains only digit.")
    else:
        print("Invalid pin, Pin can only cantain digits ex: (3333).")


pin = input("Enter your pin: ")
length = len(pin)
result = verification(pin, length)
print(result)

