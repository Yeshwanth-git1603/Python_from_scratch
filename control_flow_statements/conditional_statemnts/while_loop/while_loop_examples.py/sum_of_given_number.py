#finding the sum of given number
number=int(input("enter the number to find sum"))
sum_of_digits=0
while number > 0:
    last_digit=number % 10
    sum_of_digits +=last_digit
    number=number//10
print("the sum of the number is",sum_of_digits)
