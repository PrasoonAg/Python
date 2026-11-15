#=========================================================================#
# 01 - Iteration, Iterator and Iterable
#=========================================================================#
# Run this file top to bottom: python 01_iteration_iterable_iterator.py

import sys

#=========================================================================#
# Iteration
#=========================================================================#
# Iteration is a general term for taking each item of something, one after
# another. Any time you use a loop, explicit or implicit, to go over a group
# of items, that is iteration.

# Example -
num = [1, 2, 3]

for i in num:
    print(i)

#=========================================================================#
# Types Of Iteration
#=========================================================================#
# Definite iteration = repeating a process a known number of times.
# Example: for loop

for i in range(3):
    print("Hello")

# We know beforehand that it will repeat 3 times.

#===#
# Indefinite iteration = repeating a process an unknown number of times,
# until a condition becomes false.
# Example: while loop

# password = ""
# while password != "1234":
#     password = input("Enter a password: ")

# We do not know beforehand how many attempts the user will need. The loop
# keeps repeating until the condition becomes false.
# (Commented out so this file runs without waiting for keyboard input.)

#=========================================================================#
# What is an Iterator
#=========================================================================#
# An iterator is an object that lets the programmer traverse a sequence or
# stream of data one item at a time.
#
# The iterator fetches one item at a time and hands it to the loop. After
# that item is processed, it moves on to the next one.
#
# Many iterators produce their values lazily (on demand), so the whole data
# does not have to sit in memory at once. This reduces memory usage when
# working with large amounts of data.
#
# Note: laziness is a property of how the iterator produces values, not of
# iterators in general. An iterator over a list still points at a list that
# is already fully in memory. A range, on the other hand, never builds the
# numbers up front.

# Example - list vs range
L = [x for x in range(1, 10000)]   # List comprehension: builds all 9999 ints
# L occupies space in memory.

for i in L:
    pass   # (the original printed i*2 here, 9999 lines of output)

# To check the memory occupied by L:
print(sys.getsizeof(L) / 1024)   # ~83 KB (exact value depends on Python version)

x = range(1, 10000)   # x is an ITERABLE (a lazy sequence), NOT an iterator.
for i in x:
    pass
print(sys.getsizeof(x) / 1024)   # 0.046875 KB -> it only stores start/stop/step

# CORRECTION: the earlier note said "x is an iterator". That is wrong.
#   range(...)       -> iterable (can be looped many times, supports len, indexing)
#   iter(range(...)) -> range_iterator (the actual iterator, one pass only)
# next(range(1, 5)) raises: TypeError: 'range' object is not an iterator

# sys.getsizeof() reports only the object's own size (the list's array of
# pointers), not the int objects it points to, so the real gap is even bigger.

#=========================================================================#
# What is an Iterable
#=========================================================================#
# An iterable is an object that one can iterate over.
# It produces an iterator when it is passed to the iter() function.

L = [1, 2, 3]

print(type(L))
# L is a list, and a list is an iterable.

print(type(iter(L)))
# iter(L) --> list_iterator (an iterator)

# Important:
# Every iterator is also an iterable.        (iter(iterator) returns itself)
# Not every iterable is an iterator.         (a list is not)

# Trick:
# Every iterable has __iter__()               -> returns an iterator.
# Every iterator has __iter__() AND __next__().
#   (Legacy exception: an object with only __getitem__() that accepts
#    0, 1, 2, ... is also iterable. See 05_beyond_the_basics.py.)

#=========================================================================#
# Quick Summary
#=========================================================================#
# +-----------+------------------------+-----------------------------------+
# |           | iterable               | iterator                          |
# +-----------+------------------------+-----------------------------------+
# | methods   | __iter__()             | __iter__() and __next__()         |
# | iter(obj) | returns a NEW iterator | returns ITSELF                    |
# | reusable  | yes (new iterator each | no (one pass, then exhausted)     |
# |           | time you loop)         |                                   |
# | examples  | list, tuple, str, dict,| list_iterator, range_iterator,    |
# |           | set, range, file       | generator, file object            |
# +-----------+------------------------+-----------------------------------+
#=========================================================================#