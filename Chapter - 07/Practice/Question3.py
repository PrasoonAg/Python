#=========================================================================#
# Q3 - Count the Number of Even Numbers
#=========================================================================#
# WAF to read numbers separated by commas from a file
# and print the count of even numbers.

# Example file content:
# 1,2,45,55,86,76

count = 0

with open("practice2.txt", "r") as f:

    # read() returns the entire file contents as a string.
    data = f.read()
    print(data)

    #---------------------------------------------------------------#
    # Method 1 (Recommended)
    #---------------------------------------------------------------#

    # split(",") separates the string into a list of numbers.
    nums = data.split(",")

    print(nums)

    for val in nums:

        # Convert each number from string to integer
        # before checking whether it is even.
        if int(val) % 2 == 0:
            count += 1

print("Even numbers:", count)


#---------------------------------------------------------------#
# Method 2 (Without using split())
#---------------------------------------------------------------#

# count = 0
# num = ""

# for i in range(len(data)):
#
#     if data[i] == ",":
#
#         if int(num) % 2 == 0:
#             count += 1
#
#         num = ""
#
#     else:
#         num += data[i]
#
# # Process the last number because it is not followed by a comma.
# if int(num) % 2 == 0:
#     count += 1
#
# print("Even numbers:", count)
#=========================================================================#