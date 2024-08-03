#using reduce function
from functools import reduce
def red(n):
    s=0
    for x in range(n+1):
        s=s+x
        res=red(10)
print("the sum of the seq is:",res)

#lambda reduce function

x=reduce(lambda x,y:x+y,l1)
print("the sum of the list is:",x)
