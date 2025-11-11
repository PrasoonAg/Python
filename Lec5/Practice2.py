#05
#P-2
#=========================================================================#
#Practice Questions based on for loop
#=========================================================================#
#@1# #Print the elements of the following list using a loop:
[1,4,9,16,25,36,49,64,81,100]
lis = [1,4,9,16,25,36,49,64,81,100]
for val in lis:
    print(val)
print("")

#=========================================================================#
#@2# #Search for a number x in this tuple using loop:
# (1,4,9,16,25,36,49,64,81,100,49)
nums = (1,4,9,16,25,36,49,64,81,100,49)

x = 49 #This number to be searched # variable
idx = 0 #variable is not actaual index # variable

for el in nums:
    if(el==x):
        print("Number found at index:",idx)
        #break #This one will end the loop.
    idx += 1
print("END")

# Linear Search in Python (or in general) is a simple searching technique used to find a particular element in a list (or any sequence) by checking each element one by one until the target is found or the list ends.

#=========================================================================#