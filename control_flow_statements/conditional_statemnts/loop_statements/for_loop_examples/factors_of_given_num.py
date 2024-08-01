#factors count using for loop

n=int(input("enter the number"))
for x in range(1,n):
    if n%x==0:
        print("the factors of the number 'n' is:",x)
        
