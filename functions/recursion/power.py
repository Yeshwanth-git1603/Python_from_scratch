#power function in recursion

def power(x,n):
    if n==0:
        return 1
    else:
        return x * power(x, (n-1))
        
res=power(2,3)
print("the power of the given number is",res)
