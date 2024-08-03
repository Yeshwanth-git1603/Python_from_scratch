#using map fuction 
def map_fun(n):
    return n*n

for x in range(10+1):
    res=map_fun(x)
    print(res,end=" ")
    
l1=[10,20,30,40,50]
#lambda map function

x=list(map(lambda x:x*x,l1))
print(x)
