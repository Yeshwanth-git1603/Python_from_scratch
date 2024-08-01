# Define the range
start = 1
end = 10

# Print prime numbers in the given range
print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if num > 1:  # Prime numbers are greater than 1
        is_prime = True  # Assume num is prime
        
        # Check divisibility from 2 up to the square root of num
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        # Print the number if it is prime
        if is_prime:
            print(num)

