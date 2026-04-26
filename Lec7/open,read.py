#01
#=========================================================================#
# Open, read & close File
#=========================================================================#
# "r" - open for reading (default)
#=========================================================================#
# open("file_name or path","read mode")
f = open("demo1.txt","r")
# f stores the file object returned by open() so we can perform operations like read, write, and close on the file.
#f becomes object


# Methods read and readline #
#===#
data = f.read() # read() method will read entire file but insdie bracket  by mentioning number, letters will be printed accordinlgy.
print(data)
print(type(data))
#===#
line1 = f.readline() # reads one line at a time, and create a nextline in method i.e. \n
print(line1)

line2 = f.readline()
print(line2)

#only data can be printed once, as repeation won't happen & creates nextline
#===#

f.close # It is always recommended to close the file as anyone can access it.