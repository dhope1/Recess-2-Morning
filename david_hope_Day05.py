# David Hope
# 2200721921
# Day 5

# Defining Functions
# Function syntax and parameters
# Return value
# Lambda functions

# Functions in Python are defined using the 'def' keyword, followed by the function name and then parentheses().
# Inside the parentheses, you put a parameter name and then a colon.

# Example 1: Basic function definition and return
def multiply(a, b):
    return a * b

result = multiply(5, 10)
print(result)

# Example 2: Multiple return values
def get_coordinates():
    return 10, 20

x, y = get_coordinates()
print(x, y)

# Exercise 1: Define a function greet with a parameter name, set to 'Guest', and print the message
def greet(Guest="David"):
    print(f"I am a software engineer, {Guest}")

greet('David')

# Example 3: Return name and position
def get_name_and_position():
    name = "David Hope"
    position = "I am a software engineer"
    return name, position

name, position = get_name_and_position()
print(name, position)

# Exercise 2: Return multiple values of your name and age
def get_name_and_age():
    name = "David Hope"
    age = 30
    return name, age

name, age = get_name_and_age()
print(name, age)

"""
Summary:
def: Keyword to define a function
function_name: Name of the function
parameters: Optional, arguments passed to the function
Docstrings: Optional, describes the function's purpose
return: Optional, returns a value from the function
"""

# Lambda functions
# Lambda functions are small anonymous functions defined using the lambda keyword.
# They are restricted to a single expression.

# Syntax for lambda functions:
# lambda parameters: expression

# Example 4: Create a lambda function to add two numbers
add = lambda a, b: a + b
print(add(45, 70))

# Example 5: Use case of a lambda function for sorting
coordinates = [(1, 2), (2, 3), (3, 1), (5, 0)]
coordinates.sort(key=lambda coordinate: coordinate[1])
print(coordinates)

# Map, Filter, and Reduce
# Example 6: Get the squares of 1 to 5 using map, filter, and reduce

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)

# Exercise 3: Define a function to get user info that accepts arbitrary keyword arguments and prints each key-value pair
def student_info(**student):
    for key, value in student.items():
        print(f"Student {key}: {value}")

student_info(first_name='David', last_name='Hope')

# Example 7: Function with additional keyword arguments
def my_function(a, b, **kwargs):
    print(f"a: {a}, b: {b}")

    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(1, 2, x=100, y=200, z=300)
