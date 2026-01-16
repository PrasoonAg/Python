# 07
# P-1
#=========================================================================#
#@1# #WAP to ask the user to enter names of thier 3 favorite movies and store them in a list.
#=========================================================================#
#Self done by Prasoon
a= input("1st movie:")
b= input("2nd movie:")
c= input("3rd movie:")
list=[a,b,c]

print(list,"\n")

#or DONE BY ---APNA COLLAGE WAY---
movies1=[] #Making the list (like we always do first, it create the list so it basically doesnt mean we have to have some elements in advance in the list to assaign list)
mov = input("enter 1st movies: ")
movies1.append(mov)
mov = input("enter 2nd movies: ")
movies1.append(mov)
mov = input("enter 3rd movies: ")
movies1.append(mov)

print(movies1,"\n")

#One More By ---APNA COLLAGE WAY---
movies2 = []
movies2.append(input("enter 1st movie: "))
movies2.append(input("enter 2nd movie: "))
movies2.append(input("enter 3rd movies: "))

print(movies2,"\n")

#=========================================================================#
#@2# #WAP to check if a list contains a palindrome of elements.(Hint: use copy() method)
#Palindrome ==> A word, phrase, number, or sequence that reads the same backward as forward. Ex - ma'am, racecar.
#[1,2,3,2,1] and [1,"abc","abc",1]
#-------------------------------------------------------------------------#
#It mentioned to check palindrome so we have to have before and after reverse equal then only considered palindrome

#By Me
#list1 = [1,2,3]
#list1 = [1,2,3]
list1 = ["m","a","a","m"]
list2 = list1.copy()
list2.reverse()
print(list2)

if(list1==list2):
    print("Yes its an Palindrome")
else:
    print("Its not an Palindrome")

#By Apna Collage
lis1 = [1,2,1]
#lis1 = [1,2,3]
#lis1 = ["m","a","a","m"]

copy_lis1 = lis1.copy()
copy_lis1.reverse()

if(copy_lis1==lis1):
    print("Palindrome")
else:
    print("not Palindrome")

#=========================================================================#
#@3# #WAP to count the number of students with the "A" grade in the following tuple.
# ["C","D","A","A","B","B","A"]

grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))

#=========================================================================#
#@4# #Store the above vaules in a list & sort them from "A" to "D".
grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)
#=========================================================================#