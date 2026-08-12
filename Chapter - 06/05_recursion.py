#=========================================================================#
# 05 - Recursion
#=========================================================================#
# Recursion is a technique where a function solves a problem by calling itself on a smaller version of the same problem.

# Loops and recursion can often solve the same problems.
# Anything solvable using recursion can usually be solved using loops, and vice versa.

# Recursion Structure for beginners:

# def function_name(problem):

#     # Base case
#     if stopping_condition:
#         return value

#     # Recursive case
#     return function_name(smaller_problem)

# Every recursive function must have:
# 1. Base case (where recursion stops)
# 2. Recursive case (where the function calls itself)
#=========================================================================#
# Printing numbers in descending order using recursion:
def show(n):
    if(n==0): # Base case: the stopping condition that prevents infinite recursion.
        return
    print(n)
    show(n-1)

show(5)
# Calls:
# show(5) -> show(4) -> show(3) -> show(2) -> show(1) -> show(0)

#=========================================================================#
# Factorial of n numbers using recursion:
def factorial(n):
    if (n==1 or n==0): #Base case: stops when n==1 or n==0.
        return 1
    
    return n * factorial(n-1)  # Recursion relation: n * factorial(n-1)
                               # Flow:
                               # Push ↓ : recursive calls go deeper
                               # Pop  ↑ : values return and get multiplied
                             
print(factorial(3))

# Recursive relation: a rule that defines a problem in terms of a smaller version of itself.
# Example (factorial):
# n! = n × (n−1)!

#=========================================================================#
# Sum of n numbers using recursion:
def add(n):
    if n == 0: # Base case: stops when n==0.
        return 0
    
    return add(n-1) + n # Recursion relation: add(n-1) + n

print(add(4))

# add(4)
# = add(3) + 4
# = add(2) + 3 + 4
# = add(1) + 2 + 3 + 4
# = add(0) + 1 + 2 + 3 + 4
# = 0 + 1 + 2 + 3 + 4
# = 10
#=========================================================================#
# Whenever you see recursion, ask:
# Where does it stop? → Base case
# How does it shrink? → Recursive relation
# What happens on return? → Final answer

#=========================================================================#
# Recursion Flow (Call Stack)
# Every recursive call creates a new layer in the Call Stack.
# The Call Stack stores unfinished function calls until they complete.

# Push ↓ Phase:
# Recursive calls keep going deeper and are pushed onto the stack.
# No final calculation happens yet; functions are waiting for smaller problems to finish.

# Base Case:
# The stopping condition is reached, so recursion stops going deeper.

# Pop ↑ Phase:
# Functions return one by one and are removed (popped) from the stack.
# During this return phase, pending calculations are completed and the final answer is built.

# Example: factorial(4)

# Push ↓ : factorial(4) → factorial(3) → factorial(2) → factorial(1)

# Base   : factorial(1) = 1

# Pop  ↑ : factorial(2)=2 → factorial(3)=6 → factorial(4)=24

# Recursion goes down creating layers, reaches the base case,then comes back up solving the problem.
#=========================================================================#