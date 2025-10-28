#04
input("Enter your name:") #Taking input from user

#=========================================================================#
name = input ("Enter your Name:")
print("Welcome", name)
age = input ("Enter your Age:")
print("Your age is :", age)

#=========================================================================#
#Note: Input function takes input as string by default 
#even if user enters a number it will be taken as string
#To verify this we can use type() function
val = input ("Enter some value:")
print (type (val) , val)

#=========================================================================#
#To take integer or float input from user we need to do type casting
name = input ("Enter your Name:") #string by default
age = int(input ("Enter your Age:")) #type casting to int (Explicit conversion)
marks = float(input ("Enter your Marks:")) #type casting to float (Explicit conversion)
print ("Name =", name)
print ("Age =", age)
print ("Marks =", marks)