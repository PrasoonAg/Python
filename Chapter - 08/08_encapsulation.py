#=========================================================================#
# 08 - ENCAPSULATION
#=========================================================================#
# Encapsulation:
# Wrapping data (attributes) and methods together into a single unit (class).
# It also helps protect data from direct modification.

class Car:

    def __init__(self):
        # Private attributes (intended for internal use)
        # Should not be accessed directly from outside the class.
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

# Direct access to private attributes is discouraged/restricted.
# Data should be accessed through methods provided by the class.
# car1.__acc = True
#=========================================================================#