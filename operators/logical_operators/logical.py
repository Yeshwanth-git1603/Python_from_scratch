#logical operators

#AND,OR,NOT

x=10
y=5
z=6
if x>y and x>z:
    print("x is max")
elif y>z:
    print("y is max")
else:
    print("z is max")
    


# checking the marks for a person whether he is passed or failed with logical operator    
maths=int(input("enter the marks for maths"))
physics=int(input("enter the marks for physics"))
science=int(input("enter the science marks"))
if maths < 35 or physics < 35 or science < 35:
    print("failed")
else:
    print("passed")
    total=maths+physics+science
    print("the total is:",total)
    avg=total/3
    print("the average is:",avg)
