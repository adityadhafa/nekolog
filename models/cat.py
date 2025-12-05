from database.db import get_connection
class Cat:
    def __init__(self, name: str, breed: str, weight_kg:float, id=None):
        self.id = id              
        self.name = name          
        self.breed = breed        
        self.weight_kg = weight_kg 

    def __repr__(self):
        return f"<Kucing: {self.name} ({self.breed})>"

    @staticmethod
    def create_table(): # doesn't need self bcs it's a staticmethod
        conn = get_connection()
        cursor = conn.cursor()
        
        my_query = """
        CREATE TABLE IF NOT EXISTS cats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            breed TEXT,
            weight_kg REAL
        )
        """
        
        cursor.execute(my_query)
        conn.commit()
        conn.close()
    
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        
        my_query= """
        INSERT INTO cats (name, breed, weight_kg) VALUES (?, ?, ?)
        """
        
        data_tuple = (self.name, self.breed, self.weight_kg)
        
        cursor.execute(my_query, data_tuple)
        
        self.id = cursor.lastrowid
        
        conn.commit()  
        conn.close()