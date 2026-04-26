#=========================================================================#
# 06 - Multiple Inheritance
#=========================================================================#
# • Multiple Inheritance
    # if we have derived class it could inhertitate multiple base class i.e. two parents
    # there could be 2 or more base(parent) class
    # base1 -> Derived <- base2
    
class A: # parent (base)
    varA = "welcome to class A"

class B: # parent (base)
    varB = "welcome to class B"

class C(A, B): # derived (child) class # Inherited both A & B
    varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varA)
print(c1.varB)