#=========================================================================#
# 01 - Object-Oriented Programming (OOP)
#=========================================================================#
# Procedural Programming:
# Programs are organized around functions and procedures.
# Functions improve code reusability and reduce code duplication.

# However, as programs become larger, managing related data and functions separately can become difficult.
# OOP solves this by grouping data and functions inside objects.

name = "Prasoon" # Data

def greet(name): # Function
    print(f"Hello {name}")

greet(name) # Passing data in function

#=========================================================================#
# Object-Oriented Programming (OOP):
# Programs are organized around objects.
# Objects contain both data (attributes) and functions (methods).
# OOP improves code organization, reusability and maintainability.
# Similar objects can be created efficiently using classes.


# Class = Blueprint/template for creating objects.
# Object (Instance) = Actual object created from a class.
# One class can create many objects (instances).

#=========================================================================#
# Why Classes?
# Without classes, data for similar entities would be stored in many separate variables.
# Classes allow us to group related data and functions together.

#=========================================================================#
# Creating Class
class Student: # By convention, class names start with a capital letter.
    name = "Prasoon Agrawal"    # Class attribute (data)    

# Creating Object (instance of class/ instance)
s1 = Student()
s2 = Student()
# s1 and s2 are objects (instances) of Student.

print(s1.name)
print(s2.name)

#=========================================================================#
# Difference between Car and Car()
#=========================================================================#
class Car: # Class
    color = "blue"          # Class attribute (data)
    brand = "Mercedes"      # Class attribute (data)

car1 = Car # Refers to the class itself

print(car1.color)  # blue
print(Car.color)   # blue

car1.color = "red" # Modifies the class attribute

print(car1.color)  # red
print(Car.color)   # red

#=========================================================================#
class Car: # Class
    color = "blue"          # Class attribute (data)

car1 = Car()    # Creates object (instances)
car2 = Car()    # Creates object (instances)

car1.color = "red" # Creates/updates color for car1 only

print(car1.color)  # red
print(car2.color)  # blue
print(Car.color)   # blue

#=========================================================================#
# Car    -> Refers to the class itself.
# Car()  -> Creates a new object (instance) of the class.
#=========================================================================#