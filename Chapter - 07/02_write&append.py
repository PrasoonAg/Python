#=========================================================================#
# 02 - Write and Append
#=========================================================================#
#=========================================================================#
# "w" - Write Mode
#=========================================================================#
# Opens a file for writing.
# If the file doesn't exist, it is created.
# If the file already exists, all existing data is deleted (truncated).

f = open("2_demo1.txt", "w")

# write() writes data to the file.
# Writing again continues from the current file pointer.

f.write("I want to learn JavaScript tomorrow.\n")
f.write("Then I'll move to ReactJS.")

f.close()

#=========================================================================#
# "r+" - Read and Write Mode
#=========================================================================#
# Opens a file for both reading and writing.
# The file must already exist.
# The file pointer starts at the beginning.
# Existing data is overwritten from the current position.

d = open("2_demo2.txt", "r+")

d.write("ABC")

d.close()

#=========================================================================#
# "w+" - Read and Write Mode
#=========================================================================#
# Opens a file for both reading and writing.
# If the file doesn't exist, it is created.
# If the file already exists, all existing data is deleted (truncated).
# The file pointer starts at the beginning.

e = open("2_demo3.txt", "w+")

print(e.read())      # Prints an empty string because the file is empty.

e.write("ABC")

e.close()

#=========================================================================#
# "a+" - Append and Read Mode
#=========================================================================#
# Opens a file for both reading and appending.
# If the file doesn't exist, it is created.
# The file pointer starts at the end of the file.
# New data is always added at the end.

g = open("2_demo4.txt", "a+")

print(g.read())      # Prints an empty string because the pointer is at the end.

g.write("ABC")

g.close()

#=========================================================================#
# Quick Revision
#=========================================================================#
# "w"  -> Write only (Deletes existing data)
# "r+" -> Read & Write (Keeps existing data)
# "w+" -> Read & Write (Deletes existing data)
# "a+" -> Read & Append (Always writes at the end)
#=========================================================================#