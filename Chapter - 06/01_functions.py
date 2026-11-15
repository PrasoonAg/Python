#=========================================================================#
# 01 - Functions
#=========================================================================#
# A function is a reusable block of code that performs a specific task.

# Why use functions?
# Functions help avoid repeating the same code and make code reusable.

#=========================================================================#
# Defining and Calling a Function
#=========================================================================#
# Define a function using the 'def' keyword.
# The code inside the function runs only when the function is called.

def print_hello():
    print("Hello")

print_hello()

#=========================================================================#
# Function with Input
#=========================================================================#
# A function can receive input through parameters.
# Parameters are placeholders for the values that the function will receive.

def greet(name):
    print(f"Hello {name}")

greet("Prasoon")

#=========================================================================#
# Function with Input and Print
#=========================================================================#
# A function can take input and directly print the result.
# print() displays the result but does not return it.

def calc_sum(a, b):
    print(a + b)

calc_sum(5, 3)

#=========================================================================#
# Function with Input and Return
#=========================================================================#
# return sends a value back to the place where the function was called.
# The returned value can be stored, printed, or used in another operation.

def calc_sum(a, b):
    return a + b

result = calc_sum(5, 3)
print(result)

#=========================================================================#
# print() vs return
#=========================================================================#
# print() → displays a value
# return  → sends a value back to the caller

# return is useful when the result needs to be used outside the function.

#=========================================================================#
# Function without a Return Value
#=========================================================================#
# If a function does not use return, it returns None automatically.

def print_hello():
    print("Hello")

output = print_hello()
print(output)       # None

#=========================================================================#
# Function with Multiple Parameters
#=========================================================================#
# A function can have multiple parameters.
# Each parameter receives a corresponding argument.

def average(a, b, c):
    total = a + b + c
    return total / 3

print(average(4, 5, 3))

#=========================================================================#
# Arguments
#=========================================================================#
# Arguments are the actual values passed to a function when it is called.

# Positional Arguments:
# Arguments are assigned to parameters according to their position/order.

def example(a, b, c):
    print(a, b, c)

example(10, 20, 30)

# Keyword Arguments:
# Arguments are assigned to parameters using their parameter names.

example(c=30, a=10, b=20)

#=========================================================================#
# Practical Example
#=========================================================================#
# Functions can take input, process it, and return the required result.

def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name("PraSoON", "AGrAwaL"))

#=========================================================================#
# Using Functions Together
#=========================================================================#
# The returned value of one function can be directly used as an
# argument for another function.

def double_text(text):
    return text + text

def format_text(text):
    return text.title()

output = format_text(double_text("hello"))
print(output)

# double_text("hello") → "hellohello"
# format_text("hellohello") → "Hellohello"

# The inner function runs first, and its returned value is passed
# to the outer function.

#=========================================================================#
# Multiple things we can do
#=========================================================================#
# Can have multiple returns
# also can have return keyword without anything else afterwards
# can apply conditional statements
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return # None
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"
    print("This got printed") # function is exectuted

print(format_name(input("What is your first name? "), input("What is your last name? ")))

#=========================================================================#
# Docstring
#=========================================================================#
# A docstring is a string used to document code.
# It is written inside triple quotes (""" """).

# For functions, the docstring is placed immediately after the function
# definition. It describes what the function does and can be viewed
# when hovering over the function or using help().

def my_function(num):
    """Multiply a number by itself."""
    return num * num

print(my_function(5))

# Docstrings are mainly used to explain the purpose of a function,
# class, or module.
#=========================================================================#