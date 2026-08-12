#=========================================================================#
# 08 - Class Methods
#=========================================================================#
# Class Method:
# A method that works with the class itself, not a specific object.
# It receives the class as its first parameter (commonly named cls).
# Class methods are commonly used to access or modify class attributes.
# They are the recommended way to perform operations related to the class itself.

# Method Comparison:
# Instance Method -> Works with a specific object (self).
# Class Method    -> Works with the class itself (cls).
# Static Method   -> Works independently of both object and class.
#=========================================================================#
# CASE 1: Instance Method
#=========================================================================#
class Person1:
    name = "Anonymous" # Class Attribute

    def changeName(self, name): # Instance Method
        # Creates/updates an Instance Attribute
        # The Class Attribute remains unchanged
        self.name = name

p1 = Person1()

p1.changeName("Prasoon")

print(p1.name)      # Prasoon (Instance Attribute)
print(Person1.name) # Anonymous (It does NOT modify the Class Attribute)

print("\n")
#=========================================================================#
# CASE 2: Modifying Class Attribute using Class Name
#=========================================================================#
class Person2:
    name = "Anonymous"

    def changeName(self, name):
        # Directly modifies the Class Attribute using the class name
        Person2.name = name
        
p2 =  Person2()

p2.changeName("Prasoon Agrawal")

print(p2.name)      # Prasoon Agrawal
print(Person2.name) # Prasoon Agrawal

print("\n")
#=========================================================================#
# CASE 3: Modifying Class Attribute using self.__class__
#=========================================================================#
class Person3:
    name = "Anonymous"

    def changeName(self, name):
        # self.__class__ refers to the class of the current object
        self.__class__.name = name

p3 = Person3()

p3.changeName("Prasoon Agrawal")

print(p3.name)
print(Person3.name)

print("\n")
#=========================================================================#
# CASE 4: Proper Way using @classmethod
#=========================================================================#
class Person4:
    name = "Anonymous"

    @classmethod
    def changeName(cls, name): 
        # cls refers to the class itself
        # Recommended way to modify Class Attributes.
        cls.name = name

p4 = Person4()

p4.changeName("Alex")

print(p4.name)
print(Person4.name)
#=========================================================================#
# Which one should you use?
# self.name        -> Modify an Instance Attribute.
# Person.name      -> Modify a Class Attribute using the class name.
# self.__class__   -> Modify a Class Attribute using the object's class.
# @classmethod     -> Recommended way to work with Class Attributes.
#=========================================================================#