#09
#P-4
#=========================================================================#
#@1# # WAP to find the sum of first n natural numbers.(using while)
n = 5
sum = 0

for i in range(1,n+1):
    sum += i
print("total sum:",sum)

#or

n= 7
sum = 0
i = 0

while i <= n:
    sum += i
    i += 1
print("total sum:", sum)
    
#=========================================================================#
#@2# # WAP to find the factorial of first n numbers.(using for)

n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("factorial =", fact)

#or

n = 5
fact = 1

for i in range(1, n+1):
    fact *= i
print("factorial:",fact)
#=========================================================================#