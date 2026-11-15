#=========================================================================#
# 01 - Python Scope
#=========================================================================#
# Scope determines where a variable or name can be accessed.
# A name may refer to a variable, function, or another object.

# Namespace  -> A mapping of names to objects.
# Scope      -> The region where a name can be accessed.

# Python has local, enclosing, global, and built-in name lookup levels.

#=========================================================================#
# Local Scope
#=========================================================================#
# Variables (or functions) declared inside functions have local scope (also called
# function scope). They are only seen by other code within the same block of code.


def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()  # 2

# print(potion_strength)  # NameError: not defined in this scope
#=========================================================================#