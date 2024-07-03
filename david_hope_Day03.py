# David Hope
# 2200721921
# Day 3

"""
Follow PEP 8:
1. Indentation
2. Maximum line length
3. Blank lines
4. Use meaningful names
5. Use list comprehension
"""

# Example of a meaningful name
def calculate_circle_area(radius):
    pass

total_price = 10000

# Example of a lazy student with bad meaningful name
def calc(r):
    tp = 1000

# Python operators
"""
Summary:
Name of the operator            Symbol with example
Addition                        x + y
Subtraction                     x - y
Division                        x / y
Modulus                         x % y
Exponentiation                  x ** y
Floor division                  x // y
"""

# Example of comparison operators
"""
Name of the operator            Symbol with example
Equal                           x == y
Not Equal                       x != y
Greater than                    x > y
Less than                       x < y
Greater or equal                x >= y
Less or equal to                x <= y
Logical AND                     and
Logical OR                      or
Logical NOT                     not
"""

# Example of membership operators
"""
Name                            Symbol with example
In                              in
Not in                          not in
"""

# Example of Python Bitwise operators
"""
Name                            Symbol with example
AND                             &
OR                              |
XOR                             ^
NOT                             ~
"""

# Python cases
"""
Name                            Symbol with example
Snake case                      snake_case
Camel case                      camelCase
Upper case                      UPPERCASE
"""

# Comprehensions (List, dictionary)
"""
Summary:
Comprehensions provide a concise way of creating lists and dictionaries.

Lists: []
Dictionaries: {}
"""

# Example 1
# Basic list comprehension to create a list of squares in a list of 10
squares = [x ** 2 for x in range(10)]
print(squares)

# Example 2
# Create a list of even squares in the range of 20
even_squares = [x ** 2 for x in range(20) if x % 2 == 0]
print(even_squares)

# Dictionary comprehension
# Create a dictionary comprehension for favorite cars and count the length of each car name
favorite_cars = ['Range Rover', 'Jeep', 'Mercedes', 'Ford Raptor', 'BMW']
car_name_lengths = {car: len(car) for car in favorite_cars}
print(car_name_lengths)

# Exercise 1
# Create a dictionary comprehension of tuples where each tuple contains a number and its cube for numbers between 1 and 10
number_cubes = {x: x ** 3 for x in range(1, 11)}
print(number_cubes)
