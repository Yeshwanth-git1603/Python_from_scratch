# formating the strings
# we can format the strings in two ways
#syntax for method one
#print(f"{a} {b} {a+b}")
#syntax for method two
#print("{} {} {}".format{x,y,x+y})


x=10
y=2
#method one
print(f"the sum of {x} and {y} is {x+y}")
print(f"the prod of {x} and {y} is {x*y}")
print(f"the diff of {x} and {y} is {x-y}")
print(f"the div of {x} and {y} is {x/y}")
print(f"the div of {x} and {y} is {x//y}")
print(f"the rem of {x} and {y} is {x+y}")
#method two
print("the sum of {} and {} is {}".format(x,y,x+y))
print("the diff of {} and {} is {}".format(x,y,x-y))
print("the prod of {} and {} is {}".format(x,y,x*y))
print("the div of {} and {} is {}".format(x,y,x/y))
print("the div of {} and {} is {}".format(x,y,x//y))
