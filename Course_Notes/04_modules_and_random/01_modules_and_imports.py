#=========================================================================#
# Modules
#=========================================================================#
# What is a Module?
# A module is a Python file (.py) containing reusable code such as
# functions, variables, lists, classes, etc.
# It can be thought of as a code library.

# Why use Modules?
# - Reuse code instead of writing it again.
# - Organize code by separating related functionality into different files.
# - Use existing built-in or custom modules in programs.

# How to create a Module?
# Simply save Python code in a .py file.

# Example:
# mymodule.py

# def greeting(name):
#     print("Hello, " + name)
#
# word_list = ["apple", "banana", "mango"]

# The file mymodule.py is now a module.

#=========================================================================#
# Import
#=========================================================================#
# What is import?
# import is a Python keyword used to import a module so that its
# contents can be used in another Python file.

# Syntax:
# import module_name

# Example:
# import mymodule

# mymodule.greeting("Prasoon")
# print(mymodule.word_list)

# Access something from a module:
# module_name.item_name

# Example:
# mymodule.word_list

#=========================================================================#
# IMPORTING SPECIFIC ITEMS
#=========================================================================#
# We can import only a specific variable, list, function, etc.
# using from ... import.

# Syntax:
# from module_name import item_name

# Example:
# from mymodule import word_list
#
# print(word_list)

# Since word_list was imported directly, we don't need:
# mymodule.word_list

#=========================================================================#
# MODULE ALIAS
#=========================================================================#
# We can give an imported module a shorter name using as.

# Syntax:
# import module_name as alias

# Example:
# import mymodule as mm
#
# mm.greeting("Prasoon")

#=========================================================================#
# QUICK REMINDER
#=========================================================================#
# Module → A .py file containing reusable code.
# import  → Used to bring a module into another Python file.
# from    → Used to import specific items from a module.
# as      → Used to give an imported module/item an alias.
#=========================================================================#