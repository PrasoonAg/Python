#=========================================================================#
# Coding Exercise - Prime Number Checker
#=========================================================================#
# Question:
# Create a function is_prime() that returns True if a number is prime,
# otherwise False.
# Example: 7 -> True, 4 -> False, 1 -> False

#=========================================================================#
# My Approach
#=========================================================================#
def is_prime(num):
    if num <= 1:
        return False
    elif num % 2 == 0:
        if num == 2:
            return True
        else:
            return False
    else:
        for i in range(2, num):
            if num % i != 0:
                # Continue checking the remaining divisors.
                continue
            else:
                return False
    return True

print(is_prime(15))

#=========================================================================#
# Course Solution
#=========================================================================#
def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            # A divisor is found, so the number is not prime.
            return False

    # Runs only if no divisor is found.
    return True

print(is_prime(2))

#=========================================================================#
# Key Learning
#=========================================================================#
# My approach and the course solution use the same core logic.
# return ends the entire function, not just the loop.
# continue skips to the next loop iteration.
# return True after the loop means no divisor was found.
# My approach handles num <= 1; the course solution checks 1 and 2 only.

#=========================================================================#