#=========================================================================#
# Practice Questions
#=========================================================================#
#Q1# Write a program to open three files 1.txt, 2.txt and 3.txt
   # if any these files are not present, a message without exiting the
   # program must be printed prompting the same.

try:
    with open("1.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)
try:
    with open("2.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)
try:
    with open("3.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

print("Program not crashed!")

#=========================================================================#
#Q2# Write a program to print third, fifth and seventh element from a list
   # using enumerate function.

lis = [1,2,3,4,5,6,7,8,9,10]

for index, item in enumerate(lis, start=1):
    if index == 3 or index == 5 or index == 7:
        print(f"Item {item} is at position {index}")

#=========================================================================#
#Q3# Write a list comprehension to print a list which contains the multiplication
   # table of a user entered number.

n = int(input("Enter a number:"))
table = [n*i for i in range(1,11)]
print(table)

#=========================================================================#
#Q4# Write a program to display a/b where a and b are integers. if b=0,
   # display infinite by handling the 'ZeroDivisionError'.

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a/b)
except ZeroDivisionError as z:
    print("infinite")

#=========================================================================#
#Q5# Store the multiplication tables generated in problem 3 in a
   # file named Tables.txt.
   
with open("Tablex.txt","a") as f:
    f.write(str(table))
#=========================================================================#