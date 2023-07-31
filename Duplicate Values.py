"""
Problem: Duplicate Elements

You are given a list of elements. Your task is to write
a Python function that takes this list as input and returns
a new list containing only the duplicate elements present in
the original list. The order of the elements in the output
list should be the same as their first occurrence in the input list.
"""
# -------------#---------------#------------------#----------------#---------------#
# Solution

# Creating a Function to find duplicate values.
def find_duplicates(list):
    duplicates = []
    unique_elements = set()
    for element in list:
        if element in unique_elements:
            duplicates.append(element)
        else:
            unique_elements.add(element)
    return duplicates

# Creating a list.
list = [1, 2, 4, 3, 5, 6, 7, 3, 5, 3, 6, 7,]
result = find_duplicates(list)
print(result)
