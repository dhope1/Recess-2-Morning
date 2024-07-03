# David Hope
# 2200721921
# Day 2

"""
Control Structures:
 Conditional statements (if, elif, else)
 Loops (for, while)
 Comprehensions (list, dictionary comprehensions)
"""

# if, elif, else

# Example 1
print("Example 1")
age = 70

if age < 18:
    print('You are an adult')
elif age > 65:
    print('You are a senior citizen')
else:
    print('You are a youth')

# Example 2
print("Example 2")
# 90 and above is Excellent, 80 and above is Very good, if 70, good
# otherwise, not good.

score = 50

if score >= 90:
    print('Excellent')
elif score >= 80:
    print('Very good')
elif score >= 70:
    print('Good')
else:
    print('Not good')

"""
Exercise: Write a Python script to determine the price of a movie based on age.
Condition:
Children under 13 get a discount price = shs1000
Teenagers between 13 and 18 get a discount price = shs500
Adults 18 and above pay full price = shs2000
Senior citizens pay full price = shs5000
"""

# Exercise 1 solution
print()
print("Exercise Solution")

age = int(input("What's your age? "))
full_price = 2000
if age < 13:
    discount = 1000
    price = full_price - discount
    print(f"Children pay {price}")
elif 13 <= age < 18:
    discount = 500
    price = full_price - discount
    print(f"Teenagers pay {price}")
elif 18 <= age < 65:
    price = full_price
    print(f"Adults pay {price}")
else:
    senior_price = 5000
    print(f"Senior citizens pay {senior_price}")

# Loops (for, while)

"""
For loop iterates over a sequence (list, tuple, dictionary, set, string).
The while loop repeats as long as a condition is true.
"""

# Example 3
print()
print("Example 3")
cars = ['Tesla', 'Audi', 'BMW', 'Jeep', 'Range Rover']

for car in cars:
    print(car)

# Example 4: Count 1 to 10
print()
print("Example 4")

count = 1
while count <= 10:
    print(f"Count 1 to 10: {count}")
    count += 1

# Exercise 2

"""
Create your own list of favorite colors using a for loop.
Create a reverse of the input 12345 to be 54321 using a while loop.
"""
print()
print("Exercise 2 solution")

# Favorite colors
favorite_colors = ["red", "black", "lavender", "turquoise"]
for color in favorite_colors:
    print(color)

print()
print("Reversed colors")
reversed_colors = favorite_colors[::-1]

for color in reversed_colors:
    print(color)

print()

# Reverse number using a while loop
number = 12345
reversed_number = 0

while number != 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

print(f"Reversed number: {reversed_number}")
