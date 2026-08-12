#=========================================================================#
# 02 - Constructor & Self
#=========================================================================#
# self:
# self refers to the current object (instance).
# Python automatically passes the newly created object as self.
# self is used to access the data and methods of that object.

# Constructor (__init__):
# __init__() is a special method that runs automatically when an object is created.
# It is commonly used to initialize object attributes.
#=========================================================================#
class Student:
    
    def __init__(self):  # __init__() is called automatically whenever an object is created.
        print(self)      # Shows the current object. Same object as s1 or s2 being created.
        print("Initializing newly created Student object.")

s1 = Student()                  # Creates object (instance)
s2 = Student()                  # Creates object (instance)

# What Python does internally:
# When s1 is created:
# Student.__init__(s1)
# self becomes s1

# When s2 is created:
# Student.__init__(s2)
# self becomes s2

print(s1) # Object representation of s1 (includes memory address)
print(s2) # Object representation of s2 (includes memory address)

# s1 and s2 are different objects, so their memory addresses are different.

#=========================================================================#
# Default Constructor & Parameterized Constructor
#=========================================================================#
# Default Constructor:
# A constructor that takes only self.
# No values are passed during object creation.
# __init__() still runs automatically when an object is created.

# Parameterized Constructor:
# A constructor that accepts additional values during object creation.
# These values are commonly used to initialize object attributes.
#=========================================================================#
# Default Constructors
class Student:
    
    def __init__(self):
        print("Default Constructor called")

s1 = Student()  # No values passed

# Parameterized Constructor Example
class Student:

    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
    
# fullname and marks are received by the constructor.
# They are stored inside the object using self.

s1 = Student("Prasoon", 20)  # Values passed during object creation

print(s1.name)
print(s1.marks)

#=========================================================================#
# WHAT HAPPENS IF self IS NOT WRITTEN?
#=========================================================================#
class Test:
    
    def __init__(): # Missing self
        print("Hello")
        
# t1 = Test()
# ERROR:
# When an object is created, Python automatically passes that object as the first argument to __init__().

# Internally:
# Test.__init__(t1)

# But init() is not expecting any argument.
# Therefore Python raises a TypeError.
#=========================================================================#
# IMPORTANT NOTE:
# Even if __init__() is not written, Python automatically provides a default constructor.
# The default constructor does nothing.
# We write __init__() when we want to initialize object data.
#=========================================================================#