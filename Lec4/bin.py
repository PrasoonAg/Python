student = { #Dictionary
    "name" : "Raghav Singh",
    "subjects" : { #Nested Dictionary
        "chem" : 95,
        "phy" : 92,
        "maths" : 89,
    }
}

print(student["name"]) # Raghav Singh
print(type(student["name"]),"\n") #<class 'str'>
#print(student["name2"]) #error as key is missing.

print(student.get("name")) # Raghav Singh
print (type(student["name"]),"\n") #<class 'str'>
