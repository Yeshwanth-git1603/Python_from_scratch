# Input number
number = 153

# Store the original number for comparison
original_number = number

# Calculate the number of digits
num_digits = 0
temp_number = number
while temp_number > 0:
    num_digits += 1
    temp_number //= 10

# Compute the Armstrong sum
armstrong_sum = 0
temp_number = number
while temp_number > 0:
    digit = temp_number % 10
    armstrong_sum += digit ** num_digits
    temp_number //= 10

# Check if the original number is equal to the Armstrong sum
if original_number == armstrong_sum:
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")

