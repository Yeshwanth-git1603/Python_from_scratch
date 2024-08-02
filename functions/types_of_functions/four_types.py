#area of rectangle using functions
#there are four types of functions

#without argument without return type

def area_of_rectangle():
    length=int(input("enter the length"))
    breadth=int(input("enter the breadth"))
    area=length*breadth
    print("the area of the rectangle is:",area)
    
area_of_rectangle()

#with argument without return type

def area_of_rectangle(length,breadth):
    area=length*breadth
    print("the area of the rectangle is:",area)
    
area_of_rectangle(2,3)

#without argument with return type

def area_of_rectangle():
    length=int(input("enter the length"))
    breadth=int(input("enter the breadth"))
    area=length*breadth
    return area
    
result=area_of_rectangle()
print("the area of the rectangle is:",result)

#with argument with return type


def area_of_rectangle(length,breadth):
    area=length*breadth
    return area
    
res=area_of_rectangle(4,5)
print("the area of the rectangle is:",res)



