#=========================================================================#
# 07 - Abstraction
#=========================================================================#
# Abstraction:
# Hiding implementation details and showing only the essential features to the user.

# In simple words:
# User knows WHAT to do.
# User does not need to know HOW it is done.

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
#=========================================================================#