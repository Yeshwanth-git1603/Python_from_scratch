#lambda function for even or odd check

x=(lambda x:True if x%2==0 else False)
print(x(3))

#lambda for prime check

y=(lambda x:"not prime" if x%2==0 else "prime")
print(y(98))
