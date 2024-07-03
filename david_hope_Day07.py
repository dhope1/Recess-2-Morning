# David Hope
# 2200721921
# Day 7



# Inheritance and polymorphism
"""
Inheritance and method overriding
Polymorphism and method resolution order
Abstract classes and interfaces
"""

# Inheritance and method overriding
"""
Inheritance and method overriding allow a class (child class) to inherit attributes and methods
from another class (parent class).

Key concepts:
- Base class (parent class): Class whose properties are inherited by another class
- Derived class (child class): Class that inherits properties from the parent class
"""

# Example 1: Syntax
# Create a class where a dog inherits from animal and overrides the speak method
 
print('Inheritance')
class Creature:
    def speak(self):
        return 'Creature is making a sound'

class Dog(Creature):
    def speak(self):
        return 'Barking'
    
# Implementation of inherited classes
creature = Creature()
dog = Dog()

print(creature.speak())
print(dog.speak())

# Polymorphism
# It allows objects of different classes to be treated as objects of a common superclass.
# Method resolution order (MRO): The order in which Python looks for a method in a hierarchy of classes.

# Example 2
# How polymorphism works in Python

class Creature:
    def speak(self):
        return "Creature speaks"

class Dog(Creature):
    def speak(self):
        return "Barks"
    
class Cat(Creature):
    def speak(self):
        return "Meow"

def make_creature_speak(creature):
    print(creature.speak())

print('\n')
print('Polymorphism')
make_creature_speak(Dog())
make_creature_speak(Cat())

"""
Exercise 1: Create a simple application to manage different types of vehicles. 
Implement derived classes to demonstrate inheritance and polymorphism.

Requirements:
1. Base class Vehicle
Attributes: make, model, and year
Methods: display_info()

2. Derived classes:
Car: Inherits from Vehicle
Attributes: number_of_doors
Overrides: display_info()

Motorcycle: Inherits from Vehicle
Attributes: type_of_bike (cruiser, sport, touring)
Overrides: display_info()

Exercise 2: Polymorphism
Create a function that accepts a list of vehicle objects and calls their display_info()
method to print details of each vehicle
"""

print('\n')
# Solution 1 (Inheritance)
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Vehicle Info: {self.year} {self.brand} {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors
        
    def display_info(self):
        print(f"Car Info: {self.year} {self.brand} {self.model}, Doors: {self.doors}")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, bike_type):
        super().__init__(brand, model, year)
        self.bike_type = bike_type
        
    def display_info(self):
        print(f"Motorcycle Info: {self.year} {self.brand} {self.model}, Type: {self.bike_type}")

car = Car("Toyota", "Camry", 2020, 4)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2019, "Cruiser")

car.display_info()
motorcycle.display_info()

# Polymorphism
# Solution 2
def display_vehicle_info(vehicles):
    for vehicle in vehicles:
        vehicle.display_info()

vehicles = [car, motorcycle]
display_vehicle_info(vehicles)

print('\n')

# Reading and writing files in Python
"""
1. Working with text files
Handling CSV files
JSON and XML file processing
"""

# 1. Working with text files: open, read, write, and close
# Note: Python provides built-in functions to handle text files

# Key concepts:
"""
Functions provided by Python:
Opening file: open() 
Reading file: read()
Writing file: write()
Closing file: close()
"""

# Example 3: Write to a file and read from a file

# Writing to a text file
with open('hope.txt', 'w') as file:
    file.write('I am David, and I love programming\n')
    file.write('I like using Stack Overflow')

print('Text file created successfully')

# Reading from a text file
with open('hope.txt', 'r') as file:
    content = file.read()
    print(content)

print('The data from the text file read successfully')

print('\n')

# Handling CSV files
"""
CSV (Comma Separated Values) files are widely used for data exchange

Key concepts:
Read CSV files: Using 'csv.reader()'
Write to CSV files: Using 'csv.writer()'
DictReader and DictWriter: Classes to read and write CSV files as dictionaries
"""

# Example 4: Writing and reading CSV files

import csv

# Writing to a CSV file
with open('hope.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Name', 'Position', 'Course'])
    writer.writerow(['David Hope', 'Student', 'BSSE'])
    writer.writerow(['Henry', 'Student', 'BSE'])
    
print('CSV file created successfully')
    
with open('hope.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
        
print('Data from the CSV file read successfully')
print('\n')

# JSON and XML file processing
"""
JSON (JavaScript Object Notation) and XML (eXtensible Markup Language)
These formats are used to structure data

Key concepts:
Loading JSON data: Using json.load() for reading a JSON file
Dumping JSON data: Using json.dump() for writing a JSON file
Parsing JSON data: Using json.loads() for handling JSON strings
"""

# Example 5: Write and read JSON file
import json

# Writing to a JSON file
hope = {
    'Name': 'David',
    'Course': 'BSSE',
    'Year': '3'
}

# Open the file
with open('hope.json', 'w') as json_file:
    json.dump(hope, json_file) 

print('JSON file created successfully')

# Reading the JSON file
with open('hope.json', 'r') as json_file:
    hope = json.load(json_file)
    print(hope)
    print('The data read successfully')

print('\n')

# Exercise 2: Write and read an XML file
import xml.etree.ElementTree as ET

# Data to be written to the XML file
hope = {
    'Name': 'David',
    'Course': 'BSSE',
    'Year': '3'
}

# Writing to an XML file
root = ET.Element("student")
for key, value in hope.items():
    element = ET.SubElement(root, key)
    element.text = value

tree = ET.ElementTree(root)
tree.write("hope.xml")

print("XML file 'hope.xml' created successfully.")

# Reading from an XML file
tree = ET.parse('hope.xml')
root = tree.getroot()

hope = {}
for child in root:
    hope[child.tag] = child.text

print(hope)
print('Data from the XML file read successfully')
print('\n')

print('Abstraction')
# Exercise 3: Using abstraction to calculate the area and perimeter of a rectangle
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

rectangle = Rectangle(5, 3)
print(f"The area of the rectangle is: {rectangle.calculate_area()}")
print(f"The perimeter of the rectangle is: {rectangle.calculate_perimeter()}")
