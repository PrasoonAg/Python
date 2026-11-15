#=========================================================================#
# 01 - List Basics
#=========================================================================#
# A list is an ordered, mutable collection used to store multiple values.
# Lists are created using square brackets [].

marks = [87.4, 79.4, 56.4, 89.4, 72.7]

print(marks)
print(type(marks))  # list datatype
print(len(marks))

#=========================================================================#
# Accessing List Elements
#=========================================================================#
# List elements can be accessed using their index.
# Indexing starts from 0.

print(marks[0])
print(marks[1])

# List indexing works similarly to string indexing.

#=========================================================================#
# Mutable
#=========================================================================#
# Lists are mutable, which means their elements can be changed after creation.

student = ["Karan", 95.4, 17, "Delhi"]

print(student[0])

student[0] = "Arjun"

print(student)

# List index can be changed, while a string's characters cannot be changed.
# print(student[5]) will give an error.

#=========================================================================#
# Dynamic List
#=========================================================================#
# A Python list is dynamic, which means its size can change during
# program execution.

numbers = [10, 20, 30]

numbers.append(40)    # List grows
numbers.pop()         # List shrinks

# Why is it called Dynamic?
# We do not need to decide the size of a list when creating it.
# Python automatically manages the memory when elements are added or removed.

#=========================================================================#
# Python List vs Array in Languages like C/C++
#=========================================================================#
# Python List:
# - Dynamic size → can grow or shrink automatically
# - Heterogeneous → can store different data types
# - Memory management is handled by Python

# C/C++ Array:
# - Built-in arrays generally have a fixed size
# - Elements normally have the same data type
# - Programmer has more control over memory

#=========================================================================#
# Important Terms
#=========================================================================#
# Reference        → A list stores references to objects
# Over-allocation  → Python keeps some extra memory available for list growth

# Note:
# Dynamic mainly refers to the ability of the list to change its size.
# Heterogeneous means that the list can contain different data types.
#=========================================================================#