#=========================================================================#
# 01 - Walrus Operator (:=)
#=========================================================================#
# The Walrus Operator (:=) was introduced in Python 3.8.
# Assign a value and use it in the same expression.
# Variable := expression (this gets evaluated and assigned to vairable and then returned)

if (n := len([1,2,3,4,5]) ) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")

# Equivalent to:
# n = len([1,2,3,4,5])
# if n > 3:
#     print(f"List has {n} elements")
#=========================================================================#
num = [1,2,3,4,5]

while (n := len(num)) > 0 : # len(numbers) is assigned to n inside the loop condition
    print(num.pop())
#=========================================================================#
# Common Uses:
# 1. while loops
# 2. input handling
# 3. avoiding repeated calculations
#=========================================================================#