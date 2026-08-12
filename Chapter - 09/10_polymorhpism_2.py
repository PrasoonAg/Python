#=========================================================================#
# 10 - Implementing Operator Overloading
#=========================================================================#
# Previously, we added Complex objects by calling our own add() method.
# Since the Complex class did not define how '+' should behave,
# using '+' raised a TypeError.

# By implementing special (dunder) methods such as __add__() and __sub__(),
# we define how '+' and '-' should behave for Complex objects.
# Python can then use these operators directly with our objects.

class Complex:
    
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real, "i +", self.img, "j")
    
    # Defines how '+' works for Complex objects.
    def __add__(self, other):
        newReal = self.real + other.real
        newImg = self.img + other.img
        return Complex(newReal, newImg)
    
    # Defines how '-' works for Complex objects.
    def __sub__(self, other):
        newReal = self.real - other.real
        newImg = self.img - other.img
        return Complex(newReal, newImg)
        
        
num1 = Complex(1, 3)
num2 = Complex(4, 6)

num1.showNumber()
num2.showNumber()


# '+' automatically calls __add__()
# Python internally performs:
# num1 + num2
# ↓
# num1.__add__(num2)
result = num1 + num2
result.showNumber()

# '-' automatically calls __sub__()
# Python internally performs:
# num1 - num2
# ↓
# num1.__sub__(num2)
result = num1 - num2
result.showNumber()
#=========================================================================#
# Key Concept
#=========================================================================#
# Python only decides which special (dunder) method to call.
# The actual logic inside that method is written by the programmer.

# For example, if __add__() performed multiplication instead of addition,
# using '+' would still execute that multiplication.
#=========================================================================#