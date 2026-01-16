#04
#=========================================================================#
#Endswith() Function in Strings
str = "I am studing python from ApnaCollege"
print(str.endswith("ege")) #True
print (str.endswith("App")) #False
print("")
#=========================================================================#
#Capitalize() Function in Strings
str2 = "i am studing python from ApnaCollege"

print(str2.capitalize())
#Makes the First Character Upper Case
#and Rest Lower Case

print(str2)
#here the original string remains unchanged 

str2 = str2.capitalize()
print(str2)
#now the original string is changed and will have first letter capitalized always.

print("")
#=========================================================================#
#Replace() Function in Strings

str3 = "i am studing python from ApnaCollege"
print(str3.replace("o", "0"))
print("")
#=========================================================================#
#Find() Function in Strings
str4 = "I am studing python from ApnaCollege"
print(str4.find("o")) #gives index of first occurrence of o
print(str4.find("z")) #gives -1 if not found
print("")

#=========================================================================#
#Count() Function in Strings
str5 = "I am from studing python from ApnaCollege"
print(str5.count("from")) #gives count of occurrence of substring
print(str5.count("o"))
#=========================================================================#