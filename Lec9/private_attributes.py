#=========================================================================#
# 03 - Private(Like) Attributes and Methods
#=========================================================================#
class Person:
    __name = "anonymous" # attribute
    
    def __hello(self): # private function
        print("hello person!")
        
    # question arise why made these type of functions?
    # so it could be used by another function
    def welcome(self):
       self.__hello()
    
    #why this is done?
    # this is done to make the data secure and prevent exposing instance attribute of the class.

p1 = Person() # private
# print(p1.__name) # error

# print(p1.__hello()) # private method # error
print(p1.welcome()) # no error
