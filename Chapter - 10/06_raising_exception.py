#=========================================================================#
# 06 - Raise an Exception
#=========================================================================#
# raise creates an exception with a message but futher codes won't run i.e. Program Stops.
# raise  → "Something is wrong!"

a = int(input("Enter a number: "))
b = int(input("Enter a secound number: "))

if b == 0:
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero") 
# output -> this line of code
else:
    print(f"The division a/b is {a/b}")

# Example 1: Age Validation
age = int(input("Enter age: "))

if age < 0:
    raise ValueError("Age cannot be negative")
print(age)

print("Program continues...") # This won't run

# raise ValueError("Invalid Marks")
# raise ZeroDivisionError("Cannot divide by zero")
# raise TypeError("Wrong data type")
#=========================================================================#