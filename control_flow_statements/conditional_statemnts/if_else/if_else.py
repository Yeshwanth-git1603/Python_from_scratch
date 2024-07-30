control fow statements are divided into 3 types
#1:conditional statements
#2:loop statements
#3:un conditional statements

#1:conditional statements
#if
#if else
#elif
#nested if

#if else
#if statemnt used to compare the given condition whether it is true or false
#else statement executes when the if fails
# program for simple calculator

option=input("enter the option")
if option=="add":
    x=int(input("enter x value:"))
    y=int(input("enter y value:"))
    add=x+y
    print(add)
elif option=="sub":
    x=int(input("enter x value:"))
    y=int(input("enter y value:"))
    sub=x-y
    print(sub)
elif option=="mul":
    x=int(input("enter x value:"))
    y=int(input("enter y value:"))
    mul=x*y
    print(mul)
elif option=="div":
    x=int(input("enter x value:"))
    y=int(input("enter y value:"))
    div=x/y
    print(div)
elif option=="rem":
    x=int(input("enter x value:"))
    y=int(input("enter y value:"))
    rem=x%y
    print(rem)
else:
    print("invalid option")
    
