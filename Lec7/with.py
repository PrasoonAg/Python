#03
#=========================================================================#
# With syntax
#=========================================================================#
with open("demo6.txt","r") as f: # here as means alias(meaning same but different name like tony stark/ironman)
    data = f.read()
    print(data)
# closing is not important here as with automatically close the file.

with open("demo6.txt","w") as f:
    f.write("hello world")

# works even when error happens
# cleaner and shorter code
# automatically close the file (with handle opening and closing)

#open() use when you want manual control

