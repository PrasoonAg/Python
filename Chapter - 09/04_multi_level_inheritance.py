#=========================================================================#
# 04 - Multi-Level Inheritance
#=========================================================================#
# A Child Class becomes the Parent of another Child Class.
# Car (Parent)
#   ↓
# ToyotaCar (Child)
#   ↓
# Fortuner (Grandchild)

class Car:

    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")


class ToyotaCar(Car):
    pass

class Fortuner(ToyotaCar):
    pass

car1 = Fortuner("Diesel")

car1.start()   # Inherited from Car
#=========================================================================#