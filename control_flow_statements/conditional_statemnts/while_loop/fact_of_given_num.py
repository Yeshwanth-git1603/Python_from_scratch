#while loop
#finding factorial of a given number

n=int(input("enter a number to check:"))
i=1
s=1
while i<=n:
    s=s*i
    i=i+1
print("the factorial of a given number is:",s)
