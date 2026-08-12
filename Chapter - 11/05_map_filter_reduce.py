#=========================================================================#
# 05 - Map, Filter & Reduce
#=========================================================================#
# Map
# map() applies a function to every item of an iterable and returns a map object.
# Syntax:
# map(function, iterable)

# Without map()
numbers = [1,2,3,4,5]

squared = []
for n in numbers:
    squared.append(n*n)

print(squared)

# With map()
numbers = [1,2,3,4,5]
square = lambda x: x*x
print(list(map(square,numbers)))
# map() does not create a list directly.
# Use list() to view all results.

#=========================================================================#
# Filter
# filter() keeps only those elements for which a function returns True.
# filter(function, iterable)

# filter() returns a filter object.
# Use list() to view all results.

# Without filter()
numbers = [1,2,3,4,5,6]
even_numbers = []
for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)

print(even_numbers) # [2,4,6]

# With filter()
numbers = [1,2,3,4,5,6]

def even(n):
    return n % 2 == 0

print(list(filter(even, numbers))) # Only elements for which the function returns True are kept.

# or

numbers = [1,2,3,4,5,6]
onlyEven = filter(lambda x: x % 2 == 0, numbers)
print(list(onlyEven))

#=========================================================================#
# Reduce
# reduce() repeatedly applies a function to pairs of elements until a single value remains.
# reduce() returns a single final value.
from functools import reduce
# val = reduce(function, iterable)

numbers = [1,2,3,4,5]


# Addition
def add(a,b):
    return a + b
print(reduce(add,numbers))
# or
print(reduce(lambda a,b : a+b,numbers))
# reduce() works like:
# (((1+2)+3)+4)+5)


# Multiplication
def multiply(a,b):
    return a * b
print(reduce(multiply,numbers))
# or
print(reduce(lambda x,y : x*y,numbers))
# reduce() works like:
# ((((1*2)*3)*4)*5)
#=========================================================================#
#   map()  -> Apply a function to every element.
# filter() -> Keep only elements that satisfy a condition.
# reduce() -> Combine all elements into a single value.
#=========================================================================#