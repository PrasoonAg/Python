#=========================================================================#
# 04 - Deleting a File
#=========================================================================#
import os
# remove() is used to delete a file.
# The file must exist, otherwise Python raises a FileNotFoundError.
os.remove("4_Delete.txt")

#=========================================================================#
# Syntax
#=========================================================================#
# os.remove("file_name_or_path")

#=========================================================================#
# Important Points
#=========================================================================#
# • Import the os module before using remove().
# • The file must exist before deleting it.
# • Deleted files cannot be recovered using Python.
# • Use this function carefully.
#=========================================================================#