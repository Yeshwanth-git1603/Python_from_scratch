#printing the multiplication table for a given number using for loop
n=int(input("enter the number:"))
print(f"the multiplication table for {n} is:")
for x in range(1,10+1):
    print(f"{n} * {x} = {n*x}")
