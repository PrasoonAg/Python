#=========================================================================#
# 04 - Inheritance
#=========================================================================#
# when one class(child/derived) derives the properties & methods of another class(parent/base).
# parent/base class is the class from where the properties and methods are taken.
# child/derived is the class which take properties from parent/base class.

class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped.")
        
class ToyotaCar(Car): # all the properties of the Car class now inhertitated by this class.
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("Prius")

print(car1.start())
print(car1.color)

# There are three types of inheritance-:
# • Single Inheritance
    # Base (parent) -> Derived(child)
    # above is the example of singile inheritance.

# • Multi-Level Inheritance
    # Base (parent) -> Derived(child) (parent for the next derived) -> Derived(child)

# • Multiple Inheritance
    # if we have derived class it could inhertitate multiple base class i.e. two parents
    # there could be 2 or more base(parent) class
    # base1 -> Derived <- base2