#=========================================================================#
# 10 - List Comprehensions
#=========================================================================#
# List Comprehension is a concise way to create a new list from an iterable.
# It combines looping, optional filtering, and expression evaluation into a single line.
# Syntax:
# [expression for item in iterable]

# Expression
# The expression is the part that determines what value will be placed into the new list.
# It can be:
# Variable itself         - [x for x in numbers]
# Arithmetic expression   - [x + 10 for x in numbers]
# Function/method call    - [x.upper() for x in words]
# Conditional expression  - ["even" if x % 2 == 0 else "odd" for x in numbers]
# Multiple variables      - [x + y for x in [1, 2] for y in [10, 20]]

myList = [1,2,3,4,5,6,7,8]

# Normally
squaredList1 = []
for item in myList:
    squaredList1.append(item*item)
print(squaredList1)

# by List Comprehensions
squaredList2 = [item*item for item in myList]
print(squaredList2)

#=========================================================================#
# It can also filter
evenList = [item for item in myList if item % 2 == 0]
print(evenList)
# Syntax:
# [expression for item in iterable if condition]
# Filtering is one of the main reasons list comprehensions are used.
#=========================================================================#