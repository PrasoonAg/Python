#04
#=========================================================================#
# Set in Python => Each vaule should be unique.
#=========================================================================#
collection = {1,2,3,4,"hello","world"}
#only values are stored # Set property = Unordered + Unqiue Elements

#The Python set uses a hashing mechanism internally to store elements.

# Numbers like 1, 2, 3, 4 have simple hash values, so they often appear in ascending order by chance.

# Strings like "hello" and "world" have different hash values, so their order depends on the internal hashing — it looks “random.”

print (collection)
print(type(collection),"\n") # <class 'set'>

#=========================================================================#
collection2= {1,2,2,2,"world", " hello" , "world" , 4}
# Duplicate vaules will be printed once.
print(collection2)
print(len(collection2),"\n") #Duplicate vaules will be counted only once.

#=========================================================================#
#Empty Set

null_Dicationary={}
print(type(null_Dicationary)) # <class 'dict'>
#This is creating the dicationary not a Set.

null_Set = set() #empty set; syntax
print(type(null_Set)) # <class 'set'>
#=========================================================================#