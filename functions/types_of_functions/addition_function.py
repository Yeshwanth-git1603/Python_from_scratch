#addition of two numbers using function and its types

#without argument without return type
def add():
    x=int(input("enter x value:"))
    y=int(input("enter y value:"))
    z=x+y
    print(f"the sum of {x} and {y} is :{z}")
    
add()

#with argument without return type

def add(x,y):
    z=x+y
    print(f"the sum of {x} and {y} is :{z}")
    
add(2,3)

#without argument with return type

def add():
    x=int(input("enter a value:"))
    y=int(input("enter b value:"))
    z=x+y
    return z
    
    
res=add()
print("the sum of x and y is:",res)

#with argument with return type

def add(x,y):
    z=x+y
    return z    
result=add(2,3)
print(f"the sum of x and y is:",result)






