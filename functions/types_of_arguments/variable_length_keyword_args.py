# variable length keyword arguments

def var(**args):
    for x in args.keys():
        print(args)
        break
        
var(name="yeshwanth",age=23)
var(name="sunny",age=23)


