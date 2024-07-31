#printing the student result using three subject marks
student_name=input("enter the name of the student:")
nano_tech=int(input("enter the nano_tech marks:"))
bio_tech=int(input("enter bio_tech marks:"))
geo_tech=int(input("enter geo_tech marks:"))

if nano_tech < 35 or bio_tech < 35 or geo_tech < 35:
    print("student got failed")
else:
    print("student passed:")
    total=(nano_tech+bio_tech+geo_tech)
    print(f"{student_name} total marks is:",total)
    average=total/3
    print(f"{student_name} average is:",average)
if average>=80:
    print(f"{student_name} passesd in first class:",total)
elif average>60:
    print(f"{student_name} passesd in second class:",total)
elif average<50:
    print(f"{student_name} passesd in third class:",total)
else:
    print("enter the valid marks")
