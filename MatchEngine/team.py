class Team: 
    def __init__(self, name: str, strength: int): 
        if strength < 0: 
            raise ValueError("Strength cannot be negative") 

        self.name = name 
        self.strength = strength 
        
    def __str__(self):
        return self.name