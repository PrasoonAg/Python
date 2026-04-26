#=========================================================================#
#02# - CONSTRUCTOR & SELF EXPLANATION
#=========================================================================#
# A constructor is a special method: __init__(). All classes have this.
# It runs automatically when an object is created

# creating class
class Student:
    name = "Karan Kumar"  # class attribute (same for all objects)
    
    def __init__(self): # self = current object being created & #iniit - initialization
        
        print(self) # prints the memory address of the object
        # object hi hai object at 0x000002C0D94686E0>
        print("creating new student in Database..")
        
# _init_() function will always be executed wheater written or not. i.e. there will be always be a conctructor for us.
s1 = Student() #internally self hi hai object at 0x000002C0D94686E0>
print(s1, "\n")

#=========================================================================#
# IMPORTANT NOTE
#=========================================================================#

# Even if you DO NOT write __init__(), Python still provides a default one
# But that default constructor does NOTHING (no initialization)

# So:
# __init__ is NOT compulsory to write
# But we write it when we want to initialize data
#=========================================================================#

#===#
class Student:
    
    #default constructors
    def __init__(self):
        pass
    
    
    # paramterized constructors (takes values during object creation)
    def __init__(self1,fullname,marks): # self = current object (VERY IMPORTANT)
        
        self1.name = fullname  # object attribute (different for each object)
        self1.marks = marks    # object attribute
        
# creating objects
s1 = Student("karan","25")
print(s1.name) # karan

s2 = Student("arjun","25") 
print(s2.name, s2.marks) # arjun 25

# s1 and s2 are objects
# attributes are like s2.name, s2.marks
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
#=========================================================================#
# self:
# - refers to the current object
# - used to store/access object-specific data

# Without self:
# - data will NOT be stored in the object
# - methods cannot access object data properly
#=========================================================================#
# WHAT HAPPENS IF self IS NOT WRITTEN?
#=========================================================================#
class Test:
    def __init__(): # missing self
        print("Hello")
        
# t1 = Test()
# ERROR: Python automatically passes object, but function not expecting it.

#=========================================================================#
# FINAL SUMMARY (WRITE THIS IN NOTES)
#=========================================================================#
# __init__:
# → special method (constructor)
# → runs automatically when object is created
# → used to initialize object data

# self:
# → represents current object
# → must be first parameter in methods
# → used to access/store object attributes

# class attribute:
# → same for all objects

# object attribute:
# → different for each object