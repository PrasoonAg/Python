#=========================================================================#
# 04 - Fix the Errors
#=========================================================================#
# Fix errors (red underlines) in the editor before running your code.
# Warnings (yellow underlines) indicate potential issues. They may not
# stop execution, but should still be investigated.

#=========================================================================#
# Catching Exceptions
#=========================================================================#
# Use try/except to handle exceptions that might occur during execution.
# Place potentially risky code inside try and handle specific errors in except.

try:
    age = int(input("How old are you? "))
except ValueError:
    print("Invalid input. Please enter a numerical value.")
    age = int(input("How old are you? "))

if age > 18:
    print(f"You can drive at age {age}.")

# Note: Some bugs are not highlighted by the editor.
# Missing the 'f' in an f-string is an example:
# The code runs, but prints {age} literally instead of its value.
#=========================================================================#