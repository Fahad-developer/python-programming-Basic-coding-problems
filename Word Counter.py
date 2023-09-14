"""
Problem: Word Counter

Write a Python function called word_counter that takes a string as input 
and returns the number of words in the string. Your function should consider 
a word to be any sequence of characters separated by spaces.

For example, if the input string is "Hello world", your function should return 2. 
If the input string is "This is a test", your function should return 4.

Your program should also do the following:

Prompt the user to enter a string.

Call the word_counter function to calculate the number of words in the input string.

Display the result to the user.
"""
# Solution

def count_words(user_input):
    words = user_input.split()
    return len(words)

user_input = str(input("Enter your words to count: "))
result = count_words(user_input)
print("Total words in string is: ", result)