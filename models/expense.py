from database.db import get_connection

class Expense:
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
    
    def save(self):
        #inserting
        conn = get_connection()
        cursor = conn.cursor()
        
        save_query = """
        INSERT INTO expenses (amount, category, date, description, cat_id) VALUES (?, ?, ?, ?, ?)
        """
        
        data = (self.amount, self.category, self.date, self.description, self.cat_id)
        cursor.execute(save_query, data)
        
        # updating id 
        self.id = cursor.lastrowid
        
        conn.commit()
        conn.close()
        
    @staticmethod
    def get_by_cat_id(cat_id: int):
        conn = get_connection()
        cursor = conn.cursor()
        
        query = """
        SELECT * FROM expenses WHERE cat_id = ?
        """
        
        cursor.execute(query, (cat_id,))
        
        result = cursor.fetchall()
        
        expenses = []
        
        for row in result:
            #from sql database, change it all into object
            new_expense = Expense(
                amount=row[1],
                category=row[2],
                date=row[3],
                description=row[4],
                cat_id=row[5],
                id=row[0]
            )
            
            expenses.append(new_expense)
            
        conn.close()
        
        return expenses
    
    @staticmethod
    def get_total_by_cat_id(cat_id: int):
        conn = get_connection()
        cursor = conn.cursor()
        
        query = """
        SELECT SUM(amount) FROM expenses WHERE cat_id = ?
        """
        
        cursor.execute(query, (cat_id,))
        
        result = cursor.fetchone()
        
        conn.close()
        
        if result[0]:
            return result[0]
        else:
            return 0