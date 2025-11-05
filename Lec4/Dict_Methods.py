#03
#=========================================================================#
# Dictionary Methods
#=========================================================================#
student = { #Dictionary
    "name" : "Raghav Singh",
    "subjects" : { #Nested Dictionary
        "chem" : 95,
        "phy" : 92,
        "maths" : 89,
    }
}
#=========================================================================#
#keys
#=========================================================================#
print(student.keys(),"\n")
print(type(student),"\n") # <class 'dict'>

#===#
#Type Casting to the List
print(list(student.keys()),"\n") # This will give the data in list format (type casting).

print(type(list(student.keys())),"\n") # <class 'list'>

#===#
print(type(len(student)),"\n") #Length --> 2 
#workflow ==> Dictionary → count keys using len() → get 2 → check type → <class 'int'>.

#===#
print(len(list(student.keys())),"\n")
#workflow ==> Dictionary → get keys using .keys() →gives a dict_keys(['name', 'subjects']) → convert keys to list → ['name', 'subjects'] → count items using len() → get 2

#=========================================================================#
#values
#=========================================================================#
#HAVE TO UNDERSTAND THIS BLOCK AGAIN!!!
print(student.values(),"\n")
print(type(student.values),"\n") # <class 'builtin_function_or_method'>

#=========================================================================#
print(list(student.values()),"\n") # This will print in list type
print (type(list(student.values())),"\n") # <class 'list'>

#=========================================================================#
#items ==> all pairs will be returned
#=========================================================================#
print(student.items,"\n") # prints method object ==> <built-in method items of dict object at 0x000001CF440BD3C0>
print(student.items(),"\n") # executes the method → returns dict_items([...])

# When you don’t use parentheses (), you’re just referring to the method itself — like pointing at a tool but not using it yet.

# When you do use parentheses (), you’re calling (executing) that method — actually using the tool to get a result.

#=========================================================================#

print(type(student.items()),"\n")
print(list(student.items()),"\n") #The list contains tuples , where each tuple = (key, value) pair.

pairs = list(student.items())
print(pairs[0],"\n")

#=========================================================================#
# get
#=========================================================================#
#Learn these following codes like in difference b\w.

print(student["name"]) # Raghav Singh
print(type(student["name"]),"\n") #<class 'str'>
#print(student["name2"]) #error as key is missing.

print(student.get("name")) # Raghav Singh
print (type(student["name"]),"\n") #<class 'str'>

print(student.get("name2"),"\n") # no error ==> none
#never use [] to call a method , use () to execute it.

#=========================================================================#

print("BEFORE")
# print(student["name2"]) #error
print(student.get("name2")) #while this will not, as it is method.
print("After\n")

#=========================================================================#
# update (adding new key-value pair or overiding the exisisting one.)
#=========================================================================#
student.update({"city" : "Delhi"}) #Added city key and value Delhi.
pair1 =(list(student.items()))
print(pair1[2],"\n") #To print only city.

new_dict1 = {"landmark" : "India Gate" , "Friend" : "Rachit Agrawal"} # can add more items by using ,
student.update(new_dict1)
print(student,"\n")

# print(student.update({"name" : "Prasoon Agrawal"}),student,"\n") #none starting mai kyo de raha hai??

new_dict2 = {"name" : "Bruce Wayne"} # overiding "name"
student.update(new_dict2)
print(student)

#=========================================================================#