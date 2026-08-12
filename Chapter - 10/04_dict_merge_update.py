#=========================================================================#
# 04 - Dictionary Merge & Update Operators
#=========================================================================#
# New operators | and |= allow for merging and updating dictionaries.
# |  -> Merges two dictionaries and returns a new dictionary.
# |= -> Updates the existing dictionary using another dictionary.

# Merge Dictionaries |
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2 # If the same key exists in both dictionaries, 
                       # the value from the RIGHT dictionary wins.
print(merged) # {'a': 1, 'b': 3, 'c': 4}

# Update Dictionaries |=
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 20, "c": 3}

dict1 |= dict2
print(dict1) # {'a': 1, 'b': 20, 'c': 3}

#=========================================================================#
# | has different meanings depending on the data type.

# int | int         -> Bitwise OR
# dict | dict       -> Dictionary Merge (Python 3.9+)

# Python decides which operation to perform based on the object's type.
# This concept is called Operator Overloading.
# Same operator, different behavior depending on the object's type.
#=========================================================================#