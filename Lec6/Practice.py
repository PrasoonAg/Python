#04
#P-1
#=========================================================================#
#Practice Questions
#=========================================================================#
# #@1# WAF to print the length of a list. (list is the parameter)

# # (by apna collage)
# cities = ["Jabalpur","Bhopal","Indore","Sachi"]
# heroes = ["Thor","Spiderman","Captain America","Iron Man"]
# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heroes)

# #or

# def len_list1():
#     a,b,c = input("Enter 3 numbers: ").split()
#     Lis = [a,b,c]
#     print(Lis)
#     return Lis
# len_list1()
# #Input by default create string.

# #or

# def len_list():
#     # input() → takes input as a single string from the user
#     # .split() → splits that string into separate values based on spaces
#     # map(int, ...) → converts each split value from string to int
#     # list(...) → converts the mapped values into a list
#     lis = list(map(int, input("Enter four numbers: ").split()))
    
#     # len(lis) → counts how many items are in the list
#     print(len(lis))

#     # returning the length of the list
#     return len(lis)

# # calling the function
# # len_list()


#=========================================================================#
#@2# WAF to print the elements of a list in a single line.(list in the parameter)
cities = ["Jabalpur","Bhopal","Indore","Sachi"]
heroes = ["Thor","Spiderman","Captain America","Iron Man"]
def print_len1(list):
    x= 0
    while x < len(list):
        print(list[x])
        x +=1
    
print_len1(cities)
