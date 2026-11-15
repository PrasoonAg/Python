#=========================================================================#
# 06 - Using a Debugger
#=========================================================================#
# Most IDEs (Integrated Development Environments) provide built-in
# debugging tools to pause code execution and inspect what is happening.
# They help us trace code line by line and identify where things go wrong.

import random
import maths

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
    b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])

# Debug Panel

# Breakpoint:
# Pauses program execution at a selected line so we can inspect variables
# and follow the execution flow. Usually set by clicking the gutter
# beside the line numbers.

# Step Over:
# Executes the current line and moves to the next one without entering
# any function called on that line.

# Step Into:
# Enters a function called on the current line, allowing us to examine
# how that function works internally.

# Step Out:
# Finishes executing the current function and returns to the calling code.

# Step Into My Code:
# Similar to Step Into, but focuses on our project code and skips
# external library code.

# Mute Breakpoints:
# Temporarily disables breakpoints so the debugger does not pause at them.

# Variables:
# Displays the current values of variables. Their values update as we
# step through the code.

# Debug Console:
# Allows us to view debugging output and evaluate expressions while
# the program is paused.

#=========================================================================#
# Last tips - Take a break, Ask a friend, Run Often, Ask StackOverflow 