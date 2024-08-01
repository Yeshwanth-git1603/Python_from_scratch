#prime number check using for loop

x=int(input("enter the number to check:"))
c=0
for i in range(1,x+1):
    z=x%i
    if z==0:
        c+=1
if c==2:
    print("prime number",x)
else:
    print("not prime",x)

