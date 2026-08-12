#=========================================================================#
# 05 - Exception Handling
#=========================================================================#
# try -> Code that may cause expection
# except -> Code that runs if an exception occurs.
# except → "I know how to handle that."

# There are many built-in exceptions which are raised in python when something goes wrong.
# Exception in python can be handled using a try statement. The code that handles the exception is written in the except clause.

try:
    int(input("Enter a number:"))

except Exception as e:
    print(e) # output -> invalid literal for int() with base 10: 'dad'

print("Program continues...") # The exception is handled, the code flow continues without program interruption.

#=========================================================================#
# we can also specify the exception to catch like below:
try:
    int(input("Enter a number:"))
except ValueError as v:
    print("Heyy")
    print(v)
except ZeroDivisionError as z:
    print(z)
except TypeError as t:
    print(t)
except:
    print()

#=========================================================================#