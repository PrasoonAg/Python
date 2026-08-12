#=========================================================================#
# 03 - Dictionary Methods
#=========================================================================#
student = {
    "name" : "Prasoon Agrawal",
    "subjects" : {
        "chem" : 95,
        "phy" : 92,
        "maths" : 89,
    }
}

#=========================================================================#
# keys
#=========================================================================#
print(student.keys(),"\n")       # gives data of keys
print(type(student.keys()),"\n") # <class 'dict_keys'>
print(type(student.keys),"\n")   # <class 'builtin_function_or_method'>
#===#
# Type Casting to the List
print(list(student.keys()),"\n") 
# This will give the data(keys) in list format (type casting).
print(type(list(student.keys())),"\n") # <class 'list'>

#===#
print(type(len(student)),"\n") # Length --> 2 
# workflow ==> Dictionary → count keys using len() → get 2 → check type → <class 'int'>.
#===#
print(len(list(student.keys())),"\n")
# workflow ==> Dictionary → get keys using .keys() →gives a dict_keys(['name', 'subjects']) → convert keys to list → ['name', 'subjects'] → count items using len() → get 2

#=========================================================================#
# values
#=========================================================================#
print(student.values(),"\n")        # gives data of values
print(type(student.values()),"\n")  # <class 'dict_values'>
print(type(student.values),"\n")    # <class 'builtin_function_or_method'>
#===#
# Type Casting to the List
print(list(student.values()),"\n") # This will give the data(values) in list format (type casting).
print (type(list(student.values())),"\n") # <class 'list'>

#===#
print(type(len(student)),"\n") #Length --> 2 
# workflow ==> Dictionary → count keys using len() → get 2 → check type → <class 'int'>.
#===#
print(len(list(student.values())),"\n")
# workflow ==> Dictionary → get values using .values() →gives a dict_values(['Prasoon Agrawal', {'chem': 95, 'phy': 92, 'maths': 89}]) → convert keys to list → ['Prasoon Agrawal', {'chem': 95, 'phy': 92, 'maths': 89}] → count items using len() → get 2

#=========================================================================#
# items ==> all pairs will be returned
#=========================================================================#
print(student.items,"\n")   # prints method object ==> <built-in method items of dict object at 0x000001CF440BD3C0>
print(student.items(),"\n") # executes the method → returns dict_items([...])

# When you don’t use parentheses (), you’re just referring to the method itself — like pointing at a tool but not using it yet.

# When you do use parentheses (), you’re calling (executing) that method — actually using the tool to get a result.
#===#
print(type(student.items()),"\n") # <class 'dict_items'>
print(list(student.items()),"\n") # The list contains tuples , where each tuple = (key, value) pair.

pairs = list(student.items())
print(pairs[0],"\n")

#=========================================================================#
# get
#=========================================================================#
# Learn these following codes like in difference b\w.

print(student["name"]) # Prasoon Agrawal
print(type(student["name"]),"\n") # <class 'str'>
# print(student["name2"]) #error as key is missing.

print(student.get("name")) # Prasoon Agrawal
print (type(student["name"]),"\n") # <class 'str'>

print(student.get("name2"),"\n") # no error ==> none
# never use [] to call a method , use () to execute it.

#===#
print("BEFORE")
# print(student["name2"]) # error
print(student.get("name2")) # while this will not give error, as it is a method. # return None
print("After\n")

#=========================================================================#
# update ==> adding new key-value pair or overiding the exisisting one.)
#=========================================================================#
student.update({"city" : "Delhi"}) # Added city key and value Delhi.
pair1 =(list(student.items()))
print(pair1[2],"\n") # To print only city.

new_dict1 = {"landmark" : "India Gate" , "Friend" : "Faiz"} # New dicationary
student.update(new_dict1) # updating current dictionary with new dictionary data, basically adding it in student dic
print(student,"\n")

# print(student.update({"name" : "Prasoon Agrawal"}),student,"\n")
# update() modifies the original dictionary in place and returns None, so print() displays None first.

new_dict2 = {"name" : "Bruce Wayne"} # overiding "name"
student.update(new_dict2)
print(student)
#=========================================================================#