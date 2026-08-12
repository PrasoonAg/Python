#=========================================================================#
# 02 - Lambda Functions
#=========================================================================#
# Lambda is a small anonymous function created using the 'lambda' keyword.# syntax:
# because technically a lambda is an anonymous function (a function without a formal def name).
# lambda paramters : expression
# lambda can take multiple paramters

# Creating a function for squaring numbers
def square(n):
    return n*n
print(square(4))

square =  lambda x: x*x 
print(square(3))

# Creating a function for total
add = lambda a,b,c: a+b+c
print(add(12,13,8))

# Lambdas are used when you need a short function temporarily.
numbers = [1,2,3,4]
squared = list(map(lambda x: x*x, numbers))
print(squared)
#=========================================================================#