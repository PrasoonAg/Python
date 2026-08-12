#=========================================================================#
# 02 - Public, Private Attributes & Private Methods
#=========================================================================#
# Public Attribute:
# Can be accessed and modified from outside the class.

# Private Attribute:
# Intended to be used only inside the class.
# Created using double underscore (__).
#=========================================================================#
# Public Attribute
class Student:
    
    def __init__(self, name):
        self.name = name     # Public Attribute
        
s1 = Student("Prasoon")

print(s1.name)   # Accessible from outside

s1.name = "King" # Can be modified from outside

print(s1.name)
# Public attributes can be accessed and modified from outside the class.

#=========================================================================#
# Private Attribute
class Account:

    def __init__(self, acc_no, acc_pass):

        self.acc_no = acc_no         # Public Attribute
        self.__acc_pass = acc_pass   # Private Attribute

    def reset_pass(self):
        # Private attribute can still be accessed inside the class
        print(self.__acc_pass)

s1 = Account(23232, "abcd123")

print(s1.acc_no)   # Public attribute

# print(s1.__acc_pass)
# ERROR: Cannot access private attribute directly

s1.reset_pass()    # Accessing private data through a method

#=========================================================================#
# Private Method:
# A method intended to be used only inside the class.
# Created using double underscore (__).
# Private methods are helper methods meant for internal use inside the class.
class Person:
    __name = "anonymous" # Private Attribute

    def __hello(self):   # Private Method
        print("hello person!")

    # Public method accessing a private method
    def welcome(self):
       self.__hello()

p1 = Person()

# print(p1.__name)
# ERROR: Cannot access private attribute directly

# print(p1.__hello())
# ERROR: Cannot access private method directly

p1.welcome()  # Works because welcome() is a public method
#=========================================================================#