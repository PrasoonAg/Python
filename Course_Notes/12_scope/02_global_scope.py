#=========================================================================#
# 02 - Global Scope
#=========================================================================#
# Variables or functions declared at the top level (unindented) of a code file
# have global scope. It is accessible anywhere in the code file.

player_health = 10

def show_health():
    print(player_health)  # A function can read a global variable.

show_health()             # 10
print(player_health)      # 10

#=========================================================================#
# Local and Global Variables with the Same Name
#=========================================================================#
# A local variable can have the same name as a global variable.
# They are separate names in different scopes.

enemies = 1

def increase_enemies():
    enemies = 2  # Local variable; does not change the global variable.
    print(f"Enemies inside function: {enemies}")

increase_enemies()  # Enemies inside function: 2
print(f"Enemies outside function: {enemies}")  # Enemies outside function: 1
#=========================================================================#