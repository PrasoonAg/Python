#=========================================================================#
# 08 - Property (@property)
#=========================================================================#
# Property (@property):
# Allows a method to be accessed like an attribute (no parentheses needed).
# Commonly used when a value is calculated from other attributes and should always reflect their latest values.

# Decorator:
# A special syntax (@) that modifies or extends the behavior of a function or method.
# Examples: @staticmethod, @classmethod, @property.
#=========================================================================#
# CASE 1: Storing a Fixed Value (Problem)
#=========================================================================#
class Student1:
    
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        # Percentage is calculated only once during object creation
        self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"

stu1 = Student1(98, 97, 99)

print(stu1.percentage) # 98.0%

stu1.phy = 86 # Marks changed

print(stu1.phy) # 86
print(stu1.percentage) # 98.0% (Old value - not updated)
# Problem:
# The percentage was stored as a fixed value.
# Changing the marks does not automatically update it.
#=========================================================================#
# CASE 2: Manual update using Method
#=========================================================================#
class Student2:
    
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        
        # Inital calculation
        self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"
    
    def calcPercentage(self):
        # Recalculate percentage manually
        self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"

stu2 = Student2(98, 97, 99)

print(stu2.percentage)

stu2.phy = 86

stu2.calcPercentage() # Must be called every time marks change.

print(stu2.percentage) # 94%
# Drawback:
# Easy to forget calling calcPercentage(), resulting in outdated data.
#=========================================================================#
# CASE 3: Using @property (BEST APPROACH)
#=========================================================================#
class Student3:
    
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
    
    @property
    def percentage(self):
        # Calculated every time it is accessed,
        # so it always reflects the latest marks.
        return str((self.phy + self.chem + self.maths)/3) + "%"

stu3 = Student3(98, 97, 99)

print(stu3.percentage) # Accessed like an attribute

stu3.phy = 32          # Marks changed

print(stu3.percentage) # Automatically updated
# Advantage:
# No need to store or manually update the percentage.
# It is always calculated using the latest marks.
#=========================================================================#