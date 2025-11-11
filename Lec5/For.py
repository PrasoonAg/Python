#04
#=========================================================================#
# for Loop in Python
#=========================================================================#
nums = [1,2,3,4,5]

for val in nums: #here nums value of list is stored in variable val. 
    print(val)
print("")

#=========================================================================#
veggies = ["potato", "brinjal", "ladyfinger", "cucumber"]

for val in veggies:
    print(val)
print("")

#=========================================================================#
tup = (1,2,3,4,2,8,9)

for num in tup:
    print(num)
print("")
#=========================================================================#
# Generally, when we need to update or change values dynamically or have a specific stopping condition, we use a while loop.
# On the other hand, when we need to traverse through elements of an iterable like a list, string, or tuple, we use a for loop.
#=========================================================================#
str = "apnacollage"

for char in str:
    print(char)
print("")
#=========================================================================#
#for Loop and else
#=========================================================================#
str = "apna collage"

for char in str:
    print(char)
else: #after the for loop this will print.
    print("END")
print("")
#=========================================================================#
str = "Prasoon Agrawal"

for char in str:
    if (char == 'o'):
        print("o found")
        break #it ended here after finding the 'o'
    print(char)
else: #Here else part is not not executed as end of the loop is break.
    print("END\n")
#=========================================================================#