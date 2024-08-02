#variable length arguments

def var_arg(*args):
    sum1=0
    print(len(args))
    print(type(args))
    for x in args:
        sum1=sum1+x
    print(sum1)
        
var_arg(1,2,3,4,5)

