# 06
#=========================================================================#
# Practice Questions - 2
#=========================================================================#
#Q1# Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if (n==1):
        return 1
    return sum(n-1) + n

print(sum(5))
#=========================================================================#
#Q2# Write a recursive function to print all elements in a list.
   # Hint: use list and index as paramters.

mylist = ["a","b","c","d","e"]
index = 0
def elements(my_list,index):
    if index == len(my_list):
        return
    print(my_list[index]) # print() before recursion  -> a b c d e
    elements(my_list,index + 1)
  # print(my_list[index]) # print() after recursion   -> e d c b a
elements(mylist,0)

# In recursion, code before the recursive call executes during Push ↓.
# Code after the recursive call executes during Pop ↑.
# Example:
# print() before recursion  -> a b c d e
# print() after recursion   -> e d c b a
# This helps visualize how the Call Stack builds and unwinds.
#=========================================================================#