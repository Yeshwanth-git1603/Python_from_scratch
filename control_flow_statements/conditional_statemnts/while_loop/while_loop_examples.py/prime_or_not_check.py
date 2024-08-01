#prime number check using while loop
x=int(input("enter a number:"))
i=1
c=0
while i<x+1:
    z=x%i
    i+=1
    if z==0:
        c+=1
if c==2:
    print("prime:",x)
else:
    print("not prime:",x)
        
