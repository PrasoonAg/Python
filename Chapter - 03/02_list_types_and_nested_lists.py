#=========================================================================#
# 02 - List Types and Nested Lists
#=========================================================================#
# Python has only one built-in list datatype.
# However, lists can be described based on the type of data they contain
# or how they are structured.

#=========================================================================#
# Homogeneous List
#=========================================================================#
# A list whose elements are of the same data type.

numbers = [10, 20, 30, 40]
fruits = ["Apple", "Mango", "Banana", "Orange"]

#=========================================================================#
# Heterogeneous List
#=========================================================================#
# A list that contains elements of different data types.

data = [10, "Python", 3.14, True]

#=========================================================================#
# Empty List
#=========================================================================#
# A list that contains no elements.

empty_list = []
#=========================================================================#
# Nested List
#=========================================================================#
# A nested list is a list that contains one or more other lists as its elements.

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])  # D

# [2] -> ["C", "D"]
# [1] -> "D"

#=========================================================================#
# Accessing a List inside Another List
#=========================================================================#
L1 = ["Liam", "Sophia", "Jasper", "Isla"]
L2 = ["Arlo", "Freya", "Milo", "Elena"]

my_list = [L1, L2]
print(my_list[-1][3])  # Elena

# [-1] -> L2
# [3]  -> Elena

#=========================================================================#
# Example of a Nested List
#=========================================================================#
fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes", "Watermelon"]
vegetables = ["Potato", "Tomato", "Carrot", "Onion", "Cabbage", "Spinach"]

nested_list = [fruits, vegetables]
#=========================================================================#