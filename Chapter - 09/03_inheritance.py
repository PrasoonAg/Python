#=========================================================================#
# 03 - Inheritance
#=========================================================================#
# Inheritance:
# A mechanism that allows one class to acquire the attributes and methods
# of another class.

# Parent/Base Class:
# The class whose attributes and methods are inherited.

# Child/Derived Class:
# The class that inherits attributes and methods from another class.

# Why use Inheritance?
# To promote code reusability and avoid writing the same code again.

#=========================================================================#
# Types of Inheritance
#=========================================================================#
# 1. Single Inheritance
# One Child Class inherits from one Parent Class.
# Parent
#    ↓
# Child

# 2. Multi-Level Inheritance
# A Child Class becomes the Parent of another Child Class.
# Parent
#    ↓
# Child
#    ↓
# Grandchild

# 3. Multiple Inheritance
# One Child Class inherits from multiple Parent Classes.
# Parent1 ──┐
#           ├── Child
# Parent2 ──┘

#=========================================================================#
# Single Inheritance
#=========================================================================#
# One Child Class inherits from one Parent Class.

class Car:
    color = "Black"  # Class Attribute
    
    @staticmethod
    def start():
        print("Car started..")
    
    @staticmethod
    def stop():
        print("Car stopped.")

# ToyotaCar inherits all accessible attributes and methods from Car.
class ToyotaCar(Car):

    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")

print(car1.name)   # Fortuner

car1.start()       # Inherited method
print(car1.color)  # Inherited attribute
#=========================================================================#