"""
Problem: Sentence Capitalizer

You are given a sentence as input. Your task is to write a Python
function that takes this sentence as input and returns a new
sentence where the first letter of each word is capitalized,
and all other letters are in lowercase. The words in the new
sentence should be separated by a single space.
"""
# --------------#-----------------#---------------#---------------------#
# Solution

def sentence_capitalizer(sentence):
    # Split the sentence into words using space as the delimiter
    words = sentence.split()

    # Initialize an empty list to store the capitalized words
    capitalized_words = []

    # Capitalize the first letter of each word and convert the rest to lowercase
    for word in words:
        capitalized_word = word.capitalize()
        capitalized_words.append(capitalized_word)

    # Join the capitalized words back into a sentence using a single space as the separator
    new_sentence = ' '.join(capitalized_words)

    return new_sentence


# Test the function with an example
sentence_input = input("Enter your sentence: ")
result = sentence_capitalizer(sentence_input)
print(result)  # Output: "Hello World, How Are You?"

