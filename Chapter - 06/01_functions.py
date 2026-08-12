#=========================================================================#
# 01 - Functions
#=========================================================================#
# A function is a reusable block of code that performs a specific task.

a = 5
b = 3
sum = a+b
print(sum)

# some lines of code

a = 6
b = 2
sum = a + b
print(sum)

# some lines of code

a = 7
b = 5
sum = a + b
print(sum)

# from above observation one can see we call sum again and agin this makes code looks redundant
# to avoid this we use functions.

#=========================================================================#
# Defining a function
def calc_sum(a,b): # here a and b are Parameter(placeholder)
    sum = a + b
    print(sum)
    return sum

# Calling that function
calc_sum(5,3) # 5, 3 are an argument.
# some lines of codes

calc_sum(6,2)
# some lines of codes

calc_sum(7,5)
# some lines of codes

# Now the code is less redundant and more reusable.
print("")

#=========================================================================#
# Function Defination
def calc_sum1(a,b): # parameters(taking input)
    return a+b # for output
# return will give result
# while if used print() it will show result
# return -> sends result
# print() -> shows result

sum = calc_sum1(4,5) #9 # function call # 4,5 is called arguments
print(sum)
print("")

#=========================================================================#
def print_hello(): # no parameters are used
    print("hello")
# function without a return value

print_hello()

output = print_hello() # output = None
print(output) #not returning anything so 'None' came.
# Function reaches end without return
# Python automatically does : return none
#=========================================================================#
# average of 3 numbers
def average(a,b,c):
    value =float((a+b+c)/3)
    print(value)
    return value
average(4,5,3)

#or by mam

def cal_avg(a,b,c):
   # if (a==0):  # Conditional statments can be used in loops also, with
   # proper indentation.
    sum = a + b + c
    avg = sum/3
    print(avg)
    return avg

cal_avg(1,2,3)
#=========================================================================#