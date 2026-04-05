f = open("Demo.txt","r")
# f stores the file object returned by open() so we can perform operations like read, write, and close on the file.

data = f.read()
print(data)
print(type(data))