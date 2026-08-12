#=========================================================================#
# 02 - Function Types
#=========================================================================#
# Built-in Functions:

# A built-in function is a function already provided by Python.
# It is defined inside Python itself, so we do NOT need to write 'def' to create it.
# We can directly call it, for example: print(), len(), type(), input(),etc.

#=========================================================================#
# print()
print("apnacollege")   # print() is a built-in function.
                       # "apnacollege" is the argument passed to it.

print("Prasoon", "Agrawal")   # sep=" " → default separator between multiple values
print("king")                 # end="\n" → default ending (moves to next line)

print("apna college", end=" ")  # changing 'end' → adds a space instead of a newline
print("youtube")                # printed on the same line because we changed 'end'.

print("Apples cost ", end="$") # changing 'end' → adds $ instead of a newline
print("2")                     # printed on the same line because we changed 'end'.

#=========================================================================#
len
# This Refers to the built-in function object.
# Hovering over it shows its signature and documentation.

len()
# Calls the function.
# Used to return the number of items in an object.

range()
# Built-in function used to generate a sequence of numbers.
# Hovering over it shows the function signature:
# range(stop)
# range(start, stop)
# range(start, stop, step)
#=========================================================================#