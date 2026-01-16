#02
#Arithmetic Operators
a = 5
b = 2

print (a + b)
print (a -  b)
print (a * b)

print (a ** b)
#Exponentiation operator gives a raised to the power b

print (a/b)
#Intresting thing to notice here is that the division    always give float vaule , even if both the numbers are integers. If i do 4/2 it will give 2.0 not 2.

print (a % b)
#Modulus operator gives the remainder

print (a // b)
#Floor division operator gives the integer part of the division

#=========================================================================#

#Comparison/Relational Operators (Answers will be boolean values True or False)
a = 50
b = 20
print (a == b) #false
print (a != b) #true
print (a >= b) #true
print (a <= b) #false
print (a > b)  #true
print (a < b)  #false

#=========================================================================#
#Assignment Operators
num = 10
num = num + 10 # 10 + 10 = 20
print ("num : ", num)

#===#
num = 10
num += 10     # num = num + 10  => 10 + 10 = 20
print ("num : ", num)

#===#
num = 10
num -= 10    # num = num - 10  => 10 - 10 = 0
print ("num : ", num)

#===#
num = 10
num *= 5    # num = num * 5  => 10 * 5 = 50
print ("num : ", num)

#===#
num = 10
num /= 5 #num = num / 5 => 10 / 5 = 2.0
print ("num : ", num)

#===#
num = 10
num %= 3 #num = reminder when num is divided by 3 => 10 % 3 = 1
print ("num : ", num)

#===#
num = 10
num **= 2 # num = 10^2 => 10^2 = 100
print ("num : ", num)

#=========================================================================#
#Logical Operators (it works with boolean values)
print (not False) #True
print (not True)  #False

a = 50
b = 20
print (not a>b) #False

val1 = True
val2 = False
print ("and operator :" , val1 and val2) #False
#Basically, for 'and' operator, True True = True , False False = False , ## True False = False , False True = False ##

print ("or operator :", val1 or val2) #True
#Basically, for 'or' operator, True True = True , False False = False ,
## True False = True , False True = True ##

#Example
print ("and operator :", (a==b) and (a>b) ) #False
print ("or operator :", (a==b) or (a>b) ) #True