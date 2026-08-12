#=========================================================================#
# 10 - List Comprehensions
#=========================================================================#
# List Comprehension is a concise way to create a new list from an iterable.
# It combines looping, optional filtering, and expression evaluation into a single line.

myList = [1,2,3,4,5,6,7,8]

squaredList1 = []
for item in myList:
    squaredList1.append(item*item)
print(squaredList1)

squaredList2 = [item*item for item in myList]
print(squaredList2)
# Syntax:
# [expression for item in iterable]
#=========================================================================#
# It can also filter
evenList = [item for item in myList if item % 2 == 0]
print(evenList)
# Syntax:
# [expression for item in iterable if condition]
# Filtering is one of the main reasons list comprehensions are used.
#=========================================================================#