#06
#=========================================================================#
#@1# # Store following word meanings in a python dictionary:
# table : "a piece of furniture", "list of facts & figures"
# cat : "a small animal"

dict1 = {
    "table" : ("a peice of furniture" , "list of facts & figures"), #stored in form of tuple
    "table" : ["a peice of furniture" , "list of facts & figures"], #stored in form of list
    "cat" : "a small animal"
}
print(dict1.items(),"\n")
#=========================================================================#
#@2# # you are given a list of subjects for students. Assume one classroom is required for 1 subjets . How many classrooms are needed by all students.

# "python" , "java" , "C++" , "python" , "javascript" , "java" , "python" , "java" , "C++" , "C"

set1 = {"python" , "java" , "C++" , "python" , "javascript" , "java" , "python" , "java" , "C++" , "C"}
lemon = len(set1)
print("This many class room will be required for each subjects:",lemon,"\n")

#=========================================================================#
#@3# # WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dicitionary & add one by one. Use subject name as key & marks as value.
print("Enter your marks.")
a = int(input("Physics:"))
b = int(input("Chemistry:"))
c = int(input("Maths:"))

subjects = {
    "Physics" : a,
    "Chemistry" : b,
    "Maths" : c,
}
print(subjects,"\n")

#=========================================================================#
#@4# #Figure out a way to store 9 and 9.0 as seperate values in the set. (You can take help of built-in data types)
 
 # Solution 1 :
value = {9,"9.0"}
print(value,"\n")
 
value2 = {9.0,"9"}
print(value2,"\n")

# Solution 2 :

value3 = {
    ("float" , 9.0),
    ("int" , 9)
}
print(value3,"\n")