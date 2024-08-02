#printing the student marks using functions

def student(maths,physics,chemistry):
    if maths < 35 or physics < 35 or chemistry < 35:
        print("student failed")
    else:
        print("student passed")
        total=maths+physics+chemistry
        print("the total marks of the student is:",total)
        avg=total/3
        print("the avg of the student is:",avg)
        if avg > 60:
            print("first class")
        elif avg >= 50:
            print("second class")
        else:
            print("third class")
            
student(80,67,87)
