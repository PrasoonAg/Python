#=========================================================================#
# 03 - With Statement
#=========================================================================#
# with is used to work with files safely.
# It automatically closes the file after the block is executed,
# even if an error occurs.

# Syntax:
# with open("file_name", "mode") as variable_name:

# "as" assigns the file object to a variable.
# (It is NOT an alias in the traditional sense; it simply stores
# the returned file object in the given variable.)

with open("3_demo1.txt", "r") as f:
    data = f.read()
    print(data)

# No need to call f.close().
# The file is closed automatically after the with block.


with open("3_demo1.txt", "w") as f:
    f.write("Hello World")

#=========================================================================#
# Advantages of using with
#=========================================================================#
# Automatically closes the file.
# Works even if an error occurs.
# Makes the code cleaner and shorter.
# Recommended way to work with files.

#=========================================================================#
# When to use open() instead?
#=========================================================================#
# Use open() when you want manual control over when
# the file should be opened and closed.
#=========================================================================#