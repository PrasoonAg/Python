#03
#=========================================================================#
# Default Parameters
#=========================================================================#

#=========================================================================#
# This is for understanding the concept not acutal part of topic.
# Case 1:
#=========================================================================#
def add(a, b):
    print(a + b)

add(5,5) #output 10

#=========================================================================#
x = add(5,5)
print(x) # output 10 none

# Why?
# Because add() printed 10 but returned nothing, so Python automatically returns None.

#=========================================================================#
# This is for understanding the concept not acutal part of topic.
# Case 2:
#=========================================================================#
def add(a,b):
    return a + b

add(5, 5)
#Nothing shows up on screen (because we didn't print)
#but

x = add(5, 5)
print(x)
#Now the value is stored in x because of return.

#=========================================================================#
# Back to the Topic : Default Parameters
#=========================================================================#
def cal_prod(a,b):
    print(a*b) # shows result
    return a * b # gives result back
#cal_prod() #This will give an error as missing 2 required positional arguments: 'a' and 'b'.

x = cal_prod(2,3) # Here, First 6 is printed from function.

print(x) # Here, Secound 6 is printed from print().
print("")
#=========================================================================#
def cal_multi(x=1, y=1): # Assiging default vaules, when there is no argument is passed.
    print(x*y)
    return x*y

cal_multi() # No Argument here
# will give output 1

#=========================================================================#
def cal_multi2(x,y=2): #Default arguments must come after non-default arguments i.e.(x=2,y) this will give error
                      # Why does Python enforce this?
                      #Because when calling the function, Python won’t know which argument you meant.
                      #This cal_multi2(,3) is not valid Python syntax.
    print(x*y)
    return x*y

cal_multi2(4) # here x=4 and y=2(default)
cal_multi2(y=2,x=3) # here assaigned both
#=========================================================================#