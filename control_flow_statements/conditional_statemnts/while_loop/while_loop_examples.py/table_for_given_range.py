# table for given range using while loop
i=1
n=5
while i<=n:
    print(f"the table for the given num is:{i}")
    multiplier=1
    while multiplier<=10:
        print(f"{i} * {multiplier} = {i * multiplier}")
        multiplier+=1
        print()
    i+=1
    
