#01
#=========================================================================#
#STRINGS IN PYTHON
#=========================================================================#
str1 = "This is a string."
str2 = 'This is also a string.'

str3 = """This is a multi-line string.
It can span multiple lines."""
str31= """He said, "It's awesome!" """
#Also allows both single and double quotes inside without escaping:

str4 = "This is Prasoon's Code " #double quotes outside as python gets confused with single quote inside
str5 = 'This is Prasoon"s Code '

#=========================================================================#
#Escape Sequences Characters 
# (\n {for next line} and \t {for tab space})
str6 = "This is a String\nWe are creating in the python."
print (str6)
#This gives a new line after "String"

str7 = "This is a String\tWe are creating in the python."
print (str7)
#This gives a tab space after "String"

#=========================================================================#
#Concatenation of Strings AND # Length of Strings
str8 = "Prasoon"
str9 = "is a coder."
print(str8+str9)
print(len(str8))
#====#
final_str = str8 + str9
print (final_str)
print (len(final_str))
#====#
str10 = "Hello"
str11 = "World"
final_str2 = str10 + " " + str11 # Adding space b/w Strings
print (final_str2)
print (len(final_str2))
#=========================================================================#