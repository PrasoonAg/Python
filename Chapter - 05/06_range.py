#=========================================================================#
# 06 - Range
#=========================================================================#
print(range(5)) # no number print, output -> range(0, 5)
print("")

#=========================================================================#
seq = range(10)
for i in seq:   # output numbers from 0 to 9
    print(i)
print("")

#=========================================================================#
seq = range(5)
print(seq[4]) # output -> 4
print("")

#=========================================================================#
for i in range(5): # output numbers from 0 to 4
    print(i)
print("")

#=========================================================================#
# range(Start?, Stop, Step?)
for i in range(10): # range(stop)
    print(i)
print("")

for n in range(2,10): # range(start,stop)
    print(n)
print("")

for n in range(2,10,2): # range(start,stop,step)
    print(n)
print("")

for p in range(2,100,2):
    print(p)
#=========================================================================#