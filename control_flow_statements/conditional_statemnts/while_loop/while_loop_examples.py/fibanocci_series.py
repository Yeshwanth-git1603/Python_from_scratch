#fibanocci series using while loop
num=10
a,b=0,1
i=0
print("fibanocci series of:",num)
while i<=num:
    print(a,end=" ")
    a,b=b,a+b
    i+=1
    
