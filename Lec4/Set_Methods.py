#05
#=========================================================================#
# Set Methods
#=========================================================================#

collection = set() #Empty/Null set
#=========================================================================#
# add
collection.add(1)
collection.add(2)
collection.add(2) #value will be considered one time.
collection.add(3)
collection.add("Prasoon") # added String (immutable)
collection.add((1,2,3,"Hi")) # added tuple (immutable)

print(collection,"\n")

#collection.add([1,2,3]) #error will come

#=========================================================================#
# remove
collection.remove(1)
collection.remove(2)
# collection.remove(7) # An error will be came.
print(collection,"\n")

#=========================================================================#
#pop
print(collection.pop()) #random value will be poped
print(collection.pop(),"\n")

#=========================================================================#
# clear
collection.clear() #Will give set() and length => 0.

print(collection)
print(len(collection),"\n")

#=========================================================================#
set1 = {1,2,3}
set2 = {2,3,4}

#union
print(set1.union(set2)) #{1,2,3,4}
print(set1)
print(set2,"\n")

#=========================================================================#
#intersection
print(set1.intersection(set2)) # {2,3}

#=========================================================================#
