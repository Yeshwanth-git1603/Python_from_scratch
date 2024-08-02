#finding the sum of 1 to 10 using fucntions

def sum_of_n(n):
    sum1=0
    for x in range(1,n+1):
        sum1=sum1+x
    print("the sum of n numbers is:",sum1)
sum_of_n(10)
