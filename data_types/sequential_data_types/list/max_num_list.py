#max element of a list

def max_list(list1):
    max1=list1[0]
    for x in list1:
        if x>max1:
            max1=x
    else:
        return max1
    
list1=[1,2,3,4,55]
print("the max element in the list is:",max_list(list1))
