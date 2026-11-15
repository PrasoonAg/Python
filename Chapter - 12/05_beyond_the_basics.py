#=========================================================================#
# 05 - Beyond the Basics (added to complete the chapter)
#=========================================================================#
# Short extras that usually come right after the iterator protocol.

from itertools import islice

#=========================================================================#
# 1) iter(callable, sentinel)
#=========================================================================#
# iter() has a second form: iter(function, stop_value). It calls function()
# again and again, and stops as soon as it returns stop_value.

numbers = [3, 2, 1, 0, 9, 9]
source = iter(numbers)

# keep calling next(source) until it returns 0:
print(list(iter(lambda: next(source), 0)))   # [3, 2, 1]
# Typical real use: reading a file in chunks until read() returns "".

#=========================================================================#
# 2) Legacy: iterating with only __getitem__()
#=========================================================================#
# If a class has no __iter__() but has __getitem__(), iter() builds an
# iterator that calls obj[0], obj[1], obj[2] ... until IndexError.

class Three:
    def __getitem__(self, index):
        if index >= 3:
            raise IndexError
        return index * 10

print(list(Three()))   # [0, 10, 20]
# Modern code should define __iter__() instead.

#=========================================================================#
# 3) Built-in iterators you already use
#=========================================================================#
# - file objects are iterators:      for line in open("x.txt"): ...
# - dict iterates over keys:         for k in {"a": 1}: ...   -> "a"
# - zip(), map(), enumerate(), reversed(), filter() all return iterators
print(type(zip([1], [2])))
print(type(enumerate("ab")))

z = zip([1, 2], ["a", "b"])
print(list(z))   # [(1, 'a'), (2, 'b')]
print(list(z))   # []  -> iterators are one-pass

#=========================================================================#
# 4) Slicing an iterator: itertools.islice
#=========================================================================#
# Iterators can't be sliced with [ : ]. Use islice (works on infinite ones).
def naturals():
    n = 0
    while True:
        n += 1
        yield n

print(list(islice(naturals(), 5)))   # [1, 2, 3, 4, 5]

#=========================================================================#
# 5) Preview: generators (next chapter) - the shortcut for custom iterators
#=========================================================================#
# The PowerOfTwo class from 03 needs ~15 lines. A generator function does
# the same in 5. "yield" pauses the function and remembers its state;
# falling off the end raises StopIteration automatically.

def power_of_two(limit):
    current = 1
    while current <= limit:
        yield current
        current *= 2

print(list(power_of_two(16)))   # [1, 2, 4, 8, 16]

# A generator object is an iterator (has __iter__ and __next__), so it is
# also one-pass.
g = power_of_two(4)
print(iter(g) is g)   # True
#=========================================================================#
