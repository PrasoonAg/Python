#=========================================================================#
# 03 - How the for loop works + Custom Iterators
#=========================================================================#
# Run this file top to bottom: python 03_for_loop_and_custom_iterators.py

#=========================================================================#
# Understanding How the for Loop Works
#=========================================================================#
num = [1, 2, 3]

for i in num:
    print(i)

print("")

# How does the for loop work internally?
num = [1, 2, 3]   # num is an iterable, but not an iterator.

# Step 1 -> Get an iterator from the iterable.
iter_num = iter(num)

# Step 2 -> Get the next item from the iterator, again and again.
print(next(iter_num))   # 1
print(next(iter_num))   # 2
print(next(iter_num))   # 3

# The for loop repeatedly calls next() until there are no more values.
# When there are no more values, next() raises StopIteration, and the for
# loop catches it silently and ends.
# print(next(iter_num))   # StopIteration

print("")

#=========================================================================#
# iter() vs __iter__()
#=========================================================================#
numbers = [10, 20, 30]

a = iter(numbers)
b = numbers.__iter__()
# Both do the same job: they ask numbers (the iterable) for an iterator.

# numbers
#    │
#    └──────→ list object (A)
#
# a ─────────→ list_iterator object (B)
#
# b ─────────→ list_iterator object (C)

# For a list, each call creates a separate iterator object.
print(a is b)   # False
# a and b are two separate iterator objects, each with its own position.

# Important
# iter(obj)  →  obj.__iter__()
# next(obj)  →  obj.__next__()
# (Use iter() and next() in your code; the dunder versions are what YOUR
#  classes define so that the built-ins can call them.)

#=========================================================================#
# Making Our Own for Loop
#=========================================================================#
def my_own_for_loop(iterable):

    # Get an iterator from the iterable.
    iterator = iter(iterable)

    # Keep looping until break is executed.
    while True:
        try:
            # Get the next value from the iterator.
            print(next(iterator))

        except StopIteration:
            # Stop the loop when there are no more values.
            break

a = [1, 2, 3]
b = range(1, 4)
c = (1, 2, 3)
d = {1, 2, 3}
e = {0: 1, 1: 1}   # a dict iterates over its KEYS: 0, 1

for obj in (a, b, c, d, e):
    my_own_for_loop(obj)

# f = 1
# my_own_for_loop(f)
# TypeError: 'int' object is not iterable

#=========================================================================#
# Types Of Iterators
#=========================================================================#
# 1) Built-in iterators (created internally)
#    Example: the iterator returned by iter(range(...)) or iter([...])
#
# 2) Custom iterators
#    Classes you write yourself.

#=========================================================================#
# How to Create Custom Iterators?
#=========================================================================#
# A custom iterator is a class that implements the iterator protocol:
# __iter__() and __next__().

# Example:
# Create an iterator that generates powers of 2 up to a given limit.

# Input: 16 -> 1, 2, 4, 8, 16
# Input: 64 -> 1, 2, 4, 8, 16, 32, 64

class PowerOfTwo:   # Custom iterator -> implements __iter__() and __next__().

    def __init__(self, max_value):
        self.limit = max_value
        self.current = 1    # Stores the current value/state of the iterator.

    def __iter__(self):
        return self         # An iterator returns itself.

    def __next__(self):
        if self.current <= self.limit:
            result = self.current
            self.current = self.current * 2
            return result
        else:
            raise StopIteration

n = 16   # original: n = int(input("Enter the limit:"))

iter_obj = PowerOfTwo(n)   # Create the iterator object.

# For an iterator, iter() returns the same iterator object.
print(iter_obj is iter(iter_obj))   # True
# That is why __iter__() has "return self".

# Each call to next() returns the next value and updates the iterator's state.
# print(next(iter_obj))   # 1
# print(next(iter_obj))   # 2
# print(next(iter_obj))   # 4
# ...

# A for loop automatically calls next() until StopIteration occurs.
for ele in iter_obj:
    print(ele)

# Because PowerOfTwo is an iterator (it keeps its state in itself), it is
# used up after one pass:
for ele in iter_obj:
    print(ele)   # prints nothing, the iterator is exhausted

#=========================================================================#
# Creating our own range() function
#=========================================================================#
# Here we need TWO classes:
#   - an iterable   (MyRange)          : stores start/end, can be looped many times
#   - an iterator   (MyRangeIterator)  : stores the current position, one pass
#
# Rule of thumb: state that changes while looping (the current position)
# belongs in the ITERATOR, never in the iterable.

class MyRange:   # Iterable class (only __iter__)

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return MyRangeIterator(self)   # a NEW iterator on every call


class MyRangeIterator:   # Iterator class (__iter__ + __next__)

    def __init__(self, iterable_obj):
        self.iterable = iterable_obj
        self.current = iterable_obj.start   # its OWN position

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.iterable.end:
            raise StopIteration

        value = self.current
        self.current += 1
        return value

for i in MyRange(1, 4):
    print(i)

x = MyRange(1, 4)
print(type(x))   # <class '__main__.MyRange'>
print(iter(x))   # <__main__.MyRangeIterator object at 0x...>

# CORRECTION: the earlier version did "self.iterable.start += 1", i.e. the
# iterator modified the iterable itself. Result: the range was "used up"
# after the first loop.
#   r = my_own_range(1, 4);  list(r) -> [1, 2, 3];  list(r) -> []   (BUG)
# With the fix, the position lives in the iterator, so it can be reused:
print(list(x), list(x))   # [1, 2, 3] [1, 2, 3]

#=========================================================================#
# Lazy Evaluation
#=========================================================================#
# Lazy Evaluation = evaluating or generating a value only when it is needed.
# Iterators allow lazy evaluation by generating elements on the fly as they
# are requested. This saves memory and can improve performance when working
# with large datasets.

# Example:
# Suppose we have 20 GB of image data to process but only 16 GB of RAM.
# Loading all images into memory at once may cause a MemoryError.
# An iterator can process the images one by one, loading only the required
# image into memory at a time instead of storing all 20 GB.

# Another proof of laziness: an iterator can even be infinite.
class Naturals:
    def __init__(self):
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.current += 1
        return self.current

nat = Naturals()
print(next(nat), next(nat), next(nat))   # 1 2 3 ... never runs out
# (never do list(nat) or "for x in nat" without a break!)
#=========================================================================#
