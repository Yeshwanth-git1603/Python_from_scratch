# sum of n numbers using recursion

def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
    
res=sum(5)
print("the sum of the given seq is",res)
