#file handling
f=open("super_cars.txt","w")
f.write("1.koenigesgg CC850,2.Pagani Zonda,3.Koenigessg Jesko,4.Ferrari SF90,5.Buggati chiron")
f.writelines=["6.lamborghini aventador svj"]
f.close()

f=open("super_cars.txt","r")
read=f.read()
print(read)

with open("super_cars.txt","a") as f:
    f.write("6.lamborghini aventador svj 7.Aston martin db12 ,8.porsche 911 Gt3rs")
    f.close()
    
f=open("super_cars.txt","r")
print(f.read())

print(f.readline())
print(f.readlines(0))

f=open("sample.txt","rb")
print(f.read())

with open("koenigsegg.txt","w") as file:
    file.write(" koenigsegg cars: CC850 , jesko , chimera , regera , agera ,agera rs , one")
    file.close
    
with open("koenigsegg.txt","r") as file:
    print(file.read())





