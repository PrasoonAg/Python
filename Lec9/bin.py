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
num3 = num1.add(num2)

num3.showNumber()