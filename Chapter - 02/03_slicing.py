#=========================================================================#
# 03 - Slicing of Strings
#=========================================================================#
str = "apna college"
print(str[1:4])

#====#
str2 = "apna college"
print(str2[1:5])
print(str2[5:12])

print(str[:2])   # start to index 2
print(str2[0:2]) # same as above

print(str2[5:]) # index 5 to end of string
print(str2[5:len(str2)]) # same as above

print(len(str2[5:12]))

#=========================================================================#
# Negative Indexing
#=========================================================================#
str3 ="Apple"
print(str3[-3:-1]) #'pl'

# Remember that the in negative indexing, the -1 index is excluded.
#=========================================================================#