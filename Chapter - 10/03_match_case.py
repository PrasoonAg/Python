#=========================================================================#
# 02 - Match Case
#=========================================================================#
# match-case is Python's version of a switch statement found in other languages.
# It allows you to compare a value against multiple patterns and execute matching code.

day = 3

match day:
    case 1:
        print("Monday")
    
    case 2:
        print("Tuesday")
    
    case 3:
        print("Wednesday")
    
    case _: # Default Case
        print("Invalid Day")
        
# output - Wednesday

# Default case ( _ ) :- Match anything that wasn't matched above.

# Match case statement with constants
def check_number(x):
    match x:
        case 10:
            print("It's 10")
        case 20:
            print("It's 20")
        case _:
            print("It's neither 10 nor 20")

check_number(10)
check_number(20)
print("")

# Match case statement with OR operator
def num_check1(x):
    match x:
        case 10|20|30: # Matches 10, 20, or 30
            print(f"Matched: {x}")
        case _:
            print("no match case found")

num_check1(10) # Matched: 10
num_check1(20) # Matched: 20
num_check1(25)
print("")

# Match case statement with if condition
def num_check(x):
    match x:
        case True if x % 2 == 0:
            print("Matched 10 and its even!")
        case True if x % 2 != 0 :
            print("Matched 10 and its odd!")
        case _:
            print("no")
num_check(2)
print("")

# Match case statement on sequences
def process(data):
    match data:
        case [x,y]:
            # A list with two elements
            print(f"Two-element list: {x},{y}")
        case [x,y,z]:
            # A list with two elements
            print(f"Three-element list: {x},{y},{z}")
        case _:
            print("Unknown data format")

process([1,2])
process([1,2,3])
process([1,2,3,4])
#=========================================================================#