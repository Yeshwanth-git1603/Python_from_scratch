#prime number check using functions

def prime_check(x):
    c=0
    for i in range(1,x+1):
        z=x%i
        if z==0:
            c+=1
    if c==2:
        print("prime")
    else:
        print("not prime")
        
prime_check(6)
