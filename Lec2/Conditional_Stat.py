#06
#=========================================================================#
# Conditional Statements
#=========================================================================#
age = 99
if (age>=18):
    print("can vote")
    print("can drive\n")
#=========================================================================#
Light = input("Enter the traffic light color: ")
if (Light == "green"):
    print("go")
elif (Light == "yellow"):
    print("slow down")
elif (Light == "red"):
    print("stop")
else:
    print("invalid color")
print("End of program\n")
#=========================================================================#
num = int(input("Enter a number: "))
if (num>2):
    print("number is grater than 2")
if (num>3):
    print("number is grater than 3")
#Both if statements are checked and executed independently
elif(num>4):
    print("number is grater than 4")
#This will give an error because elif must be preceded by if or another elif
print("End of program\n")
#=========================================================================#
age = int(input("Enter your age: "))
if (age>= 18):
    print("You can vote")
else:
    print("You cannot vote")
#=========================================================================#
#Grade system based on marks
#This is one best-clean version for this
marks=int(input("Enter your marks:"))
if(marks>=90):
    print("Grade A")
elif(marks>=80):
    print("Grade B")
elif(marks>=70):
    print("Grade C")
elif(marks>=60):
    print("Grade D")
print("End of program\n")
#=========================================================================#
#Grading system done with logical operators
#This code is right but making the code redudant.
marks=int(input("Enter your marks:"))
if(marks>= 90):
    grade = "A"
elif(marks>= 80 and marks<90): #T and T
    grade = "B"
elif(marks>=70 and marks<80):
    grade = "C"
else:
    grade = "D"
print("Student Grade -->", grade)
#=========================================================================#
#nesting
age = 95
if (age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")
#=========================================================================#