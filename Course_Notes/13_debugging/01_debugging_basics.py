#=========================================================================#
# 01 -Debugging
#=========================================================================#
# Debugging is the process of identifying and fixing errors (bugs) in code.
# In 1947, a moth was found inside the Harvard Mark II computer and recorded
# by the operators. Grace Hopper is commonly associated with this incident.
# The term "bug" was already used for technical faults before this incident.
# Everyone encounters bugs while coding. :)

#=========================================================================#
# How to Identify Bugs?
#=========================================================================#
# 1) Describe the problem

def my_function():
    for i in range(1, 210):
        if i == 20:
            print("You got it")

my_function()

# The first step in solving a problem is being able to describe it.
# Understand what the code is doing and test whether your assumptions are correct.

# Write your answers as comments:
# 1. What is the for loop doing?
# 2. When is the function meant to print "You got it"?
# 3. What are your assumptions about the value of i?

# 1. The for loop iterates 209 times, with i taking values from 1 to 209.
# 2. When i becomes 20, the condition becomes True and the message is printed.
# 3. The range() function generates the values, which are assigned to i
# one at a time during each iteration.

# Note: range(start, stop) excludes the stop value.
#=========================================================================#