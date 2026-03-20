#05
#=========================================================================#
# Recursion
#=========================================================================#
# When a functions call itself repadelty.
# Loops and Recursion can do same thing.(have same concept)

#simple code
#Recursive Function
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5) #5 = n, 4 = n-1, 3 = n-2, 2 = n-3, 1 = n-4
