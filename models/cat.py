class Cat:
    def __init__(self, name: str, breed: str, weight_kg:str, id=None):
        self.id = id              
        self.name = name          
        self.breed = breed        
        self.weight_kg = weight_kg 

    def __repr__(self):
        return f"<Kucing: {self.name} ({self.breed})>"