#=========================================================================#
# 01 - Open, Read & Close a File
#=========================================================================#

# File Mode
#-------------------------------------------------------------------------#
# "r" -> Opens a file for reading.
# It is the default mode.
#
# Syntax:
# open("file_name_or_path", "r")
#=========================================================================#

# open() returns a file object.
# We store it in 'f' so we can perform operations like read(), write(),
# and close() on the file.

f = open("1_demo1.txt", "r")

#=========================================================================#
# read()
#=========================================================================#
# read() reads the entire file.
# If a number is passed (e.g. read(5)),
# it reads only that many characters.

data = f.read()

print(data)
print(type(data))      # <class 'str'>

#=========================================================================#
# readline()
#=========================================================================#
# readline() reads one line at a time.
# The returned line usually includes the newline character (\n).

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

#=========================================================================#
# Important
#=========================================================================#
# Both read() and readline() move the file pointer forward.
# Once the file pointer reaches the end of the file,
# reading again returns an empty string unless the pointer is moved back.

# Example:
# f.read()
# f.read()   # Returns "" because the file pointer is already at the end.

#=========================================================================#
# close()
#=========================================================================#
# Always close the file after using it.
# This frees system resources and is considered good practice.

f.close()

# Note:
# After closing the file, you cannot perform any operations on it
# unless you open it again.
#=========================================================================#