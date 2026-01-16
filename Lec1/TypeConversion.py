#03
#=========================================================================#
#TYPE CONVERSION
a = 2 #type int
b = 4.25 #type float
sum = a + b
#Here python automatically converts int to float i.e 2 to 2.0 and then does the addition
print("Sum is : ", sum)

#=========================================================================#
#Type Casting (Manual Conversion)
a = float("2")  # string => float conversion
b = 4.25         # type float
print(a + b)    # Output: 6.25
#===#
a = 3.14
a = str (a) # float => string conversion
print(type(a)) # Output: <class 'str'>

#=========================================================================#
#some more ways to type code
#1
a,b = 5, "2"
print (int(b)+a) #string b is converted to int and then added to a
print (float(a)+float(b)) #both a and b are converted to float and then added

#=========================================================================#
#2
a,b =int("5"),2 #string "5" is converted to int type
print(a+b)

#=========================================================================#
#3
a = float("2")
b = 4.25
print (type(a)) #type of a is float
print (a + b) #addition of two float numbers