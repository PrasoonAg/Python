#=========================================================================#
# 10 - global keyword
#=========================================================================#
# 'global' keyword is used to modify the variable outside the current scope.
a = 89
def fun():
    global a # global keyword modifies the local vairable to global
    a = 3    # inside the function a is local
    print(a)

fun()
print(a) # 3 will be printed not 89
#=========================================================================#