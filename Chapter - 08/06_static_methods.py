#=========================================================================#
# 06 - Static methods
#=========================================================================#
# Static Method:
# A method that does not use self or cls.
# It behaves like a normal function, but belongs to the class.

# Decorator:
# A special syntax (@) that tells Python to modify or extend how a function/method behaves.

class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    # Instance method accessing object attributes
    def show_details(self):
        print(self.name, self.marks)
    
    # @staticmethod tells Python that this method does not need self.
    @staticmethod
    def greet():    # This method is only for greeting, so no parameter.
        print("Hello")

s1 = Student("Prasoon", 45)

s1.show_details()

s1.greet() # Works because greet() is a static method.
Student.greet()  # Also works
#=========================================================================#