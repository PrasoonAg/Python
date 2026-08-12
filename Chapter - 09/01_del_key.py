#=========================================================================#
# 01 - del Keyword
#=========================================================================#
# del Keyword:
# Used to delete variables, object attributes, or entire objects.

class Student:
    
    def __init__(self,name):
        self.name = name

s1 = Student("Prasoon")

print(s1.name) # Prasoon

# Deleting an attribute
# del s1.name
# print(s1.name)
# ERROR: 'Student' object has no attribute 'name'

# Deleting an object
del s1
# print(s1)
# ERROR: name 's1' is not defined
#=========================================================================#