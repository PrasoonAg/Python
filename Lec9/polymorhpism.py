#=========================================================================#
# 10 - Polymorphism : Operator Overloading
#=========================================================================#
# poly means many & morph means forms (faces)
# when the same operator is allowed to have different meaning accoring to the context

#  Operators & Dunder functions
# a + b       # addition              a.__add__(b)
# a - b       # subtraction           a.__sub__(b)
# a * b       # multiplication        a.__mul___(b)
# a / b       # division              a.__trudiv___(b)
# a % b       # addition              a.__mod___(b)

# plus(+) operator perfroms different actions and are already defined according to the statements
print(1+2) #3  # add # 1 & 2 are the object for print as an integer type
print(type(1)) # 1 is the object

print("apna" + "college") # concatnate # apna and collage is the object
print(type("apna")) 

print([1,2,3] + [4,5,6]) # merge
print(type([]))