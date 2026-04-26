#=========================================================================#
# 05 - Multi-Inheritance
#=========================================================================#
# • Multi-Level Inheritance
    # Base (parent) -> Derived(child) (parent for the next derived) -> Derived(child) ->...etc
    # There can be various level of inhertiance
    # example shows:
    # Car -> ToyotaCar -> Fortuner
class Car:
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car Stopped")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand
        
class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("disel")
car1.start()