#=========================================================================#
# 07 - Try With Else
#=========================================================================#
# Sometimes we want to run a piece of code when try was successful.

# The real purpose of else is:
# Keep the try block as small as possible.
# Only put the risky code inside try.
# Put the success code inside else.

try:
    a = int(input("Enter a number: "))

except Exception as e:
    print(e)

else: # This block runs only if the try block completes without any exception.
    print(f"I am inside else, {a} is a number")

# Why not put everything inside try?
# Because the try block should contain only the code that may raise the exception we want to handle.
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)

    result = 10 / 0     # ZeroDivisionError

except ValueError:      # except only catches ValueError
    print("Invalid Input")

# Using else separates risky code from success code,
# making it easier to see where exceptions originate.
try:    # Only the code that might cause ValueError
    num = int(input("Enter a number: "))

except ValueError:
    print("Invalid Input")

else:   # Code that should run after success
    print("You entered:", num)

    result = 10 / 0 # This will give ZeroDivsionError
#=========================================================================#