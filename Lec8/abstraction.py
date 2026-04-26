
#=========================================================================#
# 07 - Abstraction
#=========================================================================#
# Abstraction:
# → Hiding internal implementation details
# → Showing only what is necessary to the user

class Car:
    def __init__(self):
        # internal state of the car (user doesn't need to manage this manually)
        self.acc = False
        self.brk = False
        self.clutch = False
        
    def start(self):
        # internal steps required to start the car (hidden from user)
        self.clutch = True
        self.acc = True
        
        # User only sees this simple output
        print("Car started..")

# creating object
car1 =  Car()

# User only calls this method -> doesn't worry about clutch/accelerator logic.
car1.start()