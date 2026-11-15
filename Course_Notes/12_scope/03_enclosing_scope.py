#=========================================================================#
# 03 - Enclosing Scope (Nested Functions)
#=========================================================================#
# A nested function can access a variable from its enclosing function.

def game():
    health_bar = 10

    def potion():
        strength = 3
        print(health_bar)  # Accesses the enclosing function's variable.
        print(strength)    # Accesses its own local variable.

    potion()

game()

# potion()  # NameError: potion is not defined at the top level.
# potion() is defined inside game(), so its name is local to game().
#=========================================================================#