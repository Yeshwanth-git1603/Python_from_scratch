# finding the reverse of a number using functions
def reverse_number(number):
    reverse_number=0
    while number>0:
        last_digit=number%10
        reverse_number=(reverse_number * 10) + last_digit
        number=number//10
    print("the reverse of the given number is",reverse_number)
reverse_number(35355353)    
