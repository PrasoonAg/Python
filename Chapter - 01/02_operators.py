#=========================================================================#
# 02 - Operators
#=========================================================================#
# Arithmetic Operators
a = 5
b = 2

print (a + b)
print (a -  b)
print (a * b)

print (a ** b) # Exponentiation Operator -  gives a raised to the power b

print (a/b) # Divsion Operator - gives always the output in float i.e. 2.5, 2.0 etc

print (a % b) # Modulus / Modulo operator - gives the remainder

# Common Uses of Modulo (%)
# Modulo is commonly used for checking divisibility and creating repeating or circular patterns.

# Check even/odd
10 % 2 == 0      # True

# Check divisibility
15 % 5 == 0      # True

# Create repeating/circular patterns
(25 + 5) % 26    # 4

print (a // b) # Floor division operator -  gives the integer part of the division

# PEDMAS or P-E-DM-AS (Left to Right)
# It basically states the order of priority is Parentheses, Exponents, Multiplication,
# Division, Addition and Subtraction.
# ()
# **
# * OR /
# + OR -

print(3 * 3 + 3/3 - 3) # 7.0
# The calculation occurs form left to right
# 3*3 = 9 and 3/3 = 1.0
# 9 + 1.0 = 10.0
# 10.0 - 3 = 7.0

# changing the above code to get the output 3
print(3 * (3 + 3) /3 - 3)

#=========================================================================#
# Comparison/Relational Operators (Answers will be boolean values True or False)
a = 50
b = 20
print (a == b) # False
print (a != b) # True
print (a >= b) # True
print (a <= b) # False
print (a > b)  # True
print (a < b)  # False

#=========================================================================#
# Assignment Operators
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
num /= 5 # num = num / 5 => 10 / 5 = 2.0
print ("num : ", num)

#===#
num = 10
num %= 3 # num = reminder when num is divided by 3 => 10 % 3 = 1
print ("num : ", num)

#===#
num = 10
num **= 2 # num = 10^2 => 10^2 = 100
print ("num : ", num)

#=========================================================================#
#Logical Operators (it works with boolean values) - not, and, or
#=========================================================================#
# not Operator - logical negation
print (not False) # True
print (not True)  # False

a = 50
b = 20
print (not a>b) # False

is_logged_in = False
if not is_logged_in:
    print("Please login")
#=========================================================================#
# and Operator 
val1 = True
val2 = False
print ("and operator :" , val1 and val2) # False
# Basically, for 'and' operator, True True = True , False False = False, ## True False = False, False True = False

# or Operator
print ("or operator :", val1 or val2) #True
# Basically, for 'or' operator, True True = True , False False = False ,
# True False = True , False True = True #
#=========================================================================#
# Example
print ("and operator :", (a==b) and (a>b) ) # False
print ("or operator :", (a==b) or (a>b) )   # True
#=========================================================================#