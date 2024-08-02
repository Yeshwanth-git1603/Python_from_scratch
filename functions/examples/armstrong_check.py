def is_armstrong_number(number):
    # Convert number to string to easily iterate over digits
    num_str = str(number)
    num_digits = len(num_str)
    
    # Compute the sum of digits each raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Compare the computed sum with the original number
    return sum_of_powers == number

# Example usage
num = int(input("Enter a number to check if it's an Armstrong number: "))
if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
