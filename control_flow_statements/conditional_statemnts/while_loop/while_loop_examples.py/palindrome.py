#checking whether a given number is palindrome or not using while loop
i=1
n=5
while i<n:
    num=input("enter the number")
    if num==num[::-1]:
        print("palindrome")
    else:
        print("not a palindrome")
    i+=1
