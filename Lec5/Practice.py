#02
#=========================================================================#
# Print numbers from 1 to 100.
a = 1
while a<= 100:
    print(a)
    a += 1
print("")
#=========================================================================#
# Print numbers from 100 to 1.
b = 100
while b>=1:
    print(b)
    b -= 1
print("")
#=========================================================================#
# Print the multiplication table of a number n.

#BY Me
n = int(input("Enter a number:"))
x = 1
while x <=10:
    print(n*x)
    x += 1
print("")

#BY Apna Collage
i = 1
while i <= 10:
    print(4*i)
    i += 1
#=========================================================================#
# Print the elements of the following list under a Loop:
#[1,4,9,16,25,36,49,64,81,100]

#Traverse ==> Travelling each elment in list , set , tuple.

#By Me (read the question wrong, made list instead)
k = []
l = 1
while l<=10:
    k.append(l*l)
    l += 1
print(k,"\n")
#Now k = [1,4,9,16,25,36,49,64,81,100]

#REVISE IT
idx = 0
while idx < len(k):
    print(k[idx])    
    idx += 1
#EXPLAINATION
#index always start with 0 so here
#index = 0 , 1 , 2 , 3 , ..... , len(list)-1
# while idx <= len(list)-1 (9=9 here and 0 to 9 values will be printed)
#or better way
#while idx < len(list) (9<10 here and 0 to 9 values will be printed)

#EXAMPLE
heroes = ["ironman","thor","superman","batman"]
h = 0
while h < len(heroes):
    print(heroes[h])
    h += 1

#=========================================================================#
#Search for a number x in this tuple using loop:
#(1,4,9,16,25,36,49,64,81,100)

nums = (1,4,9,16,25,36,49,64,81,100)
x = 100
i = 0 #intialization
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at index", i)
    else:
        print("Finding..")
    i += 1
#=========================================================================#