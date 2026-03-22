#05
#=========================================================================#
# Recursion
#=========================================================================#
# When a functions call itself repadelty.

# Loops and Recursion can do same thing.(have same concept)
# Things which can be done using loops, can also be done with Recursion.

#simple code
#Recursive Function

def show(n):
    if(n==0): # Base case = the exit point that prevents infinite looping.
        return
    print(n)
    show(n-1)

# show(5) #5 = n, 4 = n-1, 3 = n-2, 2 = n-3, 1 = n-4

#=========================================================================#
# Call stack = pile of funtions
# HAVE TO UNDERSTAND THE LAYERING ONCE AGAIN
#=========================================================================#
# return n!
def fact(n):
#Base case: stops when n==1 or n==0.
    if (n==1 or n==0):
        return 1
# recursion relation: n * factorial(n-1)
# Flow: goes down then comes back multiplying (# Flow: push ↓ pop ↑)
    return fact(n-1)* n

print(fact(3))
#=========================================================================#
# Recursive relation: a rule that defines a problem in terms of a smaller version of itself.
# Example (factorial):
# n! = (n−1)! × n
#=========================================================================#
# Whenever you see recursion, ask:
# Where does it stop? → Base case
# How does it shrink? → Recursive relation
# What happens on return? → Final answer