#=========================================================================#
# 09 - Propetry
#=========================================================================#
# Propetry:
# → allows a method to be used like an attribute (no brackets needed)
# → used when value depends on other variables and should update automatically


# Decorator : a function that wraps another function to add extra behavior without changing its original code.
# Written using @, e.g. @staticmethod, @classmethod.

#=========================================================================#
# CASE 1: Problem (Fixed value, not updating)
#=========================================================================#
class Student1:
    def __init__(self,phy,chem,maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        # percentage calculated once and stored (static value(unchangable value))
        self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"

stu1 = Student1(98,97,99) 
print(stu1.percentage) # 98.0%

stu1.phy = 86 # marks changed
print(stu1.phy) # 86
print(stu1.percentage) # 98.0% # old value, not updated automatically

# for the cases where we cant give fixed values
#=========================================================================#
# CASE 2: Manual update using method
#=========================================================================#
class Student2:
    def __init__(self,phy,chem,maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        # inital calculation
        self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"
    
    def calcPercentage(self):
        # manually recalculate percentage
        self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"

stu2 = Student2(98,97,99)
print(stu2.percentage)

stu2.phy = 86
stu2.calcPercentage() # must call manually
print(stu2.percentage) # 94%
#=========================================================================#
# CASE 3: Using @property (BEST APPROACH)
#=========================================================================#
class Student3:
    def __init__(self,phy,chem,maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
    
    @property # methods behaves like attribute (just accessed like attribute)
    def percentage(self): # method internally
        # calculated every time it is accessed (always updated)
        return str((self.phy + self.chem + self.maths)/3) + "%"

stu3 = Student3(98,97,99)
print(stu3.percentage) # 98.0%

stu3.phy = 32          # change marks
print(stu3.percentage) # 76% automatically updated
#=========================================================================#
# FINAL UNDERSTANDING
#=========================================================================#
# without @property:
# → value stored once → becomes outdated

# with @property:
# → value calculated dynamically → always correct

# Key benefit:
# → use method like attribute (stu3.percentage, not stu3.percentage())

#=========================================================================#
# memory line
#=========================================================================#
# @property → method behves like attribute + always up-to-datei