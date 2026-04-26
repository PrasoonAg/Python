#03#

# Class & Instance Attributes

# Class.attr
# Same value for all objects
# Defined inside class, outside methods
# Shared by every object

# Object Attribute (obj.attr)
# Different value for each object
# Defined using self inside constructor (__init__)
# Each object has its own copy

class Student:
    collage_name = "ABC College"
    name = "anonymous" # class attr
    
    def __init__(self, name, marks):
        self.name = name #obj attr > class atr
        self.marks = marks

s1 = Student("karan","24")
print(s1.name)
    