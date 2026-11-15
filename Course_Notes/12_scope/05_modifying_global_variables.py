#=========================================================================#
# 05 - How to Modify Variables with Global Scope
#=========================================================================#
# Using the same name for local and global variables is allowed, but can
# sometimes make code confusing.

# The global keyword allows a function to reassign a global variable.

enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")

#=========================================================================#
# Alternative: Use return Instead of Modifying a Global Variable
#=========================================================================#
# A function can return an updated value without modifying the global variable.
# We can store the returned value in a new variable.

enemies = 1

def increase_enemies(no_of_enemy):
    return no_of_enemy + 1  # Returns 2; does not modify global enemies

total_enemies = increase_enemies(enemies)

print(enemies)        # 1 -> Original variable remains unchanged
print(total_enemies)  # 2 -> New variable stores the returned value


# We can also reassign the returned value to the original variable.

enemies = increase_enemies(enemies)

print(enemies)  # 2 -> Global variable is reassigned OUTSIDE the function

# Key Difference:
# global enemies -> Allows the function to modify the global variable directly.
# return         -> Sends a value back; the caller decides where to store it.
#=========================================================================#