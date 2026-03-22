#06
#P-2
#=========================================================================#
#Practice Questions
#=========================================================================#
#@1# Write a recursive function to calculate the sum of first n natural numbers.

def calc_sum(n):
    if (n==0):
        return
    return calc_sum(n-1) + n

#or
def sum(n):
    if (n==1):
        return 1
    return sum(n-1) + n

print(sum(5))
#=========================================================================#
#@2# Write a recursive function to print all elements in a list.
# Hint: use list and index as paramters.