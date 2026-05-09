#04#
# Methods

# Methods are the functions that belong ot objects.
# method = function that is defined inside a class and works with objects(used with object)

# functions
def greet(name):
    print("hello",name)
    
greet("Prasoon") # called using function name

# method
# method = function that is defined inside a class and works with objects(used with object)

class Student:
    def greet(self): # this is a method
        # always self as a paramter
        print("hello from student")
        
s1 = Student()
s1.greet() # called using object as a method
#what python actually does:
# Student.greet(s1) #s1 = self
#===#
class Student1:
    college_name = "ABC College"
    
    def __init__(self,name,marks):
        # self -> current object being created
        # name & marks -> values passed during object creation
        self.name = name
        self.marks = marks
        
    def welcome(self):
        # accesing current objects's attributes using self
        print("welcome student",self.name)
        
    def getmarks(self):
        return self.marks
        
s2 = Student1("prasoon",99)
s2.welcome()
print(s2.getmarks())