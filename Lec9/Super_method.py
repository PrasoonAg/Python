#=========================================================================#
# 07 - Super Method
#=========================================================================#
# super() method is used to access methods of the parent class
# calling constructor of parent class to child class

class Car:
    def __init__(self, type):
        # Parent class constructor
        self.type = type # object attributes (shared by all child classes)

    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self,name,type): # have to mention the attribute of parent class.
        
        self.name = name # attribute specific to ToyotaCar
        
        # Calling parent class constructor using super()
        # This initializes 'type' attribute from parent class
        super().__init__(type) 
        # Calling parent class method
        super().start()

#creating object
car1 = ToyotaCar("prius","electric")
print(car1.type) # works beacuse super().__init__() was called