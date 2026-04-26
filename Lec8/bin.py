# class Car:
#     def __init__(self,name): #constructor
#         self.name = name # storing data in object
        
#     def start(self): #method
#         print(self.name,"started")
        
#     def stop(self): #method
#         print(self.name,"Stopped")
# c1 = Car("lambo")
# c1.start()
# c1.stop()

class A:
    def __init__(self,x):
        self.x = x
        
    def show(self):
        print(self.x)

a1 = A(10)
a1.show()

class Student:
    def __init__(self,X):
        self.X = X
        
    def show(self):
        print(self.X)
        
s1 = Student("prasoon")
s1.show()