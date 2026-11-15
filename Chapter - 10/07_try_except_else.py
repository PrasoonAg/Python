#=========================================================================#
# 07 - try-except-else
#=========================================================================#
# The else block runs only when the try block completes without an exception.

# else is optional:
# We can use try-except without else, or use try-except-else
# when we want to separate success code from risky code.

#=========================================================================#
# try-except
#=========================================================================#
try:
    a = int(input("Enter a number: "))

except ValueError:
    print("Invalid input")

# If int() raises ValueError, except runs.
# If no exception occurs, execution continues after try-except.

# else is not needed when there is no separate code that should
# run only after try succeeds.

#=========================================================================#
# try-except-else
#=========================================================================#
try:
    a = int(input("Enter a number: "))

except ValueError as e:
    # e stores the ValueError exception object.
    print(e)

else:
    # Runs only if try completes without an exception.
    print(f"I am inside else, {a} is a number")

#=========================================================================#
# Why separate the code using else?
#=========================================================================#
# The try block should contain only the code that may raise
# the exception we want to handle.

# Code that should run only after try succeeds can be placed inside else.

# This separates risky code from success code and makes it easier
# to identify where exceptions originate.


# Without else:
# Both the risky code and the code that runs after success
# are placed inside the try block.
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)

    result = 10 / 0     # ZeroDivisionError

except ValueError:
    # This except block only handles ValueError.
    print("Invalid input")

# Here, the try block contains more code than the code that
# may raise ValueError.

# If another exception occurs inside try, it can be handled
# by another matching except block if one is provided.


# With else:
# Only the code that may raise ValueError is placed inside try.
# Code that should run after successful execution is placed inside else.
try:
    num = int(input("Enter a number: "))

except ValueError:
    print("Invalid input")

else:
    print("You entered:", num)

    result = 10 / 0     # ZeroDivisionError

#=========================================================================#
# The responsibilities are now clearly separated:
# try    -> Code that may raise ValueError.
# except -> Handles ValueError if it occurs in try.
# else   -> Code that runs only when try succeeds.

# The ZeroDivisionError occurs inside else, so it is not handled
# by the ValueError except block.
#=========================================================================#