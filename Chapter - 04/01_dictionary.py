#=========================================================================#
# 01 - Dictionary
#=========================================================================#
# Dictionary stores data in key : value pairs.
# Keys must be immutable and unique.
info = {
    "name": "apna college",
    "learning": "coding",
    "age": 99,                  # integer
    "is_adult": True,           # boolean
    "marks": 94.4,              # float
    "subjects": ["python", "java", "C"],  # list
    "topics": ("dict", "set"),           # tuple
    12.99: 94.4
}

# Accessing a value using its key
print(info["name"])

# Updating an existing value
info["name"] = "Prasoon"

# Adding a new key : value pair
info["surname"] = "Agrawal"

# print(info["surname"]) → Error if key doesn't exist.

#=========================================================================#
# Empty Dictionary
#=========================================================================#
null_dict = {}

# Adding data to an empty dictionary
null_dict["name"] = "apnacollege"
print(null_dict)

#=========================================================================#
# Dictionary Operations
#=========================================================================#
programming_dictionary = {
    "Bug": "An error in a program.",
    "Function": "A piece of code that can be called repeatedly."
}

# Adding a new item
programming_dictionary["Loop"] = "Doing something repeatedly."

# Updating an existing item
programming_dictionary["Bug"] = "A moth in your computer."

# Wiping a dictionary
# programming_dictionary = {}

# Looping through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
#=========================================================================#