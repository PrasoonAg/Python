#=========================================================================#
# 06 - Python Constants and Global Scope
#=========================================================================#
# Global constants are values intended to remain unchanged throughout a program.
# Python does not enforce constants, so uppercase names (ALL_CAPS) serve as a reminder
# not to modify them.

PI = 3.14159
GOOGLE_URL = "https://www.google.com/"


# Using a Global Constant Inside a Function

def calc(radius):
    return PI * radius ** 2

print(calc(5))  # Uses PI without needing the global keyword.
#=========================================================================#