#=========================================================================#
# 08 - class method
#=========================================================================#
# A class method:
# → is bound to the class (not object)
# → takes 'cls' as first parameter (represents the class)
# → used to modify class attributes

# Note:
# static method → cannot access/modify class or instance data
# class method  → can access/modify class data

#=========================================================================#
# CASE 1: Instance method modifying attribute
#=========================================================================#
class Person1:
    name = "anonymous" # class attribute

    def changeName(self,name): # instance method
        # This creates/changes INSTANCE attribute inside object, not class attribute
        self.name = name

p1 = Person1()
p1.changeName("prasoon")

print(p1.name) # prasoon (instance attribute)
print(Person1.name) # anonymous (class attrubute unchanged)

print("\n")

#=========================================================================#
# CASE 2: Modifying class attribute using class name
#=========================================================================#
# so what we do is:
# Method 1:
class Person2:
    name = "anonymous"
    
    def changeName(self,name):
        # Directly modifying class attribute using class name
        Person2.name = name
        
p2 =  Person2()
p2.changeName("Prasoon Agrawal")

print(p2.name)      # Prasoon Agrawal
print(Person2.name) # Prasoon Agrawal

print("\n")

#=========================================================================#
# CASE 3: Using __class__ to access class
#=========================================================================#
# Method 2:

class Person3:
    name = "anonymous"
    
    def changeName(self,name):
        # self.__class__refers to the class of the object
        self.__class__.name = name

p3 = Person3()
p3.changeName("Prasoon Ag")

print(p3.name)
print(Person3.name)

print("\n")

#=========================================================================#
# CASE 4: Proper way using @classmethod
#=========================================================================#
# Method 3:

class Person4:
    name = "anonymous"
    
    @classmethod
    def changeName(cls,name): # cls referring to the class itself
        cls.name = name       # modifies class attribute

p4 = Person4()
p4.changeName("Alex")

print(p4.name)
print(Person4.name)

#=========================================================================#
# WHEN TO USE WHAT
#=========================================================================#
# 1. Instance Method (self)
# → when working with object-specific data

# 2. Class Method (cls)
# → when working with class-level data

# 3. Static Method
# → when no class or object data is needed (utility function)