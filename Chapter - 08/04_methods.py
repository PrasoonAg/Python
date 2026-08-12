#=========================================================================#
# 04 - Methods
#=========================================================================#
# Methods:
# Functions defined inside a class.
# Methods are used to perform operations related to an object.
# Instance methods use self to access object attributes and other methods.

class Student:
    
    def __init__(self, name):
        self.name = name
    
    def greet(self): # Method
        print(f"Hello, I am {self.name}")
        
s1 = Student("Prasoon")

s1.greet() # Calling method using object
# Python internally does:
# Student.greet(s1)
# self becomes s1

#=========================================================================#
# Methods Accessing Object Attributes
#=========================================================================#
class Student:

    def __init__(self, name, marks):

        self.name = name
        self.marks = marks
        
    def welcome(self):
        # Accessing the current object's attributes using self
        print("Welcome student,", self.name)
    
    # Method returning an object attribute  
    def get_marks(self):
        return self.marks
        
s1 = Student("Prasoon",99)

s1.welcome()
print(s1.get_marks())
#=========================================================================#