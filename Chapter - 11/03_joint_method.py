#=========================================================================#
# 03 - Join() Method (Strings)
#=========================================================================#
# join() combines elements of an iterable into a single string.
# The string before .join() acts as the separator.
# All elements must be strings, otherwise join() raises TypeError.

a = ["Prasoon","Rohan","Shub","Max"]

final = ",".join(a) # Prasoon,Rohan,Shub,Max
print(final)
print(type(final)) # <class 'str'>


a = ["Prasoon", 10, "Max"]
",".join(a)   # Error
#=========================================================================#