#=========================================================================#
# 02 - Iterator Protocol
#=========================================================================#
# Special/Magic Method = A method with double underscores (__) on both sides
# that Python calls automatically for certain operations.
# (Also called "dunder" methods.)

# Examples:
# __iter__(), __next__(), __add__()

# Iterator Protocol = The set of rules that defines how iteration works
# between an iterable, an iterator, and Python's iteration tools.
#
#   iter(obj)  ->  obj.__iter__()   must return an iterator
#   next(it)   ->  it.__next__()    returns the next item, or raises
#                                   StopIteration when there are none left
#
# Rule from the Python docs: an iterator's __iter__() must return the
# iterator itself. And once __next__() has raised StopIteration, it must
# keep raising it on every later call (an iterator never "restarts").

# The examples below demonstrate how these rules work in practice.

#=========================================================================#
# Checking if an object is Iterable
#=========================================================================#
a = 2

# Using a loop:
# for i in a:
#     print(i)
# TypeError: 'int' object is not iterable

# Inspecting with dir():
print("__iter__" in dir(a))   # False -> int has no __iter__(), not iterable
# (dir(a) lists every attribute/method of a; the original printed the whole
#  list, which is long. Checking one name is easier to read.)

# Note:
# dir() is useful for inspecting an object's available attributes/methods.
# It gives a basic idea of whether an object supports iteration, but it is
# not the official test (see "Best ways to check" below).

# Using iter():
# If an object is iterable, iter() returns an iterator for it.
# If not, iter() raises TypeError.

# iter(a)
# TypeError: 'int' object is not iterable

#=========================================================================#
# Checking if an object is an Iterator
#=========================================================================#
L = [1, 2, 3]

# Inspecting with dir():
print("__iter__" in dir(L), "__next__" in dir(L))
# True False -> L has __iter__() but not __next__(): iterable, NOT an iterator.

# iter() returns an iterator object from an iterable.
iter_L = iter(L)

print("__iter__" in dir(iter_L), "__next__" in dir(iter_L))
# True True -> iter_L has both __iter__() and __next__(): it is an iterator.

print(type(L))        # <class 'list'>
print(type(iter_L))   # <class 'list_iterator'>

# Important:
# iter(L) does not convert the list itself into an iterator.
# It returns a separate iterator object that walks over the list.

#=========================================================================#
# Best ways to check (recommended)
#=========================================================================#
from collections.abc import Iterable, Iterator

print(isinstance(L, Iterable), isinstance(L, Iterator))             # True False
print(isinstance(iter_L, Iterable), isinstance(iter_L, Iterator))   # True True
print(isinstance(2, Iterable))                                      # False

# Caveat: isinstance(obj, Iterable) only checks for __iter__(). The most
# reliable test is simply to try it:
def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

print(is_iterable(L), is_iterable(2))   # True False

#=========================================================================#
# Iterable vs Iterator
#=========================================================================#
# Iterable -> An object that can return an iterator using iter().
#             (has __iter__(), or the legacy __getitem__())
# Iterator -> An object that provides both __iter__() and __next__().

# Every iterator is also an iterable.
# Not every iterable is an iterator.

#=========================================================================#
# An iterator is used up after one pass (it is "exhausted")
#=========================================================================#
it = iter([1, 2, 3])
print(list(it))   # [1, 2, 3]
print(list(it))   # []  -> exhausted, it does NOT restart

# A list (iterable) gives a fresh iterator every time, so it can be reused:
nums = [1, 2, 3]
print(list(nums), list(nums))   # [1, 2, 3] [1, 2, 3]
#=========================================================================#
