#=========================================================================#
# Membership Operators
#=========================================================================#
# Membership operators are used to check whether a value exists
# in a collection.

# in = returns True if a value exists in a collection.
# not in = returns True if a value does not exist in a collection.

# Example:
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)       # True
print("mango" not in fruits)    # True


#=========================================================================#
# Membership Operators in Conditions
#=========================================================================#
# Membership operators can also be used as conditions in if statements.

# Example:
if "banana" in fruits:
    print("Banana is available.")

if "mango" not in fruits:
    print("Mango is not available.")

#=========================================================================#
# Difference Between "in" in for Loops and Conditions
#=========================================================================#

# In a for loop:
# "in" is used to iterate through each item in a collection.

# Example:
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Here, "in" means:
# Go through each item in fruits, one by one.


# In a condition:
# "in" is used as a membership operator to check whether
# a value exists in a collection.

# Example:
if "banana" in fruits:
    print("Banana is available.")

# Here, "in" means:
# Check whether "banana" exists in fruits.
#=========================================================================#