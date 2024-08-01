#factors of a given number

n=int(input("enter the num to find the factors:"))

for i in range(1,n+1):
    if n % i==0:
        print("the factors of a given number is",i)
