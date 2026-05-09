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

# Dunder functions are begin and end with double underscores, such as __init__ or __str_.

# plus(+) operator perfroms different actions and are already defined according to the statements
print(1+2) #3  # add # 1 & 2 are the object for print as an integer type
print(type(1)) # 1 is the object

print("apna" + "college") # concatnate # apna and collage is the object
print(type("apna")) 

print([1,2,3] + [4,5,6]) # merge
print(type([[1,2,3]])) # list


# nomral numbers (real) => 1,2,3,-5,3.14 like 1+2=3
# complex numbers 1i+3j (real + imaginary number)
# (2i + 5j) + (1i + 3j) = 3i + 8j # real parts and imaginary parts are added accoridngly
# (5i + 10j) + (-1i + 8j) = 4i + 18j

print("=======")

class Complex:

    def __init__(self, real, img):
        # self → current object being created
        # real and img → values passed during object creation

        self.real = real
        self.img = img
    
    def showNumber(self):
        # accessing current object's attributes using self
        print(self.real, "i +", self.img, "j")
    
    def add(self, num2):
        # self  → object calling the method
        # num2  → second object passed as argument

        # Note:
        # 'num2' is just a parameter name.
        # It can be anything like:
        # other, obj, x, abc etc.

        # Example:
        # num1.add(num2)
        # internally becomes:
        # add(num1, num2)

        # Therefore:
        # self = num1
        # num2 = num2

        newReal = self.real + num2.real
        newImg = self.img + num2.img

        # Returning a NEW Complex object after addition
        return Complex(newReal, newImg)


num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

# num1 is automatically passed as self
# num2 is passed manually as argument
num3 = num1.add(num2) # num1.add(num2)
                      # internally Python does:
                      # Complex.add(num1, num2)

                      # Therefore:
                      # self = num1  (object calling the method)
                      # num2 = num2  (object passed as argument)

num3.showNumber()

# we can do something like this:
# num3 = num1 + num2
# ther is no logic here