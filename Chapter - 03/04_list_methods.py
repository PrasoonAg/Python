#=========================================================================#
# 03 - List Methods
#=========================================================================#
# append()
#=========================================================================#
# Add an item to the end of the list.
list = [2,1,3]
list.append(4)
print(list)

list.extend([])

#=========================================================================#
# extend()
#=========================================================================#
# adds all items from an iterable to the end of the list.
list.extend([5,6,7,8,9,0])
print(list)

#=========================================================================#
# sort()
#=========================================================================#
print(list.sort()) # returns none value
print(list)

#=========================================================================#
# sort(reverse=True) (print the vaules in descending order)
list2=['a','d','e','f','c','b']
print(list2.sort(reverse=True)) # None
print(list2) # ['f', 'e', 'd', 'c', 'b', 'a']
# This gives 'f' first as in ascending 'a' comes first, so here visa versa.

#=========================================================================#
# reserve()
#=========================================================================#
list3=['a','d','e','f','c','b']
list3.reverse()
print(list3)

#=========================================================================#
# insert()
#=========================================================================#
list4=[2,1,3]
list4.insert(2,5) # (index,value)
# The new value (5) will be inserted at the index position 2
print(list4)

#=========================================================================#
# remove()
list5=[2,1,3,1] # Remove the first occurance of element
list5.remove(1)
print(list5)

#=========================================================================#
# pop() (removes the value of particular index position)
#=========================================================================#
list6 = [2,1,3,1]
list6.pop(2)
print(list6)

#=========================================================================#
# copy()
#=========================================================================#
list7 = [1,2,3]

copy_list7= list7.copy()
copy_list7.reverse # not calling this method yet, adding () this will reverse it.

if(copy_list7==list7):
    print("yup")
else:
    print("no")

#=========================================================================#
import random # importing random module
#=========================================================================#
# Fetching random data from list.

# choice()
# Choose a random element from a non-empty sequence.

friends = ["Chandler", "Joye", "Faiz", "Aaditya"]
print(random.choice(friends))

# choices()
# Returns a list containing random elements from the sequence.
# Always wraps the result in a list (e.g., ['Chandler']), even for a single item!
friends_list = random.choices(friends, k=1)
print(friends_list)

# randint()
# Return random integer in range [a, b], including both end points.

random_index = random.randint(0,3)
print(friends[random_index])
#=========================================================================#