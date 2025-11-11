#03
#=========================================================================#
#List Methods
#=========================================================================#
#Append
list = [2,1,3]
list.append(4)
print(list)
#=========================================================================#
#sort
print(list.sort()) #returns none value
print(list)
#=========================================================================#
#sort(reverse=True)(print the vaules in descending order)
list2=['a','d','e','f','c','b']
print(list2.sort(reverse=True))
print(list2)
#This gives 'f' first as in ascending 'a' comes first, so here visa versa.
#=========================================================================#
#reserve()
list3=['a','d','e','f','c','b']
list3.reverse()
print(list3)
#=========================================================================#
list4=[2,1,3]
list4.insert(2,5) #The new value (5) will be inserted at the index position 2
print(list4)
#=========================================================================#
#remove
list5=[2,1,3,1] #Remove the first occurance of element
list5.remove(1)
print(list5)
#=========================================================================#
#pop (removes the value of particular index position)
list6 = [2,1,3,1]
list6.pop(2)
print(list6)
#=========================================================================#
#copy
list7 = [1,2,3]
list8 = [1,2,3]

copy_list7= list7.copy()
copy_list7.reverse

if(copy_list7==list7):
    print("yup")
else:
    print("no")
#=========================================================================#