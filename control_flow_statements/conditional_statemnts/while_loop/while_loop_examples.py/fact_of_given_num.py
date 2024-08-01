#finding the factorial of a given number using while loop
i=1
n=int(input("enter the fact num to find"))
s=1
while i<=n:
    s=s*i
    i+=1
print("the factorial of a given number is:",s)
