#07
#P-2
#=========================================================================#
#@1# #WAP to check if a number entered by the user is odd or even.
num = int(input("Enter a number:"))
if (num%2==0):
    print("Number is Even")
else:
    print("Number is Odd")
print("")

#or by apna collage
rem = num%2
if(rem==0):
    print("Even")
else:
    print("Odd")
print("")
#=========================================================================#
#@2# #WAP to find the greatest of 3 numbers entered by the user.
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

if(a>b and a>c):
    print("a is the largest:",a)
elif(b>c):
    print("b is the largest:",b)
else:
    print("c is the largest:",c)
print("")
#=========================================================================#
#@3# #WAP to check if a number is a multiple of 7 or not.
num2 = int(input("Enter a number"))

if(num2%7==0):
    print("Yes, the number is multiple of 7")
else:
    print("not a multiple of 7")
#=========================================================================#