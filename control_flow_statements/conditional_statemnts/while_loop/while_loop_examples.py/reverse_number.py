#reverse of a given number

number=int(input("enter the number to reverse"))
reverse_number=0
while number > 0:
    last_digit=number%10
    reverse_number=(reverse_number*10) + last_digit
    number=number//10
print("the rev of the number is",reverse_number)
