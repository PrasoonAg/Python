#=========================================================================#
# 06 - super() Method
#=========================================================================#
# super():
# Used inside a Child Class to call/run methods or constructors of the Parent Class.

# Inheritance gives access to Parent Class features.
# super() is used when the Child Class explicitly wants to execute Parent Class code.
#
# Common Uses:
# super().__init__() -> Calls/Runs Parent constructor.
# super().method()   -> Calls/Runs Parent method.
#=========================================================================#
class Car:

    def __init__(self, type):
        # Parent class constructor
        self.type = type

    @staticmethod
    def start():
        print("Car started..")
    
    @staticmethod
    def stop():
        print("Car stopped.")

class ToyotaCar(Car):

    def __init__(self, name, type): # Parent constructor needs 'type', so Child constructor receives it too.

        # Attribute specific to ToyotaCar
        self.name = name

        # Parent constructor needs 'type',
        # so Child constructor receives it too.
        # Execute Parent constructor.
        super().__init__(type)

        # Execute Parent method from inside Child Class.
        super().start()

# Creating object
car1 = ToyotaCar("Prius", "Electric")

print(car1.type)  # Electric

#=========================================================================#
# Important Difference
#=========================================================================#

# Inheritance:
# Allows a Child Class to use Parent Class attributes and methods.

# Example (Outside the Child Class):
# car1.start()
# Here we are simply using an inherited method through an object.

# super():
# Used inside a Child Class when we want Parent Class code to run.

# Example (Inside the Child Class):
# super().start()
# Runs the Parent Class start() method from inside the Child Class.
#=========================================================================#