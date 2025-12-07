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
        
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        
        the_query = "SELECT * FROM cats"
        cursor.execute(the_query)
        
        results = cursor.fetchall()
        
        cats =[]
        
        for row in results:
            cat_id = row[0]
            name = row[1]
            breed = row[2]
            weight_kg = row[3]

            new_cat = Cat(name, breed, weight_kg, id=cat_id)
            
            cats.append(new_cat)
            
        conn.close()
        
        return cats

    def delete(self):
        conn = get_connection()
        cursor = conn.cursor()
        
        del_query = """
        DELETE FROM cats WHERE id = ?
        """
        
        cursor.execute(del_query, (self.id, ))
        
        self.id = None # cause it's been deleted

        conn.commit()
        conn.close()
        
    def update(self, name:str, breed:str, weight_kg:float):
        conn = get_connection()
        
        cursor = conn.cursor()
        
        update_query = """
        UPDATE cats
        SET name = ?, breed = ?, weight_kg = ?
        WHERE id = ?
        """
        
        data = (name, breed, weight_kg, self.id) 
        
        cursor.execute(update_query, data)
        
        conn.commit()
        conn.close()
        
        self.name = name
        self.breed = breed
        self.weight_kg = weight_kg
        
    @staticmethod
    def search_cat(name: str):
        conn = get_connection()
        cursor = conn.cursor()
        
        query = """
        SELECT id, name FROM cats WHERE name LIKE ?
        """
        
        data = (f"%{name}%")
        
        cursor.execute(query, (data, ))
        
        res = cursor.fetchall()
        
        conn.close()
        
        return res