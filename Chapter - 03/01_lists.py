#=========================================================================#
# 01 List
#=========================================================================#
marks =[87.4,79.4,56.4,89.4,72.7]
print(marks)
print(type(marks)) # list datatypes
print(len(marks))
print("")
# Properties are similar to the string
print(marks[0])
print(marks[1])
print("")
# Can access a particular index

#=========================================================================#
student =["Karan", 95.4, 17, "Delhi"]
print(student[0])
student [0] = "Arjun"
print(student)
print("")
# List inex can be changed while String cant
# print(student[5]) will give an error

#=========================================================================#
# Accessing list inside a list
L1 = ["Liam", "Sophia", "jasper", "Isla"]
L2 = ["Arlo", "Freya", "Milo", "Elena"]
my_list = [L1, L2]
print(my_list[-1][3]) # Elena
# [-1] -> L2 and [3] -> Elena

#=========================================================================#