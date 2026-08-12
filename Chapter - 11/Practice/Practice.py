#=========================================================================#
# Practice Questions
#=========================================================================#
#Q1# Create two virtual environments, install few packages in the first one.
   # How do you create a similar environment in the second one?

#=========================================================================#
#Q2# Write a program to input name, marks and phone number of a student and format it using the format function like below:
   # “The name of the student is Harry, his marks are 72 and phone number is 99999888”.
   
name = input("Enter Name: ")
marks = input("Enter marks: ")
phone_number = input("Enter Phone number: ")
print("The name of the student is {0}, his marks are {1} and phone number is {2}".format(name,marks,phone_number))

#=========================================================================#
#Q3# A list contains the multiplication table of 7. Write a program to convert
   # it to vertical string of same numbers.
   # 7
   # 14

table = [str(7*i) for i in range(1,11)]

s = "\n".join(table)
print(s)

#=========================================================================#
#Q4# Write a program to filter a list of numbers which are divisible by 5.

numbers = [5, 12, 10, 15, 24, 20, 34, 45, 100]

def divisible5(n):
    if(n%5 == 0):
        return True
    return False
f = list(filter(divisible5,numbers))
print(f)

# Self done
print(list(filter(lambda x:x%5==0,numbers)))

#=========================================================================#
#Q5# Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce
l = [111, 2, 65, 53, 635, 65, 74, 45, 55]

def grater(a,b):
    if(a>b):
        return a
    return b
print(reduce(grater,l))

print(reduce(lambda a,b: a if a>b else b, l))

#=========================================================================#
#Q6# Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv.

#=========================================================================#
#Q7# Explore the ‘Flask’ module and create a web server using Flask & Python.
#=========================================================================#