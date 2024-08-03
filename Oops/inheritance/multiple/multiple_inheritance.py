#multiple inheritance
class person:
    def __init__(self,name,age,phno):
        self.name=name
        self.age=age
        self.phno=phno
        print("the name of the person is:",self.name)
        print("the age of the person is:",self.age)
        print("the phno of the person is:",self.phno)
        
class neighbour:
    def __init__(self,apno):
        self.apno=apno
        print("the apartment number of the neighbour is:",self.apno)
        
class tenent(person,neighbour):
    def __init__(self,name,age,phno,apno,rent):
        super().__init__(name,age,phno)
        neighbour.__init__(self,apno)
        self.rent=rent
        print("the rent of the tenet is:",self.rent)
        
t=tenent("yeshwanth","23","6305464772","12345","20k")
