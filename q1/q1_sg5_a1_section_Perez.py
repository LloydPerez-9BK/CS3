class hero:
    def __init__(self,name,hp,):
        self.name = name
        self.hp = hp
    def dmg(self,amount):
        self.hp -=  amount

arthur = hero("Arthur",100)
morgan = hero("Morgan",100)

arthur.dmg(10)

print(f"{arthur.name}'s Hp:{arthur.hp}")
print(f"{morgan.name}'s Hp:{morgan.hp}")
        
    
