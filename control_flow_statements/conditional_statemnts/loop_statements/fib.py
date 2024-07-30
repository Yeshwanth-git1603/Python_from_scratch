#fibanocci of the given range

def fib(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
for x in range(10):
    res=fib(x)
    print(res)
    
