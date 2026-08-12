#=========================================================================#
# 08 - f-strings and .format() Method
#=========================================================================#
# String Formatting -> putting variable values inside strings
name = "Prasoon"
country = "India"
"Hey my name is Prasoon and I am from India"

# Through concatenation of strings
print("Hey my name is " + name + " and I am from " + country)

age = 19
# print("My age is " + age) # error as age is integer

#=========================================================================#
# .format() Method (important)
#=========================================================================#
letter = "Hey my age is {1} and I live in {0}"

# Without 1,0 it will give result in default order of written method i.e. from left to right.
# {} and {} are placeholders/replacement fields.
# {0},{1} -> Python replaces them with values from .format()
print(letter.format("India",100))

# Formatting Numbers
# .format() can also control appearance
price = 49.56879
print("Price is {:.2f}".format(price))
# Meaning:
# : -> formatting starts
# .2 -> 2 decimal places
# f -> float
 
#=========================================================================#
# Named Formatting
#=========================================================================#
letter = "Hey my name is {name} and I am from {country}"
print(letter.format(name="Prasoon",country="India"))
# This method is quite better than above methods as, the variables
# are placeholders and gets assigned in .format() method.

#=========================================================================#
# f-Strings
#=========================================================================#
# This method is introduced in Python 3.6 and most widely used today.
name = "Prasoon"
country = "India"

print(f"Hey my name is {name} and i am from {country}")

# f-strings can directly run expressions inside {}
a = 10
b = 20
print(f"Sum is {a+b}")

# Methods can be used inside f-strings
name = "Prasoon"
print(f"{name.upper()}")

price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt) # 49.10

print("")
#=========================================================================#
# Escaping Curly Braces
#=========================================================================#
# Escape means -> Treat special characters as normal text instead of giving it its special meaning.
name = "Prasoon"
# Single braces -> formatting
print(f"{name}") # Prasoon

# Double braces -> literal braces
print(f"{{name}}") # {name}

# Mixing Variables + Literal Braces
x = 10
print(f"Value = {{ {x} }}") # output -> Value = { 10 }

# Breakdown:
# {{  -> prints {
# {x} -> inserts variable value
# }}  -> prints }

# JSON style example
name = "Prasoon"
print(f'{{"name" : "{name}"}}') # # {"name": "Prasoon"}
#=========================================================================#