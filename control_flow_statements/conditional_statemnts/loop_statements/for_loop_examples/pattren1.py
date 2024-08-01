#printing the patterns using while loop
# pattern 1
## 1
## 1 2
##1 2 3
##1 2 3 4
##1 2 3 4 5

for x in range(1,5+1):
    for y in range(1,x+1):
        print(y,end=" ")
    print()
