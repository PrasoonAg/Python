#=========================================================================#
# 04 - Does Python Have Block Scope?
#=========================================================================#
# Unlike languages such as Java and C++, Python does not normally create
# a separate scope for if, for, or while blocks.

# A variable assigned inside a top-level if block can be accessed afterward.

game_level = 3
enemies_list = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies_list[0]

print(new_enemy)  # Skeleton

# However, a function DOES create its own local scope.
game_level = 10
def create_enemy():
    new_enemy = "" # this is done to make sure that this is varaible is always accessed irrespective of the conditonal code not being printed it gives an advantage to not have errors when if block not get printed
    if game_level < 5:
        new_enemy = enemies_list[0]  # Local to create_enemy()
    print(new_enemy)                 # Accessible inside this function

create_enemy()  # Skeleton

# print(new_enemy)  # Still refers to the top-level new_enemy above.
# The local new_enemy inside create_enemy() is not accessible here.
#=========================================================================#