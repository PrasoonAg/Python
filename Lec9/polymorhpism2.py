#=========================================================================#
# 11 - Polymorphism
#=========================================================================#
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
    
    def __add__(self,num2): # Dunder fucntions i.e. add is already defined
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    
    def __sub__(self, other):
        newReal = self.real - other.real
        newImg = self.img - other.img
        return Complex(newReal, newImg)
        
        
num1 =  Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()
print("====")

# "+" operator automatically calls __add__()

# Python only decides WHICH method to call:
# obj1 + obj2  →  obj1.__add__(obj2)

# The logic inside __add__() is written by programmer.
# So even if multiplication is written inside method instead of addition (that should be supposdly according the dunder operation),
# "+" operator will still execute that logic.
num3 = num1 + num2 # due to dunder functions it will behave as add operator
num3.showNumber()
print("====")

num3 = num1 - num2
num3.showNumber()
        