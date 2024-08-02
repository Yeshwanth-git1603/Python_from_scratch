# fibanocci using recursion

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
for x in range(0,10+1):
    res=fib(x)
    print(res,end=" ")
