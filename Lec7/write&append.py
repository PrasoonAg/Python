#02
#=========================================================================#
# Write and append
#=========================================================================#
# write #
f = open("demo2.txt","w") #if the file demo2.txt doesn't exist then it will create it

f.write("I want to learn javascript tomorrow ") #overwrite the data and add new consequently
f.write("Then I'll move to ReactJS")

# read and write "r+" #
d = open("demo3.txt","r+") # read and write(overwrite). The stream/pointer is positioned at the beginning.

d.write("abc")

# open for reading and writing "w+" #
e = open("demo4.txt","w+") # open for reading and writing truncate
print(e.read())
e.write("abc")

# open for reading and writing "a+"
g = open("demo5.txt","a+") #read and write (end). the stream/pointer is postioned at the end.
print(g.read())
g.write("abc")
g.close