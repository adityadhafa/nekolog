from database.db import get_connection

class Expenses:
    def __init__(self, amount: int, category: str, date: str, description: str, cat_id: int, id=None):
        self.id = id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description
        self.cat_id = cat_id
    
    @staticmethod
    def create_table():
        conn = get_connection()
        cursor = conn.cursor()
        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount INTEGER NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT NOT NULL,
            cat_id INTEGER NOT NULL,
            FOREIGN KEY (cat_id) REFERENCES cats(id)
        )
        """
        
        cursor.execute(create_table_query)
        
        conn.commit()
        conn.close()
    