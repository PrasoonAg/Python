#03
#=========================================================================#
# Break
#=========================================================================#

i = 1
while i <= 5:
    print(i)
    if(i==3):
        break #ended here
    i+= 1
print("End Of The Loop \n")

#=========================================================================#
nums = (1,4,9,16,25,36,49,64,81,100)

x = 36
i = 0

while i < len(nums):
    if (nums[i] == x):
        print("Found at idx",i)
        break # Code ended after finding the index
    else:
        print("finding..")
    i += 1
print("End of the loop \n")

#=========================================================================#
# Continue
#=========================================================================#
i = 0
while i<= 5:
    if (i==3):  # start: i = 3(after iteration 2) # i == 3? → Yes
        i+=1    # inside if do i += 1 → i becomes 4
        continue
# continue → skip the rest of loop body (so we do not run the i += 1 after the if, and we do not run print(i) this iteration)
# jump to while condition check
    i += 1
    print(i)
print("")

#=========================================================================#
i = 1
while i <= 10:
    if(i%2 == 0):
        i += 1
        continue #skip
    print(i)
    i+=1
print("")
#=========================================================================#
i = 1
while i <= 10:
    if(i%2 != 0):
        i += 1
        continue #skip
    print(i)
    i+=1
print("")
#=========================================================================#