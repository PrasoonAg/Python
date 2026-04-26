#=========================================================================#
# 02 - Private(Like) Attributes and Methods
#=========================================================================#
# Conceptual Implementations in Python
# Private attributes and methods are meant to be used only within the class and are not accessible from outside the class.

#-----PUBLIC-----#
# Public attributes can be accessed and modified from outside the class
class Student:
    def __init__(self,name):
        self.name = name # publiic attribute (accessible anywhere)
        
s1 = Student("Prasoon")
print(s1.name) # can access from outside

s1.name = "King" # can modify from outside
print(s1.name)
# Public variables are easy to use but NOT safe (can be changed anytime)

#-----PRIVATE-----#
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no= acc_no               # public attribute
        self.__acc_pass = acc_pass        # private attribute
    
    def reset_pass(self):
        print(self.__acc_pass)            # Private variable is accessible INSIDE the class
        
s2 = Account(23232,"dsdscc")
print(s2.acc_no)  # public attribute accessible
# print(s2.__acc_pass) #ERROR (cannot access directly)
s2.reset_pass() # accessing private data via method