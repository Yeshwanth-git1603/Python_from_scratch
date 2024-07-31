# finding the maximumof three numbers

x=int(input("enter x value:"))
y=int(input("enter y value:"))
z=int(input("enter z value:"))

if x>y and x>z:
    print("x is max:",x)
elif y>z:
    print("y is max:",y)
else:
    print("z is max:",z)
