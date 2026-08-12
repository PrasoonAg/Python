#=========================================================================#
# 02 - Type Hints
#=========================================================================#
# Specify the expected data type of variables, parameters, and return values.
# Helps with readability, autocomplete, and static type checking.

# variable: type = value
# def func(param: type) -> return_type:

# Common Types:
# int, float, str, bool, list, tuple, dict, set

#=========================================================================#
# Variables
name: str = "Prasoon"  # variable hint
age: int = 19
height: float = 5.9
is_student: bool = True

# Functions
def greet(name: str) -> None:
            # name: str -> parameter hint
            # -> str    -> return type hint
    print(f"Hello {name}")
greet("Prasoon")

def add(a: int, b: int) -> int:
    return a + b
print(add(4,5))

# Important:
# Type hints are not enforced at runtime.
age: int = "twenty"  # Valid, but type checkers will warn in Vscode or other editor.

#=========================================================================#
# Modern Python (3.9+):

# List of integers
numbers: list[int] = [1,2,3,4,5]

# Tuple of a string and an integer
person : tuple[str,int] = ("Alice",30)

# Dictionary with string keys and integer values
scores: dict[str,int] = {"Alice": 90, "Bob": 85}

# Variable can be int or str
identifier: int | str = "ID123"
identifier = 12345
#=========================================================================#