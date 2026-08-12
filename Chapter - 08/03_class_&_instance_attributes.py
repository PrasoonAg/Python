#=========================================================================#
# 03 - Class & Instance Attributes
#=========================================================================#
# Class Attribute:
# Defined inside the class, outside methods.
# Shared by all objects of the class.
# Same value is available to every object.

# Instance Attribute:
# Defined using self inside methods (commonly __init__()).
# Belongs to a specific object.
# Each object can have different values.

class Student:
    college_name = "ABC College"    # Class Attribute
    
    def __init__(self, name, marks):
        self.name = name            # Instance Attribute
        self.marks = marks          # Instance Attribute

s1 = Student("Karan", 24)
s2 = Student("Arjun", 90)

print(s1.name) # Karan
print(s2.name) # Arjun

print(s1.college_name) # ABC College
print(s2.college_name) # ABC College
#=========================================================================#
# Attribute Priority
#=========================================================================#
# If both Instance and Class Attributes have the same name,
# the Instance Attribute gets priority.
class Student:
    name = "Anonymous"   # Class Attribute
    
    def __init__(self, name):
        self.name = name # Instance Attribute

s1 = Student("Prasoon")

print(s1.name) # Prasoon
print(Student.name) # Anonymous

# s1.name uses the Instance Attribute.
# Student.name uses the Class Attribute.

# Python first looks for an Instance Attribute.
# If not found, it looks for a Class Attribute.
#=========================================================================#