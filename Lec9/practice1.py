# 12
# P-1
#=========================================================================#
#Practice Questions
#=========================================================================#
#@1# Define a Circle class to create a circle with radius r using the constructor.
# Define an Area() method of the class which calculates the area of the circle.
# Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

# by me
import math # import loads another Python module/file so we can use its features.
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def Area (self):
        print("Area of Circle is", math.pi * self.radius * self.radius)
    
    def perimeter(self):
        print("perimeter of Circle is", 2 * math.pi * self.radius)

circle1 = Circle(4)
circle1.Area()
circle1.perimeter()

# by apna college
class Circle1:
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 2 * (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
c1 = Circle1(43)
print(c1.area())
print(c1.perimeter())

#=========================================================================#
#@2# Define a Employeee class with attributes role, department & salary. This class also has showDetails() method.
# Create an Engineer class that inherits properties from Employee & has additional attributes : name & age.

print("")
class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
    
    def showDetails(self):
        print("role =", self.role)
        print("department =", self.department)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")

engg1 = Engineer("Elon Musk","40")
engg1.showDetails()

# e1 = Employee("Ai enginner","CSE","2 crore")
# e1.showDetails()

#=========================================================================#
#@3# Create a class called Order which stores item & its price.
# Use Dunder function __gt__() to convey that:
    #order1> order2 if price opf order1> price of order2

class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
    
    def __gt__(self,b):
        return self.price>b.price

odr1 = Order("Chips",30)
odr2 = Order("coffee", 20)

print(odr1 > odr2)
#=========================================================================#