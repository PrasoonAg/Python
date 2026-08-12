#=========================================================================#
# 10 - Enumerate Function
#=========================================================================#
# The 'enumerate' function adds counter to an iterable and returns it.
lis = [3, 513, 53, 535]

index1 = 0
for item in lis:
    print(f"The item number {index1} is {item}")
    index1 += 1

print("")
# This can be simplified using enumerate function

for index2,item in enumerate(lis): # enumerate() returns (index, value) pairs.
    print(f"the item number at index {index2} is {item}")
    
# By default, indexing starts from 0.
# enumerate(iterable, start=1) can be used to start from a different index.
#=========================================================================#