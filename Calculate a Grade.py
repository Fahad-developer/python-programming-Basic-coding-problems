"""
Problem: Calculate a Grade

Write a Python program that calculates the letter grade for a student based on 
their numerical score. The program should do the following:

Prompt the user to enter their numerical score as a float (e.g., 95.5).

Determine the letter grade based on the following scale:

A: 90-100
B: 80-89.9
C: 70-79.9
D: 60-69.9
F: Below 60
Display the calculated letter grade to the user.
"""

# Solution

Grade = float(input("Enter your numerical score: "))
if Grade > 100 or Grade < 0:
    print("Invalid Score!, Please enter right numerical score.")
elif Grade < 60:
    print("Your grade is: B")
elif Grade > 60 and Grade < 69.9:
    print("Your grade is: D")
elif Grade > 70 and Grade < 79.9:
    print("Your grade is: C")
elif Grade > 80 and Grade < 89.9:
    print("Your grade is: B")
elif Grade > 90 and Grade < 100:
    print("Your grade is: A")