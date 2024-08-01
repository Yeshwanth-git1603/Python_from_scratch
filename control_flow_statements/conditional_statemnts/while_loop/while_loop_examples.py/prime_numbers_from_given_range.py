#printing the prime numbers with in the limit
# Define the range
start = 10
end = 50

# Print prime numbers in the given range
print(f"Prime numbers between {start} and {end} are:")

# Initialize the current number to start of the range
num = start

while num <= end:
    # Skip numbers less than or equal to 1
    if num > 1:
        # Initialize divisor
        divisor = 2
        is_prime = True
        
        while divisor * divisor <= num:
            if num % divisor == 0:
                is_prime = False
                break
            divisor += 1
        
        # Print the number if it is prime
        if is_prime:
            print(num)
    
    # Move to the next number
    num += 1

    
    
    
