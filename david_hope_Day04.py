# David Hope
# 2200721921
# Day 4

# Dictionaries
# Creating and using dictionaries
# Dictionary methods and operations

"""
Summary:
Dictionaries in Python are collections of keys and values
- Unordered
- Mutable
- Indexed by keys
"""

# Example 1: Create a dictionary
# Create a dictionary for a student pursuing software engineering
# The key must be your name, age, technology interest, and year of study.

print("Example 1 Solution")

student_info = {
    "name": "David Hope",
    "age": "30",
    "technology": "AI and ML",
    "course": "BSE",
    "year": "Year 3"
}

print(student_info["name"])
print()

# Access values
# Modify values:

# Exercise 1: Modify age and technology
print("Exercise 1 Solution")
student_info["age"] = "42"
student_info["technology"] = "Robotics"

print(student_info["age"])
print(student_info["technology"])

# Example 2: Adding keys and values
print()
print("Example 2")
student_info["email"] = "davidhope@example.com"

print(student_info)

# Exercise 2: Remove a key and value from the student dictionary
print()
print("Exercise 2 Solution")
del student_info["age"]
print(student_info)

# Remove using the pop() method
year_value = student_info.pop("year")
print("Dictionary after removing 'year':", student_info)
print("Removed value:", year_value)
print()

# Common Dictionary methods
"""
Summary:
get()    - Returns the value for the specified key if the key is in the dictionary; if not, it returns the default value.
update() - Updates the dictionary with elements from another dictionary.
pop()    - Removes the specified key and returns the corresponding value.
"""

# Example 3: Use the get method to get the value
print("Example 3")
print(student_info.get("technology"))

# Exercise 3: Use the update method to change the value of 'age'
student_info.update({"age": "25"})
print(student_info)
print()

# Exercise 4: Use if to check if the key 'age' is present in the dictionary
print("Exercise 4 Solution")
if "age" in student_info:
    print("Age is present in the dictionary:", student_info["age"])
else:
    print("Age is not present in the dictionary.")
print()

# keys(), values(), and items() methods
print(student_info.keys())
print(student_info.values())
print(student_info.items())

"""
Summary:
keys()   - Returns a view object that displays a list of all keys.
values() - Returns a view object that displays a list of all values.
items()  - Returns a view object that displays a list of dictionary key-value tuple pairs.
"""
print()

# Exercise 5: Use the update method to change the course and add a new key "WhatsApp_Number" to the dictionary
print("Exercise 5 Solution")
student_info.update({"course": "BSC", "WhatsApp_Number": "0770636395"})
print("Student dictionary after change:", student_info)
print()
