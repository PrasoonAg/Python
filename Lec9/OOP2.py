#=========================================================================#
# 01 - del keyword
#=========================================================================#
# used to delete object properties or object itself.

class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Prasoon")
print(s1.name) # output -> Prasoon

# del s1.name 
# print(s1.name)#error = Student Object has no attribute 'name' .

del s1
print(s1.name)# error = s1 is not defined
# here we deleted the object.