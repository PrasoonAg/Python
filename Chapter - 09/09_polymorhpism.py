#=========================================================================#
# 09 - Polymorphism (Operator Overloading)
#=========================================================================#
# Poly  = Many
# Morph = Forms
# Polymorphism = One thing, many forms.

# Polymorphism:
# The ability of the same operator or method to behave differently
# depending on the object or data it is used with.

# Operator Overloading:
# Giving the same operator different behavior for different data types or objects.

#=========================================================================#
# Same Operator, Different Behavior
#=========================================================================#
print(1 + 2)              # 3 (Addition)
print("Apna" + "College") # ApnaCollege (String Concatenation)
print([1, 2] + [3, 4])    # [1, 2, 3, 4] (List Concatenation)

# The '+' operator behaves differently depending on the data type.
# Python achieves this by automatically calling the corresponding
# special (dunder) method for that data type.

#=========================================================================#
# How Python Performs Operator Overloading
#=========================================================================#
# When an operator is used, Python automatically calls the
# corresponding special (dunder) method for that object.

# Operators                    Dunder (Special) Methods
# a + b        (Addition)              a.__add__(b)
# a - b        (Subtraction)           a.__sub__(b)
# a * b        (Multiplication)        a.__mul__(b)
# a / b        (Division)              a.__truediv__(b)
# a % b        (Modulus)               a.__mod__(b)

# Internally, Python performs operations similar to:

# 5 + 3          -> int.__add__()
# "Hi" + "!"     -> str.__add__()
# [1] + [2]      -> list.__add__()

#=========================================================================#
# Dunder (Double Underscore) Methods
#=========================================================================#
# Special methods whose names begin and end with double underscores (__).
# Examples: __init__, __str__, __add__, __len__

#=========================================================================#
# Manual Addition of User-Defined Objects (Without Operator Overloading)
#=========================================================================#
# For user-defined classes, Python does not know how operators like '+'
# should behave unless we define that behavior ourselves.
class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real, "i +", self.img, "j")
    
    # Our own method for adding two Complex objects.
    # This is NOT operator overloading.
    def add(self, other):
        newReal = self.real + other.real
        newImg = self.img + other.img
        
        # Return a new Complex object containing the result
        return Complex(newReal, newImg)


num1 = Complex(1, 3)
num2 = Complex(4, 6)

num1.showNumber()
num2.showNumber()

num3 = num1.add(num2)
# Internally:
# num1.add(num2)
# ↓
# Complex.add(num1, num2)
#
# self  -> num1
# other -> num2

num3.showNumber()

# We have to call add() manually.
# '+' does not work because the Complex class does not
# define the __add__() method yet.

# num3 = num1 + num2   # TypeError
#=========================================================================#