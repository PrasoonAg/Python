#=========================================================================#
#01
#=========================================================================#
# this is procdeural programming i.e. writing code in sequence which i done earlier.
a = 10
b = 20

sum = a + b
print (sum)

diff =  a - b
print(diff)

# Function came, which gives the access of reusability of the code +.
# This helped to lower the reduancy of the code.

# object oreinted programming 
# Class = Blueprint(design)
# Object = Real instance (actual thing created from class)
# Objects are created FROM a class

# Creating class
class Student: # class first letter always start with capital
    name = "Karan Kumar"  #same name

# creating object (instance of class/ instance)
s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)

class Car:
    color = "blue"
    brand = "mercedes"
    
car1 = Car
print(car1.color)
print(car1.brand)