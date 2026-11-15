#=========================================================================#
# 04 - Practice Questions (with solutions)
#=========================================================================#
# Q1-Q5 are the original questions. Q6-Q7 were added to cover the
# iterable-vs-iterator difference. Every solution has a small assert test,
# so running the file prints "All checks passed" when everything is right.
#
# Fixed values are used instead of input() so the file runs without waiting.
# To try your own value, replace e.g.  n = 5  with  n = int(input("Enter: "))

#=========================================================================#
#Q1# Create a custom iterator CountDown that:
#     - Takes a starting number.
#     - Returns numbers down to 1.
#     - Stops using StopIteration.

class CountDown:

    def __init__(self, start_value):
        self.current = start_value   # Stores the current value.

    def __iter__(self):
        return self   # The object itself is the iterator.

    def __next__(self):
        # FIX: was "== 0", which never stops for a negative start (-1, -2, ...).
        # "< 1" also makes CountDown(0) and CountDown(-3) produce nothing.
        if self.current < 1:
            raise StopIteration   # Stops the iteration.

        result = self.current
        self.current -= 1   # Move to the next value.

        return result

n = 5
for value in CountDown(n):
    print(value)

# for loop → iter(obj) → __iter__() → return obj → next(obj) → __next__() →
# return value → update state → repeat → StopIteration → loop stops

assert list(CountDown(5)) == [5, 4, 3, 2, 1]
assert list(CountDown(1)) == [1]
assert list(CountDown(0)) == []
assert list(CountDown(-3)) == []

#=========================================================================#
#Q2# Create a custom iterator EvenNumbers that:
#     - Takes a limit.
#     - Returns only even numbers from 2 up to the limit.

class EvenNumbers:

    def __init__(self, max_value):
        self.max_value = max_value   # Stores the maximum limit.
        self.current = 2             # Stores the current even number.

    def __iter__(self):
        return self   # The object itself is the iterator.

    def __next__(self):
        if self.current > self.max_value:
            raise StopIteration   # Stops when the limit is exceeded.

        result = self.current
        self.current += 2         # Move to the next even number.

        return result

n = 10
for value in EvenNumbers(n):
    print(value)

assert list(EvenNumbers(10)) == [2, 4, 6, 8, 10]
assert list(EvenNumbers(9)) == [2, 4, 6, 8]
assert list(EvenNumbers(1)) == []

#=========================================================================#
#Q3# Create a custom iterator PowerOfTwo that:
#     - Takes a maximum value.
#     - Starts at 1.
#     - Returns powers of 2.
#     - Stops when the next power exceeds the limit.

class PowerOfTwo:

    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 1

    def __iter__(self):
        return self   # The object itself is the iterator.

    def __next__(self):
        if self.current > self.max_value:
            raise StopIteration   # Stops when the current value exceeds the limit.

        result = self.current
        self.current *= 2         # Move to the next power of 2.

        return result

n = 20
for value in PowerOfTwo(n):
    print(value)

assert list(PowerOfTwo(16)) == [1, 2, 4, 8, 16]
assert list(PowerOfTwo(20)) == [1, 2, 4, 8, 16]
assert list(PowerOfTwo(0)) == []

#=========================================================================#
#Q4# Create a custom iterator Multiples that:
#     - Takes two values: number and limit.
#     - Returns multiples of number up to limit.

class Multiples:

    def __init__(self, number, limit):
        # FIX: number = 0 would give 0, 0, 0, ... forever (0 never exceeds
        # a positive limit). Negative numbers would never reach the limit.
        if number <= 0:
            raise ValueError("number must be a positive integer")
        self.number = number
        self.limit = limit
        self.multiplier = 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.number * self.multiplier

        if result > self.limit:
            raise StopIteration

        self.multiplier += 1
        return result

for value in Multiples(3, 15):
    print(value)

assert list(Multiples(3, 15)) == [3, 6, 9, 12, 15]
assert list(Multiples(3, 14)) == [3, 6, 9, 12]
assert list(Multiples(5, 4)) == []
try:
    Multiples(0, 10)
    raise AssertionError("expected ValueError")
except ValueError:
    pass

#=========================================================================#
#Q5# Create a custom iterator Fibonacci that:
#       - Takes a count n.
#       - Returns the first n Fibonacci numbers.
# 0 1 1 2 3 5 8
#
# (The original attempt was commented out and unfinished. It tried to
#  detect the first value with "if self.a == 0", which breaks, because a
#  becomes 1 after the first step and the logic gets confusing.)
#
# Cleaner idea: keep two variables a, b = 0, 1 and a counter of how many
# numbers were already returned.
#   return a, then move forward:  a, b = b, a + b

class Fibonacci:

    def __init__(self, count):
        self.count = count      # How many numbers to produce.
        self.produced = 0       # How many were already produced.
        self.a = 0              # Current Fibonacci number.
        self.b = 1              # The one after it.

    def __iter__(self):
        return self

    def __next__(self):
        if self.produced >= self.count:
            raise StopIteration

        result = self.a
        self.a, self.b = self.b, self.a + self.b   # Move forward.
        self.produced += 1

        return result

for value in Fibonacci(7):
    print(value)   # 0 1 1 2 3 5 8

assert list(Fibonacci(7)) == [0, 1, 1, 2, 3, 5, 8]
assert list(Fibonacci(1)) == [0]
assert list(Fibonacci(0)) == []

#=========================================================================#
#Q6# (Added) Create an ITERABLE class Reverse that:
#     - Takes a list.
#     - Loops over it from the last item to the first.
#     - Can be looped over more than once.
#
# Hint: this needs two classes, like MyRange in 03. The position goes in
# the iterator class, so each loop gets a fresh one.

class Reverse:   # Iterable

    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return ReverseIterator(self.data)   # new iterator every time


class ReverseIterator:   # Iterator

    def __init__(self, data):
        self.data = data
        self.index = len(data)   # start just past the last item

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration

        self.index -= 1
        return self.data[self.index]

rev = Reverse(["a", "b", "c"])
print(list(rev))   # ['c', 'b', 'a']
print(list(rev))   # ['c', 'b', 'a']  <- works again, because Reverse is an iterable

assert list(rev) == ["c", "b", "a"]
assert list(rev) == ["c", "b", "a"]
assert list(Reverse([])) == []

#=========================================================================#
#Q7# (Added) Predict the output, then run it.
#
#   it = CountDown(3)
#   print(list(it))
#   print(list(it))
#
# Answer: [3, 2, 1] and then []. CountDown is an iterator: once used up it
# does not restart. To loop again, create a new CountDown(3).

it = CountDown(3)
print(list(it))   # [3, 2, 1]
print(list(it))   # []

assert list(CountDown(3)) == [3, 2, 1]

#=========================================================================#
print("All checks passed")
