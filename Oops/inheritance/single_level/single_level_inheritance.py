#single inheritance

class animal:
    def __init__(self,name,span,existence):
        self.name=name
        self.span=span
        self.existence=existence
        print("the name of the animal is:",self.name)
        print("the life span of the animal is:",self.span)
        print("the existence of the animal is:",self.existence)
        print()
        
class mamal1(animal):
    def __init__(self,name,span,existence,color,a_type):
        super().__init__(name,span,existence)
        self.color=color
        self.a_type=a_type
        print(f"the color of the {self.name} is:",self.color)
        print(f"the type of the {self.name} is:",self.a_type)
        print()
        
        
m=mamal1("whale","100 years","Yes","Blue","killer_type")
