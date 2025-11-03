#04
#=========================================================================#
#Tuples in Python
#=========================================================================#
tup1 = (2,1,3,1)
print(tup1[0])
print(tup1[1])
print("")
##tup [0]= 5 #This operation is not allowed as Tuples are IMMUTABLE (Same thing happens in String (as there are also IMMUTABLE))
#=========================================================================#
tup2 = () #Empty Tuple
print(tup2) #Valid
print(type(tup2))
print("")
#=========================================================================#
tup3 = (1,) #single element tuple
print(tup3)
print(type(tup3))
print("")
#=========================================================================#
tup4 = (1) #If done without commma then python will consider this as an integer
print(tup4)
print(type(tup4)) #integer
print("")
#=========================================================================#
tup5=(1,2,3,4,) #not nesseary to add comma at the end
print(tup5)
print(type(tup5))
print("")
#=========================================================================#
tup6=(1.0) #Considered as float
print(tup6)
print(type(tup6)) #float
print("")
#=========================================================================#
tup7 = ("hello") #This will be considered as String (str)
print(tup7)
print(type(tup7)) #str
print("")
#=========================================================================#
tup8 = ("hello",) #Comma added then ==> tuple
print(tup8)
print(type(tup8)) # tuple
print("")
#=========================================================================#
tup9 = (1,2,3,4)
print(tup9)
print(type(tup9)) #tuple
print("")
#=========================================================================#