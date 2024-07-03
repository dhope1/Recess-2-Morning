# David Hope
#2200721921
#Day 6

# Error handling in Python
# Exception handling with try, except, else, and finally
# Custom exceptions

"""
Error handling in Python helps handle unexpected situations and errors.

1. Try: Contains code that might throw an exception.
   NB. If an exception occurs, the rest of the code in the try block is skipped.

2. Except: Catches and handles exceptions.
   NB. You can specify different handlers for different exception types.

3. Else: The code runs if no exception occurs.
   NB. If no exception is raised in the try block, it runs.

4. Finally: It runs whether an exception occurs or not.
   NB. Used for cleaning up actions.
"""

# Example 1: Handle exception with division by zero
try:
    number = int(input('Enter a number: '))
    result = 20 / number
except ValueError:
    print('Invalid value! Enter a number.')
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
else:
    print(f"Result is {result}")
finally:
    print('Execution completed successfully.')

# Exercise 1: Write a function that converts a string to an integer and handles both ValueError if the string cannot be converted into an integer and
# TypeError if the input is not a string. Use multiple except blocks to handle these exceptions.

def convert_to_integer(value):
    try:
        result = int(value)
        return result
    except ValueError:
        print("ValueError: The provided string cannot be converted to an integer.")
    except TypeError:
        print("TypeError: The input is not a string.")

print(convert_to_integer("123"))  # Valid string
print(convert_to_integer("abc"))  # Invalid string
print(convert_to_integer(123))    # Invalid type (int)
print(convert_to_integer(None))   # Invalid type (None)

# Example 2: Exception raised for error in the input, if funds are insufficient
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Attempt to withdraw {self.amount} with only {self.balance}"
        super().__init__(self.message)

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

# Custom exception handling
try:
    balance = 20000
    amount_to_withdraw = 10000
    new_balance = withdraw(balance, amount_to_withdraw)
except InsufficientFundsError as e:
    print(f"Error: {e.message}")
else:
    print(f"Withdraw successful. New balance is {new_balance}")
finally:
    print('Transaction completed.')

"""
Summary:

Defining a custom exception:
class CustomError(Exception):
    # Custom exception for specific error cases
    
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    
# Raising a custom exception:
def check_value(value):
    if value < 0:
        raise CustomError('Value cannot be negative')
    return value
    
# Handle exceptions with try, except, else, and finally:
try:
    result = check_value(-10)
except CustomError as e:
    print(f"Custom error caught: {e.message}")
"""

# Exercise 2: Create a custom exception InvalidAgeError and write a function that raises
# this exception if the given age is negative. Handle this custom exception when calling the function.

class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        self.message = "You cannot have a negative age!"
        super().__init__(self.message)

def check_age(age):
    if age < 0:
        raise InvalidAgeError(age)
    return age

try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print(f"Error: {e.message}")
finally:
    print('Execution complete.')
