
#non sequential data types
#1:set
#set doesnt allow duplicate into it

set1={1,2,3,4,5,5,6,7,8,4,4,5,6}
print(set1)
set1.add(10)
print(set1)
set1.add(9)
print(set1)
set1.remove(9)
print(set1)

#frozen set
#unlike normal set a frozen set doesnt allow mutation like normal set the values are fixed once it is frozen

fs=frozenset(set1)
print(fs)

