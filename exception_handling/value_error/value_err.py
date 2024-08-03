# value error handling

try:
    a="str"
    b=1
    print(a+b)
except Exception as e:
    print("enter the right value")
else:
    print("successful")
finally:
    print('finally executes no matter what')
