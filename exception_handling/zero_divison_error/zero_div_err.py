#exception handling

try:
    a=10
    b=3
    print(a/b)
except Exception as e:
    print("divison by zero not possible")
else:
    print("divison successful")
finally:
    print('executes no matter what')
    
    
#exception handling


