#=========================================================================#
# 08 - ENCAPSULATION
#=========================================================================#

# Encapsulation:
# → Wrapping data (variables) and methods (functions) together inside a class
# → Restricting direct access to data (protecting it)

#=========================================================================#
# 08 - ENCAPSULATION
#=========================================================================#

# Encapsulation:
# → Wrapping data (variables) and methods (functions) together inside a class
# → Restricting direct access to data (protecting it)

class Car:

    def __init__(self):
        # Private variables (should not be accessed directly from outside)
        self.__acc = False
        self.__brk = False
        self.__clutch = False
        
    def start(self):
        # Internal logic handled inside the class
        self.__clutch = True
        self.__acc = True
        print("Car started..")
    
    def stop(self):
        self.__acc = False
        self.__brk = True
        print("Car stopped..")


# Creating object
car1 = Car()

# Accessing behavior using methods (safe way)
car1.start()
car1.stop()

# Direct access like this is NOT allowed (encapsulation)
# car1.__acc = True   ❌ (should not be done)