class anime1:
    def __init__(self,name,story):
        self.name=name
        self.story=story
        print("the name of the game is:",self.name)
        print("the story of the game is:",self.story)
        
class movie(anime1):
    def __init__(self,name,story,budget):
        super().__init__(name,story)
        self.budget=budget
        print("the budget of the movie is: ",self.budget)
        
class anime(movie):
    def __init__(self,name,story,budget,studio):
        super().__init__(name,story,budget)
        movie.__init__(self,name,story,budget)
        self.studio=studio
        print("the studio of the anime is:",self.studio)
        
a=anime("demonslayer","demonslaying","300mil","ufotable")
        
