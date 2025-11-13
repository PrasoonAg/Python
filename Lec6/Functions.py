#01
#=========================================================================#
#Functions
#=========================================================================#

# a = 5
# b = 3
# sum = a+b
# print(sum)

# # some lines of code

# a = 6
# b = 2
# sum = a + b
# print(sum)

# # some lines of code

# a = 7
# b = 5
# sum = a + b
# print(sum)

# # from above observation one can see we call sum again and agin this makes code looks redundant to avoid this we use functions.

#=========================================================================#
def calc_sum(a,b):
    sum = a + b
    print(sum)
    return sum

calc_sum(5,3)
#some lines of codes

calc_sum(6,2)
#some lines of codes

calc_sum(7,5)
#some lines of codes

# Now, the lines of code became redudant and this too make code of lines less.
print("")

#=========================================================================#
#function defination
def calc_sum1(a,b): #parameters(taking input)
    return a+b # for output

sum = calc_sum1(4,5) #9 #function call #4,5 is called arguments
print(sum)
print("")
#=========================================================================#
def print_hello(): #no parameters(taking inputs) are allowed
    print("hello")
#no returns(no output) are allowed function

print_hello()

output = print_hello()
print(output) #not returning anything so 'None' came.

#=========================================================================#
#average of 3 numbers
def average(a,b,c):
    value =float((a+b+c)/3)
    print(value)
    return value
average(4,5,3)
