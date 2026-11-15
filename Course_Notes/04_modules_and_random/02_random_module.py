#=========================================================================#
# Importing our own python file/module here
import my_module as module

print(module.my_fav_number)

#=========================================================================#
# Random Module
#=========================================================================#
import random
# The random module is a built-in Python module that provides functions for
# generating pseudo-random values.

# Pseudo-random values : Values that look random, but are actually generated
# by a computer using an algorithm.

# random.randint(a, b)
# Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
random_integer = random.randint(1,10)
print(random_integer)

# random.random()
# Return the next random floating-point number in the range 0.0 <= X < 1.0
random_float = random.random()
print(random_float) # default 0.0 to 1.0 (never include one)
random_float = random.random() * 10
print(random_float) # now 0.0 to 10.0

# random.uniform()
# random.uniform(a, b)
# Return a random floating-point number N such that a <= N <= b for a <= b and
# b <= N <= a for b < a.
random_float = random.uniform(1,10)
print(random_float) # may get 10
#=========================================================================#
# Random heads and tails

random_heads_or_tails= random.randint(0,1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")
#=========================================================================#