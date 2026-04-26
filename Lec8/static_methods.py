#06
#=========================================================================#
# Static methods
#=========================================================================#
# Methods that don't use the self parameter (imp: this works at class level)

class Student:
    
    def __init__(self,name,marks):
        self.name = name        # object attributes
        self.marks = marks      # object attributes
    
    def call(self):
        print(self.name,self.marks)
    
    @staticmethod # decorator is changing the behaviour of the function.
    def greet(): # This method is only for greeting, so no parameter.
        print("hello")

s1 = Student("prasoon",45)
s1.call()
s1.greet() # this will give an error but using decorator it will get passed


# decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanenlty modifying it