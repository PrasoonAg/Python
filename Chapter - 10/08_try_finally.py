#=========================================================================#
# 08 - Try With Finally
#=========================================================================#
# finally executes whether an exception occurs or not.
# It is commonly used for cleanup code.
try:
    a = int(input("Enter a number: "))
    print(a)

except Exception as e:
    print(e)

finally:  # Executes regardless of whether an exception occurs or not.
    print("Hey i am inside a finally")
    
# Now question arise why not write it direclty?
print("Hey i can run here aswell")
# Isn't the behaviour same?

# When finally is used in FUNCTIONS:
def main ():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally: # If finally isnt there then this block of code will not run as we return is in above code.
        print("Hey i am inside a finally")

main()
#=========================================================================#