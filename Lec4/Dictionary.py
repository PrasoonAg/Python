#01
#=========================================================================#
#Dicationary
#=========================================================================#
info = {
    
    "key" : "value",
    
    "name" : "apna collage",
    "learning" : "coding",
    "age" : 99, #integer
    "is_adult" : True, #boolean value
    "marks" : 94.4, #float
    "subjects" : ["python","java","C"], #list
    "topics" : ("dict", "set"), #tuple
    12.99 : 94.4
#keys must be immutable.
}
print(info)
print(type(info),"\n")

print(info["name"])
print(info["topics"])
print(info["name"])
print(info["age"])
#print(info["surname"]) #This will give error as key doesn't exist

info["name"] = "Prasoon" #name already exist so, now values get updated
info["learnig"] = 23
info["surname"] = "Agrawal"
print (info)

#=========================================================================#
null_dict = {} #It is an null dictionary
null_dict["name"]= "apnacollage"
print(null_dict)

#=========================================================================#