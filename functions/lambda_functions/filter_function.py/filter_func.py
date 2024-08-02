#filter function
#filters the given list based on condition
l1=[1,2,3,4,5,6,7,8,9,10]
x=list(filter(lambda x:True if x%2==0 else False,l1))
print(x)

