#=========================================================================#
# 05 - Squash bugs with a print() statement
#=========================================================================#
# print() is your friend when debugging. It helps expose hidden values
# while the code is running.

# In loops, intermediate values can be difficult to track. Using print()
# helps us observe how variables change during each iteration.

word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))  # Bug: == compares values; = assigns a value.

print(pages, word_per_page)  # Displays 0 for word_per_page because it was never reassigned.

total_words = pages * word_per_page
print(total_words)

#=========================================================================#
# Use Print()
#=========================================================================#
# print() is your friend when debugging. It helps expose hidden values
# while the code is running.

# In loops, intermediate values can be difficult to track. Using print()
# helps us observe how variables change during each iteration.

word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))  # Bug: == compares values; = assigns a value.

print(pages, word_per_page)  # Displays 0 for word_per_page because it was never reassigned.

total_words = pages * word_per_page
print(total_words)
#=========================================================================#